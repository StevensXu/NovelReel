import os
from pathlib import Path
import requests
import yaml
from urllib.parse import urlparse

from volcenginesdkarkruntime import Ark
from volcenginesdkarkruntime.types.images.images import SequentialImageGenerationOptions


DEFAULT_SEEDREAM_CONFIG = {
    "base_url": "https://ark.cn-beijing.volces.com/api/v3",
    "api_key": "",
    "model": "doubao-seedream-5-0-260128",
    "multi_view_size": "2K",
    "sizes": {
        "16:9": "2848x1600",
        "9:16": "1600x2848",
        "1:1": "2048x2048",
    },
}

DEFAULT_IMAGE_CONFIG = {
    "provider": "seedream",
    "seedream": DEFAULT_SEEDREAM_CONFIG,
}

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CONFIG_PATH = PROJECT_ROOT / "config.yaml"


def _resolve_config_path(config_path):
    if not config_path:
        return DEFAULT_CONFIG_PATH
    path = Path(config_path)
    if path.is_absolute() or path.exists():
        return path
    return PROJECT_ROOT / path


def _deep_merge(base, override):
    merged = dict(base)
    for key, value in (override or {}).items():
        if isinstance(value, dict) and isinstance(merged.get(key), dict):
            merged[key] = _deep_merge(merged[key], value)
        elif value is not None:
            merged[key] = value
    return merged


def _load_image_config(config_path):
    config_path = _resolve_config_path(config_path)
    if not config_path.exists():
        return DEFAULT_IMAGE_CONFIG
    with open(config_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f) or {}
    return _deep_merge(DEFAULT_IMAGE_CONFIG, config.get("image", {}))


def _legacy_seedream_sizes():
    return {
        "16:9": "2848x1600",
        "9:16": "1600x2848",
        "1:1": "2048x2048",
    }


class ImageGenerator(object):
    """图像生成模型，使用 seedream (Volcengine Ark API)

    功能：文生图，用于生成角色图和环境图
    """

    def __init__(self, output_dir="output", provider=None, config_path=None):
        """
        Args:
            output_dir: 输出目录
            provider: 生图引擎，目前仅支持 "seedream"；不传时读取项目根目录的 config.yaml
            config_path: 配置文件路径
        """
        self.output_dir = output_dir
        image_config = _load_image_config(config_path)
        self.provider = provider or image_config.get("provider", "seedream")
        if self.provider != "seedream":
            raise ValueError(f"Unsupported image provider: {self.provider}")

        seedream_config = image_config.get("seedream", {})
        self.seedream_model = seedream_config.get("model")
        self.seedream_sizes = seedream_config.get("sizes") or _legacy_seedream_sizes()
        self.seedream_multi_view_size = seedream_config.get("multi_view_size", "2K")
        api_key = seedream_config.get("api_key", "")
        if not api_key:
            raise ValueError("Missing image.seedream.api_key in config.yaml")

        self.ark_client = Ark(
            base_url=seedream_config.get("base_url"),
            api_key=api_key,
        )

    def _text_to_image(self, prompt, save_path, aspect_ratio="16:9", force=False):
        """文生图，根据 provider 选择不同的生图引擎

        Args:
            prompt: 生图 prompt
            save_path: 图片保存路径
            aspect_ratio: 宽高比，如 "9:16", "16:9", "1:1"
            force: 是否强制覆盖已有图片

        Returns:
            tuple: (保存的图片路径, image_url)，失败返回 ("", "")
                   image_url 为 seedream 返回的远程 URL
        """
        if os.path.exists(save_path) and not force:
            print(f"  图片已存在，跳过: {save_path}")
            return save_path, ""

        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        return self._text_to_image_seedream(prompt, save_path, aspect_ratio)

    def _text_to_image_seedream(self, prompt, save_path, aspect_ratio="16:9"):
        """调用 Volcengine Ark API (seedream) 文生图"""
        size = self.seedream_sizes.get(aspect_ratio, self.seedream_sizes.get("16:9", "2848x1600"))

        try:
            response = self.ark_client.images.generate(
                model=self.seedream_model,
                prompt=prompt,
                sequential_image_generation="disabled",
                response_format="url",
                size=size,
                stream=False,
                watermark=False,
            )

            image_url = response.data[0].url
            # 下载图片并保存
            img_resp = requests.get(image_url, timeout=120)
            img_resp.raise_for_status()
            with open(save_path, "wb") as f:
                f.write(img_resp.content)
            print(f"  图片已保存: {save_path}")
            return save_path, image_url
        except Exception as e:
            print(f"  生图失败: {e}")
            return "", ""

    def _image_to_image_seedream(self, prompt, image_urls, save_path, aspect_ratio="16:9", force=False):
        """用 seedream 参考图生成新图。

        Ark 的 image 参数需要可访问 URL；如果没有 URL，调用方应回退到文生图。
        """
        if os.path.exists(save_path) and not force:
            print(f"  图片已存在，跳过: {save_path}")
            return save_path, ""

        clean_urls = [
            url for url in (image_urls or [])
            if isinstance(url, str) and urlparse(url).scheme in {"http", "https"}
        ]
        if not clean_urls:
            return self._text_to_image(prompt, save_path, aspect_ratio=aspect_ratio, force=force)

        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        size = self.seedream_sizes.get(aspect_ratio, self.seedream_sizes.get("16:9", "2848x1600"))

        try:
            response = self.ark_client.images.generate(
                model=self.seedream_model,
                prompt=prompt,
                image=clean_urls,
                sequential_image_generation="disabled",
                response_format="url",
                size=size,
                stream=False,
                watermark=False,
            )

            image_url = response.data[0].url
            img_resp = requests.get(image_url, timeout=120)
            img_resp.raise_for_status()
            with open(save_path, "wb") as f:
                f.write(img_resp.content)
            print(f"  图片已保存: {save_path}")
            return save_path, image_url
        except Exception as e:
            print(f"  参考图生图失败: {e}")
            return "", ""

    def generate_character_image(self, character_description, save_path=None, force=False, reference_image_urls=None):
        """根据角色描述生成全身形象图（白色背景）

        Returns:
            tuple: (图片路径, image_url)
        """
        if save_path is None:
            os.makedirs(os.path.join(self.output_dir, "characters"), exist_ok=True)
            save_path = os.path.join(self.output_dir, "characters", "char_auto.png")
        if reference_image_urls:
            return self._image_to_image_seedream(
                character_description,
                reference_image_urls,
                save_path,
                aspect_ratio="16:9",
                force=force,
            )
        return self._text_to_image(character_description, save_path, aspect_ratio="16:9", force=force)

    def generate_reference_image(self, prompt, reference_image_urls, save_path, aspect_ratio="16:9", force=False):
        """根据参考图生成图片；没有可用 URL 时自动回退到文生图。"""
        return self._image_to_image_seedream(
            prompt,
            reference_image_urls,
            save_path,
            aspect_ratio=aspect_ratio,
            force=force,
        )

    def generate_multi_view_environment(self, env_desc, view_count, save_dir, env_id, style="写实"):
        """使用 seedream 多图生成同一环境的多个视角图

        Args:
            env_desc: 环境描述文本
            view_count: 需要生成的视角数量（1-4）
            save_dir: 图片保存目录
            env_id: 环境ID，用于文件命名
            style: 画面风格

        Returns:
            list[dict]: 每个视角的信息 [{"path": ..., "image_url": ..., "view_index": 1}, ...]
        """
        os.makedirs(save_dir, exist_ok=True)
        view_count = max(1, min(4, view_count))

        # 如果只需要1张，走普通单图生成
        if view_count == 1:
            prompt = f"{style}风格，{env_desc}, no people, no characters, cinematic, wide shot, high quality, detailed"
            save_path = os.path.join(save_dir, f"env_{env_id:03d}_v1.png")
            result_path, image_url = self._text_to_image(prompt, save_path, aspect_ratio="16:9")
            return [{"path": result_path or save_path, "image_url": image_url, "view_index": 1}]

        # 多视角：用 seedream 多图生成
        prompt = (
            f"{style}风格，生成{view_count}张同一场景不同视角/机位的图片。"
            f"场景描述：{env_desc}。"
            f"要求：每张图展示该场景的不同拍摄角度（如正面全景、侧面、俯瞰、仰视等），"
            f"保持场景一致但视角不同。no people, no characters, cinematic, high quality, detailed"
        )

        # 检查是否已有缓存
        existing = []
        for i in range(1, view_count + 1):
            p = os.path.join(save_dir, f"env_{env_id:03d}_v{i}.png")
            if os.path.exists(p):
                existing.append({"path": p, "image_url": "", "view_index": i})
        if len(existing) == view_count:
            print(f"  环境 {env_id} 的 {view_count} 张视角图已存在，跳过")
            return existing

        try:
            response = self.ark_client.images.generate(
                model=self.seedream_model,
                prompt=prompt,
                size=self.seedream_multi_view_size,
                sequential_image_generation="auto",
                sequential_image_generation_options=SequentialImageGenerationOptions(
                    max_images=view_count
                ),
                response_format="url",
                watermark=False,
            )

            results = []
            for i, image_data in enumerate(response.data, start=1):
                save_path = os.path.join(save_dir, f"env_{env_id:03d}_v{i}.png")
                img_resp = requests.get(image_data.url, timeout=120)
                img_resp.raise_for_status()
                with open(save_path, "wb") as f:
                    f.write(img_resp.content)
                results.append({
                    "path": save_path,
                    "image_url": image_data.url,
                    "view_index": i,
                })
                print(f"  环境 {env_id} 视角{i} 已保存: {save_path}")

            # 如果返回的图片数少于请求数，补充生成
            while len(results) < view_count:
                idx = len(results) + 1
                fallback_prompt = (
                    f"{style}风格，{env_desc}, 从不同角度拍摄（视角{idx}），"
                    f"no people, no characters, cinematic, high quality, detailed"
                )
                save_path = os.path.join(save_dir, f"env_{env_id:03d}_v{idx}.png")
                result_path, image_url = self._text_to_image(fallback_prompt, save_path, aspect_ratio="16:9")
                results.append({
                    "path": result_path or save_path,
                    "image_url": image_url,
                    "view_index": idx,
                })

            return results
        except Exception as e:
            print(f"  多视角生成失败，回退到逐张生成: {e}")
            results = []
            for i in range(1, view_count + 1):
                fallback_prompt = (
                    f"{style}风格，{env_desc}, 从不同角度拍摄（视角{i}），"
                    f"no people, no characters, cinematic, high quality, detailed"
                )
                save_path = os.path.join(save_dir, f"env_{env_id:03d}_v{i}.png")
                result_path, image_url = self._text_to_image(fallback_prompt, save_path, aspect_ratio="16:9")
                results.append({
                    "path": result_path or save_path,
                    "image_url": image_url,
                    "view_index": i,
                })
            return results

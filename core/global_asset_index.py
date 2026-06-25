import json
import os
import re


def chapter_sort_key(path):
    name = os.path.basename(os.path.normpath(path))
    match = re.match(r"chapter_(\d+)$", name)
    if match:
        return (1, int(match.group(1)), name)
    return (0, 0, name)


class GlobalAssetIndex:
    """Persistent cross-chapter index for characters, props, and environments."""

    def __init__(self, base_output_dir="output"):
        self.base_output_dir = base_output_dir
        self.characters_path = os.path.join(base_output_dir, "global_characters.json")
        self.character_images_path = os.path.join(base_output_dir, "global_character_images.json")
        self.props_path = os.path.join(base_output_dir, "global_props.json")
        self.prop_images_path = os.path.join(base_output_dir, "global_prop_images.json")
        self.environments_path = os.path.join(base_output_dir, "global_environments.json")

    def load_characters(self, fallback_dir=""):
        data = self._load_json(self.characters_path)
        if data:
            return self._normalize_character_data(data)
        return self._migrate_characters(fallback_dir)

    def save_characters_from_chapter(self, chapter_data, chapter_name=""):
        global_data = self.load_characters()
        style = chapter_data.get("style") or global_data.get("style", "写实")
        merged = {self._character_key(char): dict(char) for char in global_data.get("characters", [])}

        for char in chapter_data.get("characters", []):
            if not isinstance(char, dict):
                continue
            item = dict(char)
            item["latest_chapter"] = chapter_name
            chapters = set(merged.get(self._character_key(item), {}).get("chapters", []))
            if chapter_name:
                chapters.add(chapter_name)
            if chapters:
                item["chapters"] = sorted(chapters)
            merged[self._character_key(item)] = item

        result = {
            "style": style,
            "characters": sorted(merged.values(), key=lambda char: int(char.get("id", 10**9))),
        }
        self._save_json(self.characters_path, result)
        return result

    def load_character_images(self, fallback_dir=""):
        data = self._load_json(self.character_images_path)
        if isinstance(data, dict) and data:
            return self._normalize_named_image_index(data)
        return self._migrate_character_images(fallback_dir)

    def save_character_images_from_chapter(self, character_images):
        merged = self.load_character_images()
        for name, info in (character_images or {}).items():
            if isinstance(info, dict):
                merged[name] = dict(info)
            else:
                merged[name] = {"path": info, "image_url": "", "prompt": ""}
        self._save_json(self.character_images_path, merged)
        return merged

    def load_props(self, fallback_dir=""):
        data = self._load_json(self.props_path)
        if data:
            return self._normalize_prop_data(data)
        return self._migrate_props(fallback_dir)

    def save_props_from_chapter(self, chapter_data, chapter_name=""):
        global_data = self.load_props()
        merged = {self._prop_key(prop): dict(prop) for prop in global_data.get("props", [])}

        for prop in chapter_data.get("props", []):
            if not isinstance(prop, dict):
                continue
            item = dict(prop)
            item["latest_chapter"] = chapter_name
            chapters = set(merged.get(self._prop_key(item), {}).get("chapters", []))
            if chapter_name:
                chapters.add(chapter_name)
            if chapters:
                item["chapters"] = sorted(chapters)
            merged[self._prop_key(item)] = item

        result = {
            "props": sorted(merged.values(), key=lambda prop: int(prop.get("id", 10**9))),
        }
        self._save_json(self.props_path, result)
        return result

    def load_prop_images(self, fallback_dir=""):
        data = self._load_json(self.prop_images_path)
        if isinstance(data, dict) and data:
            return self._normalize_named_image_index(data)
        return self._migrate_prop_images(fallback_dir)

    def save_prop_images_from_chapter(self, prop_images):
        merged = self.load_prop_images()
        for name, info in (prop_images or {}).items():
            if isinstance(info, dict):
                merged[name] = dict(info)
            else:
                merged[name] = {"path": info, "image_url": "", "prompt": ""}
        self._save_json(self.prop_images_path, merged)
        return merged

    def load_environments(self, fallback_dir=""):
        data = self._load_json(self.environments_path)
        if isinstance(data, dict) and data:
            return self._environment_match_index(data)
        return self._migrate_environments(fallback_dir)

    def save_environments_from_chapter(self, env_images, chapter_name=""):
        merged = self._load_json(self.environments_path)
        if not isinstance(merged, dict):
            merged = {}
        for env_id, info in (env_images or {}).items():
            if isinstance(info, dict):
                item = dict(info)
            else:
                item = {"path": info, "image_url": "", "environment_description": ""}
            desc = item.get("environment_description", "") or item.get("prompt", "") or str(env_id)
            key = self._environment_key(desc)
            item["latest_chapter"] = chapter_name
            item["latest_chapter_environment_id"] = env_id
            previous_global_id = item.get("previous_environment_id")
            if previous_global_id is not None and item.get("asset_action") in {"reuse", "update"}:
                item.setdefault("global_environment_id", previous_global_id)
            item.setdefault("global_environment_id", len(merged) + 1)
            if key in merged:
                item["global_environment_id"] = merged[key].get("global_environment_id", item["global_environment_id"])
                chapters = set(merged[key].get("chapters", []))
            else:
                chapters = set()
            if chapter_name:
                chapters.add(chapter_name)
            if chapters:
                item["chapters"] = sorted(chapters)
            merged[key] = item
        self._save_json(self.environments_path, merged)
        return merged

    def _migrate_characters(self, fallback_dir=""):
        merged = {"style": "写实", "characters": []}
        seen = {}
        for chapter_dir in self._asset_dirs("characters.json", fallback_dir):
            path = os.path.join(chapter_dir, "characters.json")
            data = self._normalize_character_data(self._load_json(path))
            merged["style"] = data.get("style") or merged["style"]
            chapter_name = os.path.basename(os.path.normpath(chapter_dir))
            for char in data.get("characters", []):
                item = dict(char)
                item["latest_chapter"] = chapter_name
                item["chapters"] = sorted(set(item.get("chapters", []) + [chapter_name]))
                seen[self._character_key(item)] = item
        merged["characters"] = sorted(seen.values(), key=lambda char: int(char.get("id", 10**9)))
        if merged["characters"]:
            self._save_json(self.characters_path, merged)
        return merged

    def _migrate_character_images(self, fallback_dir=""):
        merged = {}
        for chapter_dir in self._asset_dirs("character_images.json", fallback_dir):
            data = self._load_json(os.path.join(chapter_dir, "character_images.json"))
            merged.update(self._normalize_named_image_index(data))
        if merged:
            self._save_json(self.character_images_path, merged)
        return merged

    def _migrate_props(self, fallback_dir=""):
        merged = {"props": []}
        seen = {}
        for chapter_dir in self._asset_dirs("props.json", fallback_dir):
            path = os.path.join(chapter_dir, "props.json")
            data = self._normalize_prop_data(self._load_json(path))
            chapter_name = os.path.basename(os.path.normpath(chapter_dir))
            for prop in data.get("props", []):
                item = dict(prop)
                item["latest_chapter"] = chapter_name
                item["chapters"] = sorted(set(item.get("chapters", []) + [chapter_name]))
                seen[self._prop_key(item)] = item
        merged["props"] = sorted(seen.values(), key=lambda prop: int(prop.get("id", 10**9)))
        if merged["props"]:
            self._save_json(self.props_path, merged)
        return merged

    def _migrate_prop_images(self, fallback_dir=""):
        merged = {}
        for chapter_dir in self._asset_dirs("prop_images.json", fallback_dir):
            data = self._load_json(os.path.join(chapter_dir, "prop_images.json"))
            merged.update(self._normalize_named_image_index(data))
        if merged:
            self._save_json(self.prop_images_path, merged)
        return merged

    def _migrate_environments(self, fallback_dir=""):
        merged = {}
        for chapter_dir in self._asset_dirs("env_images.json", fallback_dir):
            data = self._load_json(os.path.join(chapter_dir, "env_images.json"))
            chapter_name = os.path.basename(os.path.normpath(chapter_dir))
            for env_id, info in self._normalize_environment_index(data).items():
                item = dict(info)
                desc = item.get("environment_description", "") or item.get("prompt", "") or str(env_id)
                key = self._environment_key(desc)
                item["latest_chapter"] = chapter_name
                item["latest_chapter_environment_id"] = env_id
                item["global_environment_id"] = merged.get(key, {}).get("global_environment_id", len(merged) + 1)
                chapters = set(merged.get(key, {}).get("chapters", []))
                chapters.add(chapter_name)
                item["chapters"] = sorted(chapters)
                merged[key] = item
        if merged:
            self._save_json(self.environments_path, merged)
        return self._environment_match_index(merged)

    def _asset_dirs(self, asset_filename, fallback_dir=""):
        dirs = []
        if os.path.isdir(self.base_output_dir):
            for entry in os.listdir(self.base_output_dir):
                candidate = os.path.join(self.base_output_dir, entry)
                if os.path.isdir(candidate) and os.path.exists(os.path.join(candidate, asset_filename)):
                    dirs.append(candidate)
        if fallback_dir and os.path.exists(os.path.join(fallback_dir, asset_filename)):
            dirs.append(fallback_dir)
        return sorted(set(dirs), key=chapter_sort_key)

    def _normalize_character_data(self, data):
        if isinstance(data, list):
            return {"style": "写实", "characters": data}
        if isinstance(data, dict):
            return {"style": data.get("style", "写实"), "characters": data.get("characters", [])}
        return {"style": "写实", "characters": []}

    def _normalize_prop_data(self, data):
        if isinstance(data, list):
            return {"props": data}
        if isinstance(data, dict):
            return {"props": data.get("props", [])}
        return {"props": []}

    def _normalize_named_image_index(self, data):
        if not isinstance(data, dict):
            return {}
        normalized = {}
        for name, info in data.items():
            normalized[name] = dict(info) if isinstance(info, dict) else {"path": info, "image_url": "", "prompt": ""}
        return normalized

    def _environment_match_index(self, data):
        normalized = {}
        for key, info in self._normalize_environment_index(data).items():
            env_id = info.get("global_environment_id", key)
            normalized[str(env_id)] = info
        return normalized

    def _normalize_environment_index(self, data):
        if not isinstance(data, dict):
            return {}
        normalized = {}
        for env_id, info in data.items():
            normalized[str(env_id)] = dict(info) if isinstance(info, dict) else {"path": info, "image_url": "", "environment_description": ""}
        return normalized

    def _character_key(self, char):
        char_id = char.get("id")
        return f"id:{char_id}" if isinstance(char_id, int) else f"name:{char.get('name', '')}"

    def _prop_key(self, prop):
        prop_id = prop.get("id")
        return f"id:{prop_id}" if isinstance(prop_id, int) else f"name:{prop.get('name', '')}"

    def _environment_key(self, description):
        return re.sub(r"\s+", "", str(description).strip())[:120]

    def _load_json(self, path):
        if not path or not os.path.exists(path):
            return None
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def _save_json(self, path, data):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
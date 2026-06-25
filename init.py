from __future__ import annotations

import argparse
import shutil
import subprocess
from pathlib import Path
from typing import Iterable

import cv2
import numpy as np
from tkinter import Tk, filedialog


IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".bmp", ".webp", ".tif", ".tiff"}
VIDEO_EXTS = {".mp4", ".mov", ".avi", ".mkv", ".webm", ".m4v"}


def read_image(path: Path):
    data = np.fromfile(str(path), dtype=np.uint8)
    if data.size == 0:
        return None
    return cv2.imdecode(data, cv2.IMREAD_COLOR)


def write_image(path: Path, image) -> bool:
    ext = path.suffix or ".jpg"
    ok, encoded = cv2.imencode(ext, image)
    if not ok:
        return False
    encoded.tofile(str(path))
    return True


def choose_files() -> list[Path]:
    root = Tk()
    root.withdraw()
    root.update()

    filetypes = [
        ("Images and videos", "*.jpg *.jpeg *.png *.bmp *.webp *.tif *.tiff *.mp4 *.mov *.avi *.mkv *.webm *.m4v"),
        ("Images", "*.jpg *.jpeg *.png *.bmp *.webp *.tif *.tiff"),
        ("Videos", "*.mp4 *.mov *.avi *.mkv *.webm *.m4v"),
        ("All files", "*.*"),
    ]
    selected = filedialog.askopenfilenames(title="Select images/videos to crop", filetypes=filetypes)
    root.destroy()
    return [Path(item) for item in selected]


def first_video_frame(path: Path):
    cap = cv2.VideoCapture(str(path))
    ok, frame = cap.read()
    cap.release()
    return frame if ok else None


def preview_frame(path: Path):
    suffix = path.suffix.lower()
    if suffix in IMAGE_EXTS:
        return read_image(path)
    if suffix in VIDEO_EXTS:
        return first_video_frame(path)
    return None


def select_crop_box(frame) -> tuple[int, int, int, int]:
    cv2.namedWindow("Select crop area", cv2.WINDOW_NORMAL)
    x, y, w, h = cv2.selectROI(
        "Select crop area",
        frame,
        showCrosshair=True,
        fromCenter=False,
    )
    cv2.destroyWindow("Select crop area")
    return int(x), int(y), int(w), int(h)


def clamp_box(box: tuple[int, int, int, int], width: int, height: int):
    x, y, w, h = box
    left = max(0, min(x, width))
    top = max(0, min(y, height))
    right = max(left, min(x + w, width))
    bottom = max(top, min(y + h, height))

    out_width = right - left
    out_height = bottom - top
    if out_width <= 0 or out_height <= 0:
        return None

    # H.264 with yuv420p needs even output dimensions.
    if out_width > 1 and out_width % 2:
        right -= 1
    if out_height > 1 and out_height % 2:
        bottom -= 1

    if right <= left or bottom <= top:
        return None
    return left, top, right, bottom


def find_ffmpeg() -> str | None:
    ffmpeg = shutil.which("ffmpeg")
    if ffmpeg:
        return ffmpeg

    try:
        import imageio_ffmpeg
    except ImportError:
        return None

    return imageio_ffmpeg.get_ffmpeg_exe()


def crop_image(path: Path, output_dir: Path, box: tuple[int, int, int, int]) -> bool:
    image = read_image(path)
    if image is None:
        print(f"[skip] Cannot read image: {path}")
        return False

    height, width = image.shape[:2]
    clamped = clamp_box(box, width, height)
    if clamped is None:
        print(f"[skip] Crop box is outside image: {path}")
        return False

    left, top, right, bottom = clamped
    cropped = image[top:bottom, left:right]
    out_path = output_dir / f"{path.stem}_cropped{path.suffix}"
    if write_image(out_path, cropped):
        print(f"[done] Image: {out_path}")
        return True

    print(f"[fail] Cannot write image: {out_path}")
    return False


def crop_video(path: Path, output_dir: Path, box: tuple[int, int, int, int], ffmpeg: str) -> bool:
    frame = first_video_frame(path)
    if frame is None:
        print(f"[skip] Cannot read first video frame: {path}")
        return False

    height, width = frame.shape[:2]
    clamped = clamp_box(box, width, height)
    if clamped is None:
        print(f"[skip] Crop box is outside video: {path}")
        return False

    left, top, right, bottom = clamped
    out_width = right - left
    out_height = bottom - top
    out_path = output_dir / f"{path.stem}_cropped.mp4"
    crop_filter = f"crop={out_width}:{out_height}:{left}:{top}"

    command = [
        ffmpeg,
        "-y",
        "-hide_banner",
        "-i",
        str(path),
        "-map",
        "0:v:0",
        "-map",
        "0:a?",
        "-vf",
        crop_filter,
        "-c:v",
        "libx264",
        "-crf",
        "18",
        "-preset",
        "medium",
        "-pix_fmt",
        "yuv420p",
        "-c:a",
        "aac",
        "-b:a",
        "192k",
        "-movflags",
        "+faststart",
        str(out_path),
    ]

    print(f"[work] Video with audio: {path.name}")
    result = subprocess.run(command, text=True, capture_output=True, encoding="utf-8", errors="replace")
    if result.returncode == 0:
        print(f"[done] Video: {out_path}")
        return True

    print(f"[fail] ffmpeg failed: {path}")
    if result.stderr:
        print(result.stderr[-2000:])
    return False


def iter_supported(files: Iterable[Path]) -> Iterable[Path]:
    supported = IMAGE_EXTS | VIDEO_EXTS
    for path in files:
        if path.suffix.lower() in supported:
            yield path
        else:
            print(f"[skip] Unsupported file type: {path}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Select one crop box and batch-crop images/videos.")
    parser.add_argument("files", nargs="*", type=Path, help="Input images/videos. If empty, a file picker opens.")
    parser.add_argument("-o", "--output", type=Path, default=Path("cropped_output"), help="Output directory.")
    args = parser.parse_args()

    files = args.files or choose_files()
    files = list(iter_supported(files))
    if not files:
        print("No supported images or videos selected.")
        return 1

    sample = preview_frame(files[0])
    if sample is None:
        print(f"Cannot read first file for preview: {files[0]}")
        return 1

    print("Drag a crop box in the popup window, then press Enter or Space. Press C to cancel.")
    box = select_crop_box(sample)
    if box[2] <= 0 or box[3] <= 0:
        print("Canceled, or no valid crop area selected.")
        return 1

    has_video = any(path.suffix.lower() in VIDEO_EXTS for path in files)
    ffmpeg = find_ffmpeg() if has_video else None
    if has_video and not ffmpeg:
        print("ffmpeg is required for video audio preservation.")
        print("Install it with: pip install imageio-ffmpeg")
        return 1

    output_dir = args.output
    output_dir.mkdir(parents=True, exist_ok=True)

    success = 0
    for path in files:
        suffix = path.suffix.lower()
        if suffix in IMAGE_EXTS:
            success += int(crop_image(path, output_dir, box))
        elif suffix in VIDEO_EXTS and ffmpeg:
            success += int(crop_video(path, output_dir, box, ffmpeg))

    print(f"Finished: {success}/{len(files)} files. Output: {output_dir.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

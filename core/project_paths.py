from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent


def resolve_project_path(path):
    resolved = Path(path or ".")
    if resolved.is_absolute():
        return str(resolved)
    return str(PROJECT_ROOT / resolved)


def resolve_chapter_output_dir(output_dir, chapter_name):
    output_dir = str(output_dir)
    if not chapter_name:
        return output_dir
    safe_name = str(chapter_name).strip().strip("/\\")
    if not safe_name:
        return output_dir
    if Path(output_dir).resolve().name == safe_name:
        return output_dir
    return str(Path(output_dir) / safe_name)


def resolve_previous_asset_dir(previous_output_dir, asset_filename):
    """Resolve the directory that contains a previous chapter asset file."""
    if not previous_output_dir:
        return ""

    previous_output_dir = Path(str(previous_output_dir).strip())
    if not str(previous_output_dir):
        return ""

    direct_path = previous_output_dir / asset_filename
    if direct_path.exists():
        return str(previous_output_dir)

    if not previous_output_dir.is_dir():
        return str(previous_output_dir)

    candidates = [
        candidate
        for candidate in previous_output_dir.iterdir()
        if candidate.is_dir() and (candidate / asset_filename).exists()
    ]
    if not candidates:
        return str(previous_output_dir)

    def chapter_sort_key(path):
        name = path.name
        if name.startswith("chapter_") and name.replace("chapter_", "", 1).isdigit():
            return (1, int(name.replace("chapter_", "", 1)), name)
        return (0, 0, name)

    return str(sorted(candidates, key=chapter_sort_key)[-1])
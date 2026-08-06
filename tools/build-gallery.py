#!/usr/bin/env python3
"""Build a small JSON index for OhMyStyle Style Packages."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import yaml

from safe_yaml import safe_load


IMAGE_SUFFIXES = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".tif", ".tiff"}


def discover_packages(path: Path) -> list[Path]:
    path = path.resolve()
    if (path / "styles").is_dir():
        path = path / "styles"
    return sorted(child for child in path.iterdir() if (child / "style.yaml").is_file())


def count_images(path: Path) -> int:
    if not path.exists():
        return 0
    return sum(1 for item in path.rglob("*") if item.is_file() and item.suffix.lower() in IMAGE_SUFFIXES)


def load_package(path: Path, repo_root: Path) -> dict[str, Any]:
    with (path / "style.yaml").open(encoding="utf-8") as handle:
        style = safe_load(handle)
    identity = style.get("visual_identity", {})
    return {
        "id": style["id"],
        "name": style["name"],
        "version": style["version"],
        "type": style["type"],
        "summary": style["summary"],
        "mood": identity.get("mood", []),
        "dominant_colors": identity.get("color", {}).get("dominant_colors", []),
        "references": count_images(path / "references"),
        "accepted_examples": count_images(path / "examples/successful"),
        "rejected_examples": count_images(path / "examples/rejected"),
        "path": path.relative_to(repo_root).as_posix() if path.is_relative_to(repo_root) else path.name,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a Style Package gallery index.")
    parser.add_argument("--source", type=Path, default=Path("styles"))
    parser.add_argument("--output", type=Path, default=Path("docs/style-packages.json"))
    args = parser.parse_args()

    repo_root = Path.cwd().resolve()
    packages = [load_package(path, repo_root) for path in discover_packages(args.source)]
    payload = {
        "schema": "https://github.com/ZhouYinLong-lab/OhMyStyle/schema/style.schema.json",
        "generated_by": "tools/build-gallery.py",
        "packages": packages,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"WROTE: {args.output} ({len(packages)} package(s))")


if __name__ == "__main__":
    main()

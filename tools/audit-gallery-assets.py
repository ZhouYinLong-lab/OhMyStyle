#!/usr/bin/env python3
"""Audit representative images used by structured style packages.

The audit is intentionally provider-neutral and uses only Pillow.  It checks
the package-local representative image, its native aspect ratio, basic image
integrity, and the README link that exposes it to users.  It never rewrites
images or silently substitutes a missing asset.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from PIL import Image, ImageStat


ASPECT_RATIO = 16 / 9
ASPECT_TOLERANCE = 0.02
BLANK_RATIO = 0.97
MIN_DIMENSION = 320


def discover_packages(root: Path) -> list[Path]:
    root = root.resolve()
    if not root.is_dir():
        raise SystemExit(f"Path does not exist: {root}")
    packages = sorted(path.parent for path in root.rglob("package.yaml"))
    if not packages:
        raise SystemExit(f"No package.yaml found under: {root}")
    return packages


def read_readme_status(package: Path, image_name: str) -> tuple[bool, str]:
    readme = package / "README.md"
    if not readme.is_file():
        return False, "README.md is missing"
    try:
        text = readme.read_text(encoding="utf-8")
    except OSError as exc:
        return False, f"README.md is unreadable: {exc}"
    if image_name not in text:
        return False, f"README.md does not reference {image_name}"
    return True, "README.md references representative image"


def blank_status(image: Image.Image) -> tuple[bool, str]:
    preview = image.convert("RGB").resize((64, 64))
    pixels = list(preview.get_flattened_data())
    near_black = sum(max(pixel) <= 8 for pixel in pixels) / len(pixels)
    near_white = sum(min(pixel) >= 247 for pixel in pixels) / len(pixels)
    extrema = ImageStat.Stat(preview).extrema
    channel_span = sum(high - low for low, high in extrema) / 3
    if near_black >= BLANK_RATIO:
        return False, f"{near_black:.1%} of pixels are near-black"
    if near_white >= BLANK_RATIO:
        return False, f"{near_white:.1%} of pixels are near-white"
    if channel_span < 2:
        return False, "image has almost no channel variation"
    if near_black >= 0.90 or near_white >= 0.90 or channel_span < 8:
        return True, "image is suspiciously blank or low-variation"
    return True, "image has visible variation"


def audit_package(package: Path, repository_root: Path) -> dict[str, Any]:
    image_name = "gallery-16x9.jpg"
    image_path = package / image_name
    result: dict[str, Any] = {
        "package": package.relative_to(repository_root).as_posix(),
        "image": image_path.relative_to(repository_root).as_posix(),
        "status": "PASS",
        "messages": [],
    }

    def fail(message: str) -> None:
        result["status"] = "FAIL"
        result["messages"].append(message)

    def warn(message: str) -> None:
        if result["status"] == "PASS":
            result["status"] = "WARN"
        result["messages"].append(message)

    if not image_path.is_file():
        fail("missing representative image")
    else:
        try:
            with Image.open(image_path) as image:
                image.verify()
            with Image.open(image_path) as image:
                width, height = image.size
                result["width"] = width
                result["height"] = height
                result["format"] = image.format
                if width < MIN_DIMENSION or height < MIN_DIMENSION:
                    warn(f"low resolution: {width}x{height}")
                ratio = width / height if height else 0
                result["aspect_ratio"] = round(ratio, 6)
                if abs(ratio - ASPECT_RATIO) > ASPECT_TOLERANCE:
                    fail(f"aspect ratio mismatch: {width}x{height}")
                visible, message = blank_status(image)
                if not visible:
                    fail(f"suspiciously blank image: {message}")
                elif "suspiciously" in message:
                    warn(f"suspiciously blank image: {message}")
        except Exception as exc:  # Pillow raises several format-specific errors.
            fail(f"corrupt or unreadable image: {exc}")

    readme_ok, readme_message = read_readme_status(package, image_name)
    result["readme_reference"] = readme_ok
    if not readme_ok:
        fail(readme_message)

    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path, default=Path("style-packages"))
    parser.add_argument("--output", type=Path, help="write the machine-readable report")
    parser.add_argument("--strict", action="store_true", help="treat warnings as failures")
    args = parser.parse_args()

    style_root = args.path.resolve()
    repository_root = style_root.parent if style_root.name == "style-packages" else style_root
    results = [audit_package(package, repository_root) for package in discover_packages(style_root)]
    counts = {status: sum(item["status"] == status for item in results) for status in ("PASS", "WARN", "FAIL")}
    for item in results:
        for message in item["messages"] or ["valid image"]:
            print(f"{item['status']}: {item['package']}: {message}")

    report = {
        "schema_version": "1.0.0",
        "root": args.path.as_posix(),
        "counts": counts,
        "packages": results,
    }
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    if counts["FAIL"] or (args.strict and counts["WARN"]):
        raise SystemExit(1)
    print(f"SUMMARY: {counts['PASS']} pass, {counts['WARN']} warn, {counts['FAIL']} fail")


if __name__ == "__main__":
    main()

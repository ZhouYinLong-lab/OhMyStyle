#!/usr/bin/env python3
"""Compare two Style Package manifests using transparent vocabulary overlap."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import yaml


DIMENSIONS = {
    "mood": ("visual_identity", "mood"),
    "dominant_colors": ("visual_identity", "color", "dominant_colors"),
    "lighting": ("visual_identity", "lighting", "direction"),
    "framing": ("visual_identity", "composition", "framing"),
    "composition_principles": ("visual_identity", "composition", "principles"),
    "avoid": ("avoid",),
}


def load_style(path: Path) -> dict[str, Any]:
    package = path / "style.yaml" if path.is_dir() else path
    with package.open(encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise SystemExit(f"Not a YAML object: {package}")
    return data


def get_path(data: dict[str, Any], path: tuple[str, ...]) -> list[str]:
    value: Any = data
    for key in path:
        if not isinstance(value, dict):
            return []
        value = value.get(key)
    if not isinstance(value, list):
        return []
    return [str(item).lower() for item in value]


def overlap(left: list[str], right: list[str]) -> dict[str, Any]:
    left_set, right_set = set(left), set(right)
    union = left_set | right_set
    return {
        "left": sorted(left_set),
        "right": sorted(right_set),
        "shared": sorted(left_set & right_set),
        "jaccard": round(len(left_set & right_set) / len(union), 3) if union else 0.0,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Compare two Style Package manifests.")
    parser.add_argument("left", type=Path)
    parser.add_argument("right", type=Path)
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()

    left, right = load_style(args.left), load_style(args.right)
    dimensions = {
        name: overlap(get_path(left, path), get_path(right, path))
        for name, path in DIMENSIONS.items()
    }
    result = {
        "left": {"id": left.get("id"), "name": left.get("name"), "version": left.get("version")},
        "right": {"id": right.get("id"), "name": right.get("name"), "version": right.get("version")},
        "dimensions": dimensions,
        "interpretation": "Vocabulary overlap is a review aid, not a claim that two styles are visually identical.",
    }

    if args.as_json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return
    print(f"{result['left']['id']} vs {result['right']['id']}")
    for name, values in dimensions.items():
        print(f"- {name}: {values['jaccard']:.3f}; shared={', '.join(values['shared']) or 'none'}")


if __name__ == "__main__":
    main()

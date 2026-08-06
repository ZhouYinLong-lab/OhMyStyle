#!/usr/bin/env python3
"""Create resource.yaml contracts for existing executable style packages."""

from __future__ import annotations

import argparse
from pathlib import Path

import yaml

from resource_registry import discover_packages, load_yaml


DIMENSIONS = {
    "artist": ["medium", "composition", "lighting", "palette", "surface", "texture"],
    "movement": ["medium", "composition", "lighting", "palette", "surface", "texture"],
    "school": ["medium", "composition", "lighting", "palette", "surface", "texture"],
    "photographer": ["camera", "composition", "lighting", "palette", "surface", "subject_treatment"],
    "technique": ["medium", "process", "lighting", "surface", "texture"],
    "game_art": ["medium", "composition", "lighting", "palette", "texture", "layout"],
    "preset": ["composition", "lighting", "palette", "surface"],
}


def image_count(directory: Path) -> int:
    if not directory.is_dir():
        return 0
    ignored = {".md", ".yaml", ".yml", ".json", ".csv", ".txt"}
    return sum(1 for path in directory.iterdir() if path.is_file() and path.suffix.lower() not in ignored)


def build_manifest(package: Path) -> dict:
    package_data = load_yaml(package / "package.yaml")
    accepted = image_count(package / "examples" / "accepted")
    return {
        "schema_version": "1.0.0",
        "resource_id": package_data["id"],
        "resource_type": "visual_style",
        "maturity": "L3" if accepted else "L2",
        "task_independent": True,
        "focus_dimensions": DIMENSIONS[package_data["kind"]],
        "artifacts": {
            "package": "package.yaml",
            "identity": "identity.yaml",
            "visual_signature": "visual-signature.yaml",
            "reproduction": "reproduction.yaml",
            "evaluation": "evaluation.yaml",
            "references": "references/manifest.csv",
            "provenance": "provenance.yaml",
            "prompt": "prompts/base.txt",
            "accepted_examples": "examples/accepted",
            "rejected_examples": "examples/rejected",
        },
        "evidence": {
            "reference_backed": True,
            "accepted_example": bool(accepted),
            "rejected_examples_optional": True,
        },
        "rights": {
            "reference_policy": "Each reference manifest row governs source, license, attribution, and redistribution status.",
            "generated_demo_policy": "Generated demonstrations are anonymous new scenes and are not source artworks.",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path, default=Path("style-packages"))
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    for package in discover_packages(args.path):
        output = package / "resource.yaml"
        if output.exists() and not args.force:
            continue
        output.write_text(yaml.safe_dump(build_manifest(package), sort_keys=False, allow_unicode=True), encoding="utf-8")
    print(f"SCAFFOLDED: {len(discover_packages(args.path))} resource manifest(s)")


if __name__ == "__main__":
    main()

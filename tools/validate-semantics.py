#!/usr/bin/env python3
"""Validate package classification, relationship metadata, and subject leakage."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

from safe_yaml import safe_load


REQUIRED_RELATION_KEYS = {
    "family",
    "near_duplicates",
    "supersedes",
    "conflicts",
    "distinctives",
    "avoid_overlap",
}

EXPECTED_SOURCE_TYPES = {
    "artist": "artist",
    "photographer": "photographer",
    "movement": "movement",
    "school": "design_school",
    "technique": "technique",
    "preset": "preset",
    "game_art": "game_art",
}

# These patterns intentionally target requirement language, not ordinary
# descriptive vocabulary. A package may mention a bridge as an optional motif;
# it must not require a bridge in every generated image.
FIXED_SUBJECT_PATTERNS = [
    re.compile(r"\b(?:city|forest|bridge|railway|house|alley|portrait|flower)\s+(?:must|required|always)\b", re.I),
    re.compile(r"(?:城市|森林|桥|铁路|房屋|巷道|人像|花卉)(?:必须|必需|默认)"),
]


def load(path: Path) -> Any:
    with path.open(encoding="utf-8") as handle:
        return safe_load(handle)


def discover(root: Path) -> list[Path]:
    if not root.exists():
        raise SystemExit(f"Path does not exist: {root}")
    if (root / "package.yaml").is_file():
        return [root]
    base = root / "style-packages" if (root / "style-packages").is_dir() else root
    return sorted(path.parent for path in base.rglob("package.yaml"))


def list_values(value: Any) -> list[str]:
    return [str(item) for item in value] if isinstance(value, list) else []


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate semantic package metadata")
    parser.add_argument("path", nargs="?", type=Path, default=Path("style-packages"))
    args = parser.parse_args()

    packages = discover(args.path)
    errors: list[str] = []
    warnings: list[str] = []
    package_ids = {path.name for path in packages}

    for package in packages:
        manifest_path = package / "package.yaml"
        relations_path = package / "relations.yaml"
        try:
            manifest = load(manifest_path)
            relations = load(relations_path)
        except Exception as exc:  # validation should report the package, not crash
            errors.append(f"{package}: invalid metadata YAML: {exc}")
            continue

        if not isinstance(manifest, dict):
            errors.append(f"{package}: package.yaml must be an object")
            continue
        if not isinstance(relations, dict):
            errors.append(f"{package}: relations.yaml must be an object")
            continue

        kind = str(manifest.get("kind", ""))
        classification = manifest.get("classification")
        if not isinstance(classification, dict):
            errors.append(f"{package}: missing classification")
        else:
            expected = EXPECTED_SOURCE_TYPES.get(kind)
            if expected and classification.get("source_type") != expected:
                errors.append(f"{package}: classification.source_type must be {expected}")
            axes = classification.get("visual_axes")
            if not isinstance(axes, list) or not axes:
                errors.append(f"{package}: classification.visual_axes must be a non-empty list")

        policy = manifest.get("subject_policy")
        if not isinstance(policy, dict) or policy.get("mode") != "open":
            errors.append(f"{package}: subject_policy.mode must be open")
        elif list_values(policy.get("fixed_subjects")):
            errors.append(f"{package}: subject_policy.fixed_subjects must be empty")

        missing = sorted(REQUIRED_RELATION_KEYS - set(relations))
        for key in missing:
            errors.append(f"{package}: relations.yaml missing {key}")

        for relation_key in ("near_duplicates", "supersedes", "conflicts"):
            for target in list_values(relations.get(relation_key)):
                target_id = target.rsplit("/", 1)[-1]
                if target_id not in package_ids:
                    errors.append(f"{package}: {relation_key} points to unknown package {target}")
                if target_id == package.name:
                    errors.append(f"{package}: {relation_key} points to itself")

        if list_values(relations.get("near_duplicates")) and not list_values(relations.get("distinctives")):
            errors.append(f"{package}: near_duplicates requires non-empty distinctives")

        for relative in ("prompts/base.txt", "visual-signature.yaml", "identity.yaml"):
            path = package / relative
            if not path.is_file():
                continue
            text = path.read_text(encoding="utf-8")
            for pattern in FIXED_SUBJECT_PATTERNS:
                if pattern.search(text):
                    warnings.append(f"{package}: possible fixed subject language in {relative}")
                    break

    for warning in sorted(set(warnings)):
        print(f"WARN: {warning}")
    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        raise SystemExit(1)
    print(f"PASS: {len(packages)} package(s) passed semantic validation")
    print(f"WARNINGS: {len(set(warnings))}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Validate a 20-package OhMyStyle expansion batch manifest."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

from safe_yaml import safe_load


TARGET_COUNT = 20
KNOWN_CATEGORIES = {
    "artists",
    "photographers",
    "movements",
    "schools",
    "techniques",
    "presets",
    "game-art",
}
STATUSES = {"pending", "in_progress", "complete"}
REQUIRED_PACKAGE_FIELDS = {
    "package_id",
    "category",
    "name",
    "source_status",
    "reference_status",
    "package_status",
    "gallery_status",
    "docs_status",
    "validation_status",
    "commit",
}
COMPLETE_FIELDS = (
    "source_status",
    "reference_status",
    "package_status",
    "gallery_status",
    "docs_status",
    "validation_status",
)


def load_manifest(path: Path) -> dict:
    if not path.is_file():
        raise ValueError(f"manifest does not exist: {path}")
    with path.open(encoding="utf-8") as handle:
        value = safe_load(handle)
    if not isinstance(value, dict):
        raise ValueError("top-level value must be an object")
    return value


def package_path(root: Path, package_id: str) -> Path:
    parts = Path(package_id).parts
    if len(parts) != 2 or any(part in {"", ".", ".."} for part in parts):
        raise ValueError("package_id must be category/package-id")
    return root / parts[0] / parts[1]


def validate(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        manifest = load_manifest(path)
    except (OSError, ValueError, yaml.YAMLError) as exc:
        return [f"{path}: invalid manifest: {exc}"]

    if manifest.get("target_count") != TARGET_COUNT:
        errors.append(f"target_count must be {TARGET_COUNT}")
    status = manifest.get("status")
    if status not in {"planning", "research", "building", "review", "complete"}:
        errors.append("status must be planning, research, building, review, or complete")

    plan = manifest.get("category_plan")
    if not isinstance(plan, dict):
        errors.append("category_plan must be an object")
        plan = {}
    plan_total = 0
    for category, count in plan.items():
        if category not in KNOWN_CATEGORIES:
            errors.append(f"category_plan contains unknown category: {category}")
        if not isinstance(count, int) or count < 0:
            errors.append(f"category_plan.{category} must be a non-negative integer")
        else:
            plan_total += count
    if plan_total != TARGET_COUNT:
        errors.append(f"category_plan must total {TARGET_COUNT}, got {plan_total}")

    packages = manifest.get("packages")
    if not isinstance(packages, list):
        errors.append("packages must be a list")
        packages = []
    if len(packages) != TARGET_COUNT:
        errors.append(f"packages must contain exactly {TARGET_COUNT} entries, got {len(packages)}")

    ids: set[str] = set()
    actual_counts: dict[str, int] = {}
    repo_root = path.parent.parent if path.parent.name == "batches" else path.parent
    for index, entry in enumerate(packages, start=1):
        prefix = f"packages[{index}]"
        if not isinstance(entry, dict):
            errors.append(f"{prefix} must be an object")
            continue
        missing = REQUIRED_PACKAGE_FIELDS - set(entry)
        if missing:
            errors.append(f"{prefix} missing fields: {', '.join(sorted(missing))}")
        package_id = entry.get("package_id")
        category = entry.get("category")
        if not isinstance(package_id, str) or not package_id:
            errors.append(f"{prefix}.package_id must be a non-empty string")
            continue
        if package_id in ids:
            errors.append(f"duplicate package_id: {package_id}")
        ids.add(package_id)
        if not isinstance(category, str) or category not in KNOWN_CATEGORIES:
            errors.append(f"{prefix}.category is not a known category")
        else:
            actual_counts[category] = actual_counts.get(category, 0) + 1
        for field in COMPLETE_FIELDS:
            if entry.get(field) not in STATUSES:
                errors.append(f"{prefix}.{field} must be one of {sorted(STATUSES)}")
        if status == "complete":
            if any(entry.get(field) != "complete" for field in COMPLETE_FIELDS):
                errors.append(f"{prefix} is not complete while the batch is complete")
            if not isinstance(entry.get("commit"), str) or not entry.get("commit").strip():
                errors.append(f"{prefix}.commit is required for a complete batch")
            try:
                package = package_path(repo_root, package_id)
            except ValueError as exc:
                errors.append(f"{prefix}: {exc}")
                continue
            for required in ("package.yaml", "README.md", "README.en.md", "gallery-16x9.jpg"):
                if not (package / required).is_file():
                    errors.append(f"{package}: missing {required}")

    expected_counts = {key: value for key, value in plan.items() if value}
    if actual_counts != expected_counts:
        errors.append(f"category_plan does not match package categories: plan={plan}, actual={actual_counts}")
    return errors


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    args = parser.parse_args()
    errors = validate(args.manifest)
    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        raise SystemExit(1)
    print(f"PASS: {args.manifest} is a valid {TARGET_COUNT}-package batch manifest")


if __name__ == "__main__":
    main()

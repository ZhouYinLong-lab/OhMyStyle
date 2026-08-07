#!/usr/bin/env python3
"""Create a contributor-ready executable style package from the canonical template."""

from __future__ import annotations

import argparse
import csv
import re
import shutil
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_ROOT = ROOT / "templates" / "style-package"

KIND_DIRECTORIES = {
    "artist": "artists",
    "photographer": "photographers",
    "movement": "movements",
    "school": "schools",
    "technique": "techniques",
    "preset": "presets",
    "game_art": "game-art",
}

KIND_NAMES = {
    "artist": "艺术家",
    "photographer": "摄影师",
    "movement": "艺术流派",
    "school": "艺术与摄影学校",
    "technique": "工艺与媒介",
    "preset": "原创预设",
    "game_art": "游戏美术",
}

FOCUS_DIMENSIONS = {
    "artist": ["medium", "composition", "lighting", "palette", "surface", "texture"],
    "movement": ["medium", "composition", "lighting", "palette", "surface", "texture"],
    "school": ["medium", "composition", "lighting", "palette", "surface", "texture"],
    "photographer": ["camera", "composition", "lighting", "palette", "surface", "subject_treatment"],
    "technique": ["medium", "process", "lighting", "surface", "texture"],
    "game_art": ["medium", "composition", "lighting", "palette", "texture", "layout"],
    "preset": ["composition", "lighting", "palette", "surface"],
}

DOMAIN_NAMES = {
    "painting": "绘画",
    "photography": "摄影",
    "printmaking": "版画",
    "design": "设计",
    "game_art": "游戏美术",
    "hybrid": "混合媒介",
}

TOKEN_PATTERN = re.compile(r"\{\{([A-Z0-9_]+)\}\}")
SLUG_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a new executable style package from templates/style-package."
    )
    parser.add_argument("--kind", required=True, choices=sorted(KIND_DIRECTORIES))
    parser.add_argument("--id", required=True, help="URL-safe package id, for example: coastal-noir")
    parser.add_argument("--name", required=True, help="Human-facing package name")
    parser.add_argument("--domain", required=True, choices=["painting", "photography", "printmaking", "design", "game_art", "hybrid"])
    parser.add_argument("--summary", required=True, help="Observable package summary, at least 30 characters")
    parser.add_argument("--root", type=Path, default=Path("style-packages"), help="Style package root")
    parser.add_argument("--entity", help="Optional catalog entity path")
    parser.add_argument("--source-url", help="Optional primary source URL; enables L2 reference-backed output")
    parser.add_argument("--source-title", help="Title of the primary source")
    parser.add_argument("--source-creator", help="Creator or institution of the primary source")
    parser.add_argument("--source-license", default="link_only", help="Rights label for the source")
    parser.add_argument("--source-attribution", help="Required attribution text for the source")
    parser.add_argument("--source-role", default="primary", choices=["primary", "secondary", "details"])
    return parser.parse_args()


def validate_args(args: argparse.Namespace) -> None:
    if not SLUG_PATTERN.fullmatch(args.id):
        raise SystemExit("--id must contain lowercase letters, numbers, and single hyphens only")
    if len(args.summary.strip()) < 30:
        raise SystemExit("--summary must contain at least 30 characters")
    source_fields = [args.source_title, args.source_creator, args.source_attribution]
    if args.source_url and not all(source_fields):
        raise SystemExit("--source-url requires --source-title, --source-creator, and --source-attribution")
    if not args.source_url and any(source_fields):
        raise SystemExit("source metadata requires --source-url")


def token_values(args: argparse.Namespace) -> dict[str, str]:
    maturity = "L2" if args.source_url else "L1"
    reference_backed = "true" if args.source_url else "false"
    source_note = (
        "A primary source is recorded below; verify redistribution rights before bundling any image."
        if args.source_url
        else "No source has been recorded yet. Add at least one traceable source before submitting a pull request."
    )
    entity_line = f"entity: {args.entity}\n" if args.entity else ""
    identity_sources = f"  - {yaml_quote(args.source_url)}\n" if args.source_url else "  []\n"
    provenance_sources = (
        f"  - url: {yaml_quote(args.source_url)}\n"
        f"    title: {yaml_quote(args.source_title)}\n"
        f"    authority: {yaml_quote(args.source_creator)}\n"
        "    supports: source traceability and package scope\n"
        if args.source_url
        else "  []\n"
    )
    return {
        "ID": args.id,
        "NAME": args.name.strip(),
        "KIND": args.kind,
        "KIND_ZH": KIND_NAMES[args.kind],
        "DOMAIN": args.domain,
        "DOMAIN_ZH": DOMAIN_NAMES[args.domain],
        "SUMMARY": args.summary.strip(),
        "VERSION": "0.1.0",
        "MATURITY": maturity,
        "REFERENCE_BACKED": reference_backed,
        "SOURCE_NOTE": source_note,
        "ENTITY_LINE": entity_line,
        "PACKAGE_PATH": f"style-packages/{KIND_DIRECTORIES[args.kind]}/{args.id}",
        "FOCUS_DIMENSIONS": "".join(f"  - {item}\n" for item in FOCUS_DIMENSIONS[args.kind]),
        "IDENTITY_SOURCES": identity_sources,
        "PROVENANCE_SOURCES": provenance_sources,
    }


def yaml_quote(value: str) -> str:
    if "\n" in value or "\r" in value:
        raise SystemExit("source metadata must be single-line text")
    return "'" + value.replace("'", "''") + "'"


def render(text: str, values: dict[str, str]) -> str:
    rendered = text
    for token, value in values.items():
        rendered = rendered.replace("{{" + token + "}}", value)
    unknown = sorted(set(TOKEN_PATTERN.findall(rendered)))
    if unknown:
        raise ValueError(f"unresolved template tokens: {', '.join(unknown)}")
    return rendered


def write_manifest(package: Path, args: argparse.Namespace) -> None:
    manifest = package / "references" / "manifest.csv"
    manifest.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "asset_id", "local_path", "title", "creator", "year", "source_url",
        "license", "attribution", "role", "notes",
    ]
    with manifest.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        if args.source_url:
            writer.writerow({
                "asset_id": f"{args.id}-primary-source",
                "local_path": "",
                "title": args.source_title,
                "creator": args.source_creator,
                "year": "",
                "source_url": args.source_url,
                "license": args.source_license,
                "attribution": args.source_attribution,
                "role": args.source_role,
                "notes": "Link-only source record; bundle a local asset only after redistribution rights are verified.",
            })


def create_package(args: argparse.Namespace) -> Path:
    validate_args(args)
    if not TEMPLATE_ROOT.is_dir():
        raise SystemExit(f"Template directory is missing: {TEMPLATE_ROOT}")
    target = args.root / KIND_DIRECTORIES[args.kind] / args.id
    if target.exists():
        raise SystemExit(f"Target already exists; refusing to overwrite: {target}")

    values = token_values(args)
    target.mkdir(parents=True)
    try:
        for source in TEMPLATE_ROOT.rglob("*"):
            relative = source.relative_to(TEMPLATE_ROOT)
            if relative.name == "TEMPLATE.md":
                continue
            if source.is_dir():
                (target / relative).mkdir(parents=True, exist_ok=True)
                continue
            destination_relative = Path(str(relative).replace(".tmpl", ""))
            destination = target / destination_relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            if relative.as_posix() == "references/manifest.csv":
                continue
            if source.suffix == ".tmpl" or source.suffix in {".md", ".txt", ".yaml", ".json", ".csv"}:
                destination.write_text(render(source.read_text(encoding="utf-8"), values), encoding="utf-8")
            else:
                shutil.copyfile(source, destination)
        write_manifest(target, args)
    except Exception:
        shutil.rmtree(target)
        raise
    return target


def main() -> None:
    args = parse_args()
    try:
        target = create_package(args)
    except (OSError, ValueError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
    maturity = "L2" if args.source_url else "L1"
    print(f"CREATED: {target}")
    print(f"MATURITY: {maturity}")
    print("NEXT: fill the TODO fields, replace gallery-16x9.svg, then run the validation commands in CONTRIBUTING.md")


if __name__ == "__main__":
    main()

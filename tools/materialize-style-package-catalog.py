#!/usr/bin/env python3
"""Materialize a curated, reference-backed style-package catalog."""

from __future__ import annotations

import argparse
import csv
import html
import json
import re
import sys
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_ROOT = ROOT / "templates" / "style-package"
KIND_DIRS = {"artist": "artists", "photographer": "photographers", "game_art": "game-art"}
KIND_ZH = {"artist": "艺术家", "photographer": "摄影师", "game_art": "游戏美术"}
DOMAIN_ZH = {"painting": "绘画", "photography": "摄影", "game_art": "游戏美术"}
FOCUS = {
    "artist": ["medium", "composition", "lighting", "palette", "surface", "texture"],
    "photographer": ["camera", "composition", "lighting", "palette", "surface", "subject_treatment"],
    "game_art": ["medium", "composition", "lighting", "palette", "texture", "layout"],
}
TOKEN_RE = re.compile(r"\{\{([A-Z0-9_]+)\}\}")


def read_spec(path: Path) -> list[dict[str, Any]]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or not isinstance(data.get("packages"), list):
        raise SystemExit(f"Invalid catalog spec: {path}")
    packages = data["packages"]
    ids = [item.get("id") for item in packages]
    if len(ids) != len(set(ids)) or len(packages) != 25:
        raise SystemExit(f"Catalog must contain exactly 25 unique packages, found {len(packages)}")
    return packages


def dump_yaml(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True), encoding="utf-8")


def render_template(template: Path, values: dict[str, str]) -> str:
    text = template.read_text(encoding="utf-8")
    for key, value in values.items():
        text = text.replace("{{" + key + "}}", value)
    unknown = sorted(set(TOKEN_RE.findall(text)))
    if unknown:
        raise ValueError(f"unresolved template tokens in {template}: {', '.join(unknown)}")
    return text


def svg_gallery(item: dict[str, Any]) -> str:
    colors = item["palette"][:5]
    swatches = []
    for index, color in enumerate(colors):
        x = 80 + index * 288
        swatches.append(f'<rect x="{x}" y="600" width="248" height="150" rx="18" fill="{html.escape(color["hex"], quote=True)}"/>')
        swatches.append(f'<text x="{x + 18}" y="730" font-family="sans-serif" font-size="22" fill="#ffffff">{html.escape(color["name"], quote=True)}</text>')
    title = html.escape(item["name"], quote=True)
    description = html.escape(item["summary"], quote=True)
    shapes = [html.escape(color["hex"], quote=True) for color in colors]
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 900" role="img" aria-labelledby="title desc">
  <title id="title">{title} palette card</title>
  <desc id="desc">{description}</desc>
  <rect width="1600" height="900" fill="#10151D"/>
  <circle cx="1280" cy="240" r="250" fill="{shapes[0]}" opacity="0.85"/>
  <circle cx="1030" cy="360" r="190" fill="{shapes[1]}" opacity="0.85"/>
  <path d="M0 520 C280 360 510 690 800 500 S1260 330 1600 520 V900 H0 Z" fill="{shapes[2]}" opacity="0.9"/>
  <path d="M0 640 C280 520 530 760 880 610 S1260 520 1600 680 V900 H0 Z" fill="{shapes[3]}" opacity="0.9"/>
  {''.join(swatches)}
  <text x="80" y="120" font-family="sans-serif" font-size="52" font-weight="700" fill="#F5F1E8">{title}</text>
  <text x="80" y="175" font-family="sans-serif" font-size="24" fill="#C8D0D8">版权安全的抽象色板卡 · 可替换为已获授权的代表图</text>
</svg>
'''


def write_manifest(package: Path, item: dict[str, Any]) -> None:
    source = item["source"]
    fields = ["asset_id", "local_path", "title", "creator", "year", "source_url", "license", "attribution", "role", "notes"]
    with (package / "references" / "manifest.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerow({
            "asset_id": f"{item['id']}-primary-source", "local_path": "", "title": source["title"],
            "creator": source["authority"], "year": "", "source_url": source["url"], "license": "link_only",
            "attribution": source["attribution"], "role": "primary",
            "notes": "Link-only source record. Do not bundle or redistribute external artwork without explicit permission.",
        })


def benchmark(item: dict[str, Any]) -> dict[str, Any]:
    task_ids = [("portrait", "portrait"), ("still-life", "still_life"), ("architecture-environment", "architecture_environment"), ("minimal-composition", "minimal_composition"), ("fuzzy-brief", "fuzzy_brief")]
    return {
        "schema_version": "1.0.0", "benchmark_id": f"{item['id']}-visual-style-core-v1",
        "package": "package.yaml", "package_version": "0.1.0", "suite": "visual-style-core-v1",
        "rubric": "../../../../tasks/benchmarks/rubric.yaml", "maturity_target": "L3",
        "minimum_overall_score": 3.0, "minimum_task_score": 2.5,
        "tasks": [{"id": task_id, "kind": kind, "task": f"../../../../tasks/benchmarks/{kind.replace('_', '-')}.yaml"} for task_id, kind in task_ids],
    }


def write_package(item: dict[str, Any], force: bool) -> Path:
    package = ROOT / "style-packages" / KIND_DIRS[item["kind"]] / item["id"]
    if package.exists() and not force:
        raise SystemExit(f"Target already exists; refusing to overwrite: {package}")
    for relative in ["palette", "prompts", "examples/accepted", "examples/generated", "examples/rejected", "benchmark", "references"]:
        (package / relative).mkdir(parents=True, exist_ok=True)

    dump_yaml(package / "package.yaml", {
        "id": item["id"], "name": item["name"], "kind": item["kind"], "domain": item["domain"],
        "version": "0.1.0", "summary": item["summary"],
        "files": {"identity": "identity.yaml", "visual_signature": "visual-signature.yaml", "reproduction": "reproduction.yaml", "relations": "relations.yaml", "palette": "palette/palette.json", "prompts": "prompts", "evaluation": "evaluation.yaml", "references": "references/manifest.csv", "provenance": "provenance.yaml"},
    })
    dump_yaml(package / "identity.yaml", {
        "canonical_name": item["name"], "entity_type": item["entity_type"], "origin": item["origin"], "period": item["period"], "domain": item["domain"],
        "scope": {"use_cases": item["use_cases"], "exclusions": item["exclusions"]}, "sources": [item["source"]["url"]],
        "rendering": {"model": item["reproduction"]["medium"], "scene_logic": "New subject and composition; preserve only observable package rules.", "output_behavior": "Readable, independently authored image with no copied source arrangement."},
    })
    dump_yaml(package / "visual-signature.yaml", item["signature"])
    dump_yaml(package / "reproduction.yaml", {"medium": item["reproduction"]["medium"], "materials": item["reproduction"]["materials"], "process": item["reproduction"]["process"], "technical_direction": item["reproduction"]["technical"], "safety_note": "Use observable traits only. Do not reconstruct a named work, character, location, logo, text, or exact composition."})
    dump_yaml(package / "relations.yaml", {"related_packages": [], "contrast_note": "Compare medium, composition, lighting, palette, surface, and texture before crossing this package with another.", "crossing": {"supported": True, "default_mode": "adaptive", "note": "Cross-style composition is handled by the repository-level workflow, not by this package identity."}})
    dump_yaml(package / "evaluation.yaml", {
        "package_id": item["id"], "package_version": "0.1.0",
        "invariants": [
            {"id": "style_recognition", "weight": 3, "test": "The package medium, edge, light, palette, and texture decisions remain recognizable after the subject changes."},
            {"id": "prompt_adherence", "weight": 3, "test": "The requested subject, count, setting, and aspect ratio are followed without adding a copied source arrangement."},
            {"id": "material_readability", "weight": 2, "test": "Requested materials and capture behavior remain visually distinguishable."},
            {"id": "human_artifact_control", "weight": 2, "test": "Hands, faces, geometry, text, reflections, and repeated details do not show avoidable generative defects."},
        ],
        "rejections": ["copied_named_work", "generic_global_filter", "unreadable_subject", "style_pollution", "unmotivated_extra_objects"],
        "minimum_score": 8, "benchmark_suite": ["portrait", "still_life", "architecture_environment", "minimal_composition", "fuzzy_brief"],
    })
    source = item["source"]
    dump_yaml(package / "provenance.yaml", {"package_id": item["id"], "package_version": "0.1.0", "curation_status": "reference_backed_link_only", "source_policy": "External works and game materials are recorded as links for research and visual analysis only. They are not bundled or redistributed.", "sources": [{"url": source["url"], "authority": source["authority"], "title": source["title"], "supports": "source traceability and observable package scope", "accessed": "2026-08-07"}], "attribution": source["attribution"]})
    dump_yaml(package / "resource.yaml", {"schema_version": "1.0.0", "resource_id": item["id"], "resource_type": "visual_style", "maturity": "L2", "task_independent": True, "focus_dimensions": FOCUS[item["kind"]], "artifacts": {"package": "package.yaml", "identity": "identity.yaml", "visual_signature": "visual-signature.yaml", "reproduction": "reproduction.yaml", "evaluation": "evaluation.yaml", "references": "references/manifest.csv", "provenance": "provenance.yaml", "prompt": "prompts/base.txt", "accepted_examples": "examples/accepted", "rejected_examples": "examples/rejected", "benchmark": "benchmark/benchmark.yaml"}, "evidence": {"reference_backed": True, "accepted_example": False, "rejected_examples_optional": True}, "rights": {"reference_policy": "Reference manifest rows are link-only unless redistribution rights are separately verified.", "generated_demo_policy": "Generated demonstrations must be new anonymous scenes and must not reproduce a source work."}})
    (package / "palette" / "palette.json").write_text(json.dumps({"name": item["id"], "usage": "Curated role-based colors; treat values as anchors, not a global filter.", "colors": item["palette"]}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    signature_lines = [line for values in item["signature"].values() if isinstance(values, list) for line in values[:3]]
    base_prompt = "Create a new subject and composition using these observable visual decisions:\n" + "\n".join(f"- {line}" for line in signature_lines) + "\nKeep the medium, lighting, palette roles, surface behavior, and edge language coherent. Do not copy any reference work, named character, location, logo, text, or exact arrangement."
    negative = ["copied composition or recognizable source scene", "unmotivated style mixing", "generic global color filter", "unreadable subject or broken geometry", "extra logos, readable text, or watermarks"] + item["exclusions"]
    (package / "prompts" / "base.txt").write_text(base_prompt + "\n", encoding="utf-8")
    (package / "prompts" / "negative.txt").write_text("\n".join(f"- {entry}" for entry in negative) + "\n", encoding="utf-8")
    (package / "gallery-16x9.svg").write_text(svg_gallery(item), encoding="utf-8")

    package_path = f"style-packages/{KIND_DIRS[item['kind']]}/{item['id']}"
    zh_values = {"NAME": item["name"], "KIND_ZH": KIND_ZH[item["kind"]], "KIND": item["kind"], "DOMAIN_ZH": DOMAIN_ZH[item["domain"]], "DOMAIN": item["domain"], "SUMMARY": item["summary"], "PACKAGE_PATH": package_path}
    en_values = {"NAME": item["name_en"], "KIND_ZH": KIND_ZH[item["kind"]], "KIND": item["kind"], "DOMAIN_ZH": DOMAIN_ZH[item["domain"]], "DOMAIN": item["domain"], "SUMMARY": item["summary_en"], "PACKAGE_PATH": package_path}
    (package / "README.md").write_text(render_template(TEMPLATE_ROOT / "README.md.tmpl", zh_values), encoding="utf-8")
    (package / "README.en.md").write_text(render_template(TEMPLATE_ROOT / "README.en.md.tmpl", en_values), encoding="utf-8")
    (package / "version.md").write_text("# Version\n\n- 0.1.0: initial reference-backed package\n", encoding="utf-8")
    (package / "examples/accepted/README.md").write_text("# Accepted examples\n\nThis reference-backed package is ready for an independently generated example. Add a new anonymous scene only after it passes `evaluation.yaml`.\n", encoding="utf-8")
    (package / "examples/generated/README.md").write_text("# Generated examples\n\nGenerated images are optional and are not included until their prompt, model, seed, license, and review status are recorded.\n", encoding="utf-8")
    (package / "examples/rejected/README.md").write_text("# Rejected examples\n\nRecord failed outputs here only when they teach a reproducible failure mode.\n", encoding="utf-8")
    dump_yaml(package / "benchmark/benchmark.yaml", benchmark(item))
    write_manifest(package, item)
    return package


def card(item: dict[str, Any], english: bool) -> str:
    name = item["name_en"] if english else item["name"]
    readme = "README.en.md" if english else "README.md"
    link_text = "Open README" if english else "打开 README"
    alt = html.escape(f"{name} representative image", quote=True)
    return f'<td width="33%" valign="top" align="center"><a href="{item["id"]}/{readme}"><img src="{item["id"]}/gallery-16x9.svg" width="230" alt="{alt}"></a><br><strong>{html.escape(name)}</strong><br><a href="{item["id"]}/{readme}">{link_text}</a></td>'


def update_category_readme(kind: str, items: list[dict[str, Any]]) -> None:
    category = KIND_DIRS[kind]
    for path, english in ((ROOT / "style-packages" / category / "README.md", False), (ROOT / "style-packages" / category / "README.en.md", True)):
        text = path.read_text(encoding="utf-8")
        marker = "## 本批新增" if not english else "## Added in this batch"
        if marker in text:
            continue
        count_match = re.search(r"收录 ([0-9]+) 个独立风格包|contains ([0-9]+) independent style packages", text)
        if count_match:
            old_count = int(next(value for value in count_match.groups() if value is not None))
            text = text[:count_match.start(1 if count_match.group(1) else 2)] + str(old_count + len(items)) + text[count_match.end(1 if count_match.group(1) else 2):]
        rows = []
        for start in range(0, len(items), 3):
            chunk = items[start:start + 3]
            cells = [card(item, english) for item in chunk]
            cells += ['<td width="33%"></td>'] * (3 - len(cells))
            rows.append("<tr>" + "".join(cells) + "</tr>")
        note = "这些包使用版权安全的抽象色板卡作为临时代表图，获得授权或完成独立生图审核后可替换。" if not english else "These packages use rights-safe abstract palette cards temporarily; replace them after an authorized or independently generated representative image is reviewed."
        section = f"\n\n{marker}\n\n{note}\n\n<table>\n" + "\n".join(rows) + "\n</table>\n"
        path.write_text(text.rstrip() + section, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("spec", type=Path, nargs="?", default=Path("tasks/style-package-expansion.yaml"))
    parser.add_argument("--force", action="store_true", help="overwrite only the catalog package targets")
    parser.add_argument("--no-index", action="store_true", help="do not append category README cards")
    args = parser.parse_args()
    spec_path = args.spec if args.spec.is_absolute() else ROOT / args.spec
    items = read_spec(spec_path)
    packages = [write_package(item, args.force) for item in items]
    if not args.no_index:
        for kind in KIND_DIRS:
            update_category_readme(kind, [item for item in items if item["kind"] == kind])
    print(f"MATERIALIZED: {len(packages)} package(s)")
    print("NEXT: run tools/validate-package.py, tools/validate-resources.py, tools/validate-benchmarks.py, and tools/build-registry.py")


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, yaml.YAMLError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc

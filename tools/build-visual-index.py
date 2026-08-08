#!/usr/bin/env python3
"""Generate user-facing visual-feature indexes from package metadata."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

import yaml


FEATURES: list[tuple[str, str, tuple[str, ...]]] = [
    ("柔和自然光", "Soft natural light", ("natural-light", "window-light", "overcast", "daylight", "frosted", "soft-light", "quiet-natural")),
    ("深暗戏剧光", "Deep dramatic light", ("chiaroscuro", "shadow", "tenebrism", "baroque", "caravaggio", "rembrandt", "nocturnal", "noir")),
    ("高饱和撞色", "High-chroma colour", ("chroma", "high-chroma", "acid", "hard-light", "color-block", "synthwave", "vaporwave", "pop-art", "memphis", "kitsch")),
    ("几何版式", "Geometric layout", ("geometric", "geometry", "grid", "bauhaus", "de-stijl", "ulm", "constructivism", "suprematism", "minimalism", "typographic")),
    ("印刷颗粒", "Print texture", ("print", "grain", "cyanotype", "linocut", "woodcut", "screen-print", "mezzotint", "drypoint", "halftone")),
    ("水彩与透明层", "Watercolour and transparent layers", ("watercolor", "watercolour", "fresco", "wash", "transparent", "encaustic")),
    ("像素网格", "Pixel grid", ("pixel", "rpg-maker", "top-down", "side-scrolling", "zx-spectrum", "isometric-pixel")),
    ("霓虹城市", "Neon city", ("cyberpunk", "neon", "synthwave", "vaporwave", "cybercore")),
    ("低多边形与体素", "Low-poly and voxel", ("low-poly", "voxel", "stylized-pbr", "diorama", "papercraft")),
    ("拼贴与混合媒介", "Collage and mixed media", ("collage", "mixed-media", "scrapbook", "assemblage", "bearden")),
]


def discover(root: Path) -> list[Path]:
    return sorted(path.parent for path in root.resolve().rglob("package.yaml"))


def package_text(package: Path, package_data: dict[str, Any], relations: dict[str, Any]) -> str:
    values: list[str] = [package.name, str(package_data.get("name", "")), str(relations.get("family", ""))]
    for key in ("distinctives",):
        values.extend(str(value) for value in relations.get(key, []) if isinstance(value, str))
    classification = package_data.get("classification", {})
    values.extend(str(value) for value in classification.get("visual_axes", []) if isinstance(value, str))
    return " ".join(values).lower()


def render(root: Path, english: bool = False) -> str:
    repository_root = root.resolve().parent
    packages: list[dict[str, str]] = []
    for package in discover(root):
        package_data = yaml.safe_load((package / "package.yaml").read_text(encoding="utf-8"))
        relations = yaml.safe_load((package / "relations.yaml").read_text(encoding="utf-8"))
        if not isinstance(package_data, dict) or not isinstance(relations, dict):
            continue
        packages.append({
            "path": package.relative_to(repository_root).as_posix(),
            "name": str(package_data.get("name", package.name)),
            "text": package_text(package, package_data, relations),
        })

    title = "Visual feature index" if english else "视觉特征索引"
    intro = (
        "This index is generated from each package's classification and relations metadata. "
        "It is a navigation aid, not a new package taxonomy; the seven source-based gallery categories remain unchanged."
        if english else
        "本索引由各风格包的 `classification` 与 `relations.yaml` 自动生成，用于按视觉问题查找，不新增或替换主画廊的七大来源分类。"
    )
    lines = [f"# {title}", "", intro, ""]
    for chinese, english_name, terms in FEATURES:
        label = english_name if english else chinese
        lines.extend([f"## {label}", ""])
        matches = [item for item in packages if any(term in item["text"] for term in terms)]
        if not matches:
            lines.append("No package is currently indexed here." if english else "当前没有包被索引到这里。")
        else:
            for item in matches:
                readme = f"../{item['path']}/README.en.md" if english else f"../{item['path']}/README.md"
                lines.append(f"- [{item['name']}]({readme})")
        lines.append("")
    lines.extend([
        "## Notes" if english else "## 说明",
        "",
        "The package controls visual language, not a fixed subject. Read the package README and subject-independence policy before generating." if english else "风格包只控制视觉语言，不规定固定主体。生成前请阅读对应 README 与主体独立性说明。",
        "",
    ])
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path, default=Path("style-packages"))
    parser.add_argument("--output", type=Path, default=Path("docs/VISUAL-INDEX.md"))
    parser.add_argument("--output-en", type=Path, default=Path("docs/VISUAL-INDEX.en.md"))
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(render(args.path), encoding="utf-8")
    args.output_en.write_text(render(args.path, english=True), encoding="utf-8")
    print(f"PASS: generated {args.output} and {args.output_en}")


if __name__ == "__main__":
    main()

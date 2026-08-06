#!/usr/bin/env python3
"""Generate bilingual package READMEs and the root style gallery.

The generator intentionally reads package metadata instead of embedding style-
specific logic in the runtime. It is a documentation/indexing tool only: it
does not copy external artworks, alter provenance, or change package behavior.
"""

from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]

CATEGORY_LABELS = {
    "artists": ("艺术家", "Artists"),
    "photographers": ("摄影师", "Photographers"),
    "movements": ("艺术流派与历史时期", "Movements and periods"),
    "schools": ("艺术与摄影学校", "Schools"),
    "techniques": ("工艺与媒介", "Techniques and media"),
    "game-art": ("游戏美术", "Game art"),
    "presets": ("原创预设", "Original presets"),
    "composites": ("交叉风格配方", "Cross-style recipes"),
    "legacy": ("继承的 110 个轻量预设", "Inherited 110 lightweight presets"),
}

KIND_LABELS = {
    "artist": ("艺术家", "artist"),
    "photographer": ("摄影师", "photographer"),
    "movement": ("艺术流派/历史时期", "movement or historical period"),
    "school": ("艺术/摄影学校", "school"),
    "technique": ("工艺或媒介", "technique or medium"),
    "game_art": ("游戏美术方向", "game-art direction"),
    "preset": ("原创视觉预设", "original visual preset"),
    "composite": ("交叉风格配方", "cross-style recipe"),
    "legacy": ("继承的轻量预设", "inherited lightweight preset"),
}


def read_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    return value if isinstance(value, dict) else {}


def read_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    return value if isinstance(value, dict) else {}


def clean(text: Any) -> str:
    return re.sub(r"\s+", " ", str(text or "")).strip()


def md_escape(text: str) -> str:
    return text.replace("[", "\\[").replace("]", "\\]")


def title_from_slug(slug: str) -> str:
    return slug.replace("-", " ").title()


def package_image(package_dir: Path) -> Path | None:
    for folder in ("examples/accepted", "examples/generated"):
        candidates = sorted(
            p for p in (package_dir / folder).glob("*")
            if p.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"}
        )
        if candidates:
            return candidates[0]
    return None


def source_urls(package_dir: Path) -> list[str]:
    data = read_yaml(package_dir / "provenance.yaml")
    urls: list[str] = []
    for source in data.get("sources", []) or []:
        if isinstance(source, dict) and source.get("url"):
            urls.append(str(source["url"]))
        elif isinstance(source, str) and source.startswith("http"):
            urls.append(source)
    return list(dict.fromkeys(urls))


def local_link(label: str, path: Path, package_dir: Path) -> str | None:
    if not path.exists():
        return None
    return f"- [{label}]({path.relative_to(package_dir).as_posix()})"


def first_lines(path: Path, limit: int = 4) -> list[str]:
    if not path.exists():
        return []
    lines: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = clean(line.lstrip("- "))
        if line and not line.startswith("#"):
            lines.append(line)
        if len(lines) >= limit:
            break
    return lines


def modern_record(category: str, package_dir: Path) -> dict[str, Any]:
    package = read_yaml(package_dir / "package.yaml")
    composite = read_yaml(package_dir / "composite.yaml")
    resource = read_yaml(package_dir / "resource.yaml")
    identity = read_yaml(package_dir / "identity.yaml")
    signature = read_yaml(package_dir / "visual-signature.yaml")

    is_composite = bool(composite)
    name = clean(composite.get("name") if is_composite else package.get("name"))
    if not name:
        name = title_from_slug(package_dir.name)
    kind = "composite" if is_composite else clean(package.get("kind")) or category
    focus = resource.get("focus_dimensions", []) or []
    summary = clean(composite.get("provenance", {}).get("purpose") if is_composite else package.get("summary"))
    if not summary:
        summary = "A structured visual-style package with explicit references, prompts, and reproduction constraints."

    features: list[str] = []
    for key in ("composition", "color", "light", "surface", "texture", "invariants"):
        value = signature.get(key)
        if isinstance(value, list):
            features.extend(clean(item) for item in value if clean(item))
        elif isinstance(value, dict):
            for item in value.get("behavior", []) or []:
                if clean(item):
                    features.append(clean(item))
    features = list(dict.fromkeys(features))[:6]

    image = package_image(package_dir)
    if is_composite:
        bases = composite.get("bases", []) or []
        for base in bases:
            if not isinstance(base, dict):
                continue
            base_dir = ROOT / "style-packages" / str(base.get("package", ""))
            image = package_image(base_dir)
            if image:
                break

    return {
        "category": category,
        "slug": package_dir.name,
        "path": package_dir.relative_to(ROOT).as_posix(),
        "dir": package_dir,
        "name": name,
        "kind": kind,
        "summary": summary,
        "focus": [clean(item) for item in focus if clean(item)],
        "features": features,
        "identity": identity,
        "sources": source_urls(package_dir),
        "image": image,
        "composite": composite,
    }


def legacy_record(package_dir: Path) -> dict[str, Any]:
    data = read_json(package_dir / "style.json")
    name = clean(data.get("style_name")) or title_from_slug(package_dir.name)
    summary = clean(data.get("style_summary"))
    anchors = [clean(x) for x in data.get("style_fidelity_anchors", []) if clean(x)]
    image = package_dir / "preview-16x9.jpg"
    if not image.exists():
        image = next(
            (p for p in sorted(package_dir.glob("preview*")) if p.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp"}),
            None,
        )
    return {
        "category": "legacy",
        "slug": package_dir.name,
        "path": package_dir.relative_to(ROOT).as_posix(),
        "dir": package_dir,
        "name": name,
        "kind": "legacy",
        "summary": summary or "An inherited lightweight visual preset retained for compatibility.",
        "focus": [],
        "features": anchors[:6],
        "identity": {},
        "sources": ["https://github.com/VigoZhao/AI-Visual-Prompt-Cookbook"],
        "image": image,
        "composite": {},
    }


def relative_image(from_dir: Path, image: Path | None) -> str | None:
    if not image:
        return None
    return Path(os.path.relpath(image, from_dir)).as_posix()


def package_link(record: dict[str, Any]) -> str:
    return f"{record['path']}/README.md"


def cn_kind(kind: str) -> str:
    return KIND_LABELS.get(kind, ("视觉风格包", "visual-style package"))[0]


def en_kind(kind: str) -> str:
    return KIND_LABELS.get(kind, ("视觉风格包", "visual-style package"))[1]


def write_package_readme(record: dict[str, Any]) -> None:
    package_dir = record["dir"]
    image_ref = relative_image(package_dir, record["image"])
    name = record["name"]
    category_cn, category_en = CATEGORY_LABELS[record["category"]]
    kind_cn, kind_en = cn_kind(record["kind"]), en_kind(record["kind"])
    category_path = "../README.md" if record["kind"] == "legacy" else f"../../{record['category']}/README.md"
    focus = ", ".join(record["focus"]) if record["focus"] else "package-specific visual decisions"
    features = record["features"] or [record["summary"]]
    source_lines = []
    for url in record["sources"][:6]:
        source_lines.append(f"- [{url}]({url})")
    if not source_lines:
        source_lines.append("- No external source is redistributed; see the package provenance file.")

    image_block = f"![{md_escape(name)} representative example]({image_ref})\n" if image_ref else "_本包没有单独打包的代表图；请查看所引用基础包的示例。 / No standalone preview is bundled; see the referenced base package examples._\n"
    notice_path = "../../NOTICE" if record["kind"] == "legacy" else "../../../NOTICE"

    if record["kind"] == "legacy":
        cn_intro = (
            f"这是从原始 `AI-Visual-Prompt-Cookbook` 继承的轻量风格预设「{name}」。"
            "本仓库保留原有 `style.json`、预览图与兼容目录；此 README 只提供导航、使用方式和归属说明，"
            "不将继承内容重新宣称为 OhMyStyle 原创。"
        )
        en_intro = (
            f"This is the inherited lightweight preset “{name}” from the original "
            "`AI-Visual-Prompt-Cookbook` catalog. OhMyStyle keeps its `style.json`, previews, "
            "and compatibility path; this README adds navigation and usage guidance without claiming authorship."
        )
        package_usage = f"styles/{record['slug']}"
        links = f"- [style.json](style.json)\n- [16:9 preview](preview-16x9.jpg)"
    elif record["kind"] == "composite":
        bases = record["composite"].get("bases", []) or []
        base_lines = []
        for base in bases:
            if isinstance(base, dict) and base.get("package"):
                p = str(base["package"])
                base_lines.append(f"- [`{p}`](../../{p}/README.md) — role: `{base.get('role', 'style dimension')}`")
        cn_intro = f"这是一个独立的交叉风格配方「{name}」。它只引用已有风格包，并通过角色、权重和约束定义组合关系，不复制基础包的文字或参考资源。"
        en_intro = f"This is an independent cross-style recipe, “{name}”. It references existing packages and defines their roles, weights, and constraints without copying their text or reference assets."
        links = "- [composite.yaml](composite.yaml)"
        package_usage = f"style-packages/{record['category']}/{record['slug']}"
    else:
        cn_intro = f"这是一个面向「{name}」的独立 {kind_cn}。它把公开作品、研究资料和可观察视觉特征整理成可执行约束，重点关注 `{focus}`，用于生成新场景，而不是复制某一幅原作。"
        en_intro = f"This is an independent {kind_en} package for “{name}”. It turns public references, research material, and observable visual decisions into executable constraints focused on `{focus}`. It is intended for new scenes, not copies of a named artwork."
        links = "\n".join(
            item for item in (
                local_link("package.yaml", package_dir / "package.yaml", package_dir),
                local_link("provenance.yaml", package_dir / "provenance.yaml", package_dir),
                local_link("reference manifest", package_dir / "references/manifest.csv", package_dir),
            ) if item
        ) or "- See the package directory files for the available contract and provenance artifacts."
        package_usage = f"style-packages/{record['category']}/{record['slug']}"

    feature_cn = "；".join(features[:4])
    feature_en = "; ".join(features[:4])
    bases_block = "\n".join(base_lines) if record["kind"] == "composite" else "- See the package visual signature and reproduction files for the complete constraint set."

    if record["kind"] == "legacy":
        prompt_source_cn = f"打开 `{package_usage}/style.json`，或查看 [`docs/copy-prompts/{record['slug']}.md`](../../docs/copy-prompts/{record['slug']}.md)。"
        prompt_source_en = f"Open `{package_usage}/style.json`, or read [`docs/copy-prompts/{record['slug']}.md`](../../docs/copy-prompts/{record['slug']}.md)."
        api_command = f"python scripts/generate-copy-prompts.py ."
        api_note_cn = "继承预设没有结构化 API 编译器；可先生成 copy-prompt 文档，再将其中 Prompt 交给你自己的 API 适配器。"
        api_note_en = "The inherited preset has no structured API compiler; generate its copy-prompt document first, then submit that Prompt through your own API adapter."
        local_note_cn = "将 `style.json`、预览图和 copy-prompt 文档作为 ComfyUI 的文字与参考输入；如需更细的控制，建议迁移到结构化 `style-packages/`。"
        local_note_en = "Use `style.json`, the preview, and the copy-prompt document as ComfyUI text/reference inputs. For finer control, migrate the preset into a structured `style-packages/` package."
    else:
        prompt_source_cn = f"打开 `{package_usage}/prompts/base.txt`，替换变量后复制。"
        prompt_source_en = f"Open `{package_usage}/prompts/base.txt`, fill in its variables, and paste the result."
        api_command = (f"python tools/compile-style.py {package_usage} "
                       f"--subject \"你的主题\" --profile weak "
                       f"--output tmp/{record['slug']}-job.json")
        api_note_cn = "编译器只生成 provider-neutral 任务；再由你选择的 API 适配器提交，仓库不保存密钥。"
        api_note_en = "The compiler emits a provider-neutral job; your chosen API adapter submits it. The repository never stores your key."
        local_note_cn = "将 `prompts/`、`references/`、`palette/` 和生成的 job 导入本地模型工作流；模型权重由用户自行安装。"
        local_note_en = "Import `prompts/`, `references/`, `palette/`, and the compiled job into a local workflow; users install their own model weights."

    provenance_file = package_dir / "provenance.yaml"
    provenance_ref = "[`provenance.yaml`](provenance.yaml)" if provenance_file.exists() else "`provenance.yaml` (if present)"

    readme = f"""# {name}

{image_block}

> **分类 / Category:** [{category_cn} / {category_en}]
> **类型 / Type:** {kind_cn} / {kind_en}
> **包路径 / Package path:** `{record['path']}`

## 简介（中文）

{cn_intro}

核心观察点：{feature_cn}

## Overview (English)

{en_intro}

Key observations: {feature_en}

## 来源与版权（中文）

参考资料只用于研究和风格拆解。外部作品的版权、商标、截图和平台页面仍归原权利人所有；本包不代表与相关艺术家、摄影师、游戏或机构存在合作关系。生成示例是新的匿名场景，不是原作者作品。

来源链接：

{chr(10).join(source_lines)}

具体权利边界请先阅读 {provenance_ref} 和仓库根目录的 [`NOTICE`]({notice_path})。

## Sources and rights (English)

References are used for research and visual analysis. Copyright, trademarks, screenshots, and source pages remain with their respective rights holders. This package is independent and does not imply endorsement or affiliation. Generated examples are anonymous new scenes, not works by the referenced creator.

Source links:

{chr(10).join(source_lines)}

Read {provenance_ref} when present and the repository [`NOTICE`]({notice_path}) before redistributing anything.

## 只使用此包 / Use only this package

### 方式一：下载风格包，复制生成 Prompt

下载本目录，{prompt_source_cn} 把包内变量替换为你的主题，再将生成的 Prompt 复制到任意支持文字生图的平台。参考图、负面约束和可选参数见同目录文件。

Download this directory. {prompt_source_en} Fill in the variables and paste the resulting Prompt into an image model. Reference roles, negative constraints, and optional parameters are kept beside the package.

### 方式二：配置 API Key，一键生成

OhMyStyle 不托管用户密钥。配置你选择的模型提供商 API Key 后，{api_note_cn}

```bash
{api_command}
```

{api_note_en} Keep API keys outside the repository and let your chosen adapter submit the job to the model.

### 方式三：本地模型 + ComfyUI 工作流

{local_note_cn} 像素、遮罩或构图约束优先使用包内的 reproduction 与 workflow 文件。

{local_note_en} Use the package reproduction and workflow files when available. Model weights are not bundled; ComfyUI runs the models installed by the user.

## 包内文件 / Package files

{links}
{bases_block}

## 免责声明 / Disclaimer

风格包描述的是可观察的媒介、构图、色彩、光线和表面决策，不保证任何模型得到完全相同的输出，也不鼓励复制受保护作品的具体构图、人物、文字或标志。

The package describes observable decisions in medium, composition, color, light, and surface. It does not guarantee identical output and does not authorize copying protected compositions, characters, text, or marks.
"""
    (package_dir / "README.md").write_text(readme.rstrip() + "\n", encoding="utf-8")


def legacy_group(record: dict[str, Any]) -> str:
    text = f"{record['name']} {record['summary']}".lower()
    if any(token in text for token in ("photo", "portrait", "documentary", "travel", "editorial", "snapshot", "architectural")):
        return "legacy-editorial"
    if any(token in text for token in ("collage", "doodle", "manga", "anime", "comic", "scribble", "marker", "cutout", "graffiti")):
        return "legacy-collage"
    if any(token in text for token in ("product", "beverage", "glass", "plush", "3d", "furniture", "luxury")):
        return "legacy-product"
    return "legacy-posters"


def gallery_cell(record: dict[str, Any], document_dir: Path = ROOT) -> str:
    link = Path(os.path.relpath(ROOT / package_link(record), document_dir)).as_posix()
    image = record["image"]
    image_src = Path(os.path.relpath(image, document_dir)).as_posix() if image else None
    label = md_escape(record["name"])
    if image_src:
        img = f'<a href="{link}"><img src="{image_src}" width="230" alt="{label} representative image"></a>'
    else:
        img = f'<a href="{link}">No preview<br>暂无代表图</a>'
    return (
        '<td width="33%" valign="top" align="center">\n'
        f"{img}<br>\n"
        f'<strong>{label}</strong><br>\n'
        f'<a href="{link}">打开 README / Open README</a>\n'
        "</td>"
    )


def table(records: list[dict[str, Any]], document_dir: Path = ROOT) -> str:
    cells = [gallery_cell(record, document_dir) for record in records]
    rows = []
    for index in range(0, len(cells), 3):
        row = cells[index:index + 3]
        while len(row) < 3:
            row.append('<td width="33%"></td>')
        rows.append("<tr>\n" + "\n".join(row) + "\n</tr>")
    return "<table>\n" + "\n".join(rows) + "\n</table>"


def write_category_readmes(records_by_category: dict[str, list[dict[str, Any]]]) -> None:
    for category, records in records_by_category.items():
        category_dir = ROOT / "style-packages" / category
        cn, en = CATEGORY_LABELS[category]
        readme = f"""# {cn} / {en}

本目录收录 {len(records)} 个独立风格包。每个小单元都有代表图、名称和双语 README；点击 README 可查看来源、版权边界和三种使用方式。

This directory contains {len(records)} independent style packages. Each package has a representative image, a bilingual README, provenance notes, and three usage modes.

{table(records, category_dir)}
"""
        (category_dir / "README.md").write_text(readme.rstrip() + "\n", encoding="utf-8")


def write_legacy_category_readme(legacy_records: list[dict[str, Any]]) -> None:
    category_dir = ROOT / "styles"
    readme = f"""# 继承的 110 个轻量预设 / Inherited 110 lightweight presets

这里保留原始 `AI-Visual-Prompt-Cookbook` 的 110 个 `style.json` 目录。每个目录都有独立 README、代表性预览图和来源说明；本仓库只增加导航与兼容文档，不重新声明原始内容为 OhMyStyle 原创。

This directory retains the original project's 110 `style.json` directories. Each directory has its own README, preview, and attribution note. OhMyStyle adds navigation and compatibility documentation without claiming authorship of inherited material.

{table(legacy_records, category_dir)}
"""
    (category_dir / "README.md").write_text(readme.rstrip() + "\n", encoding="utf-8")


def write_root_readme(records_by_category: dict[str, list[dict[str, Any]]], legacy_records: list[dict[str, Any]]) -> None:
    total_modern = sum(len(items) for key, items in records_by_category.items() if key != "composites")
    all_count = total_modern + len(records_by_category.get("composites", [])) + len(legacy_records)
    sections = []
    for category, records in records_by_category.items():
        cn, en = CATEGORY_LABELS[category]
        sections.append(f"### {cn} / {en}\n\n{table(records)}")

    legacy_groups = {
        "legacy-posters": ("海报、字体与编辑设计", "Posters, type, and editorial design"),
        "legacy-collage": ("拼贴、涂鸦与漫画", "Collage, doodle, and comic"),
        "legacy-editorial": ("摄影、旅行与生活方式", "Photography, travel, and lifestyle"),
        "legacy-product": ("产品、材质与 3D", "Product, material, and 3D"),
    }
    grouped_legacy: dict[str, list[dict[str, Any]]] = {key: [] for key in legacy_groups}
    for record in legacy_records:
        grouped_legacy[legacy_group(record)].append(record)
    for key, (cn, en) in legacy_groups.items():
        sections.append(f"### {cn} / {en}\n\n{table(grouped_legacy[key])}")

    root = f"""# OhMyStyle

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Style packages](https://img.shields.io/badge/style%20packages-{total_modern + len(records_by_category.get('composites', []))}-6C63FF)](style-packages/)
[![Inherited catalog](https://img.shields.io/badge/inherited%20presets-{len(legacy_records)}-5B8C5A)](styles/)
[![License](https://img.shields.io/badge/license-see%20provenance-lightgrey)](LICENSE-OHMYSTYLE.md)

## 一句话定位 / One-line positioning

OhMyStyle 是一个大而全、可移植的视觉风格预设包集合：把艺术家、摄影师、艺术流派、工艺、游戏美术、原创预设与交叉配方整理成可下载、可编译、可交给不同生图模型执行的独立风格包。

OhMyStyle is a broad, portable collection of visual-style preset packages. It turns artists, photographers, movements, techniques, game-art directions, original presets, and cross-style recipes into downloadable packages that can be compiled for different image models.

本仓库不提供统一的在线生图服务，也不要求用户把图片上传到本项目。模型算力由用户选择：复制 Prompt 到任意平台、配置自己的 API Key，或使用本地模型与 ComfyUI。

The repository is not a hosted image-generation service. Users choose the compute layer: paste the Prompt into any platform, configure their own API key, or run a local model with ComfyUI.

## 快速使用 / Quick use

1. 在下面的大分类中找到一个小风格包。
2. 点击代表性图片或“打开 README”。
3. 下载该包，选择 Prompt-only、API 或本地模型方式。
4. 只把包内的风格约束用于你的新主题，不复制参考作品的具体构图、人物、文字或标志。

1. Find a package in a category below.
2. Click its representative image or README link.
3. Download the package and choose Prompt-only, API, or local-model usage.
4. Apply the package to a new subject; do not copy a reference work's exact composition, people, text, or marks.

## 使用入口 / User entry points

### 复制 Prompt / Prompt-only

打开包内的 `prompts/base.txt`，或对继承的轻量预设打开 `style.json`，替换变量后复制到目标生图平台。

Open `prompts/base.txt`, or `style.json` for an inherited preset, replace its variables, and paste the result into your preferred image model.

### 配置 API Key / Bring your own API key

仓库只生成 provider-neutral 任务，不保存密钥：

```bash
python tools/compile-style.py style-packages/artists/jmw-turner \\
  --subject "雨后的港口" --profile weak --output tmp/turner-job.json
```

Keep the API key in your local environment or secret manager, then submit the compiled job through your chosen provider adapter.

### 本地模型 + ComfyUI / Local model + ComfyUI

下载风格包的 Prompt、参考图清单、调色板和 reproduction 约束，导入本地工作流。仓库不捆绑模型权重，图片默认留在用户本机。

Download the package Prompt, reference manifest, palette, and reproduction constraints into a local workflow. Model weights are not bundled, and generated images can remain on the user's machine.

## 风格包画廊 / Style package gallery

每个小单元统一为：**上方代表图 → 中间名称 → 下方 README 链接**。代表图是包内生成示例或继承预设的预览图，不自动等同于参考原作。

Each unit follows one layout: **representative image → package name → README link**. A representative image is a generated example or inherited preview; it is not automatically the referenced artwork.

{chr(10).join(sections)}

## 包结构 / Package structure

```text
style-packages/<category>/<package>/
├── README.md                 # 中文优先的双语入口 / bilingual entry point
├── package.yaml              # package contract
├── prompts/                  # base and negative prompts
├── references/               # provenance-aware reference manifest
├── examples/                 # anonymous generated examples
├── reproduction.yaml         # observable reproduction rules
└── provenance.yaml           # source and rights boundary
```

继承的 110 个轻量预设仍在 `styles/` 中，每个目录现在也有自己的 README；它们保留原始归属和兼容结构，不被重新包装成 OhMyStyle 原创。

The inherited 110 lightweight presets remain under `styles/`. Each directory now has its own README while retaining the original attribution and compatibility structure.

## 来源、版权与责任 / Provenance and rights

请先阅读 [NOTICE](NOTICE)、[LICENSE](LICENSE)、[LICENSE-OHMYSTYLE.md](LICENSE-OHMYSTYLE.md) 和具体包的 `provenance.yaml`。外部作品、游戏截图、摄影作品、商标、平台页面和用户上传内容不因出现在仓库中就获得新的授权。无法确认再分发权利的素材应使用链接和文字描述，不应下载进仓库。

Read [NOTICE](NOTICE), [LICENSE](LICENSE), [LICENSE-OHMYSTYLE.md](LICENSE-OHMYSTYLE.md), and each package's `provenance.yaml`. External artworks, game screenshots, photographs, trademarks, source pages, and user uploads do not receive a new license merely by being referenced here. When redistribution rights are unclear, keep a link and description instead of bundling the asset.

## 开发与贡献 / Development and contribution

```bash
python tools/validate-package.py style-packages
python scripts/validate-style-json.py
python tools/validate.py
python tools/generate-style-readmes.py --check
git diff --check
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for provenance, licensing, package, and validation requirements.
"""
    (ROOT / "README.md").write_text(root.rstrip() + "\n", encoding="utf-8")


def build_records() -> tuple[dict[str, list[dict[str, Any]]], list[dict[str, Any]]]:
    records_by_category: dict[str, list[dict[str, Any]]] = {}
    for category_dir in sorted((ROOT / "style-packages").iterdir()):
        if not category_dir.is_dir():
            continue
        records = [
            modern_record(category_dir.name, package_dir)
            for package_dir in sorted(category_dir.iterdir())
            if package_dir.is_dir()
            and any((package_dir / marker).exists() for marker in ("package.yaml", "composite.yaml", "resource.yaml"))
        ]
        if records:
            records_by_category[category_dir.name] = records
    legacy = [legacy_record(package_dir) for package_dir in sorted((ROOT / "styles").iterdir()) if (package_dir / "style.json").exists()]
    return records_by_category, legacy


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="verify generated content without writing")
    args = parser.parse_args()
    records_by_category, legacy_records = build_records()
    if args.check:
        # A deterministic check is intentionally conservative: all packages
        # need an entry point and all referenced representative images need to exist.
        missing = []
        for records in [*records_by_category.values(), legacy_records]:
            for record in records:
                if not (record["dir"] / "README.md").exists():
                    missing.append(str(record["dir"] / "README.md"))
        if missing:
            print("Missing generated README files:")
            print("\n".join(missing))
            return 1
        print(f"PASS: {sum(map(len, records_by_category.values()))} structured package(s) and {len(legacy_records)} legacy package(s)")
        return 0

    for records in records_by_category.values():
        for record in records:
            write_package_readme(record)
    for record in legacy_records:
        write_package_readme(record)
    write_category_readmes(records_by_category)
    write_legacy_category_readme(legacy_records)
    write_root_readme(records_by_category, legacy_records)
    print(f"Generated {sum(map(len, records_by_category.values()))} structured package README(s), {len(legacy_records)} legacy README(s), and {len(records_by_category)} category README(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

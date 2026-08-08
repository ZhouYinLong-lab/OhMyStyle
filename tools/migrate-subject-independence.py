#!/usr/bin/env python3
"""Normalize existing packages to the subject-independent prompt contract.

This migration is intentionally conservative: it preserves visual vocabulary,
but removes fixed demo scenes from base prompts and records those examples as
optional rather than mandatory content.
"""

from __future__ import annotations

import argparse
from pathlib import Path


CONTRACT = """SUBJECT INDEPENDENCE CONTRACT:
User subject: {SUBJECT}
User setting: {LOCATION}
The user-supplied subject and setting are authoritative. This package controls
visual treatment only: medium, composition, lighting, palette, surface,
texture, and edge behavior. Do not add a recurring object, setting, character,
landmark, or narrative motif unless the user explicitly requests it. Any
concrete noun used below is optional visual vocabulary, not a default subject.

"""


REPLACEMENTS = {
    "一幅原创的电影化低分辨率像素冒险环境：傍晚海边的小型车站、远处水面和一名匿名旅行者。": "以用户提供的主体和场景生成一幅原创的电影化低分辨率像素冒险图像。",
    "一幅原创的等距像素策略游戏场景：石砌庭院、分层地块、几名匿名小型单位、清晰的行动路径和高低差。": "以用户提供的主体和场景生成一幅原创的等距像素策略游戏图像。",
    "Create a new oil painting of an anonymous courtly or civic encounter in an unfamiliar interior.": "Create a new oil painting of {SUBJECT} in {LOCATION}.",
    "Create a new oil painting of an unfamiliar riverside public garden on a bright afternoon.": "Create a new oil painting of {SUBJECT} in {LOCATION}, under the requested light.",
    "Create a new oil painting of an anonymous everyday action in a quiet seventeenth-century-like interior, without copying any known artwork.": "Create a new oil painting of {SUBJECT} in {LOCATION}, without copying any known artwork.",
    "Create a new Synthetist oil painting of an unfamiliar symbolic gathering beside a river at late afternoon.": "Create a new Synthetist oil painting of {SUBJECT} in {LOCATION}, at the requested time of day.",
    "Create a new historical chronophotographic study of an unfamiliar human movement, such as a craft gesture or athletic preparation.": "Create a new historical chronophotographic study of {SUBJECT}; use motion only when the user requests it.",
    "Create a new anonymous nineteenth-century studio portrait photograph of an adult sitter who is not a recognizable person.": "Create a new anonymous nineteenth-century studio photograph of {SUBJECT}, without making it a recognizable person.",
    "Create a new nineteenth-century documentary photograph of an unfamiliar field camp or roadside work site, not a named historical scene.": "Create a new nineteenth-century documentary photograph of {SUBJECT} in {LOCATION}, not a named historical scene.",
    "一张原创的极简摄影棚静物照片：三个彼此分离的陶瓷物体，在一盏硬质方向光下形成清楚而柔和边缘的投影。": "一张原创的极简摄影棚图像：用户指定的主体在硬质方向光下形成清楚而柔和边缘的投影。",
    "一张原创的低饱和纪实彩色照片：雨后普通街道、旧店面和一辆自行车，自然阴天光，真实表面磨损和轻微曝光不均，取景像偶然观察而非摆拍。": "一张原创的低饱和纪实彩色照片：用户指定的主体和场景采用自然阴天光，真实表现表面磨损和轻微曝光不均，取景像偶然观察而非摆拍。",
    "Create a new photography image with blue-hour residential street, deep navy sky, cool window lights, subtle wet pavement reflections, realistic low light.": "Create a new photography image of {SUBJECT} in {LOCATION}, using blue-hour low light, deep navy atmosphere, cool practical light, and subtle surface reflections.",
    "一张原创的蓝色接触印相平面影像：叶片和种荚作为感光对象排列在手工纸上": "一张原创的蓝色接触印相平面影像：将用户指定的主体作为感光对象排列或呈现在手工纸上",
    "一张原创的两色到三色分色套印海报构成：抽象工具和植物轮廓由不透明油墨分层组成": "一张原创的两色到三色分色套印构成：用户指定的主体由不透明油墨分层组成",
    "Create a new game image with low-poly adventure game environment, angular island, faceted rocks, simple shrine, calm ocean, teal ochre and coral.": "Create a new low-poly adventure game image of {SUBJECT} in {LOCATION}, with faceted forms and a calm teal, ochre, and coral palette.",
    "Create a new game image with side-scrolling platformer pixel art, layered forest platforms, readable silhouettes, bright limited palette, parallax depth.": "Create a new side-scrolling platformer pixel-art image of {SUBJECT} in {LOCATION}, with readable silhouettes, a bright limited palette, and parallax depth.",
    "Create a new game image with top-down 16-bit adventure environment, readable tile grid, compact village path, warm dusk palette, crisp pixel clusters.": "Create a new top-down 16-bit adventure image of {SUBJECT} in {LOCATION}, with a readable tile grid, warm dusk palette, and crisp pixel clusters.",
}


def add_scope_policy(identity: Path) -> None:
    text = identity.read_text(encoding="utf-8")
    if "subject_policy:" in text:
        return
    marker = "scope:\n"
    policy = (
        "scope:\n"
        "  subject_policy: open\n"
        "  subject_note: User-supplied subjects are authoritative; use_cases are optional benchmark labels, not default scene requirements.\n"
    )
    if marker in text:
        text = text.replace(marker, policy, 1)
    else:
        text = text.rstrip() + "\n" + policy
    identity.write_text(text, encoding="utf-8")


def normalize_prompt(prompt: Path) -> None:
    text = prompt.read_text(encoding="utf-8")
    for old, new in REPLACEMENTS.items():
        text = text.replace(old, new)
    if "SUBJECT INDEPENDENCE CONTRACT:" not in text:
        text = CONTRACT + text.lstrip()
    if "{SUBJECT}" not in text and "[SUBJECT]" not in text:
        text = "{SUBJECT}\n\n" + text
    prompt.write_text(text.rstrip() + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path, default=Path("style-packages"))
    args = parser.parse_args()
    root = args.path / "style-packages" if (args.path / "style-packages").is_dir() else args.path
    packages = sorted(path.parent for path in root.resolve().rglob("package.yaml"))
    for package in packages:
        add_scope_policy(package / "identity.yaml")
        normalize_prompt(package / "prompts" / "base.txt")
    print(f"NORMALIZED: {len(packages)} package(s)")


if __name__ == "__main__":
    main()

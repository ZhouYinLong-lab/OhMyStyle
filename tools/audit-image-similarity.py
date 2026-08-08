#!/usr/bin/env python3
"""Build a lightweight, provider-neutral similarity report for gallery images.

This first-pass audit deliberately avoids a large vision model.  It compares
representative images using an average perceptual hash, quantized colour
histograms, luminance, edge density, and a centre-versus-border layout signal.
The result is a review queue, not an automatic merge or deletion decision.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path
from typing import Any, Iterable

import yaml
from PIL import Image


GRID_SIZE = 32
HASH_SIZE = 16
PAIR_LIMIT = 300
DEFAULT_THRESHOLD = 0.82

REVIEW_GROUPS: dict[str, set[str]] = {
    "quiet natural light": {
        "photographers/emilie-hofferber",
        "photographers/rinko-kawauchi",
        "presets/natural-window-light",
    },
    "pixel adventure": {
        "game-art/rpg-maker-pixel-art",
        "game-art/cinematic-pixel-adventure",
    },
    "neon urban game art": {
        "game-art/cyberpunk-night-city",
        "game-art/neon-noir-3d-game-art",
        "game-art/stray-neon-cybercity",
    },
    "modernist geometry": {
        "schools/bauhaus",
        "movements/de-stijl",
        "schools/ulm-school",
        "techniques/grid-3x3",
    },
    "chiaroscuro": {
        "artists/caravaggio",
        "artists/rembrandt",
        "movements/tenebrism",
        "presets/deep-shadow-theater",
    },
}


def discover(root: Path) -> list[Path]:
    root = root.resolve()
    if not root.is_dir():
        raise SystemExit(f"Path does not exist: {root}")
    packages = sorted(path.parent for path in root.rglob("package.yaml"))
    if not packages:
        raise SystemExit(f"No package.yaml found under: {root}")
    return packages


def chunks(values: list[float], width: int) -> Iterable[list[float]]:
    for offset in range(0, len(values), width):
        yield values[offset : offset + width]


def dot(left: list[float], right: list[float]) -> float:
    return sum(a * b for a, b in zip(left, right))


def norm(values: list[float]) -> float:
    return math.sqrt(dot(values, values))


def cosine(left: list[float], right: list[float]) -> float:
    left_norm = norm(left)
    right_norm = norm(right)
    if not left_norm or not right_norm:
        return 0.0
    return max(0.0, min(1.0, dot(left, right) / (left_norm * right_norm)))


def image_features(path: Path) -> dict[str, Any]:
    with Image.open(path) as source:
        image = source.convert("RGB").resize((GRID_SIZE, GRID_SIZE), Image.Resampling.LANCZOS)
    pixels = list(image.get_flattened_data())
    luma = [0.2126 * r + 0.7152 * g + 0.0722 * b for r, g, b in pixels]
    mean_luma = sum(luma) / len(luma)
    mean_rgb = [sum(pixel[channel] for pixel in pixels) / len(pixels) for channel in range(3)]

    hash_grid = image.convert("L").resize((HASH_SIZE, HASH_SIZE), Image.Resampling.BILINEAR)
    hash_values = list(hash_grid.get_flattened_data())
    median = sorted(hash_values)[len(hash_values) // 2]
    average_hash = "".join("1" if value >= median else "0" for value in hash_values)

    histogram = [0.0] * 64
    for r, g, b in pixels:
        index = (r // 64) * 16 + (g // 64) * 4 + (b // 64)
        histogram[index] += 1.0
    histogram = [value / len(pixels) for value in histogram]

    horizontal = [abs(luma[index] - luma[index - 1]) for index in range(1, len(luma)) if index % GRID_SIZE]
    vertical = [abs(luma[index] - luma[index - GRID_SIZE]) for index in range(GRID_SIZE, len(luma))]
    edge_density = (sum(horizontal) + sum(vertical)) / (len(horizontal) + len(vertical)) / 255

    center: list[float] = []
    border: list[float] = []
    for row in range(GRID_SIZE):
        for column in range(GRID_SIZE):
            value = luma[row * GRID_SIZE + column]
            if GRID_SIZE // 4 <= row < GRID_SIZE * 3 // 4 and GRID_SIZE // 4 <= column < GRID_SIZE * 3 // 4:
                center.append(value)
            if row < GRID_SIZE // 8 or row >= GRID_SIZE * 7 // 8 or column < GRID_SIZE // 8 or column >= GRID_SIZE * 7 // 8:
                border.append(value)
    border_mean = sum(border) / len(border)
    center_focus = min(1.0, abs(sum(center) / len(center) - border_mean) / 255)

    return {
        "average_hash": average_hash,
        "color_histogram": histogram,
        "mean_rgb": [round(value, 3) for value in mean_rgb],
        "mean_luma": round(mean_luma, 3),
        "edge_density": round(edge_density, 6),
        "center_focus": round(center_focus, 6),
    }


def hash_similarity(left: str, right: str) -> float:
    distance = sum(a != b for a, b in zip(left, right))
    return 1 - distance / max(1, len(left))


def feature_similarity(left: dict[str, Any], right: dict[str, Any]) -> dict[str, float]:
    histogram = cosine(left["color_histogram"], right["color_histogram"])
    luma = max(0.0, 1 - abs(left["mean_luma"] - right["mean_luma"]) / 255)
    edges = max(0.0, 1 - abs(left["edge_density"] - right["edge_density"]))
    layout = max(0.0, 1 - abs(left["center_focus"] - right["center_focus"]))
    perceptual_hash = hash_similarity(left["average_hash"], right["average_hash"])
    total = (
        0.45 * perceptual_hash
        + 0.25 * histogram
        + 0.10 * luma
        + 0.10 * edges
        + 0.10 * layout
    )
    return {
        "total": round(total, 6),
        "perceptual_hash": round(perceptual_hash, 6),
        "color": round(histogram, 6),
        "luminance": round(luma, 6),
        "texture": round(edges, 6),
        "layout": round(layout, 6),
    }


def review_group(left: str, right: str) -> str | None:
    left = left.removeprefix("style-packages/")
    right = right.removeprefix("style-packages/")
    for label, members in REVIEW_GROUPS.items():
        if left in members and right in members:
            return label
    return None


def package_record(package: Path, repository_root: Path) -> dict[str, Any]:
    package_data = yaml.safe_load((package / "package.yaml").read_text(encoding="utf-8"))
    relative = package.relative_to(repository_root).as_posix()
    image_path = package / "gallery-16x9.jpg"
    record: dict[str, Any] = {
        "package": relative,
        "name": package_data.get("name", package.name) if isinstance(package_data, dict) else package.name,
        "image": image_path.relative_to(repository_root).as_posix(),
    }
    if not image_path.is_file():
        record["error"] = "missing gallery-16x9.jpg"
        return record
    try:
        with Image.open(image_path) as image:
            record["dimensions"] = {"width": image.width, "height": image.height}
            image.verify()
        record["features"] = image_features(image_path)
    except Exception as exc:
        record["error"] = f"unreadable image: {exc}"
    return record


def build_clusters(records: list[dict[str, Any]], pairs: list[dict[str, Any]], threshold: float) -> list[list[str]]:
    parent = {record["package"]: record["package"] for record in records if "features" in record}

    def find(item: str) -> str:
        while parent[item] != item:
            parent[item] = parent[parent[item]]
            item = parent[item]
        return item

    def union(left: str, right: str) -> None:
        left_root, right_root = find(left), find(right)
        if left_root != right_root:
            parent[right_root] = left_root

    for pair in pairs:
        if pair["similarity"]["total"] >= threshold:
            union(pair["left"], pair["right"])
    groups: dict[str, list[str]] = {}
    for package in parent:
        groups.setdefault(find(package), []).append(package)
    return sorted((sorted(group) for group in groups.values() if len(group) > 1), key=lambda group: (-len(group), group))


def write_markdown(path: Path, report: dict[str, Any], clusters: list[list[str]]) -> None:
    lines = [
        "# 代表图相似度审查",
        "",
        "本报告使用感知哈希、颜色分布、明度、边缘密度和中心—边缘布局信号生成。结果只用于人工复核，不自动删除、合并或否定任何风格包。",
        "",
        f"- 包数量：{len(report['packages'])}",
        f"- 比较对数：{report['pair_count']}",
        f"- 审查阈值：`{report['threshold']}`",
        "",
        "## 相似集群",
        "",
    ]
    if not clusters:
        lines.append("未发现超过阈值的相似集群。")
    else:
        for index, cluster in enumerate(clusters, start=1):
            lines.append(f"### 集群 {index}")
            lines.extend(f"- `{package}`" for package in cluster)
            lines.append("")
    lines.extend(["## 最高相似度组合", "", "| 相似度 | 左侧 | 右侧 | 已知复核组 |", "| ---: | --- | --- | --- |"])
    for pair in report["pairs"][:100]:
        lines.append(
            f"| {pair['similarity']['total']:.3f} | `{pair['left']}` | `{pair['right']}` | {pair.get('review_group') or '—'} |"
        )
    lines.extend(["", "## 解释", "", "总分是第一版启发式指标：感知哈希 45%、颜色 25%、明度 10%、纹理 10%、布局 10%。高分表示代表图可能相似，不等于风格包语义重复。"])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path, default=Path("style-packages"))
    parser.add_argument("--threshold", type=float, default=DEFAULT_THRESHOLD)
    parser.add_argument("--json-output", type=Path, default=Path("reports/image-similarity.json"))
    parser.add_argument("--markdown-output", type=Path, default=Path("reports/image-clusters.md"))
    args = parser.parse_args()

    style_root = args.path.resolve()
    repository_root = style_root.parent if style_root.name == "style-packages" else style_root
    records = [package_record(package, repository_root) for package in discover(style_root)]
    errors = [f"{record['package']}: {record['error']}" for record in records if "error" in record]
    usable = [record for record in records if "features" in record]
    pairs: list[dict[str, Any]] = []
    for index, left in enumerate(usable):
        for right in usable[index + 1 :]:
            similarity = feature_similarity(left["features"], right["features"])
            if similarity["total"] >= args.threshold:
                pairs.append(
                    {
                        "left": left["package"],
                        "right": right["package"],
                        "similarity": similarity,
                        "review_group": review_group(left["package"], right["package"]),
                    }
                )
    pairs.sort(key=lambda pair: (-pair["similarity"]["total"], pair["left"], pair["right"]))
    pairs = pairs[:PAIR_LIMIT]
    report = {
        "schema_version": "1.0.0",
        "method": "average perceptual hash + quantized RGB histogram + luminance + edge density + center focus",
        "threshold": args.threshold,
        "package_count": len(records),
        "usable_image_count": len(usable),
        "pair_count": len(usable) * (len(usable) - 1) // 2,
        "candidate_pair_count": len(pairs),
        "errors": errors,
        "packages": records,
        "pairs": pairs,
    }
    clusters = build_clusters(records, pairs, args.threshold)
    report["clusters"] = clusters
    args.json_output.parent.mkdir(parents=True, exist_ok=True)
    args.json_output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(args.markdown_output, report, clusters)
    for pair in pairs[:25]:
        print(f"WARN: {pair['similarity']['total']:.3f} {pair['left']} <> {pair['right']}")
    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        raise SystemExit(1)
    print(f"SUMMARY: {len(records)} packages, {len(pairs)} candidate pairs, {len(clusters)} clusters")


if __name__ == "__main__":
    main()

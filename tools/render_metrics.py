#!/usr/bin/env python3
"""Deterministic, model-free image checks for Style Package render jobs."""

from __future__ import annotations

import math
import re
from pathlib import Path
from typing import Any

from PIL import Image, ImageOps

from style_runtime import choose_pair, load_package


def _luminance(rgb: tuple[int, int, int]) -> float:
    return (0.2126 * rgb[0] + 0.7152 * rgb[1] + 0.0722 * rgb[2]) / 255.0


def _srgb_to_linear(value: int) -> float:
    value /= 255.0
    return value / 12.92 if value <= 0.04045 else ((value + 0.055) / 1.055) ** 2.4


def _lstar(rgb: tuple[int, int, int]) -> float:
    """Approximate CIE L* using sRGB/D65 relative XYZ."""
    red, green, blue = (_srgb_to_linear(channel) for channel in rgb)
    y = 0.2126 * red + 0.7152 * green + 0.0722 * blue
    epsilon = 216 / 24389
    kappa = 24389 / 27
    fy = y ** (1 / 3) if y > epsilon else (kappa * y + 16) / 116
    return 116 * fy - 16


def hex_to_rgb(value: str) -> tuple[int, int, int]:
    value = value.strip().lstrip("#")
    if len(value) != 6:
        raise ValueError(f"Expected a six-digit HEX color, got {value!r}")
    try:
        return tuple(int(value[index : index + 2], 16) for index in (0, 2, 4))  # type: ignore[return-value]
    except ValueError as exc:
        raise ValueError(f"Invalid HEX color: {value!r}") from exc


def _distance(left: tuple[int, int, int], right: tuple[int, int, int]) -> float:
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(left, right))) / 441.673


def _saturation(rgb: tuple[int, int, int]) -> float:
    values = [channel / 255.0 for channel in rgb]
    return max(values) - min(values)


def _pixels(image: Image.Image, limit: int = 256) -> list[tuple[int, int, int]]:
    image = ImageOps.exif_transpose(image).convert("RGB")
    image.thumbnail((limit, limit), Image.Resampling.BILINEAR)
    getter = getattr(image, "get_flattened_data", None)
    return list(getter()) if getter else list(image.getdata())


def _edge_delta(image: Image.Image, limit: int = 256) -> tuple[float, float]:
    image = ImageOps.exif_transpose(image).convert("RGB")
    image.thumbnail((limit, limit), Image.Resampling.BILINEAR)
    width, height = image.size
    getter = getattr(image, "get_flattened_data", None)
    data = list(getter()) if getter else list(image.getdata())
    if width < 2 or height < 2:
        return 0.0, 0.0
    deltas: list[float] = []
    luminances: list[float] = []
    for y in range(height):
        for x in range(width):
            current = data[y * width + x]
            luminances.append(_luminance(current))
            if x + 1 < width:
                deltas.append(_distance(current, data[y * width + x + 1]))
            if y + 1 < height:
                deltas.append(_distance(current, data[(y + 1) * width + x]))
    mean = sum(deltas) / len(deltas)
    average_luma = sum(luminances) / len(luminances)
    variance = sum((value - average_luma) ** 2 for value in luminances) / len(luminances)
    return mean, math.sqrt(variance)


def _percentage_range(value: Any) -> tuple[float, float] | None:
    match = re.fullmatch(r"\s*(\d+(?:\.\d+)?)\s*-\s*(\d+(?:\.\d+)?)_percent\s*", str(value))
    if not match:
        return None
    return float(match.group(1)) / 100.0, float(match.group(2)) / 100.0


def evaluate_image(
    package_path: Path,
    image_path: Path,
    pair_id: str | None = None,
    profile: str = "default",
    color_threshold: float = 0.28,
    dominant_rgb: tuple[int, int, int] | None = None,
    counter_rgb: tuple[int, int, int] | None = None,
    max_lstar_delta: float | None = None,
) -> dict[str, Any]:
    runtime = load_package(package_path)
    if (dominant_rgb is None) != (counter_rgb is None):
        raise ValueError("dominant_rgb and counter_rgb must be supplied together")
    if dominant_rgb is None:
        pair = choose_pair(runtime, pair_id)
        dominant = tuple(pair["dominant"]["rgb"])
        counter = tuple(pair["counter"]["rgb"])
    else:
        pair = {"id": "custom", "dominant": {"rgb": list(dominant_rgb)}, "counter": {"rgb": list(counter_rgb)}}
        dominant = dominant_rgb
        counter = counter_rgb
    with Image.open(image_path) as opened:
        image = ImageOps.exif_transpose(opened).convert("RGB")
        pixels = _pixels(image)
        mean_edge_delta, global_luma_std = _edge_delta(image)

    dominant_pixels: list[tuple[int, int, int]] = []
    counter_pixels: list[tuple[int, int, int]] = []
    unassigned_high_chroma = 0
    for pixel in pixels:
        dominant_distance = _distance(pixel, dominant)
        counter_distance = _distance(pixel, counter)
        if min(dominant_distance, counter_distance) <= color_threshold:
            if dominant_distance <= counter_distance:
                dominant_pixels.append(pixel)
            else:
                counter_pixels.append(pixel)
        elif _saturation(pixel) >= 0.48:
            unassigned_high_chroma += 1

    total = max(len(pixels), 1)
    dominant_share = len(dominant_pixels) / total
    counter_share = len(counter_pixels) / total
    pair_coverage = dominant_share + counter_share
    dominant_luma = sum(_luminance(pixel) for pixel in dominant_pixels) / max(len(dominant_pixels), 1)
    counter_luma = sum(_luminance(pixel) for pixel in counter_pixels) / max(len(counter_pixels), 1)
    luminance_delta = abs(dominant_luma - counter_luma) if dominant_pixels and counter_pixels else 1.0
    dominant_lstar = sum(_lstar(pixel) for pixel in dominant_pixels) / max(len(dominant_pixels), 1)
    counter_lstar = sum(_lstar(pixel) for pixel in counter_pixels) / max(len(counter_pixels), 1)
    lstar_delta = abs(dominant_lstar - counter_lstar) if dominant_pixels and counter_pixels else 100.0

    profile_data = runtime["evaluation"].get("profiles", {}).get(profile, {})
    lstar_limit = max_lstar_delta if max_lstar_delta is not None else profile_data.get("max_lstar_delta")
    area_rules = runtime["reproduction"].get("area_ratio", {})
    dominant_range = _percentage_range(area_rules.get("dominant_color", ""))
    counter_range = _percentage_range(area_rules.get("counter_color", ""))
    area_ratio_pass = True
    if profile_data.get("enforce_area_ratio") and dominant_range and counter_range:
        area_ratio_pass = (
            dominant_range[0] <= dominant_share <= dominant_range[1]
            and counter_range[0] <= counter_share <= counter_range[1]
        )
    checks = {
        "pair_coverage": {
            "value": round(pair_coverage, 4),
            "minimum": profile_data.get("min_pair_coverage", 0.0),
            "pass": pair_coverage >= float(profile_data.get("min_pair_coverage", 0.0)),
        },
        "unassigned_high_chroma": {
            "value": round(unassigned_high_chroma / total, 4),
            "maximum": profile_data.get("max_unassigned_high_chroma", 1.0),
            "pass": unassigned_high_chroma / total <= float(profile_data.get("max_unassigned_high_chroma", 1.0)),
        },
        "area_ratio": {
            "dominant_share": round(dominant_share, 4),
            "counter_share": round(counter_share, 4),
            "dominant_range": dominant_range,
            "counter_range": counter_range,
            "pass": area_ratio_pass,
        },
        "luminance_delta": {
            "value": round(luminance_delta, 4),
            "maximum": profile_data.get("max_luminance_delta"),
            "pass": profile_data.get("max_luminance_delta") is None
            or luminance_delta <= float(profile_data["max_luminance_delta"]),
        },
        "lstar_delta": {
            "value": round(lstar_delta, 4),
            "maximum": lstar_limit,
            "pass": lstar_limit is None or lstar_delta <= float(lstar_limit),
        },
        "mean_edge_delta": {
            "value": round(mean_edge_delta, 4),
            "maximum": profile_data.get("max_mean_edge_delta"),
            "pass": profile_data.get("max_mean_edge_delta") is None
            or mean_edge_delta <= float(profile_data["max_mean_edge_delta"]),
        },
    }
    return {
        "image": str(image_path.resolve()),
        "package": runtime["package"].get("id"),
        "pair": pair["id"],
        "profile": profile,
        "image_size": list(image.size),
        "metrics": {
            "dominant_share": round(dominant_share, 4),
            "counter_share": round(counter_share, 4),
            "pair_coverage": round(pair_coverage, 4),
            "dominant_luminance": round(dominant_luma, 4),
            "counter_luminance": round(counter_luma, 4),
            "luminance_delta": round(luminance_delta, 4),
            "dominant_lstar": round(dominant_lstar, 4),
            "counter_lstar": round(counter_lstar, 4),
            "lstar_delta": round(lstar_delta, 4),
            "mean_edge_delta": round(mean_edge_delta, 4),
            "global_luminance_std": round(global_luma_std, 4),
            "unassigned_high_chroma": round(unassigned_high_chroma / total, 4),
        },
        "checks": checks,
        "status": "pass" if all(item["pass"] for item in checks.values()) else "fail",
        "interpretation": "Screening metrics only; semantic object identity and artistic quality still require human review.",
    }

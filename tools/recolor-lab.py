#!/usr/bin/env python3
"""Deterministically recolor a masked region in CIELAB while preserving texture."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageOps

from render_metrics import hex_to_rgb


EPSILON = 216 / 24389
KAPPA = 24389 / 27


def _pivot(value: float) -> float:
    return value ** (1 / 3) if value > EPSILON else (KAPPA * value + 16) / 116


def _inverse_pivot(value: float) -> float:
    cube = value**3
    return cube if cube > EPSILON else (116 * value - 16) / KAPPA


def rgb_to_lab(rgb: tuple[int, int, int]) -> tuple[float, float, float]:
    channels = []
    for channel in rgb:
        value = channel / 255.0
        channels.append(value / 12.92 if value <= 0.04045 else ((value + 0.055) / 1.055) ** 2.4)
    red, green, blue = channels
    x = (0.4124564 * red + 0.3575761 * green + 0.1804375 * blue) / 0.95047
    y = 0.2126729 * red + 0.7151522 * green + 0.0721750 * blue
    z = (0.0193339 * red + 0.1191920 * green + 0.9503041 * blue) / 1.08883
    fx, fy, fz = _pivot(x), _pivot(y), _pivot(z)
    return 116 * fy - 16, 500 * (fx - fy), 200 * (fy - fz)


def lab_to_rgb(lab: tuple[float, float, float]) -> tuple[int, int, int]:
    lightness, a, b = lab
    fy = (lightness + 16) / 116
    fx = fy + a / 500
    fz = fy - b / 200
    x, y, z = _inverse_pivot(fx) * 0.95047, _inverse_pivot(fy), _inverse_pivot(fz) * 1.08883
    red = 3.2404542 * x - 1.5371385 * y - 0.4985314 * z
    green = -0.9692660 * x + 1.8760108 * y + 0.0415560 * z
    blue = 0.0556434 * x - 0.2040259 * y + 1.0572252 * z
    values = []
    for channel in (red, green, blue):
        channel = 12.92 * channel if channel <= 0.0031308 else 1.055 * channel ** (1 / 2.4) - 0.055
        values.append(max(0, min(255, round(channel * 255))))
    return tuple(values)  # type: ignore[return-value]


def recolor(input_path: Path, output_path: Path, mask_path: Path, target_hex: str, texture_strength: float) -> None:
    if not 0 <= texture_strength <= 1:
        raise ValueError("texture-strength must be between 0 and 1")
    with Image.open(input_path) as source, Image.open(mask_path) as mask_source:
        image = ImageOps.exif_transpose(source).convert("RGB")
        mask = ImageOps.exif_transpose(mask_source).convert("L")
        if mask.size != image.size:
            raise ValueError(f"Mask size {mask.size} does not match image size {image.size}")
        pixels = list(image.getdata())
        mask_values = list(mask.getdata())
        target_lab = rgb_to_lab(hex_to_rgb(target_hex))
        region_labs = [rgb_to_lab(pixel) for pixel, level in zip(pixels, mask_values) if level >= 128]
        if not region_labs:
            raise ValueError("Mask contains no active pixels")
        mean_l = sum(lab[0] for lab in region_labs) / len(region_labs)
        output_pixels = []
        for pixel, level in zip(pixels, mask_values):
            if level < 128:
                output_pixels.append(pixel)
                continue
            current_l = rgb_to_lab(pixel)[0]
            adjusted_l = target_lab[0] + texture_strength * (current_l - mean_l)
            output_pixels.append(lab_to_rgb((adjusted_l, target_lab[1], target_lab[2])))
        result = Image.new("RGB", image.size)
        result.putdata(output_pixels)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        result.save(output_path)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--mask", required=True, type=Path, help="Grayscale mask; white pixels are recolored")
    parser.add_argument("--target-hex", required=True)
    parser.add_argument("--texture-strength", type=float, default=0.12)
    args = parser.parse_args()
    recolor(args.input, args.output, args.mask, args.target_hex, args.texture_strength)
    print(f"WROTE: {args.output}")


if __name__ == "__main__":
    main()

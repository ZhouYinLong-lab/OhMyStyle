#!/usr/bin/env python3
"""Deterministically recolor a masked region in CIELAB while preserving texture."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageOps

from color_science import lab_to_rgb, rgb_to_lab
from render_metrics import hex_to_rgb

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

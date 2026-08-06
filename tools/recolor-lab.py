#!/usr/bin/env python3
"""Deterministically recolor a masked region in CIELAB while preserving texture."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageOps

from color_science import lab_to_rgb, rgb_to_lab
from image_limits import ensure_working_size
from render_metrics import hex_to_rgb


def recolor(input_path: Path, output_path: Path, mask_path: Path, target_hex: str, texture_strength: float) -> None:
    if not 0 <= texture_strength <= 1:
        raise ValueError("texture-strength must be between 0 and 1")
    with Image.open(input_path) as source, Image.open(mask_path) as mask_source:
        oriented_image = ImageOps.exif_transpose(source)
        oriented_mask = ImageOps.exif_transpose(mask_source)
        if oriented_mask.size != oriented_image.size:
            raise ValueError(f"Mask size {oriented_mask.size} does not match image size {oriented_image.size}")
        ensure_working_size(oriented_image.size, "recolor image")
        image = oriented_image.convert("RGB")
        mask = oriented_mask.convert("L")
        target_lab = rgb_to_lab(hex_to_rgb(target_hex))
        image_pixels = image.load()
        mask_pixels = mask.load()
        total_l = 0.0
        active_pixels = 0
        for y in range(image.height):
            for x in range(image.width):
                if mask_pixels[x, y] >= 128:
                    total_l += rgb_to_lab(image_pixels[x, y])[0]
                    active_pixels += 1
        if not active_pixels:
            raise ValueError("Mask contains no active pixels")
        mean_l = total_l / active_pixels
        output_pixels = Image.new("RGB", image.size)
        output_data = output_pixels.load()
        for y in range(image.height):
            for x in range(image.width):
                pixel = image_pixels[x, y]
                if mask_pixels[x, y] < 128:
                    output_data[x, y] = pixel
                    continue
                current_l = rgb_to_lab(pixel)[0]
                adjusted_l = target_lab[0] + texture_strength * (current_l - mean_l)
                output_data[x, y] = lab_to_rgb((adjusted_l, target_lab[1], target_lab[2]))
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_pixels.save(output_path)


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

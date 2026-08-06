#!/usr/bin/env python3
"""Small dependency-free sRGB/CIELAB conversion helpers shared by tools."""

from __future__ import annotations


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

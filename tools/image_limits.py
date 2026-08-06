"""Shared resource limits for deterministic image processing."""

from __future__ import annotations

from typing import Iterable


# 4K images are below this limit; very large inputs are rejected before the
# mask/recolor pipeline can allocate several full-resolution working buffers.
MAX_WORKING_PIXELS = 25_000_000


def ensure_working_size(size: Iterable[int], label: str = "image") -> None:
    width, height = (int(value) for value in size)
    pixels = width * height
    if pixels > MAX_WORKING_PIXELS:
        raise ValueError(
            f"{label} is {width}x{height} ({pixels:,} pixels), above the safe "
            f"processing limit of {MAX_WORKING_PIXELS:,} pixels"
        )

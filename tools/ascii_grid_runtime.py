"""Rasterize literal ASCII source cells; never synthesize scene geometry."""

from __future__ import annotations

import hashlib
import io
import json
import platform
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from PIL import Image, ImageDraw, ImageFont, __version__ as pillow_version

from art_direction_runtime import validate_grid
from compiled_job_runtime import validate_compiled_job


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_grid(raw: bytes, columns: int, rows: int) -> list[str]:
    """Accept printable ASCII and LF/CRLF only, preserving leading spaces."""
    try:
        source = raw.decode("ascii").replace("\r\n", "\n")
    except UnicodeDecodeError as error:
        raise ValueError("Grid source must contain ASCII characters only") from error
    if any(char != "\n" and not 32 <= ord(char) <= 126 for char in source):
        raise ValueError("Grid source contains tabs or unsupported control characters")
    # A terminal newline is optional; blank scene rows still count.
    lines = source.removesuffix("\n").split("\n")
    if len(lines) != rows:
        raise ValueError(f"Expected {rows} rows, received {len(lines)}")
    if any(len(line) > columns for line in lines):
        raise ValueError(f"Grid rows must not exceed {columns} columns")
    if not any(line.strip() for line in lines):
        raise ValueError("Grid source cannot be entirely blank")
    return [line.ljust(columns) for line in lines]


def render_grid_job(
    job: dict[str, Any], source_path: Path, font_path: Path, output: Path
) -> dict[str, Any]:
    """Create a lossless image and the source/configuration needed to reproduce it."""
    validate_compiled_job(job)
    execution = job.get("execution", {})
    if job.get("job_type") != "ascii_grid_construction" or execution.get("route") != "deterministic_grid":
        raise ValueError("This renderer requires an ASCII grid construction job")
    grid = execution.get("grid", {})
    validate_grid(grid)
    raw = source_path.read_bytes()
    lines = read_grid(raw, grid["columns"], grid["rows"])
    font_bytes = font_path.read_bytes()
    # Load the hashed bytes, so font identity and rendered data cannot diverge.
    font = ImageFont.truetype(io.BytesIO(font_bytes), size=grid["font_size"])
    glyphs = [chr(value) for value in range(32, 127)]
    advances = [font.getlength(char) for char in glyphs]
    if max(advances) - min(advances) > 0.01:
        raise ValueError("An explicitly selected monospace font is required")
    cell_width = (grid["width"] - 2 * grid["margin"]) / grid["columns"]
    cell_height = (grid["height"] - 2 * grid["margin"]) / grid["rows"]
    boxes = [font.getbbox(char, anchor="ls") for char in glyphs if char != " "]
    left = min(box[0] for box in boxes)
    top = min(box[1] for box in boxes)
    right = max(box[2] for box in boxes)
    bottom = max(box[3] for box in boxes)
    if max(advances[0], right - left) > int(cell_width) or bottom - top > int(cell_height):
        raise ValueError("Font glyphs do not fit the configured cells; reduce font_size or grid density")
    x_offset = (int(cell_width) - (right - left)) // 2 - left
    y_offset = (int(cell_height) - (bottom - top)) // 2 - top
    image = Image.new("RGB", (grid["width"], grid["height"]), grid["background"])
    draw = ImageDraw.Draw(image)
    occupied = 0
    for row, line in enumerate(lines):
        for column, char in enumerate(line):
            if char == " ":
                continue
            color = grid["glyph_colors"].get(char, grid["foreground"])
            if color.lower() == grid["background"].lower():
                raise ValueError(f"Glyph {char!r} is invisible against the background")
            draw.text(
                (grid["margin"] + int(column * cell_width) + x_offset,
                 grid["margin"] + int(row * cell_height) + y_offset),
                char, font=font, fill=color, anchor="ls",
            )
            occupied += 1
    normalized = ("\n".join(lines) + "\n").encode("ascii")
    image_buffer = io.BytesIO()
    image.save(image_buffer, format="PNG")
    image_bytes = image_buffer.getvalue()
    record = {
        "schema_version": "1.0.0",
        "route": "deterministic_grid",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "subject": job.get("subject"),
        "art_direction": job.get("art_direction"),
        "grid": grid,
        "occupied_cells": occupied,
        "source": {"path": str(source_path.resolve()), "sha256": sha256(raw),
                   "normalized_sha256": sha256(normalized)},
        "font": {"path": str(font_path.resolve()), "sha256": sha256(font_bytes),
                 "name": list(font.getname())},
        "renderer": {"sha256": sha256(Path(__file__).read_bytes()),
                     "pillow": pillow_version, "python": platform.python_version(),
                     "cell_width": cell_width, "cell_height": cell_height,
                     "anchor": "ls", "glyph_offset": [x_offset, y_offset]},
        "output": {"file": "master.png", "sha256": sha256(image_bytes),
                   "rgb_pixels_sha256": sha256(image.tobytes())},
        "review": {"status": "pending", "note": "Literal construction does not establish scene readability or style quality."},
    }
    # Require a fresh directory; never replace an earlier render or its evidence.
    output.mkdir(parents=True, exist_ok=False)
    (output / "master.png").write_bytes(image_bytes)
    (output / "source_grid.txt").write_bytes(normalized)
    (output / "render_record.json").write_text(
        json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return record

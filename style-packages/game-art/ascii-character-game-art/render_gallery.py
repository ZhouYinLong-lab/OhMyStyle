#!/usr/bin/env python3
"""Render the ASCII gallery image from its literal, fixed-width character grid."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "examples" / "ascii-cave-grid.txt"
OUTPUT = ROOT / "gallery-16x9.jpg"
WIDTH, HEIGHT = 1280, 720
ROWS = 36
BACKGROUND = (10, 14, 19)

PALETTE = {
    "rock": (116, 130, 139),
    "detail": (83, 101, 112),
    "ground": (147, 119, 79),
    "light": (241, 184, 91),
    "torch": (255, 219, 137),
    "player": (194, 210, 218),
}


def glyph_color(char: str, row: int) -> tuple[int, int, int]:
    """Choose ink for a cell; the glyph itself always carries the visible shape."""
    if char in "*+":
        return PALETTE["torch"]
    if char in "@Oo":
        return PALETTE["player"]
    if char in "#":
        return PALETTE["rock"] if row < 31 else PALETTE["ground"]
    if char in ".,:;'`":
        return PALETTE["light"] if row >= 23 else PALETTE["detail"]
    if char in "_|/\\(){}[]<>^-=":
        return PALETTE["detail"]
    return PALETTE["rock"]


def main() -> None:
    rows = SOURCE.read_text(encoding="ascii").splitlines()
    if len(rows) != ROWS:
        raise ValueError(f"Expected {ROWS} rows, got {len(rows)}")
    if any(len(row) > 100 for row in rows):
        raise ValueError("A grid row exceeds the 100-column canvas")
    if any(not char.isprintable() or ord(char) > 127 for row in rows for char in row):
        raise ValueError("The source grid must contain printable ASCII characters only")

    font_candidates = [
        Path(r"C:\Windows\Fonts\consola.ttf"),
        Path(r"C:\Windows\Fonts\CascadiaMono.ttf"),
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"),
        Path("/Library/Fonts/Menlo.ttc"),
    ]
    font_path = next((candidate for candidate in font_candidates if candidate.exists()), None)
    if font_path is None:
        raise FileNotFoundError("Install a monospaced font (Consolas, Cascadia Mono, DejaVu Sans Mono, or Menlo)")
    font = ImageFont.truetype(str(font_path), 19)
    image = Image.new("RGB", (WIDTH, HEIGHT), BACKGROUND)
    draw = ImageDraw.Draw(image)

    cell_width = font.getlength("M")
    occupied = [x for row in rows for x, char in enumerate(row) if char != " "]
    content_left, content_right = min(occupied), max(occupied) + 1
    content_width = (content_right - content_left) * cell_width
    x_offset = (WIDTH - content_width) / 2 - content_left * cell_width
    cell_height = HEIGHT / ROWS
    for y, row in enumerate(rows):
        for x, char in enumerate(row.ljust(100)):
            if char == " ":
                continue
            draw.text(
                (round(x_offset + x * cell_width), round(y * cell_height)),
                char,
                font=font,
                fill=glyph_color(char, y),
            )

    image.save(OUTPUT, format="JPEG", quality=94, subsampling=0)
    print(f"Rendered {OUTPUT} from {SOURCE} ({len(rows)} x 100 character cells)")


if __name__ == "__main__":
    main()

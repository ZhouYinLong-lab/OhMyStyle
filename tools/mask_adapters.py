#!/usr/bin/env python3
"""Provider-neutral model masks plus conservative CIELAB color segmentation."""

from __future__ import annotations

import hashlib
import json
import math
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Mapping

from PIL import Image, ImageChops, ImageFilter, ImageOps

from color_science import rgb_to_lab
from image_limits import ensure_working_size
from render_metrics import hex_to_rgb


@dataclass(frozen=True)
class MaskRequest:
    image_path: Path
    target_hex: str
    role: str = "subject"
    safety_profile: str = "generic"
    lab_radius: float = 24.0
    lstar_tolerance: float | None = None
    min_component_area: int = 64
    protected_classes: tuple[str, ...] = ()
    exclude_specular: bool = True
    border_connected_is_background: bool = True
    min_coverage: float = 0.002
    max_coverage: float = 0.85
    fail_closed: bool = True


@dataclass
class MaskResult:
    mask: Image.Image
    reflection_mask: Image.Image
    status: str
    confidence: float
    reasons: list[str] = field(default_factory=list)
    metrics: dict[str, Any] = field(default_factory=dict)
    provenance: dict[str, Any] = field(default_factory=dict)


class MaskAdapterError(ValueError):
    pass


def _pixel_data(image: Image.Image):
    getter = getattr(image, "get_flattened_data", None)
    return getter() if getter else image.getdata()


def _count_active(image: Image.Image, threshold: int = 128) -> int:
    return sum(value >= threshold for value in _pixel_data(image))


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _load_mask(path: Path, size: tuple[int, int]) -> Image.Image:
    if not path.exists():
        raise MaskAdapterError(f"Mask file does not exist: {path}")
    with Image.open(path) as source:
        image = ImageOps.exif_transpose(source).convert("L")
    if image.size != size:
        raise MaskAdapterError(f"Mask size {image.size} does not match image size {size}: {path}")
    return image


class FileSegmentationAdapter:
    """Load same-image semantic masks exported by any provider."""

    name = "file-segmentation-manifest"

    def __init__(self, manifest_path: Path, image_path: Path) -> None:
        self.manifest_path = manifest_path
        self.image_path = image_path
        payload = json.loads(manifest_path.read_text(encoding="utf-8"))
        if not isinstance(payload, dict) or not isinstance(payload.get("classes"), dict):
            raise MaskAdapterError("Segmentation manifest must contain an object field: classes")
        image_sha256 = payload.get("image_sha256")
        if not isinstance(image_sha256, str) or not image_sha256.strip():
            raise MaskAdapterError("Segmentation manifest must contain image_sha256 for same-image binding")
        if image_sha256 != _sha256(image_path):
            raise MaskAdapterError("Segmentation manifest image_sha256 does not match the input image")
        with Image.open(image_path) as source:
            size = ImageOps.exif_transpose(source).size
        ensure_working_size(size, "segmentation image")
        manifest_root = manifest_path.resolve().parent
        self._masks: dict[str, Image.Image] = {}
        for class_name, raw_path in payload["classes"].items():
            if not isinstance(class_name, str) or not isinstance(raw_path, str):
                raise MaskAdapterError("Manifest classes must map strings to mask paths")
            if Path(raw_path).is_absolute():
                raise MaskAdapterError(f"Manifest mask path must be relative: {raw_path!r}")
            candidate = (manifest_root / raw_path).resolve()
            try:
                candidate.relative_to(manifest_root)
            except ValueError as exc:
                raise MaskAdapterError(f"Manifest mask path escapes manifest directory: {raw_path!r}") from exc
            self._masks[class_name] = _load_mask(candidate, size)

    @property
    def classes(self) -> tuple[str, ...]:
        return tuple(sorted(self._masks))

    def get(self, class_name: str) -> Image.Image | None:
        return self._masks.get(class_name)

    def require(self, class_names: tuple[str, ...]) -> dict[str, Image.Image]:
        missing = [name for name in class_names if name not in self._masks]
        if missing:
            raise MaskAdapterError(f"Segmentation manifest is missing protected classes: {', '.join(missing)}")
        return {name: self._masks[name] for name in class_names}


def _lab_distance(left: tuple[float, float, float], right: tuple[float, float, float]) -> float:
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(left, right)))


def _binary(mask: Image.Image, threshold: int = 128) -> Image.Image:
    return mask.point(lambda value: 255 if value >= threshold else 0, mode="L")


def _remove_small_components(mask: Image.Image, min_area: int) -> Image.Image:
    width, height = mask.size
    pixels = mask.load()
    visited: set[tuple[int, int]] = set()
    output = Image.new("L", mask.size, 0)
    out = output.load()
    for y in range(height):
        for x in range(width):
            if pixels[x, y] == 0 or (x, y) in visited:
                continue
            stack = [(x, y)]
            visited.add((x, y))
            component: list[tuple[int, int]] = []
            while stack:
                cx, cy = stack.pop()
                component.append((cx, cy))
                for nx, ny in ((cx - 1, cy), (cx + 1, cy), (cx, cy - 1), (cx, cy + 1)):
                    if 0 <= nx < width and 0 <= ny < height and pixels[nx, ny] and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        stack.append((nx, ny))
            if len(component) >= min_area:
                for px, py in component:
                    out[px, py] = 255
    return output


def _border_connected(mask: Image.Image) -> Image.Image:
    width, height = mask.size
    pixels = mask.load()
    visited: set[tuple[int, int]] = set()
    stack = [(x, 0) for x in range(width)] + [(x, height - 1) for x in range(width)]
    stack += [(0, y) for y in range(height)] + [(width - 1, y) for y in range(height)]
    while stack:
        x, y = stack.pop()
        if (x, y) in visited or pixels[x, y] == 0:
            continue
        visited.add((x, y))
        for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
            if 0 <= nx < width and 0 <= ny < height:
                stack.append((nx, ny))
    result = Image.new("L", mask.size, 0)
    result.putdata(bytearray(255 if (x, y) in visited else 0 for y in range(height) for x in range(width)))
    return result


def _specular_candidates(image: Image.Image) -> Image.Image:
    mask = Image.new("L", image.size, 0)
    mask.putdata(bytearray(
        255 if lightness >= 78 and math.hypot(a, b) <= 60 else 0
        for lightness, a, b in (rgb_to_lab(pixel) for pixel in _pixel_data(image))
    ))
    return mask.filter(ImageFilter.MaxFilter(3))


def segment_by_color(request: MaskRequest, protected_masks: Mapping[str, Image.Image] | None = None) -> MaskResult:
    """Intersect Lab color seeds with protected semantic masks and safety gates."""
    with Image.open(request.image_path) as source:
        oriented = ImageOps.exif_transpose(source)
        ensure_working_size(oriented.size, "mask image")
        image = oriented.convert("RGB")
    target_lab = rgb_to_lab(hex_to_rgb(request.target_hex))
    specular = _specular_candidates(image)
    initial = Image.new("L", image.size)
    def candidate_values():
        for pixel in _pixel_data(image):
            lab = rgb_to_lab(pixel)
            distance = _lab_distance(lab, target_lab)
            in_lstar = request.lstar_tolerance is None or abs(lab[0] - target_lab[0]) <= request.lstar_tolerance
            yield 255 if distance <= request.lab_radius and in_lstar else 0

    initial.putdata(bytearray(candidate_values()))

    protected = Image.new("L", image.size, 0)
    missing_protected: list[str] = []
    for class_name in request.protected_classes:
        class_mask = (protected_masks or {}).get(class_name)
        if class_mask is None:
            missing_protected.append(class_name)
            continue
        protected = ImageChops.lighter(protected, _binary(class_mask))
    protected_overlap = ImageChops.multiply(initial, protected)
    safe = ImageChops.subtract(initial, protected)
    excluded_specular = ImageChops.multiply(safe, specular) if request.exclude_specular else Image.new("L", image.size, 0)
    safe = ImageChops.subtract(safe, excluded_specular)
    if request.border_connected_is_background and request.role != "background":
        safe = ImageChops.subtract(safe, _border_connected(safe))
    safe = safe.filter(ImageFilter.MinFilter(3)).filter(ImageFilter.MaxFilter(3))
    safe = _remove_small_components(safe, request.min_component_area)

    active = _count_active(safe)
    initial_count = _count_active(initial)
    protected_count = _count_active(protected_overlap)
    specular_count = _count_active(excluded_specular)
    total = image.width * image.height
    coverage = active / total if total else 0
    protected_ratio = protected_count / initial_count if initial_count else 0
    specular_ratio = specular_count / initial_count if initial_count else 0
    reasons: list[str] = []
    if request.safety_profile == "person" and not request.protected_classes:
        reasons.append("person safety profile requires protected_classes")
    if missing_protected:
        reasons.append(f"missing protected semantic masks: {', '.join(missing_protected)}")
    if request.safety_profile == "reflective" and not request.exclude_specular:
        reasons.append("reflective safety profile requires exclude_specular=true")
    if coverage < request.min_coverage:
        reasons.append(f"active mask coverage {coverage:.4f} is below {request.min_coverage:.4f}")
    if coverage > request.max_coverage:
        reasons.append(f"active mask coverage {coverage:.4f} is above {request.max_coverage:.4f}")
    if protected_ratio > 0:
        reasons.append(f"target-color seeds overlap protected regions by {protected_ratio:.2%}")
    if request.safety_profile == "reflective" and specular_ratio > 0.35:
        reasons.append(f"specular candidates consume {specular_ratio:.2%} of target-color seeds")
    if request.safety_profile == "reflective" and initial_count and active / initial_count < 0.35:
        reasons.append("less than 35% of target-color seeds remain after reflection and boundary safety gates")
    status = "ready" if not reasons else ("needs_review" if not request.fail_closed else "rejected")
    confidence = max(0.0, min(1.0, (active / initial_count if initial_count else 0) * (1 - protected_ratio)))
    return MaskResult(
        mask=safe,
        # Keep the full candidate map for inspection; excluded_specular is
        # only the overlap with target-color seeds used by the safety gates.
        reflection_mask=specular,
        status=status,
        confidence=round(confidence, 4),
        reasons=reasons,
        metrics={
            "image_size": [image.width, image.height],
            "target_hex": request.target_hex,
            "target_lab": [round(value, 4) for value in target_lab],
            "initial_pixels": initial_count,
            "active_pixels": active,
            "coverage": round(coverage, 6),
            "protected_overlap_pixels": protected_count,
            "protected_overlap_ratio": round(protected_ratio, 6),
            "excluded_specular_pixels": specular_count,
            "excluded_specular_ratio": round(specular_ratio, 6),
            "reflection_candidates": _count_active(specular),
        },
        provenance={
            "adapter": "color-threshold-lab",
            "safety_profile": request.safety_profile,
            "role": request.role,
            "lab_radius": request.lab_radius,
            "lstar_tolerance": request.lstar_tolerance,
            "protected_classes": list(request.protected_classes),
            "fail_closed": request.fail_closed,
        },
    )

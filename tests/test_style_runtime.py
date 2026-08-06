from __future__ import annotations

import sys
import tempfile
import unittest
import importlib.util
import hashlib
import io
import json
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from render_metrics import evaluate_image, hex_to_rgb  # noqa: E402
from mask_adapters import FileSegmentationAdapter, MaskRequest, MaskAdapterError, segment_by_color  # noqa: E402

_preflight_spec = importlib.util.spec_from_file_location("preflight_render", ROOT / "tools/preflight-render.py")
assert _preflight_spec and _preflight_spec.loader
_preflight_module = importlib.util.module_from_spec(_preflight_spec)
_preflight_spec.loader.exec_module(_preflight_module)
build_plan = _preflight_module.build_plan
load_task = _preflight_module.load_task

_recolor_spec = importlib.util.spec_from_file_location("recolor_lab", ROOT / "tools/recolor-lab.py")
assert _recolor_spec and _recolor_spec.loader
_recolor_module = importlib.util.module_from_spec(_recolor_spec)
_recolor_spec.loader.exec_module(_recolor_module)
rgb_to_lab = _recolor_module.rgb_to_lab
lab_to_rgb = _recolor_module.lab_to_rgb
from style_runtime import compile_job, load_package, manifest_records, select_references  # noqa: E402
from safe_yaml import safe_load  # noqa: E402
from image_limits import ensure_working_size  # noqa: E402


PACKAGE = ROOT / "style-packages/presets/high-chroma-color-pairing"


class StyleRuntimeTests(unittest.TestCase):
    def test_custom_hex_colors_are_supported(self) -> None:
        self.assertEqual(hex_to_rgb("#0070FC"), (0, 112, 252))
        self.assertEqual(hex_to_rgb("C85400"), (200, 84, 0))

    def test_preflight_blocks_exact_luminance_task_from_model_only(self) -> None:
        task = load_task(ROOT / "tasks/same-luminance-portrait.yaml")
        plan = build_plan(task)
        self.assertEqual(plan["status"], "ready_for_generation")
        self.assertFalse(plan["model_only_allowed"])
        self.assertEqual(plan["strategy"], "hybrid_model_plus_deterministic_postprocess")
        self.assertAlmostEqual(plan["colors"]["shirt"]["lstar"], plan["colors"]["background"]["lstar"], places=2)

    def test_preflight_blocks_unsafe_mask_profile_declarations(self) -> None:
        task = {
            "id": "unsafe-mask-task",
            "subject": "portrait",
            "output": {"aspect_ratio": "1:1"},
            "constraints": {
                "masking": {
                    "required": True,
                    "targets": [{"id": "shirt", "target_hex": "#0070FC", "role": "subject", "safety_profile": "person"}],
                }
            },
        }
        plan = build_plan(task)
        self.assertEqual(plan["status"], "blocked_until_resolved")
        self.assertIn("protected_classes", plan["warnings"][0])

    def test_preflight_compiles_crop_safe_fuzzy_brief(self) -> None:
        task = load_task(ROOT / "tasks/fragrance-autumn-key-visual.yaml")
        plan = build_plan(task)
        self.assertEqual(plan["status"], "ready_for_generation")
        self.assertFalse(plan["model_only_allowed"])
        self.assertIn("safe zone", " ".join(plan["hard_requirements"]).lower())
        self.assertIn("mask-from-color.py", " ".join(plan["postprocess"]))

    def test_lab_round_trip_and_target_lightness(self) -> None:
        target = (0, 112, 252)
        lab = rgb_to_lab(target)
        round_trip = lab_to_rgb(lab)
        self.assertLessEqual(max(abs(left - right) for left, right in zip(target, round_trip)), 1)
        self.assertAlmostEqual(lab[0], 50.24, places=1)

    def test_compiler_selects_palette_reference_and_explicit_pair(self) -> None:
        job = compile_job(
            PACKAGE,
            "a ceramic chair in a quiet studio",
            pair_id="cobalt-warm-yellow",
            profile="weak",
        )
        self.assertEqual(job["palette_pair"]["id"], "cobalt-warm-yellow")
        self.assertEqual(len(job["reference_images"]), 1)
        self.assertIn("#002EA6", job["prompt"])
        self.assertIn("SUBJECT:", job["prompt"])
        self.assertTrue(job["reference_images"][0]["absolute_path"].endswith("palette-01-cobalt-yellow.webp"))

    def test_compiler_is_generic_across_non_pair_style_packages(self) -> None:
        packages = sorted((ROOT / "style-packages").glob("*/*/package.yaml"))
        self.assertEqual(len(packages), 12)
        for package in packages:
            job = compile_job(package.parent, "a quiet study of the requested subject", profile="weak")
            self.assertEqual(job["model"]["adapter"], "provider-neutral")
            self.assertNotIn("flower arrangement", job["prompt"].lower())
            self.assertNotIn("blue-orange", job["prompt"].lower())

    def test_weak_profile_preserves_package_base_prompt(self) -> None:
        runtime = load_package(ROOT / "style-packages/artists/anna-ancher")
        job = compile_job(ROOT / "style-packages/artists/anna-ancher", "a quiet kitchen", profile="weak")
        self.assertIn("Create a quiet oil painting of a quiet kitchen", job["prompt"])
        self.assertIn("ordinary, unperformed body language", job["prompt"])

    def test_non_pair_package_evaluation_is_supported(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            image_path = Path(directory) / "render.png"
            Image.new("RGB", (32, 32), (120, 120, 120)).save(image_path)
            result = evaluate_image(ROOT / "style-packages/artists/anna-ancher", image_path)
        self.assertIsNone(result["pair"])
        self.assertIsNone(result["metrics"]["pair_coverage"])
        self.assertEqual(result["status"], "pass")

    def test_unknown_evaluation_profile_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            image_path = Path(directory) / "render.png"
            Image.new("RGB", (32, 32), (120, 120, 120)).save(image_path)
            with self.assertRaises(ValueError):
                evaluate_image(PACKAGE, image_path, profile="typo")

    def test_evaluator_detects_pair_and_luminance_failure(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            image_path = Path(directory) / "same-luminance-test.png"
            image = Image.new("RGB", (128, 64))
            for x in range(128):
                if x < 77:
                    color = (0, 46, 166)
                elif x < 109:
                    color = (255, 231, 111)
                else:
                    color = (128, 128, 128)
                for y in range(64):
                    image.putpixel((x, y), color)
            image.save(image_path)
            result = evaluate_image(
                PACKAGE,
                image_path,
                pair_id="cobalt-warm-yellow",
                profile="same-luminance",
            )
        self.assertGreater(result["metrics"]["pair_coverage"], 0.80)
        self.assertEqual(result["status"], "fail")
        self.assertFalse(result["checks"]["lstar_delta"]["pass"])
        self.assertTrue(result["checks"]["area_ratio"]["pass"])

    def test_person_adapter_requires_protected_semantic_masks(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            image_path = Path(directory) / "portrait.png"
            Image.new("RGB", (64, 64), (128, 128, 128)).save(image_path)
            result = segment_by_color(
                MaskRequest(
                    image_path=image_path,
                    target_hex="#0070FC",
                    safety_profile="person",
                    protected_classes=("skin", "hair"),
                    min_component_area=4,
                )
            )
        self.assertEqual(result.status, "rejected")
        self.assertIn("missing protected semantic masks", result.reasons[0])

    def test_generic_adapter_requires_declared_protected_masks(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            image_path = Path(directory) / "render.png"
            Image.new("RGB", (64, 64), (0, 112, 252)).save(image_path)
            result = segment_by_color(
                MaskRequest(
                    image_path=image_path,
                    target_hex="#0070FC",
                    safety_profile="generic",
                    protected_classes=("skin",),
                    min_component_area=4,
                )
            )
        self.assertEqual(result.status, "rejected")
        self.assertTrue(any(reason.startswith("missing protected semantic masks") for reason in result.reasons))

    def test_person_adapter_excludes_protected_overlap(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            image_path = root / "portrait.png"
            image = Image.new("RGB", (64, 64), (128, 128, 128))
            for x in range(10, 54):
                for y in range(10, 54):
                    image.putpixel((x, y), (0, 112, 252))
            image.save(image_path)
            protected = Image.new("L", (64, 64), 0)
            for x in range(10, 20):
                for y in range(10, 20):
                    protected.putpixel((x, y), 255)
            masks = {}
            for class_name in ("skin", "hair"):
                mask_path = root / f"{class_name}.png"
                (protected if class_name == "skin" else Image.new("L", (64, 64), 0)).save(mask_path)
                masks[class_name] = mask_path.name
            manifest = root / "manifest.json"
            manifest.write_text(
                json.dumps({"image_sha256": hashlib.sha256(image_path.read_bytes()).hexdigest(), "classes": masks}),
                encoding="utf-8",
            )
            adapter = FileSegmentationAdapter(manifest, image_path)
            result = segment_by_color(
                MaskRequest(
                    image_path=image_path,
                    target_hex="#0070FC",
                    safety_profile="person",
                    protected_classes=("skin", "hair"),
                    min_component_area=4,
                ),
                adapter.require(("skin", "hair")),
            )
        self.assertEqual(result.status, "rejected")
        self.assertGreater(result.metrics["protected_overlap_pixels"], 0)
        protected_crop = result.mask.crop((10, 10, 20, 20))
        values = list(protected_crop.get_flattened_data()) if hasattr(protected_crop, "get_flattened_data") else list(protected_crop.getdata())
        self.assertTrue(all(value == 0 for value in values))

    def test_reflective_adapter_separates_highlight_mask(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            image_path = Path(directory) / "glass.png"
            image = Image.new("RGB", (64, 64), (20, 20, 20))
            for x in range(12, 52):
                for y in range(12, 52):
                    image.putpixel((x, y), (255, 119, 15))
            for x in range(28, 36):
                for y in range(16, 48):
                    image.putpixel((x, y), (255, 255, 255))
            image.save(image_path)
            result = segment_by_color(
                MaskRequest(
                    image_path=image_path,
                    target_hex="#FF770F",
                    role="product",
                    safety_profile="reflective",
                    lab_radius=34,
                    min_component_area=4,
                )
            )
        self.assertGreater(result.metrics["reflection_candidates"], 0)
        self.assertEqual(result.reflection_mask.getpixel((30, 30)), 255)
        self.assertEqual(result.mask.getpixel((30, 30)), 0)

    def test_manifest_rejects_masks_from_another_render(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            image_path = root / "render.png"
            Image.new("RGB", (8, 8), (0, 0, 0)).save(image_path)
            mask_path = root / "skin.png"
            Image.new("L", (8, 8), 0).save(mask_path)
            manifest = root / "manifest.json"
            manifest.write_text(json.dumps({"image_sha256": "wrong", "classes": {"skin": "skin.png"}}), encoding="utf-8")
            with self.assertRaises(MaskAdapterError):
                FileSegmentationAdapter(manifest, image_path)

    def test_manifest_requires_hash_and_rejects_path_traversal(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "package"
            root.mkdir()
            outside = Path(directory) / "outside.png"
            Image.new("L", (8, 8), 0).save(outside)
            image_path = root / "render.png"
            Image.new("RGB", (8, 8), (0, 0, 0)).save(image_path)
            manifest = root / "manifest.json"
            manifest.write_text(json.dumps({"classes": {"skin": "../outside.png"}}), encoding="utf-8")
            with self.assertRaises(MaskAdapterError):
                FileSegmentationAdapter(manifest, image_path)

            manifest.write_text(
                json.dumps({
                    "image_sha256": hashlib.sha256(image_path.read_bytes()).hexdigest(),
                    "classes": {"skin": "../outside.png"},
                }),
                encoding="utf-8",
            )
            with self.assertRaises(MaskAdapterError):
                FileSegmentationAdapter(manifest, image_path)

    def test_duplicate_yaml_keys_are_rejected(self) -> None:
        with self.assertRaises(Exception):
            safe_load(io.StringIO("masking:\n  required: true\n  required: false\n"))

    def test_manifest_duplicates_and_unknown_references_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "references").mkdir()
            manifest = root / "references/manifest.csv"
            manifest.write_text(
                "asset_id,local_path,title,creator,year,source_url,license,attribution,role,notes\n"
                "same,,One,Creator,2020,https://example.com,CC0,Creator,details,\n"
                "same,,Two,Creator,2021,https://example.com,CC0,Creator,details,\n",
                encoding="utf-8",
            )
            with self.assertRaises(ValueError):
                manifest_records({"root": root})

            manifest.write_text(
                "asset_id,local_path,title,creator,year,source_url,license,attribution,role,notes\n"
                "known,,One,Creator,2020,https://example.com,CC0,Creator,details,\n",
                encoding="utf-8",
            )
            with self.assertRaises(ValueError):
                select_references({"root": root}, {"reference_asset_ids": ["unknown"]})

    def test_image_processing_limit_rejects_unsafe_input_size(self) -> None:
        with self.assertRaises(ValueError):
            ensure_working_size((10_000, 10_000), "test image")


if __name__ == "__main__":
    unittest.main()

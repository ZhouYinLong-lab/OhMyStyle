from __future__ import annotations

import sys
import tempfile
import unittest
import importlib.util
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from render_metrics import evaluate_image, hex_to_rgb  # noqa: E402

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
from style_runtime import compile_job  # noqa: E402


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

    def test_preflight_compiles_crop_safe_fuzzy_brief(self) -> None:
        task = load_task(ROOT / "tasks/fragrance-autumn-key-visual.yaml")
        plan = build_plan(task)
        self.assertEqual(plan["status"], "ready_for_generation")
        self.assertTrue(plan["model_only_allowed"])
        self.assertIn("safe zone", " ".join(plan["hard_requirements"]).lower())

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


if __name__ == "__main__":
    unittest.main()

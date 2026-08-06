from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from composite_runtime import compile_composite, infer_mode, validate_composite_definition


class CompositeRuntimeTests(unittest.TestCase):
    def test_infers_stack_for_distinct_roles(self):
        data = {"bases": [{"package": "a", "role": "medium"}, {"package": "b", "role": "lighting"}]}
        self.assertEqual(infer_mode(data), "stack")

    def test_infers_blend_for_repeated_roles(self):
        data = {"bases": [{"package": "a", "role": "palette"}, {"package": "b", "role": "palette"}]}
        self.assertEqual(infer_mode(data), "blend")

    def test_infers_contrast_for_zones(self):
        data = {
            "bases": [
                {"package": "a", "role": "medium", "zone": "foreground"},
                {"package": "b", "role": "palette", "zone": "background"},
            ]
        }
        self.assertEqual(infer_mode(data), "contrast")

    def test_explicit_stack_rejects_duplicate_roles(self):
        data = {"bases": [{"package": "a", "role": "medium"}, {"package": "b", "role": "medium"}]}
        with self.assertRaises(ValueError):
            validate_composite_definition(data, explicit_mode="stack")

    def test_real_stack_recipe_compiles(self):
        job = compile_composite(
            ROOT / "style-packages/composites/rpg-maker-x-turner",
            "a small harbor at dawn",
            profile="weak",
        )
        self.assertEqual(job["composite"]["mode"], "stack")
        self.assertEqual(len(job["components"]), 2)
        self.assertIn("COMPOSITE STYLE MODE: stack", job["prompt"])

    def test_real_blend_recipe_compiles(self):
        job = compile_composite(
            ROOT / "style-packages/composites/vermeer-x-monet",
            "a vase beside a rain-streaked window",
            profile="weak",
        )
        self.assertEqual(job["composite"]["mode"], "blend")
        self.assertIn("normalized weights", job["prompt"])

    def test_real_contrast_recipe_compiles(self):
        job = compile_composite(
            ROOT / "style-packages/composites/rpg-maker-x-gauguin",
            "a village path with a character in the foreground",
            profile="weak",
        )
        self.assertEqual(job["composite"]["mode"], "contrast")
        self.assertIn("foreground uses medium", job["prompt"])


if __name__ == "__main__":
    unittest.main()

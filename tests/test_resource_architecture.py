from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from resource_registry import build_registry, discover_packages, load_yaml


class ResourceArchitectureTests(unittest.TestCase):
    def test_every_structured_package_has_resource_contract(self):
        packages = discover_packages(ROOT / "style-packages")
        self.assertEqual(len(packages), 32)
        for package in packages:
            resource = load_yaml(package / "resource.yaml")
            package_data = load_yaml(package / "package.yaml")
            self.assertEqual(resource["resource_id"], package_data["id"])
            self.assertTrue(resource["task_independent"])
            self.assertIn(resource["maturity"], {"L2", "L3"})

    def test_l3_resources_have_accepted_examples(self):
        for package in discover_packages(ROOT / "style-packages"):
            resource = load_yaml(package / "resource.yaml")
            accepted = [path for path in (package / "examples" / "accepted").iterdir() if path.suffix.lower() == ".png"]
            self.assertEqual(resource["maturity"] == "L3", bool(accepted))

    def test_registry_is_deterministic_and_complete(self):
        registry = load_yaml(ROOT / "registry/index.yaml")
        generated = build_registry(ROOT / "style-packages")
        self.assertEqual(registry, generated)
        self.assertEqual(len(registry["packages"]), 32)
        self.assertEqual(len({entry["resource_id"] for entry in registry["packages"]}), 32)


if __name__ == "__main__":
    unittest.main()

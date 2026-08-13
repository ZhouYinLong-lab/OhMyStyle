from __future__ import annotations

import io
import json
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import remote_repository  # noqa: E402


def archive_bytes() -> bytes:
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w") as archive:
        archive.writestr("OhMyStyle-main/SKILL.md", "---\nname: ohmystyle\ndescription: test\n---\n")
        archive.writestr("OhMyStyle-main/style-packages/README.md", "styles")
    return buffer.getvalue()


class RemoteRepositoryTests(unittest.TestCase):
    def test_downloads_and_reuses_a_cached_repository(self) -> None:
        payload = archive_bytes()
        with tempfile.TemporaryDirectory() as directory:
            with patch.object(remote_repository, "_cache_root", return_value=Path(directory)):
                with patch.object(remote_repository, "_download", return_value=payload) as download:
                    config = {"url": "https://github.com/example/OhMyStyle", "ref": "main"}
                    first = remote_repository.ensure_repository(config)
                    second = remote_repository.ensure_repository(config)
                    self.assertEqual(first, second)
                    download.assert_called_once_with(config["url"], config["ref"])
                    metadata = json.loads((first.parents[1] / "repository.json").read_text(encoding="utf-8"))
                    self.assertEqual(metadata["ref"], "main")

    def test_rejects_hash_mismatch(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            with patch.object(remote_repository, "_cache_root", return_value=Path(directory)):
                with patch.object(remote_repository, "_download", return_value=archive_bytes()):
                    with self.assertRaises(ValueError):
                        remote_repository.ensure_repository({
                            "url": "https://github.com/example/OhMyStyle",
                            "ref": "main",
                            "sha256": "0" * 64,
                        })

    def test_rejects_non_github_or_non_https_urls(self) -> None:
        for url in ("http://github.com/example/OhMyStyle", "https://example.com/repo", "https://github.com/example"):
            with self.subTest(url=url):
                with self.assertRaises(ValueError):
                    remote_repository.ensure_repository({"url": url})


if __name__ == "__main__":
    unittest.main()

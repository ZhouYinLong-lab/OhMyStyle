#!/usr/bin/env python3
"""Safe, cache-backed loading of OhMyStyle from a GitHub repository URL."""

from __future__ import annotations

import hashlib
import io
import json
import os
import re
import shutil
import tempfile
import zipfile
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
from urllib.parse import urlparse


MAX_ARCHIVE_BYTES = 100 * 1024 * 1024
MAX_EXTRACTED_BYTES = 500 * 1024 * 1024
GITHUB_RE = re.compile(r"^/([^/]+)/([^/]+?)(?:\.git)?/?$")


def _cache_root() -> Path:
    local_app_data = os.environ.get("LOCALAPPDATA")
    base = Path(local_app_data) if local_app_data else Path.home() / ".cache"
    return base / "OhMyStyle" / "repositories"


def _parse_github_url(url: str) -> tuple[str, str]:
    parsed = urlparse(url)
    if parsed.scheme != "https" or parsed.netloc.lower() != "github.com":
        raise ValueError("repository URL must be an HTTPS GitHub repository URL")
    match = GITHUB_RE.match(parsed.path)
    if not match:
        raise ValueError("repository URL must look like https://github.com/OWNER/REPOSITORY")
    return match.group(1), match.group(2)


def _archive_url(url: str, ref: str) -> str:
    owner, repo = _parse_github_url(url)
    return f"https://github.com/{owner}/{repo}/archive/{ref}.zip"


def _safe_extract(archive: bytes, destination: Path) -> None:
    with zipfile.ZipFile(io.BytesIO(archive)) as handle:
        entries = handle.infolist()
        total = 0
        for entry in entries:
            name = entry.filename.replace("\\", "/")
            target = (destination / name).resolve()
            try:
                target.relative_to(destination.resolve())
            except ValueError as exc:
                raise ValueError(f"repository archive contains an escaping path: {entry.filename!r}") from exc
            # ZIP symlinks can escape after extraction even when their name is safe.
            if (entry.external_attr >> 16) & 0o170000 == 0o120000:
                raise ValueError(f"repository archive contains a symlink: {entry.filename!r}")
            total += entry.file_size
            if total > MAX_EXTRACTED_BYTES:
                raise ValueError("repository archive is too large after extraction")
        for entry in entries:
            handle.extract(entry, destination)


def _find_repository_root(extracted: Path) -> Path:
    candidates = [extracted] + [path for path in extracted.iterdir() if path.is_dir()]
    for candidate in candidates:
        if (candidate / "style-packages").is_dir() and (candidate / "SKILL.md").is_file():
            return candidate.resolve()
    raise ValueError("downloaded repository does not contain OhMyStyle style-packages and SKILL.md")


def _download(url: str, ref: str) -> bytes:
    request = Request(_archive_url(url, ref), headers={"User-Agent": "OhMyStyle/1.0"})
    try:
        with urlopen(request, timeout=60) as response:
            length = int(response.headers.get("Content-Length", "0"))
            if length > MAX_ARCHIVE_BYTES:
                raise ValueError("repository archive is too large")
            chunks: list[bytes] = []
            size = 0
            while True:
                chunk = response.read(1024 * 1024)
                if not chunk:
                    break
                size += len(chunk)
                if size > MAX_ARCHIVE_BYTES:
                    raise ValueError("repository archive is too large")
                chunks.append(chunk)
            return b"".join(chunks)
    except (HTTPError, URLError, TimeoutError) as exc:
        raise RuntimeError(f"could not download repository archive: {exc}") from exc


def ensure_repository(config: dict[str, str]) -> Path:
    """Return a cached, verified repository root for a remote config."""
    if not isinstance(config, dict):
        raise ValueError("repository configuration must be an object")
    url = config.get("url", "")
    if not isinstance(url, str):
        raise ValueError("repository.url must be a string")
    _parse_github_url(url)
    ref = config.get("commit") or config.get("ref") or "main"
    if not isinstance(ref, str) or not re.fullmatch(r"[A-Za-z0-9._/@-]{1,160}", ref):
        raise ValueError("repository ref contains unsupported characters")
    expected_hash = config.get("sha256")
    if expected_hash and not re.fullmatch(r"[0-9a-fA-F]{64}", expected_hash):
        raise ValueError("repository.sha256 must be a 64-character hexadecimal hash")

    cache_key = hashlib.sha256(f"{url}\n{ref}".encode("utf-8")).hexdigest()
    cache_dir = _cache_root() / cache_key
    marker = cache_dir / "repository.json"
    if marker.is_file():
        metadata = json.loads(marker.read_text(encoding="utf-8"))
        root = cache_dir / metadata["root_relative"]
        if root.is_dir() and (root / "style-packages").is_dir():
            if expected_hash and metadata.get("sha256") != expected_hash.lower():
                raise ValueError("cached repository hash does not match repository.sha256")
            return root

    archive = _download(url, ref)
    digest = hashlib.sha256(archive).hexdigest()
    if expected_hash and digest.lower() != expected_hash.lower():
        raise ValueError("repository archive sha256 does not match repository.sha256")
    cache_dir.parent.mkdir(parents=True, exist_ok=True)
    temporary = Path(tempfile.mkdtemp(prefix=f"{cache_key}-", dir=cache_dir.parent))
    try:
        extracted = temporary / "source"
        extracted.mkdir()
        _safe_extract(archive, extracted)
        root = _find_repository_root(extracted)
        root_relative = root.relative_to(temporary)
        metadata = {"url": url, "ref": ref, "sha256": digest, "root_relative": root_relative.as_posix()}
        marker_tmp = temporary / "repository.json"
        marker_tmp.write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        if cache_dir.exists():
            shutil.rmtree(cache_dir)
        temporary.rename(cache_dir)
        return cache_dir / root_relative
    except Exception:
        shutil.rmtree(temporary, ignore_errors=True)
        raise

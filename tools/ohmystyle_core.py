#!/usr/bin/env python3
"""Provider-neutral conversation and generation orchestration for OhMyStyle."""

from __future__ import annotations

import json
import re
import subprocess
import uuid
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from resource_registry import discover_packages, load_yaml
from composite_runtime import compile_composite
from style_runtime import compile_job, resolve_package


ROOT = Path(__file__).resolve().parents[1]
STYLE_ROOT = ROOT / "style-packages"
PHASES = (
    "content_confirmation",
    "detail_confirmation",
    "style_matching",
    "style_confirmation",
    "ready",
    "compiled",
    "generated",
    "review",
)


def now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _tokens(value: Any) -> set[str]:
    if value is None:
        return set()
    ignored = {"16", "9", "4", "3", "1", "16x9", "9x16", "4x5", "the", "and", "with", "style"}
    return {
        token.lower()
        for token in re.findall(r"[\w\u4e00-\u9fff]+", str(value))
        if len(token) > 1 and token.lower() not in ignored and not token.isdigit()
    }


def _flatten(value: Any) -> list[str]:
    if isinstance(value, dict):
        return [item for child in value.values() for item in _flatten(child)]
    if isinstance(value, list):
        return [item for child in value for item in _flatten(child)]
    return [str(value)] if value is not None else []


def _package_record(path: Path) -> dict[str, Any]:
    package = load_yaml(path / "package.yaml")
    identity = load_yaml(path / "identity.yaml")
    signature = load_yaml(path / "visual-signature.yaml")
    classification = package.get("classification", {})
    searchable = " ".join(
        [
            str(package.get("id", "")),
            str(package.get("name", "")),
            str(package.get("summary", "")),
            " ".join(_flatten(classification)),
            " ".join(_flatten(identity.get("scope", {}))),
            " ".join(_flatten(signature)),
        ]
    )
    return {
        "id": package.get("id"),
        "name": package.get("name"),
        "kind": package.get("kind"),
        "domain": package.get("domain"),
        "version": package.get("version"),
        "summary": package.get("summary", ""),
        "path": path.relative_to(ROOT).as_posix(),
        "searchable": searchable,
        "subject_policy": identity.get("subject_policy", identity.get("scope", {}).get("subject_policy", "open")),
        "gallery": (path / "gallery-16x9.jpg").relative_to(ROOT).as_posix() if (path / "gallery-16x9.jpg").is_file() else None,
    }


def list_style_records() -> list[dict[str, Any]]:
    return [_package_record(path) for path in discover_packages(STYLE_ROOT)]


def match_styles(brief: str, details: dict[str, Any] | None = None, limit: int = 5) -> list[dict[str, Any]]:
    query = " ".join([brief, " ".join(_flatten(details or {}))])
    query_tokens = _tokens(query)
    records = list_style_records()
    scored: list[tuple[float, dict[str, Any]]] = []
    for record in records:
        record_tokens = _tokens(record["searchable"])
        overlap = query_tokens & record_tokens
        score = len(overlap) / max(1, len(query_tokens))
        if record["kind"] in _tokens(query):
            score += 0.05
        result = {key: value for key, value in record.items() if key != "searchable"}
        result["match_score"] = round(min(score, 1.0), 4)
        result["matched_terms"] = sorted(overlap)[:12]
        result["reason"] = "；".join(
            [
                f"视觉资料命中 {len(overlap)} 个需求词" if overlap else "可作为开放主体的候选包",
                "包的主体策略保持开放" if record["subject_policy"] else "请检查主体策略",
            ]
        )
        scored.append((score, result))
    scored.sort(key=lambda item: (-item[0], item[1]["id"]))
    return [item[1] for item in scored[: max(1, limit)]]


def _question(phase: str) -> list[str]:
    return {
        "content_confirmation": ["主体是什么？", "这张图的用途是什么？", "是否有必须保留或禁止出现的内容？"],
        "detail_confirmation": ["需要什么画幅和构图？", "需要哪些材质、光线和色彩？", "是否使用参考图或输入照片？"],
        "style_confirmation": ["请选择一个候选风格包，或提交你自己的风格包路径。", "确认后才会编译 Prompt 并进入生图。"],
        "ready": ["需求和风格已确认，可以编译生成任务。"],
    }.get(phase, [])


def new_session(brief: str = "", session_id: str | None = None) -> dict[str, Any]:
    session = {
        "schema_version": "1.0.0",
        "session_id": session_id or f"oms-{uuid.uuid4().hex[:12]}",
        "created_at": now(),
        "updated_at": now(),
        "phase": "content_confirmation",
        "brief": brief.strip(),
        "content": {},
        "details": {},
        "style_candidates": [],
        "style_selection": None,
        "confirmation": {"content": False, "details": False, "style": False},
        "job": None,
        "result": None,
        "events": [],
    }
    if brief.strip():
        session["content"]["brief"] = brief.strip()
    return _record(session, "session_started", {"brief": brief.strip()})


def _record(session: dict[str, Any], event: str, payload: dict[str, Any]) -> dict[str, Any]:
    session["updated_at"] = now()
    session.setdefault("events", []).append({"at": session["updated_at"], "event": event, "payload": payload})
    return session


def _require(data: dict[str, Any], keys: tuple[str, ...], label: str) -> None:
    missing = [key for key in keys if not str(data.get(key, "")).strip()]
    if missing:
        raise ValueError(f"{label} missing required fields: {', '.join(missing)}")


def advance(session: dict[str, Any], update: dict[str, Any]) -> dict[str, Any]:
    """Apply one structured confirmation turn and return the updated session."""
    phase = session.get("phase")
    if phase == "content_confirmation":
        content = dict(session.get("content", {}))
        content.update(update.get("content", update))
        if update.get("confirmed") is True or update.get("content_confirmed") is True:
            _require(content, ("subject",), "content")
            session["content"] = content
            session["confirmation"]["content"] = True
            session["phase"] = "detail_confirmation"
        else:
            session["content"] = content
        return _record(session, "content_updated", {"phase": session["phase"]})
    if phase == "detail_confirmation":
        details = dict(session.get("details", {}))
        details.update(update.get("details", update))
        if update.get("confirmed") is True or update.get("details_confirmed") is True:
            _require(details, ("aspect_ratio",), "details")
            session["details"] = details
            session["confirmation"]["details"] = True
            session["style_candidates"] = match_styles(
                session.get("brief", ""),
                {**session.get("content", {}), **details},
                int(update.get("limit", 5)),
            )
            session["phase"] = "style_matching"
        else:
            session["details"] = details
        return _record(session, "details_updated", {"phase": session["phase"]})
    if phase == "style_matching":
        candidates = match_styles(session.get("brief", ""), session.get("details", {}), int(update.get("limit", 5)))
        session["style_candidates"] = candidates
        session["phase"] = "style_confirmation"
        return _record(session, "styles_matched", {"count": len(candidates)})
    if phase == "style_confirmation":
        selection = update.get("style_selection") or update.get("package")
        if not selection:
            raise ValueError("style_selection or package is required")
        if isinstance(selection, str):
            selection = {"package": selection}
        package = str(selection.get("package", ""))
        resolve_style_reference(package)
        session["style_selection"] = selection
        if update.get("confirmed") is True or update.get("style_confirmed") is True:
            session["confirmation"]["style"] = True
            session["phase"] = "ready"
        return _record(session, "style_selected", {"package": package, "confirmed": session["confirmation"]["style"]})
    raise ValueError(f"Session cannot accept confirmation in phase {phase!r}")


def resolve_style_reference(reference: str) -> Path:
    raw = Path(reference)
    candidates = [ROOT / raw, STYLE_ROOT / raw]
    for candidate in candidates:
        try:
            resolved = candidate.resolve()
            resolved.relative_to(STYLE_ROOT.resolve())
            if (resolved / "package.yaml").is_file() or (resolved / "composite.yaml").is_file():
                return resolved
        except (FileNotFoundError, ValueError):
            continue
    for manifest in STYLE_ROOT.rglob("package.yaml"):
        if load_yaml(manifest).get("id") == reference:
            return manifest.parent.resolve()
    for manifest in (STYLE_ROOT / "composites").rglob("composite.yaml"):
        if load_yaml(manifest).get("id") == reference:
            return manifest.parent.resolve()
    raise FileNotFoundError(f"Style package is not inside style-packages: {reference}")


def compile_session(session: dict[str, Any], model: str = "provider-neutral") -> dict[str, Any]:
    if session.get("phase") != "ready" or not session.get("confirmation", {}).get("style"):
        raise ValueError("Session is not ready; complete content, detail, and style confirmation first")
    selection = session["style_selection"]
    package = resolve_style_reference(str(selection["package"]))
    content = session["content"]
    details = session["details"]
    subject = str(content["subject"])
    variables = {key.upper(): str(value) for key, value in details.items() if key not in {"aspect_ratio"}}
    if (package / "composite.yaml").is_file():
        job = compile_composite(package, subject, variables=variables)
        job["model"] = {"name": model, "profile": "generic", "adapter": "provider-neutral"}
    else:
        job = compile_job(package, subject, model=model, variables=variables)
    job["session_id"] = session["session_id"]
    job["request"] = {"content": content, "details": details, "style_selection": selection}
    job["output"] = {"aspect_ratio": details.get("aspect_ratio"), "provider": model}
    session["job"] = job
    session["phase"] = "compiled"
    _record(session, "job_compiled", {"package": selection["package"], "model": model})
    return job


def generate_session(session: dict[str, Any], provider: dict[str, Any] | None = None) -> dict[str, Any]:
    if session.get("phase") not in {"compiled", "generated"}:
        raise ValueError("Compile the confirmed session before generation")
    if not session.get("job"):
        raise ValueError("Session has no compiled job")
    provider = provider or {"type": "provider-neutral"}
    provider_type = provider.get("type", "provider-neutral")
    if provider_type == "provider-neutral":
        result = {"status": "awaiting_provider", "provider": provider, "job": session["job"]}
    elif provider_type == "command":
        command = provider.get("command")
        if not isinstance(command, list) or not command or not all(isinstance(item, str) for item in command):
            raise ValueError("command provider requires a non-empty string command list")
        result = _run_command_provider(command, session["job"], provider)
    elif provider_type == "http_json":
        result = _run_http_json_provider(session["job"], provider)
    else:
        raise ValueError(f"Unknown provider type: {provider_type}")
    session["result"] = result
    session["phase"] = "generated" if result.get("status") == "completed" else "compiled"
    _record(session, "generation_requested", {"provider": provider_type, "status": result.get("status")})
    return result


def _run_command_provider(command: list[str], job: dict[str, Any], provider: dict[str, Any]) -> dict[str, Any]:
    output_dir = Path(provider.get("output_dir", "outputs")).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    job_path = output_dir / f"{job['session_id']}.json"
    job_path.write_text(json.dumps(job, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    completed = subprocess.run(command + [str(job_path)], capture_output=True, text=True, check=False)
    if completed.returncode:
        raise RuntimeError(f"Provider command failed ({completed.returncode}): {completed.stderr.strip()}")
    return {
        "status": "completed",
        "provider": {"type": "command", "command": command},
        "job_path": str(job_path),
        "stdout": completed.stdout,
        "stderr": completed.stderr,
    }


def _run_http_json_provider(job: dict[str, Any], provider: dict[str, Any]) -> dict[str, Any]:
    url = provider.get("url")
    if not isinstance(url, str) or not url.startswith(("http://", "https://")):
        raise ValueError("http_json provider requires an http(s) url")
    headers = provider.get("headers", {})
    if not isinstance(headers, dict) or not all(isinstance(key, str) and isinstance(value, str) for key, value in headers.items()):
        raise ValueError("http_json provider headers must be a string map")
    payload = json.dumps(job, ensure_ascii=False).encode("utf-8")
    request = Request(url, data=payload, headers={"Content-Type": "application/json", **headers}, method="POST")
    timeout = float(provider.get("timeout", 120))
    try:
        with urlopen(request, timeout=timeout) as response:
            raw = response.read().decode("utf-8")
            try:
                body: Any = json.loads(raw)
            except json.JSONDecodeError:
                body = {"raw": raw}
            return {"status": "completed", "provider": {"type": "http_json", "url": url}, "response": body}
    except (HTTPError, URLError, TimeoutError) as exc:
        raise RuntimeError(f"HTTP provider failed: {exc}") from exc


def session_view(session: dict[str, Any]) -> dict[str, Any]:
    return {"session": session, "questions": _question(session.get("phase", "")), "can_compile": session.get("phase") == "ready"}

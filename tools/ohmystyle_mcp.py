#!/usr/bin/env python3
"""Minimal MCP-style stdio server for the OhMyStyle Skill.

The server implements the JSON-RPC methods needed by MCP clients without
adding an SDK dependency: initialize, tools/list, and tools/call.
"""

from __future__ import annotations

import json
import sys
from typing import Any

from ohmystyle_core import advance, compile_session, generate_session, match_styles, new_session, session_view
from remote_repository import ensure_repository


SESSIONS: dict[str, dict[str, Any]] = {}
SERVER_REPOSITORY: dict[str, Any] | None = None
SERVER_PROVIDER: dict[str, Any] | None = None


TOOLS = [
    {"name": "ohmystyle_start_session", "description": "Start a multi-turn OhMyStyle style selection session.", "inputSchema": {"type": "object", "properties": {"brief": {"type": "string"}, "session_id": {"type": "string"}}}},
    {"name": "ohmystyle_turn", "description": "Apply one confirmed content, detail, or style-selection turn.", "inputSchema": {"type": "object", "required": ["session_id"], "properties": {"session_id": {"type": "string"}, "update": {"type": "object"}}}},
    {"name": "ohmystyle_match_styles", "description": "Match the confirmed request to style packages.", "inputSchema": {"type": "object", "required": ["session_id"], "properties": {"session_id": {"type": "string"}, "limit": {"type": "integer"}}}},
    {"name": "ohmystyle_compile", "description": "Compile a confirmed session into a provider-neutral job.", "inputSchema": {"type": "object", "required": ["session_id"], "properties": {"session_id": {"type": "string"}, "model": {"type": "string"}}}},
    {"name": "ohmystyle_generate", "description": "Request generation through a user-managed provider.", "inputSchema": {"type": "object", "required": ["session_id"], "properties": {"session_id": {"type": "string"}, "provider": {"type": "object"}}}},
]


def result(value: object, request_id: object) -> dict[str, Any]:
    return {"jsonrpc": "2.0", "id": request_id, "result": {"content": [{"type": "text", "text": json.dumps(value, ensure_ascii=False, indent=2)}]}}


def error(message: str, request_id: object) -> dict[str, Any]:
    return {"jsonrpc": "2.0", "id": request_id, "error": {"code": -32000, "message": message}}


def call_tool(name: str, arguments: dict[str, Any]) -> object:
    if name == "ohmystyle_start_session":
        if arguments.get("repository") is not None:
            raise ValueError("MCP clients cannot submit repositories; configure one on the server")
        session = new_session(arguments.get("brief", ""), arguments.get("session_id"), SERVER_REPOSITORY)
        SESSIONS[session["session_id"]] = session
        return session_view(session)
    session_id = arguments.get("session_id")
    if not isinstance(session_id, str) or session_id not in SESSIONS:
        raise ValueError("unknown session_id")
    session = SESSIONS[session_id]
    if name == "ohmystyle_turn":
        return session_view(advance(session, arguments.get("update", {})))
    if name == "ohmystyle_match_styles":
        candidates = match_styles(session.get("brief", ""), {**session.get("content", {}), **session.get("details", {})}, int(arguments.get("limit", 5)), session.get("repository"))
        session["style_candidates"] = candidates
        session["phase"] = "style_confirmation"
        return session_view(session)
    if name == "ohmystyle_compile":
        return compile_session(session, arguments.get("model", "provider-neutral"))
    if name == "ohmystyle_generate":
        if arguments.get("provider") is not None:
            raise ValueError("MCP clients cannot submit providers; configure one on the server")
        return generate_session(session, SERVER_PROVIDER)
    raise ValueError(f"unknown tool: {name}")


def handle(request: dict[str, Any]) -> dict[str, Any] | None:
    request_id = request.get("id")
    method = request.get("method")
    if method == "notifications/initialized":
        return None
    if method == "initialize":
        return result({"protocolVersion": "2024-11-05", "capabilities": {"tools": {}}, "serverInfo": {"name": "ohmystyle", "version": "1.0.0"}}, request_id)
    if method == "tools/list":
        return result({"tools": TOOLS}, request_id)
    if method == "tools/call":
        try:
            params = request.get("params", {})
            return result(call_tool(str(params.get("name")), params.get("arguments", {})), request_id)
        except Exception as exc:
            return error(str(exc), request_id)
    return error(f"method not found: {method}", request_id)


def serve() -> None:
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            response = handle(json.loads(line))
            if response is not None:
                print(json.dumps(response, ensure_ascii=False), flush=True)
        except Exception as exc:
            print(json.dumps(error(str(exc), None), ensure_ascii=False), flush=True)


if __name__ == "__main__":
    serve()

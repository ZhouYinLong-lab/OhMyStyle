#!/usr/bin/env python3
"""Dependency-light HTTP interface for the OhMyStyle Skill."""

from __future__ import annotations

import argparse
import json
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from threading import RLock
from urllib.parse import urlparse

from ohmystyle_core import advance, compile_session, generate_session, match_styles, new_session, session_view


class SessionStore:
    def __init__(self) -> None:
        self._sessions: dict[str, dict] = {}
        self._lock = RLock()

    def put(self, session: dict) -> dict:
        with self._lock:
            self._sessions[session["session_id"]] = session
        return session

    def get(self, session_id: str) -> dict:
        with self._lock:
            if session_id not in self._sessions:
                raise KeyError(session_id)
            return self._sessions[session_id]


STORE = SessionStore()
SERVER_PROVIDER: dict | None = None
SERVER_REPOSITORY: dict | None = None


def _json_bytes(data: object) -> bytes:
    return (json.dumps(data, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


class Handler(BaseHTTPRequestHandler):
    server_version = "OhMyStyleHTTP/1.0"

    def _send(self, status: int, data: object) -> None:
        body = _json_bytes(data)
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _read(self) -> dict:
        length = int(self.headers.get("Content-Length", "0"))
        if length > 2_000_000:
            raise ValueError("request body is too large")
        raw = self.rfile.read(length) if length else b"{}"
        data = json.loads(raw.decode("utf-8"))
        if not isinstance(data, dict):
            raise ValueError("request body must be a JSON object")
        return data

    def do_GET(self) -> None:  # noqa: N802
        path = urlparse(self.path).path.rstrip("/")
        if path == "":
            self._send(HTTPStatus.OK, {"service": "ohmystyle", "status": "ok"})
            return
        parts = path.split("/")
        if len(parts) == 3 and parts[1] == "sessions":
            try:
                self._send(HTTPStatus.OK, session_view(STORE.get(parts[2])))
            except KeyError:
                self._send(HTTPStatus.NOT_FOUND, {"error": "session not found"})
            return
        self._send(HTTPStatus.NOT_FOUND, {"error": "not found"})

    def do_POST(self) -> None:  # noqa: N802
        path = urlparse(self.path).path.rstrip("/")
        try:
            body = self._read()
            if path == "/sessions":
                if body.get("repository") is not None:
                    raise ValueError("HTTP clients cannot submit repositories; configure one when starting the server")
                session = STORE.put(new_session(body.get("brief", ""), body.get("session_id"), SERVER_REPOSITORY))
                self._send(HTTPStatus.CREATED, session_view(session))
                return
            parts = path.split("/")
            if len(parts) < 4 or parts[1] != "sessions":
                self._send(HTTPStatus.NOT_FOUND, {"error": "not found"})
                return
            session = STORE.get(parts[2])
            action = parts[3]
            if action == "turn":
                result = advance(session, body)
                self._send(HTTPStatus.OK, session_view(STORE.put(result)))
            elif action == "match":
                candidates = match_styles(session.get("brief", ""), {**session.get("content", {}), **session.get("details", {})}, int(body.get("limit", 5)), session.get("repository"))
                session["style_candidates"] = candidates
                session["phase"] = "style_confirmation"
                self._send(HTTPStatus.OK, session_view(STORE.put(session)))
            elif action == "compile":
                job = compile_session(session, body.get("model", "provider-neutral"))
                self._send(HTTPStatus.OK, job)
            elif action == "generate":
                requested = body.get("provider")
                if requested:
                    raise ValueError("HTTP clients cannot submit providers; configure one when starting the server")
                if SERVER_PROVIDER is None:
                    self._send(HTTPStatus.OK, generate_session(session, None))
                else:
                    self._send(HTTPStatus.OK, generate_session(session, SERVER_PROVIDER))
            else:
                self._send(HTTPStatus.NOT_FOUND, {"error": "unknown session action"})
        except KeyError:
            self._send(HTTPStatus.NOT_FOUND, {"error": "session not found"})
        except (ValueError, FileNotFoundError) as exc:
            self._send(HTTPStatus.BAD_REQUEST, {"error": str(exc)})
        except Exception as exc:  # pragma: no cover - defensive HTTP boundary
            self._send(HTTPStatus.INTERNAL_SERVER_ERROR, {"error": str(exc)})

    def log_message(self, format: str, *args: object) -> None:
        return


def serve(
    host: str = "127.0.0.1",
    port: int = 8765,
    provider_config: dict | None = None,
    repository_config: dict | None = None,
) -> None:
    global SERVER_PROVIDER, SERVER_REPOSITORY
    SERVER_PROVIDER = provider_config
    SERVER_REPOSITORY = repository_config
    server = ThreadingHTTPServer((host, port), Handler)
    print(f"OhMyStyle HTTP listening on http://{host}:{port}", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8765)
    parser.add_argument("--provider-config", type=Path, help="JSON provider config loaded by the server")
    parser.add_argument("--repository-config", type=Path, help="JSON remote repository config loaded by the server")
    args = parser.parse_args()
    provider = json.loads(args.provider_config.read_text(encoding="utf-8")) if args.provider_config else None
    repository = json.loads(args.repository_config.read_text(encoding="utf-8")) if args.repository_config else None
    serve(args.host, args.port, provider, repository)


if __name__ == "__main__":
    main()

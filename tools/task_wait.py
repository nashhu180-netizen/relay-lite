#!/usr/bin/env python3
"""Bounded, read-only wait for the exact current dispatch's durable signal.

READY means a matching signal can be inspected, never approval or completion.
No Herdr commands, model turns, notification replay, or filesystem writes.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import time
from typing import Callable

MAX_SIGNAL_BYTES = 65536
FIELDS = ("task", "phase", "agent", "batch", "path", "review_round", "remediation_count")


class WaitError(Exception):
    """Whitelisted, nonsecret reason only."""


def check_receipt(env: dict[str, str]) -> None:
    if "RELAY_RECEIPT" in env:
        raise WaitError("relay_receipt_present")


def signal_path(root: Path, name: str) -> Path:
    relative = Path(name)
    if relative.is_absolute() or not relative.parts or any(p in {".", ".."} for p in relative.parts):
        raise WaitError("signal_path_outside_workspace")
    if not re.fullmatch(r"(?:DONE|BLOCKED)\.[A-Za-z0-9_.-]+\.md", relative.name):
        raise WaitError("invalid_signal_filename")
    path = root
    for component in relative.parts:
        path = path / component
        if path.is_symlink():
            raise WaitError("signal_symlink_rejected")
    if not path.resolve().is_relative_to(root):
        raise WaitError("signal_path_outside_workspace")
    return path


def inspect(root: Path, names: list[str], expected: dict[str, str]) -> dict | None:
    matches = []
    for name in names:
        path = signal_path(root, name)
        try:
            # Limit read memory; a partial write is not a matching signal yet.
            with path.open("rb") as stream:
                raw = stream.read(MAX_SIGNAL_BYTES + 1)
        except FileNotFoundError:
            continue
        except OSError:
            raise WaitError("signal_read_failed") from None
        if len(raw) > MAX_SIGNAL_BYTES:
            raise WaitError("signal_too_large")
        try:
            line = raw.decode("utf-8").strip()
        except UnicodeError:
            continue
        if "\n" in line or "\r" in line:
            continue
        parts = line.split()
        if not parts or parts[0] not in {"DONE", "BLOCKED"}:
            continue
        values = {}
        for token in parts[1:]:
            if "=" not in token:
                break
            key, value = token.split("=", 1)
            if key in values or not value:
                break
            values[key] = value
        else:
            if any(values.get(k) != v for k, v in expected.items()):
                continue
            if not values.get("evidence") or not re.fullmatch(r"[A-Z][A-Z0-9_]{0,39}", values.get("verdict", "")):
                continue
            if parts[0] == "BLOCKED" and not re.fullmatch(r"[a-z][a-z0-9_]{0,79}", values.get("reason", "")):
                continue
            if not path.name.startswith(parts[0] + "."):
                continue
            matches.append({"state": "READY", "signal": name,
                            "signal_kind": parts[0], "verdict": values["verdict"],
                            "sha256": hashlib.sha256(raw).hexdigest(),
                            "acceptance": "requires_owner_review"})
    if len(matches) > 1:
        raise WaitError("conflicting_matching_signals")
    return matches[0] if matches else None


def wait(root: Path, names: list[str], expected: dict[str, str], *, timeout: float = 50,
         poll_seconds: float = 1, sleep: Callable[[float], None] = time.sleep,
         monotonic: Callable[[], float] = time.monotonic) -> dict:
    root = root.resolve()
    if not root.is_dir():
        raise WaitError("workspace_directory_required")
    if not names or len(set(names)) != len(names) or set(expected) != set(FIELDS):
        raise WaitError("exact_dispatch_required")
    if not 0 <= timeout <= 60 or not 0 < poll_seconds <= 5:
        raise WaitError("invalid_wait_bound")
    deadline = monotonic() + timeout
    while True:
        check_receipt(dict(os.environ))
        result = inspect(root, names, expected)
        if result:
            return result
        remaining = deadline - monotonic()
        if remaining <= 0:
            return {"state": "PENDING", "reason": "matching_signal_not_ready",
                    "acceptance": "not_evaluated"}
        sleep(min(poll_seconds, remaining))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", required=True, type=Path, help="exact task workspace, not Herdr space ID")
    parser.add_argument("--signal", required=True, action="append", help="exact relative DONE/BLOCKED filename")
    for field in FIELDS:
        parser.add_argument("--" + field.replace("_", "-"), required=True)
    parser.add_argument("--timeout", type=float, default=50, help="0..60 seconds; PENDING is not task failure")
    try:
        args = parser.parse_args(argv)
        check_receipt(dict(os.environ))
        expected = {k: getattr(args, k) for k in FIELDS}
        result = wait(args.root, args.signal, expected, timeout=args.timeout)
    except WaitError as exc:
        print(json.dumps({"state": "BLOCKED", "reason": str(exc)}, sort_keys=True))
        return 2
    print(json.dumps(result, sort_keys=True))
    return 0 if result["state"] == "READY" else 3


if __name__ == "__main__":
    sys.exit(main())

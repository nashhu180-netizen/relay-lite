#!/usr/bin/env python3
"""single-task Herdr workspace observer. Memory only; never sends keys.

Run in a dedicated Herdr shell pane, independent of any model turn.
Notifications are hints, never node completion or authorization.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import socket
import subprocess
import sys
import time
from dataclasses import dataclass
from typing import Callable

POLL_SECONDS = 120


class WatchError(Exception):
    """An observation or delivery could not be proved; stop for the watcher."""


class NotificationDeferred(WatchError):
    """No submission was attempted. Keep the event for a later poll."""


RECOVERABLE_OBSERVATION_ERRORS = {
    "herdr_command_failed", "herdr_command_rejected", "herdr_error_response",
    "herdr_invalid_json", "herdr_missing_result", "herdr_missing_agent",
    "herdr_invalid_agents", "herdr_incomplete_state",
    "herdr_membership_changed_during_poll",
}


def acquire_instance(workspace: str, env: dict[str, str]) -> socket.socket:
    """No lock files: hold a local socket for this server/workspace only.

    Port collisions fail closed. Do not use SO_REUSEADDR, which allows duplicate
    binders on Windows. The socket never accepts connections or sends data.
    """
    scope = env.get("HERDR_SOCKET_PATH") or env.get("HERDR_SESSION", "default")
    digest = hashlib.sha256(f"{scope}\0{workspace}".encode()).digest()
    port = 39000 + int.from_bytes(digest[:4], "big") % 20000
    guard = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        if hasattr(socket, "SO_EXCLUSIVEADDRUSE"):
            guard.setsockopt(socket.SOL_SOCKET, socket.SO_EXCLUSIVEADDRUSE, 1)
        guard.bind(("127.0.0.1", port))
    except OSError:
        guard.close()
        raise WatchError("monitor_instance_conflict") from None
    return guard


@dataclass(frozen=True)
class AgentState:
    pane_id: str
    status: str
    seq: int


def check_environment(env: dict[str, str]) -> None:
    if "RELAY_RECEIPT" in env:
        raise WatchError("relay_receipt_present")
    if env.get("HERDR_ENV") != "1":
        raise WatchError("herdr_environment_required")


class Herdr:
    def call(self, *args: str) -> dict:
        try:
            proc = subprocess.run(
                ["herdr", *args], capture_output=True, timeout=15, check=False,
            )
        except (OSError, subprocess.TimeoutExpired):
            raise WatchError("herdr_command_failed") from None
        # Do not print stdout/stderr: they may contain terminal content/credentials.
        if proc.returncode:
            raise WatchError("herdr_command_rejected")
        try:
            payload = json.loads(proc.stdout)
        except (ValueError, UnicodeError):
            raise WatchError("herdr_invalid_json") from None
        if not isinstance(payload, dict) or "error" in payload:
            raise WatchError("herdr_error_response")
        result = payload.get("result")
        if not isinstance(result, dict):
            raise WatchError("herdr_missing_result")
        return result

    def agents(self) -> list[dict]:
        agents = self.call("agent", "list").get("agents")
        if not isinstance(agents, list) or any(not isinstance(a, dict) for a in agents):
            raise WatchError("herdr_invalid_agents")
        return agents

    def get(self, name: str) -> dict:
        agent = self.call("agent", "get", name).get("agent")
        if not isinstance(agent, dict):
            raise WatchError("herdr_missing_agent")
        return agent

    def pane(self, pane_id: str) -> dict:
        pane = self.call("pane", "get", pane_id).get("pane")
        if not isinstance(pane, dict):
            raise WatchError("herdr_missing_pane")
        return pane

    def notify(self, name: str, message: str) -> AgentState:
        # Submit once to the exact pane, including while the owner is working.
        # A state transition proves neither prompt consumption nor task completion.
        try:
            before = state(self.get(name))
        except WatchError:
            raise NotificationDeferred("notification_target_unavailable") from None
        if before.status in {"blocked", "unknown"}:
            raise NotificationDeferred("notification_target_not_ready")
        result = self.call("agent", "prompt", before.pane_id, message)
        if result.get("type") != "agent_prompted":
            raise WatchError("notification_unconfirmed")
        # This confirms submission only. The owner still reads the actual signals.
        return before


def agent_name(agent: dict) -> str:
    # agent is a kind (codex/claude), never a CLI identity. Unnamed
    # occupants are monitored using their opaque pane ID.
    name = agent.get("name") or agent.get("pane_id")
    if not isinstance(name, str) or not name or not name.isascii() or any(c.isspace() for c in name):
        raise WatchError("herdr_invalid_agent_name")
    return name


def state(agent: dict) -> AgentState:
    pane = agent.get("pane_id")
    status = agent.get("agent_status")
    seq = agent.get("state_change_seq")
    if (not isinstance(pane, str) or not pane or
        status not in {"idle", "working", "blocked", "done", "unknown"} or
        type(seq) is not int or seq < 0):
        raise WatchError("herdr_incomplete_state")
    return AgentState(pane, status, seq)


class SpaceWatch:
    def __init__(self, workspace: str, notify: str, own_name: str | None,
                 client: Herdr, env: dict[str, str]):
        self.workspace, self.notify, self.own_name = workspace, notify, own_name
        self.client, self.env = client, env
        self.previous: dict[str, AgentState] | None = None
        self.pending_message: str | None = None
        self.last_unconfirmed_message: str | None = None
        self.deferred_reason: str | None = None

    def snapshot(self) -> dict[str, AgentState]:
        check_environment(self.env)
        agents = self.client.agents()  # Rediscover every cycle; never a name prefix.
        members = [a for a in agents if a.get("workspace_id") == self.workspace]
        if self.own_name is None:
            pane = self.env.get("HERDR_PANE_ID")
            own = [a for a in members if pane and a.get("pane_id") == pane]
        else:
            own = [a for a in members if agent_name(a) == self.own_name]
        if not own:
            # A normal shell is deliberately absent from agent list. Resolve only
            # the caller's own inherited pane; never another pane by a guessed ID.
            caller_pane = self.env.get("HERDR_PANE_ID")
            if not caller_pane or self.own_name not in {None, caller_pane}:
                raise WatchError("watcher_identity_not_in_workspace")
            pane = self.client.pane(caller_pane)
            if pane.get("pane_id") != caller_pane or pane.get("workspace_id") != self.workspace:
                raise WatchError("watcher_identity_mismatch")
            own = [dict(pane, name=caller_pane)]
        if len(own) != 1:
            raise WatchError("watcher_identity_not_in_workspace")
        if self.env.get("HERDR_PANE_ID") and own[0].get("pane_id") != self.env["HERDR_PANE_ID"]:
            raise WatchError("watcher_identity_mismatch")
        self.own_name = agent_name(own[0])
        if self.notify == self.own_name:
            raise WatchError("watcher_cannot_notify_self")
        target = self.client.get(self.notify)
        target_pane = target.get("pane_id")
        if not isinstance(target_pane, str) or not target_pane:
            raise WatchError("notification_target_identity_missing")
        if target_pane == own[0].get("pane_id"):
            raise WatchError("watcher_cannot_notify_self")
        snapshot = {}
        for member in members:
            name = agent_name(member)
            # The principal orchestrator is the recipient, never monitored.
            # Resolve its actual pane on each poll rather than using a prefix.
            if name == self.own_name or member.get("pane_id") == target_pane:
                continue
            if name in snapshot:
                raise WatchError("herdr_duplicate_agent")
            detail = self.client.get(member.get("pane_id"))
            # List/get may race a move or replacement. Never invent a disappearance.
            if (detail.get("workspace_id") != self.workspace or
                detail.get("pane_id") != member.get("pane_id")):
                raise WatchError("herdr_membership_changed_during_poll")
            snapshot[name] = state(detail)
        return snapshot

    def poll(self) -> list[str]:
        current = self.snapshot()
        if self.previous is None:
            self.previous = current  # First successful observation is baseline.
            return []
        changes = []
        for name in sorted(self.previous.keys() | current.keys()):
            old, new = self.previous.get(name), current.get(name)
            if old == new:
                continue
            def label(value: AgentState | None) -> str:
                return "absent" if value is None else f"{value.status}:{value.seq}:{value.pane_id}"
            changes.append(f"{name} {label(old)} -> {label(new)}")
        if changes:
            self.pending_message = f"[relay-lite] space-change {self.workspace} " + "; ".join(changes)
            try:
                self.client.notify(self.notify, self.pending_message)
            except NotificationDeferred as exc:
                if self.deferred_reason != str(exc):
                    print(f"SPACE_WATCH_DEFERRED reason={exc}", flush=True)
                self.deferred_reason = str(exc)
                # No command was sent. Coalesce against the original baseline.
                return changes
            except WatchError as exc:
                # The command may have been submitted. Preserve the uncertainty,
                # continue observing, and never replay this delta automatically.
                self.last_unconfirmed_message = self.pending_message
                print(f"SPACE_WATCH_UNCONFIRMED reason={exc} {self.pending_message}", flush=True)
            else:
                event_id = hashlib.sha256(self.pending_message.encode()).hexdigest()
                print(f"SPACE_WATCH_SUBMITTED workspace={self.workspace} event={event_id}", flush=True)
        # Successful observations advance independently of notification delivery.
        self.previous = current
        self.pending_message = None
        self.deferred_reason = None
        return changes


def run(watch: SpaceWatch, *, sleep: Callable[[float], None] = time.sleep) -> None:
    degraded = None
    while True:
        try:
            watch.poll()
        except WatchError as exc:
            if str(exc) not in RECOVERABLE_OBSERVATION_ERRORS:
                raise
            if degraded != str(exc):
                print(f"SPACE_WATCH_DEGRADED reason={exc}", flush=True)
            degraded = str(exc)
        else:
            if degraded is not None:
                print("SPACE_WATCH_RECOVERED", flush=True)
            degraded = None
        sleep(POLL_SECONDS)


def notify_exit(watch: SpaceWatch, reason: str) -> None:
    """One best-effort exit hint; failure never replays the original event."""
    try:
        watch.client.notify(watch.notify, f"[relay-lite] watcher-stopped {watch.workspace} reason={reason}")
    except NotificationDeferred as exc:
        print(f"SPACE_WATCH_EXIT_NOTICE_DEFERRED reason={exc}", flush=True)
    except WatchError as exc:
        print(f"SPACE_WATCH_EXIT_NOTICE_UNCONFIRMED reason={exc}", flush=True)
    else:
        print(f"SPACE_WATCH_EXIT_NOTICE_SUBMITTED reason={reason}", flush=True)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace", required=True, help="exact Herdr workspace ID")
    parser.add_argument("--notify", required=True, help="orchestrator Herdr name")
    parser.add_argument("--self", dest="own_name", help="own shell pane ID or legacy watcher agent name")
    args = parser.parse_args(argv)
    watch = SpaceWatch(args.workspace, args.notify, args.own_name, Herdr(), dict(os.environ))
    guard = None
    try:
        check_environment(dict(os.environ))
        # Check identities before taking the per-workspace guard.
        watch.poll()
        guard = acquire_instance(args.workspace, dict(os.environ))
        print(f"SPACE_WATCH_STARTED workspace={args.workspace} pid={os.getpid()} interval={POLL_SECONDS}", flush=True)
        run(watch)
    except WatchError as exc:
        print(f"SPACE_WATCH_BLOCKED reason={exc}", file=sys.stderr, flush=True)
        if watch.pending_message:
            # Whitelisted state diff only; never raw CLI/pane content. The watcher
            # can identify the unconfirmed event even after this process exits.
            print(f"UNCONFIRMED {watch.pending_message}", file=sys.stderr, flush=True)
        if guard is not None:
            notify_exit(watch, str(exc))
        return 2
    except KeyboardInterrupt:
        if guard is not None:
            notify_exit(watch, "interrupted")
        return 0
    finally:
        if guard is not None:
            guard.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())

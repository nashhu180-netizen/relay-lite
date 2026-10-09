"""Dispatch-bound completion discovery independent of watcher availability."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))
import task_wait as tw


class TaskWaitTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name).resolve()
        self.expected = dict(task="RLT_36", phase="batch", agent="worker#1", batch="1",
                             path="na", review_round="1", remediation_count="0")
        self.name = "DONE.batch.worker.md"
        self.signal = "DONE " + " ".join(f"{k}={v}" for k, v in self.expected.items()) + " verdict=PASS evidence=report.md\n"

    def write(self, signal=None, name=None):
        (self.root / (name or self.name)).write_text(signal or self.signal, encoding="utf-8")

    def test_ready_preserves_original_bytes_and_requires_owner_review(self):
        self.write()
        before = (self.root / self.name).read_bytes()
        with patch("subprocess.run", side_effect=AssertionError("no notification or agent commands")):
            result = tw.wait(self.root, [self.name], self.expected, timeout=0)
        self.assertEqual("READY", result["state"])
        self.assertEqual("requires_owner_review", result["acceptance"])
        self.assertEqual(hashlib.sha256(before).hexdigest(), result["sha256"])
        self.assertEqual(before, (self.root / self.name).read_bytes())

    def test_wrong_dispatch_old_round_or_partial_write_never_ready(self):
        for signal in (self.signal.replace("task=RLT_36", "task=OTHER"),
                       self.signal.replace("review_round=1", "review_round=2"),
                       self.signal.replace("agent=worker#1", "agent=other#1"),
                       self.signal[:40], self.signal + "extra-line\n"):
            with self.subTest(signal=signal):
                self.write(signal)
                self.assertEqual("PENDING", tw.wait(self.root, [self.name], self.expected, timeout=0)["state"])

    def test_matching_blocked_is_ready_for_inspection_not_success(self):
        name = "BLOCKED.batch.worker.md"
        self.write(self.signal.replace("DONE ", "BLOCKED ").replace("verdict=PASS", "verdict=BLOCKED reason=missing_dependency"), name)
        result = tw.wait(self.root, [self.name, name], self.expected, timeout=0)
        self.assertEqual("READY", result["state"])
        self.assertEqual("BLOCKED", result["signal_kind"])
        self.assertEqual("requires_owner_review", result["acceptance"])

    def test_worker_finishes_during_wait_without_watcher(self):
        now = 0
        def clock():
            return now
        def sleep(seconds):
            nonlocal now
            now += seconds
            self.write()
        with patch("subprocess.run", side_effect=AssertionError("watcher unavailable")):
            result = tw.wait(self.root, [self.name], self.expected, timeout=50, sleep=sleep, monotonic=clock)
        self.assertEqual("READY", result["state"])
        self.assertEqual(1, now)

    def test_timeout_is_bounded_pending(self):
        now = 0
        def sleep(seconds):
            nonlocal now
            now += seconds
        result = tw.wait(self.root, [self.name], self.expected, timeout=2.5, sleep=sleep, monotonic=lambda: now)
        self.assertEqual("PENDING", result["state"])
        self.assertEqual(2.5, now)
        with self.assertRaisesRegex(tw.WaitError, "invalid_wait_bound"):
            tw.wait(self.root, [self.name], self.expected, timeout=61)

    def test_conflicting_done_and_blocked_fail_closed(self):
        self.write()
        blocked = "BLOCKED.batch.worker.md"
        self.write(self.signal.replace("DONE ", "BLOCKED ").replace("verdict=PASS", "verdict=BLOCKED reason=contradiction"), blocked)
        with self.assertRaisesRegex(tw.WaitError, "conflicting_matching_signals"):
            tw.wait(self.root, [self.name, blocked], self.expected, timeout=0)

    def test_outside_workspace_or_symlinks_are_rejected(self):
        for name in ("../DONE.other.md", str(self.root / self.name), "report.md"):
            with self.subTest(name=name), self.assertRaises(tw.WaitError):
                tw.wait(self.root, [name], self.expected, timeout=0)
        if os.name == "nt":
            return  # Windows symlinks need a separate privilege; path traversal above is portable.
        (self.root / self.name).symlink_to(self.root / "private-file")
        with self.assertRaisesRegex(tw.WaitError, "signal_symlink_rejected"):
            tw.wait(self.root, [self.name], self.expected, timeout=0)

    def test_receipt_stops_before_signal_read(self):
        with patch.dict(os.environ, {"RELAY_RECEIPT": ""}), patch.object(tw, "inspect") as inspect:
            with self.assertRaisesRegex(tw.WaitError, "relay_receipt_present"):
                tw.wait(self.root, [self.name], self.expected, timeout=0)
            inspect.assert_not_called()

    def test_cli_reports_pending_then_ready_with_native_exit_codes(self):
        command = [sys.executable, str(Path(tw.__file__)), "--root", str(self.root), "--signal", self.name, "--timeout", "0"]
        for k, v in self.expected.items():
            command.extend(["--" + k.replace("_", "-"), v])
        pending = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(3, pending.returncode, pending.stderr)
        self.assertEqual("PENDING", json.loads(pending.stdout)["state"])
        self.write()
        ready = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(0, ready.returncode, ready.stderr)
        self.assertEqual("READY", json.loads(ready.stdout)["state"])

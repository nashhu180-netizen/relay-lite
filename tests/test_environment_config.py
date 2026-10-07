"""Executable contract for the read-only relay-lite environment gate."""
from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))
import environment_config


ROOT = Path(__file__).resolve().parent.parent
TOOL = ROOT / "tools" / "environment_config.py"


class EnvironmentConfigTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        self.skill = Path(self.tempdir.name) / "skill"
        (self.skill / "references").mkdir(parents=True)
        (self.skill / "SKILL.md").write_text("skill\n", encoding="utf-8")
        (self.skill / "references" / "environment.md").write_text("protocol\n", encoding="utf-8")
        self.write_config()

    def tearDown(self) -> None:
        self.tempdir.cleanup()

    def write_config(self, text: str | None = None) -> None:
        (self.skill / "environments.toml").write_text(text or """version = 1
default = "test"

[environments.test]
protocol = "references/environment.md"

[environments.test.required_env]
TEST_ENV = "ready"
""", encoding="utf-8")

    def invoke(self, *args: str, env: dict[str, str] | None = None) -> tuple[int, dict]:
        runtime = {"PATH": os.environ.get("PATH", ""), **(env or {})}
        proc = subprocess.run([sys.executable, str(TOOL), "--skill-dir", str(self.skill), *args],
                              capture_output=True, text=True, env=runtime, check=False)
        self.assertEqual("", proc.stderr)
        return proc.returncode, json.loads(proc.stdout)

    def assert_blocked(self, reason: str, *args: str, env: dict[str, str] | None = None) -> None:
        code, payload = self.invoke(*args, env=env)
        self.assertEqual(2, code)
        self.assertEqual({"schema": environment_config.SCHEMA, "state": "BLOCKED", "reason": reason}, payload)

    def test_default_and_explicit_selection_real_cli(self) -> None:
        code, payload = self.invoke(env={"TEST_ENV": "ready"})
        self.assertEqual(0, code)
        self.assertEqual("READY", payload["state"])
        self.assertEqual("test", payload["environment"])
        self.assertEqual(str((self.skill / "environments.toml").resolve()), payload["config"])
        self.assertEqual(str((self.skill / "references/environment.md").resolve()), payload["protocol"])
        self.assertEqual(payload, json.loads(subprocess.check_output(
            [sys.executable, str(TOOL), "--skill-dir", str(self.skill), "--environment", "test"],
            env={"PATH": os.environ.get("PATH", ""), "TEST_ENV": "ready"}, text=True)))

    def test_unknown_empty_and_recovery_conflict_stop(self) -> None:
        self.assert_blocked("environment_unknown", "--environment", "other", env={"TEST_ENV": "ready"})
        self.assert_blocked("invalid_arguments", "--environment", "", env={"TEST_ENV": "ready"})
        self.assert_blocked("environment_conflict", "--expected", "other", env={"TEST_ENV": "ready"})

    def test_receipt_presence_precedes_environment_and_does_not_expose_value(self) -> None:
        code, payload = self.invoke(env={"RELAY_RECEIPT": "private-value", "TEST_ENV": "wrong"})
        self.assertEqual(2, code)
        self.assertEqual("relay_receipt_present", payload["reason"])
        self.assertNotIn("private-value", json.dumps(payload))

    def test_required_runtime_environment_is_strict_and_secret_free(self) -> None:
        self.assert_blocked("environment_required")
        code, payload = self.invoke(env={"TEST_ENV": "wrong-secret"})
        self.assertEqual(2, code)
        self.assertEqual("environment_required", payload["reason"])
        self.assertNotIn("wrong-secret", json.dumps(payload))

    def test_malformed_and_closed_schema_stop(self) -> None:
        self.write_config("version = 1\ndefault = \"test\"\n[environments.test]\nprotocol = \"references/environment.md\"\n")
        self.assert_blocked("configuration_invalid", env={"TEST_ENV": "ready"})
        self.write_config("version = 2\ndefault = \"test\"\n[environments.test]\nprotocol = \"references/environment.md\"\n[environments.test.required_env]\nTEST_ENV = \"ready\"\n")
        self.assert_blocked("configuration_invalid", env={"TEST_ENV": "ready"})
        self.write_config("version = 1\ndefault = \"other\"\n[environments.test]\nprotocol = \"references/environment.md\"\n[environments.test.required_env]\nTEST_ENV = \"ready\"\n")
        self.assert_blocked("configuration_invalid", env={"TEST_ENV": "ready"})
        self.write_config("version = 1\ndefault = \"test\"\nextra = true\n[environments.test]\nprotocol = \"references/environment.md\"\n[environments.test.required_env]\nTEST_ENV = \"ready\"\n")
        self.assert_blocked("configuration_invalid", env={"TEST_ENV": "ready"})

    def test_missing_protocol_and_path_escapes_stop(self) -> None:
        (self.skill / "references/environment.md").unlink()
        self.assert_blocked("protocol_missing", env={"TEST_ENV": "ready"})
        self.write_config("version = 1\ndefault = \"test\"\n[environments.test]\nprotocol = \"../outside.md\"\n[environments.test.required_env]\nTEST_ENV = \"ready\"\n")
        self.assert_blocked("protocol_path_invalid", env={"TEST_ENV": "ready"})
        outside = Path(self.tempdir.name) / "outside.md"
        outside.write_text("outside", encoding="utf-8")
        # Windows hosted CI may lack symlink permission; path traversal above
        # remains unconditional and does not weaken the same runtime guard.
        try:
            (self.skill / "references/environment.md").symlink_to(outside)
        except OSError:
            return
        self.write_config()
        self.assert_blocked("protocol_path_invalid", env={"TEST_ENV": "ready"})

    def test_missing_config_and_argument_syntax_are_fixed_json(self) -> None:
        (self.skill / "environments.toml").unlink()
        self.assert_blocked("configuration_missing", env={"TEST_ENV": "ready"})
        self.write_config()
        self.assert_blocked("invalid_arguments", "--nope", env={"TEST_ENV": "ready"})

    def test_repository_configuration_has_only_herdr(self) -> None:
        config = ROOT / "skill" / "environments.toml"
        import tomllib
        data = tomllib.loads(config.read_text(encoding="utf-8"))
        self.assertEqual(1, data["version"])
        self.assertEqual("herdr", data["default"])
        self.assertEqual({"herdr"}, set(data["environments"]))

    def test_invalid_default_rejected_even_with_valid_explicit_selection(self) -> None:
        text = (self.skill/'environments.toml').read_text().replace('default = "test"', 'default = "other"')
        self.write_config(text)
        self.assert_blocked("configuration_invalid", "--environment", "test", env={"TEST_ENV": "ready"})

    def test_version_types_and_duplicate_keys_are_not_coerced(self) -> None:
        base = (self.skill/'environments.toml').read_text()
        for value in ('true', '1.0', '"1"'):
            self.write_config(base.replace('version = 1', 'version = '+value))
            self.assert_blocked("configuration_invalid", env={"TEST_ENV": "ready"})
        self.write_config(base+'version = 1\nversion = 1\n')
        self.assert_blocked("configuration_invalid", env={"TEST_ENV": "ready"})

    def test_receipt_empty_is_rejected_before_configuration_read(self) -> None:
        (self.skill/'environments.toml').unlink()
        self.assert_blocked("relay_receipt_present", env={"RELAY_RECEIPT": ""})

    def test_other_registered_environment_selects_its_own_protocol(self) -> None:
        base = (self.skill/'environments.toml').read_text()
        (self.skill/'references/other.md').write_text('other protocol')
        self.write_config(base+'\n[environments.other]\nprotocol = "references/other.md"\n[environments.other.required_env]\nOTHER_ENV = "ready"\n')
        code, payload = self.invoke('--environment', 'other', env={'OTHER_ENV':'ready'})
        self.assertEqual(0, code)
        self.assertEqual('other', payload['environment'])
        self.assertEqual(str((self.skill/'references/other.md').resolve()), payload['protocol'])

    def test_all_registered_protocols_must_exist_before_any_selection(self) -> None:
        base = (self.skill/'environments.toml').read_text()
        self.write_config(base+'\n[environments.other]\nprotocol = "references/missing.md"\n[environments.other.required_env]\n')
        self.assert_blocked('protocol_missing', env={'TEST_ENV':'ready'})

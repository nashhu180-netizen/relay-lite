#!/usr/bin/env python3
"""Read and validate the relay-lite environment selection without side effects."""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import tomllib
from pathlib import Path, PureWindowsPath
from typing import Mapping


SCHEMA = "relay-lite.environment.v1"
_NAME = re.compile(r"[a-z][a-z0-9_-]*\Z")
_ENV_NAME = re.compile(r"[A-Z][A-Z0-9_]*\Z")


class ConfigError(Exception):
    def __init__(self, reason: str):
        self.reason = reason


class Parser(argparse.ArgumentParser):
    def error(self, message: str) -> None:
        raise ConfigError("invalid_arguments")


def _default_skill_dir() -> Path:
    here = Path(__file__).resolve().parent
    return here if (here / "SKILL.md").is_file() else here.parent / "skill"


def _require_string(value: object, *, name: str, pattern: re.Pattern[str] | None = None) -> str:
    if not isinstance(value, str) or not value or (pattern is not None and pattern.fullmatch(value) is None):
        raise ConfigError("configuration_invalid")
    return value


def _read_configuration(skill_dir: Path) -> tuple[dict[str, object], Path]:
    if not skill_dir.is_dir() or not (skill_dir / "SKILL.md").is_file():
        raise ConfigError("configuration_missing")
    config_path = skill_dir / "environments.toml"
    try:
        with config_path.open("rb") as handle:
            data = tomllib.load(handle)
    except FileNotFoundError:
        raise ConfigError("configuration_missing") from None
    except (OSError, tomllib.TOMLDecodeError):
        raise ConfigError("configuration_invalid") from None
    if not isinstance(data, dict) or set(data) != {"version", "default", "environments"}:
        raise ConfigError("configuration_invalid")
    if type(data["version"]) is not int or data["version"] != 1:
        raise ConfigError("configuration_invalid")
    _require_string(data["default"], name="default", pattern=_NAME)
    environments = data["environments"]
    if not isinstance(environments, dict) or not environments:
        raise ConfigError("configuration_invalid")
    for key, value in environments.items():
        _require_string(key, name="environment", pattern=_NAME)
        if not isinstance(value, dict) or set(value) != {"protocol", "required_env"}:
            raise ConfigError("configuration_invalid")
        _require_string(value["protocol"], name="protocol")
        required = value["required_env"]
        if not isinstance(required, dict):
            raise ConfigError("configuration_invalid")
        for env_name, expected in required.items():
            _require_string(env_name, name="required environment", pattern=_ENV_NAME)
            _require_string(expected, name="required environment value")
    if data["default"] not in environments:
        raise ConfigError("configuration_invalid")
    for definition in environments.values():
        _protocol_path(skill_dir, definition["protocol"])
    return data, config_path


def _protocol_path(skill_dir: Path, value: str) -> Path:
    relative = Path(value)
    if (relative.is_absolute() or PureWindowsPath(value).is_absolute() or "\\" in value
            or ".." in relative.parts or not relative.parts or relative.suffix != ".md"):
        raise ConfigError("protocol_path_invalid")
    try:
        root = skill_dir.resolve(strict=True)
        protocol = (root / relative).resolve()
        protocol.relative_to(root)
    except (OSError, ValueError, RuntimeError):
        raise ConfigError("protocol_path_invalid") from None
    if not protocol.is_file():
        raise ConfigError("protocol_missing")
    return protocol


def evaluate(skill_dir: Path, environment: str | None = None, expected: str | None = None,
             env: Mapping[str, str] | None = None) -> dict[str, str]:
    if env is None:
        env = os.environ
    if "RELAY_RECEIPT" in env:
        raise ConfigError("relay_receipt_present")
    data, config_path = _read_configuration(skill_dir)
    environments = data["environments"]
    assert isinstance(environments, dict)
    chosen = environment if environment is not None else data["default"]
    if not isinstance(chosen, str) or not chosen or _NAME.fullmatch(chosen) is None:
        raise ConfigError("invalid_arguments")
    if chosen not in environments:
        raise ConfigError("environment_unknown")
    if expected is not None and expected != chosen:
        raise ConfigError("environment_conflict")
    definition = environments[chosen]
    assert isinstance(definition, dict)
    required = definition["required_env"]
    assert isinstance(required, dict)
    if any(env.get(key) != value for key, value in required.items()):
        raise ConfigError("environment_required")
    protocol = _protocol_path(skill_dir, definition["protocol"])
    return {"schema": SCHEMA, "state": "READY", "environment": chosen,
            "config": str(config_path.resolve()), "protocol": str(protocol)}


def _result(reason: str | None = None, **values: str) -> dict[str, str]:
    if reason is not None:
        return {"schema": SCHEMA, "state": "BLOCKED", "reason": reason}
    return {"schema": SCHEMA, "state": "READY", **values}


def main(argv: list[str] | None = None) -> int:
    parser = Parser(description=__doc__)
    parser.add_argument("--skill-dir")
    parser.add_argument("--environment")
    parser.add_argument("--expected")
    try:
        args = parser.parse_args(argv)
        root = Path(args.skill_dir).resolve() if args.skill_dir is not None else _default_skill_dir()
        payload = evaluate(root, args.environment, args.expected)
    except (OSError, ValueError, RuntimeError):
        print(json.dumps(_result("configuration_invalid"), sort_keys=True))
        return 2
    except ConfigError as exc:
        print(json.dumps(_result(exc.reason), ensure_ascii=False, sort_keys=True))
        return 2
    print(json.dumps(payload, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())

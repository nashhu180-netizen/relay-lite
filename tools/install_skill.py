#!/usr/bin/env python3
"""Install the self-contained relay-lite skill from this independent repository.

Stdlib only. Explicit aliases synchronize the same single-card protocol to the
old discovery name; they never enable the retired full mode. Writes are not
atomic: failed copies leave a visible nonzero result and can be repaired by
rerunning after the cause is resolved. No background agent or runtime is started.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

SKILL_FILES = (
    "SKILL.md", "references/adapter-claude-code.md",
    "references/adapter-codex.md", "references/environment-herdr.md",
    "environments.toml", "roles.toml", "space_watch.py", "environment_config.py", "task_wait.py",
    "templates/card-chain.md",
)
SIDES = (".claude", ".codex", ".agents")
MANIFEST_NAME = "manifest.json"
RETIRED_FILES = ("dh-mapping.toml",)

class InstallError(Exception):
    """The package or installation could not be verified."""

def _targets_for_home(home: Path, legacy_alias: bool = False) -> list[Path]:
    names = ("relay-lite", "relay-light") if legacy_alias else ("relay-lite",)
    return [home / side / "skills" / name for name in names for side in SIDES]

def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def _copy_file(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dst)

def _git(source_dir: Path, *args: str) -> str | None:
    try:
        proc = subprocess.run(["git", "-C", str(source_dir), *args],
                              capture_output=True, text=True, timeout=15)
    except (OSError, subprocess.TimeoutExpired):
        return None
    return proc.stdout.strip() if proc.returncode == 0 else None

def _source_fields(source_dir: Path) -> dict:
    # Include both the package and its sibling observer source in provenance.
    dirty = _git(source_dir, "status", "--porcelain", "--", ".", "../tools/space_watch.py", "../tools/environment_config.py", "../tools/task_wait.py")
    return {"source_head": _git(source_dir, "rev-parse", "HEAD"),
            "source_dirty": None if dirty is None else bool(dirty)}

def _source_file(source_dir: Path, rel: str) -> Path:
    if rel in {"space_watch.py", "environment_config.py", "task_wait.py"} and not (source_dir / rel).is_file():
        return source_dir.parent / "tools" / rel
    return source_dir / rel

def _retired_managed_files(target: Path) -> list[Path]:
    present = [target / rel for rel in RETIRED_FILES if (target / rel).exists()]
    if not present:
        return []
    try:
        manifest = json.loads((target / MANIFEST_NAME).read_text(encoding="utf-8"))
        files = manifest["files"]
        if not isinstance(files, dict):
            raise ValueError("invalid files")
    except (OSError, ValueError, KeyError, TypeError):
        raise InstallError("retired file has no trustworthy managed manifest") from None
    for path in present:
        if not path.is_file() or files.get(path.name) != _sha256(path):
            raise InstallError("retired managed file changed; preserve and resolve explicitly")
    return present

def _sync_target(source_dir: Path, target: Path) -> Path:
    retired = _retired_managed_files(target)
    for rel in SKILL_FILES:
        _copy_file(_source_file(source_dir, rel), target / rel)
    files = {}
    for rel in SKILL_FILES:
        digest = _sha256(_source_file(source_dir, rel))
        if _sha256(target / rel) != digest:
            raise InstallError(f"hash mismatch after copy: {rel}")
        files[rel] = digest
    for path in retired:
        path.unlink()
    manifest = {**_source_fields(source_dir), "files": files,
                "installed_to": str(target), "installed_at": datetime.now(timezone.utc).isoformat()}
    out = target / MANIFEST_NAME
    out.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return out

def install_all(source_dir: Path, home: Path, legacy_alias: bool = False) -> list[Path]:
    missing = [rel for rel in SKILL_FILES if not _source_file(source_dir, rel).is_file()]
    if missing:
        raise InstallError("skill source incomplete, missing: " + ", ".join(missing))
    targets = _targets_for_home(home, legacy_alias)
    # Preserve unexpected local changes before touching any target.
    for target in targets:
        _retired_managed_files(target)
    return [_sync_target(source_dir, target) for target in targets]

def main(argv: list[str] | None = None, *, home: Path | None = None,
         source_dir: Path | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--all", action="store_true", required=True)
    parser.add_argument("--legacy-alias", action="store_true",
                        help="also synchronize the relay-light discovery alias")
    args = parser.parse_args(argv)
    source = source_dir or Path(__file__).resolve().parent.parent / "skill"
    try:
        outputs = install_all(source, home or Path.home(), args.legacy_alias)
    except (InstallError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    for output in outputs:
        print(f"installed: {output.parent}")
    return 0

if __name__ == "__main__":
    sys.exit(main())

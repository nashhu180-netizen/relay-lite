"""Migration conservation and standalone package boundaries."""
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import tomllib
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'tools'))
import install_skill

ROOT = Path(__file__).resolve().parent.parent
DOCS = ('SKILL.md', 'references/adapter-codex.md', 'references/adapter-claude-code.md')

class MigrationTests(unittest.TestCase):
    def test_inventory_exactly_matches_preconstruction_plan(self):
        actual = json.loads((ROOT/'docs/migration-inventory.json').read_text(encoding='utf-8'))
        plan = json.loads((ROOT/'docs/modules/relay-lite/workspace/33-RLT_33-independent/migration-plan.json').read_text(encoding='utf-8'))
        self.assertEqual(plan['source_sha'], actual['source_sha'])
        expected = {r['source']:r['sha256'] for r in plan['files']}
        self.assertEqual(len(plan['files']), len(expected))
        self.assertEqual(expected, {r['source']:r['sha256'] for r in actual['files']})
        for row in actual['files']:
            if row['target'] is not None:
                self.assertEqual(hashlib.sha256((ROOT/row['target']).read_bytes()).hexdigest(), row['sha256'], row['source'])
            else:
                self.assertEqual('retired_at_source_sha', row['disposition'])

    def test_active_table_bodies_preserve_all_authorization_and_status_bytes(self):
        plan = json.loads((ROOT/'docs/modules/relay-lite/workspace/33-RLT_33-independent/migration-plan.json').read_text(encoding='utf-8'))
        tables = [r for r in plan['files'] if r['new_active']]
        cutover = json.loads((ROOT/'docs/table-cutover.json').read_text(encoding='utf-8'))
        latest = {r['source']:r for r in cutover['tables']}
        self.assertEqual(2, len(tables))
        for row in tables:
            new = (ROOT/row['new_active']).read_bytes()
            header, body = new.split(b'\n\n',1)
            self.assertIn('迁移'.encode(), header)
            extra = latest.get(row['source'])
            original = ROOT/(extra['snapshot'] if extra else row['archive'])
            self.assertEqual(original.read_bytes(),body,row['source'])
            if extra:
                self.assertEqual(extra['sha256'],hashlib.sha256(body).hexdigest())

class PackageTests(unittest.TestCase):
    def test_roles_and_new_dispatch_use_executor(self):
        roles = tomllib.loads((ROOT/'skill/roles.toml').read_text(encoding='utf-8'))
        self.assertEqual({'orchestrator','builder','plan-reviewer','executor','batch-reviewer','reviewer','decider','watcher'},set(roles))
        self.assertIn('gpt-6.1-sol',roles['executor']['launch'])
        for rel in DOCS:
            text = (ROOT/'skill'/rel).read_text(encoding='utf-8')
            self.assertIn('[relay-lite:single-task]',text)
            self.assertIn('builder/executor/reviewer/decider',text)
            self.assertNotIn('builder/coder/',text)
            for retired in ('stage-lead','<RELAY_LOG>','## 五阶段','## 账本用法','[relay-lite] worker · node='):
                self.assertNotIn(retired,text)
            for field in ('review_round','remediation_count','RELAY_RECEIPT','execution_strategy.md'):
                self.assertIn(field,text)
        self.assertFalse((ROOT/'tools/relay_log.py').exists())
        self.assertFalse((ROOT/'skill/dh-mapping.toml').exists())

    def test_isolated_package_installs_and_observer_help_runs_without_source_checkout(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)/'standalone';root.mkdir()
            for folder in ('skill','tools'):
                shutil.copytree(ROOT/folder,root/folder,ignore=shutil.ignore_patterns('__pycache__'))
            home=Path(tmp)/'home';home.mkdir()
            code=("import sys; from pathlib import Path; "
                  "sys.path.insert(0,'tools'); import install_skill; "
                  "raise SystemExit(install_skill.main(['--all'],home=Path(sys.argv[1])))")
            proc=subprocess.run([sys.executable,'-c',code,str(home)],cwd=root,capture_output=True,text=True)
            self.assertEqual(0,proc.returncode,proc.stderr)
            for target in install_skill._targets_for_home(home):
                files={str(f.relative_to(target)).replace('\\','/') for f in target.rglob('*') if f.is_file()}
                self.assertEqual(set(install_skill.SKILL_FILES)|{'manifest.json'},files)
                manifest=json.loads((target/'manifest.json').read_text(encoding='utf-8'))
                self.assertIsNone(manifest['source_head']) # no Git or old checkout required
                proc=subprocess.run([sys.executable,str(target/'space_watch.py'),'--help'],cwd=tmp,capture_output=True,text=True)
                self.assertEqual(0,proc.returncode,proc.stderr)
                self.assertTrue((target/'templates/card-chain.md').is_file())
                self.assertFalse((target/'archive').exists())
                for doc in ('SKILL.md','references/adapter-codex.md','references/adapter-claude-code.md','templates/card-chain.md'):
                    text=(target/doc).read_text(encoding='utf-8')
                    self.assertNotIn('/home/nash/work/dh-relay',text)
                    self.assertNotIn('tools/relay-light/',text)

    def test_legacy_alias_is_explicit_and_removes_only_unchanged_managed_retired_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            home=Path(tmp);old=home/'.codex/skills/relay-light';old.mkdir(parents=True)
            stale=old/'dh-mapping.toml';stale.write_text('old mapping',encoding='utf-8')
            digest=hashlib.sha256(stale.read_bytes()).hexdigest()
            (old/'manifest.json').write_text(json.dumps({'files':{'dh-mapping.toml':digest}}))
            install_skill.install_all(ROOT/'skill',home)
            self.assertTrue(stale.exists())
            unrelated=old/'user-notes.md';unrelated.write_text('user data')
            targets=install_skill.install_all(ROOT/'skill',home,legacy_alias=True)
            self.assertEqual(6,len(targets));self.assertFalse(stale.exists());self.assertTrue(unrelated.exists())
            for output in targets:
                target=output.parent
                self.assertEqual((ROOT/'skill/SKILL.md').read_bytes(),(target/'SKILL.md').read_bytes())

    def test_changed_or_unmanaged_retired_file_preserved_without_mutating_any_target(self):
        for managed in (False,True):
            with tempfile.TemporaryDirectory() as tmp:
                home=Path(tmp);old=home/'.codex/skills/relay-light';old.mkdir(parents=True)
                stale=old/'dh-mapping.toml';stale.write_text('local edits')
                if managed:
                    (old/'manifest.json').write_text(json.dumps({'files':{'dh-mapping.toml':'0'*64}}))
                self.assertNotEqual(0,install_skill.main(['--all','--legacy-alias'],home=home))
                self.assertEqual('local edits',stale.read_text())
                self.assertFalse((home/'.claude/skills/relay-lite').exists())

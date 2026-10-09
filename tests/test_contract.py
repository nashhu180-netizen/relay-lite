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
            extra = latest.get(row['source'])
            self.assertIsNotNone(extra)
            imported = extra['import_commit']
            self.assertRegex(imported,r'\A[0-9a-f]{40}\Z')
            subprocess.run(['git','merge-base','--is-ancestor',imported,'HEAD'],cwd=ROOT,check=True,capture_output=True)
            new = subprocess.check_output(['git','show',f"{imported}:{row['new_active']}"],cwd=ROOT)
            self.assertTrue((ROOT/row['new_active']).is_file())
            header, body = new.split(b'\n\n',1)
            self.assertIn('迁移'.encode(), header)
            original = ROOT/extra['snapshot']
            self.assertEqual(original.read_bytes(),body,row['source'])
            self.assertEqual(extra['sha256'],hashlib.sha256(body).hexdigest())

class PackageTests(unittest.TestCase):
    def test_new_task_clear_is_a_predispatch_gate(self):
        core = (ROOT/'skill/SKILL.md').read_text(encoding='utf-8')
        title = '### 新批次与新任务的标签页会话清理闸'
        self.assertEqual(1, core.count(title))
        gate = core.split(title, 1)[1].split('\n### ', 1)[0]
        new_task = next(line for line in gate.splitlines() if line.startswith('- **新的独立任务**'))
        self.assertIn('先 clear 并确认，再投递新派单', new_task)
        self.assertIn('工件、证据与原角色 signal 已保存', new_task)
        self.assertIn('重新读取新任务的 AGENTS、精确派单与指定 workspace', new_task)
        self.assertIn('不能沿用前任务授权或写权', new_task)
        for guard in ('durable signal 为 PASS', '本批工件齐全', '各执行一次 `/clear`',
                      '分别复验已清理', '与新派单分两次投递', '已核实支持的原生会话清理命令',
                      '清理失败或结果未知时不投递新任务、不盲重发',
                      'FAIL/整改期间禁止 `/clear`', 'E2 targeted attempt 2 沿用原会话',
                      '不能把旧实例 `/clear` 后冒充 fresh', 'watcher 常驻、不 clear',
                      '不清除 `RELAY_*`', '不为未闭合原任务放行或重置额度'):
            with self.subTest(guard=guard):
                self.assertIn(guard, gate)

    def test_both_adapters_require_clear_before_dispatch(self):
        for rel in DOCS[1:]:
            text = (ROOT/'skill'/rel).read_text(encoding='utf-8')
            with self.subTest(adapter=rel):
                self.assertIn('「新批次与新任务的标签页会话清理闸」', text)
                self.assertIn('确认清理成功后再投递派单文件指针', text)
                self.assertIn('清理命令与派单不可合并', text)
                self.assertIn('失败或未知不派新单、不盲重发', text)

    def test_environment_gate_is_shared_before_carrier_commands(self):
        config = tomllib.loads((ROOT/'skill/environments.toml').read_text(encoding='utf-8'))
        self.assertEqual('herdr', config['default'])
        self.assertEqual({'herdr'}, set(config['environments']))
        protocol = ROOT/'skill'/config['environments']['herdr']['protocol']
        self.assertTrue(protocol.is_file())
        for rel in DOCS:
            text = (ROOT/'skill'/rel).read_text(encoding='utf-8')
            self.assertIn('environment_config.py', text, rel)
            self.assertIn('非零退出', text, rel)
            self.assertIn('--expected', text, rel)
            self.assertIn('protocol', text, rel)
            self.assertNotIn('herdr agent start', text, rel)
            self.assertNotIn('herdr tab create', text, rel)
            self.assertNotIn('herdr agent prompt', text, rel)
        text = protocol.read_text(encoding='utf-8')
        self.assertLess(text.index('herdr --skill'), text.index('herdr workspace create'))
        self.assertLess(text.index('herdr workspace create'), text.index('herdr tab create'))
        self.assertLess(text.index('herdr tab create'), text.index('herdr agent start'))
        for guard in ('交互式 agent', '原生清理成功', '不盲重发', 'HERDR_ENV', 'RELAY_RECEIPT'):
            self.assertIn(guard, text)

    def test_watcher_lifecycle_is_common_to_all_kinds(self):
        core = (ROOT/'skill/SKILL.md').read_text(encoding='utf-8')
        shared = core.split('#### watcher 通用启动与监控步骤', 1)[1].split('### 恢复依据', 1)[0]
        for guard in ('所有 agent 共用同一 watcher 合同', '真实子进程句柄', '确认接管',
                      '每 120 秒', '排除 watcher 自身和主编排', '不按 kind',
                      '无变化静默', '退出只一次通知', '不自动重拉', '完全只读',
                      'durable signal', '所有 kind 通用'):
            self.assertIn(guard, shared)
        self.assertNotIn('write_stdin', shared)
        self.assertNotIn('run_in_background', shared)
        for rel in DOCS[1:]:
            text = (ROOT/'skill'/rel).read_text(encoding='utf-8')
            self.assertIn('watcher 通用启动与监控步骤', text)
            self.assertIn('所有 agent 的监控规则相同', text)
            self.assertNotIn('herdr agent prompt', text)

    def test_host_process_handles_are_kept_in_their_adapters(self):
        codex = (ROOT/'skill/references/adapter-codex.md').read_text(encoding='utf-8')
        claude = (ROOT/'skill/references/adapter-claude-code.md').read_text(encoding='utf-8')
        for guard in ('session_id', 'write_stdin', 'Script running with cell ID',
                      '不是脚本 session_id', 'await tools.exec_command', '真实返回', '不超过60秒'):
            self.assertIn(guard, codex)
        for guard in ('run_in_background=true', 'task_id', '立即', '不超过60秒'):
            self.assertIn(guard, claude)

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
                proc=subprocess.run([sys.executable,str(target/'task_wait.py'),'--help'],cwd=tmp,capture_output=True,text=True)
                self.assertEqual(0,proc.returncode,proc.stderr)
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

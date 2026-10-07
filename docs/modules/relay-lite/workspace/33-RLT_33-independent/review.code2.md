# RLT_33 独立代码轮 2

审阅者：fresh context `code_review2`；未参与实施或代码轮 1。Review Batch：`RB-RLT33-2`。本报告只审当前候选，不构成需求/一致性/教训/人验、PR/CI、合入或 verify 放行。

审阅对象：独立仓候选 `db18185b160c653eebe2121727b9f9f85c22716b`（相对初始 `60bc7ea`）；源仓迁出候选 `d8f88ae948ae6767daea4dae491eea5b292b07e6`（相对冻结源 `2246b16cb82f86a594f7b2c36365e7851fe11263`）。

## 覆盖与证据

- 独立读取仓根 `AGENTS.md`、本卡 `brief.md`/`task_plan.md`、设计 RL33-M1～M6、P1 和代码轮 1；逐项复核独立安装包、源仓退役入口、迁移库存/两份现役总表、两 adapter 与 watcher。
- 安装器：`tools/install_skill.py` 的 `--legacy-alias` 只在显式请求时同步 `relay-light`；对已安装的受管 `dh-mapping.toml` 先按 manifest/hash 验证后删除，改动或无可信 manifest 时在复制任何 target 前失败，且不删除其它用户文件。新包自身只含闭集 `SKILL.md`、两 adapter、`roles.toml`、watcher 和总表模板；孤立安装也不复制 archive。
- 权限/身份：新派单和 `roles.toml` 使用 `executor`，核心和 adapter 的 model-allocation gate 与实际 launch 均为 watcher `gpt-6-luna/medium`、executor/batch-reviewer `gpt-6.1-sol/high`、decider `gpt-6-astra/medium`、reviewer `gpt-6.1-sol/high`。旧 `coder` signal、旧单卡标头和两份总表正文保留为只读历史；新实例不得复用其模型确认。`RELAY_RECEIPT`、watcher 零写入、独立 signal、复核/人验及自动接续权限闸均仍在现役协议和两 adapter 中。
- 源仓：`tools/tests/relay-light-log.ps1` 只断言产品目录已迁出、无重复现役 `relay_plan.md`、迁移目的地可定位；未删除 Runner 汇总入口或把产品检查改成静默 skip。实跑 `pwsh -NoProfile -File tools/tests/relay-light-log.ps1`，输出 `SUITE PASS relay-lite retirement boundary`，退出 0。
- 独立仓实跑 `python3 -m unittest discover -s tests -v`：39 tests，退出 0。覆盖孤立包安装、manifest、三侧目标、显式旧别名、已管理旧 `dh-mapping.toml` 的受保护删除、失败前全 target 预检、watcher 动态发现/投递确认/环境拒绝和 archive/迁移字节约束。

## Findings

| 级别 | 结论 |
|---|---|
| P0 | 无 |
| P1 | 无 |
| P2 | 无 |
| P3 | 无 |

## 有效变异点（仅指定，未执行）

- 生产点：`tools/install_skill.py`，`install_all()` 的第 100–102 行，精确地将预检循环 `for target in targets: _retired_managed_files(target)` 删除，直接执行 `return [_sync_target(source_dir, target) for target in targets]`。
- 指定测试：`tests/test_contract.py::PackageTests::test_changed_or_unmanaged_retired_file_preserved_without_mutating_any_target`。
- 预期 RED：含未受管或已改动 `relay-light/dh-mapping.toml` 的 `--legacy-alias` 安装会先创建/更新前序 `relay-lite` target，违反该测试的业务断言 `self.assertFalse((home/'.claude/skills/relay-lite').exists())`；测试必须失败。该点验证“冲突旧别名不改变任何 target”的安装隔离，而非仅验证异常退出。

## Verdict

`PASS`：候选满足本轮独立代码审阅所覆盖的安装器旧别名/manifest 保护、现役与 archive 的独立性、旧协议权限语义保留及源仓退役测试耦合处理。仍须按 heavy 卡合同完成同批其它独立路径、指定变异的实际 RED→精确恢复→GREEN，以及后续 PR/CI/合入态复验和 verify。

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

## 定向补充：最新 AW 总表切换候选

审阅范围仅限本工作树尚未提交的 `docs/table-cutover.json`、AW 现役表候选、`live-source-table-5a47a4f9.md` / readback 证据及 `tests/test_contract.py` 的表体校验；不复审产品代码，不改变冻结的 948 条库存。

- `table-cutover.json` 锁定源 `5a47a4f98d01e77f9a78994765dc59d8b54dd6a5` 和 AW 表快照 SHA256 `b8a7a5aa6729ba3d5355132b72c8f5f3466de7afbfaf31530c2449df5f7343d5`。独立以 `git show 5a47a4f:<AW 表路径>` 复算，和快照字节相同。
- 新 AW 表只新增迁移候选头；移除该头后的表体与上述快照逐字节一致，故原状态、自动接续授权、维护会话、历史通知和旧 `coder` 正文均未被重写。切换清单现也显式列出 WFP：其 snapshot 指向原 archive，SHA256 `e91b6125dcba63eef6adc8298339bd607a8e89aaf5ffde3832931bb7e584221f` 同时匹配冻结源和本地主树 `5a47a4f`；WFP 候选头同样写明待原维护者确认、旧表仍权威且禁止并写。`test_inventory_exactly_matches_preconstruction_plan` 仍确认 948 条冻结库存未变。
- `test_active_table_bodies_preserve_all_authorization_and_status_bytes` 现在从 `table-cutover.json` 为明确列出的 AW 表选择额外快照并核对 SHA256，未列出的 WFP 表仍取原 archive。独立复跑 `python3 -m unittest discover -s tests -v`：39 tests / exit 0；另以相同选择逻辑复算两份现役表体，均匹配各自授权快照。
- 切换清单和两份候选头均明确 `pending_maintainer_ack`：向 AW、WFP 的原维护者通知均因 active writer 未送达，旧 dh-relay 表仍是权威，候选不得并写或合入。该状态与用户本次迁最新并协调原维护者的边界相符，不将未送达通知写成确认。

| 级别 | 结论 |
|---|---|
| P0 | 无 |
| P1 | 无 |
| P2 | 无 |
| P3 | 无 |

定向结论：`PASS`（仅表切换候选与其测试/证据）。此结论不解除 `pending_maintainer_ack`，不把新表宣布为权威，也不放行合并。

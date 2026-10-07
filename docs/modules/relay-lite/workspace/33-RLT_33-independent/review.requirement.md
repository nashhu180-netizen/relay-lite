# RLT_33 · 需求方向独立复核

审阅者：fresh-context `requirement_review`（未参与实施）。审阅对象：独立仓候选 `db18185b160c653eebe2121727b9f9f85c22716b`，源仓候选 `d8f88ae948ae6767daea4dae491eea5b292b07e6`，冻结源 `2246b16cb82f86a594f7b2c36365e7851fe11263`。本轮为侦测型只读复核（环境没有机器只读隔离）；未重跑测试、未修改产品或既有工件。本报告只判断当前候选与原始需求的对应关系，不代替整卡验收、人验、其它 heavy 复核路径、PR/CI、合入或 verify。

## 需求逐项核对

| 原始需求 | 现态证据 | 结论 |
|---|---|---|
| coder 改为简洁英文执行者 | `skill/SKILL.md`「角色与术语」把 `executor` 定义为获授权执行者；`skill/roles.toml`、两份 adapter 的新派单均用 `[relay-lite:single-task]` 和 `executor`。`SKILL.md` 的存量兼容节只将旧 `coder` 留为历史 signal/模型确认的只读身份，要求登记映射且禁止改写。`tests/test_contract.py::test_roles_and_new_dispatch_use_executor` 对此有结构断言；现有 `evidence/isolated-clone-tests.log` 记录 39 tests / OK。 | PASS |
| 删除完整模式，只保留单卡分工和接力计划 | `skill/SKILL.md` 开头明确仅提供单卡接力；`docs/relay/README.md` 仅定义卡级总表；`README.md` 明示无账本、五阶段或阶段主管。`tests/test_contract.py` 同时断言现役 docs/adapter 不含 `stage-lead`、五阶段、账本命令或旧 node 标头，且 `tools/relay_log.py`、`skill/dh-mapping.toml` 不存在。源候选相对冻结源删除 `tools/relay-light/relay_log.py`、完整模式 skill/config 与旧执行计划，并将 `docs/relay/README.md` 改为迁出指针。旧完整计划保留在 `archive/dh-relay/`，`docs/migration.md` 明定只读、不启动、不代关闭业务卡。 | PASS |
| 独立目录/仓库，不耦合 dh-relay | 新仓根 `AGENTS.md`、`README.md` 和 `docs/migration.md` 都声明 relay-lite 为独立产品入口；安装闭集是 `SKILL.md`、两 adapter、`roles.toml`、watcher、总表模板。`tests/test_contract.py::test_isolated_package_installs_and_observer_help_runs_without_source_checkout` 将仅 `skill/`、`tools/` 复制到临时 standalone 目录，再以临时 home 安装三侧包，断言 manifest 无 Git/source checkout、安装包不带 archive、文档不含 `/home/nash/work/dh-relay` 或 `tools/relay-light/`，并运行 watcher `--help`。该测试的现有孤立 clone 证据为 `evidence/isolated-clone-tests.log`（39 tests / OK）。归档仍含 `archive/dh-relay/` 是历史保存，不作为安装包或现役运行依赖；与独立边界一致。 | PASS |
| 建 Issue 后开工 | 新仓 `design/01-产品设计与验收.md`、`dev_plan/P1-独立交付.md` 和本卡 `brief.md` 均记录 relay-lite #1 与源仓 #156，并逐字引用用户 2026-10-07「建个issue 后开工」。`execution_strategy.md` 记录两仓 Draft PR 编号；这与当前本地 `origin/wt/RLT_33-issue-1` 尚停在较早 SHA 的事实分开，不把远端推送/CI/合入冒充完成。 | PASS（开工顺序已落档；远端交付仍是未闭合闸） |
| 不扩到设计 #154；不改历史、人验或授权 | 本卡 `brief.md` 和 `design/01-产品设计与验收.md` 均明确不实施 #154、也不代收口其它卡。源候选相对 `2246b16` 的 diff 未触及 `docs/modules/relay-light/design/01-RelayLight-产品设计与验收.md`；它只将 design/dev-plan 入口改为迁出/历史说明。两份现役总表的迁移规则由 `tests/test_contract.py::test_active_table_bodies_preserve_all_authorization_and_status_bytes` 约束为新增迁移头后的正文逐字等于 archive；`docs/migration.md` 亦明确不变更原卡授权、人验、运行中 pane 或原 signal。 | PASS |

## Findings

| 级别 | 结论 |
|---|---|
| P0 | 无 |
| P1 | 无 |
| P2 | 无 |
| P3 | 无 |

## Verdict

`PASS`：当前候选完整承接用户的四项原始要求，并保留历史、授权与人验边界，未见扩入 #154 的实现性修改。独立安装边界有当前候选的孤立 clone 测试记录和可读结构测试支撑。

仍未闭合的整卡事项按任务合同保留：fresh 代码轮 2、一致性、教训、有效变异 RED→恢复 GREEN、两仓远端 PR/必需 CI/合入态复验及 `verify(relay-lite)`；本报告不以本轮 PASS 代替这些闸门。

## 2026-10-07 定向补充：最新总表切换

复核对象为当前未提交补充，不重跑测试。用户新增决定是“本次迁移最新总表，并协调原维护会话切换新仓”；其范围只覆盖总表版本选择与交接协调，不授予合入、清理、代替维护者确认或改写 AW_07 业务状态的权限。

- **状态与历史保真：PASS。** `table-cutover.json` 现列两表；冻结 `migration-plan.json`、`migration-inventory.json` 与 `archive/**` 未改。独立读回源主树 `5a47a4f98d01e77f9a78994765dc59d8b54dd6a5`：AW 表 SHA256 为 `b8a7a5aa6729ba3d5355132b72c8f5f3466de7afbfaf31530c2449df5f7343d5`，与额外快照相同；WFP 表 SHA256 为 `e91b6125dcba63eef6adc8298339bd607a8e89aaf5ffde3832931bb7e584221f`，与冻结 archive 相同。两候选表正文经迁移候选头后逐字等于各自列明的快照；`tests/test_contract.py` 的扩展断言以对应快照校验正文与 hash。
- **权限与停止线：PASS，且仍受阻。** 两个候选页头、`brief.md`、`migration.md` 和 `progress.md` 一致写明 `pending_maintainer_ack`：旧仓表在确认前仍权威、候选表禁止并写、两 PR 不合入且不清理。`table-cutover.json` 对 `AW_07 orchestrator#2` 与 `WFP_08 orchestrator` 均记录 active writer、未送达及 `ack=null`；没有把任一未送达尝试写成已交接，也没有向 Herdr pane 施加外部控制。`review.md` 的 RL33-M5 同步降为“冻结 archive PASS、现役 cutover 待确认”，未冒称切换完成。

| 级别 | 定向补充 finding |
|---|---|
| P0 | 无 |
| P1 | 无 |
| P2 | 无；维护者确认缺失是明确的合入/清理停止条件，不是可忽略的通过项。 |
| P3 | 无 |

**定向结论：PASS（候选与用户此次切换决定一致）。** 维护者确认仍为未闭合依赖；在收到可核查回执并按其内容完成旧表停写/新路径登记前，保持 `pending_maintainer_ack`、旧表权威和 Draft/不合入状态。本结论不代替该交接、整卡验收或任何既有出口闸。

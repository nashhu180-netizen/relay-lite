<!-- dh:v1 -->
# RLT_33 一致性独立复核

范围：RB-RLT33-2 的 consistency 路径。独立未施工实例只读审查新仓 `db18185b160c653eebe2121727b9f9f85c22716b` 与源仓 `d8f88ae948ae6767daea4dae491eea5b292b07e6`；未作 commit、push、远端/Herdr 实操或整卡验收。本报告不是其它复核路径、CI、verify 或人验的替代物。

## 结论

**PASS（本一致性路径）**。已核现役协议的 executor 角色、九值 phase、signal schema、写者边界、模型确认闸、单卡与旧完整模式的互斥、总表维护授权，以及两仓迁出分工。发现数：P0=0、P1=0、P2=0、P3=0。

| 核项 | 具体事实与反例核查 | 评级 | 结论 |
| --- | --- | --- | --- |
| 现役角色与存量身份 | `skill/roles.toml` 现役角色集含 `executor` 而无 `coder`；`skill/SKILL.md` 说明旧 coder signal 仅历史读取、不得改写或跨实例复用。`tests/test_contract.py::test_roles_and_new_dispatch_use_executor` 同时断言两 adapter 使用新标头/`executor`，并否定 `builder/coder/`。 | P0–P3：0 | 一致。 |
| phase、signal 与 receipt 分流 | 两 adapter 的 phase 闭集均为 `plan`、`plan-review`、`batch`、`batch-review`、`workflow-final`、`e2-code-review`、`decision`、`watcher`、`human-acceptance`；同段给出 `DONE|BLOCKED` 的 task/phase/agent/batch/path/review_round/remediation_count/verdict/evidence schema。`RELAY_RECEIPT` 下产出角色只写精确 BLOCKED，而 watcher 保持零写入并只作非 durable 通知。结构测试 `test_phase_closed_set_is_nine_phases_not_legacy_five`、`test_durable_signal_schema_and_stop`、`test_relay_receipt_fail_closed_split_watcher_vs_producers` 均通过。 | P0–P3：0 | 一致且有反例约束。 |
| 写权与模型 gate | `skill/SKILL.md` 将编排、executor/reviewer、watcher 的职责区分；adapter `决定落点与写者` 限定 `execution_strategy.md`、`findings.md`、`progress.md`、`lesson_candidates.md` 的写者。adapter `启动前 model-allocation gate` 要求模型与推理档先获用户明确确认，实态登记在 `execution_strategy.md`；结构测试覆盖 gate 的硬合同与先后顺序。 | P0–P3：0 | 一致。 |
| 单卡/旧完整模式互斥 | `skill/SKILL.md` 明示旧完整标头/计划不受支持且 archive 只读；`tests/test_contract.py` 检查现役 skill/adapter 不含 `stage-lead`、`<RELAY_LOG>`、五阶段、账本用法或旧 node 标头，且 `tools/relay_log.py` 与 `skill/dh-mapping.toml` 不存在。对照 `/tmp/rlt33-frozen-source` 的 `AGENTS.md` 仍含 stage-lead 与账本，说明新旧边界是有意迁移而非漏搜。 | P0–P3：0 | 互斥明确。 |
| 卡级总表 | `skill/SKILL.md` 规定每表只有登记的维护会话写入，worker/reviewer/decider/watcher 默认不得写；自动接续栏只由用户写定，维护会话只在列明条件与模型档齐备时执行有限开局步骤。两份现役 `docs/relay/**/relay_plan.md` 均声明是人工维护的卡级衔接总表、不是 `relay_log.py` 执行计划；`test_active_table_bodies_preserve_all_authorization_and_status_bytes` 通过。 | P0–P3：0 | 授权与写权一致。 |
| 两仓迁出分工 | 新仓 `docs/migration-inventory.json` 与 workspace `migration-plan.json` 的清单/hash 由 `test_inventory_exactly_matches_preconstruction_plan` 覆盖；隔离安装测试确认不依赖旧 checkout。源仓 `tools/tests/relay-light-log.ps1` 反例断言 `tools/relay-light` 和源 `relay_plan.md` 均不得残留，并要求迁出链接；源 PowerShell 证据 `evidence/source-pwsh-final.log` 记录该 suite PASS。 | P0–P3：0 | 职责分割一致，未见双写入口。 |

## 本次核验

- 在新仓上述 HEAD 执行 `python3 -m unittest discover -s tests -v`：39 tests，PASS。
- 新、源仓均执行 `git diff --check`：无输出。
- 限制：未访问 GitHub Actions 的最终结论，未启动 Herdr/真实 worker，也未执行合入、verify 或人验；这些均不在本侦测型只读路径的可核范围内。

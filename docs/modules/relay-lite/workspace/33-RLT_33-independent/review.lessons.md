<!-- dh:v1 -->
# RLT_33 教训独立复核

范围：RB-RLT33-2 的 lessons 路径。独立未施工实例只读查阅 archive 的 relay-light 历史候选/复核、RLT_33 候选与现有证据；未改变正式教训库、产品、历史失败或任务结论。

## 结论

**PASS（本教训路径）**。适用的既有教训已经被本卡的迁移闭集、静态反例、隔离测试或保留的证据覆盖。RLT_33 的 L1/L2 是本卡实施线索，均有对应执行证据；不将已明确失效的旧活动树基线当作 RED。发现数：P0=0、P1=0、P2=0、P3=0。

| 适用教训/候选 | 本卡如何落实 | 评级 | 结论 |
| --- | --- | --- | --- |
| RLT_30 L-02：基线须由可核 SHA 取得，不能手抄会话快照 | `task_plan.md` 固定来源为 `2246b16...`，并要求迁移清单逐项含 source/sha256；`tests/test_contract.py::test_inventory_exactly_matches_preconstruction_plan` 实测 source SHA、清单唯一性和目标 hash。`evidence/frozen-baseline.log` 的相关 44 tests 是在冻结 Git 副本运行。 | P2 防回归；本轮 P0–P3：0 | 已覆盖。 |
| RLT_29 L-02/L-03：按角色分流 fail-closed，sole-writer 不可形成越权或死锁 | 当前 `skill/SKILL.md` 将 watcher 零写入与 producer BLOCKED 分开；adapter 明定总表只由维护会话写、worker/reviewer/decider/watcher 默认不得写，并对 findings/progress/lesson candidates 分配唯一写者。结构测试覆盖 receipt 分流、watcher 零写入和 signal schema。 | P1/P2 防回归；本轮 P0–P3：0 | 已覆盖。 |
| RLT_29 L-05：回显/退出码不等于真实投递，Enter 必须有界 | 两 adapter 的 watcher 条款要求同 pane、`working`、`state_change_seq` 同时确认，未知投递不得重发；安全 Enter 仅三条件同真且只一次。`tests/test_space_watch.py` 覆盖 `accepted_stalled_not_delivery`、`seq_advance_without_working_is_unconfirmed` 与拒绝/超时不发送 Enter 的反例。 | P2 防回归；本轮 P0–P3：0 | 已覆盖。 |
| RLT_29 L-06：历史 schema 演进不回写，精确例外才可读取 | 本卡不改写旧 coder signal：`skill/SKILL.md` 要求旧身份/信号只读并登记映射；`task_plan.md` 同样禁止改写原信号或借旧确认放行新实例。迁移归档由 `migration-inventory.json` hash 与 `test_inventory_exactly_matches_preconstruction_plan` 约束。 | P2 防回归；本轮 P0–P3：0 | 已覆盖。 |
| RLT_31：watcher 应由 workspace ID 动态发现，环境/receipt 前置 fail closed，监控不得依赖无人接收的后台等待 | 新 `tools/space_watch.py` 与两 adapter 保留 workspace-id 动态发现、120 秒节拍、HERDR_ENV/RELAY_RECEIPT 拒绝和 PID 巡检；当前 39-test 实跑中，相关 `SpaceWatchTests` 与 `HerdrDeliveryTests` 全绿。 | P1/P2 防回归；本轮 P0–P3：0 | 已覆盖。 |
| RLT_33 L1：外部测试入口可能耦合已退役产品 | `findings.md` F6 记录原失败与必要联动；源 `tools/tests/relay-light-log.ps1` 现以显式退役反例验证产品目录、重复现役计划及迁出链接；`evidence/source-pwsh-final.log` 为 `RELAY ALL PASS (SKIPPED: 1)`，其中退役 suite PASS。 | P2；本轮 P0–P3：0 | 候选已被执行证据覆盖，仍可保留为卡内线索。 |
| RLT_33 L2：活动树删除会使长基线失效，失效日志不应用于归因或变异 RED | `progress.md` 与 `findings.md` F5 明确把 `invalidated-baseline.log` 标为退休文件并发读取造成的无效记录，不用于归因/放行；该日志本身显示旧路径缺失后的失败。有效替代是冻结副本的 44-test 记录和当前隔离 clone 39-test 记录，后二者均 GREEN。 | P2；本轮 P0–P3：0 | 已正确分流；无效 baseline 不是 RED。 |

## 限制

archive 中没有独立的 `docs/modules/relay-light/knowledge/` 目录；可用历史教训位于各 RLT workspace 的 `lesson_candidates.md` 与独立复核报告，已按本卡相关主题查阅。未进行真实 Herdr 演练、GitHub CI/合入态、verify 或人验，因此本报告不把本地/隔离测试提升为这些结论。

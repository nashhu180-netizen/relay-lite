# RLT_33 独立方案审核（独立只读）

审核范围：仅审核 `design/01-产品设计与验收.md`、`dev_plan/P1-独立交付.md`、本 workspace 的 brief/task_plan/findings，以及源仓冻结事实；未参与起草，未执行产品迁移或测试。

## 方案问题

### P1 — 卡级总表与历史的迁移闭集未定义，不能证明原始授权字段不变

设计要求“已有模块设计/计划/工作区与所有接力计划先保存逐文件 SHA256 迁移清单和只读历史”，并称“**两份**卡级总表移入新仓 `docs/relay/`，行状态/自动接续授权/人验原话不改”（设计 `目标与边界`）；但 task_plan 只有“保存历史后撤源现役入口”“历史 archive 原字节，当前两份表机械迁移”，没有列出两份表的源绝对仓相对路径、其余接力计划的逐项归档/留源决定、目标路径、每个文件的 SHA256、字节比较命令或验收记录位置。

独立核查源冻结 `2246b16cb82f86a594f7b2c36365e7851fe11263`：`docs/relay/` 至少已有 6 个 `relay_plan.md`，其中 `agent-playground/agent-workbench/aw-mvp/relay_plan.md` 与 `wf-analytics-platform/workflow-platform/wfp-p1-obd-p5/relay_plan.md` 明确是卡级衔接总表，并含“自动接续授权”、维护会话、原卡人验/授权文字；源仓还保存 `docs/modules/relay-light/relay/rlt12-win-01`、`rlt27-linux-codex-01`（含 retry02）等完整模式 `relay_plan.md`/`relay_log.jsonl`。现有表述无法审计哪些恰是“二份”、哪些为其他当前接力计划、哪些完整模式文件进入只读 archive，以及旧源/新副本怎样避免双写。

整改门槛：施工前在 task_plan 或受控迁移清单冻结逐文件 source→destination/留源/只读 archive 分类、SHA256、字节级 readback 命令和“自动接续/人验/状态字段不变”的字段级断言；对每个未迁移的 `docs/relay/**/relay_plan.md` 明示留源理由。实现后需用该清单复验，而不能只用目录扫描。

### P1 — “删除完整模式”缺少源仓退役范围与独立包负向验收的可执行边界

用户原话要求“删除 relay-lite 完整模式，仅留单卡分工和接力计划”。设计扩大为“移除完整模式五阶段、stage-lead、账本与专属配置”，并要求旧完整计划/日志保留为历史；这个解释合理，但 task_plan 没有冻结产品文件清单及每项去向。源冻结包含 `tools/relay-light/relay_log.py`、`skill/roles.toml`、完整模式段落和适配器中的 W/C/R/X/F、stage-lead、账本命令；源仓 `AGENTS.md` 也同时承载完整模式入口和 single-task 段。仅写“删完整模式模板/账本配置”“按白名单更新旧仓入口/CI”不足以防止独立仓残留可执行入口，或反过来误删需只读留档的历史。

整改门槛：把源产品文件逐项列为 remove / 改写为 single-task / 原样 archive，并为新仓临时 HOME 安装列出负向断言（无 `relay_log.py` 可执行入口、无完整模式标头/五阶段/stage-lead 路由、archive 不被安装或发现为现役）；同时保留针对 source 历史文件的 hash/readback。不得将 archive 内的历史文本误判为现役残留。

### P2 — executor 更名的兼容矩阵与安装验收未具体化

用户原话为“coder 改为执行者要简洁英文”。设计选择 `executor`，并规定旧 `coder` signal 不改写、旧标头只作存量单卡别名，这符合不篡改历史的方向；但 task_plan 未列出现役受影响的标头、phase/role 枚举、signal 文件名、adapter、测试 fixture、安装 manifest 和恢复映射，也未规定何处记录旧/新身份映射。

独立核查冻结源中现役 single-task 正文仍使用 `builder/coder/reviewer/decider`，而完整模式配置还含 `coder` 与 `stage-lead`。若不先分清“应改的现役单卡语义”与“不可改的历史/完整模式文本”，会造成用户期望的简洁英文未完全落地，或破坏历史信号。

整改门槛：将 role/phase/signal/install 输入分为现役替换、兼容读取、历史只读三列；增加孤立安装后新 executor 派单/恢复旧 coder signal 的正反例，且断言新派单不接受或产生完整模式路径。

### P3 — 源 SHA 的事实正确，但“来源最新”措辞应绑定远端 ref 与读回证据

独立核查显示 `2246b16cb82f86a594f7b2c36365e7851fe11263` 存在，提交主题为 `chore(relay-light): update default Codex role allocations (#155)`，当前是源仓 `origin/master`；RLT_33 源任务分支的文档提交 `b86c672` 以它为祖先。因此设计/brief 的冻结 SHA 可用。建议迁移清单记录读取时间、`origin/master` ref 和 `git rev-parse` 输出，避免把“当前主 checkout 同时前进”误写成来源已变。

## 用户理解风险

- 用户的“删除 relay-lite 完整模式，仅留单卡分工和接力计划”应按设计解释为：删除**现役可执行分发/安装入口**，但完整模式计划、账本和在途/历史证据作为只读历史保存；不能理解为删除历史，亦不能把 archive 当作可恢复执行的产品入口。这个边界须在迁移清单和安装测试中可证。
- 用户的“独立文件夹与仓库不耦合 dh-relay”要求不仅是孤立 clone 能运行，也要求安装、运行时定位、文档链接、总表模板及 CI 不引用 `/home/nash/work/dh-relay` 或源仓相对路径。设计已有方向，当前 task_plan 尚未逐项列出扫描范围与失败判据。
- 用户要求建 issue 后开工；方案记录 relay-lite #1、dh-relay #156，当前 scaffold 已在两个任务分支/Draft PR 上。该状态只证明迁移可开工，不替代上述内容闭集，也不授权把在途旧完整模式计划转换、启动或关闭。

## 需要用户决定的问题

无新增方向性问题。P1 项可由实施方基于冻结源树先形成完整库存，再按已写入设计的“只读历史 + 两份卡级总表机械迁移 + 不改授权字段”原则执行；若库存发现无法唯一识别设计所称“两份”表，才需将候选路径、字段差异和影响汇总后一次性请用户裁决。

**Verdict：REVISE（存在 2 个 P1；补齐上述可审计迁移闭集后再进入产品迁移）。**

---

## 定向复查（原 P1/P2，2026-10-07）

原 P1 已闭合。`migration-plan.json` 固定 source SHA `2246b16cb82f86a594f7b2c36365e7851fe11263`、`origin/master`、948 个唯一文件的 `source`、`sha256`、`archive`、`new_active`、`action`、`source_action`。独立复算覆盖源 `docs/modules/relay-light`、`docs/relay`、`tools/relay-light` 三棵 tracked 树 948/948，且逐个以 Git 对象内容复算 SHA256 为 948/948 一致。两个 `archive_and_migrate_table` 条目精确为：

- `docs/relay/agent-playground/agent-workbench/aw-mvp/relay_plan.md`
- `docs/relay/wf-analytics-platform/workflow-platform/wfp-p1-obd-p5/relay_plan.md`

两者均同时保留只读 archive，并以 `remove_and_redirect` 从源现役位置退役。更新后的 task_plan 明确新表只可新增迁移说明，移除该 header 后全文须与 archive 逐字相等，覆盖自动接续授权、状态、模型确认、维护人和人验原话；其余 `docs/relay` 计划以及模块内完整计划/账本均归档、不转换、不启动。先前点名的 `rlt12-win-01`、`rlt27-linux-codex-01`（含 retry02）完整模式目录也在清单中逐项 `archive_readonly`。

原第二个 P1 已闭合。task_plan 已将源 `tools/relay-light` 11 个产品文件逐项标为 `retire_product_at_source_sha/remove_product`，并冻结新仓仅保留的工具、测试、skill、adapter 与总表模板闭集；验收同时要求 archive 不安装、现役包无 `relay_log.py` / `dh-mapping.toml`、无 stage-lead/五阶段/账本命令/旧完整标头，且在临时 HOME、孤立 clone、源目录不存在时仍成功。这足以区分历史文本与现役入口。

原 P2 已闭合。新增兼容矩阵把新派单、角色配置、默认模型和 signal role 收敛为 `executor`；九值 phase 保持不变；旧 coder signal 和已确认实例模型只读；恢复映射写入 `execution_strategy.md`；新标头为 `[relay-lite:single-task]`，旧单卡标头仅作存量别名，完整模式标头不接受。该约束既承接用户“coder 改为执行者要简洁英文”，也不改写历史证据。

**定向 verdict：PASS（原 P1/P2 整改充分；本结论仅放行尚未开始的产品迁入进入施工，不代替后续实现、测试、独立代码复核、CI、PR 合入、verify 或人验）。**

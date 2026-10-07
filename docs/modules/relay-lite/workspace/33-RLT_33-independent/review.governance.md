# RLT_33 · 治理补正独立复核

审阅者：独立新实例 `governance_miner`，但以 `fork_turns=all` 继承父会话上下文；未参与本卡产品施工、五路既有复核或总表维护，**不满足 fresh-context 审阅/miner 身份**。审阅范围仅为当前未提交的治理补正：仓根 `AGENTS.md`、设计/DevPlan/brief/task-plan/review/progress/execution strategy 的格式与事实登记、设计证据页，以及首次 `dh` 失败日志。未修改产品、接力计划、业务卡、PR 或维护者回执。

## 核对结果

- `AGENTS.md` 仅补“宪章 / 硬规则”“入口闸”“任务类型阅读矩阵（索引）”标题和既有语义的显式文字；未改变开工、复核、验收、权限或清理规则。
- design README 的正式输入链接补 `./`；brief 补“覆盖任务”和“边界”；review 补 AI 提交、独立复核、人类签名三区；task-plan 将花括号伪占位改成逐项路径；这些补正与 `evidence/dh-check-before.log` 的八项失败逐一对应。
- DevPlan 的 RL33-M1～M6 与设计和 brief 人工逐条比对一致；允许路径覆盖本卡现有新仓工件，未新增业务卡或 #154 实施授权。A-full 与 B-adjust 各有一条 planning-event，分别指向设计和 DevPlan；设计证据页明确是既有审核/理解证据的机器登记补正，并明确不把施工后的登记伪称为施工前新审核。
- 最新总表补充只记录用户的迁移时机决定、AW `5a47a4f` 与 WFP 未合入 `65f87a0` 的来源、两维护者暂停 ACK 和“新仓实际合入后仍须原维护者更新入口”的停止线；没有把 ACK 写成人验、合入、维护权转移或业务卡状态变化。

## R14 适用性复判与 `dh relay-lite` 复核

本轮实跑结果：**0 failures，2 warnings**（退出码 0），完整输出见 `/tmp/rlt33-governance-review-dh.log`；工作树 `git diff --check` 无输出。

R14 的 reader 位于 `/home/nash/.agents/skills/dev-harness/tools/dh-check.mjs` 738–758 行。它只识别以 `> DH_<数字> 计划|验收` 开头的卡片（742 行），且只从该卡片行收集含“验收口径”的内容（752–756 行）。`RLT_33` 与本卡的 `#### RLT_33` 标题均不在这个硬编码支持域；因此 warning 是 reader 的任务 ID/标题格式限制，不能据此推断本卡没有验收口径。不得把 RLT_33 改成 DH 编号、添加虚假的 DH 别名，或越出本卡范围修改外部 skill 工具。

我逐行去除 Markdown 列表缩进后比较设计 16–21 行、DevPlan 16–21 行和 brief 15–20 行：三份六项 RL33-M1～M6 的归一 SHA-256 均为 `4bba095b9ca0949b3555b8d2a8617075ba1ab67ed07c7d483f3ec51d8b63eaf0`。这是继承上下文的新实例所作的人工合同一致性核对，不将工具 warning 写成不存在，也不计作 fresh 独立证据。R19 只是新文件命名建议；为保持既有链接和审核证据路径，本轮不重命名。

源仓补正亦已只读核对：提交 `de6bf37` 仅为其 RLT_33 brief 增加覆盖任务、完成条件、边界三段，承接主合同 RL33-M1～M6 与源侧已登记边界；未改产品、其他任务或业务授权。源 `dh` 的 baseline/current 均为 101 failures；`source-dh-delta.json` 记录的变化是旧 RLT_27 的全仓差异归因从“无基线”变为 R30，仍属他卡历史现场，保留且不修复，不可称源仓 dh 全绿。

| 级别 | finding |
|---|---|
| P0 | 无 |
| P1 | 无 |
| P2 | 无。R14 是外部 reader 对 DH 标题/编号的支持域限制，且六项主合同已由本实例归一比对相等；不是产品、权限或验收缺口。 |
| P3 | 无。R19 是文件名建议，稳定链接与历史审核路径保留的决定有明确依据。 |

## Verdict

**PASS_WITH_NONBLOCKING_WARNINGS（限本继承上下文实例的事实核对）。** 当前补正忠实登记了已有授权、审核、回执和停止线，未发现产品、权限或验收漂移。R14/R19 仍如实保留为工具 warning，不能称 `dh` 全绿；本报告不计入 fresh-context 路径，也不放行合入、verify、维护权切换或人验。

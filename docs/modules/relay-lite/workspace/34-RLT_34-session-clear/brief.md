<!-- dh:v1 -->
<!-- dh:workspace-contract:v2 -->
# brief — RLT_34 新批次与新任务清理会话

## 覆盖任务
RLT_34；来源：../../dev_plan/P2-会话清理维护.md#rlt_34；Issue #7。

## 目标 (Outcome)
标签页复用时先清除旧任务上下文，核实成功后才投递新任务。

## 本卡开工授权
用户本轮原话“确认开工”（日期 2026-10-07，分钟未知）；承接前轮已展示的规则、标准档和三份产品文档范围。
目标仓库 nashhu180-netizen/relay-lite / origin；wt/RLT_34 → master。包含本卡完整 Git 交付、必要回归测试和治理证据；不授权用户现有标签页操作、安装/部署/重启或下一卡。

## 分类事实
仅修改文档协议与协议测试；无生产实操作、业务迁移、指标口径或安全/共享保证破坏。新独立任务清理前置规则为行为语义变化，因此 normal；不改认证、凭据与 RELAY_RECEIPT 边界。

## 边界 (Boundaries)
In scope：三份产品文档、必要协议测试、本卡计划/七件套/证据。Out of scope：自动化清理工具、安装副本、真实 Herdr 操作、历史 archive、其它 worktree、其它卡授权。

## 完成条件

| # | 条件 | 谁验（AI / 人） | 出处 |
|---|---|---|---|
| RL34-M1 | 新批次派单前，前批 durable PASS 且工件齐全，executor 与 batch-reviewer 各 clear 一次并分别确认成功。 | AI | P2 / RLT_34 / RL34-M1 |
| RL34-M2 | 标签页接新的独立任务前保存前任务工件与 signal，清理旧会话并确认成功，再读取新派单；新建空会话不冒充复用会话的 clear。 | AI | P2 / RLT_34 / RL34-M2 |
| RL34-M3 | 同任务 FAIL/整改与 E2 定向复查保留原会话及计数；fresh reviewer 必须是未参与实施的独立新实例；常驻 watcher 不逐批 clear。 | AI | P2 / RLT_34 / RL34-M3 |
| RL34-M4 | 清理失败或结果未知时停止新派单，不盲重发；core 与两 adapter 一致；历史 signal、证据、计数及 RELAY_* 保留。 | AI | P2 / RLT_34 / RL34-M4 |
| RL34-M5 | 协议回归及变异 RED→还原 GREEN、fresh 独立复核、Ubuntu/Windows CI、PR 合入态复验和 verify(relay-lite) 齐备。 | AI | P2 / RLT_34 / RL34-M5 |

## 三档分类引用
源卡 v2 五项事实，normal=[code_review]；本工作区不另建分类。

## 触及子系统
产品协议文档；最新行为直接记 skill/SKILL.md 与两 adapter，无新程序子系统。人验栏为空：交付对象是书面派单协议与回归证据，不声称真实标签页已被清理。

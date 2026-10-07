# AGENTS.md — relay-lite

所有 agent 的唯一入口。relay-lite 是独立的单卡接力协议与跨卡接力计划仓库，给任意业务仓使用。

## 宪章 / 硬规则

- 默认主干 master；先建本仓 GitHub Issue，任务分支 + 一卡一 worktree，变更通过 PR、必要 CI 和独立复核后服务端合入；本卡开工授权覆盖其全程交付，生产操作/下一卡不随包授权。
- 【入口闸】非平凡任务动代码前先落户，按 dev-harness 分流；用户明确确认标准档后开工。任务类型按启动合同冻结，施工者不自审；heavy 五路：代码轮1、fresh代码轮2、需求、一致性、教训。完整证据和 verify(relay-lite) 提交齐备后才称完成。
- 模块根 docs/modules/relay-lite/；设计 design/README.md 指定正式输入，任务与状态 dev_plan/，现场 workspace/，verify scope=relay-lite。
- 产品入口 skill/SKILL.md；两 adapter 在 skill/references/；代码 tools/；测试 tests/；接力计划 docs/relay/，模板 skill/templates/card-chain.md。archive/ 只读历史，不是流程入口，不执行旧模式。
- worker 先读精确派单与业务仓 AGENTS、指定 workspace；只完成当前派单，不派活、不自审、不问用户。DONE/BLOCKED signal 后立即停止，不等 node_closed。watcher 对 repo/workspace 零写入，只运行观察脚本与报信。
- 派单标头 [relay-lite:single-task]；角色 executor 表示执行获授权任务，涵盖代码、文档、配置与验证。worker 为所有被派活角色统称。
- RELAY_RECEIPT 存在（含空值）即 fail closed：产出型角色只写精确 BLOCKED signal，watcher 非 durable 通知后停，不清除 RELAY_*。
- 编排只派发/通信/核状态/路由，不代跑测试、不代判内容；模型分配、写者、复核与自动接续授权以 skill/SKILL.md 和原卡为准。文档角色默认不启用。
- 凭据值永不入工件；枚举/截图证据先白名单过滤。用户授权不代替人验，不改历史失败。范围外发现只记 findings；部署、重启、环境写入另行授权。
- 独立复核可派 fresh-context subagent，只读产品与其它工件，仅写该路径 review。当前会话只维护其被授权任务，不清理其它 worktree。

## 任务类型阅读矩阵（索引）

规划/开工/收口使用 dev-harness 对应 A/B/D/E/R references；协议维护读 skill/SKILL.md、两 adapter、对应任务工件；恢复读 dev_plan、workspace 和实际 Git。跨卡接续读接力计划与原卡，摘要不能替代证据。历史出处见 docs/migration.md。

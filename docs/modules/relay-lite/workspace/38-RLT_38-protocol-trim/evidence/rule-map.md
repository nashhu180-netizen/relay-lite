# RLT_38 规则保真与读取矩阵

旧源统一为0b08c18，比较用git show BASE:skill/路径。正文按引用图安装可达，语义等价仍由独立fresh复核判断；下表是定位，不自证PASS。

| 规则 | 旧核心/adapter节 | 新落点 | 必读者/触发与核法 |
|---|---|---|---|
| 授权与停止 | 硬规则、编排职责、两adapter边界 | 核心硬规则 + references/orchestration.md | 全员核心；编排首次/恢复、decider必读；对照权限闭集及未知场景 |
| 角色与拓扑 | 角色与术语、adapter拓扑 | 核心角色；当前space例外与一worktree从adapter合入 | 全员；静态核角色/当前space实ID/写权 |
| 环境选择 | 环境配置与派发入口、adapter启动 | 核心同节、adapter必要入口、environment-herdr | 环境动作前；原环境测试和三入口断言 |
| 模型 | 核心gate、两adapter gate | 核心gate；询问不另启agent从adapter合入 | 启动/更换/恢复；核明确确认及自动接续例外 |
| 写者 | 核心durable signal、adapter决定落点 | 核心同节；策略仅事实变化时维护合入 | 全员；核唯一写者/并写/候选冻结/决定原始来源 |
| signal与RECEIPT | 核心标头/signal、两派单模板 | 核心 + 唯一templates/dispatch.md | 全员/编排派单；保留九phase、batch、空receipt分流、写完即停，原测试 |
| 生命周期与额度 | 核心生命周期、基线失败 | 核心计数 + verification.md | 全员/取证审核；核batch同人/final换fresh/E2同人targeted区别 |
| 原生clear | 核心清理闸、adapter启动 | 核心同节保留原文、adapter引用 | 全员；原全部clear断言保留，未知/失败/额度/新任务授权保持 |
| 恢复 | 核心恢复、两adapter恢复 | 核心恢复唯一正文 | 全员恢复；核四类权威，findings不是第五类，摘要不可代原件 |
| 跨卡更新/交棒 | 核心总表 + adapter总表 | references/card-chain.md | 首次/恢复先查关联；有关联或待定位的协调会话必读；核唯一写者与接收方确认 |
| 自动接续/并行 | 核心总表长段 | card-chain自动接续1–4及并行 | 维护会话；核用户栏/来源/模型、扇入证据、五步、半成品、冲突串行、唯一询问者 |
| 失败归因 | 核心范围外既有失败 | references/verification.md | 编排派测试/取证前、executor/reviewer必读；核原phase/path/额度及归因非放行 |
| 文档可选 | 核心文档agent、adapter文档 | references/document-role.md | 明确启用时编排/document/责任方必读；核READY_FOR_DOCUMENT→SYNCED→同reviewer确认，原FAIL不可翻PASS |
| 监控及等待 | 核心watcher、adapter共用段 | references/watcher.md + environment-herdr | 编排启动/等待/处理通知、watcher必读；原watcher全部scope断言及运行单测 |
| 宿主差异 | adapter watcher/等待工具 | 两adapter对应段保留 | 对应宿主；原session_id/cell ID/Promise与task_id断言 |
| 派单上下文 | 两份adapter模板 | templates/dispatch.md | 编排派单必须使用；消费者测试核唯一模板与全部上下文字段 |

## 重组方式

- card-chain/document-role：原长段拆为顺序小节并缩句，约束与例外按上表逐项核，不删除功能。
- orchestration/verification/watcher：原节迁移为主，修相对链接和跨文件指代；独有adapter限定合入核心或对应合同。
- adapter：重复协议段删除，共用模板迁移一份；保留宿主真实句柄调用与必要gate提醒。
- 核心：增加按角色读取表及原节路由；环境说明压缩，公共硬闸保留。拆文件的字符仍计入总数。
- 模型配置roles.toml、环境注册environments.toml、原card-chain模板不改；历史工件/归档不改。

## 安装闭环

新增六文件：references/card-chain.md、orchestration.md、verification.md、document-role.md、watcher.md、templates/dispatch.md。均源自skill/同路径，进入安装器显式SKILL_FILES闭集。六个临时安装入口（.agents/.codex/.claude × relay-lite/relay-light）沿核心路由读取；adapter直链核心/派单/watcher/决策；环境协议直链watcher。

test_installed_reading_routes_are_closed_and_template_is_unique从安装SKILL.md递归访问真实相对链接、拒逃逸/缺件，核新增六件字节与模板唯一性。test_missing_routed_contract_rejects_before_install逐件缺包时验证全部安装前拒绝。生产清单漏掉card-chain的变异必须使安装消费者因缺文件真实断言失败，再原字节恢复。

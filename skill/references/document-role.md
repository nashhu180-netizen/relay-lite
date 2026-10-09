# 文档 agent（single-task 可选分工）

公共闸见[核心协议](../SKILL.md)。默认不启用：原责任方写文档，不建独立agent/tab、不登记document、不走确认链或等SYNCED；缺配置/信号不阻塞。

用户明确指定本卡试验后才执行本合同，不强制迁移在途卡。在既有任务/执行策略登记实例、模型档、获授权文件和内容责任方；默认建议低成本档，实际遵循model-allocation gate，已有确认直接登记。

## 范围与责任

授权路径内的建卡、设计/计划、进度、问题、复核/决策报告、使用说明、as-built、收口和总表均可委托。用户可保留产品文档给executor，document仅记过程；单一类别的试验不证明其它类别有效。共享设计/计划/总表由登记维护方委托，禁止多卡并写。

executor提供方案、实际结果和测试输出；reviewer/decider提供结构化定位、级别、结论、证据和版本。document直接读指定diff、原始结果和目标文档，不要求他人先写正式报告。原始日志、工具产物和durable signal仍由生产者生成，document不得修改来源、施工/测试、部署、代验收、派活或自行commit/push/merge。

工作区尚不存在时，主会话先给Issue/任务来源、已确认模型、精确创建路径、分工和验收输入，派document在plan创建任务文档及execution_strategy；主会话核登记后才启动依赖角色。开工/模型闸不豁免，不另建账本。

## 派单与确认

document是角色，不改roles.toml、九值phase或batch枚举。沿文档所属phase：建卡plan、施工batch、审核plan-review/batch-review/workflow-final/e2-code-review、决策decision、收口human-acceptance；不使用watcher。

每次派单给请求标识、原阶段/path、候选版本或文件摘要、结论/证据、精确可写文件及责任确认方。`path=document-<请求标识>`；成功`verdict=SYNCED`只证明同步，缺证/冲突/过期写BLOCKED及reason。独立信号文件如`DONE.<phase>.document-<请求标识>.md`，重试换请求标识，不覆盖历史。SYNCED/READY不替代执行、复核或人验PASS。

复核代笔顺序：reviewer独立检查并自写原始结构化结果和`READY_FOR_DOCUMENT`阶段signal → 编排派document → document写报告与SYNCED → **同一reviewer**核结论、级别、遗漏、证据、版本，另写原路径确认signal，保留原signal。只有reviewer确认可放行，原FAIL/REVISE不得转PASS。代笔纠错回document，不重跑施工、不重置计数；实质发现走原整改/轮次。文字确认不增加复核轮、不替代后续fresh独立审核。

机械进度按原始结果填；方案/决定/模型/验收状态经原责任方确认才供消费。确认指向具体章节/结论及版本，无关追加不失效，改已确认内容须重核。编排只核身份、路径、版本和确认引用，不代判内容。人验只引用户真实判断，human-acceptance不授予代签；决定/知会入findings，execution_strategy只放指针，progress不记决定。

## 顺序、恢复与效果

委托文件由document顺序写，原责任方不并写；未委托文件保持原写者。可复用文档会话，每次signal后即停，下次再派，不常驻轮询。验证/复核冻结相关候选。并发改动、来源漂移、缺证/中断时保留待同步事实，不猜或覆盖。恢复核原始来源、请求和当前文件，避免重复追加；必要记录未同步不称交棒、不清现场。失联保留待同步，换实例仍须确认，不静默恢复多写者。

执行侧评估准确性/遗漏、及时性/可接续性、纠错负担、可得耗时用量，document仅转录。未知费用如实记，无可比基线不称省钱，不另造台账。合同可演练/审计，工具不提供沙盒或自动阻断保证。

仅覆盖明确委托文件的默认sole writer、取证人工落笔和总表代笔；决定权、取证责任、RELAY_RECEIPT、独立复核、授权、watcher零写入不变。恢复仍核四类权威：原角色signals、责任方确认的报告及原始来源、编排核对的执行策略、选中环境实态；不能只凭摘要。

# adapter-claude-code — relay-lite 单卡接力

默认安装目录：`~/.claude/skills/relay-lite/`。协议核心见 `../SKILL.md`；单卡只分派获授权角色，不执行旧模式。

## 启动与投递

先执行核心 `SKILL.md`「环境配置与派发入口」：运行已安装的 `<SKILL_DIR>/environment_config.py`；非零退出或非 READY 即停止。新卡可传明确 `--environment`，恢复必须带 `--expected <execution_strategy 已登记环境>`。读取返回 `protocol`，按选中环境的派发、通知、观察与身份核对方式操作；目前只有 [Herdr 环境协议](environment-herdr.md)，派发前须加载当前 `herdr --skill`。

新批次/新独立任务先执行核心「新批次与新任务的标签页会话清理闸」，核实际 pane/kind，使用当前模型帮助或实际 UI 已核实的原生清理命令。支持 `/clear` 才使用；其它 kind 核其等效命令，不猜模型能力。以实际 pane 的原生清理成功提示或新空会话状态确认，`state_change_seq` 推进/idle/done/屏幕变空不作成功判据。确认清理成功后再投递派单文件指针；清理命令与派单不可合并。失败或未知不派新单、不盲重发；记录对象/任务或批次/命令/成功依据，保留历史工件/计数及 RELAY_*。不是 shell `clear`。

模型和推理档按已确认 execution_strategy，原生启动参数仅透传给交互式 CLI，不使用 headless 替代。只读角色写权由精确派单限制，工具权限不扩大授权。等待须有接收者，watcher 通知用于唤醒，放行读 durable signal。

## single-task 单卡接力（本侧适配）

协议语义以 `SKILL.md` 为准；这里只描述本侧启动、派单、观察和恢复写法。

### 总表关联与交棒

完整语义执行核心「卡级总表维护与交棒核对」：首次/恢复登记总表与唯一维护人，状态/等待/结果/交棒按原证据顺序汇总；非维护卡发 `card-chain update`，维护人移交发 `maintainer-handoff`，并行决定转发 `card-chain decision`，全部通过选中环境的通知入口并确认实际送达。维护移交必须接收方登记后回复确认；不可达按核心交回用户/总表待同步出口处理。

自动接续/并行开卡只在核心该行用户授权、前置证据与模型分配满足时，由维护会话按核心五步准备；新卡先校验其环境配置，再按对应环境协议新建 space/tab/交互式 orchestrator，不从本卡环境猜下一卡。任一步失败保留半成品、按原停止线报告，不重试、不扩大下一卡权限。总表不是运行真相，worker/watcher不读写总表；可选 document 仅按核心授权代笔。

### 编排边界与验证派单

执行 `SKILL.md` single-task 的「编排职责与执行边界」「范围外既有失败」合同。需要测试、基线对照或验收证据复算时，派给已获授权的 executor/当前路径 reviewer（批次内为 batch-reviewer，workflow-final/E2 保留原 phase/path 及各自换人/计数规则）；orchestrator 不使用自己的 shell、后台任务或工具代跑。可做的只读核对限于身份、路径、状态、字段及已有结论的程序性核对，缺证则路由补证，不自行重建业务结论。

非方向小决策按 SKILL「小决策交 decider，问用户攒齐一次」派 decider（`phase=decision`），白名单与仍问用户闭集以 SKILL 为准；decider 结论由 orchestrator 登记 findings（注明 decision 文件）并知会用户。命中问用户闭集的事项先登记 D 项，攒齐后用一次 `AskUserQuestion`（多题合并在同一次调用里；单次上限 4 题，超出时同一停点连续发、不夹带其它工作，仍算一次询问）问用户，不逐项打断；拿不准归哪边按问用户处理。并行开卡期间本卡不自行发问，只登记 D 项并通知维护会话，由维护会话统一问并以 `[relay-lite] card-chain decision <卡号> <用户原始消息指针>` 转回（SKILL「并行开卡」③）；本卡 orchestrator 收到后在本卡 findings 登记来源（经维护会话转达的用户答复及时间）。维护会话在自己的自然停点统一询问时用 同一停点的一次 AskUserQuestion按卡分组。

用户对进行中动作提出原则性纠正时，不自动解释为立即 kill 或删除现场；停止发起新的同类动作，语义不清由主会话澄清并保留现场。明确停止指令或既有停止条件立即执行；终止进程与删除现场分别判断。

### 启动前 model-allocation gate

- 默认模型与推理档提案统一取核心 `SKILL.md`「model-allocation gate」表及 `roles.toml` 对应角色：watcher=`gpt-6-luna`/`medium`，executor 与 batch-reviewer=`gpt-6.1-sol`/`high`，decider=`gpt-6-astra`/`medium`，reviewer=`gpt-6.1-sol`/`high`（batch-reviewer 默认参考 `roles.toml` 的 `[executor]`，独立只读角色）；派单记录模型与推理档两个字段，`gpt-6.1-sol-high` 不作为模型 ID。默认不覆盖在途已确认分配，启动仍遵守下方确认闸。

- 拉起任何 agent 之前，orchestrator 先向用户展示全部拟启动角色/实例的模型与推理档提案表并明确询问确认；推荐默认仅是提案、不写死模型，用户可逐角色修改。**未获明确确认不得启动任何 agent**——缺询问、先启动后补确认、按未确认的默认选择直接拉起、角色/实例/模型/推理档变更免确认，均属违规。
- 确认后由 orchestrator 机械地把确认来源、角色/实例、模型、推理档写入任务工作区 `execution_strategy.md`；未启动的 tab/pane 标 pending，启动后补齐实际 environment/space/tab/pane 与观察来源并逐项比对。`execution_strategy.md` 仅 orchestrator 在授权/停止线、角色/模型/实例、总表关联/维护人、派单路由、批次/clear 闸或提交/checkpoint SHA 变化时维护，其余角色与 watcher 默认只读；启用 document 时按核心首次建卡/代笔与核对合同执行，模型决定不转移；`roles.toml` 只是默认分配提案，不为本模式写死模型；本模式可参考其中默认模型提案与启动写法，运行时采用用户确认后的 `execution_strategy.md` 分配，不把模板直接当作本卡授权。
- 恢复时可沿用已有明确确认且分配未变的快照；新增/更换角色或实例、换模型或推理档必须再次询问确认。超时、静默或最大工具权限均不推定确认；最大工具权限不扩张 commit/push/PR/merge/deploy/verify/人验授权。询问由当前主会话执行，不为询问另启 agent。

### 拓扑与拉起

一张卡一个所选环境的 space，每角色实例独立具名 tab；按环境协议依次创建、解析真实 ID、启动交互式 agent。用户明确使用当前 space 时，先核真实 space ID，再为各实例建 tab，不另开 space；同一 Git 任务仍只用一个 worktree，不共享写权。模型档以用户已确认 execution_strategy 为准。

### 决定落点与写者

执行核心 SKILL「durable signal 与写者边界」：用户裁决（点选/确认时间与原始来源，未知时间标未知）、decider 摘要与独立 decision 引用、D 项状态、范围外发现/P3 去处和给用户的知会统一落 `findings.md`。遗留须用户明确点头并标去处；知会或沉默不是同意。orchestrator 仅记录已有裁决与引用，executor 按派单记发现/证据；基线归因及关闭仍仅 executor 按审核流程回写，编排不代判。编排安排同文件错开写，每次指定章节与唯一写者；复核期间冻结相关候选内容，启用 document 才按原责任方确认代笔。

`execution_strategy.md` 只记上述编排事实，业务决定只放 findings 对应条目的指针；授权/模型确认事实仍在执行策略。`progress.md` 仅当前 batch executor 追加施工里程碑与证据引用，不放决定；`lesson_candidates.md` 仍仅 executor 按派单追加。主会话人验结果仍引用真实用户来源记录到 findings，不能用开工授权或摘要代签。只使用本节默认写者，不引入其它模式的写权。

### 文档 agent 派单

默认由原责任方直接写文档，不要求创建独立文档 agent、终端或标签页，不登记 document 实例，也不等待其 SYNCED 信号；缺少 document 配置或信号不构成阻塞。仅在用户明确指定本卡试验时启用，并执行核心 SKILL「文档 agent（single-task 可选分工）」全部合同；以下代笔规则仅在启用时覆盖本侧默认写者描述。document 模型/实例须已确认；可委托全部获授权人工文档，也可按用户指定保留产品文档给执行者、只委托过程记录。首次建卡由主会话先给已确认分工、任务来源与创建路径，再由 document 登记执行策略，不要求先存在该文件。

沿用下方九值 phase：document 是角色，path=document-<请求标识>，成功 verdict=SYNCED，独立请求文件名；不新增 phase/账本或修改 roles.toml。派单附来源版本、原阶段/路径、结论与证据、精确写路径及责任确认方。reviewer 先自写 READY_FOR_DOCUMENT 和原始结构化结果；文档代笔完成后，同一 reviewer 核对映射再另发确认 signal，原 FAIL/REVISE 不得翻成 PASS。document 的 DONE/SYNCED 不用于原路径放行，代笔纠错不算新复核轮；实质改变仍走原复核规则。任何 phase 下 document 都不执行测试、部署、提交或验收。

同一获授权文档顺序写，验证期间冻结相关文件。来源过期/冲突/缺失时 BLOCKED/待同步，保留原始证据，不重跑已完成施工。效果由执行侧评价，document 只转录；恢复核经责任方确认的报告及原始来源，不信单独摘要。以上为协议约束，不是工具或沙箱硬保证。

### 派单 prompt 模板（orchestrator → worker）

```text
[relay-lite:single-task] worker · phase=<phase> · agent=<角色>#<实例> · batch=<n|na> · round=<n> · workspace=<任务工作区>
读：<repo>/AGENTS.md → <任务工作区>/brief.md、task_plan.md（及派单指定的其它工件）
边界：<本棒 allowed-paths 一句话>
验证责任：<执行者；独立核验者；不涉及验证则写不适用>
对照基线：<整卡/批次用途；完整 SHA；选择依据；不适用须说明>
执行合同：<cwd；解释器；完整命令；必要环境/依赖；收集范围；串行要求>
临时现场：<允许位置/准备方式；所需资源；证据保存与清理责任；无则写无>
证据与写者：<精确路径/章节及本次唯一写者；findings 的决定记录由编排或获派 executor 错开追加，基线归因仍仅 executor 写、review 由 reviewer 写；启用 document 时按确认代笔，原始结论/signal 仍由原角色写>
决定引用：<findings 条目与用户/decision 原始来源；无则写无；缺源/冲突/待决定时不推进依赖动作，回报编排澄清>
通过/阻塞：<必需通过项；允许失败集合及审核/授权引用；缺证或新增失败的 BLOCKED 出口>
硬规则：你是 worker：不拉终端、不派活、不回头问用户；先跑 RELAY_RECEIPT preflight；
卡住写本角色精确 BLOCKED 单行 signal 不憋死；凭据/密钥值永不写进任何工件。
完成：只写派单指向的产出与本角色单行 DONE/BLOCKED signal 即停；无 node_closed，
不创建/读写 relay_plan.md、relay_log.jsonl。
```

- phase 闭集：`plan` / `plan-review` / `batch` / `batch-review` / `workflow-final` / `e2-code-review` / `decision` / `watcher` / `human-acceptance`；`batch=1|2|3|na`。已有 `[relay-light:single-task]` 单卡标头按核心兼容节读取；旧节点执行标头不受支持。
- durable signal 单行 schema：`DONE|BLOCKED task=<t> phase=<p> agent=<r>#<i> batch=<1|2|3|na> path=<path|na> review_round=<n> remediation_count=<0|1|2> verdict=<v> evidence=<repo 相对路径[,...]>`，BLOCKED 另含 `reason=<snake_case>`；值无空白。产出型 builder/executor/reviewer/decider（含已启用的 document）写完 signal 即停；orchestrator 只按 durable signal 与独立 review/decision 工件机械分发/路由，不把终端状态当真相。
- `RELAY_RECEIPT` fail closed 分流：产出型 builder/executor/reviewer/decider（含已启用的 document）命中时只写本角色精确 `BLOCKED.*.md` 单行 signal 后立即停止；watcher 命中保持 repo/workspace 零写入，只用选中环境的通知入口非 durable 通知 orchestrator 后停、不写 BLOCKED。两分支均不得清除任何 `RELAY_*`。

### watcher 节拍与安全 Enter

核心 watcher 通用合同适用于全部 kind：当前 Herdr 的 `space_watch.py` 根据 `workspace_id` 动态观察，`--workspace`、`--notify`、`--self` 从环境协议及真实派单取得；排除 watcher 自身和主编排，不按名字前缀或名单筛选。默认由环境协议在独立普通终端常驻程序，`phase=watcher` agent可选；120 秒节拍由脚本维持，不再自己比对状态；完整监控、启动确认、通知/退出与安全 Enter 步骤读取核心及选中环境协议。

#### watcher 宿主工具调用（Claude Code，旧 agent 子进程兼容入口）

执行核心「watcher 通用启动与监控步骤」及选中环境协议；所有 agent 的监控规则相同，这里只说明宿主工具。固定脚本路径与真实 space/notify/self 从环境协议/派单取得。

用 Bash 的 `run_in_background=true` 运行固定脚本，读取真实后台 task_id/进程标识；立即用该宿主的任务状态/输出工具短等待核原后台任务存活或退出，再通过环境通知入口确认启动。随后对同一 task_id 短等待巡检；后台句柄缺失或无法证明持续运行即报告 blocked。120秒观察节拍在脚本内；宿主每次等待不超过60秒，不靠模型长阻塞维持循环。

stdout/stderr仅保留宿主临时任务输出，不重定向进仓库/工作区；正常静默，退出一次报信确认；通知未知不重发，观察继续；不自动重启。安全 Enter、RECEIPT、watcher不逐批clear与durable signal路由全部沿核心。

### 主编排有界结果等待

按环境协议调用task_wait.py只读等待本批精确DONE/BLOCKED文件，不依赖watcher模型持续working。主编排保持有接收者的等待回合；每次最多60秒。PENDING/退出3是本批结果未出现，继续有界等待或按真实停止线报告，不以watcher暂停终止整卡；READY/退出0只发现结果，仍核原signal、完整报告与适用复核，再按原授权接力，不代判或代跑worker测试。

等待工具用Bash前台有界命令或run_in_background=true所得真实task_id与任务状态工具读回结果；后台任务没有自动恢复回合能力时使用前台有界等待，PENDING回来继续等待，不把后台句柄当结果。

### 恢复依据

恢复权威只有四类：原角色自写的 durable signals、独立 review/decision 工件及其原始来源、由 orchestrator 核对的 `execution_strategy.md`、选中环境实态。`progress.md` 只是施工证据索引、watcher 通知只是即时提示，二者都不是运行真相；本模式不存在 relay 账本。恢复/重启从四类权威重建，不依赖终端存活状态。 `findings.md` 是决定与遗留的检索入口，沿其来源引用回查上述独立工件及用户原始裁决，不新增第五类运行权威；摘要缺源、冲突或仍待用户决定时，不推进依赖该决定的动作，回原责任方澄清。


## 红线

凭据值不入工件；不清除 RELAY_*；watcher 零写入；不代判验收，不运行旧完整计划。

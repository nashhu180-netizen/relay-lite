# adapter-claude-code — relay-lite 单卡接力

默认安装目录：`~/.claude/skills/relay-lite/`。协议核心见 `../SKILL.md`；单卡只分派获授权角色，不执行旧模式。

## 启动与投递

先确认模型/推理档、任务 worktree、Herdr workspace ID 与 worker 身份。新 space 使用 `herdr workspace create`；每角色实例独立具名 tab：`herdr tab create --workspace <ws> --cwd <任务worktree> --label <角色> --no-focus`，读取 root_pane.pane_id 后启动。

- codex kind：`herdr agent start <名> --kind codex --pane <pane_id> -- -m <用户确认模型> -c model_reasoning_effort=<确认推理档> --dangerously-bypass-approvals-and-sandbox`。
- claude kind：PATH shim 不可靠时 `herdr pane run <pane_id> "claude --model <确认模型> --effort <确认档> --dangerously-skip-permissions"`，再 `herdr agent rename <pane_id> <名>`。
- devin/omp 启动参数按本卡已确认配置，不猜模型。只读角色的写权由派单明确限制；最大工具权限不扩大任务授权。
- 提示词仅发 ASCII 文件指针，长中文派单放获授权文件。调用 agent prompt 后核本次 state_change_seq 推进、实际 pane 与已提交状态；确认未送达时按协议报阻塞，未知投递不盲重发。pane idle/done 不是任务完成证据。
- 新批次或新的独立任务派单前，先执行核心 `SKILL.md`「新批次与新任务的标签页会话清理闸」：复用标签页时核实际 pane 与 kind，单独投递该 kind 已核实支持的原生会话清理命令，确认清理成功后再投递派单文件指针。清理命令与派单不可合并；`state_change_seq` 推进仅证明状态变化，清理结果另核原生提示/新空会话。失败或未知不派新单、不盲重发；同任务整改/E2 定向复查、fresh 独立复核及 watcher 沿核心各自边界。不是向 shell 运行 `clear`。
- 等待须有接收者：watcher 提示只用于唤醒，放行仍读独立 durable signal；watcher 缺席时用有接收者的前台等待，每次不超过 120 秒。不要结束回合后无人接收地空等。

## single-task 单卡接力（本侧适配）

协议语义以 `SKILL.md` 为准；这里只描述本侧启动、派单、观察和恢复写法。

### 总表关联与交棒

启动/恢复时先执行 `SKILL.md`「卡级总表维护与交棒核对」：在已有 `execution_strategy.md` 登记总表路径和唯一维护会话，无关联则明确记无。等待、卡级结果改变、停下及交棒时由维护会话更新总表；交棒前核对状态、下一步、证据及日期，无法完成则报告“总表待同步”，不宣称已交棒。非维护卡在卡级事件写好待同步行后，由其 orchestrator 用 `herdr agent prompt <维护会话的 Herdr 名> "[relay-lite] card-chain update <卡号> <交接工件仓相对路径>"` 通知维护会话（发后照本文件通知投递确认规则读 pane 末行），维护会话先核原证据再汇总，通知不可达按“总表待同步”报告；维护会话所在卡收口汇报前必须先把维护权移交（默认给下一张已开工且关联本表的卡的 orchestrator，多张按总表行序取首张，无则交回用户）：交出方用 `herdr agent prompt <接收方 Herdr 名> "[relay-lite] card-chain maintainer-handoff <总表仓相对路径>"` 通知（读 pane 末行确认投递），接收方在自己的 execution_strategy.md 登记并回一行确认，交出方收到后才改总表页头和自己的登记；接收方未确认/不可达按交回用户处理，未完成移交不算收口。维护会话在本卡收口移交前（或收到非维护卡收口通知时）先执行 `SKILL.md`「自动接续」：总表该下一卡行「自动接续」为「是」（用户写定，含 orchestrator 模型档）且接棒条件证据齐全时，先按 SKILL ② 完成 Issue / 分支与 worktree / Draft MR/PR，再按上方「启动与投递」写法新开 Herdr workspace（`herdr workspace create`）、建 orchestrator tab 并按该行写定的模型档 `herdr agent start`，启动 prompt 给原卡路径、总表路径、Issue 号、分支、worktree 路径、MR/PR 号与写定分配，读 pane 末行确认投递后再对它发 maintainer-handoff；「否」/空白只核对报告；首次关联/恢复核表或用户新写定「是」时，对接棒条件已齐且互不依赖的「是」卡按 SKILL「并行开卡」同样逐张拉起，各开各的 Herdr workspace，此触发不发 maintainer-handoff；模型档未写定或任一步失败按 SKILL ④ 停，行写「等待：<原因>」，不重试、不临时向用户索要分配。这里允许维护会话读写卡级总表，不允许 worker/watcher 读写跨卡计划；默认不委托总表写入。启用 document 时登记维护方可按核心分工顺序委托总表代笔，watcher 仍零写入。总表不是运行真相，恢复仍以本节四类权威为准。

### 编排边界与验证派单

执行 `SKILL.md` single-task 的「编排职责与执行边界」「范围外既有失败」合同。需要测试、基线对照或验收证据复算时，派给已获授权的 executor/当前路径 reviewer（批次内为 batch-reviewer，workflow-final/E2 保留原 phase/path 及各自换人/计数规则）；orchestrator 不使用自己的 shell、后台任务或工具代跑。可做的只读核对限于身份、路径、状态、字段及已有结论的程序性核对，缺证则路由补证，不自行重建业务结论。

非方向小决策按 SKILL「小决策交 decider，问用户攒齐一次」派 decider（`phase=decision`），白名单与仍问用户闭集以 SKILL 为准；decider 结论由 orchestrator 登记 findings（注明 decision 文件）并知会用户。命中问用户闭集的事项先登记 D 项，攒齐后用一次 `AskUserQuestion`（多题合并在同一次调用里；单次上限 4 题，超出时同一停点连续发、不夹带其它工作，仍算一次询问）问用户，不逐项打断；拿不准归哪边按问用户处理。并行开卡期间本卡不自行发问，只登记 D 项并通知维护会话，由维护会话统一问并以 `[relay-lite] card-chain decision <卡号> <用户原始消息指针>` 转回（SKILL「并行开卡」③）；本卡 orchestrator 收到后在本卡 findings 登记来源（经维护会话转达的用户答复及时间）。维护会话在自己的自然停点统一询问时用 同一停点的一次 AskUserQuestion按卡分组。

用户对进行中动作提出原则性纠正时，不自动解释为立即 kill 或删除现场；停止发起新的同类动作，语义不清由主会话澄清并保留现场。明确停止指令或既有停止条件立即执行；终止进程与删除现场分别判断。

### 启动前 model-allocation gate

- 默认模型与推理档提案统一取核心 `SKILL.md`「model-allocation gate」表及 `roles.toml` 对应角色：watcher=`gpt-6-luna`/`medium`，executor 与 batch-reviewer=`gpt-6.1-sol`/`high`，decider=`gpt-6-astra`/`medium`，reviewer=`gpt-6.1-sol`/`high`（batch-reviewer 默认参考 `roles.toml` 的 `[executor]`，独立只读角色）；派单记录模型与推理档两个字段，`gpt-6.1-sol-high` 不作为模型 ID。默认不覆盖在途已确认分配，启动仍遵守下方确认闸。

- 拉起任何 agent 之前，orchestrator 先向用户展示全部拟启动角色/实例的模型与推理档提案表并明确询问确认；推荐默认仅是提案、不写死模型，用户可逐角色修改。**未获明确确认不得启动任何 agent**——缺询问、先启动后补确认、按未确认的默认选择直接拉起、角色/实例/模型/推理档变更免确认，均属违规。
- 确认后由 orchestrator 机械地把确认来源、角色/实例、模型、推理档写入任务工作区 `execution_strategy.md`；未启动的 tab/pane 标 pending，启动后补齐实际 Herdr workspace/tab/pane 与观察来源并逐项比对。`execution_strategy.md` 仅 orchestrator 在授权/停止线、角色/模型/实例、总表关联/维护人、派单路由、批次/clear 闸或提交/checkpoint SHA 变化时维护，其余角色与 watcher 默认只读；启用 document 时按核心首次建卡/代笔与核对合同执行，模型决定不转移；`roles.toml` 只是默认分配提案，不为本模式写死模型；本模式可参考其中默认模型提案与启动写法，运行时采用用户确认后的 `execution_strategy.md` 分配，不把模板直接当作本卡授权。
- 恢复时可沿用已有明确确认且分配未变的快照；新增/更换角色或实例、换模型或推理档必须再次询问确认。超时、静默或最大工具权限均不推定确认；最大工具权限不扩张 commit/push/PR/merge/deploy/verify/人验授权。询问由当前主会话执行，不为询问另启 agent。

### 拓扑与拉起

- 一张任务卡 = 一个 Herdr workspace；每个角色实例一个独立具名 tab，按上方启动模板创建；模型/推理档以 execution_strategy.md 中用户确认的分配为准。

用户明确要求在当前 space 的标签页执行时，复用已核实的 workspace ID，为本卡角色分别创建具名 tab；不新建 space，不依赖失效的继承 ID 或 UI 焦点。同一 Git 任务仍只用一个 worktree，共享 space 不共享写权。

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
- `RELAY_RECEIPT` fail closed 分流：产出型 builder/executor/reviewer/decider（含已启用的 document）命中时只写本角色精确 `BLOCKED.*.md` 单行 signal 后立即停止；watcher 命中保持 repo/workspace 零写入，只用 Herdr prompt 非 durable 通知 orchestrator 后停、不写 BLOCKED。两分支均不得清除任何 `RELAY_*`。

### watcher 节拍与安全 Enter

- 监控范围固定（2026-10-07 用户修订）：所在 Herdr workspace 的其他 agent，每轮按 `workspace_id` 重新发现，新拉起的角色自动纳入；排除 watcher 自身和主编排，不按名字前缀或派单名单筛选。主编排始终只作通知对象，无论是否在这个 space；每轮 `get <编排名>` 解析 `--notify` 对应主编排的实际 pane 身份后排除该 pane，不靠模型猜角色，不静默排除其它角色。
- 固定脚本负责比对：`python3 <SPACE_WATCH> --workspace <Herdr_workspace_id> --notify <编排名> --self <watcher_Herdr名>`。`SPACE_WATCH` 在仓内为 `tools/space_watch.py`，安装后为 `<skill目录>/space_watch.py`；Herdr workspace ID 与标头里的任务文档 workspace 路径分别填写，不能混用。第一轮成功快照建基线，随后每 120 秒 list 全部 agent、按 workspace_id 筛选并按 pane ID get 状态（`agent` 是 kind，不是名字；未命名成员同样按 pane 监控）；新增/离开、`agent_status` 或 `state_change_seq` 有变化即通知，无变化静默。通知只是即时提示，不是 durable signal。
- 投递确认由脚本执行 `herdr agent prompt --wait --until working --timeout 5000` 并核通知对象同 pane、最终 `working` 与 `state_change_seq` 推进（极快结束未捕获 working 也保守报未确认）；失败/超时/未确认不提交比较基线，输出固定 `SPACE_WATCH_BLOCKED reason=...`、仅白名单状态 diff 的 `UNCONFIRMED` 提示并非零退出，交 watcher 报信。脚本不读取/保存终端正文，不发送 Enter、不盲目重发。watcher 需人工核实际投递结果后由编排恢复，可能已送达的未知结果不得当成未发送再补发。
- watcher 常驻，对 repo/workspace **完全只读**：只拉起已批准的脚本子进程并巡检其存活，不再由模型自己目测比较状态；不写 signal/progress/execution_strategy/轮询日志/通知日志或任何文档，不路由、不分派、不启动 agent。快照仅在脚本内存，无日志文件，stdout/stderr 不重定向进仓或任务工作区。启动后立即核脚本进程，再每 120 秒核 PID/退出码；正常运行静默，退出则一次 Herdr prompt 通知 orchestrator 并核投递，无法送达明确报告 blocked 后停止，不自行重拉 agent 或无限重启。检查精确子进程 PID，不以包含脚本路径的 shell 命令文本作为存活证据。
- 启动前核 `HERDR_ENV=1` 与当前 watcher 身份；默认可按 `HERDR_PANE_ID` 自动定位，自填 `--self` 也必须在目标 workspace 且与已提供的 pane 身份一致。`RELAY_RECEIPT` 存在（含空值）时不启动脚本，watcher 只按既有 fail closed 规则通知并停止，不清除环境变量。
- 安全 Enter：仅当三条件**同时**成立才由 watcher 发一次并复验——①本次派单文本仍停在输入框（含 Devin queued 指令仍排队未发出）；②`state_change_seq` 未推进；③当前界面不是审批/确认 UI。任一不满足即不按；一次仍失败则通知 orchestrator 并交编排换 fresh 实例，禁止连按。脚本不承担安全 Enter 判断。


#### single-task watcher 专用派单模板

```text
[relay-lite:single-task] worker · phase=watcher · agent=watcher#<实例> · batch=na · round=1 · workspace=<任务工作区>
Herdr workspace_id=<真实 space ID>；notify=<编排名>；self=<watcher Herdr 名>。
读 AGENTS.md 与本节 watcher 合同；RELAY_RECEIPT preflight，HERDR_ENV 必须为 1。
只启动：python3 <SPACE_WATCH> --workspace <真实 space ID> --notify <编排名> --self <watcher Herdr 名>
监控集合固定为本 workspace 的其他 agent，排除 watcher 自身和主编排；不接受角色名单或名字过滤。
启动后立即核子进程存活，随后每 120 秒查 PID/退出码；不再自己比对 agent 状态。
正常运行静默；退出一次通知编排并确认送达，无法送达报告 blocked 后停；不自动重发未知通知。
不写任何仓库或任务工作区文件，不输出/保存终端正文，不路由、不派活、不启动 agent。
```

脚本由 run_in_background 启动。启动/巡检用短工具等待，脚本内部的 120 秒节拍不由模型维持；stdout/stderr 保留宿主临时进程输出，不另建通知或轮询日志。watcher 的退出通知仍按安全 Enter 三条件核对，脚本永不发键。

### 恢复依据

恢复权威只有四类：原角色自写的 durable signals、独立 review/decision 工件及其原始来源、由 orchestrator 核对的 `execution_strategy.md`、Herdr 实态。`progress.md` 只是施工证据索引、watcher 通知只是即时提示，二者都不是运行真相；本模式不存在 relay 账本。恢复/重启从四类权威重建，不依赖终端存活状态。 `findings.md` 是决定与遗留的检索入口，沿其来源引用回查上述独立工件及用户原始裁决，不新增第五类运行权威；摘要缺源、冲突或仍待用户决定时，不推进依赖该决定的动作，回原责任方澄清。


## 红线

凭据值不入工件；不清除 RELAY_*；watcher 零写入；不代判验收，不运行旧完整计划。

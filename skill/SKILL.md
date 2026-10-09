---
name: relay-lite
description: 独立的单卡接力分工与跨卡接力计划；orchestrator 直接派发 builder/executor/reviewer/decider，watcher 只观察报信。触发 relay-lite/relay-light/接力/分工表或 relay_plan.md；高频交互任务走单会话。
---

# relay-lite

> 版本：v2.1.1

relay-lite 给任意业务仓使用，只提供单卡接力。跨卡接力计划负责卡间依赖和交棒；每张卡内部由 orchestrator 直接分派角色，不建账本或阶段主管。协议来源为独立 relay-lite 仓，不要求其它协议仓 checkout。

## 使用方式

- 一张已落户卡：按本文单卡分工执行，角色/模型先确认。
- 多张卡：复制随安装包提供的 `templates/card-chain.md` 到 relay-lite 仓 `docs/relay/<施工仓名>/<牵头模块>/<plan_id>/relay_plan.md`；一行一张卡，跨模块只有一份表，每张卡仍走单卡接力。
- 未安装仓库的使用者可 clone 独立 relay-lite 仓后维护计划；模板就在 skill 中，不依赖其它仓库。
- 交互任务按下方边界走单会话，总表可记等待，不派交互 worker。

## 按角色读取

所有角色先读本文，按宿主读 [Codex adapter](references/adapter-codex.md) 或 [Claude Code adapter](references/adapter-claude-code.md)；环境操作前读校验返回的 protocol。下列必读条件在首次执行及恢复时均适用，不要求无关角色全量加载。

| 角色/动作 | 继续读取 |
|---|---|
| orchestrator 编排/恢复 | [编排合同](references/orchestration.md)；派单用唯一[派单模板](templates/dispatch.md) |
| 规划/执行/复核 worker | 精确派单、业务仓 AGENTS 和指定 workspace；模板要求由编排写入派单 |
| 测试/基线/失败归因的派单与执行审核 | [取证合同](references/verification.md) |
| decider 咨询与决定 | [编排权限](references/orchestration.md)与[决策指南](references/decision-guide.md) |
| 关联总表的协调会话 | [跨卡合同](references/card-chain.md) |
| 监控/通知/结果等待的编排与 watcher | [watcher 合同](references/watcher.md) |
| 用户明确启用 document 的编排、代笔与责任方 | [文档合同](references/document-role.md) |

## 角色与术语

`executor`（执行者）执行获授权任务，包含代码、文档、配置、诊断和验证；是否可 commit/远端写入以本卡合同为准。`worker` 是所有被派活角色的统称。

| 角色 | 职责 |
|---|---|
| orchestrator | 组织已授权任务推进，核状态与证据来源；识别偏离并交 decider，落实决定、跟踪结果及维护协调工件，不代施工或代判 |
| builder | 建任务工作区与施工计划，承接目标及已生效决定；计划中的路线分歧交编排转 decider，不代替开工授权 |
| plan-reviewer | 独立审核施工计划 |
| executor | 按派单实施、验证并登记证据/发现及可行建议；许可内处理常规问题，需改变路线或越界时交回编排 |
| batch-reviewer | 独立核本批产物，按原卡冻结配方执行 |
| reviewer | 按指定复核路径独立核查产物与证据，指出缺口；不自审施工，decider建议不替代复核结论 |
| decider | 顾问与决策者：在路线偏离、任务调整、异常或需要完整路径判断时提出方案；授权内决定、授权外建议用户裁决；正常已授权步骤不新增决策闸 |
| watcher | 固定程序常驻观察并报信；可选 agent 只协助核状态，对 repo/workspace 零写入 |
| document（按需） | 用户明确启用时顺序代笔，不代判、不改原始结果或 signal |

编排由用户拉起，直接分派本卡角色；一张卡一个终端空间，每实例一个独立具名 tab/pane。agent kind（claude/codex/devin/omp 等）与运行环境分开；环境由下节配置选择，派发命令只在选中环境的协议中维护，宿主工具差异见两 adapter。模型默认提案在 roles.toml，实际分配来自用户确认后的 execution_strategy.md。用户明确使用当前 space 时先核真实 ID，再为各实例建 tab，不另开 space；同一 Git 任务只用一个 worktree，不共享写权。模型确认由当前主会话询问，不为询问另启 agent。

## 环境配置与派发入口

任何新建、恢复、清理、派单、观察或通知前，先读取包内 `environments.toml`，通过 `environment_config.py` 校验；**非零退出或 state 不是 READY 即停止，不执行任何派发/控制命令**。配置目前有且只有 `herdr`，默认也是 `herdr`。模型提案 `roles.toml` 不参与环境选择。

安装包入口（`<SKILL_DIR>` 为当前所读 skill 的真实目录，不是业务仓或任务文档 workspace）：

```bash
python3 <SKILL_DIR>/environment_config.py
python3 <SKILL_DIR>/environment_config.py --environment <用户或派单明确的环境>
python3 <SKILL_DIR>/environment_config.py --environment <恢复指令或已登记环境> --expected <已登记环境>
```

仓内用 `python3 tools/environment_config.py`（默认定位兄弟 skill/）；安装后默认自身目录。首次明确环境优先，否则取 default；恢复将 execution_strategy 已登记环境传入 `--expected`，未指定新选择时也传作 `--environment`。存量缺字段先核原策略和运行身份再登记；冲突停止，不借默认值切换。

成功 JSON：`schema=relay-lite.environment.v1 state=READY`，含 environment/config/protocol；必须读取返回 protocol 后执行。失败 `state=BLOCKED reason=<固定原因>` 是诊断，不是授权或任务signal；按角色fail-closed分流。工具只读，不启动agent、运行配置命令或写文件；RELAY_RECEIPT存在含空值即拒绝，不清RELAY_*。

execution_strategy登记environment、配置/协议来源、CLI版本及启动后实际返回的space/tab/pane/agent与观察来源；未启动填pending，不预测ID。恢复同时核登记与实态。新增环境需独立协议、配置注册及安装清单/测试，不复制到模型adapter，注册不代表启用授权。未知环境、坏配置、缺default/协议、路径越界或实态不满足均停，不回退。

当前仅实现[Herdr](references/environment-herdr.md)，不宣称其它环境能力。派发前实际加载 `herdr --skill`；环境gate与协议通过后按 **space → 独立具名tab → 交互agent → 派单**，复用tab先过核心清理闸。

## 硬规则

凭据值永不进入工件，证据先白名单过滤；原业务仓入口、允许路径、独立复核、verify 与人验闸不变。开工授权不冒充人验，batch PASS 不替代卡级收口；未知结果不自动重试。不部署、不修改环境或业务数据，除非本卡另有明确授权。

## 存量单卡兼容

新派单只用 `[relay-lite:single-task]` 和 executor。已有单卡的 `[relay-light:single-task]` 作为同一协议的存量别名可继续读；旧 coder 的模型确认与 signal 仅作为该实例的历史身份读取，在 execution_strategy.md 登记 coder→executor 映射，不改写原 signal、不跨实例复用确认。旧完整模式标头/计划不受支持，应 BLOCKED 交原责任方；archive 只读，不启动旧计划。

## 卡级总表维护与交棒核对

首次启动/恢复先核总表关联：明确无表记“总表：无（独立单卡）”；提到总表但缺路径记“总表待定位”，不猜。有关联或需定位总表的 orchestrator/交互主会话，更新、通知、交棒、自动接续或并行开卡前必须读[跨卡合同](references/card-chain.md)。worker 默认不读写总表；明确获委托的 document 另按文档合同。

## 适用边界：交互型任务走单会话

需要用户亲手执行环境命令、输入凭据/扫码/物理操作、预计往返确认至少三次、或下一步依赖无法预拆的现场输出时，使用单个会话按业务仓 dev-harness 处理；独立复核、入口/出口、人验与证据要求不变。接力总表保留等待与恢复入口，不派交互 worker。

## `single-task` 单卡接力模式

用于一张已落户卡的规划、执行、复核与人验接力。跨卡计划由登记维护会话管理，其它 worker 不读写计划，不创建账本，不使用旧阶段词。

### 编排职责与执行边界

orchestrator 只派发、通信、核状态/已有结论与路由，不代施工、测试、归因或验收。首次编排/恢复及路线偏离时必读[编排合同](references/orchestration.md)；decider 同读[决策指南](references/decision-guide.md)。正常已授权步骤直接推进，超出权限的决定交用户。

### 范围外既有失败

测试、对照取证或失败归因派单前，orchestrator、executor 与对应 reviewer 必须读[取证与失败合同](references/verification.md)。归因闭合不等于修复或验收放行；缺证/未知不自动重试，不放宽必需通过项。

### 标头与 phase 闭集

- worker 派单 prompt 首行固定为 `[relay-lite:single-task] worker · phase=<phase> · agent=<role>#<instance> · batch=<n|na> · round=<n> · workspace=<repo-relative-path>`；存量单卡标头按「存量单卡兼容」读取。
- phase 闭集：`plan` / `plan-review` / `batch` / `batch-review` / `workflow-final` / `e2-code-review` / `decision` / `watcher` / `human-acceptance`；`batch=1|2|3|na`。
- `RELAY_RECEIPT` fail closed 分流：进程环境存在 `RELAY_RECEIPT` 时，产出型 builder/executor/reviewer/decider（含已启用的 document）只写本角色精确 `BLOCKED.*.md` 单行 signal 后立即停止；watcher 保持 repo/workspace 零写入，只用 选中环境的通知入口 非 durable 通知 orchestrator 后立即停止，不写 `BLOCKED`。两个分支均不得清除任何 `RELAY_*` 环境变量。

### model-allocation gate（启动任何 agent 之前的硬闸）

默认模型提案（2026-10-07 用户设置）：

| 角色 | Codex 模型 | 推理档 |
|---|---|---|
| watcher | `gpt-6-luna` | `medium` |
| executor / batch-reviewer | `gpt-6.1-sol` | `high` |
| decider | `gpt-6-astra` | `medium` |
| reviewer | `gpt-6.1-sol` | `high` |

`reviewer gpt-6.1-sol-high` 按模型 `gpt-6.1-sol` 与推理档 `high` 分开填写，不把后缀当模型 ID。`batch-reviewer` 默认参考 `roles.toml` 的 `[executor]` 模型、推理档和启动参数，其只读约束由派单 prompt 承担。相应启动模板见随 skill 安装的 `roles.toml`：`codex -m <模型> -c model_reasoning_effort=<推理档> --dangerously-bypass-approvals-and-sandbox`。未列出的角色保持原有默认或用户指定；本表是新建分配的默认提案，不覆盖在途卡的明确确认，不替代下方启动确认闸。single-task 确认后的分配仍写入 `execution_strategy.md`，不创建计划级模型 config。

- orchestrator 必须先向用户展示全部拟启动角色/实例的模型与推理档提案表，并明确询问确认；推荐默认仅是提案，不写死模型。用户可逐角色修改；**未获明确确认不得启动任何 agent**。唯一例外：卡级总表「自动接续」栏由用户写定的分配（见该节），视为对应角色的明确确认，其余角色仍照本条询问。
- 确认后由 orchestrator 机械地把确认来源、角色/实例、模型、推理档写入 `execution_strategy.md`；未启动的 tab/pane 标 pending，启动后补齐实际 environment/space/tab/pane 与观察来源并逐项比对。默认由 orchestrator 维护 `execution_strategy.md`，watcher 与其它角色只读；启用 document 时按[文档代笔合同](references/document-role.md)的首次建卡/代笔规则登记，由 orchestrator 核对分配事实。授权与模型确认事实保留在此，业务决定只按下文「决定落点」引用 findings。
- 恢复时可沿用已有明确确认且分配未变的快照；新增/更换角色或实例、换模型或推理档必须再次询问确认。超时、静默或最大工具权限均不推定确认；最大工具权限不扩张 commit/push/PR/merge/deploy/verify/人验授权。

### 生命周期与计数

固定生命周期：任务工作区七件套与 `task_plan.md` → plan review → 分批开发 + batch review → 开发后按 `task_type` Recipe 展开的全量 workflow-final review → E2 code_review → 主会话人验。batch review 与 workflow-final 是**两道独立闸**，batch PASS 不替代 final。

- `review_round` 与 `remediation_count` 分开记：初审 `review_round=1 remediation_count=0`；plan/batch review 各最多整改 2 轮，FAIL 回同一 builder/executor、原 reviewer 复审；超限交 decider，六类方向问题（方向/范围/验收/数据语义/安全/生产影响）交用户；超限之外的非方向小决策同样交 decider，见「编排职责与执行边界」。
- workflow-final 每条适用 path 最多返工 2 轮，**每轮换 fresh reviewer**，不得复用上一轮实例冒充 fresh；E2 `code_review` 初审为完整 fresh，仅出现 open P0/P1 后由**同一 `reviewer_session_id`** 做 targeted attempt 2。两层证据分别登记身份/输入/finding/结论，条件相斥不得合并为一条。
- 完成谓词：全部适用 `task_type` Recipe path PASS 或有可核查 N/A，最终汇总无 open P0/P1；heavy 五路（code-round1/code-round2/requirement/consistency/lesson）一条不少；单一 final reviewer、batch PASS 或 E2 receipt 均不替代整套 Recipe。施工者不复核自己的施工。

### 新批次与新任务的标签页会话清理闸

这里的 clear 指 agent 的会话上下文清理，不是 shell 的 `clear` 清屏。标签页承接新的批次或新的独立任务时，orchestrator 先核真实 tab/pane、当前任务与 agent kind，按以下时序清理，再派单。

- 仅当该批 batch reviewer 的 durable signal 为 PASS **且**本批工件齐全（本批交付物、验证证据、executor signal、review 产物、reviewer durable PASS）后，orchestrator 对本批 executor 与 batch reviewer **各执行一次 `/clear`** 并分别复验已清理，之后才启动下一批。终端 idle/done 或 executor DONE 不替代此门。
- **新的独立任务**：复用标签页前，先核前任务已按原合同停下，且工件、证据与原角色 signal 已保存；对该标签页内的旧会话**先 clear 并确认，再投递新派单**。清理完成后 worker 重新读取新任务的 AGENTS、精确派单与指定 workspace，不能沿用前任务授权或写权。全新实例的空会话按真实启动事实登记，不伪造执行过 `/clear`；原合同要求新 workspace/实例时仍照原合同创建。
- **执行与确认**：使用该 agent kind 已核实支持的原生会话清理命令（支持 `/clear` 时使用 `/clear`，其它 kind 使用已核实的等效命令），与新派单分两次投递；命令送达后，核对实际 pane 的原生清理成功提示或新空会话状态，再发派单。仅命令已输入、`state_change_seq` 推进、idle/done 或屏幕变空，都不能证明上下文已清理。在既有 `execution_strategy.md` 记录清理对象、对应任务/批次、命令与确认依据，不新建清理账本。前批已 clear 且复验成功、期间未再承接任务时，直接使用该已确认空会话，不重复 clear；恢复时回查原记录与 选中环境实态，无法确认仍停在清理门。
- FAIL/整改期间禁止 `/clear`，保持原 executor/原 reviewer session，不借清理清零整改计数；清理失败或无法复验时不得启动下一批，也不盲目重复发送 `/clear`。watcher 常驻、不 clear；decider 按需拉起，不纳入每批固定 clear。
- 同任务补证与 E2 targeted attempt 2 沿用原会话，不作为新任务 clear；workflow-final 每轮和要求 fresh 的独立复核仍换未参与实施的新实例，不能把旧实例 `/clear` 后冒充 fresh。清理失败或结果未知时不投递新任务、不盲重发。clear 不删除或改写历史工件、signal、失败、`review_round`/`remediation_count`，不清除 `RELAY_*`，不为未闭合原任务放行或重置额度。

### durable signal 与写者边界

- 每个产出型 worker 的收口物是单行 signal：`DONE`/`BLOCKED` + `task phase agent batch path review_round remediation_count verdict evidence`（BLOCKED 另含 `reason=<snake_case>`），值无空白、证据为 repo 相对路径逗号分隔；写完即停，不等 `node_closed`，不碰跨卡计划或账本。
- sole writer（未启用文档 agent 时）：`execution_strategy.md` 仅 orchestrator 写；各 review/check/decision 工件由对应 reviewer/decider 自写；`lesson_candidates.md` 仅 executor 按派单追加；`progress.md` 仅由当前顺序执行的 batch executor 在自己 batch 完成时追加**一条**简洁施工里程碑 + 证据引用——不记决定、pane/agent 状态、轮询、通知或终端输出；reviewer/watcher/orchestrator 不写 progress。
- **决定落点**：`findings.md` 承载用户裁决（含点选/确认时间与原始来源，未知时间如实标未知）、decider 结论摘要及独立 decision 引用、D 项（待用户决定项）状态、范围外发现与 P3 遗留去处、给用户的知会。遗留须用户明确点头并标去处；未确认保持待决定，不把知会、沉默或编排摘要当作同意，不用记录代替解决。
- **findings 写者**：orchestrator 只追加已有裁决的来源、摘要、D 项状态、遗留去处和知会，不自行生成业务结论或基线归因；executor 按派单追加发现与证据，基线归因仍遵守[取证与失败合同](references/verification.md)的专属写者及审核闭合流程。同文件由编排安排错开写入，每次派单注明精确章节与唯一写者；复核期间冻结相关候选内容，不并写或覆盖他人记录。仅启用 document 时可按原责任方确认代笔，不强制启用。
- **执行策略内容**：`execution_strategy.md` 仅在以下编排事实变化时维护：授权与停止线、角色/模型/实例、总表关联与维护人、派单与路由、批次流转与 clear 闸、提交/checkpoint SHA；业务决定处只放指向 findings 对应条目的指针，不放决定正文。模型确认事实不因此迁出，记录模型来源不等于扩大授权。
- **人验与恢复**：主会话人验后的用户选择及知会仍落 findings，并指回真实用户来源；decider 摘要不覆盖独立 decision，开工授权不冒充人验。缺来源或摘要与原件冲突时保留待核状态并回原责任方澄清，受影响动作不凭摘要放行；恢复按下文四类权威回查。
- watcher 对 repo/workspace **完全只读**：不写 signal/progress/execution_strategy/轮询日志/通知日志或任何文档；不路由、不分派、不启动 agent。

### 文档 agent（single-task 可选分工）

默认不启用，原责任方直接写文档，不登记 document、不等 SYNCED。用户明确启用后，首次派单前编排、document 与内容责任方必须读[文档代笔合同](references/document-role.md)；代笔不转移决定权，SYNCED 不替代原路径 PASS。

### watcher 节拍与安全 Enter

启动/接管监控、派单后等待结果或处理通知前，编排与 watcher 必须读[watcher 通用启动与监控步骤](references/watcher.md)及选中环境协议。默认普通终端运行固定程序；watcher 零写入，通知不替代 durable signal/报告，未知不盲重发。宿主工具写法见 adapter。

### 恢复依据

恢复权威只有四类：原角色自写的 durable signals、独立 review/decision 工件及其原始来源、由 orchestrator 核对的 `execution_strategy.md`、选中环境实态。`progress.md` 只是施工证据索引、watcher 通知只是即时提示，二者都不是运行真相；恢复/重启时从四类权威重建，不依赖终端存活状态。 `findings.md` 是决定与遗留的检索入口，沿其来源引用回查上述独立工件及用户原始裁决，不新增第五类运行权威；摘要缺源、冲突或仍待用户决定时，不推进依赖该决定的动作。

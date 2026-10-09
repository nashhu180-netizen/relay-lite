---
name: relay-lite
description: 独立的单卡接力分工与跨卡接力计划；orchestrator 直接派发 builder/executor/reviewer/decider，watcher 只观察报信。触发 relay-lite/relay-light/接力/分工表或 relay_plan.md；高频交互任务走单会话。
---

# relay-lite

> 版本：v2.1.0

relay-lite 给任意业务仓使用，只提供单卡接力。跨卡接力计划负责卡间依赖和交棒；每张卡内部由 orchestrator 直接分派角色，不建账本或阶段主管。协议来源为独立 relay-lite 仓，不要求其它协议仓 checkout。

## 使用方式

- 一张已落户卡：按本文单卡分工执行，角色/模型先确认。
- 多张卡：复制随安装包提供的 `templates/card-chain.md` 到 relay-lite 仓 `docs/relay/<施工仓名>/<牵头模块>/<plan_id>/relay_plan.md`；一行一张卡，跨模块只有一份表，每张卡仍走单卡接力。
- 未安装仓库的使用者可 clone 独立 relay-lite 仓后维护计划；模板就在 skill 中，不依赖其它仓库。
- 交互任务按下方边界走单会话，总表可记等待，不派交互 worker。

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

编排由用户拉起，直接分派本卡角色；一张卡一个终端空间，每实例一个独立具名 tab/pane。agent kind（claude/codex/devin/omp 等）与运行环境分开；环境由下节配置选择，派发命令只在选中环境的协议中维护，宿主工具差异见两 adapter。模型默认提案在 roles.toml，实际分配来自用户确认后的 execution_strategy.md。

## 环境配置与派发入口

任何新建、恢复、清理、派单、观察或通知前，先读取包内 `environments.toml`，通过 `environment_config.py` 校验；**非零退出或 state 不是 READY 即停止，不执行任何派发/控制命令**。配置目前有且只有 `herdr`，默认也是 `herdr`。模型提案 `roles.toml` 不参与环境选择。

安装包入口（`<SKILL_DIR>` 为当前所读 skill 的真实目录，不是业务仓或任务文档 workspace）：

```bash
python3 <SKILL_DIR>/environment_config.py
python3 <SKILL_DIR>/environment_config.py --environment <用户或派单明确的环境>
python3 <SKILL_DIR>/environment_config.py --environment <恢复指令或已登记环境> --expected <已登记环境>
```

仓内开发入口为 `python3 tools/environment_config.py`，工具默认定位兄弟 `skill/`；安装后默认定位自身目录。首次明确 environment 优先，否则取配置 default；恢复必须传入 `execution_strategy.md` 已登记 environment 作为 `--expected`，未指定新选择时同时作为 `--environment`，有冲突停止，不静默切换。存量卡缺该字段时先根据原策略与实际运行身份核实并登记，不借默认值切换环境。

成功 JSON `schema=relay-lite.environment.v1`、`state=READY` 包含选中 `environment`、`config` 和 `protocol`；读取返回的协议路径，按它执行。失败 JSON `state=BLOCKED` 的固定 `reason` 是阻塞原因，不是授权或任务完成 signal；按原角色 fail-closed 出口处理。工具只读取，不启动 agent、执行配置命令或写工件。`RELAY_RECEIPT` 存在含空值时工具拒绝，先按本文角色分流处理，不清除任何 `RELAY_*`。

在既有 `execution_strategy.md` 登记选中 environment、配置/协议来源、CLI版本以及启动后从实际返回核实的 space/tab/pane/agent 身份；未启动写 pending，不预测 ID。恢复同时核已有选择与该环境实态。新增环境需新增其独立协议、注册配置并追加安装器封闭清单/测试，不复制到模型 adapter，也不因注册就自动启用或授权。未知环境、配置损坏、缺 default/协议、路径越界或实际环境不满足均停止，不回退。

Herdr 派发前必须加载当前 `herdr --skill`；配置 gate 与环境协议均通过后按 **space → 独立具名标签页 → 交互式 agent → 派单**。新任务/新批次复用同标签页时先执行下文清理闸，再投递。详见配置所选 [Herdr 环境协议](references/environment-herdr.md)；仅 Herdr 已实现，不宣称其它环境能力。

## 硬规则

凭据值永不进入工件，证据先白名单过滤；原业务仓入口、允许路径、独立复核、verify 与人验闸不变。开工授权不冒充人验，batch PASS 不替代卡级收口；未知结果不自动重试。不部署、不修改环境或业务数据，除非本卡另有明确授权。

## 存量单卡兼容

新派单只用 `[relay-lite:single-task]` 和 executor。已有单卡的 `[relay-light:single-task]` 作为同一协议的存量别名可继续读；旧 coder 的模型确认与 signal 仅作为该实例的历史身份读取，在 execution_strategy.md 登记 coder→executor 映射，不改写原 signal、不跨实例复用确认。旧完整模式标头/计划不受支持，应 BLOCKED 交原责任方；archive 只读，不启动旧计划。

## 卡级总表维护与交棒核对

本节适用于已关联的卡级接力计划（衔接总表）。`relay_plan.md` 是跨卡导航表，不是账本或节点执行器。这是会话必做的流程检查，**没有程序自动同步或强制拦截**。

- **入口**：单卡 orchestrator 在首次启动/恢复时检查用户交接和已有 `execution_strategy.md`，关联已知总表并记录「总表：`relay-lite:<仓相对路径>`；维护会话：<唯一会话/恢复入口>」。交互单会话在已有进度工件记录，不为此新建工作区。确认没有关联总表的独立卡写「总表：无（独立单卡）」即可；交接提到总表却缺路径时标「总表待定位」，不猜路径、不静默记无。已有在途卡下次恢复时补登记，不重启角色或补造历史。
- **写入者**：每份总表只由登记的一个协调会话写；单卡时可以是原 orchestrator，交互任务可以是原主会话，不要求另拉常驻 agent。多卡并行时各卡在自己的既有交接工件提供行更新内容和证据指针，由该维护会话顺序汇总，不让多个 executor/orchestrator 并写总表。维护人更换先完成交接并同步关联记录（时机见下条「维护人卡收口前移交」）；worker/reviewer/decider/watcher 默认不写总表；single-task 显式启用文档 agent 时，登记维护会话可按下文顺序委托代笔，维护责任不转移，不扩大文件或消息发送权限。
- **触发**：首次关联与恢复时先核对原卡、workspace 证据及当前行；进入/解除等待、卡级结果改变（例如复核结束、合入、验收）、准备停下或交棒时，更新对应行的接力情况、下一步/去向、证据引用和核对日期。不抄批次日志，不把未发生的结果写成完成。
- **非维护卡通知**：关联了总表的非维护卡，在卡级事件（开工、进入/解除等待、卡级结果变化如复核结束/合入/验收、停下、交棒）发生并把待同步行写进自己的交接工件后，由该卡 orchestrator（交互单会话为主会话）向登记的维护会话发一行 选中环境的通知入口：`[relay-lite] card-chain update <卡号> <交接工件仓相对路径>`（除卡号和路径外不加中文）。维护会话收到后先核原证据，再按顺序汇总更新对应行与核对日期；不因通知直接照抄。通知失败（维护会话不在线/不可达）时走下文「无法更新」出口报告“总表待同步”，不自行写总表。这只是 orchestrator 向维护会话的内部通知，不扩大 worker/reviewer/decider/watcher 的写权或消息权限，也不授予任何开工/合入权限。反方向由维护会话发给他卡的 `card-chain decision` 见「并行开卡」③，同样只是通信，不授予开工/合入权限。
- **维护人卡收口前移交**：维护会话所在的卡，在收口汇报（宣称整卡完成/交棒）前必须先移交维护权：默认交给下一张已开工且关联本表的卡的 orchestrator（多张时按总表行序取首张）；没有已开工卡时交回用户，标「维护会话：待指定（用户）」；用户可另行指定接收方。移交步骤：交出方用 选中环境的通知入口 通知接收方 orchestrator（`[relay-lite] card-chain maintainer-handoff <总表仓相对路径>`，发后读 pane 末行确认投递）；接收方在自己的 execution_strategy.md（或进度工件）「卡级总表」登记为维护会话，并回一行确认；交出方收到确认后再改总表页头「维护会话」和自己的登记。交出方不写接收方的工件。接收方未确认/不可达时不算移交完成，按“交回用户”处理（页头写「维护会话：待指定（用户）」并报告用户）。未完成移交不算收口完成。
- **交棒核对**：关联总表的卡在对外报告“已交棒”或按总表接续下一卡前，逐项核对：①行状态与原卡证据一致；②等待原因/下一步清楚；③交接条件有证据指针，版本交接有提交 SHA；④本次核对日期已更新。普通停下可以报告等待，不要求强行完成。确认项写在原有交接/最终汇报的一行「总表已核对：<路径>；<卡号>；<日期>」，不另造 receipt 或运行账本。对外消息仍需原授权，核对本身不授予下一卡开工/合入/verify 等权限；下一卡开工授权只来自总表该卡行的「自动接续」栏（见下条）。
- **自动接续**（2026-09-30 用户裁决）：总表每行设「自动接续」栏，**只由用户写定**（或用户明确指示主会话代填，代填必须附用户消息指针，该指针即页头来源），维护会话与任何 orchestrator 只读、不得新增或修改该栏；页头记「自动接续授权：<用户消息/提交 SHA 指针>」，核对时追溯不到用户来源即按「否」。栏值以字面「是」开头才算是，其余（「否」、空白、待定）都按「否」。「是」必须同时写定下一卡 orchestrator 的模型与推理档，可再附其余角色分配；写定的分配视为该卡 model-allocation gate 的明确确认（gate 节的对应例外），下一卡 orchestrator 机械登记到自己的 `execution_strategy.md`，未附的角色由它启动后照 gate 向用户询问。「是」等同于 AGENTS.md 协作流程第 5 条对该卡的开工授权，范围、验收以原卡为准。执行者只有**维护会话**：本卡收口时在「维护人卡收口前移交」之前执行一次；收到非维护卡收口的 `card-chain update` 通知时，核完原证据后也按 ①–④ 对以该卡为前置的下一卡执行，这种情况不触发维护权移交；非收口时机的触发见下条「并行开卡」。非维护卡收口只发通知，不自行执行。对以收口卡为前置的每张下一卡按行序处理：①核对其「接棒条件」——条件必须写明以哪道闸为准（合入 SHA / verify 提交 / 人验结论），且全部前置卡（含其它链路的扇入前置）都有证据指针，任一缺证即不开；含人验的条件由主会话/用户在接力流程外给出结论，orchestrator 不代判；条件在本卡收口之后才满足的（如本卡 verify、人验），收口时只写「等待：<条件>」，收口卡不驻留等待，之后由用户人工放行或指示维护会话再判。②「是」且条件齐全时，按目标仓协作规则做开局准备且只做这五步：Issue 立户（正文取自原卡的目标/范围/验收/档位/风险/停止边界，原卡缺项即按 ④ 停；已有 Issue 则复用）、从目标远端 master 建任务分支与 worktree、开工提交推上去建 Draft MR/PR 并关联 Issue、按选中环境协议新开一个 space、按环境协议与 adapter 的宿主写法以写定的模型档拉起该卡 orchestrator；启动 prompt 给原卡路径、总表路径、Issue 号、分支名、worktree 路径、MR/PR 号与写定的分配，由它自己登记，本卡 orchestrator 不写它的工件；读 pane 末行确认投递。多张满足条件的「是」卡逐张全部拉起，维护权按「维护人卡收口前移交」交给行序首张。③「否」时只做到核对，行写「等待：用户放行开工」并报告用户，不建 Issue、不拉 agent。④任一步失败（Issue 建不成或原卡缺项、worktree 冲突、分配未写定、拉起不成或投递未确认）即停当前这张卡：行写「等待：<原因>」，其余「是」卡按行序继续；收口汇报带上失败原因和已建成的半成品（Issue 号、分支、Draft MR/PR 号、workspace），交用户接手或清理；不重试、不修环境、不向用户临时索要分配、不代做下一卡施工；维护权仍按「维护人卡收口前移交」默认规则处理，只是本次失败的卡不算已开工。自动接续不设跨卡常驻编排、不新增角色/账本/脚本；被拉起的 orchestrator 仍按 `single-task` 从入口登记开始执行，对未写定的角色自行走 gate。
- **并行开卡**（2026-10-06 用户裁决）：接棒条件互不依赖的多张「是」卡（彼此都不是对方的前置，接棒条件写「无」也算）可同时按各卡选中环境各开一个 space 并行推进，不必等前一张收口；允许路径重叠或改同一文件的卡视同有依赖，按行序串行，拿不准按有依赖处理；因此被串行的卡行写「等待：与 <卡> 路径重叠」，维护会话收到该冲突卡收口通知时，对它同样按 ①–④ 再判，不因它不以冲突卡为前置而漏判。除上条两种收口触发外，维护会话在首次关联/恢复核表时，以及用户新写定「是」后，对当时接棒条件已齐、行状态为「未开始」且尚无已登记 Issue/分支/workspace 的「是」卡按上条 ①–④ 各执行一次（已开工、已收口或留有半成品的卡一律不再拉起，半成品按 ④ 交用户）——这只是「自动接续」同一流程的另一触发点，不是新授权；非收口触发不移交维护权，维护会话照常留在原位。边界：①每张卡仍须本行「自动接续」为「是」且全部前置有证据，有依赖的卡仍等其前置，「否」的卡只核对报告；②维护权仍只一份，并行各卡的 orchestrator 只按「非维护卡通知」发 `card-chain update`，总表仍由维护会话顺序汇总；③询问者唯一：并行期间（同表有两张及以上卡在推进）各卡 orchestrator 不自行向用户发问，只按 single-task「小决策交 decider，问用户攒齐一次」先交 decider、把仍需用户决定的事项登记为本卡 findings D 项，作为「进入等待」卡级事件通知维护会话；维护会话在对应行写「等待：用户决定（<卡> findings D 项）」，在维护会话的最近自然停点把各卡待决项按卡分组一次问用户（命中停卡、安全、生产影响的立即问），再用 选中环境的通知入口 `[relay-lite] card-chain decision <卡号> <用户原始消息指针>`（如维护会话名 + 答复时间；只传指针，不在 prompt 里放答复原文）把每卡答复的来源转给该卡 orchestrator（读 pane 末行确认投递），由它在本卡 findings 登记来源（经维护会话转达的用户答复、时间）。维护会话不写他卡工件、不改写或代答；只剩一张卡在推进时恢复由本卡 orchestrator 自问；④并行不改变每卡的 model-allocation gate、Issue/分支/Draft MR/PR、一卡一 worktree 与收口规则，也不新增跨卡常驻编排。
- **无法更新**：路径不存在、维护会话不可用、无写权或文件冲突时，不创建替代表或覆盖他人修改；在本卡既有交接工件保留待更新的行内容及证据位置，并向用户报告「总表待同步」和原因。未核对前不能宣称已交棒、不能依赖旧摘要放行后续；不阻断无关的已授权卡内工作。恢复后先核原证据再补表，不能仅凭旧摘要恢复。

## 适用边界：交互型任务走单会话

需要用户亲手执行环境命令、输入凭据/扫码/物理操作、预计往返确认至少三次、或下一步依赖无法预拆的现场输出时，使用单个会话按业务仓 dev-harness 处理；独立复核、入口/出口、人验与证据要求不变。接力总表保留等待与恢复入口，不派交互 worker。

## `single-task` 单卡接力模式

用于一张已落户卡的规划、执行、复核与人验接力。跨卡计划由登记维护会话管理，其它 worker 不读写计划，不创建账本，不使用旧阶段词。

### 编排职责与执行边界

- orchestrator 负责已授权的派发、通信、运行状态核对、信号路由及指定协调工件维护，并按下方规则识别需要重新规划的偏离、落实决定与跟踪结果；担任维护会话的 orchestrator 另可按「卡级总表维护与交棒核对」的「自动接续」「并行开卡」授权（含本卡收口前、收到非维护卡收口通知时及并行开卡的非收口触发）执行下一卡的开局准备，限「自动接续」②写明的五步，不含下一卡的施工与测试；不自行运行测试、回归、复现、基线对照或业务证据复算，也不为这些工作自行建立临时测试目录/worktree、装配环境。不得以“只读”“临时”“交用户前自核”为例外。
- 测试和基线取证交当前获派的 executor；独立核验交发现问题的当前复核路径 reviewer（批次内为 batch-reviewer，workflow-final/E2 按下节对应路径），必要时复跑。编排发现缺证或矛盾，退回对应产出方补证，不代产证据、不代判 PASS；补证沿用现有 phase、signal、轮次与写者规则，不新增角色或绕过 model-allocation gate。
- 编排可读 signal、报告、Git 状态/SHA/diff，核对路径、身份、字段与既有结论是否一致；可解析 JSON 读取已有 verdict/证据引用。重新计算业务结果、判断验收或失败归因属于执行/复核：例如从 ops profile 计算 capability 增删、digest 差异或 manifest hash，或从测试输出推导“既有失败、可放行”，均应派给 executor/reviewer。是否越界按用途判断，不按命令名称或是否写文件判断。
- Draft MR/PR 与闸门评论（2026-09-30 用户裁决，新卡起生效，在途卡按原合同继续）：Issue 立户、任务分支首个提交推上去后即建 Draft MR（GitLab）/ Draft PR（GitHub）关联 Issue，号登记在 `execution_strategy.md`；分支基于目标远端 master，合并用平台 squash。plan-review、batch-review、workflow-final 各路、E2 code_review 与人验结论，由 orchestrator 按判定方自写结论发评论（闸门名 + verdict + 被审 SHA + P0～P3 计数 + 证据路径），只转述、不代判、不含凭据；每道闸通过或返工提交后推送分支更新 MR/PR。发评论属通信/协调职责，不改变「不代判 PASS」；推送/建 MR 的机制与合并授权仍按各仓协作规则，最终解除 Draft、更新描述并按授权合并。
- **小决策交 decider，问用户攒齐一次**：既有方案及授权覆盖的正常步骤直接推进；任务调整、路线选择、同类阻塞反复出现、局部成功后仍缺通往验收的路径、可预见的新增授权需求，交 decider（`phase=decision`）重审从当前状态到原目标的完整路径。编排核既有报告及步骤/授权依赖以识别这些信号，不自行作技术归因；单纯缺证先路由原产出方补证，已触发停止条件的受影响动作先停，不等待顾问分析。
- **决定权限与咨询范围**：decider 可决定验证方法或环境细节、派单纠正、允许路径内修法、诊断后修复方式、已授权范围与额度内额外整改、不扩路径的兼容/实现路线。**仍问用户的闭集**：扩出卡上允许路径、新的真实外部调用或额度授权、停卡、合入（开工授权包已覆盖则直接按授权执行）、部署、改变验收口径及「生命周期与计数」六类方向问题。拿不准权限时不放行受影响动作；咨询仍可先研究已有证据、备选路线和推荐，不能只以“请用户决定”代替分析。咨询范围宽于决定权限，不授予取证、资源操作、派活或验收权；缺事实由编排派原 executor/reviewer 补证。decider 不代写施工实现，也不以冻结完整脚本迫使后续普通修正逐次索权。
- **完整路径与再次询问**：decider 沿用 `decision.<d>.md`，说明当前路线是否可达目标、后续步骤/依赖、主要失败分支、权限/预算依据、验证与收束，以及本轮成功后仍需用户决定的事项。报告长度按问题复杂度调整，详见[决策指南](references/decision-guide.md)；不是每步新增审批。编排核这些内容及来源是否齐全，缺项退原 decider 补齐，不代写技术结论。再次提问必须交代新增事实/超出边界、此前为何无法合理预见；若此前漏想，如实承认并补齐剩余路径，不把漏想包装成新风险。
- **落实与升级**：decider 结论由编排在 findings 记摘要、decision 引用并知会用户；权限与适用证据齐备的卡内决定不等回复即路由，DECIDED 本身不构成授权或验收。触及用户闭集的部分登记 D 项，带具体方案、推荐及后续审批点，在最近自然停点集中询问；不因部分待决停止无依赖的已授权工作。紧急停止/安全/生产影响按既有规则立即报告或问用户，不等待攒齐；只执行已授权安全处置，不借紧急之名杀进程、清理或扩权。并行询问仍由维护会话统一处理（「并行开卡」③）；decider 未在确认分配内时，模型确认并入该次询问，不擅自拉起。
- **边界与结果跟踪**：用户明示停止线、窄授权、预算与失败/未知历史保持；协议更新不追溯扩权。许可内可修复故障与身份/结果未知、新风险、预算耗尽分开处理，后者不自动重试或追加额度。编排收到执行/复核结果后与 decision 约定的结果及去向核对，不代判 PASS；同类阻塞重复或仍不能接近目标时带历史回 decider 整体调整，不循环追加同类限定包。builder 承接生效方案，reviewer 保留独立结论，watcher只观察报信，document只按原责任方确认代笔；不增角色、账本、固定审批层或重置计数。

- 用户对进行中动作提出原则性纠正时，不自动解释为立即终止或删除现场；停止发起新的同类动作，按明确指令处理在途工作。语义不清由主会话澄清并保留现场；明确要求立即停止或命中既有停止条件时立即执行。终止进程与删除现场分别判断，不以纠正分工为由一并清理证据。

### 范围外既有失败

- **取证与写者**（默认写者；启用文档 agent 时只委托人工落笔，原始取证责任不变）：executor 在首批或首次发现失败的复核路径取证，由对应 reviewer 独立审核。`findings.md` 中基线取证、归因及其关闭状态仅 executor 写；下文决定记录的追加权不扩大归因写权。reviewer 只写自己的 review/check 工件；reviewer 发现的基线问题由编排路由 executor 登记，编排不自行登记归因。测试明细放派单指定的证据文件，`progress.md` 仍只由当前 batch executor 在批末写一条里程碑和证据引用。
- **最小证据**：记录基线用途（整卡或批次）、完整 SHA 与选择依据、候选 SHA 及未提交差异标识、精确 cwd/解释器/完整命令、必要环境与依赖条件、实际收集范围和 passed/failed/error/skipped/deselected 数量、退出码、逐项测试标识与失败阶段/原因、证据路径。批次前基线不能冒充整卡开工基线；同一解释器不等于环境可比，缺少资源或导入了候选代码的对照不作有效基线。
- **临时现场**：由执行者按派单指定位置及权限准备隔离对照环境，优先考虑 `git archive <SHA>`，保留所需文档/配置/资源并核实实际导入路径；依赖 Git 元数据的测试不能强制使用 archive，替代方法须在派单允许范围内。不得修改共享依赖或借临时现场扩张权限。正式验证期间冻结影响被测现场的写入；可能互相污染的测试严格串行，每次取得退出码再继续。先保存白名单过滤后的有效证据，再按派单清理自己建立的临时现场。
- **归因与放行分开**：证据完整且独立审核通过，才可将归因记为 `closed-as-baseline`；它只表示归因闭合，不表示缺陷修复、验收豁免或 CI 通过。证据缺失/未审核保持待核，不先关闭后补。允许失败集合必须引用明确清单和审核证据，并符合既有验收合同；从“全绿”变为“无新增失败”若改变验收标准，交用户确认，不由编排/executor/reviewer 自行放宽。基线归因不自动降级 P0/P1，不覆盖必需 CI、独立复核、verify 或人验门。
- **批次内闭合时序**：首次送审时 executor 可在 findings 保留待核状态并提交完整证据。若 reviewer 确认基线归因、但 findings 尚待回写审核引用/关闭状态，须在自己的 review/check 记录归因结论及待补登记项，以本批 FAIL 按既有整改路径回同一 executor（计入原整改计数，不清上下文、不新增或重置轮次）。executor 仅按审核证据更新 findings/允许集合引用并重新送审，由原 reviewer 核对后才发 batch PASS；归因成立不等于整批 PASS。不得先 PASS/clear 再找编排代写；本批剩余整改额度不足时按既有超限路径处理。
- **最终复核/E2 首次发现**：留在发现问题的原 `phase/path`，不重开已 PASS/clear 的批次，也不借 batch-reviewer 替代当前路径 reviewer。缺证或归因未闭合由该 reviewer 在自己的工件与 signal 记录阻断项；编排按本路径现有整改合同派 executor 补证/回写 findings（派单沿用 `phase=workflow-final` 或 `phase=e2-code-review`、原 path，`batch=na`，精确产出和 signal 路径由派单指定）。executor 仅施工/补证并送审，不自审。workflow-final 每轮复审换 fresh reviewer、每 path 最多返工 2 轮；E2 仅初审有 open P0/P1 才进入同一 `reviewer_session_id` 的 targeted attempt 2，不发第三派。归因确认但 findings 待回写时同样作为未闭合项返回 executor，不能提前 PASS；下一次审核遵守该路径的换人/计数规则，不套用批次内“原 reviewer”规则。额度不足或不满足 E2 定向复查条件即按既有决策/用户路径停报，不新开 batch、重置计数或绕过未闭合项。补证结束由该路径 reviewer 的独立结论及 signal 恢复路由，不能用 executor DONE 代替。
- **逐项判定**：完整执行约定测试后，当前失败须属于有效允许集合，且同名失败阶段/原因无实质变化；本卡必需通过项全部通过。核对收集范围及跳过/排除原因，不能用漏收集、删测、skip、弱化断言制造子集。已按合同修复转绿的项由 executor 登记、reviewer 核验后移出允许集合，再失败不得沿用旧豁免。不得强求允许项继续失败来凑齐数量。
- **停止条件**：基线无法复现、环境不可比、测试中断、证据缺失或集合外失败，执行者写本角色 BLOCKED signal，由编排按既有规则路由；不自动补入基线、不顺手修范围外问题。审核未通过不得放行，executor 的 DONE 只表示送审就绪；最终路由仍依据 reviewer 自写的独立结论和 durable signal。

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

`reviewer gpt-6.1-sol-high` 按模型 `gpt-6.1-sol` 与推理档 `high` 分开填写，不把后缀当模型 ID。`batch-reviewer` 默认参考 `roles.toml` 的 `[executor]` 模型、推理档和启动参数，其只读约束由派单 prompt 承担；只读约束由派单承担。相应启动模板见随 skill 安装的 `roles.toml`：`codex -m <模型> -c model_reasoning_effort=<推理档> --dangerously-bypass-approvals-and-sandbox`。未列出的角色保持原有默认或用户指定；本表是新建分配的默认提案，不覆盖在途卡的明确确认，不替代下方启动确认闸。single-task 确认后的分配仍写入 `execution_strategy.md`，不创建计划级模型 config。

- orchestrator 必须先向用户展示全部拟启动角色/实例的模型与推理档提案表，并明确询问确认；推荐默认仅是提案，不写死模型。用户可逐角色修改；**未获明确确认不得启动任何 agent**。唯一例外：卡级总表「自动接续」栏由用户写定的分配（见该节），视为对应角色的明确确认，其余角色仍照本条询问。
- 确认后由 orchestrator 机械地把确认来源、角色/实例、模型、推理档写入 `execution_strategy.md`；未启动的 tab/pane 标 pending，启动后补齐实际 environment/space/tab/pane 与观察来源并逐项比对。默认由 orchestrator 维护 `execution_strategy.md`，watcher 与其它角色只读；启用 document 时按下文首次建卡/代笔合同登记，由 orchestrator 核对分配事实。授权与模型确认事实保留在此，业务决定只按下文「决定落点」引用 findings。
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
- **findings 写者**：orchestrator 只追加已有裁决的来源、摘要、D 项状态、遗留去处和知会，不自行生成业务结论或基线归因；executor 按派单追加发现与证据，基线归因仍遵守上节专属写者及审核闭合流程。同文件由编排安排错开写入，每次派单注明精确章节与唯一写者；复核期间冻结相关候选内容，不并写或覆盖他人记录。仅启用 document 时可按原责任方确认代笔，不强制启用。
- **执行策略内容**：`execution_strategy.md` 只记编排事实：授权与停止线、角色/模型/实例、总表关联与维护人、派单与路由、批次流转与 clear 闸、提交/checkpoint SHA；业务决定处只放指向 findings 对应条目的指针，不放决定正文。模型确认事实不因此迁出，记录模型来源不等于扩大授权。
- **人验与恢复**：主会话人验后的用户选择及知会仍落 findings，并指回真实用户来源；decider 摘要不覆盖独立 decision，开工授权不冒充人验。缺来源或摘要与原件冲突时保留待核状态并回原责任方澄清，受影响动作不凭摘要放行；恢复按下文四类权威回查。
- watcher 对 repo/workspace **完全只读**：不写 signal/progress/execution_strategy/轮询日志/通知日志或任何文档；不路由、不分派、不启动 agent。

### 文档 agent（single-task 可选分工）

- **默认不启用**：不要求创建独立文档 agent、终端或标签页。文档由原责任方按既有写者规则直接编写；未启用 document 时，不登记 document 实例、不走代笔确认链，也不等待 document 的 SYNCED 信号。缺少 document 配置或信号不构成阻塞。
- **仅按用户明确要求试验**：用户明确指定本卡试验文档分工后，才适用以下代笔合同；在本卡既有任务/执行策略中登记 document 实例、模型档、获授权文件和内容责任方。默认建议低成本档，实际模型沿用 model-allocation gate；已有明确分配直接登记。未启用的卡沿用默认写者，不强制迁移在途卡。
- **范围**：建卡、设计/计划、进度、问题、复核/决策正式报告、使用说明、as-built、收口与总表均可在授权路径内委托。文档本身是产品交付物时，用户可指定由执行者编写，document 只记录过程；例如“Codex 改 skill，document 写 dev-harness 过程”不等于已验证所有文档类别。共享设计/计划/总表由登记维护方委托，不允许多卡并写。
- **责任**：执行者提供方案、实际结果和测试输出；reviewer/decider 提供最小结构化问题定位、级别、结论、证据与适用版本。document 直接读指定 diff、原始结果和目标文档，不要求其它角色先写正式报告。原始日志、工具产物与 durable signals 仍由生产者生成，document 不修改来源、不施工/测试、不代验收、不派活、不自行 commit/push/merge。
- **首次建卡**：工作区不存在时，主会话先在派单中给出 Issue/任务来源、已确认模型、精确创建路径、分工和验收输入，再派 document 在 plan 阶段创建任务文档及 execution_strategy。主会话核对登记后再启动依赖该配置的角色；不豁免模型确认或开工授权，不另建账本。
- **派单**：document 是角色，不是新 phase。沿用文档所属的现有 phase：建卡 plan、施工 batch、审核 plan-review/batch-review/workflow-final/e2-code-review、决策 decision、收口 human-acceptance；不使用 watcher phase，不改九值闭集或 batch 枚举。每次写明请求标识、原阶段/路径、候选版本或文件摘要、结论/证据、精确可写文件和待核责任方。document 的 path=document-<请求标识>，成功 verdict=SYNCED，仅表示已同步；缺证/冲突/过期写 BLOCKED 和 reason。信号文件用独立请求名，如 DONE.<phase>.document-<请求标识>.md；重试另取请求标识，不覆盖历史。SYNCED/READY 不能替代执行、复核或人验 PASS。
- **复核代笔**：reviewer 独立检查候选并生成原始结果，自写 verdict=READY_FOR_DOCUMENT 的阶段 signal，编排仅据此派文档。document 写报告并发 SYNCED 后，同一 reviewer 核对结论、级别、遗漏、证据和适用版本，再另写该路径确认 signal（不同文件名，原 signal 保留）。仅 reviewer 确认可用于原路径放行；原始 FAIL/REVISE 不得转成 PASS。代笔错误回 document，不重跑施工或重置计数；实质发现改变仍走原路径整改/轮次。文字来源确认不是新增复核轮，也不替代后续 fresh reviewer 独立审候选与原始证据。
- **其它记录**：机械进度按原始结果回填；方案、决定、模型配置与验收状态由原责任方确认再供后续消费。人验只引用用户真实判断，human-acceptance 不授予代签权；决定与知会写入 findings，执行策略只放对应指针，progress 不放决定。编排核身份、路径、版本和确认引用，不替 reviewer 判断内容。确认记录指向具体章节/结论与版本；无关章节追加不使旧确认失效，修改已确认内容则重新核对。
- **顺序与恢复**：明确委托的人工文档由 document 顺序写，原责任方不再同时写入这些文件；未委托文件保留原写者。可按需复用同一文档会话，写完本次 signal 即停，下次由编排派单，不常驻轮询。验证/复核期间冻结相关候选文件；并发修改、来源漂移、缺证或中断时保留事实及待同步项，不猜、不覆盖他人改动。恢复核原始来源、请求与当前文件，避免重复追加；必要记录未同步不宣称交棒、不清理现场。失联保留待同步，换实例沿用确认规则，不静默恢复多写者。
- **效果**：由实际执行侧评估准确性、遗漏、及时性/可接续性、交接纠错负担及可得耗时用量，document 只转录。费用未知写未知，无可比基线不声称省钱，不为评估新增台账。这些是可演练、可审计的协议约束，现有工具不提供沙箱隔离或自动阻断保证。
- **优先级**：仅覆盖 single-task 中明确委托文件的默认 sole writer、取证段中的人工落笔要求及总表代笔要求；决定权、取证、RELAY_RECEIPT、独立复核、授权和 watcher 零写入不变。四类恢复依据保留：原角色 signals、经责任方确认的报告及原始来源、经编排核对的执行策略、选中环境实态；不能只凭文档摘要恢复。

### watcher 节拍与安全 Enter

#### watcher 通用启动与监控步骤

**所有 agent 共用同一 watcher 合同**。监控主体是 `space_watch.py` 常驻程序，默认放在 Herdr 独立普通终端；不要求模型不断产生回合。可选 watcher agent 的模型/实例仍须确认，其空闲、结束回复或暂停不应终止独立监控终端。兼容旧 agent 内的持久子进程入口，但新的启动优先采用独立普通终端；两种入口不得同时监控同一 space。

参数映射：真实 `workspace_id` → `--workspace`，接收方 → `--notify`，普通监控pane或兼容agent身份 → `--self`；具体CLI命令只在环境协议维护。不按名字前缀或派单名单筛选，watcher不再自己目测比对agent状态。

1. **准备与身份**：编排核环境配置、真实 `workspace_id`、接收方 `notify` 和普通监控终端 `self`，登记在 execution_strategy。普通程序没有模型，无需为它另启模型实例；可选 agent 仍走 model-allocation gate。独立终端按环境协议创建，固定脚本运行在该终端的真实 shell 内，保留继承的 HERDR 上下文，不导出伪造身份。
2. **启动与接管**：执行 RECEIPT/环境/身份 preflight，按环境协议启动固定程序；取得真实子进程句柄/PID与该 pane 的对应关系，确认进程存活和 `SPACE_WATCH_STARTED` 后才称确认接管。同一服务端/space 用内存 socket 防止重复实例，无锁文件；冲突停止新实例，不杀旧进程。启动失败应由主编排直接处理结果等待，不能把外层包装工具 running 当脚本存活。
3. **固定观察**：每 120 秒动态发现本 space 其它 agent，排除 watcher 自身和主编排，不按 kind、名字前缀或派单名单过滤。比较 agent_status/state_change_seq及新增/离开/pane替换，无变化静默；快照仅内存。临时读取失败保留观察基线，输出一次降级原因后下一节拍继续只读观察，恢复只报告一次；RELAY_RECEIPT、环境、身份错误等硬闸仍停止。
4. **通知独立于观察**：向已核接收方的精确 pane 单次提交；CLI agent_prompted 仅证明提交，不要求主编排出现新的 working/seq，不冒称消费或完成。已知审批/unknown UI时不提交，保留事件并在后续节拍合并观察；尝试后的失败/超时/未知保留 UNCONFIRMED，继续观察且不盲重发该事件。正常提交后只等待真实报告/signal；主编排状态变化不触发通知回声。
5. **退出和兜底**：退出只一次通知，按通知事实保留未知；不自动重拉 agent、不自动重启未知状态的脚本。主编排从自己已派出的精确结果文件，用 `task_wait.py` 做有接收者的有界前台等待；不结束回合后无人接收地空等。每次等待最多60秒，PENDING表示本批结果尚未出现，不是任务失败；继续有界等待或明确报告已有停止条件。连续PENDING时只读核已派worker的身份/状态与精确工件；明确失败、审批阻塞或退出无signal按原合同报告阻塞，不无限空等、不自动重投。READY只表示结果可读，编排核原角色 durable signal、完整报告、适用独立复核与实际状态后，才按原授权路由。监控暂停/失联不是已授权交接的额外放行闸，也不放宽审批/人验/开工闸。

watcher 对 repo/workspace **完全只读**：不写 signal/progress/execution_strategy/轮询日志/通知日志或任何文档，不路由、不分派、不启动 agent。stdout/stderr只留独立终端或宿主临时输出，不保存终端正文；旧子进程入口由宿主工具取真实句柄、短等待巡检，不再自己目测比对状态。watcher 常驻，不逐批 clear。主编排的 task_wait 只读精确任务结果，不代跑 worker测试，不代判结果。

**安全 Enter**：只有①本次派单仍在输入框（含 queued 未提交指令）、②`state_change_seq` 未推进、③不是审批/确认 UI，三条件同时成立才由获授权 watcher agent 发一次并复验；一次失败交编排按原授权路由，禁止连按。程序永不发键、不读取/保存终端正文。

#### watcher 专用派单模板（所有 kind 通用，兼容可选 agent）

```text
[relay-lite:single-task] worker · phase=watcher · agent=watcher#<实例> · batch=na · round=1 · workspace=<任务工作区>
environment=<已校验环境>；space_id=<真实ID>；notify=<编排身份>；self=<watcher身份>。
读 AGENTS、核心 watcher 通用合同、环境协议与自己的宿主 adapter；RELAY_RECEIPT preflight。
监控主体采用独立普通终端中的space_watch.py；不要为保持监控反复要求模型续跑。
已有程序时只核精确PID/终端与启动结果，不重复启动；旧子进程入口须取得真实持久句柄。
程序每120秒动态观察本space其它agent，排除self/编排，不按kind或名单过滤。
变化才通知，无变化静默；提交不冒称消费；未知不盲重发，观察继续。
不写仓库或工作区文件，不存终端正文，不路由、不派活、不启动agent，不自动重启脚本。
```

### 恢复依据

恢复权威只有四类：原角色自写的 durable signals、独立 review/decision 工件及其原始来源、由 orchestrator 核对的 `execution_strategy.md`、选中环境实态。`progress.md` 只是施工证据索引、watcher 通知只是即时提示，二者都不是运行真相；恢复/重启时从四类权威重建，不依赖终端存活状态。 `findings.md` 是决定与遗留的检索入口，沿其来源引用回查上述独立工件及用户原始裁决，不新增第五类运行权威；摘要缺源、冲突或仍待用户决定时，不推进依赖该决定的动作。

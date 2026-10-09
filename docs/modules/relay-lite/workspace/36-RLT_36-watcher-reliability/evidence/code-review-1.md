# RLT_36 · normal 完整独立代码复核 · attempt 1

结论：**approved**。本次完整候选复核未发现需要登记的 P0/P1/P2/P3，findings=[]。这只闭合本卡 `code_review`，不替代必要 CI、实际合入复验、verify 或业务卡验收。

复核实例 `/root/rlt36_code_review`，未参与实施，fresh context；实施实例 `codex-root-rlt36-20261009`。模型分配依据精确派单为 `gpt-6.1-sol/high`，dispatch_ref=E-009；类型 normal，attempt=1，kind=full。检查时 RELAY_RECEIPT 不存在。本实例未运行 Herdr 控制、通知或演练，没有派活、代验收、修改产品或其它角色工件；仅写本报告与同名 JSON。离线验证的安装和测试临时目录已清理，没有安装用户副本。

## 候选绑定与复核输入

- baseline_sha=`dfbe56371b569ff768e7bcd82eeb8d204d55dfea`
- target_sha=`fa9c21fa2dcce7f55760ef19f93ac28a3188e34b`
- diff_sha256=`9d351c5118e97824b9530b283d0186cb647a0f572078b12bec87c22aab9d149a`

实际 HEAD 与 target 一致。按共享 collector `rebuildDiffTriple` 的 `git diff --binary --full-index --no-ext-diff --no-textconv --no-color --no-renames <baseline> <target> --` 重建完整 diff，摘要与派单、review-freeze.json 一致。默认 Git diff 的其它摘要来自参数差异，不作为漂移。工作树已有的 execution_strategy/progress/review 冻结登记及新增证据由原写者维护，没有纳入本实例施工或改写目标身份。

已读根 AGENTS、skill/SKILL.md、两 adapter、environment-herdr，源卡 P4-watcher可靠性、设计审核记录，以及本工作区 brief/task_plan/findings/progress/review/execution_strategy、方案初审及定向复审、lesson_candidates 和指定 evidence。检查真实 baseline→target 的全部 55 个变更文件，覆盖脚本、安装器、测试、协议、说明、任务工件及隔离 live 原报告和 signal。

## 代码与需求核查

`space_watch.py` 的普通监控 pane 身份核验仅使用继承 HERDR_PANE_ID 与实际 pane/workspace；兼容旧 watcher agent 入口。常驻进程独立于模型回合，内存 socket 拒绝重复实例且释放后可复用，不生成锁文件。动态发现仍覆盖本 space 各 agent，排除 self 和接收编排实际 pane，不按角色、kind 或名称前缀过滤。

通知在目标 blocked/unknown 或提交前不可用时延后并保留观察基线；真正尝试后失败/超时/未知保存 UNCONFIRMED，同时推进已观察基线，下一轮不自动重发旧 delta。正常 `agent_prompted` 只记提交，不要求 working/seq 推进，也不推断消费。临时只读错误保留基线并恢复观察，RELAY_RECEIPT/环境/身份硬闸仍停止；退出提示只尝试一次。代码不写 repo/workspace，不调用发键入口，不保存终端正文。

`task_wait.py` 只读精确结果路径，以七个派单字段绑定本批任务，拒绝越界、symlink、重复/冲突结果及 receipt。单次等待限制 0..60 秒，PENDING/退出3保留结果尚未出现的语义；匹配 BLOCKED 同样返回 READY 供 owner 检查，READY/退出0明确 `requires_owner_review`，不作为 PASS。核心、两个 adapter 和环境协议同步规定 owner 持续有界等待、连续 PENDING 核实际 worker/工件/原停止线，以及 READY 后读原报告、signal、适用复核和真实停止状态。监控失联没有放宽审批、人验或开工闸。

安装器闭集、工具源路径与 source_dirty 登记均纳入 task_wait.py。实际 diff 在源卡允许路径内；历史失败、初次 wrapper 重复参数错误及初次 monitor 源码对齐过程保留，没有用新成功覆盖旧失败。

## 独立验证及证据闭合

1. 本实例运行 `PYTHONDONTWRITEBYTECODE=1 python3 -B -m unittest discover -s tests -v`，76 tests，3.878 秒，exit0/OK。包含 busy 精确 pane 提交、审批延后、未知不重发、新变化继续、临时观察恢复、身份/receipt 硬闸、singleton、退出提示、精确结果/冲突/有界等待等行为断言。
2. 临时 home 下通过 install_all 安装三侧闭集，逐项核 manifest/hash/source_head；三侧安装后的原生 task_wait 实际读取本卡 live 精确 signal，均返回 exit0、READY_FOR_REVIEW、requires_owner_review 及原 signal hash `2b498bd81b6ff07192215e2d2d7c98b3776a267b200adea397440af7f447a2a3`。没有以 `--help` 成功替代等待行为。
3. 有效单测 E-005 的变异点为 task_wait 精确字段比较被 `if False` 放过。以候选原始字节在内存重建，变异 hash=`43d3c84dc8ea423be73f9e282aabc19f78f30e318f354770e7c50d4ed4951e47`，与登记一致；mutation-red.log 的三个失败均是错 task/错轮/错 agent 被误返回 READY 的业务断言，不是 setup/import 错误。恢复 hash 与候选 `5526592c267158079f3d549df7e409aa148c3a28f11946bba4dd1ccf894797a0` 一致，restored-green 与本次独立运行均为76项绿。未改产品重做变异。
4. live/final.json 的两脚本源码 hash、worker/orch 原报告及两份 durable signal hash 均与磁盘字节一致。S-A 的同一 PID740665 实际存活169秒，watcher模型已done，owner仍working、seq3055未推进，同时存在一条 SPACE_WATCH_SUBMITTED；这是独立监控存活及 busy 提交证据，未推定消费。
5. S-B 先记录 PID 消失且 worker 未派单，之后 worker 首次派单；owner 原报告记录4次真实 wait、3次 exit3/PENDING 后 native READY JSON，实读 signal/report/hash及 worker done 身份，再写预授权 HANDOFF_CONFIRMED 工件和最终 signal。final.json 的 native_ready_json_count=0 是外部终端 token 计数，原 owner 报告保留真实 READY 结果，不能把该外部计数解释为未发生 READY。没有再次 prompt owner，交接仅是隔离演练授权，不是业务验收或下一卡开工。

RL36-M1～M5 的实现与现有隔离运行证据闭合原需求。M6 的安装闭集、行为回归、有效单测和本次 fresh code_review 在此得到核查；必要双平台 CI、实际合入复验与 verify 仍由后续交付节点完成，本报告不提前判整卡完成，也不声称本实例执行了 Herdr live 演练。Linux 隔离实态不推断 Windows Herdr 常驻实态。

## findings

无，`[]`。本报告和 JSON 完成后立即停止。

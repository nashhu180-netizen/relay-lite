<!-- dh:v1 -->
# task_plan — RLT_36

1. 建 Issue并读回，主树落户，独立 wt/RLT_36 worktree；冻结授权/分类/允许路径与原始失败。当前主干 dfbe56371b569ff768e7bcd82eeb8d204d55dfea。
2. 先跑原58项基线；新增真实行为负例钉住暂停/通知异常不阻断。space_watch 在普通 Herdr pane 常驻，核 self pane 与 workspace；通知单次提交、审批延后、未知不盲重发；读失败保留原基线；不写repo/workspace。
3. task_wait.py 精确只读结果等待，校验本任务/phase/agent/batch/path/round等预期；有界 READY/PENDING/BLOCKED输出不代验收。按允许路径同步安装包/核心/adapter/环境协议/README。
4. 行为回归、临时home三端安装、有效变异RED→精确恢复GREEN；现有业务space只读保护。
5. 独立新测试space：已确认luna三角色；普通monitor独立pane。暂停/结束watcher模型回合，worker交付精确signal，主编排走task_wait核报告并完成隔离交接。只保存白名单事实/来源/hash，不保存凭据/终端全文。
6. 提交完整候选、共享collector冻结；fresh独立reviewer gpt-6.1-sol/high，只读产品与证据、只写自己的review及原报告。normal仅一次full；真实open P0/P1才同人唯一targeted。
7. 必要CI、实现PR服务端合入，实际merge SHA隔离复验、verify(relay-lite)、有限收口PR及本卡Issue关闭/树清理。

## 环境预检
Python3与git/gh/dh/herdr可用；HERDR_ENV=1，当前kpi-agg/w6X:p1；本仓master与origin/master相同，主树无改动；CI Ubuntu/Windows Python3.12。隔离演练模型已明确确认。未知CLI语法先读help，受保护分支/必要检查先核平台事实。禁止触碰其它worktree。

## 第5步演练细化（PR36-01/02/03，原验收不变）

S-A：独立普通monitor w6Y:p4在三模型启动后建基线。watcher模型执行一次只读核PID后结束回合，实际idle/done；保持同一monitor PID跨至少120秒。编排先进入精确signal的50秒有界等待（worker尚未派单），使其实际working。以watcher模型状态序号变化作为本space真实worker变化触发通知；monitor自身白名单提交诊断和编排实际working身份事实证明单次提交，不用提交推定消费。
S-B：记录S-A提交后，仅在本卡隔离普通monitor终端发送ctrl+c，核原PID消失且未重启，watcher模型保持idle。编排此前已真实至少一次PENDING并继续下一等待；此后才投递worker初次派单，worker写本批报告和精确signal。不得再次prompt编排、用户唤醒或重投任务；主编排通过待决的task_wait返回READY，读取报告/signal/hash/任务字段、worker实际停止事实，再写预先授权orch-report及handoff signal。若编排提前final/需外部唤醒/接受错轮或仅idle，S-B FAIL。
演练总预算：编排最多8次50秒wait（400秒），worker最多1次初始派单；未知prompt不重投。预算用尽、worker明确错误/审批阻塞或退出无signal，只核状态/精确工件并报告阻塞，不能无限轮询或因为watcher暂停停整卡。
证据：启动失败原证、实际角色argv/cwd/env白名单、startup marker与PID/父链、至少120秒同PID存活、通知目标working与单次提交/事件hash、停止monitor的准确时刻/PID状态、编排原生PENDING→继续→READY和完整报告/最后signal/hash/worker停止状态、实际交接产物。输出只保留白名单结构字段或本卡非secret结果；终端全文不保存。追加live/runtime及final JSON索引，原失败不覆盖。

## 第2～4步验收与oracle对应（PR36-02）
| 验收 | 行为oracle/证据 |
|---|---|
| M1 | shell_monitor_survives_watcher_agent_disappearance；live同PID跨120秒/模型idle。 |
| M2 | busy_target_submission_needs_no_state_transition；unconfirmed_notification_continues_without_resending；deferred_before_submission_is_coalesced_then_sent_once；native prompt参数精确pane、无wait/keys。 |
| M3 | transient_read_failure_recovers_without_consuming_delta；duplicate_runtime_is_rejected_and_release_is_reusable；runtime_hard_guard_is_not_retried；environment_and_receipt_before_any_command；身份错配/list-get竞争负例；受控退出通知单次且未知不重发。 |
| M4 | task_wait七字段错任务/旧轮/错agent/partial不READY；冲突DONE/BLOCKED、越界/symlink/receipt拒绝；真实CLI exit3→exit0，READY仍需owner核验。 |
| M5 | S-A/S-B明确时序、输入失败与400秒预算，live结构化事实及原signal/报告/hash/停止状态。 |
| M6 | 完整测试日志；task_wait同一命令有效变异RED→原hash恢复GREEN；临时home三端manifest/入口实际复跑；fresh最终代码复核、Linux/Windows CI、合入复验/verify。 |
Windows CI仅证明Python包与行为，不冒称Windows Herdr常驻实态。所有证据回填review对应行；原始失败不覆盖。

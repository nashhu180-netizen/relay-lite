<!-- dh:v1 -->
# execution_strategy — RLT_36

本卡标准档 normal；implementer_session_id=codex-root-rlt36-20261009；本会话实施。
授权来源：用户“确认开始修复，建个issue”；模型确认来源本轮异步答复“确认这组分配”。Issue15已创建并读回，状态open。
目标 origin wt/RLT_36 → master，完整交付；隔离本地Herdr真实演练；不操作现有三业务space、不安装用户副本、不部署/下一卡。
reviewer=gpt-6.1-sol/high，实例待完整候选后fresh启动；隔离编排/worker/watcher=gpt-6-luna/medium，space/tab/pane均pending。普通监控进程无模型。
环境：Herdr，当前真实kpi-agg/w6X:p1；测试拓扑另建本卡独立space。现役安装版CLI为操作权威，不沿用历史ID。
派单与路由、真实Git/SHA/模型/清理仅在本文件登记；业务结论与问题在findings，原始证据在evidence。

隔离worktree=.dh-worktrees/RLT_36，branch=wt/RLT_36，baseline=dfbe56371b569ff768e7bcd82eeb8d204d55dfea；仅本卡治理先主树创建后精确迁入，主树恢复干净。
方案独立reviewer_session_id=/root/rlt36_plan_review，gpt-6.1-sol/high，fresh上下文，只写review.plan.md；该实例不承担最终fresh code_review。
新隔离Herdr space实际创建为w6Y（RLT_36-test），root pane=w6Y:p1；其它space未改。

隔离首次三角色startup失败：wrapper重复--no-daemon，三者agent_not_found且终端报精确参数错误，未启动模型回合；保留startup-failure.json。后续使用已继承wrapper默认，只透传模型/推理档，不改任何用户配置；不是未知投递重试。

隔离三模型修正后实际启动：rlt36-orch=w6Y:p1、rlt36-worker=w6Y:p2、rlt36-watcher=w6Y:p3；model=gpt-6-luna、effort=medium；实际argv含--yolo/--no-daemon/--no-alt-screen且cwd本卡树，见live/runtime-models.json。普通monitor=w6Y:p4，PID740665，源hash在monitor-start.json；初次PID737311在发模型派单前受控停止以对齐源码，已核消失，原证保留。
方案原reviewer定向追加PASS，仅关闭方案发现，不是最终code_review。S-A已派编排与watcher；worker尚未派单；现场实际watcher模型done、编排working且task_wait真实helper进程运行。

隔离S-A/S-B完成：monitor PID740665受控停止且消失；三角色均done。编排只初次派单一次、worker初次派单一次、watcher初次派单一次；未再prompt编排，3PENDING→READY原报告/最后signal/实态齐备。原证索引E-007/008。测试space只在证据归档与最终复核后清理，不动其它space。

<!-- dh:v1 -->
# execution_strategy — RLT_37

本会话直接实施，非业务卡relay orchestrator派单；遵循本仓AGENTS的dev-harness维护路径，不启动Herdr角色。独立fresh subagent由本仓AGENTS明确允许，继承当前模型，不选新的模型/provider。只写本复核报告，派出前后核Git基线；非机器只读。
implementer_session_id=codex-root-rlt37-20261009。
目标origin wt/RLT_37→master，基线183d6c2724924276e189069fcbd62bbd0ae6e59b。总表：无（独立维护卡）。
授权见brief#本卡开工授权；独立实例/候选/PR在实际发生后登记。

首次PR创建早于push进程结束而明确失败（Head ref must be a branch）；等待原push成功后读回无PR再创建，不重复push。

任务树=.dh-worktrees/RLT_37，branch=wt/RLT_37；Draft PR19已创建。新增tests/test_install_skill.py只同步现有包闭集断言，属于Issue18分发范围。

方案检查/root/rlt37_plan_check仅写原plan-check.md；主会话持续维护自身文件，未声称机器沙盒隔离。最终code_review将冻结产品并核前后Git状态。远端保护只读查询404（Branch not protected）、rulesets=[]；仍要求双平台CI与本卡独立复核，不绕检查。CI仅Python单测，无deploy。

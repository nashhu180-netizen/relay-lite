<!-- dh:v1 -->
# execution_strategy — RLT_34

授权：brief.md#本卡开工授权；用户“确认开工”。标准档 normal。
角色：主会话 /root 负责实施/测试/集成，implementer_session_id=codex-root-rlt34-20261007；独立复核用 fresh-context subagent（继承主会话模型/推理档，fork_turns=none），只写指定 review 报告。AGENTS.md 明确允许此种独立复核；不启用 relay single-task 终端编排，无额外 Herdr/model-allocation 启动。
总表：无（独立单卡）。
分支：wt/RLT_34；worktree：/home/nash/work/relay-lite/.dh-worktrees/RLT_34；目标：origin/master。
GitHub Issue：#7。原现场另有 AW_07-table-resume worktree，本卡不清理。
停止线：沿 brief/task_plan，不派下一卡，不部署、不安装。

Draft PR：[GitHub #8](https://github.com/nashhu180-netizen/relay-lite/pull/8)，开工提交 126c82e。

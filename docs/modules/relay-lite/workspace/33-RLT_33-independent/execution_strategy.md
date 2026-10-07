# 执行策略

授权：本卡用户消息；单会话实施，独立 fresh-context 复核。主干 master；本卡不运行 relay-lite 多角色流程，故不伪造 Herdr 模型确认/实例。卡级总表：无（独立迁移卡）。

Draft PR：新仓 #2 / 源仓 #157。源冻结2246b16；方案初审及定向结论见review.plan.md，主会话采纳两P1整改，不产生新方向决定。

Review Batch RB-RLT33-2：code_review2、requirement_review、consistency_lessons_review 并发启动；后者独立承担一致性/教训两路，分别报告，不冒充两个身份。五条适用路径均已PASS；code1/2不同fresh实例，无openP0/P1。Mode=inline_registration，本卡未启用document、未运行Herdr流水。
同卡上传辅助branch upload/RLT_33-issue-1只承载候选对象，分批树最终等于db18185；正式分支保持原候选历史、无force，最终收口后仅删除该辅助branch。

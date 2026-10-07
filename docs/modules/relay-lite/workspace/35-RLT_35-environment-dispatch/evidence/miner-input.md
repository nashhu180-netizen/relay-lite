=== dh mine: relay-lite / 35-RLT_35-environment-dispatch ===
（只读备料·不抽教训——抽取归 subagent。把下面整份简报交给一个 fresh-context subagent）

① 工件清单（让 subagent 读这些，按筛子抽『别再踩第二次』的教训）：
  ✓ /home/nash/work/relay-lite/.dh-worktrees/RLT_35/docs/modules/relay-lite/workspace/35-RLT_35-environment-dispatch/review.md　— 两轮独立复核的 P0/P1 发现（最肥食材）
  ✓ /home/nash/work/relay-lite/.dh-worktrees/RLT_35/docs/modules/relay-lite/workspace/35-RLT_35-environment-dispatch/findings.md　— 维护/复核问题清单的根因与级别
  ✓ /home/nash/work/relay-lite/.dh-worktrees/RLT_35/docs/modules/relay-lite/workspace/35-RLT_35-environment-dispatch/progress.md　— 返工/换方向的过程记录（『原以为…其实…』、>2 轮返工）

② 去重对照（动手前先扫，撞正册标『疑似 L-00X』、撞候选区跳过）：
  正册 教训库.md（0 条在册）：
    （空 / 文件不存在——无在册教训，无需对照正册）
  候选区 教训库-候选.md（3 条候选；3 条待裁决）：
    · 候选-001 · 拆分产品前先枚举仓外测试入口　｜触发：产品目录迁出到独立仓时，源仓仍需保留 Runner 回归与退役边界。
    · 候选-002 · 变更性取证在冻结副本运行　｜触发：迁移/删除会改变被测文件，且需要保留基线、变异或回归取证。
    · 候选-003 · 祖先提交审计须在 CI 明示完整历史前提　｜触发：仓库契约测试用固定祖先提交验证一次性迁入内容。

③ 候选格式（抽出的每条按此写，字段对齐正册、裁决时直接搬）：
    ### 候选-N · <一句话标题>
    触发场景：<…> · 建议分类：<领域知识/编码陷阱/行为流程> · 来源：<review 第2轮 P1 / 病历-yy 根因>
    疑似重复：<无 / L-00X>
    - 现象：<一句>
    - 反思：<一句根因>
    - 建议后续动作：<下次怎么做>
    状态：待裁决

④ append 落点：/home/nash/work/relay-lite/.dh-worktrees/RLT_35/docs/modules/relay-lite/knowledge/教训库-候选.md
    抽完在 workspace/35-RLT_35-environment-dispatch/progress.md 记一行指针：『本次 miner 产出 N 条候选 → 候选区』（gate 软报告靠它判跑没跑）。

⑤ 派单模板（spawn subagent 时的一句话指令）：
    读 35-RLT_35-environment-dispatch 工作区的 review.md / findings.md / progress.md，按筛子抽『别再踩第二次』的教训候选：
    review 两轮 P0/P1（根因类、非一次性笔误）/ findings·病历根因 / progress 返工信号；
    排除一次性手误·环境抖动·流水账·已在册（先扫上面②两张去重）。
    每条按③格式写、append 到 教训库-候选.md 状态『待裁决』。判据：下个类似任务会不会再撞？会→抽，纯偶然→扔。

（只读派生、不落盘；候选 ≠ 入册，正册只进人裁决过的——miner 只能往候选区堆）

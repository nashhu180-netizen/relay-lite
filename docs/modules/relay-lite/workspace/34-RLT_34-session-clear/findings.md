<!-- dh:v1 -->
# findings — RLT_34

## 决定与发现
用户确认标准档开工；需求及范围见 brief。无 open P0/P1，无人判项、未验证的承诺结果或风险接受。
Chrome CDP 前置检查连接超时，不修改浏览器设置；GitHub 原生 gh 已成功查询仓库/分支并建 Issue，不以浏览器检查结果冒充 CDP 可用。
仅本卡主会话顺序维护本文件，复核文件由独立复核者写。

miner 初始派单允许 lesson_candidates.md，冻结后证据增量检查发现其不属于 collector 可接受的后续路径；主会话及时收窄为 evidence/miner.md。miner 已按初始派单写入的内容保留 evidence/miner-initial-path.md，lesson_candidates.md 精确恢复被审候选原字节。不改历史结果、不重派代码复核。

机械验收元数据 R21 首次核对失败：M1～M4 结果已独立核准但覆盖态仍为创建期“部分”，M5 未完成却沿用“本地回归通过”字样。按已有证据将 M1～M4 记等价覆盖，M5 明确待集成/verify；保留 check-premerge.log，不把尚未发生的交付改写为通过。

R29 机械回填格式：规划 fingerprint 忽略状态/时间/verify列，但不忽略 release_mode 列。保留该列原值，release_mode=full 登记在该卡“状态：”机械事实行；不新增规划事件。首次及第二次失败保存 closeout-check-first.log、closeout-check-second.log，最终结果另存，不覆盖失败。

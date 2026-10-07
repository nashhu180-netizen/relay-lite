# RLT_35 开工 / 施工计划独立复核（侦测型降级；非机器只读）

本复核只读取 RLT_35 的设计、DevPlan、工作区计划和现有仓库事实；未运行测试、未控制 Herdr、未核验实时环境。用户已明确“确认”标准档 normal 开工，并纠正“不是 codex 的 watcher 针对所有agent都一样”。

## 方案问题

- **P1｜施工计划的回归入口还没有写成可直接照做的命令矩阵。** `task_plan.md` 第 4 步只写“Test 协议契约与全回归”，而本卡新增 `tests/test_environment_config.py`，并同时影响安装器、协议文本和既有 watcher 合同。仓库现有事实是 `tools/install_skill.py` 的 `SKILL_FILES` 目前只含 `space_watch.py` 等六个安装项，且 `tests/test_install_skill.py` 对该封闭集合做精确断言；安装闭包、配置工具安装位置和三端解析必须由同一组明确命令覆盖。影响是实施者虽能判断测试类别，却无法只凭计划复现最小回归集和变异后的 GREEN。建议在实施开始前把“新配置工具单测、安装器隔离安装、协议契约、既有 `test_space_watch.py`、全量 unittest”的实际命令及各自预期写入 `task_plan.md`，并把 RED 的精确变异点、断言和字节级还原动作同处登记。该项不改变范围或验收，不阻塞已获授权开工。

- **已核承接：完整。** 正式设计的 RL35-M1～M8 已逐条投影进 DevPlan、brief 和 review 验收表；允许路径包括配置、环境协议、两 adapter、安装器、相关测试及本卡工件。依赖 RLT_33/RLT_34 已在 DevPlan 写明且没有把 Orca 或真实 Herdr 操作偷偷纳入。用户原话“目前有且只有herdr”与只注册 herdr 的范围一致。

- **已核公共监控分层：完整。** 施工第 3 步把“通用 watcher 模板适用全部 kind”放在公共合同，并将 Codex cell/session 与 Claude 后台任务差异限定在各 adapter；这符合用户纠正。现有 `tools/space_watch.py` 的 `snapshot()` 每轮按 `workspace_id` 重发现成员并排除 watcher 与 notify pane，也支持该公共范围，不需要改脚本行为。

## 用户理解风险

- “所有 agent 共用 watcher”指监控集合、通知与 fail-closed 语义对全部 kind 相同；它不意味着各宿主用同一种持久进程 API。计划已把该区别留在 adapter，但施工时不能把 Codex 的 `session_id` / `write_stdin` 写回环境通用协议。

- 环境校验器只选择环境和协议路径，不会创建 space、tab 或 agent。离线配置、安装和契约测试不能证明真实 Herdr 操作成功；该限制已在正式设计和任务计划保留。

## 需要用户决定项

- 无。用户的“确认”已授权标准档 normal 本卡开工；环境消费层级、首次/恢复选择规则、Herdr-only 范围和通用 watcher 分层均已在正式设计、DevPlan 与 execution strategy 固定。上述 P1 是可由实施者补全的运行证据入口，不引入产品、范围、验收、权限或生产取舍。

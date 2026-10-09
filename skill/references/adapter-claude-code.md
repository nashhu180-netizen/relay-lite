# adapter-claude-code — relay-lite 单卡接力

默认安装目录：`~/.claude/skills/relay-lite/`。协议核心见 [SKILL.md](../SKILL.md)；单卡只分派获授权角色，不执行旧模式。

## 启动与投递

先读核心的环境、模型和「新批次与新任务的标签页会话清理闸」。运行已安装的 `<SKILL_DIR>/environment_config.py`，非零退出/非 READY 停；恢复带 `--expected <已登记环境>`，读取返回 protocol；当前为 [Herdr](environment-herdr.md)，须加载 `herdr --skill`。原生参数透传交互CLI，不换 headless。

确认清理成功后再投递派单文件指针；清理命令与派单不可合并，失败或未知不派新单、不盲重发。成功判据、例外和保留历史要求完整沿核心，不用 shell clear、idle/done或工具权限代替协议闸。

## 派单与公共规则

先完整读取核心及其按角色路由的必读合同；所有 kind 共用同一协议。派单只使用[共用模板](../templates/dispatch.md)，角色/模型确认、计数、写者、RELAY_RECEIPT 分流及恢复依据沿核心，不在 adapter 另设规则。decider 读[决策指南](decision-guide.md)。

#### watcher 宿主工具调用（Claude Code，旧 agent 子进程兼容入口）

执行[watcher 通用启动与监控步骤](watcher.md)及选中环境协议；所有 agent 的监控规则相同，这里只说明宿主工具。固定脚本路径与真实 space/notify/self 从环境协议/派单取得。

用 Bash 的 `run_in_background=true` 运行固定脚本，读取真实后台 task_id/进程标识；立即用该宿主的任务状态/输出工具短等待核原后台任务存活或退出，再通过环境通知入口确认启动。随后对同一 task_id 短等待巡检；后台句柄缺失或无法证明持续运行即报告 blocked。120秒观察节拍在脚本内；宿主每次等待不超过60秒，不靠模型长阻塞维持循环。

stdout/stderr仅保留宿主临时任务输出，不重定向进仓库/工作区；正常静默，退出一次报信确认；通知未知不重发，观察继续；不自动重启。安全 Enter、RECEIPT、watcher不逐批clear与durable signal路由全部沿核心。

### 主编排有界结果等待

先执行[通用结果等待合同](watcher.md)及环境协议：task_wait.py只读等待精确结果，READY不是PASS，PENDING继续有接收者的有界等待；单次不超过60秒。

等待工具用Bash前台有界命令或run_in_background=true所得真实task_id与任务状态工具读回结果；后台任务没有自动恢复回合能力时使用前台有界等待，PENDING回来继续等待，不把后台句柄当结果。

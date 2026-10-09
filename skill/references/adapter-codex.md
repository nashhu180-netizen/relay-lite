# adapter-codex — relay-lite 单卡接力

默认安装目录：`~/.codex/skills/relay-lite/`。协议核心见 [SKILL.md](../SKILL.md)；单卡只分派获授权角色，不执行旧模式。

## 启动与投递

先读核心的环境、模型和「新批次与新任务的标签页会话清理闸」。运行已安装的 `<SKILL_DIR>/environment_config.py`，非零退出/非 READY 停；恢复带 `--expected <已登记环境>`，读取返回 protocol；当前为 [Herdr](environment-herdr.md)，须加载 `herdr --skill`。原生参数透传交互CLI，不换 headless。

确认清理成功后再投递派单文件指针；清理命令与派单不可合并，失败或未知不派新单、不盲重发。成功判据、例外和保留历史要求完整沿核心，不用 shell clear、idle/done或工具权限代替协议闸。

## 派单与公共规则

先完整读取核心及其按角色路由的必读合同；所有 kind 共用同一协议。派单只使用[共用模板](../templates/dispatch.md)，角色/模型确认、计数、写者、RELAY_RECEIPT 分流及恢复依据沿核心，不在 adapter 另设规则。decider 读[决策指南](decision-guide.md)。

#### watcher 宿主工具调用（Codex，旧 agent 子进程兼容入口）

执行[watcher 通用启动与监控步骤](watcher.md)及选中环境协议；所有 agent 的监控规则相同，这里只说明宿主工具。固定脚本路径与真实 space/notify/self 从环境协议/派单取得。保留 stdout/stderr 在宿主临时输出，不写仓库或工作区。

1. 直接 `exec_command({cmd: <固定脚本完整命令>, yield_time_ms: 1000})`，取得真实返回的 `session_id`（若立刻返回退出码，脚本未常驻，按通用退出规则处理）。
2. 若工具嵌在 `functions.exec`，必须 `await tools.exec_command(...)` 并回传返回对象；只有外层返回 `Script running with cell ID ...` 时才调用 `functions.wait(cell_id=...)` 取得内层结果。外层 cell ID 不是脚本 session_id，不能据它宣布启动成功；未等待的 Promise 可能随 isolate 结束被丢弃。
3. 取得内层 session_id 后，立即 `write_stdin({session_id: <真实ID>, chars: "", yield_time_ms: 1000})` 检查原进程是否仍运行或已经退出，再按环境通知入口向编排确认启动；返回退出码或找不到 session 即处理退出，不从 shell 文本/包装函数推断存活。
4. 随后用同一 `write_stdin` session 短等待巡检，不新开后台 shell 或写轮询日志。工具若没有持久进程能力，报告 blocked；脚本每120秒自行观察，watcher巡检宿主句柄时每次工具等待不超过60秒。进程退出不重启；通知未知保留事件而继续观察、不重发。

不得把 `/clear` 清理 watcher、把脚本通知当 durable PASS、以 `idle/done` 判任务完成。安全 Enter 三条件与 RECEIPT 零写入分流仍沿核心。

### 主编排有界结果等待

先执行[通用结果等待合同](watcher.md)及环境协议：task_wait.py只读等待精确结果，READY不是PASS，PENDING继续有接收者的有界等待；单次不超过60秒。

等待工具也用 `await tools.exec_command(...)` 取得真实session_id；必要时 `write_stdin` 短等待读回该命令结果。工具嵌套的cell ID不是脚本session_id，不用未await的Promise。PENDING回来后仍保持接收者，不发final后等待无人接收的通知。

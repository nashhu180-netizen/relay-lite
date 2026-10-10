# watcher 节拍与安全 Enter

适用入口与公共硬闸见[核心协议](../SKILL.md)。本文件是按需读取的完整合同，不能用入口摘要代替。

#### watcher 通用启动与监控步骤

**所有 agent 共用同一 watcher 合同**。监控主体是 `space_watch.py` 常驻程序，默认放在 Herdr 独立普通终端；不要求模型不断产生回合。可选 watcher agent 的模型/实例仍须确认，其空闲、结束回复或暂停不应终止独立监控终端。兼容旧 agent 内的持久子进程入口，但新的启动优先采用独立普通终端；两种入口不得同时监控同一 space。

参数映射：真实 `workspace_id` → `--workspace`，接收方 → `--notify`，普通监控pane或兼容agent身份 → `--self`；具体CLI命令只在环境协议维护。不按名字前缀或派单名单筛选，watcher不再自己目测比对agent状态。

1. **准备与身份**：编排核环境配置、真实 `workspace_id`、接收方 `notify` 和普通监控终端 `self`，登记在 execution_strategy。普通程序没有模型，无需为它另启模型实例；可选 agent 仍走 model-allocation gate。独立终端按环境协议创建，固定脚本运行在该终端的真实 shell 内，保留继承的 HERDR 上下文，不导出伪造身份。
2. **启动与接管**：执行 RECEIPT/环境/身份 preflight，按环境协议启动固定程序；取得真实子进程句柄/PID与该 pane 的对应关系，确认进程存活和 `SPACE_WATCH_STARTED` 后才称确认接管。同一服务端/space 用内存 socket 防止重复实例，无锁文件；冲突停止新实例，不杀旧进程。启动失败应由主编排直接处理结果等待，不能把外层包装工具 running 当脚本存活。
3. **固定观察**：每 120 秒动态发现本 space 其它 agent，排除 watcher 自身和主编排，不按 kind、名字前缀或派单名单过滤。比较 agent_status/state_change_seq及新增/离开/pane替换，无变化静默；快照仅内存。临时读取失败保留观察基线，输出一次降级原因后下一节拍继续只读观察，恢复只报告一次；RELAY_RECEIPT、环境、身份错误等硬闸仍停止。
4. **通知独立于观察**：向已核接收方的精确 pane 单次提交；CLI agent_prompted 仅证明提交，不要求主编排出现新的 working/seq，不冒称消费或完成。已知审批/unknown UI时不提交，保留事件并在后续节拍合并观察；尝试后的失败/超时/未知保留 UNCONFIRMED，继续观察且不盲重发该事件。正常提交后只等待真实报告/signal；主编排状态变化不触发通知回声。
5. **退出和兜底**：退出只一次通知，按通知事实保留未知；不自动重拉 agent、不自动重启未知状态的脚本。主编排从自己已派出的精确结果文件，用 `task_wait.py` 做有接收者的有界前台等待；不结束回合后无人接收地空等。每次等待最多60秒，PENDING表示本批结果尚未出现，不是任务失败；继续有界等待或明确报告已有停止条件。连续PENDING时只读核已派worker的身份/状态与精确工件；明确失败、审批阻塞或退出无signal按原合同报告，并由主编排按[解阻路由](orchestration.md)组织下一步；不无限空等、不自动重投。READY只表示结果可读，编排核原角色 durable signal、完整报告、适用独立复核与实际状态后，才按原授权路由。监控暂停/失联不是已授权交接的额外放行闸，也不放宽审批/人验/开工闸。

watcher 对 repo/workspace **完全只读**：不写 signal/progress/execution_strategy/轮询日志/通知日志或任何文档，不路由、不分派、不启动 agent。stdout/stderr只留独立终端或宿主临时输出，不保存终端正文；旧子进程入口由宿主工具取真实句柄、短等待巡检，不再自己目测比对状态。watcher 常驻，不逐批 clear。主编排的 task_wait 只读精确任务结果，不代跑 worker测试，不代判结果。

**安全 Enter**：只有①本次派单仍在输入框（含 queued 未提交指令）、②`state_change_seq` 未推进、③不是审批/确认 UI，三条件同时成立才由获授权 watcher agent 发一次并复验；一次失败交编排按原授权路由，禁止连按。程序永不发键、不读取/保存终端正文。

#### watcher 专用派单模板（所有 kind 通用，兼容可选 agent）

```text
[relay-lite:single-task] worker · phase=watcher · agent=watcher#<实例> · batch=na · round=1 · workspace=<任务工作区>
environment=<已校验环境>；space_id=<真实ID>；notify=<编排身份>；self=<watcher身份>。
读 AGENTS、核心 watcher 通用合同、环境协议与自己的宿主 adapter；RELAY_RECEIPT preflight。
监控主体采用独立普通终端中的space_watch.py；不要为保持监控反复要求模型续跑。
已有程序时只核精确PID/终端与启动结果，不重复启动；旧子进程入口须取得真实持久句柄。
程序每120秒动态观察本space其它agent，排除self/编排，不按kind或名单过滤。
变化才通知，无变化静默；提交不冒称消费；未知不盲重发，观察继续。
不写仓库或工作区文件，不存终端正文，不路由、不派活、不启动agent，不自动重启脚本。
```


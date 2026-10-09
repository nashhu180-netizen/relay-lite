# Herdr 环境协议

由 `environments.toml` 注册、`environment_config.py` 校验选择；本文件由所有 agent kind 共用。宿主后台进程调用见对应 adapter，监控公共步骤见[watcher 通用启动与监控步骤](watcher.md)。不依赖本仓 checkout 的安装目录。

## 进入前：加载当前 Herdr skill

先执行核心环境配置 gate，非零/非 READY 停止；命中 RELAY_RECEIPT 先按原角色 fail-closed 分流，不能借工具错误绕过零写入通知出口。任何 Herdr 控制命令前：

```bash
test "${HERDR_ENV:-}" = 1
herdr --skill
herdr --version
herdr --help
```

`herdr --skill` 是当前二进制内置技能入口，必须实际读取其完整输出，不能只知道名字或复制本文件当上游 skill。CLI 缺失、读取失败或输出无法识别为 Herdr skill 时报告 blocked 后停止，不安装/更新/伪造 HERDR_*。在执行策略只记读取来源/CLI版本，不存全文或环境值。

CLI 语法以安装版帮助为准；按需运行无子命令的 `herdr workspace`、`herdr tab`、`herdr agent`、`herdr pane` 读取帮助（帮助退出码2不等于控制失败），不靠省略变更命令参数探查。禁止 bare `herdr` 探查，它会打开TUI；不触碰其它 session、用户焦点、tab或pane。内置 skill 的默认 sibling pane 只是默认值，本用户/卡合同明确的一卡 space、每实例独立 tab 优先；用户已明确复用当前space时按实际 ID 复用。

## 首次启动：space → tab → 交互式 agent → 派单

先核开工/角色/模型确认与任务 worktree。尚无本卡space时创建：

```bash
herdr workspace create --cwd <任务worktree> --label <卡名> --no-focus
herdr tab create --workspace <返回的workspace_id> --cwd <任务worktree> --label <角色实例> --no-focus
herdr agent start <唯一名称> --kind <已确认kind> --pane <返回的pane_id> -- <已确认原生模型与推理参数>
```

workspace create 会自带初始 tab/root_pane：首实例可直接使用返回的 `.result.tab` / `.result.root_pane.pane_id`；其余实例各 tab create。操作顺序仍是先space、已有/新建独立tab、再交互agent，不额外造空tab。每次从JSON解析 `.result.workspace.workspace_id`、`.result.tab.tab_id`、`.result.root_pane.pane_id`（按当前版实际响应核字段）；不预测ID，不用UI焦点。名称须当前CLI合法且live唯一；kind是agent类型，不能当name/ID。agent start 不建拓扑，目标pane须空闲交互shell，不能已有前台进程。成功后核真实pane/agent及ready；blocked/unknown/超时只查真实结果、按原停止线处理，不盲重启。

原生参数只在 `--` 后，透传已确认模型档；Codex 默认提案形式为 `-m <模型> -c model_reasoning_effort=<档> --dangerously-bypass-approvals-and-sandbox`，Claude 为 `--model <模型> --effort <档> --dangerously-skip-permissions`；实际由用户确认，最大工具权限不扩大授权。优先 agent start；当前版无法可靠启动相应CLI时按已确认调用方式 `herdr pane run <pane> "<交互式CLI完整命令>"` 后 `herdr agent rename <pane> <名>`，读回检测成功再派单。绝不换成exec/headless模式。

## 派单、清理与投递确认

只向已核实的目标agent发ASCII派单文件指针，长中文派单保存在获授权文件；同任务新批次/新独立任务复用tab先执行核心清理闸。用目标模型当前帮助/实际UI核支持的原生清理命令，单独投递并确认原生成功提示/新空会话，再投新派单；`state_change_seq`变化不足以证明clear成功。不得用shell clear、清RELAY_*、覆盖历史signal/失败/计数，整改/E2/fresh/watcher例外沿核心。

```bash
herdr agent get <目标name或pane_id>
herdr agent prompt <目标> "Read and follow <dispatch-file>." --wait --timeout 30000
herdr agent get <目标>
```

提交成功只证明输入写入；默认 `--wait` 等待首次 settled idle/done/blocked，新投递从非working状态需观察本次working/blocked活动。核目标同pane、原生已提交输入与本次 `state_change_seq` 推进，完成仍读signal。普通任务不用多加 `--until`，有特定观察状态时才用。超时/blocked/stalled/未知不证明未发送，不盲重发；先核实际get/UI状态，证据白名单过滤，不把终端正文保存为监控日志。clear不像普通任务，状态推进以外仍须原生清理成功判据。

## 跨卡通信与通知

核心 card-chain update / maintainer-handoff / card-chain decision 的ASCII内容通过：

```bash
herdr agent prompt <登记的接收方name或pane_id> "<获授权ASCII通知>" --wait --until working --timeout 5000
herdr agent get <同一目标>
```

发送前后get核同pane、`state_change_seq`推进与working，极快结束没捕获working保守记未确认；需要原接收方确认的移交仍须它登记并回复。通信不授予写权/开工/合入；不可达或未知出口沿核心，不自动重发。RELAY_RECEIPT命中的watcher不能先跑被gate拒绝的脚本，直接按本节既有非durable通知权限通知后停。

## 固定观察脚本（全部 kind 共用）

默认让普通终端承载程序，watcher agent可选。编排按已确认测试/任务拓扑创建独立具名tab，解析真实pane ID；不要在现有用户pane里抢占前台。程序从真实shell继承上下文：

```bash
herdr tab create --workspace <真实space_id> --cwd <授权cwd> --label relay-monitor --no-focus
herdr pane run <返回的monitor-pane-id> "python3 <SPACE_WATCH> --workspace <真实space_id> --notify <编排name> --self <同一monitor-pane-id>"
herdr pane process-info --pane <同一monitor-pane-id>
```

仓内 SPACE_WATCH=`tools/space_watch.py`；安装后 `<SKILL_DIR>/space_watch.py`。空白/特殊字符路径须按真实shell转义，不用JSON当shell转义。普通monitor pane不出现在agent list中；脚本用pane get核self等于HERDR_PANE_ID且workspace_id正确。旧 `--self <watcher_name>` 兼容已启动agent，仍检查真实pane与继承身份；无持久宿主能力时不要把它当默认常驻方式。

启动后从指定终端只提取 `SPACE_WATCH_STARTED workspace=<id> pid=<pid> interval=120`，并用process-info/实际PID核程序仍活；只保留这些白名单事实，不能用shell文本猜PID，也不保存终端全文。同服务端/space固定内存socket占位防止重复启动；新实例冲突失败不影响旧实例，不生成repo/workspace锁文件。

脚本先拒绝缺失HERDR_ENV和存在（含空值）的RELAY_RECEIPT；每120秒按workspace_id动态发现agent，排除self与主编排的实际pane，不按kind/前缀/派单名单过滤，未命名agent按pane观察。身份/环境硬闸仍停止；临时只读命令失败/状态不全/list-get竞争保留原基线，下一节拍重新只读观察，避免假消失。

变化通知先核接收者并向其精确pane执行一次：

```bash
herdr agent prompt <已核接收方pane-id> "<白名单变化通知>"
```

返回agent_prompted只确认提交，不证明消费。主编排working可提交，不用working/seq推进作为提交判据；审批blocked/unknown时不提交、待下轮观察后合并。命令尝试后超时/失败/结果未知，输出 `SPACE_WATCH_UNCONFIRMED` 及白名单diff，保留未知，不自动重发该事件，观察仍继续；后续真实新变化独立处理。程序不发送Enter或读存终端正文。这里的提交语义仅适用于watcher即时提示，跨卡维护移交仍沿前节原确认合同。

## 主编排精确结果等待（watcher 暂停/缺席时同样有效）

每次派单后，编排按自己的精确派单选DONE/BLOCKED两个独立文件，不能扫描其它卡或用idle/done放行。WAIT_TOOL仓内 `tools/task_wait.py`，安装后 `<SKILL_DIR>/task_wait.py`：

```bash
python3 <WAIT_TOOL> --root <任务workspace绝对路径> --signal signals/DONE.batch.worker-1.md --signal signals/BLOCKED.batch.worker-1.md --task <当前task> --phase batch --agent <精确worker实例> --batch 1 --path na --review-round 1 --remediation-count 0 --timeout 50
```

root是任务文档workspace，与Herdr space ID不同。路径、文件名和七字段必须来自本批派单。只读工具拒绝越界/symlink/冲突signal/RELAY_RECEIPT；不调用Herdr、不发消息、不写文件，不启动agent。

退出0/READY：输出结果路径/hash与DONE/BLOCKED类型，**不是PASS**；主编排读完整原报告与signal核版本/复核/写者/原停止线，再处理结果或继续获授权交接。退出3/PENDING：没有匹配本批的完整结果，保持接收者并继续有界等待，不把一次超时当整个任务终止；不能发final空等watcher。连续PENDING时只读核已派worker的身份/状态与精确工件；明确失败、审批阻塞或退出无signal按原合同报告阻塞，不无限空等、不自动重投。退出2/BLOCKED：参数/边界/冲突硬闸，保留现场并处理实际阻塞。等待时按宿主adapter取真实句柄，单次工具等待不超过60秒，不让watcher在线成为结果核收前置。

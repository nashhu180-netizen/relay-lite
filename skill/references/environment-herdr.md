# Herdr 环境协议

由 `environments.toml` 注册、`environment_config.py` 校验选择；本文件由所有 agent kind 共用。宿主后台进程调用见对应 adapter，监控公共步骤见核心「watcher 通用启动与监控步骤」。不依赖本仓 checkout 的安装目录。

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

编排先按公共步骤给watcher独立tab/交互agent并写真实参数，watcher运行：

```bash
python3 <SPACE_WATCH> --workspace <真实space_id> --notify <编排name> --self <watcher_name>
```

仓内 SPACE_WATCH=`tools/space_watch.py`；安装后为 `<SKILL_DIR>/space_watch.py`。不是把业务任务文档的workspace路径传给`--workspace`。用宿主adapter持久进程工具运行并取真实句柄，启动后立即确认/报信，随后短等待巡检；只在宿主临时输出保留结果，无repo/workspace日志。所有kind都用此脚本和同一监控范围。

脚本要求 HERDR_ENV=1；RELAY_RECEIPT存在含空值拒绝。`--self`必须位于目标space，若提供HERDR_PANE_ID也须一致；不填self时可用该ID自动定位。内部每120秒 `herdr agent list` 动态发现workspace_id成员，按pane get状态，排除自身/主编排pane（主编排无论是否在该space都仅作为notify目标），不按kind或前缀/名单筛选；未命名agent也按pane观察。

第一轮快照仅内存建基线；新增/离开/agent_status或state_change_seq变动才通知。脚本通知用 `herdr agent prompt --wait --until working --timeout 5000`，核同pane、working与seq推进。投递失败/超时/未知不提交比较基线，输出固定 `SPACE_WATCH_BLOCKED reason=...` 与仅白名单diff的UNCONFIRMED、非零退出，不盲重发、不读存终端正文、不发送Enter。watcher核退出/存活，退出一次报信，通知不能确认则blocked后停，编排恢复前核实际结果，不自动重启。

watcher启动确认也通过上节通知入口，消息如 `[relay-lite] watcher-started <space_id> <self>`，仅核到真实子进程仍活后发；确认未知不能当监控已接管。原脚本的周期与基线不因此改变。仅核心安全Enter三条件同时满足时由watcher人工发一次；脚本永不发键。编排放行只读durable signal与独立工件，agent idle/done和watcher提示均不作完成真相。

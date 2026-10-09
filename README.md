# relay-lite

独立的单卡接力分工与跨卡接力计划，给任意业务仓使用。

- 卡内：orchestrator 直接分派 builder、executor（执行者）、reviewer、decider；watcher 只观察报信。
- 卡间：一个 Markdown 接力计划记录原卡、依赖、接棒条件、状态与下一步；只有用户写定的授权可自动接续。
- 任务不限代码：executor 可按授权写文档、配置、诊断和验证。

## 使用

先读 [协议](skill/SKILL.md) 和 [AGENTS.md](AGENTS.md)，通过 [环境配置](skill/environments.toml) 的校验工具选择派发方式，再按环境协议与 Codex/Claude 宿主 adapter 执行已获授权的单卡。模型确认与原仓的入口/出口/人验要求保持。

```bash
python3 tools/install_skill.py --all
python3 -m unittest discover -s tests -v
```

安装到当前用户的 `.claude/skills/relay-lite/`、`.codex/skills/relay-lite/` 与 `.agents/skills/relay-lite/`，包内含 watcher 和计划模板，不需要其它仓 checkout。存量会话需要旧 skill 名时显式追加 `--legacy-alias`，它仅安装同版单卡协议别名，不提供旧模式；磁盘更新不刷新已打开会话。

接力计划目录 [docs/relay/](docs/relay/README.md)，模板 [skill/templates/card-chain.md](skill/templates/card-chain.md)。[迁移来源与边界](docs/migration.md)，旧证据在 archive/ 只读保存。没有账本、五阶段或阶段主管。

当前仅注册 Herdr：派发前读取 `herdr --skill`，按 space → 独立 tab → 交互式 agent 启动；新任务/新批次复用 tab 先原生清理会话并确认，再派发。所有 agent 共用核心 watcher 启动/监控/报信/退出步骤，宿主 adapter 只处理进程工具差异。

仓内配置入口 `python3 tools/environment_config.py`；安装后 `python3 <skill目录>/environment_config.py`。工具只校验并返回环境协议路径，错误停止，不自动启动 agent。安装包新增配置/校验器/Herdr协议，不需要此仓checkout；Herdr运行仍需该环境与CLI。本卡测试为离线协议/配置/安装验证，不证明真实Herdr演练。

## watcher 持续运行

新监控默认在独立 Herdr 普通终端运行space_watch.py，watcher模型空闲/结束回复不影响它。通知确认提交后由编排核原结果；通知未知保留且不盲重发，观察继续。主编排用task_wait.py按本批精确派单有界等待DONE/BLOCKED，READY不代替验收，PENDING不结束整卡。启动、身份/重复实例核验和命令见[Herdr环境协议](skill/references/environment-herdr.md)。真实在途space的切换/重启需要原任务授权，不因更新代码自动发生。

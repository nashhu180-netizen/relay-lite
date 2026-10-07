# relay-lite

独立的单卡接力分工与跨卡接力计划，给任意业务仓使用。

- 卡内：orchestrator 直接分派 builder、executor（执行者）、reviewer、decider；watcher 只观察报信。
- 卡间：一个 Markdown 接力计划记录原卡、依赖、接棒条件、状态与下一步；只有用户写定的授权可自动接续。
- 任务不限代码：executor 可按授权写文档、配置、诊断和验证。

## 使用

先读 [协议](skill/SKILL.md) 和 [AGENTS.md](AGENTS.md)，再按 Codex/Claude adapter 执行已获授权的单卡。模型确认与原仓的入口/出口/人验要求保持。

```bash
python3 tools/install_skill.py --all
python3 -m unittest discover -s tests -v
```

安装到当前用户的 `.claude/skills/relay-lite/`、`.codex/skills/relay-lite/` 与 `.agents/skills/relay-lite/`，包内含 watcher 和计划模板，不需要其它仓 checkout。存量会话需要旧 skill 名时显式追加 `--legacy-alias`，它仅安装同版单卡协议别名，不提供旧模式；磁盘更新不刷新已打开会话。

接力计划目录 [docs/relay/](docs/relay/README.md)，模板 [skill/templates/card-chain.md](skill/templates/card-chain.md)。[迁移来源与边界](docs/migration.md)，旧证据在 archive/ 只读保存。没有账本、五阶段或阶段主管。

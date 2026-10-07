# RLT_35 独立代码复核（normal / 第 1 次完整初审）

结论：**changes-requested**。fresh-context reviewer 未参与实施；P0=0、P1=1、P2=0、P3=0。

## 被审候选与冻结核对

- baseline：`e473f1d6ca99b8ca8a2f0f31280290823cda1ee9`
- target：`3e7797417a09c8a9e2ee96bf29fd731fed182966`
- dispatch：`E-010`；实现者：`codex-root-rlt35-20261007`
- 使用冻结口径 `git diff --no-ext-diff --no-renames --full-index <baseline> <target> | sha256sum`，结果为 `621d81ba88ce1fe87935318bd37c2390dfbabb7531c0655f91f5690e37dc18fe`，与 freeze/派单一致。

## 发现

### CR-001 · P1 · Windows 必要 CI 失败

`tests/test_install_skill.py:165` 以未经 `resolve()` 的 `target / "references/environment-herdr.md"` 与 helper 输出比较；`tools/environment_config.py:30,118` 则通过 `Path.resolve()` 选取 skill 根与协议路径。Windows runner 的短路径 `C:\\Users\\RUNNER~1` 因此与 helper 的规范路径 `C:\\Users\\runneradmin` 字符串不等，令 `test_environment_gate_is_standalone_after_source_checkout_disappears` 失败。原始白名单证据见 `evidence/ci-windows-failure.log`（GitHub Actions run `37645600395` / job `112875415085`）；58 项中 1 项失败。

修复必须让测试期望按同一 `Path.resolve()` 口径规范化（或采用另一份明确且一致的输出契约），并保留路径逃逸拒绝。修复后需要 Windows、Ubuntu 完整 CI 及同一 reviewer 的一次 `attempt=2` 定向复核；normal 配方不允许另换 reviewer 或新增完整初审。

## 已核通过的部分

- `environment_config.py` 严格校验闭集 TOML、默认注册、全量协议路径、路径越界和运行环境；未知、冲突、缺件、`RELAY_RECEIPT`（含空值）均输出固定的无凭据 BLOCKED JSON 并非零退出。
- 核心和两份 adapter 均先经过环境 gate，Herdr 控制命令只在 `environment-herdr.md`；恢复的 `--expected`、原生 clear 成功判据和失败/未知停止均未削弱 RLT_34 的历史、额度与 `RELAY_*` 边界。
- watcher 公共合同位于核心协议且明确适用于所有 kind；Herdr 协议仅载体/监控合同，两份 adapter 仅保留各自真实子进程句柄的宿主调用方式。通知、退出和未知状态均 fail-closed，且不把外层运行提示当脚本存活。
- 安装闭包含配置、校验器和 Herdr 协议；三端 manifest 逐项哈希，安装后 helper 可在源 checkout 消失时独立解析协议。无真实安装副本或 Herdr 环境被操作。

## 验证

本 reviewer 在 Linux 执行 `python3 -m unittest discover -s tests -v`，58 项通过，退出码 0；原始输出见 `evidence/reviewer-tests.log`。该本地结果不覆盖 Windows CI 失败。测试前后以冻结口径复算的候选 diff 摘要不变。

局限：本复核及测试验证离线配置、安装与书面协议，不证明真实 Herdr 的 space/tab/agent 操作；该实时环境操作不属于本卡范围。

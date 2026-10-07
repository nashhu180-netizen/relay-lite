# RLT_34 code review — attempt 1

结论：**approved**。这是 normal 卡的完整 fresh `code_review`；审查者未参与实施。

## 核对范围

- 仅审 `43f68e0822785e57d640aa32d885148ba97ff8ac..e6adef4fe009972bc86071a636e03009e54337d0`；`git diff --full-index` 的 SHA-256 为 `7acbd4404927f0b053aae0874293636a15f778cd9b8af995765beed7f9ea1da6`。
- `skill/SKILL.md` 把新批次与新独立任务的 clear 规定为派单前门：先保存原工件/signal，复用 tab 先 clear 并确认，再投递；命令和派单分两次投递，未知或失败不派新单、不盲重发。
- 同一核心段保留 batch PASS/齐件后 executor 和 batch-reviewer 各一次 clear、FAIL/整改和 E2 原会话、fresh 不得由旧实例 clear 冒充、watcher 不 clear、历史 signal/计数与 `RELAY_*` 不清除等边界。
- 两份 adapter 都引用核心门，并重复要求清理成功后再投递、不可合并投递及失败/未知 fail-closed；与核心一致。
- 新契约测试覆盖核心门和两 adapter；登记的变异点删除“先 clear 并确认”后指定测试 RED，原字节还原后 GREEN，属于有效的文档协议变异断言。

## 独立验证

`python3 -m unittest discover -s tests -v`：41 项通过，退出码 0。

## 证据局限

本卡改变的是书面协议与契约测试。没有自动会话清理程序，也未操作真实 Herdr tab；这与源卡明示边界一致，不能据此声称已在真实环境执行 clear。

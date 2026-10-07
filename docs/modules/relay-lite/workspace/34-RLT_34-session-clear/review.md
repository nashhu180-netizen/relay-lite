<!-- dh:v1 -->
# review — RLT_34

## 独立复核区
normal=[code_review]，初审完整 fresh；未派前不伪填 receipt/result。

## AI 提交区

**Confidence Challenge**：待验证与独立复核。

## 完成条件逐条挂证据

| # | 完成条件 | 谁验 | 证据 | 达成? |
|---|---|---|---|---|
| RL34-M1 | 新批次派单前，前批 durable PASS 且工件齐全，executor 与 batch-reviewer 各 clear 一次并分别确认成功。 | AI | | 待验证 |
| RL34-M2 | 标签页接新的独立任务前保存前任务工件与 signal，清理旧会话并确认成功，再读取新派单；新建空会话不冒充复用会话的 clear。 | AI | | 待验证 |
| RL34-M3 | 同任务 FAIL/整改与 E2 定向复查保留原会话及计数；fresh reviewer 必须是未参与实施的独立新实例；常驻 watcher 不逐批 clear。 | AI | | 待验证 |
| RL34-M4 | 清理失败或结果未知时停止新派单，不盲重发；core 与两 adapter 一致；历史 signal、证据、计数及 RELAY_* 保留。 | AI | | 待验证 |
| RL34-M5 | 协议回归及变异 RED→还原 GREEN、fresh 独立复核、Ubuntu/Windows CI、PR 合入态复验和 verify(relay-lite) 齐备。 | AI | | 待验证 |

## 需求对齐证据
待核心规则、adapter 与回归就位后逐项挂证据。交付是文档规则，真实运行不在本卡承诺内。

## 人类签名区
无人判结果项，不代签用户人验。

## 自动收口记录
未进入放行；待实际复核与 CI/合入态验证。

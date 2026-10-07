<!-- dh:v1 -->
# progress — RLT_35

## 日志 (Log)

| 时间 | 谁 | 做了什么 | 证据 | 下一步 |
|---|---|---|---|---|
| 2026-10-07 | /root | 确认承接；#12 落户与独立 worktree/正式输入/七件套 | brief、review.plan、GitHub #12 | 实施/测试 |

## 证据账本 (Evidence Ledger)

| ID | 类型 | 命令 / 路径 | 结果 (pass/fail/observed/waived) | 支撑什么结论 |
|----|------|-----------|------|------|
| E-001 | test | python3 -m unittest discover -s tests -v；evidence/baseline.log | pass | 开工基线41项，exit0；不证明live Herdr |
| E-002 | check | dh relay-lite；evidence/check-initial.log | fail | 初始规划marker/需求表预填格式17失败，原结果保留；按实际规划原报告补正 |
| E-003 | check | dh relay-lite；evidence/check-planning.log | pass | 规划/预填格式补正后0失败，警告非阻断 |
| E-004 | test | evidence/config-implementation.log | pass | 配置局部实现17项定向测试；三端工具闭包 |
| E-005 | test | evidence/candidate-first.log | fail | 首轮53项1 error：旧watcher标题引用；保持兼容标题修正 |
| E-006 | test | evidence/candidate-green.log | fail | 58项1 failure：核心漏workspace_id映射，补显式接口说明 |
| E-007 | test | evidence/candidate-final.log | pass | 全套58项exit0；包括动态发现/通知与安装/CLI |
| E-008 | test | evidence/mutation-red.log；mutation.json | observed | 未知环境回退变异，指定测试断言失败exit1，不是导入/环境失败 |
| E-009 | test | evidence/restored-green.log | pass | 生产代码精确原字节还原；全58项exit0 |
| E-010 | review-dispatch | dh dispatch | observed | 复核派出：fresh-context-subagent｜path=code_review target_sha=3e7797417a09c8a9e2ee96bf29fd731fed182966 diff_sha256=621d81ba88ce1fe87935318bd37c2390dfbabb7531c0655f91f5690e37dc18fe｜path=code_review｜attempt=1 kind=full session=/root/rlt35_code_review |

| E-011 | review | evidence/code-review.json/md | fail | 初次完整独立复核 CR-001 P1：Windows 短路径断言失败；原报告保留 |
| E-012 | CI | evidence/ci-windows-failure.log；ci-initial.json | fail | 初次 Ubuntu PASS / Windows 58项1失败，非产品路径逃逸 |
| E-013 | test | evidence/repair-green.log/json | pass | 断言按 helper 相同 resolve 规范口径比较；全58项 exit0，待双平台CI |

## 实施验证命令矩阵（开工计划复核 P1 补充）

| 用途 | 精确命令 | 预期/证据 |
|---|---|---|
| 工具与三端安装 | python3 -m unittest discover -s tests -p test_environment_config.py -v；python3 -m unittest discover -s tests -p test_install_skill.py -v | 局部执行者串行完成，config-implementation.log |
| 协议/全回归 | python3 -m unittest discover -s tests -v | 全写入结束后root串行，candidate-green.log |
| 有效单测 | python3 -m unittest discover -s tests -p test_environment_config.py -k unknown -v | 未知环境拒绝语义变异必须断言失败；精确恢复GREEN |
| 原证闸/文档闸 | dh gate relay-lite 35-RLT_35-environment-dispatch --review-json；dh relay-lite | 当前worktree根调用；原JSON/实际退出码 |
| 合入复验 | python3 -m unittest discover -s tests -v；dh gate relay-lite 35-RLT_35-environment-dispatch --review-json | 主干实际merge后，完整Git元数据，同产品原字节 |

独立开工计划复核已确认设计/任务完整，命令矩阵P1采用；watcher通用流程适用全部kind，CLI能力在环境协议，宿主进程句柄在两adapter。

实施里程碑@候选就绪：环境gate/Herdr协议/通用watcher/安装闭包就绪，58项回归与有效单测完成，失败历史保留；下一步fresh code_review。

CR-001 同范围修复：仅测试期望路径规范化；候选登记 miner 两条草稿，不改验收/产品/正式知识库。

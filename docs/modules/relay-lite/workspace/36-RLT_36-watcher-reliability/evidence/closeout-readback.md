# RLT_36 · 有限收口归档机械核验

结论：**归档内容真实、范围机械；未发现本次有限核验的阻塞。** 拟采用服务端普通 merge 可保留 verify 的原 SHA 可达性。本报告不是第二次 code_review，不增加 attempt，不重做实现复核或验收；唯一代码复核原 md/json 保持原字节。

核验实例 `/root/rlt36_code_review`。仅按 dev-harness `references/动作-E-收口.md`「远端交付顺序与失败处理」第4条，核有限收口实际内容、verify 消息和目标可达性。检查时 RELAY_RECEIPT 不存在；本次没有运行测试、Herdr 控制/消息、安装、部署、派活或代签用户结果，仅写本文件。

## 精确候选与范围

- worktree：`/home/nash/work/relay-lite/.dh-worktrees/RLT_36`
- branch：`closeout/RLT_36`
- 最终读取 source：`ddaf317bafe3b74a779aba89d11e384eaad59dbd`
- 初次派单 source：`42593c61cc85a20358fdd32c41fc580b6340ff1c`
- 实现 merge/base：`b940ca0e15a8b10fa82aa64b3388e7b204e4d5ad`
- verify：`54df8535721f959bea4e0326d626cdb413028e5a`

读取最终 source 时工作树无未提交改动。base→最终 source 的13个变更文件全部位于本卡 W 或源卡 `dev_plan/P4-watcher可靠性.md`；tools/tests/skill/README/as-built 的 diff 为空。后续 ddaf317 相对42593c6只调整源卡 status 和任务行的最终机械措辞，没有改验收、分类、授权、允许路径或产品。源卡日期2026-10-09、verify全SHA、release_mode=full，与实际机器证据一致。

源卡现在的“已完成/已归档”为有限 PR17 拟合入后的最终状态候选；有限 PR 未实际合入前，不能据此宣称远端已包含这些新增证据、Issue已关闭或本卡 worktree/branch 已清理。review.md 明确保留该条件，下一步不自动续卡，也不把源码归档解释为现有业务 space/用户副本升级。

## verify 与交付证据

verify 的唯一父提交为上述实际 merge/base，之后 source 含机械归档提交。消息为 `verify(relay-lite): RLT_36 端到端验收通过`，footer 完整记录：Verified-By=AI codex-root-rlt36-20261009；Verified-Via=本卡 task-start-authorization/brief授权锚点；Verified-At=2026-10-09 Asia/Shanghai及隔离w6Y/merged master完整SHA；Evidence 指向单测、check、gate、PR16、integration.json与live/final.json；Verification=full；Risk-Count=0；Risk-Refs=none；DoD三项勾选。消息没有用户签名；原机器验收记录明确未代签用户整体体验。

`integration.json` 绑定实际 merge b940ca0、PR source158d132c73f0babdce38093568a7dbf6163ecf57和原所审fa9c21f，记录 clean_before_tests=true、product_bytes_equal_reviewed_candidate=true及 tests/check/gate 三项exit0。此次只读 Git 比较也确认原所审候选→实际merge的产品diff为空。integration-tests.log 的最终结果为76 tests、4.083秒、OK；integration-check.log/check-release.log 保留0失败、9警告的实际输出，没有把警告改写成无警告；两份原 gate 工件均为dh.review-gate.v2/PASS、open_blockers=[]，仍绑定唯一 code_review 原结果。

`pr16-final-ci.json` 的 headRefOid 为158d132c73f0babdce38093568a7dbf6163ecf57，Ubuntu/Windows两个CheckRun均COMPLETED/SUCCESS。`pr16-merge.json` 的同一 headRefOid、state=MERGED、mergeCommit=b940ca0、mergedAt=2026-10-09T10:05:55Z，与实际Git双父merge一致。核验依据为归档的原平台readback，本实例没有重新联网读取平台状态，也没有将初次fa9c21f的CI代替最终source CI。

`cleanup-space.json` 保留仅关闭自建w6Y的close_exit=0、首次readback非JSON异常、后续只读workspace_list缺席和monitor PID740665消失；没有重复close或控制其它space。这是原隔离测试space清理证据，不能解释为Git worktree/branch已清理。本次没有运行Herdr重新验证该历史事实。

原 `code-review-1.md/json` 与实现source158d132中的字节分别完全相同，SHA256为 `9e526357f989f6ec2b20f08a81e2ad11c55fa4430ccd196cb1bfda11a76581fe` / `96c299b0bb1522bbb9b2da2bc96739325098af04ce34ddf5098076b458a5476d`。原attempt1/approved/findings=[]未被改写，本次不新增复核路径或receipt。

## 目标可达性

只读 Git 核实原所审fa9c21f可达实际merge/base，base为verify祖先，verify为最终source祖先。当前本地master指向verify54df853，已读取的本地tracking origin/master为实际merge b940ca0；它们不是本实例新增的远端状态声明。

服务端以普通merge合入该source时，source成为新merge的父提交或其祖先，因此verify54df853及原实现候选仍可达，满足保留原verify SHA的归档方式。此结论绑定普通merge及上述source祖先链，不提前声明有限PR已经合入。最终merge SHA、远端包含证据、Issue关闭和仅本卡Git现场清理仍由原编排按实际平台结果核收。

有限机械核验完成，本实例立即停止。

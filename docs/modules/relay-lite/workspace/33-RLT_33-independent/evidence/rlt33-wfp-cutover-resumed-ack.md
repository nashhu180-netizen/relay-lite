# WFP 新表恢复维护 ACK — RLT_33

2026-10-07 18:19:15 +08:00，依据本轮用户RLT_33恢复通知。

- 唯一现役表：/home/nash/work/relay-lite/docs/relay/wf-analytics-platform/workflow-platform/wfp-p1-obd-p5/relay_plan.md。已确认新仓master本机HEAD7a3346f3c2f1f6cd010df382ccd06f96b513e453，状态干净；迁入表体对源PR158/65f87a0已核字节一致。
- 唯一维护权保留：wfp08-orch/kpi-agg/w6F:t1/p1，GPT-6.1 Sol high/session01a11599-07ad-7b93-8097-042301220688；原w61保留历史。确认恢复新表维护，旧表不再写，不并写。execution_strategy入口已为新绝对路径，并登记本次恢复。
- 源PR157 squash8cbff631af90198484036f60c2a82a2b032ff680由RLT_33通知；本机origin/master实际同SHA。dh-relay当前本机HEAD3940ad542a20e76c51153dd6941db60f103cfc51/verify(dh-relay): RLT_33 源仓迁出验收通过，状态干净；相比通知中的普通merge已前进到RLT证据收口，不回退/不push此无关链。PowerShell ALL PASS/SKIPPED1只引用RLT通知，本会话未重跑。
- 当前WFP08：B4仍BLOCKED；历史B1/B2/B3与R1原2/2、supplement1/1、resident4/3/2/2不变。I=c020f205c2f26e94127db8c22b5cc2dff03ab9a3非完整G。transport-1类型生成/check各一次exit0，但SFTP回传及故障只读exit1，资源未清理/主仓后态NOT_PROVEN，失败与额度保留。原coder在identity/frozen本地准备；同decider已有有限回传决定，后续原coder精确续派，不重跑生成；未执行第三次R1/R0～R6/真实PAT/部署/配置装配/源调用。
- 最近用户另明确仅WFP08四路终审+独立E2，heavy/有效单测/三非代码required/所有真实与人验/verify保留；该决定来源是用户异步答复，不是本迁移恢复通知。官方selector对原P1非规范卡标题出现card-not-found，未用于派发，交同decider有限格式澄清；不默退旧策略/不预派终审。
- 待同步新表精确WFP08行/最近核对/维护说明，自动接续栏只读、其他卡不扩写；按新仓原规则Issue+独立文档分支/PR+必要CI/独立审核交付。旧PR158当前OPEN/head65f87a0，内容已迁入；按原合同在确认新表维护交付后处理旧PR，不合入退休旧路径、不删历史分支。
- 业务授权、模型、signal、历史失败/预算不因迁移变化；本ACK不视为H1～H3或任何真实业务人验。此前paused/active ACK保留。

HANDOFF_CONFIRMED_RLT36

- task_wait: 4 calls; actual PENDING count=3. First three calls returned exit 3 with {"acceptance":"not_evaluated","reason":"matching_signal_not_ready","state":"PENDING"}.
- Native task_wait READY result: {"acceptance":"requires_owner_review","sha256":"2b498bd81b6ff07192215e2d2d7c98b3776a267b200adea397440af7f447a2a3","signal":"signals/DONE.batch.worker.md","signal_kind":"DONE","state":"READY","verdict":"READY_FOR_REVIEW"}. READY is not PASS.
- Signal identity: task=RLT_36_TEST phase=batch agent=worker#rlt36 batch=1 path=na review_round=1 remediation_count=0 verdict=READY_FOR_REVIEW. On-disk signal SHA256 matches task_wait: 2b498bd81b6ff07192215e2d2d7c98b3776a267b200adea397440af7f447a2a3.
- Worker report: evidence/live/worker-report.md SHA256=875b042b9bb348d482eb8d1e487933513846ceaa7b68c4e478a9e5e00368ecc4; contains WORKER_RESULT_RLT36 and says this is a local temporary test deliverable, not business task acceptance.
- Worker signal and report are consistent with the exact dispatch and evidence path. No batch PASS or business acceptance is inferred.
- Actual Herdr readback: name=rlt36-worker, kind=codex, session_id=01a12009-9c9d-7d40-be8b-9083c11d4c66, workspace_id=w6Y, tab_id=w6Y:t2, pane_id=w6Y:p2, agent_status=done, state_change_seq=3062, interactive_ready=true. The worker is stopped/settled; no routing was performed.
- The watcher model ended and the independent monitor was stopped by the test owner before worker dispatch: watcher actor readback reports done with WATCHER_MODEL_TURN_ENDED; scene-B-monitor-stop records pid_absent=true, reason=authorized controlled stop, and worker_dispatched=false. The worker dispatch independently records the same prerequisite.

<!-- dh:v1 -->
# RLT_38 plan check

## Scope and method

Read-only cross-check on 2026-10-09. Compared the RLT_38 DevPlan contract,
`brief.md`, and `task_plan.md` against the baseline protocol, installer, and
contract/install tests identified by `task_plan.md` (`0b08c18…`). This is a
plan check only: it does not assess an implementation, consume a code-review
attempt, or alter product files. Concurrent product changes that appeared
after this baseline read are outside this check.

## Conclusion

**PLAN_NEEDS_AMENDMENT — do not dispatch implementation from the current
`task_plan.md`.**

The task is correctly scoped as a normal standard-delivery protocol refactor:
the source card and brief agree on M1–M4, the allowed paths cover the intended
protocol, installer, tests, workspace evidence, and as-built note, and the
classification explains why the reading/routing change is normal rather than
light. The plan also correctly keeps real installation upgrades, business
cards, environment/production operations, and rule changes outside scope.

Its four implementation lines do not yet provide enough worker-executable,
reviewable evidence design for M1–M3. In particular, the required rule
preservation, installed-package reachability, and unique-template proofs are
named but not made reproducible. M4 can only be planned after those proof
artifacts and test cases are specified.

## Required plan additions before implementation dispatch

1. **M1 baseline and delta ledger.** State one deterministic counting command
   and exact input set for each of: package/skill total, `SKILL.md` core, and
   both adapters. Record the baseline SHA (`0b08c18…`), before values, after
   values, and an itemized classification of every character delta as
   `moved`, `deduplicated`, or `new required routing text`. Name a durable
   workspace evidence path (for example `evidence/size-ledger.md`). “基线统计”
   and “保存逐节映射” in the current step 1 do not define the unit, inclusion
   set, destination, or distinction required by RL38-M1.

2. **M2 rule-preservation matrix.** Add a matrix with one row for every
   required invariant from RL38-M2: authorization, roles, model allocation,
   writer ownership, signals/fail-closed receipt handling, counters, native
   clear/cleanup, recovery, card-chain handoff, and unknown-stop behavior.
   Each row needs: pre-change source heading or stable text anchor, post-change
   file plus heading, whether it is common/core or host-specific, and its
   verification method (targeted contract assertion or a precise static read
   check). Include the related cross-file references in the same matrix. A
   generic “逐项核…语义保留” cannot show that a rule moved to an on-demand file
   remains reachable from the reader who needs it.

3. **M3 distribution and reference closure.** Before moving files, enumerate
   the final managed package set, including every newly introduced referenced
   protocol document and template. For each file state: source location,
   installing consumer(s), incoming link/trigger, and how it is reached after
   an isolated install. The current installer’s closed `SKILL_FILES` list does
   not include the proposed `skill/references/card-chain.md`,
   `document-role.md`, `verification.md`, `orchestration.md`, `watcher.md`, or
   `templates/dispatch.md`; step 3 says to extend that baseline list but does
   not define the complete target set. The plan must also state the source-to-installed
   link check and a temporary-home install check for every required consumer,
   rather than relying only on source-tree links.

4. **M3 canonical dispatch-template proof.** Specify the exact canonical
   template path, the adapters/core headings that link to it, and the adapter
   fields that may remain host-specific. Add a test/static assertion that both
   adapters point to the canonical template and that neither retains a second
   full dispatch template. Pair it with the M2 matrix rows for the dispatch
   header, executor/role terms, required fields, and fail-closed signal rules;
   otherwise “唯一” risks reducing wording while losing a host-specific guard.

5. **M4 test and mutation contract.** Name the test methods and assertions for
   (a) final closed package manifest, (b) source/installed byte identity for
   each managed file, (c) installed reference reachability, and (d) the
   fail-closed mutation. For (d), pin the mutation target to one required
   distribution/reference file, state the expected failing test and failure
   reason, then restore and rerun GREEN. “缺分发文件” alone is ambiguous: it
   could exercise an irrelevant file or a source-only check, neither proving
   M3’s installed-consumer requirement.

6. **Execution evidence locations.** Allocate the requested ledgers/matrix
   and test/mutation transcripts under this workspace, and reserve the
   allowed `as-built/protocol-reading.md` for the final reader-facing map.
   State which artifact supplies each M1–M4 conclusion to the normal fresh
   `code_review`, CI, merge-state recheck, and verify. This preserves the
   existing one-attempt normal review contract; no additional review route is
   requested.

## Evidence references

- DevPlan: `docs/modules/relay-lite/dev_plan/P6-协议精简.md:20-58` defines
  scope, M1–M4, allowed paths, and the normal task contract.
- Brief: `docs/modules/relay-lite/workspace/38-RLT_38-protocol-trim/brief.md:5-25`
  repeats scope/classification/completion conditions and excludes a claim of
  real business-session validation.
- Current plan: `docs/modules/relay-lite/workspace/38-RLT_38-protocol-trim/task_plan.md:4-14`
  has the relevant intent but lacks the concrete artifacts and assertions
  above.
- Baseline packaging: `tools/install_skill.py` supplies a closed
  explicit install list; `tests/test_install_skill.py` validates that list and
  isolated installation. This makes the final managed-file/link inventory a
  necessary pre-implementation plan input, rather than a detail that can be
  inferred after documents move.

## Stop line

No product implementation was reviewed or changed. Resume implementation only
after the task plan is amended with the six items above; then execute the
existing normal one-fresh-code-review route without resetting or adding review
attempts.

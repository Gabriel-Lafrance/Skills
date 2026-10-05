---
name: gabriel-mode
description: Orchestrate an already precise ticket through test and coding subagents, each reviewing its own contribution before the main agent judges it. Use when the user invokes /gabriel-mode. Finish with combined review, verification, and a ready-for-PR assessment.
category: Code
---

# Gabriel mode

Build one already precise ticket through bounded worker slices. Each implementing worker runs `/review` on its own contribution. The main agent independently checks correctness and omissions against the ticket and project rules, and returns fixes to that worker. Finish with review of the combined changes, then verification.

Inspired by pstack's [poteto-mode](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/SKILL.md). This skill owns orchestration only. Existing pack skills own implementation standards, tests, review evidence, verification, and shipping permissions.

## Read when

- At entry: read the project's instructions, the ticket and relevant decisions, [`/task`](../task/SKILL.md), its [doctrine](../task/doctrine.md) and [reference](../task/reference.md), and the [execution context](../rules/planning.md#execution-context).
- Before a delegation or correctness decision: open [principles.md](../rules/principles.md) and [main-context.md](../rules/main-context.md), then the applicable project rules. Pass those rule paths to workers. A verdict without checking the governing rules is incomplete.
- Before implementation or review: apply [code-quality.md](../rules/code-quality.md) and [code-structure.md](../rules/code-structure.md). Open [strong-foundation.md](../rules/strong-foundation.md) for a Feature, and [user-experience.md](../rules/user-experience.md) plus the project's `docs/design.md` for user-facing work.
- When tests are specified: read [`/task-with-tests`](../task-with-tests/SKILL.md), its [reference](../task-with-tests/reference.md), [no-unrequested-tests.md](../rules/no-unrequested-tests.md), and [testing.md](../rules/testing.md).
- At each review or verification: follow [`/review`](../review/SKILL.md) or [`/verification`](../verification/SKILL.md), including their required reads.
- Before writing or asking: follow [Plain language](../rules/writing-style.md#plain-language) and [Asking the user](../rules/writing-style.md#asking-the-user).

## Local orchestration contract

Use the selected task route's contracts and standards, not a second complete `/task` run inside each worker. These differences apply only during an explicit `/gabriel-mode` run:

| Existing default | This run |
| --- | --- |
| `/task` builds its slices itself | Workers implement bounded slices; the main agent owns decomposition and acceptance. |
| `/task-with-tests` writes tests before the product plan | Decompose only accepted test work first. Keep product planning and implementation after test approval and baseline. |
| `/task` suggests behavior locks | A ticket with no specified tests goes directly to coding decomposition. Do not manufacture a test phase. New test proposals still require user acceptance. |
| Review and verification run together | Worker review, main slice judgment, combined review, main whole judgment, then verification, in that order. |
| Run state stays in chat | Also maintain the explicitly requested temporary process record below. It never grants authority. |
| Completion may lead to shipping | Stop at the ready-for-PR assessment. This invocation grants no shipping permission. |

Do not change the defaults of `/task`, `/task-with-tests`, or `/review` outside this run. Preserve accepted test assertions, user refusals, rule ownership, and [shipping.md](../rules/shipping.md). A worker never owns the branch, ticket, or shipping. Do not commit, push, create a PR, merge, deploy, or install as part of this workflow.

## Process

1. **Establish the run.** Apply the shared [ready-ticket preflight](../rules/execution.md#ready-ticket-preflight) and [handoff contract](../rules/execution.md#handoffs-and-evidence), reading the ticket as [read-only context](../task/doctrine.md#ticket-context). Announce the current lock, decision sources and next phase.
2. **Open the process record.** Use a unique Markdown file at `<system-temp>/gabriel-mode/<run-id>/process.md` unless the user supplied a destination. Announce its actual absolute path. The main agent is the sole writer; workers read it and return updates in handoffs. Keep the current goal and decisions, ticket and fixed point, phase, slice owners and dependencies, evidence, fix backlog, drift, and goal or implementation changes. Mark proposed changes separately from approved ones and cite their decision source. Update at phase changes and handoffs. Keep material decisions visible in chat; this file is a coordination aid, not a ticket rewrite, approval source, or hidden recovery requirement. Do not commit it.
3. **Select the test route.** Specified tests select `/task-with-tests` semantics. A ticket's proposed tests alone are not acceptance: carry forward explicit acceptances and refusals with their user decision source, and ask once about unsettled tests using its [tests prompt](../task-with-tests/reference.md#tests-prompt). Do not repeat settled questions. If no tests are specified, or all are refused, use `/task` semantics and proceed to coding decomposition. A missing public entry or conflicting test requirement is a blocker to resolve, not permission to invent a test.
4. **Build the accepted tests first.** Decompose accepted tests into worker slices using the slice loop below. Every brief names why the test matters, what it locks, and how it exercises the public entry. Workers write tests only; do not implement product behavior to make them pass. Each worker reviews its test contribution and the main agent judges it. Apply the [red baseline](../task-with-tests/reference.md#red-baseline): fix setup failures, record expected failures or already-green behavior, and stage only this run's accepted test files when doing so preserves unrelated index work. If the index cannot hold that baseline safely, resolve the workspace boundary before continuing. Once every test slice is approved and its baseline recorded, carry the accepted tests into coding Done when.
5. **Decompose and build code.** Use the existing [slice split](../task/reference.md#slice-split) and [inline plan contract](../task/reference.md#inline-plan-contract), with the [planning rules](../rules/planning.md) for product plans. Apply the slice loop to each coding slice. Product workers leave accepted test assertions and scenarios fixed under the [test rules](../task-with-tests/reference.md#test-rules). Work in dependency order; parallelize only independent slices with separate write ownership. Size delegation to the work and available harness, without fixed worker counts or model mandates.
6. **Review the combined result.** Once slices are accepted, run `/review` in local mode over all this run's changes, including tests and cross-slice seams, against the pinned run baseline. Use a fresh review subagent with the [combined review context](../review/contract.md#fresh-combined-review-context), including the whole ticket and factual slice evidence, without the implementation conversation or worker verdicts. The main agent then independently checks the actual combined diff for correctness and omissions against every Done when item and rule. Slice approvals alone cannot pass this gate. If either review or the main judgment finds a gap, return to coding decomposition with the bounded fix backlog, then review and judge the resulting combined changes again. Test defects follow the test rules and route back to their test owner when authorized.
7. **Verify after whole approval.** Launch `/verification` in a fresh subagent only after the combined review and main judgment pass. Supply the whole contract, accepted tests, combined diff, evidence, and [selected verification scope](../rules/execution.md#verification-scope). It runs applicable suites and real-path checks, expanding for shared/high-risk effects or an explicit full request. For the tests route, include every accepted test passing and the [fixed-test check](../task-with-tests/reference.md#fixed-test-check). The main agent reads the evidence and judges it against the same project rules and Done when.
8. **Assess readiness.** Use the [`/task` completion summary](../task/reference.md#completion-summary), naming the checked revision and working diff, accepted tests, review findings, verification evidence, and remaining blockers. Say ready for PR only when the actual combined result meets the ticket, applicable gates passed, and there are no unresolved blocking findings. Otherwise say blocked or incomplete and give the next action. Report any named user waiver separately from proof. Leave shipping to a separately authorized action under [shipping.md](../rules/shipping.md).

## Slice loop

1. **Brief the worker.** Use the shared [handoff contract](../rules/execution.md#handoffs-and-evidence), including the slice's reason, concrete approach, public entry and process-record path. Supply the current contract directly even when that temporary record is unavailable.
2. **Implement, then self-review.** The implementing worker follows the selected task route within that brief. The same worker invokes `/review` in local mode, scoped to its contribution and relevant callers. Use initial Standards and Spec depth for a new contribution; use remediation mode for named fixes. Return its bounded diff, the [review output](../review/contract.md#review-output), checks and outcomes, omissions or blockers, and proposed process-record updates. It does not run an independent task lifecycle or ship.
3. **Judge in the main context.** Read the relevant diff and evidence, consult the applicable project rules, and check both correctness and completeness against the slice contract. Do not accept the worker's verdict on trust. Record approval or specific gaps with rule or Done when references. Main judgment is an independent acceptance check, not a replacement for the worker's review.
4. **Return bounded fixes to the same worker.** The main agent owns [remediation](../rules/execution.md#remediation), including analysis as needed and promotion of named fixes. This invocation authorizes that in-scope loop. Repeat the same worker's scoped review and main judgment until accepted or blocked; do not add a generic reviewer per slice. If the worker cannot resume, give a replacement its bounded contribution, current contract and evidence.

Workers may raise questions whenever blocked or a ticket deviation is needed. The main agent batches user-owned decisions under [Asking the user](../rules/writing-style.md#asking-the-user). Look up repository facts; do not guess approvals. Pause affected work while a required answer is pending. Record an approved change as the current decision, and refresh affected briefs before work resumes. Do not silently rewrite the source ticket or carry superseded options as current requirements.

## Recovery and limits

- **Verification finds a code defect:** assign the bounded fix to its responsible worker, repeat the slice loop, then combined review and main judgment before running verification again on the changed result. A newly requested test still needs acceptance; changing an accepted assertion still needs the user's decision.
- **Evidence, blockers and resume:** follow shared [handoffs and evidence](../rules/execution.md#handoffs-and-evidence) and [recovery and completion](../rules/execution.md#recovery-and-completion). Keep the process record consistent with actual state.
- **No subagents available:** report that the requested worker workflow is unavailable and ask whether to use a serial alternative. Do not silently claim the multi-agent gates ran.

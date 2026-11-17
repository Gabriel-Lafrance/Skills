---
name: gabriel-mode
description: Use when the user invokes /gabriel-mode or asks to run a precise ticket through worker subagents with main-agent review of each slice. An unclear ticket goes to write-ticket; an ordinary build goes to task.
category: Code
---

# Gabriel mode

Build one already precise ticket through bounded worker slices.

Inspired by pstack's [poteto-mode](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/SKILL.md).

## Read when

- At entry: the ticket and relevant decisions, [`/task`](../task/SKILL.md), its [doctrine](../task/doctrine.md) and [reference](../task/reference.md), and the [execution context](../rules/planning.md#execution-context).
- Before a delegation or correctness decision: the applicable project rules. Pass those rule paths to workers. A verdict without checking the governing rules is incomplete.
- At each review or verification: [`/review`](../review/SKILL.md) or [`/verification`](../verification/SKILL.md), including their required reads.

## Local orchestration contract

Use the selected task route's contracts and standards, not a second complete `/task` run inside each worker. These differences apply only during an explicit `/gabriel-mode` run:

| Existing default | This run |
| --- | --- |
| `/task` builds its slices itself | Workers implement bounded slices; the main agent owns decomposition and acceptance. |
| Review and verification run together | Worker review, main slice judgment, combined review, main whole judgment, then verification, in that order. |
| Completion may lead to shipping | Stop at the ready-for-PR assessment. This invocation grants no shipping permission. |

A worker never owns the branch, ticket, or shipping. Do not commit, push, create a PR, merge, deploy, or install in this workflow.

## Process

1. **Establish the run.** Apply the shared [ready-ticket preflight](../rules/execution.md#ready-ticket-preflight) and [handoff contract](../rules/execution.md#handoffs-and-evidence), reading the ticket as [read-only context](../task/doctrine.md#ticket-context). Announce the current lock, decision sources and next phase.
2. **Track the run in chat.** Keep phase, slice owners and dependencies, evidence, fix backlog and drift in the [execution context](../rules/planning.md#execution-context), marking proposed changes apart from approved ones with their decision source.
3. **Decompose and build code.** Use the [slice split](../task/reference.md#slice-split) and [inline plan contract](../task/reference.md#inline-plan-contract), with the [planning rules](../rules/planning.md) for product plans. Apply the slice loop to each coding slice. Product workers write no tests. Work in dependency order; parallelize only independent slices with separate write ownership. Size delegation to the work and available harness, without fixed worker counts or model mandates.
4. **Review the combined result.** Once slices are accepted, run `/review` in local mode over all this run's changes, including tests and cross-slice seams, against the pinned run baseline. Use a fresh review subagent with the [combined review context](../review/contract.md#fresh-combined-review-context), including the whole ticket and factual slice evidence, without the implementation conversation or worker verdicts. The main agent then independently checks the actual combined diff for correctness and omissions against every Done when item and rule. Slice approvals alone cannot pass this gate. On a gap from either, return to decomposition with the bounded fix backlog, then review and judge the combined changes again. Test defects follow the test rules and route back to their test owner when authorized.
5. **Verify after whole approval.** Launch `/verification` in a fresh subagent only after the combined review and main judgment pass. Supply the whole contract, the tests the ticket specified or the user accepted, combined diff, evidence, and [selected verification scope](../rules/execution.md#verification-scope). It writes those accepted tests under [testing.md](../rules/testing.md) and proposes any others worth keeping. The main agent reads the evidence and judges it against the same project rules and Done when.
6. **Assess readiness.** Use the [`/task` completion summary](../task/reference.md#completion-summary), naming the checked revision and working diff, accepted tests, review findings, verification evidence, and remaining blockers. Say ready for PR only when the actual combined result meets the ticket, applicable gates passed, and no blocking finding is unresolved. Otherwise say blocked or incomplete and give the next action. Report any named user waiver separately from proof.

## Slice loop

1. **Brief the worker.** Use the shared [handoff contract](../rules/execution.md#handoffs-and-evidence), including the slice's reason, concrete approach, public entry and the current contract.
2. **Implement, then self-review.** The implementing worker follows the selected task route within that brief. The same worker invokes `/review` in local mode, scoped to its contribution and relevant callers: Standards and Spec depth for a new contribution, remediation mode for named fixes. Return its bounded diff, the [review output](../review/contract.md#review-output), checks and outcomes, omissions or blockers, and proposed execution context updates. It does not run an independent task lifecycle or ship.
3. **Judge in the main context.** Read the relevant diff and evidence, consult the applicable project rules, and check correctness and completeness against the slice contract. Do not accept the worker's verdict on trust. Record approval or specific gaps with rule or Done when references.
4. **Return bounded fixes to the same worker.** The main agent owns [remediation](../rules/execution.md#remediation). This invocation authorizes that in-scope loop. Repeat the same worker's scoped review and main judgment until accepted or blocked; add no generic reviewer per slice. If the worker cannot resume, give a replacement its bounded contribution, current contract and evidence.

Workers raise questions when blocked or when the ticket needs to change; the main agent batches user-owned decisions under [Asking the user](../rules/writing-style.md#asking-the-user). Record an approved change as the current decision and refresh affected briefs before work resumes. Never silently rewrite the source ticket or carry superseded options as current requirements.

## Recovery and limits

- **Verification finds a code defect:** assign the bounded fix to its responsible worker, repeat the slice loop, then combined review and main judgment before running verification again. A newly requested test still needs acceptance; changing an accepted assertion still needs the user's decision.
- **Evidence, blockers and resume:** follow shared [handoffs and evidence](../rules/execution.md#handoffs-and-evidence) and [recovery and completion](../rules/execution.md#recovery-and-completion).
- **No subagents available:** report that the requested worker workflow is unavailable and ask whether to use a serial alternative. Do not claim the multi-agent gates ran.

# Implement Flow

Use the shared [execution context](../pack-shared/execution-context.md). The
parent sends a complete [Worker Brief](../orchestrate/flow.md#worker-brief) in
chat; do not reconstruct intent from a workspace, plan, or agent-owned state.

## Read first

1. The inline outcome, Done when, non-goals, Ticket / PR, fixed point, locked
   decisions, Active Rules, current slice, write lane, and dependencies.
2. Only the named ticket / PR, relevant Git diff/history, repository code and
   rules, and repo paths listed in the brief.
3. `/taste`; for UI, the inline Design card and `/design` doctrine.

## Deliver one bounded slice

1. Stay in the write allowlist. Parallel work is safe only when the parent
   brief proves non-overlapping lanes and compatible interfaces.
2. Honor the inline Structure / Design decisions and Active Rules. If a
   required behavior-preserving move is in the brief, do it before feature
   code and show that the old observable behavior still holds.
3. Reuse existing services and primitives. Do not copy a known-wrong shape or
   invent a shared API, service, abstraction, or lane. Return the smallest
   viable option as a finding when the slice needs one.
4. Gather only slice-local evidence needed for Completion: existing terminal
   output first, then a narrow relevant command if needed.
5. Do not run `/validate` or `/code-review`; the parent integrates Completion
   reports and owns those gates. Do not update tickets, registries, status, or
   other agent bookkeeping.
6. Do not write or edit tests. `/create-test` follows a parent review
   recommendation when needed.

## Completion

End with only the [`## Completion` envelope](../pack-shared/execution-context.md#worker-handoff):
status, scope, evidence, findings, and handoff. Do not append Progress,
workspace status, or a validation/review report.

## Escalation

If acceptance, dependencies, behavior, or a structural decision is missing,
return `blocked` with the smallest decision or interface the parent must
provide. The parent updates the inline context or asks the user; the worker
does not create a plan or hidden artifact.

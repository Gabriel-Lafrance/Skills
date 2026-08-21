---
name: implement
description: >-
  Implement one bounded worker slice from the parent’s inline execution
  context.
disable-model-invocation: true
---

# Implement

**Must read:** [../pack-shared/standards.md](../pack-shared/standards.md) — Read `/taste` and `/architecture` doctrines this turn before writing code. Do not skip.

**Ask style:** [../pack-shared/asking.md](../pack-shared/asking.md)

This skill is a worker step for `/task` or `/just-do-it`, not a typical user start.
You own **how**. The parent sends **what** and need-to-know, not a recipe.

Use the shared [execution context](../pack-shared/execution-context.md). The
parent sends a complete [Worker Brief](../pack-shared/subagents.md#worker-brief) in
chat; do not reconstruct intent from a workspace, plan, or agent-owned state.
Fail the job if taste or architecture bars are skipped.

## Read first

1. `/taste` and `/architecture` doctrines (keep it simple + named principles +
   structure). For UI, follow taste React & UI guidance.
2. The inline outcome, Done when, non-goals, Ticket / PR, fixed point, locked
   decisions, Active Rules, current slice, write lane, and dependencies.
3. Only the named ticket / PR, relevant Git diff/history, repository code and
   rules, and repo paths listed in the brief.

## Deliver one bounded slice

1. Stay in the write allowlist. Parallel work is safe only when the parent
   brief proves non-overlapping lanes and compatible interfaces.
2. Honor the inline Structure decisions and Active Rules. If a
   required behavior-preserving move is in the brief, do it before feature
   code and show that the old observable behavior still holds. Apply `/taste`
   implement self-check and `/architecture` self-check before Completion.
3. Reuse existing services and primitives. Do not copy a known-wrong shape or
   invent a shared API, service, abstraction, or lane. Return the smallest
   viable option as a finding when the slice needs one.
4. Gather only slice-local evidence needed for Completion: existing terminal
   output first, then a narrow relevant command if needed.
5. Do not run acceptance evidence or `/code-review`; the parent integrates
   Completion reports and owns those gates. Do not update tickets, registries,
   status, or other agent bookkeeping.
6. Do not write or edit tests. Only `/create-test` writes tests, and only
   after the user starts it.

## Completion

End with only the [`## Completion` envelope](../pack-shared/execution-context.md#worker-handoff):
status, scope, evidence, **Taste / architecture:** `applied`, findings, and
handoff. Skip on that mark is a fail. Do not append Progress, workspace
status, or a validation/review report.

## Escalation

If acceptance, dependencies, behavior, or a structural decision is missing,
return `blocked` with the smallest decision or interface the parent must
provide. The parent updates the inline context or asks the user; the worker
does not create a plan or hidden artifact.

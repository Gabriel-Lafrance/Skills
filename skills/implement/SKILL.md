---
name: implement
description: >-
  Implement one bounded worker slice from the parent’s inline execution
  context.
disable-model-invocation: true
---

# Implement

Implement one bounded non-UI slice for `/task` (a worker step, not a typical user start). You own **how**; the parent sends **what** and need-to-know in a complete [Worker Brief](../pack-shared/subagents.md#worker-brief), not a recipe. Do not reconstruct intent from a workspace, plan, or agent-owned state.

User-facing UI is `/design`. If this brief's write allowlist is screens,
components, styling, or visible copy, return `blocked` and tell the parent
to dispatch `/design` instead.

## Read when

- Before writing code: [code-quality.md](../rules/code-quality.md) and [code-structure.md](../rules/code-structure.md) ([standards.md](../pack-shared/standards.md)). Skipping taste or architecture bars fails the job.
- Every run: the inline outcome, Done when, non-goals, Ticket / PR, fixed
  point, locked decisions, rules that must stay true, current slice, write
  lane, and dependencies from the shared [execution context](../pack-shared/execution-context.md).
- As needed, only: the named ticket / PR, relevant Git diff/history,
  repository code and rules, and repo paths listed in the brief.
- Before asking the parent a question: [asking.md](../pack-shared/asking.md).

## Process

1. Stay in the write allowlist. Parallel work is safe only when the parent
   brief proves non-overlapping lanes and compatible interfaces.
2. Honor the inline Structure decisions and rules that must stay true. Create the
   owning folder from the folder map **before** writing files
   (`architecture:folders`). Do not add new files as mixed siblings in
   `src/`, `app/`, `convex/`, or any other mixed parent. If a
   required behavior-preserving move is in the brief, do it before feature
   code and show that the old observable behavior still holds. Apply the checklist in [code-quality.md](../rules/code-quality.md) and the self-check in [code-structure.md](../rules/code-structure.md) before Completion.
3. Reuse existing services and primitives. Do not copy a known-wrong shape or
   invent a shared API, service, abstraction, or lane. Return the smallest
   viable option as a finding when the slice needs one. Before adding an
   environment variable, inventory existing names and jobs (`taste:reuse-env`).
   If `SITE_URL` already holds the public site URL, read it; do not create
   `FRONTEND_URL`.
4. Gather only slice-local evidence needed for Completion: existing terminal
   output first, then a narrow relevant command if needed.
5. Do not run acceptance evidence or `/review`; the parent integrates
   Completion reports and owns those gates. Do not update tickets, registries,
   status, or other agent bookkeeping.
6. Do not write or edit tests. An accepted lock is a later `/task` slice that
   summons `tester` through `/create-test`.

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

---
name: just-do-it
description: >-
  Autonomously turn a Linear ticket into a typed branch, reviewed implementation,
  and visible GitHub PR. Carries safety and review state in chat execution
  context. Use when the user wants ticket-to-PR execution.
disable-model-invocation: true
---

# Just Do It

**Must read:** [../pack-shared/standards.md](../pack-shared/standards.md) — Read `/taste` and `/architecture` doctrines this turn before analyze, build, or review. Do not skip. For user-facing work also load `/design` and `docs/design.md`.

**Read:** [doctrine.md](doctrine.md) · [reference.md](reference.md) · [../pack-shared/execution-context.md](../pack-shared/execution-context.md) · [../pack-shared/pr-ship.md](../pack-shared/pr-ship.md) · [../publish/doctrine.md](../publish/doctrine.md) · [../publish/reference.md](../publish/reference.md) · **Ask style:** [../pack-shared/asking.md](../pack-shared/asking.md)

This skill is a user start. Do not nest it under `/task`. Parent orchestrator
only. Dispatch Task workers per
[../pack-shared/subagents.md](../pack-shared/subagents.md) and review their
Completions; do not solo non-trivial labor, grep the tree, or write tests. It
takes recommended soft decisions, auto-fixes only named Fix-now blockers, keeps
optional improvements as follow-ups, and leaves `/pr-review` to a human.

## Lifecycle

1. Resolve the Linear ticket through read-only `/trackers` and open the parent
   execution context.
2. Create a typed branch after git hard stops pass.
3. Run `/analyze` (this parent owns the next step), then `/task` for the
   bounded build (`/task` returns evidence; this parent owns shipping).
   Pick specialists from [subagents.md](../pack-shared/subagents.md); do not
   follow a fixed spawn order.
4. Checkpoint-commit the working tree; pin `baseSha...headSha`. Run
   `/code-review` (CR1); remediate Fix-now with `/analyze` + `/task`
   Fix mode; checkpoint before each re-review.
5. Checkpoint if dirty; run a fresh `/code-review` (CR2) against the pinned
   fixed point; remediate the same way.
6. Ship commit(s) if needed, preflight, print the full PR draft in chat, then
   push and create the PR (opened, not merged) using
   [pr-ship.md](../pack-shared/pr-ship.md) — screenshots, review canvas, and
   Cursor’s pull-request tool when available. Do not skip that contract because
   this skill is not `/publish`.

Hard stops, review caps, shipping, context handoffs, and new-chat recovery live
in the doctrine and reference.

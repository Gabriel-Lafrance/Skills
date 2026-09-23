---
name: just-do-it
description: >-
  Autonomously turn a Linear ticket into a typed branch, reviewed implementation,
  and visible GitHub PR. Carries safety and review state in chat execution
  context. Use when the user wants ticket-to-PR execution.
disable-model-invocation: true
---

# Just Do It

**Must read:** [../pack-shared/standards.md](../pack-shared/standards.md). Apply the **Taste** and **Architecture** sections of `AGENTS.md` this turn before analyze, build, or review. Do not skip. For user-facing work also follow the App UX section of `AGENTS.md` and `docs/design.md`. The designer owns that UI.

**Read:** [doctrine.md](doctrine.md) · [reference.md](reference.md) · [../pack-shared/execution-context.md](../pack-shared/execution-context.md) · [../pack-shared/pr-ship.md](../pack-shared/pr-ship.md) · [../publish/doctrine.md](../publish/doctrine.md) · [../publish/reference.md](../publish/reference.md) · **Ask style:** [../pack-shared/asking.md](../pack-shared/asking.md)

This skill is a user start. Do not nest it under `/task`. Parent orchestrator
only. Dispatch specialists per
[../pack-shared/subagents.md](../pack-shared/subagents.md) (the harness
specialist tool when it has one, otherwise that role as its own pass) and review their
Completions; do not solo non-trivial labor, grep the tree, or write tests. It
takes recommended soft decisions, auto-fixes only named Fix-now blockers, keeps
optional improvements as follow-ups, and leaves `/pr-review` to a human. The
`/task` behavior-lock question is not a soft decision: wait, and the user may
refuse every test.

## Lifecycle

1. Read the Linear ticket with that tracker's read API and open the parent
   execution context. Do not change status, comment, or close unless the user asks in that turn.
2. Create a typed standalone branch after git hard stops pass (`git switch --detach <base-sha>`, then `git switch -c`, or `--no-track`). It must not track `dev`, `main`, or `master`.
3. Run `/analyze` (this parent owns the next step), then `/task` for the
   bounded build (`/task` returns evidence; this parent owns shipping).
   Pick specialists from [subagents.md](../pack-shared/subagents.md); do not
   follow a fixed spawn order.
4. Checkpoint-commit the working tree without the CI mirror when that commit
   will not be pushed. If a PR is already open, run the mirror in
   [pr-ship.md](../pack-shared/pr-ship.md) first. Pin `baseSha...headSha`. Run
   `/code-review` (CR1); remediate Fix-now with `/analyze` + `/task`
   Fix mode; checkpoint before each re-review.
5. Checkpoint if dirty; run a fresh `/code-review` (CR2) against the pinned
   fixed point; remediate the same way.
6. Ship commit(s) if needed, run the CI mirror in
   [pr-ship.md](../pack-shared/pr-ship.md) before the push, preflight, print the full PR draft in chat, then
   push and create the PR (opened, not merged) using
   [pr-ship.md](../pack-shared/pr-ship.md) (the harness pull-request tool when
   it has one, otherwise `gh`). Do not skip that contract because
   this skill is not `/publish`.

Hard stops, review caps, shipping, context handoffs, and new-chat recovery live
in the doctrine and reference.

---
name: just-do-it
description: >-
  Autonomously turn a Linear ticket into a typed branch, reviewed implementation,
  and visible GitHub PR. Carries safety and review state in chat execution
  context. Use when the user wants ticket-to-PR execution.
disable-model-invocation: true
---

# Just Do It

**Variants:** [../pack-shared/variants.md](../pack-shared/variants.md) — standalone-only. If flow is requested, use the no-flow message.

**Read:** [doctrine.md](doctrine.md) · [reference.md](reference.md) · [../pack-shared/execution-context.md](../pack-shared/execution-context.md) · [../publish/doctrine.md](../publish/doctrine.md) · [../publish/reference.md](../publish/reference.md) · **Ask style:** [../pack-shared/asking.md](../pack-shared/asking.md)

Standalone parent orchestrator only. It takes recommended soft decisions,
auto-fixes only named Fix-now blockers, keeps optional improvements as
follow-ups, and leaves `/pr-review` to a human.

## Lifecycle

1. Resolve the Linear ticket through read-only `/trackers` and open the parent
   execution context.
2. Create a typed branch after git hard stops pass.
3. Run **flow** `/analyze`, then **flow** `/goal` for the bounded build.
4. Checkpoint-commit the working tree; pin `baseSha...headSha`. Run flow
   `/code-review` (CR1); remediate Fix-now with flow `/analyze` + flow `/goal`
   Fix mode; checkpoint before each re-review.
5. Checkpoint if dirty; run standalone `/code-review` (CR2) against the pinned
   fixed point; remediate the same way.
6. Ship commit(s) if needed, preflight, print the full PR draft in chat, then
   push and create the PR (opened, not merged).

Hard stops, review caps, shipping, context handoffs, and new-chat recovery live
in the doctrine and reference.

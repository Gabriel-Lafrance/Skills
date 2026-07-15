---
name: trackers-flow
description: >-
  Goal-scoped Linear/GitHub fetch and ACHIEVED close-out for ticket-driven
  goals under .agents/temp/goals/<goal-id>/. Looked up by /goal. Not for
  auto-invocation — use /trackers for ad-hoc issue work.
disable-model-invocation: true
---

# Trackers Flow

Ticket ops **inside an active `/goal`**. Detect/fetch/normalize/close-out doctrine lives in **`/trackers`** — follow it.

## Preconditions

1. Resolve **`goal-id`** and ticket id from GOAL / user
2. Fetch **before** planning; still grill open product decisions via `/grill-me-flow`
3. Close-out **only** after `/validate-flow` pass (and usually `/code-review-flow`)

## Process

1. **Start:** fetch → ticket brief → store link in `GOAL.md` (not full body spam).
2. **While running:** brief is spec for `/create-plan-flow` / `/validate-flow` / `/code-review-flow`; optional In Progress once.
3. **ACHIEVED:** `/trackers` close-out steps → then `/goal` deletes workspace.

## Anti-patterns

- Closing before validate evidence
- Inventing AC from the id alone
- Using this outside a goal for casual issue edits — use `/trackers`

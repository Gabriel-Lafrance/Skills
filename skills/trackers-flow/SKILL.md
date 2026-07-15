---
name: trackers-flow
description: >-
  Goal-scoped read-only Linear/GitHub fetch into a ticket brief for
  .agents/temp/goals/<goal-id>/. Looked up by /goal and other *-flow callers.
  Never invoke alone; never write or close-out tickets.
disable-model-invocation: true
---

# Trackers Flow

Read-only ticket context **inside an active `/goal`**. Fetch/normalize doctrine lives in **`/trackers`** — follow it (including the **never write** rule).

## Preconditions

1. Resolve **`goal-id`** and ticket/PR id from GOAL / user
2. Caller is `/goal` or another `*-flow` skill — not a standalone user slash for “update Linear”
3. Fetch **before** planning; still grill open product decisions via `/grill-me-flow`

## Process

1. **Fetch** via `/trackers` (issue + comments + linked PR/QA when present).
2. Store **link** (+ short Ask pointer) in `GOAL.md` — not full-body spam.
3. Brief is Spec / Done when source for `/create-plan-flow`, `/validate-flow`, `/code-review-flow`.
4. **Never** set In Progress, comment, close, or ACHIEVED close-out. Ticket close is manual / user’s PR flow after `/goal` announces ACHIEVED.

## Anti-patterns

- Any tracker write
- Inventing AC from the id alone
- Invoking this outside a goal for casual issue edits — still read-only via `/trackers`, and only as a callee of another skill

---
name: grill-me-flow
description: >-
  Goal-scoped grill: hard gate before plans under
  .agents/temp/goals/<goal-id>/. Writes GRILL.md and waits for shared
  understanding. Looked up by /goal. Not for auto-invocation — use /grill-me
  outside a goal.
disable-model-invocation: true
---

# Grill Me Flow

Interview **inside a `/goal` workspace**. Question style lives in **`/grill-me`** — follow it.

## Preconditions

1. Resolve **`goal-id`**
2. Workspace: `.agents/temp/goals/<goal-id>/` with draft `GOAL.md` / `STATUS.md`
3. Hard gate before any `plans/*` exist

## Process

1. Run the full `/grill-me` interview.
2. Persist locked answers in `.agents/temp/goals/<goal-id>/GRILL.md`.
3. Update `GOAL.md` Done when / Constraints from the grill.
4. Set `STATUS.md` `last: grilling` until confirmed.
5. **Stop** for explicit shared understanding — wait for yes.
6. **Never** write `plans/*` before that yes. Return to `/goal` Phase 1 (`/create-plan-flow` + INDEX).

## Anti-patterns

- Writing plans before shared-understanding yes
- Using this outside a goal workspace — use `/grill-me`

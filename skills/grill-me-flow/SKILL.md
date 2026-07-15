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

Interview **inside a `/goal` workspace**. Doctrine (question style, one-at-a-time, recommended answer first) lives in **`/grill-me`** — follow it.

## Preconditions

1. Resolve **`goal-id`**
2. Workspace: `.agents/temp/goals/<goal-id>/` with draft `GOAL.md` / `STATUS.md`
3. This is the **hard gate** before any `plans/*` exist

## Process

1. Run the full `/grill-me` interview (outcome, non-goals, users, edges, entry shape, data/scale, plan count, file lanes).
2. Persist locked answers in `.agents/temp/goals/<goal-id>/GRILL.md` as you go (or once before confirm).
3. Update `GOAL.md` Done when / Constraints from the grill.
4. Set `STATUS.md` `last: grilling` until confirmed.
5. **Stop** for explicit shared understanding — e.g. “Shared understanding — ready to write N plans?” Wait for yes.
6. **Never** write `plans/*` before that yes. Then return to `/goal` Phase 1 (`/create-plan-flow` + INDEX).

## Anti-patterns

- Writing plans before shared-understanding yes
- Skipping grill on fuzzy/product work (unless `/goal` skip rule applies)
- Using this outside a goal workspace — use `/grill-me`

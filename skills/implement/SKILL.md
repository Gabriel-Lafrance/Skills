---
name: implement
description: >-
  Orchestrate implementation from .scratch/goals/<goal-id>/PLAN.md using Task
  subagents scoped to that workspace so concurrent goals do not clash. Use under
  /goal, after /create-plan, or when given a goal-id.
disable-model-invocation: true
---

# Implement

Build from **one** goal workspace. Follow **`/orchestrate`**.

## Preconditions

1. Resolve **`goal-id`** (from `/goal` binding, user, or plan path). Read:
   - `.scratch/goals/<goal-id>/PLAN.md`
   - `.scratch/goals/<goal-id>/GOAL.md`
2. If PLAN missing and non-trivial → `/create-plan` for **that** id
3. Stay in Agent mode
4. Read **`/taste`** (+ **`/design`** if UI)
5. Ticket without brief → `/trackers` fetch
6. Skim `.scratch/goals/REGISTRY.md` — if another `running` goal shares your File lane, serialize overlapping work

## Process

1. Structure/design gaps → `/architecture` / `/design` Mode B into **this** PLAN
2. Sibling cite → parallel `explore` (prompt includes this goal-id)
3. Slice → `/split-task` into `.scratch/goals/<goal-id>/pieces/` when needed
4. Dispatch `generalPurpose` workers — one slice each; parallel only if no file overlap **and** no conflict with other running goals
5. Integrate; enforce entry point + folders
6. Taste (+ design) check on merged diff
7. Verify via running stack (`/taste` Verify)
8. `/validate` for **this** goal-id
9. `/code-review` for **this** goal-id
10. Do not close tracker here
11. Commit only if user asked

## Cursor notes

- Every Task prompt: `goal-id` + this workspace paths + Touch only
- Never write another `.scratch/goals/<other-id>/`
- Update this `PLAN.md` if scope changes
- Default labor = subagents

## Done means

- `/validate` pass for this goal
- Taste / architecture / design checks pass
- No scope creep beyond this PLAN/GOAL

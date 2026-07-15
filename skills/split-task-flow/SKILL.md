---
name: split-task-flow
description: >-
  Goal-scoped split: turn grill output into multiple plans/INDEX rows under
  .agents/temp/goals/<goal-id>/. Looked up by /goal. Not for auto-invocation —
  use /split-task outside a goal.
disable-model-invocation: true
---

# Split Task Flow

Decomposition **inside a `/goal` workspace**. Smart-zone doctrine lives in **`/split-task`** — follow it.

## Preconditions

1. Resolve **`goal-id`**
2. Read `GOAL.md` + `GRILL.md`
3. Prefer **multiple `plans/NN-*.md` via `/create-plan-flow`** (update INDEX) over loose pieces; optional extras under `pieces/`

## Process

1. Capture parent from GOAL/GRILL (ticket id stays on every child if present — `/trackers-flow` brief as Ask).
2. Split ruthlessly into agent-sized pieces (smart zone from `/split-task`).
3. Write/update `plans/INDEX.md` with order + blockers.
4. Quiz once on INDEX granularity when more than one plan — then `/create-plan-flow` per row.
5. Do not `/implement-flow` until INDEX plans exist (unless user overrides).

## Hand-offs

- Still fuzzy → `/grill-me-flow`
- Plan files → `/create-plan-flow`
- Build → `/implement-flow`

---
name: repair-flow
description: >-
  Goal/implement-scoped repair under .agents/temp/goals/<goal-id>/ (and optional
  nested repairs/ note). Pessimistic hunt, grill what/how, acceptance, smallest
  fix, then validate-flow. Looked up by /goal and /implement-flow. Not for
  auto-invocation — use /repair outside a goal.
disable-model-invocation: true
---

# Repair Flow

Bug hunt **inside a `/goal` / `/implement-flow` lane**. Full doctrine in **`/repair`** — pessimistic framing, grill before cut, acceptance, smallest footprint, then validate.

## Preconditions

1. Resolve **`goal-id`** + active `plans/NN-*.md` / file lane
2. Read `GOAL.md`, `GRILL.md`, that plan
3. Ticket via **`/trackers-flow`** if present
4. Stay in this goal’s lane

## State (goal-nested)

Prefer a short repair note under the goal workspace so `/validate-flow` can find criteria:

```text
.agents/temp/goals/<goal-id>/
  repairs/
    <repair-id>/
      BUG.md
      GRILL.md
      ACCEPTANCE.md
      STATUS.md
      FIX.md
```

Also fine to use top-level `.agents/temp/repairs/<repair-id>/` and link it from `STATUS.md` — but keep the **file lane** of the parent plan.

## Process

1. Hunt pessimistically (`/repair` framing) inside the lane.
2. Classify Local / Narrow / Massive.
3. **Massive:** escalate (new `/goal` or `/split-task-flow` + plans) — do not sprawl.
4. **Local/Narrow:**
   - `/grill-me-flow` (or `/grill-me` topics) on what/how to fix — recommended = smallest patch
   - Write `ACCEPTANCE.md`
   - Apply smallest fix
   - **`/validate-flow`** against that `ACCEPTANCE.md` **plus** relevant plan/GOAL criteria touched by the fix
5. Fail validate → repair again or escalate if scope exploded.
6. Pass → return to `/implement-flow` / `/goal` wave (later full-goal validate + code-review still required for ACHIEVED).

## Worker note

Task workers: **`/orchestrate-flow`** — omit `model`; include goal-id, plan, lane, acceptance path, “smallest footprint only.”

## Anti-patterns

- Patching without grill + acceptance
- Skipping validate after the fix
- Using this with no goal — use `/repair`
- Closing trackers

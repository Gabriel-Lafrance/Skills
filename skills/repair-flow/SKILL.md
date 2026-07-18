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

Bug hunt **inside a `/goal` / `/implement-flow` lane**. Read [../repair/doctrine.md](../repair/doctrine.md). Ask style: [../asking.md](../asking.md).

## Preconditions

1. Resolve **`goal-id`** + active `plans/NN-*.md` / file lane
2. Read `GOAL.md`, `GRILL.md`, that plan
3. Ticket via **`/trackers-flow`** if present
4. Stay in this goal's lane

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

1. Hunt pessimistically (doctrine framing) inside the lane.
2. Classify Local / Narrow / Massive.
3. **Massive:** escalate (new `/goal` or `/split-task-flow` + plans) — do not sprawl.
4. **Local/Narrow:** grill → `ACCEPTANCE.md` → smallest fix → **`/validate-flow`** (+ relevant plan/GOAL criteria)
5. Fail validate → repair again or escalate if scope exploded.
6. Pass → return to `/implement-flow` / `/goal` wave.

## Worker note

Task workers: **`/orchestrate-flow`** — omit `model`; include goal-id, plan, lane, acceptance path, "smallest footprint only."

## Anti-patterns

- Patching without grill + acceptance
- Skipping validate after the fix
- Using this with no goal — use `/repair`
- Closing trackers

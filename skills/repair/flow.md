# Repair Flow

Bug hunt **inside a `/goal` / `/implement` lane**. Read [./doctrine.md](./doctrine.md). Ask style: [../asking.md](../asking.md).

## Preconditions

1. Resolve **`goal-id`**, `goal_root` per [../workspace-roots.md](../workspace-roots.md), and the active `plans/NN-*.md` / file lane
2. Read `<goal-root>/GOAL.md`, `<goal-root>/GRILL.md`, and that plan
3. Ticket via **`/trackers`** if present
4. Stay in this goal's lane

## State (goal-nested)

Prefer a short repair note under the goal workspace so `/validate` can find criteria:

```text
<goal-root>/
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
3. **Massive:** escalate (new `/goal` or `/split-task` + plans) — do not sprawl.
4. **Local/Narrow:** grill → `ACCEPTANCE.md` → smallest fix → **`/validate`** (+ relevant plan/GOAL criteria)
5. Fail validate → repair again or escalate if scope exploded.
6. Pass → return to `/implement` / `/goal` wave.

## Worker note

Task workers: **`/orchestrate`** — omit `model`; include goal-id, resolved goal-root, plan, lane, acceptance path, "smallest footprint only."

## Anti-patterns

- Patching without grill + acceptance
- Skipping validate after the fix
- Closing trackers

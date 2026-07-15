---
name: implement
description: >-
  Orchestrate implementation from a plan file under
  .agents/temp/goals/<goal-id>/plans/NN-*.md using Task subagents scoped to that
  plan’s file lane. Agents may auto-invoke. Use when given goal-id + plan path
  outside the /goal loop. Under /goal use /implement-flow.
---

# Implement

Build from **one plan file** inside a goal workspace. Follow **`/orchestrate`**.

Inside an active `/goal` loop, use **`/implement-flow`** instead.

## Preconditions

1. Resolve **`goal-id`** and **plan file** (`plans/NN-*.md` or frontier from `plans/INDEX.md`)
2. Read `GOAL.md`, `GRILL.md` (if any), that plan file, `plans/INDEX.md`
3. `/taste` (+ `/design` if UI); ticket brief via `/trackers` if needed
4. REGISTRY: serialize if another running goal shares File lane

## Process

1. Structure/design gaps → update **this** plan via `/architecture` / `/design`
2. Dispatch `generalPurpose` for this plan (parallel only across non-overlapping plans)
3. Integrate; mark INDEX row status
4. Taste check; verify via **existing terminals** (`/taste` Verify) — **no** Convex MCP ritual
5. `/validate` / `/code-review` when this plan (or wave) is done — prefer terminals over MCP
6. No tracker close here; commit only if asked

## Notes

- Paths: `.agents/temp/goals/<goal-id>/…` only
- One plan file per worker prompt
- Never write another goal-id’s tree
- After a slice: one terminals glance is enough if `convex dev` is quiet/green

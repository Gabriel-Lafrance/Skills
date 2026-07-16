---
name: implement-flow
description: >-
  Internal implement: frontier workers from plans/INDEX under
  .agents/temp/goals/<goal-id>/. Looked up by /goal only. Never for users or
  auto-invocation.
disable-model-invocation: true
---

# Implement Flow

Build from **one plan file** inside a goal workspace. Follow **`/orchestrate-flow`**.

## Preconditions

1. Resolve **`goal-id`** and **plan file** (`plans/NN-*.md` or frontier from `plans/INDEX.md`)
2. Read `GOAL.md`, `GRILL.md` (if any), that plan file, `plans/INDEX.md`
3. `/taste-flow` (+ `/design-flow` if UI); ticket brief via `/trackers-flow` if needed
4. REGISTRY: serialize if another running goal shares File lane

## Process

1. Structure/design gaps → update **this** plan via `/architecture-flow` / `/design-flow`
2. Dispatch `generalPurpose` for this plan (parallel only across non-overlapping plans). **Omit Task `model`** — inherit parent (see `/orchestrate-flow`)
3. Integrate; mark INDEX row status
4. Taste check; verify via **existing terminals** (`/taste-flow` Verify) — **no** Convex MCP ritual
5. Bugs mid-slice → **`/repair-flow`** (pessimistic hunt → grill what/how → acceptance → smallest fix → **`/validate-flow`**)
6. `/validate-flow` / `/code-review-flow` when this plan (or wave) is done — prefer terminals over MCP
7. No tracker close here; commit only if asked

## Notes

- Paths: `.agents/temp/goals/<goal-id>/…` only
- One plan file per worker prompt
- Never write another goal-id’s tree
- After a slice: one terminals glance is enough if `convex dev` is quiet/green

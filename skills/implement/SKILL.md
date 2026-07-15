---
name: implement
description: >-
  Orchestrate implementation from
  .agents/temp/goals/<goal-id>/plans/NN-*.md using Task subagents scoped to that
  plan’s file lane. Use under /goal after plans exist, or when given goal-id +
  plan path.
disable-model-invocation: true
---

# Implement

Build from **one plan file** inside a goal workspace. Follow **`/orchestrate`**.

## Preconditions

1. Resolve **`goal-id`** and **plan file** (`plans/NN-*.md` or frontier from `plans/INDEX.md`)
2. Read `GOAL.md`, `GRILL.md` (if any), that plan file, `plans/INDEX.md`
3. Under `/goal`: refuse to implement if grill never completed / no plans yet → send back to `/goal` Phase 0–1b
4. `/taste` (+ `/design` if UI); ticket brief via `/trackers` if needed
5. REGISTRY: serialize if another running goal shares File lane

## Process

1. Structure/design gaps → update **this** plan via `/architecture` / `/design`
2. Dispatch `generalPurpose` for this plan (parallel only across non-overlapping plans)
3. Integrate; mark INDEX row status
4. Taste check; verify via **existing terminals** (`/taste` Verify) — **no** Convex MCP ritual
5. When implementing under `/goal`, continue frontier plans until INDEX done or hand back to `/goal`
6. `/validate` / `/code-review` at goal level when all frontier work for this wave is done (or per `/goal`) — validate must also prefer terminals over MCP
7. No tracker close here; commit only if asked

## Notes

- Paths: `.agents/temp/goals/<goal-id>/…` only
- One plan file per worker prompt
- Never write another goal-id’s tree
- After a slice: one terminals glance is enough if `convex dev` is quiet/green

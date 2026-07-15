---
name: design-flow
description: >-
  Goal-scoped UI craft: write a Design card into plans under
  .agents/temp/goals/<goal-id>/ when creating or changing UI. Looked up by
  /goal, /create-plan-flow, /implement-flow. Not for auto-invocation — use
  /design for standalone polish outside a goal.
disable-model-invocation: true
---

# Design Flow

UI craft **inside a `/goal` workspace**. Doctrine lives in **`/design`** — follow it; do not restate it here.

Examples: [examples.md](examples.md) (same folder) or [../design/examples.md](../design/examples.md).

## Preconditions

1. Resolve **`goal-id`**
2. Workspace exists: `.agents/temp/goals/<goal-id>/`
3. Read `GOAL.md`, `GRILL.md`, and the target `plans/NN-*.md`

If there is no goal workspace, stop and use **`/design`** (standalone) or start `/goal`.

## Process

When the work **creates or substantially changes** UI:

1. Before coding pixels: write a tiny **Design card** (fold into the plan via `/create-plan-flow`):

```markdown
## Design
**Job of this screen:** one sentence
**Primary action:** …
**Hierarchy:** what is top / mid / background
**Surfaces:** bg-dark / bg / bg-light (or token names)
**Depth:** which elements raise vs recess
**States:** buttons/inputs that need default·hover·active·disabled (+ loading/error if relevant)
**Psychology (if flow):** defaults / progress / reciprocity / endowment — ethical only
**Out of scope visually:** …
```

2. Implement against that card; mobile first (`/taste-flow` + `/design` doctrine).
3. Validate visually via localhost; taste self-check still applies.
4. Stay within `GOAL.md` / this plan’s file lane.

## Hand-offs

- Structure → `/architecture-flow`
- Style → `/taste-flow`
- After build → `/validate-flow`

# Create Plan Flow

Write **one** plan file **inside an active `/goal`**. Stay in **Agent mode** — no `SwitchMode`, no CreatePlan UI.

**Internal only** — looked up by `/goal`. There is no standalone `/create-plan`; start `/goal` to plan and build.

## Location

```text
.agents/temp/goals/<goal-id>/plans/<NN>-<slug>.md
.agents/temp/goals/<goal-id>/plans/INDEX.md    # update when adding a plan
```

- `<NN>`: `01`, `02`, … dependency order (blockers first)
- If only one plan: still use `plans/01-<slug>.md` (not a root `PLAN.md`)
- **Never** use `.scratch/` or a global ACTIVE plan file

## Preconditions

1. Resolve **`goal-id`**
2. Grill shared understanding yes (`GRILL.md` present) — else `/grill-me`
3. Stay in Agent mode — no `SwitchMode`, no CreatePlan UI

## Process

### 1. Context

Read `GOAL.md` + `GRILL.md`. Also read `.agents/temp/grills/language.md`, `choice.md`, `rules.md` when present — use those terms in Overview/Approach/AC; honor choices and rules.

1. `/orchestrate`, `/taste`, ticket → `/trackers`
2. Explore if needed; `/architecture` (+ `/design` if UI) into Structure/Design

### 2. Write the plan file

```markdown
# <title>

**Status:** pending
**Updated:** <ISO>
**Goal id:** <goal-id>
**Plan file:** `.agents/temp/goals/<goal-id>/plans/<NN>-<slug>.md`
**Blocked by:** <none | 01-…>

## Overview
…

## Problem
…

## Approach
<concrete; /taste; no Option A/B>

## Structure
…

## Design
<n/a or Design card>

## Key files
- …

## File lane
Paths this plan may write

## Seams / verification
…

## Acceptance criteria
- [ ] … (when structure is in play: callers stay thin; complexity behind service X; no entropy growth in touched lane)

## Out of scope
…

## Todos
- [ ] …
```

Update `plans/INDEX.md` row for this NN. Bump `STATUS.md` (`last: plan NN written`).

### 3. Continue

Once per INDEX row until complete — then `/implement` for frontier plans.

### 4. Subagents

Task prompts: `goal-id` + `GOAL.md` + **this** `plans/NN-*.md`.

## Anti-patterns

- Planning before grill yes
- Never `.scratch/` or root `PLAN.md`
- Single root `PLAN.md` when INDEX has multiple slices
- `SwitchMode` / CreatePlan UI
- Coding the feature here
- Invoking this outside `/goal` as a user-facing skill

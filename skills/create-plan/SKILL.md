---
name: create-plan
description: >-
  Write one implementation plan file under
  .agents/temp/goals/<goal-id>/plans/NN-slug.md (multi-plan friendly). Stays in
  Agent mode. Use after /grill-me under /goal, or when planning a slice.
disable-model-invocation: true
---

# Create Plan

Write **one** plan file into a goal workspace. Stay in **Agent mode** — no `SwitchMode`, no CreatePlan UI.

Under `/goal`, plans are written **only after** grill shared understanding (see `/goal` Phase 0).

## Location

```text
.agents/temp/goals/<goal-id>/plans/<NN>-<slug>.md
.agents/temp/goals/<goal-id>/plans/INDEX.md    # update when adding a plan
```

- `<NN>`: `01`, `02`, … dependency order (blockers first)
- If only one plan for the whole goal: still use `plans/01-<slug>.md` (not a root `PLAN.md`)
- Standalone (no goal yet): allocate `goal-id`, create workspace + minimal `GOAL.md`/`STATUS.md`, upsert `REGISTRY.md`, then write the plan
- **Never** use `.scratch/` or a global ACTIVE plan file

## Process

### 1. Context

Follow **`/orchestrate`**. Read `GOAL.md` + `GRILL.md` when present.

- `/taste`; ticket → `/trackers` brief
- Parallel `explore` if not already done this goal
- `/architecture` (+ `/design` Mode B if UI) into this plan’s Structure/Design

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
<n/a or Mode B>

## Key files
- …

## File lane
Paths this plan may write

## Seams / verification
…

## Acceptance criteria
- [ ] …

## Out of scope
…

## Todos
- [ ] …
```

Update `plans/INDEX.md` row for this NN. Bump `STATUS.md` (`last: plan NN written`).

### 3. Hand off

Announce the path. Under `/goal` / build requests: continue to next plan in INDEX or `/implement` for frontier plans. No confirmation UI.

Multiple plans: call this skill **once per INDEX row** (or batch writes in one turn) until INDEX is complete — then implement.

### 4. Subagents

Task prompts: `goal-id` + `GOAL.md` + **this** `plans/NN-*.md` (not every plan unless needed).

## Anti-patterns

- `.scratch/` paths
- Single root `PLAN.md` when INDEX has multiple slices
- Planning before grill yes (under `/goal`)
- `SwitchMode` / CreatePlan UI
- Coding the feature here

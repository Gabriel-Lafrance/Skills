---
name: create-plan
description: >-
  Write one implementation plan file under
  .agents/temp/goals/<goal-id>/plans/NN-slug.md (multi-plan friendly). Stays in
  Agent mode. Agents may auto-invoke. Use when planning a slice outside the
  /goal loop. Under /goal after grill use /create-plan-flow.
---

# Create Plan

Write **one** plan file into a goal workspace. Stay in **Agent mode** — no `SwitchMode`, no CreatePlan UI.

**Standalone** — for the active `/goal` loop after grill, use **`/create-plan-flow`**.

## Location

```text
.agents/temp/goals/<goal-id>/plans/<NN>-<slug>.md
.agents/temp/goals/<goal-id>/plans/INDEX.md    # update when adding a plan
```

- `<NN>`: `01`, `02`, … dependency order (blockers first)
- If only one plan: still use `plans/01-<slug>.md` (not a root `PLAN.md`)
- No goal yet: allocate `goal-id`, create workspace + minimal `GOAL.md`/`STATUS.md`, upsert `REGISTRY.md`, then write the plan
- **Never** use `.scratch/` or a global ACTIVE plan file

## Process

### 1. Context

Read `GOAL.md` + `GRILL.md` when present. Also read `.agents/temp/grills/language.md`, `choice.md`, `rules.md` when present — use those terms in Overview/Approach/AC; honor choices and rules.

- `/taste-flow`; ticket → `/trackers-flow` brief
- Parallel `explore` if needed
- `/architecture` (+ `/design` if UI) into this plan’s Structure/Design

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
<concrete; /taste-flow; no Option A/B>

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

### 3. Hand off

Announce the path. Continue to `/goal` if they want the full loop, or stop. No confirmation UI.

### 4. Subagents

Task prompts: `goal-id` + `GOAL.md` + **this** `plans/NN-*.md`.

## Anti-patterns

- `.scratch/` paths
- Single root `PLAN.md` when INDEX has multiple slices
- `SwitchMode` / CreatePlan UI
- Coding the feature here

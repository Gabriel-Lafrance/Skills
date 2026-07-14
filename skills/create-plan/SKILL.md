---
name: create-plan
description: >-
  Write an implementation plan into a goal workspace
  (.scratch/goals/<goal-id>/PLAN.md) so concurrent goals never clash. Stays in
  Agent mode. Use after grilling, under /goal, or when planning non-trivial work.
disable-model-invocation: true
---

# Create Plan

Write a durable plan file inside **one goal workspace**. Stay in **Agent mode** — no `SwitchMode`, no CreatePlan UI.

## Plan location

Under `/goal` (or when `goal-id` is known):

```text
.scratch/goals/<goal-id>/PLAN.md
```

Standalone (no goal yet): create a workspace first:

1. Allocate `goal-id` (same rules as `/goal`: ticket id, or slug + short suffix)
2. Create `.scratch/goals/<goal-id>/` and a minimal `GOAL.md` + `STATUS.md`
3. Upsert `.scratch/goals/REGISTRY.md`
4. Write `PLAN.md` there

**Never** write `.scratch/plans/ACTIVE.md` or any global singleton plan file.

If `PLAN.md` already exists for that id, replace it only for **this** id — leave other goals’ plans untouched.

## Process

### 1. Gather context (subagents explore; you decide)

Follow **`/orchestrate`**. Point explores at this goal’s `GOAL.md`.

- Read **`/taste`**
- Ticket in play → `/trackers` brief
- `CONTEXT.md` / ADRs if present
- Parallel `explore` Tasks: sibling, lane, seams
- Multi-file / UI → `/architecture` (+ `/design` Mode B if UI)

One clarifying question only if the entry shape is a real undecided product choice.

Do **not** implement feature code here.

### 2. Write PLAN.md

Path: `.scratch/goals/<goal-id>/PLAN.md`

```markdown
# <title>

**Status:** active
**Updated:** <ISO date>
**Goal id:** <goal-id>
**Goal / ticket:** <none | IN-1234 | #42 — URL>
**Path:** `.scratch/goals/<goal-id>/PLAN.md`

## Overview
<1–2 sentences>

## Problem
…

## Approach
<concrete; fits /taste; no Option A/B>

## Structure
<entry point, folder map, extension seam, Scalability>

## Design
<Mode B card or n/a>

## Key files
- [path](path) — why

## File lane (multi-goal)
Paths this goal may write (workers must stay inside; avoid other running goals’ lanes)

## Seams / verification
…

## Acceptance criteria
- [ ] …
- [ ] <scalable-data row when needed>

## Out of scope
…

## Todos
- [ ] …
```

Also bump `.scratch/goals/<goal-id>/STATUS.md` (`last: plan written`).

### 3. Hand off

Announce: `Plan written to .scratch/goals/<goal-id>/PLAN.md`.

**Under `/goal` or user asked to build:** continue to `/split-task` or `/implement` with that `goal-id`. No confirmation wait.

**Standalone “just plan”:** stop unless they ask to implement.

### 4. Subagent rule

Task prompts must say: read `.scratch/goals/<goal-id>/GOAL.md` and `PLAN.md` — **not** another id.

## Anti-patterns

- Global ACTIVE plan files
- Writing into the wrong `goal-id`
- `SwitchMode` / CreatePlan UI
- Plan only in chat
- Coding the feature in this skill
- Skipping acceptance criteria / folder map / entry point
- `{ success: false }` APIs, dynamic imports, Convex names with `-`/`_`

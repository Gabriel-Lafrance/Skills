---
name: create-plan-flow
description: >-
  Goal-scoped plan write: one plans/NN-slug.md under
  .agents/temp/goals/<goal-id>/ only after grill shared understanding. Looked up
  by /goal. Not for auto-invocation — use /create-plan outside the goal loop.
disable-model-invocation: true
---

# Create Plan Flow

Write **one** plan file **inside an active `/goal`**. Template and location rules live in **`/create-plan`** — follow them.

## Preconditions

1. Resolve **`goal-id`**
2. Grill shared understanding yes (`GRILL.md` present) — else send back to `/grill-me-flow`
3. Stay in Agent mode — no `SwitchMode`, no CreatePlan UI

## Process

1. Context: `/orchestrate-flow`, `/taste-flow`, ticket → `/trackers-flow`
2. Explore if needed; `/architecture-flow` (+ `/design-flow` if UI) into Structure/Design
3. Write `.agents/temp/goals/<goal-id>/plans/<NN>-<slug>.md` using the `/create-plan` template
4. Update `plans/INDEX.md` + `STATUS.md`
5. Call once per INDEX row (or batch in one turn) until INDEX complete — then `/implement-flow` for frontier plans

## Anti-patterns

- Planning before grill yes
- `.scratch/` or root `PLAN.md` instead of `plans/NN-*.md`
- Coding the feature here

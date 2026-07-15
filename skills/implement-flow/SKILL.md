---
name: implement-flow
description: >-
  Goal-scoped implement: frontier workers from plans/INDEX under
  .agents/temp/goals/<goal-id>/. Looked up by /goal after plans exist. Not for
  auto-invocation — use /implement for a single plan outside the loop.
disable-model-invocation: true
---

# Implement Flow

Build **inside an active `/goal`**. Worker rules live in **`/orchestrate-flow`**; single-plan process mirrors **`/implement`**.

## Preconditions

1. Resolve **`goal-id`** + plan file / INDEX frontier
2. Refuse if grill never completed / no plans yet → `/goal` Phase 0–1b
3. `/taste-flow` (+ `/design-flow` if UI); ticket → `/trackers-flow`
4. REGISTRY lane check

## Process

1. Gaps → `/architecture-flow` / `/design-flow` on **this** plan
2. Parallel `/orchestrate-flow` workers for non-overlapping frontier plans
3. Integrate; mark INDEX statuses
4. Verify via terminals (`/taste` Verify) — no Convex MCP ritual
5. Continue frontier until INDEX done or hand back to `/goal`
6. Wave done → `/validate-flow` / `/code-review-flow` per `/goal`

## Anti-patterns

- Implementing before grill/plans
- Workers missing goal-id / wrong plan file
- Touching another goal’s tree

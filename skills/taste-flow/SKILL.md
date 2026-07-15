---
name: taste-flow
description: >-
  Goal-scoped taste reminder: read /taste before plan/implement under
  .agents/temp/goals/<goal-id>/. Looked up by /goal and *-flow siblings. Not for
  auto-invocation — use /taste outside a goal.
disable-model-invocation: true
---

# Taste Flow

Style contract **inside a `/goal` workspace**. Full doctrine lives in **`/taste`** — read it (and [../taste/examples.md](../taste/examples.md) when unsure).

## Preconditions

1. Resolve **`goal-id`**
2. Before `/create-plan-flow`, `/implement-flow`, `/validate-flow`, or `/code-review-flow` on this goal: apply `/taste` non-negotiables + Verify (terminals first)

## Process

1. Paste or enforce taste into worker prompts (`/orchestrate-flow`).
2. Plans must include taste-relevant acceptance when structure/UI is in scope.
3. Each implement slice: run the implement self-check from `/taste`.
4. Failures are hard for `/validate-flow` and Standards in `/code-review-flow`.

## Hand-offs

- Structure → `/architecture-flow`
- UI → `/design-flow`

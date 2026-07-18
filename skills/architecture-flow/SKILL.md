---
name: architecture-flow
description: >-
  Goal-scoped structure card: domain services (public APIs), feature entry,
  folder map, behavior-preserving moves for prior mistakes, and write-path
  scale into plans under .agents/temp/goals/<goal-id>/. Looked up by /goal and
  create-plan-flow. Not for auto-invocation — use /architecture outside a goal.
disable-model-invocation: true
---

# Architecture Flow

Structure craft **inside a `/goal` workspace**. Read [../architecture/doctrine.md](../architecture/doctrine.md) and [../architecture/examples.md](../architecture/examples.md). Read **`/taste-flow`** first.

## Preconditions

1. Resolve **`goal-id`**
2. Workspace: `.agents/temp/goals/<goal-id>/`
3. Prefer explore via **`/orchestrate-flow`**

## Process

1. Explore siblings, **existing services**, and target folders (subagents OK). Reuse/extend a service before inventing a parallel one. Flag wrong existing shape in the lane.
2. Draft the **Structure** card from doctrine (Services + **Moves / corrections** + Feature entry + Folder map + Scalability). A required move may block new feature code until listed on the card.
3. Fold into the relevant `plans/NN-*.md` via `/create-plan-flow` (or patch if already written).
4. Mid-implement sprawl, duplicated domain logic, or newly spotted prior mistake → update this plan's Structure (Moves / corrections), then continue `/implement-flow` with the move.

## Hand-offs

- UI → `/design-flow`
- Plan write → `/create-plan-flow`
- Scale, duplicated-service, or "should have moved" failures later → `/validate-flow` / `/code-review-flow`

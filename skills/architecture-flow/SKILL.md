---
name: architecture-flow
description: >-
  Goal-scoped structure card: inject entry point, folder map, and write-path
  scale into plans under .agents/temp/goals/<goal-id>/. Looked up by /goal and
  create-plan-flow. Not for auto-invocation — use /architecture outside a goal.
disable-model-invocation: true
---

# Architecture Flow

Structure craft **inside a `/goal` workspace**. Doctrine lives in **`/architecture`** — follow it.

Examples: [../architecture/examples.md](../architecture/examples.md). Read **`/taste-flow`** (or `/taste`) first.

## Preconditions

1. Resolve **`goal-id`**
2. Workspace: `.agents/temp/goals/<goal-id>/`
3. Prefer explore via **`/orchestrate-flow`** (parallel `explore` Tasks)

## Process

1. Explore siblings / target folders (subagents OK).
2. Draft the **Structure** card from `/architecture`.
3. Fold the card into the relevant `plans/NN-*.md` via `/create-plan-flow` (or patch the plan if already written).
4. Mid-implement sprawl → update **this** plan’s Structure, then continue `/implement-flow`.

## Hand-offs

- UI → `/design-flow`
- Plan write → `/create-plan-flow`
- Scale failures later → `/validate-flow` fails them

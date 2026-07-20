# Architecture Flow

Structure craft **inside a `/goal` workspace**. Read [./doctrine.md](./doctrine.md) and [./examples.md](./examples.md). Read **`/taste`** first.

## Preconditions

1. Resolve **`goal-id`**
2. Workspace: `.agents/temp/goals/<goal-id>/`
3. Prefer explore via **`/orchestrate`**

## Process

1. Explore siblings, **existing services**, and target folders (subagents OK). Reuse/extend a service before inventing a parallel one. Flag wrong existing shape in the lane.
2. Draft the **Structure** card from doctrine (Services + **Moves / corrections** + Feature entry + Folder map + Scalability). A required move may block new feature code until listed on the card.
3. Fold into the relevant `plans/NN-*.md` via `/create-plan` (or patch if already written).
4. Mid-implement sprawl, duplicated domain logic, or newly spotted prior mistake → update this plan's Structure (Moves / corrections), then continue `/implement` with the move.

## Hand-offs

- UI → `/design`
- Plan write → `/create-plan`
- Scale, duplicated-service, or "should have moved" failures later → `/validate` / `/code-review`

# Design Flow

UI craft **inside a `/goal` workspace**. Read [./doctrine.md](./doctrine.md). Examples: [./examples.md](./examples.md).

## Preconditions

1. Resolve **`goal-id`**
2. Workspace exists: `.agents/temp/goals/<goal-id>/`
3. Read `GOAL.md`, `GRILL.md`, and the target `plans/NN-*.md`

If there is no goal workspace, stop and use **`/design`** (standalone) or start `/goal`.

## Process

When the work **creates or substantially changes** UI:

1. Before coding pixels: write a tiny **Design card** (fold into the plan via `/create-plan`) — see doctrine Mode A template
2. Implement against that card; mobile first (`/taste` + design doctrine)
3. Validate visually via localhost; taste self-check still applies
4. Stay within `GOAL.md` / this plan's file lane

## Hand-offs

- Structure → `/architecture`
- Style → `/taste`
- After build → `/validate`

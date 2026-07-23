# Design Flow

UI craft **inside a `/goal` workspace**. Read [./doctrine.md](./doctrine.md). Examples: [./examples.md](./examples.md).

## Preconditions

1. Resolve **`goal-id`**
2. Resolve `goal_root` per [../workspace-roots.md](../workspace-roots.md); workspace exists at `<goal-root>/`
3. Read `<goal-root>/GOAL.md`, `<goal-root>/GRILL.md`, and the target `<goal-root>/plans/NN-*.md`

If there is no goal workspace, stop and use **`/design`** (standalone) or start `/goal`.

## Process

When the work **creates or substantially changes** UI:

1. Before coding pixels: write a tiny **Design card** (fold into the plan via `/create-plan`) — see doctrine Mode A template
2. Implement against that card; mobile first (`/taste` + design doctrine)
3. For browser-reachable UI criteria, follow the [Browser validation reference](../validate/reference.md) when Browser capability is available; otherwise report visual validation as blocked. Taste self-check still applies.
4. Stay within `<goal-root>/GOAL.md` / this plan's file lane

## Hand-offs

- Structure → `/architecture`
- Style → `/taste`
- After build → `/validate`

# Design Flow

Craft UI for a bounded parent slice. Read [doctrine.md](doctrine.md) and
[examples.md](examples.md). Use the shared
[execution context](../pack-shared/execution-context.md), not a workspace or
plan file.

## Read first

1. The inline outcome, Done when, non-goals, locked decisions, Active Rules,
   current slice, acceptance criteria, and write lane.
2. The named Ticket / PR, relevant Git diff/history, repository UI code,
   existing tokens, and project rules.

## Process

When work creates or substantially changes UI:

1. Before coding pixels, put the doctrine's small **Design** card in chat (or
   a user-approved destination). The parent includes its relevant decisions in
   the inline context and Worker Brief.
2. Implement against that card: mobile first, with `/taste` and the design
   doctrine's hierarchy, state, depth, color, and ethical-flow rules.
3. For browser-reachable UI criteria, follow the
   [browser evidence protocol](../pack-shared/browser-evidence.md) when Browser
   capability is available; otherwise report visual validation as blocked.
4. Stay within the current slice's lane. Return structural gaps, scope
   changes, or shared-component decisions to the parent; do not create a
   plan, workspace, status, or other agent-owned artifact.

## Hand-offs

- Structure → `/architecture`
- Style → `/taste`
- After build → parent-owned acceptance evidence

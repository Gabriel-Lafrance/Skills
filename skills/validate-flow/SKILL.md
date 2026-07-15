---
name: validate-flow
description: >-
  Goal-scoped validate: check GOAL Done when + plans INDEX under
  .agents/temp/goals/<goal-id>/ (terminals first, no Convex MCP ritual). Looked
  up by /goal. Not for auto-invocation — use /validate outside the loop.
disable-model-invocation: true
---

# Validate Flow

Gate out **inside an active `/goal`**. Report format, scalability table, and evidence rules live in **`/validate`** — follow them.

## Preconditions

1. Resolve **`goal-id`**
2. Criteria from this workspace only: `GOAL.md` Done when → `/trackers-flow` brief → completed `plans/INDEX` rows → user paste
3. Also: `/taste-flow` self-check, scalability (`/architecture`), `/design-flow` if UI

## Process

1. Restate the bar as checkboxes.
2. One terminals read (`/taste` Verify) — **no** Convex MCP by default.
3. Scalability section required.
4. Report with `/validate` template.
5. All pass → `/code-review-flow`; any fail → fix and re-run; blocked → ask. Ticket close is manual (trackers are read-only).

## Anti-patterns

- Mixing another goal-id’s criteria
- MCP verify loops when terminals already have the signal

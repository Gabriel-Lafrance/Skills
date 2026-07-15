---
name: code-review-flow
description: >-
  Goal-scoped two-axis review after validate under
  .agents/temp/goals/<goal-id>/. Looked up by /goal. Not for auto-invocation —
  use /code-review for ad-hoc branch/PR review.
disable-model-invocation: true
---

# Code Review Flow

Standards + Spec review **inside an active `/goal`**. Process, smell baseline, and prompts live in **`/code-review`** — follow them.

## Preconditions

1. Resolve **`goal-id`**
2. Prefer after `/validate-flow` pass
3. Spec source: this workspace’s `GOAL.md` + `GRILL.md` + INDEX + plans; ticket via `/trackers-flow`
4. Workers via `/orchestrate-flow` — scope to this goal-id only

## Process

1. Pin fixed point (ask if missing).
2. Parallel Standards + Spec Tasks per `/code-review`.
3. Aggregate two axes separately.
4. Failures → fix → re-`/validate-flow` if behavior changed; then continue `/goal` ACHIEVED path.

## Anti-patterns

- Solo-reviewing a large goal diff when workers can
- Reading another goal workspace
- Flagging missing Convex MCP / ritual lint as Standards failures

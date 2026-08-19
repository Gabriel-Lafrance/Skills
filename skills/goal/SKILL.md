---
name: goal
description: >-
  Stateless Cursor goal loop: grill, plan, implement, gather acceptance
  evidence, and review one verifiable outcome using in-chat execution context.
  Use when the user wants a feature or outcome built end to end. Nested under
  /just-do-it when that parent owns shipping.
disable-model-invocation: true
---

# Goal

**Must read:** [../pack-shared/standards.md](../pack-shared/standards.md) — Read `/taste` and `/architecture` doctrines this turn before grilling, planning, or implementing. Do not skip.

**Execution context:** [../pack-shared/execution-context.md](../pack-shared/execution-context.md) · **Read:** [doctrine.md](doctrine.md) · [reference.md](reference.md) · **Ask style:** [../pack-shared/asking.md](../pack-shared/asking.md) · **Browser:** [../pack-shared/browser-evidence.md](../pack-shared/browser-evidence.md) · **PR ship:** [../pack-shared/pr-ship.md](../pack-shared/pr-ship.md) when this chat opens a PR

Orchestrator only. Dispatch Task workers per
[../pack-shared/subagents.md](../pack-shared/subagents.md). Always load
`/taste` and `/architecture` during grill and before every implement wave.

`/goal` follows the stateless
[execution-context contract](../pack-shared/execution-context.md): plans are
inline unless the user explicitly requests a saved artifact and approves its
destination.

## Process

1. Establish or refresh the in-chat execution context.
   If a parent already supplied ticket, lane, Done when, non-goals, Active
   Rules, fixed point, and slice bounds, accept that brief. Do not re-derive
   ticket or branch ownership the parent holds.
2. Run the [lifecycle](reference.md#lifecycle): grill (unless skip-grill
   applies) → plan → implement → acceptance evidence → `/code-review` → Fix
   mode as needed. Task waves follow
   [subagents.md](../pack-shared/subagents.md). Always load `/taste` and
   `/architecture` during grill and before every implement wave.
3. Announce completion.

### If a parent already owns the ticket, branch, and PR

Do not ask ship Questions. Do not commit, push, or open a PR from this skill.
Return a completion summary plus evidence envelope to the parent.

### If this chat owns shipping

Offer ship Questions only after all gates pass (see
[reference.md](reference.md#ship-questions)). Do not commit or open a PR
unless the user answers yes. If they ask to open a PR, follow
[../pack-shared/pr-ship.md](../pack-shared/pr-ship.md). Do not invent a parent.

Recovery, progress, lookup, and safety rules live in the doctrine and reference.

## Anti-patterns

- Asking ship Questions when a parent owns shipping
- Pushing, committing for ship, or opening a PR when nested

# Goal (flow)

Bounded build nested under a parent orchestrator (typically `/just-do-it`).
Read [doctrine.md](doctrine.md) and [reference.md](reference.md). Use the shared
[execution context](../pack-shared/execution-context.md).

## Parent owns

- Ticket resolution and typed branch
- Shipping: checkpoint commits, push, PR draft/create
- Soft autonomy and hard stops for the outer wave

## This flow owns

1. Grill (unless parent already locked Done when / Active Rules and skip-grill applies)
2. Plan, implement, acceptance evidence (Done when + Active Rules + seams;
   browser protocol when UI)
3. `/code-review` and Fix-mode remediation loops the parent delegates into this
   build context
4. Return a completion summary + evidence envelope to the parent

## Process

1. Accept the parent brief: ticket, lane, Done when, non-goals, Active Rules,
   fixed point, and slice constraints.
2. Run the doctrine lifecycle inside those bounds. Task waves follow
   [subagents.md](../pack-shared/subagents.md).
3. Do **not** ask ship Questions. Return completion evidence to the parent.

## Anti-patterns

- Pushing, committing for ship, or opening a PR from this flow
- Re-deriving ticket/branch ownership the parent already holds
- Loading the standalone ship Questions batch

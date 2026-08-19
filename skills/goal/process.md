# Goal process

Read [../pack-shared/standards.md](../pack-shared/standards.md), then
[doctrine.md](doctrine.md) and [reference.md](reference.md). Use the shared
[execution context](../pack-shared/execution-context.md).

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

## Anti-patterns

- Asking ship Questions when a parent owns shipping
- Pushing, committing for ship, or opening a PR when nested
- Loading a second copy of this process

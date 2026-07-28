# Create Plan Flow

Produce **one inline plan contract** for an active `/goal`. Stay in **Agent mode** — no `SwitchMode`, no CreatePlan UI.

**Internal only** — `/goal` uses this flow to turn a Locked split into an implementation-ready slice. The output stays in chat; do not create a plan file, INDEX, status file, or workspace state.

## Preconditions

1. The shared [execution context](../pack-shared/execution-context.md) has an outcome, Done when, non-goals, lane, and relevant Active Rules.
2. `/grill-me` has announced Locked closing: non-goals, intended split, and shared understanding. Otherwise return to `/grill-me`.
3. The slice has a narrow lane, a clear owner, and known dependencies.

If the user explicitly asks to save the contract, get or honor an approved destination and write only that requested artifact.

## Process

### 1. Gather the applicable context

Read the in-chat execution context. Extract the Active Rules that this slice implements or preserves before choosing structure or acceptance criteria.

Use `/orchestrate`, `/taste`, and `/trackers` when ticket context applies. Explore as needed; carry `/architecture` and `/design` decisions into the contract when structure or UI is in scope.

### 2. Issue the contract

Produce the [inline plan contract](../goal/reference.md#inline-plan-contract) for one ordered slice. It must include:

- one verifiable outcome and 1–3 binary acceptance criteria;
- allowed paths or symbols, explicit exclusions, and Active Rules;
- concrete approach, structure or design decisions, and seam verification;
- owner, dependencies, handoffs, and paths or seams siblings must not touch;
- blockers first, with a clear frontier status.

No unresolved option menu belongs in an implementation contract. If an important decision remains open, return to the grill instead of inventing scope.

### 3. Update chat state

Add or replace the matching entry under **Current slices** in the execution context. Keep the frontier, dependencies, and current phase visible in chat. Re-announce the Locked split if the contract changes it materially.

Continue with `/implement` only for frontier slices. Do not write an automatic plan path or rely on a hidden artifact for a worker handoff.

### 4. Dispatch workers

Each Task prompt carries the applicable outcome, Done when, non-goals, Active Rules, lane, current slice contract, dependencies, and prior decisions. The parent keeps integration, acceptance evidence, and `/code-review`.

## Anti-patterns

- Planning before Locked grill closing
- Writing automatic plan files, INDEXes, status files, or resume state
- Sending a worker a file path instead of its in-chat contract
- One vague mega-plan when independent slices fit
- Coding the feature in this flow

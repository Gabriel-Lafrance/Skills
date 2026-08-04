# Grill Me flow

Use this variant inside an active `/goal` or parent wave. Read
[doctrine.md](doctrine.md), the shared
[execution context](../pack-shared/execution-context.md), and the
[asking contract](../pack-shared/asking.md). The parent carries all context in
chat; this flow creates no automatic artifacts.

## Preconditions

- The parent has supplied an outcome, current slice, non-goals, lane, and any
  ticket/PR or fixed-point evidence.
- The parent is ready to settle intent before issuing plans or implementation
  work.

## Process

1. Refresh the in-chat context from live repository, ticket, PR, and diff
   evidence. Re-announce only facts or user decisions that changed or were
   missing.
2. Gather every unsettled topic from the doctrine's behavior sweep. Include
   plan count and file lane alongside product questions so the first batch is
   complete.
3. Apply the relevant quality discipline before recommending answers:

   | When | Include in the batch |
   | --- | --- |
   | Always | `/taste`: **KISS**, named principles (SoC, SLAP, CQS, fail fast, Boy Scout, cohesion/coupling, idempotency, explicit, PoLA, honest names), error style, naming, entry-shape bias, verification |
   | Multi-file, data, or scale | `/architecture`: domain owner, public boundary, reuse versus a new primitive, folders, write path, and behavior-preserving corrections |

4. Send a **Questions-only** batch for every real open decision (no Locked
   heading in that message). Wait for the reply.
5. Put answers, Active Rules, corrections, and revised lanes directly in the
   execution context. If a correction exposes a new material unknown, send a
   new Questions-only batch.
6. When material Questions are settled, announce **Locked (correct if wrong)**
   for non-goals, split, and shared understanding in a **separate**
   announce-only message. Do not issue plans until that Locked closure stands
   and every relevant Active Rule has an enforcement and verification owner.
   Hand the inline context back to `/goal` for planning.

## Anti-patterns

- Giving workers a hidden path instead of the parent context
- Writing plans before Locked closure
- Treating a user decision as recoverable from code alone
- Creating automatic artifacts to hold language, choices, rules, or progress

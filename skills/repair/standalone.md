# Repair

Pessimistic bug hunt with the smallest possible fix. Read
[doctrine.md](doctrine.md), the shared
[execution context](../pack-shared/execution-context.md), and the
[asking contract](../pack-shared/asking.md).

## Process

1. Open a compact repair execution context: symptom, evidence, suspected cause,
   lane, and non-goals.
2. Hunt pessimistically and classify Local, Narrow, or Massive.
3. For Local/Narrow, grill what/how and binary acceptance before editing.
4. Apply only the smallest grilled fix.
5. Run `/validate` against the acceptance held in chat.

Massive → escalate to `/goal`; do not patch-sprawl. On pass, summarize the
evidence and any manual follow-up. Do not create persistent process artifacts;
save only an artifact the user requested at a location they approved.

## New-chat recovery

Rediscover the code and ticket facts, then re-announce the repair context.
Ask only for any missing user-owned grill decision or acceptance criterion.

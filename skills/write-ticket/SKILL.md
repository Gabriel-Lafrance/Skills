---
name: write-ticket
description: >-
  Create or promote one Linear or GitHub ticket: Memo (idea, no grill),
  Research (the need, after /grill-me), or Plan (how to build it in one
  pass, after a second grill). Use for a new ticket, a promotion, or a
  don't-forget note. Never inside /task.
disable-model-invocation: true
---

# Write Ticket

Create or promote one tracker ticket. User start only; `/task` reads tickets ([ticket context](../task/doctrine.md#ticket-context)) and never promotes one. This skill never implements the ticket.

## Read when

- Before analyzing or drafting: [code-quality.md](../rules/code-quality.md) and [code-structure.md](../rules/code-structure.md), plus [doctrine.md](doctrine.md) (stage gate, topic lists, work kind, promotion).
- Before sending a batch (steps 2 and 5): [asking.md](../pack-shared/asking.md) and the matching batch in [reference.md](reference.md).
- Drafting the body (steps 3 and 5): the stage body in [reference.md](reference.md).

## Process

1. Load an existing ticket or the prompt. Infer the tracker. Infer the target stage when the prompt or the current body already names Memo, Research, or Plan.
2. If the target stage is missing, send **one** asking-contract batch for the stage. Include priority, assignee, and tracker in that same batch when those are also missing. Wait.
3. **Memo.** Draft the short note and write it. No `/analyze`. No `/grill-me`.
4. **Research or Plan.** Run `/analyze` to full memo depth for that stage (this parent owns the next step). Then run `/grill-me` with the stage topic list in the doctrine. `/grill-me` returns here.
5. Fill that stage's body from the reference. Assign the work kind during Research. Show the draft in a Locked message with no Questions. If priority, assignee, or tracker is still missing, one metadata batch, then write. If those were already known, write after the draft is visible.
6. On a promotion, post the previous body as a comment, replace the description, and set the stage label. Same ticket. Status is **Todo** on create. On promote or refine, keep the current status unless the prompt names another.

## Anti-patterns

- Nesting this skill under `/task`, or starting `/task` from it
- Asking "write this?" after the Locked draft

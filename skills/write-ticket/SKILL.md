---
name: write-ticket
description: >-
  Create or promote one Linear or GitHub ticket as Memo, Research, or Plan.
  Memo saves an idea with no grill. Research records the need and the problem
  after /grill-me. Plan records how to solve it in code after a second
  /grill-me, detailed enough to implement in one pass. Use for a new ticket,
  a promotion, or a don't-forget note. Never inside /task.
disable-model-invocation: true
---

# Write Ticket

**Must read:** [../pack-shared/standards.md](../pack-shared/standards.md). Apply the rules in [code-quality.md](../rules/code-quality.md) and [code-structure.md](../rules/code-structure.md) this turn before analyzing or drafting. Do not skip.

**Read:** [doctrine.md](doctrine.md) · [reference.md](reference.md) · **Ask style:** [../pack-shared/asking.md](../pack-shared/asking.md)

This skill is a user start. Do not nest it under `/task`. It writes a tracker ticket; `/trackers` reads.
`/task` does not promote a ticket. This skill does. It never implements the ticket.

## Process

1. Load an existing ticket or the prompt. Infer the tracker. Infer the target stage when the prompt or the current body already names Memo, Research, or Plan.
2. If the target stage is missing, send **one** asking-contract batch for the stage. Include priority, assignee, and tracker in that same batch when those are also missing. Wait.
3. **Memo.** Draft the short note and write it. No `/analyze`. No `/grill-me`.
4. **Research or Plan.** Run `/analyze` to full memo depth for that stage (this parent owns the next step). Then run `/grill-me` with the stage topic list in the doctrine. `/grill-me` returns here. Do not start `/task`.
5. Fill that stage's body from the reference. Assign the work kind during Research. Show the draft in a Locked message with no Questions. If priority, assignee, or tracker is still missing, one metadata batch, then write. If those were already known, write after the draft is visible. No "write this?" question.
6. On a promotion, post the previous body as a comment, replace the description, and set the stage label. Same ticket. Status is **Todo** on create. On promote or refine, keep the current status unless the prompt names another.

Bodies, topic lists, and tracker fields live in the doctrine and reference.

---
name: write-ticket
description: Create or promote one Linear or GitHub ticket as a Memo, Research, or Plan. Use when the user asks to write, file, open, or draft a ticket or issue, or to note something so it is not forgotten. Never inside /task.
category: Documents
---

# Write Ticket

Create or promote one tracker ticket. User start only; `/task` reads tickets ([ticket context](../task/doctrine.md#ticket-context)) and never promotes one. This skill never implements the ticket.

## Read when

- About to analyze or draft? Open [code-quality.md](../rules/code-quality.md), [code-structure.md](../rules/code-structure.md), and [doctrine.md](doctrine.md) (stage gate, topic lists, work kind, promotion). Skip them and the ticket plans a shape the rules reject.
- About to grill or draft a Research or Plan ticket for a Feature? Open [strong-foundation.md](../rules/strong-foundation.md). Skip it and the Plan has no seams (named extension points where a new variant plugs in), so the next ticket rebuilds the feature instead of adding one adapter.
- About to send a batch (steps 2 and 7)? Open [Asking the user](../rules/writing-style.md#asking-the-user) and the matching batch in [reference.md](reference.md). Skip them and you ask for metadata the tracker already has.
- About to draft the body (steps 3 and 5)? Open the stage body in [reference.md](reference.md). Skip it and the ticket misses the sections its stage needs.

## Process

1. Load an existing ticket or the prompt. Infer the tracker. Infer the target stage when the prompt or the current body already names Memo, Research, or Plan.
2. If the target stage is missing, send **one** asking-contract batch for the stage. Include priority, assignee, and tracker in that same batch when those are also missing. Wait.
3. **Memo.** Draft the short note and write it, skipping `/analyze` and `/grill-me`.
4. **Research or Plan.** Run `/analyze` to full memo depth for that stage (this parent owns the next step). Then run `/grill-me` with the stage topic list in the doctrine. `/grill-me` returns here.
5. Fill that stage's body from the reference. Assign the work kind during Research.
6. Show the draft in a Locked in message with no Questions.
7. If priority, assignee, or tracker is still missing, send one metadata batch, then write. If those were already known, write after the draft is visible.
8. On a promotion, post the previous body as a comment, replace the description, and set the stage label. Keep it the same ticket.
9. Status is **Todo** on create. On promote or refine, keep the current status unless the prompt names another.

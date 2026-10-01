---
name: write-ticket
description: Creates or promotes Linear or GitHub tickets as Memo, Research, or Plan. Larger Plans default to a parent with small, reviewable subissues ordered for stacked pull requests. Use when the user asks to write, file, draft, or split tickets, or save an idea for later. Never inside /task.
category: Documents
---

# Write Ticket

Create or promote a tracker ticket, with linked subissues when a Plan needs multiple reviewable pull requests. User start only; `/task` reads tickets ([ticket context](../task/doctrine.md#ticket-context)) and never promotes one. This skill never implements the ticket.

## Read when

- About to analyze or draft? Open [code-quality.md](../rules/code-quality.md), [code-structure.md](../rules/code-structure.md), and [doctrine.md](doctrine.md) (stage gate, topic lists, work kind, promotion). Skip them and the ticket plans a shape the rules reject.
- About to grill or draft a Research or Plan ticket for a Feature? Open [strong-foundation.md](../rules/strong-foundation.md). Skip it and the Plan has no seams (named extension points where a new variant plugs in), so the next ticket rebuilds the feature instead of adding one adapter.
- About to send a batch (steps 2 and 7)? Open [Asking the user](../rules/writing-style.md#asking-the-user) and the matching batch in [reference.md](reference.md). Skip them and you ask for metadata the tracker already has.
- About to draft the body (steps 3 and 5)? Open the stage body in [reference.md](reference.md). Skip it and the ticket misses the sections its stage needs.
- About to draft or write the body (steps 3, 5, 6, 7, and 8)? Open [Final-version description](doctrine.md#final-version-description). Skip it and the ticket keeps dead ideas, strikethrough, and a record of how the decision changed.

## Process

1. Load an existing ticket or the prompt. Infer the tracker. Infer the target stage when the prompt or the current body already names Memo, Research, or Plan.
2. If the target stage is missing, send **one** asking-contract batch for the stage. Include priority, assignee, and tracker in that same batch when those are also missing. Wait.
3. **Memo.** Draft the short note, scrub it to [final-version cleanliness](doctrine.md#final-version-description), and write it, skipping `/analyze` and `/grill-me`.
4. **Research or Plan.** Run `/analyze` to full memo depth for that stage (this parent owns the next step). Then run `/grill-me` with the stage topic list in the doctrine. `/grill-me` returns here.
5. Fill that stage's body from the reference. Assign the work kind during Research or a direct start at Plan. For Plan, apply [PR-sized subissues](doctrine.md#pr-sized-subissues): default to a parent and children when the work has multiple reviewable outcomes. Fill the [stack handoff](reference.md#stack-handoff) and each child's Plan from the same locked context. Scrub every body to [final-version cleanliness](doctrine.md#final-version-description) before it is shown.
6. Show the complete draft in a Locked in message with no Questions, including child bodies and stack order when split. The draft is already final-version clean. The agent owns the split; ask only about unresolved decisions that change the work.
7. If priority, assignee, or tracker is still missing, send one metadata batch, then write. If those were already known, write after the draft is visible. Before that write, scrub the draft to [final-version cleanliness](doctrine.md#final-version-description). On update, replace the description with the clean body. Do not merge old canceled text into the new description. For a split Plan, create or reuse the parent and children, then link them with the real returned IDs using [Tracker write](reference.md#tracker-write).
8. On a promotion, post the previous body as a comment, replace the description with the scrubbed new stage body, and set the stage label. On a material same-stage refine, post the previous body as a comment once when it would otherwise be lost, then replace it with the clean body. Keep the existing ticket as the parent when adding children.
9. Status is **Todo** on create. On promote or refine, keep the current status unless the prompt names another.

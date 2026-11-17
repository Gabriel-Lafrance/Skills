---
name: write-ticket
description: Use when the user asks to write, file, open, draft, refine, or split an implementation-ready Linear or GitHub ticket or issue. Drafts in chat unless asked to write it. Never runs inside /task.
category: Documents
---

# Write Ticket

Develop the final ticket in the same chat as the research and decisions. User start only; `/task` reads tickets ([ticket context](../task/doctrine.md#ticket-context)). Never implement the ticket.

## Read when

- Investigating a touched user flow: [user-experience.md](../rules/user-experience.md#action-and-continuation). Carry the result into the Plan's UX/UI section. Backend-only work skips this.
- Before investigating or drafting: [code-quality.md](../rules/code-quality.md), [code-structure.md](../rules/code-structure.md), [doctrine.md](doctrine.md).
- Before asking: [Asking the user](../rules/writing-style.md#asking-the-user) and the relevant [reference.md](reference.md) guidance.
- Before drafting or writing: [Plain language](../rules/writing-style.md#plain-language), the [Plan body](reference.md#plan), [fresh-executor handoff](doctrine.md#fresh-executor-handoff), [final-version description](doctrine.md#final-version-description).

## Process

1. Read the prompt and any named existing ticket. Identify the outcome and whether the user wants a chat draft or a tracker write. Infer repository and tracker facts. Do not ask for a ticket stage.
2. Investigate the problem and the code yourself, reusing a current investigation and refreshing only gaps. When the change warrants it, apply [public boundary investigation](doctrine.md#public-boundary-investigation) before decomposition. Keep preparation in this chat; no intermediate ticket or saved research artifact.
3. Run `/grill-me` with the [decision guidance](doctrine.md#grill), including its intent restatement and [readiness check](../grill-me/doctrine.md#readiness-check). Carry exact contracts, reasons, dependencies, and blockers into the owning work items. As answers arrive, research new facts and revise the ticket here; do not restart the interview or re-investigate without a gap.
4. Fill the [Plan body](reference.md#plan) with items in dependency order under the [work-item contract](doctrine.md#implementation-items), and assign the work kind. When the work has reviewable PR boundaries, apply [PR-sized subissues](doctrine.md#pr-sized-subissues) and derive child bodies and the [stack handoff](reference.md#stack-handoff) from the same context. Scrub every body to its final current version.
5. Apply the [fresh-executor handoff](doctrine.md#fresh-executor-handoff) and resolve its blockers. Then show the complete final draft, with child bodies and stack order when split, once in a Locked in message with no Questions. An incomplete or unchecked draft stays in chat with its gaps visible; never call it implementation-ready.
6. Draft-only: stop with that draft. Authorized tracker write: gather still-missing priority, assignee, or tracker in one metadata batch. Write after the complete draft is visible, without asking permission again. Follow [Tracker write](reference.md#tracker-write), preserving ticket identity and the material prior body on update. Recheck final-version cleanliness after corrections.
7. Read back the saved body and relationships. Return actual URLs, kind, applied metadata, stack order when relevant, and any incomplete write or blocker. Do not reprint the body; follow [Working output](../rules/writing-style.md#working-output). Do not start implementation or publishing.

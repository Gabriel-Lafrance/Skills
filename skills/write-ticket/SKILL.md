---
name: write-ticket
description: Develop an implementation-ready Linear or GitHub ticket in one conversation, using analysis and grilling to settle intent and context. Draft in chat or write when requested; split into linked subissues when real PR boundaries help. Never inside /task.
category: Documents
---

# Write Ticket

Develop the final ticket in the same chat as the research and decisions. User start only; `/task` reads tickets ([ticket context](../task/doctrine.md#ticket-context)). This skill never implements the ticket.

## Read when

- Preparing a touched user flow? Open [user-experience.md](../rules/user-experience.md#action-and-continuation) during investigation and carry the result into the Plan's conditional UX/UI section. Backend-only work skips this.
- About to analyze or draft? Open [code-quality.md](../rules/code-quality.md), [code-structure.md](../rules/code-structure.md), and [doctrine.md](doctrine.md). Skip them and the ticket plans a shape the rules reject.
- About to grill or draft for a Feature? Open [strong-foundation.md](../rules/strong-foundation.md). Skip it and the Plan has no seams where a new variant plugs in.
- About to ask? Open [Asking the user](../rules/writing-style.md#asking-the-user) and the relevant [reference.md](reference.md) guidance. Skip them and you ask for facts the repo or tracker already has.
- About to draft or write? Open the [Plan body](reference.md#plan), [fresh-executor handoff](doctrine.md#fresh-executor-handoff), and [final-version description](doctrine.md#final-version-description). Skip them and the ticket needs the old chat to make sense.

## Process

1. Read the prompt and any named existing ticket. Identify the intended outcome and whether the user requested a chat draft or an actual tracker write. Infer repository and tracker facts when available. Do not ask for a ticket stage.
2. Gather problem and code evidence through `/analyze`, reusing current analysis and refreshing only gaps. Its targeted `/how` and `/why` investigations apply when they materially improve understanding. Apply its [public boundary investigation](../analyze/doctrine.md#public-boundary-investigation) when the change warrants it, before decomposition. Keep preparation in the same chat; no intermediate ticket or saved research artifact is required.
3. Apply `/grill-me` using the [decision guidance](doctrine.md#grill), including its own-words, line-by-line intent restatement. Ask only unresolved consequential user choices; a fully settled request needs no questions. Reuse settled answers. As answers change the understanding, research new facts and revise the developing ticket here; do not restart the interview or require another analysis pass without a gap.
4. Fill the [Plan body](reference.md#plan) from that evidence and locked context. Write meaningful implementation items in dependency order, each with local Do, Why, How, and planned Verify details under the [work-item contract](doctrine.md#implementation-items). Keep shared context in the other sections without repeating item rationale. Assign the work kind. Apply [PR-sized subissues](doctrine.md#pr-sized-subissues) when the work has useful reviewable PR boundaries. Derive child bodies and the [stack handoff](reference.md#stack-handoff) from the same context. Scrub every body to its final current version.
5. Apply the [fresh-executor handoff](doctrine.md#fresh-executor-handoff), including its fresh-context read-only checker for nontrivial drafts and conditional stack check. Resolve its concrete blockers, then show the complete final draft once in a Locked in message with no Questions (the final response for draft-only). Include child bodies and stack order when split. Incomplete or unchecked drafts remain in chat with the gaps visible; do not call them implementation-ready.
6. For a draft-only request, stop with that single final draft. For an authorized tracker write, gather any still-missing priority, assignee, or tracker in one metadata batch. Write after the complete draft is visible, without a redundant permission question. Follow [Tracker write](reference.md#tracker-write), preserving ticket identity and the material prior body on update. Recheck final-version cleanliness after corrections.
7. Read back the saved body and relationships. Return actual URLs, kind, applied metadata, and stack order when relevant, with any incomplete write or blocker. Do not print the complete body again; follow [Working output](../rules/writing-style.md#working-output). Status is **Todo** on create; preserve it on update unless the user named another. Do not start implementation or publishing.

---
name: analyze
description: Stateless analysis returned in chat. Use when the user asks to look into, investigate, research, or explain a bug, an idea, or a question before anything is built, or nested under write-ticket or review remediation. Does not write tickets or code.
category: Documents
---

# Analyze

Investigate a task, idea, ticket, PR, or review-fix backlog and return an evidence-backed memo in chat. Never write to Linear or GitHub.

## Read when

- About to research, even when the ask looks like a single file? Open [code-quality.md](../rules/code-quality.md), [code-structure.md](../rules/code-structure.md), [doctrine.md](doctrine.md), and the [execution context](../rules/planning.md#execution-context). Skip them and the memo recommends a fix the rules reject.
- About to search widely or read large files? Open [main-context.md](../rules/main-context.md). Skip it and raw search output buries the analysis.
- About to ask the user anything? Open [Asking the user](../rules/writing-style.md#asking-the-user). Skip it and you ask what the repo already answers.

## Contract

- Rediscover repository, ticket, PR, and diff facts from their live sources.
- Keep user decisions, rules, areas, and promotion state visible in the execution context, and take them from the user, not from code.
- Return the analysis memo in chat only, and keep state in the execution context.
- Save a memo only when the user explicitly requests it and approves the destination.

## Mechanics or rationale only

If the user only wants how something works (a walkthrough, who owns a layer, how layers fit), stop and follow [`/how`](../how/SKILL.md). If they only want why it is this way, stop and follow [`/why`](../why/SKILL.md). A bug, an idea, impact, or a build seed stays here.

## Process

1. Establish or refresh the relevant execution context and normalize the ask.
   When a parent already locked Done when and rules that must stay true,
   reuse them without re-grilling product intent.
2. Investigate the affected flow using the doctrine's [research rules](doctrine.md#research-rules). Derive consequential choices from actual inputs, state changes, writes, and consumers where relevant. Separate facts, settled decisions, ordinary implementer choices, and unresolved tradeoffs before recommending a design.
   For any parent, follow [nested capabilities](../rules/planning.md#nested-capabilities) and return the relevant
   facts, conclusions, source pointers, and uncertainty directly into the
   parent conversation. Use [bounded scouts](doctrine.md#bounded-research-scouts) only for independently uncertain boundaries. Reuse current evidence; no separate
   standard memo is required in nested mode.
   When understanding the existing mechanics would materially change the
   analysis, use [`/how`](../how/SKILL.md) for that bounded flow or owner.
   When a concrete historical design question could change the scope or
   constraints, use [`/why`](../why/SKILL.md) with its full evidence contract.
   Reuse current outputs instead of repeating those investigations. Carry
   their relevant conclusions, source pointers, and uncertainty into the memo.
   `/how` describes the existing system; it does not choose the new design.
   `/why` explains evidenced rationale; the user's desired benefit still comes
   from the user. Neither replaces this memo's impact and risk judgment or
   starts another interview.
3. Standalone, post the doctrine memo. Lead with a Mermaid diagram.
   Include an inline execution seed when the work is buildable.

### Review remediation

Use this mode only when the active orchestrator requests analysis of named
Fix-now rows under [remediation](../rules/execution.md#remediation). Return
root cause, smallest fix, touch surface, uncertainty, and verification keyed
to each stable finding ID. Add no findings, product discovery, or follow-ups.
The orchestrator adjudicates and dispatches once; analysis does not promote
or launch an implementation lifecycle.

### If a parent already owns the next step

Follow [nested capabilities](../rules/planning.md#nested-capabilities). Return
bounded evidence and recommendations. The parent owns preparation, promotion,
and any next step, including when it already has implementation authorization.

### If this is a user one-off

Ask one batch for real unknowns, then offer the explicit hand-off choices
in [doctrine.md](doctrine.md#apply) (Done / Sharpen / Promote / Write ticket /
Promote + start). Ask those Questions unless the user already named the next
step, and work without a parent brief.

## Anti-patterns

- Returning a raw search hit list instead of the memo
- Answering a pure how or why question with this memo
- Creating tickets, implementing code, or writing tests

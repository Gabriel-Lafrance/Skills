---
name: analyze
description: >-
  Stateless task analysis returned in chat. One-off research with
  promote-to-task handoffs, or nested under a parent (write-ticket, review
  remediation). Does not write tickets or automatic artifacts.
disable-model-invocation: true
---

# Analyze

Investigate a task, idea, ticket, PR, or review-fix backlog and return an evidence-backed memo in chat. Never write to Linear or GitHub.

## Read when

- Before researching, even when the ask looks like a single file: [code-quality.md](../rules/code-quality.md) and [code-structure.md](../rules/code-structure.md), plus [doctrine.md](doctrine.md) and the [execution context](../rules/planning.md#execution-context).
- Before asking the user anything: [Asking the user](../rules/writing-style.md#asking-the-user).

## Contract

- Rediscover repository, ticket, PR, and diff facts from their live sources.
- Keep user decisions, rules, lanes, and promotion state visible in the execution context; never infer them from code.
- Return the analysis memo in chat. Do not create automatic runtime artifacts or hidden paths.
- Save a memo only when the user explicitly requests it and approves the destination.

## Process

1. Establish or refresh the relevant execution context and normalize the ask.
   Do not re-grill product intent when a parent already locked Done when and
   rules that must stay true.
2. Investigate: find the relevant code first, then judge how, impact, and
   risk from those facts. A `/write-ticket` Research or Plan seed
   still gets the complete standard memo: Research memos gather the problem,
   Plan memos gather the code that would change.
3. Post the doctrine memo (standard or review-remediation). Lead with a
   Mermaid diagram. Include an inline `/task` seed when the work is
   buildable, except when a parent will write the ticket itself.

### Review remediation

Use this mode only for named Fix-now rows from `/review`.
Present every selected stable-finding analysis before any promotion choice.
Do not add findings, reopen product discovery, or analyze Follow-up items
and nits.

### If a parent already owns the next step

Skip one-off hand-off Questions. Skip `/task` promotion unless the parent
explicitly instructed `promote + start`. Return the memo to the parent.

- `/write-ticket`: return the memo; the parent grills, then drafts and writes the ticket.
- Review remediation: parent shows the complete memo, then promotes under
  its rules.

### If this is a user one-off

Ask one batch for real unknowns, then offer the explicit hand-off choices
in [doctrine.md](doctrine.md#apply) (Done / Sharpen / Promote / Write ticket /
Promote + start). Do not invent a parent brief or skip those Questions unless
the user already named the next step.

## Anti-patterns

- Offering hand-off Questions when a parent owns the next step
- Stubbing the memo because a `/write-ticket` Research or Plan seed is short
- Returning a memo with no diagram when the path can be drawn
- Returning a raw search hit list instead of the memo
- Broadening into product discovery during review remediation
- Creating tickets, implementing code, or writing tests

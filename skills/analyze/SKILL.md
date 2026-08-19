---
name: analyze
description: >-
  Stateless task analysis returned in chat. One-off research with
  promote-to-goal handoffs, or nested under a parent (write-ticket, just-do-it,
  review remediation). Does not write tickets or automatic artifacts.
disable-model-invocation: true
---

# Analyze

**Must read:** [../pack-shared/standards.md](../pack-shared/standards.md) — Read `/taste` and `/architecture` doctrines this turn before researching or posting the memo. Do not skip.

**Execution context:** [../pack-shared/execution-context.md](../pack-shared/execution-context.md) · **Ask style:** [../pack-shared/asking.md](../pack-shared/asking.md)

`/analyze` investigates a task, idea, ticket, PR, or review-fix backlog and returns an evidence-backed memo in chat. It never writes to Linear or GitHub.

## Contract

- Rediscover repository, ticket, PR, and diff facts from their live sources.
- Keep user decisions, rules, lanes, and promotion state visible in the execution context; never infer them from code.
- Return the analysis memo in chat. Do not create automatic runtime artifacts or hidden paths.
- Save a memo only when the user explicitly requests it and approves the destination.

**Read:** [doctrine.md](doctrine.md). **Always** Read and apply `/taste` and
`/architecture` (see [standards.md](../pack-shared/standards.md)). Do not skip
architecture because the ask looks like a single file.

## Process

1. Establish or refresh the relevant execution context and normalize the ask.
   Do not re-grill product intent when a parent already locked Done when and
   Active Rules.
2. Investigate via Task workers per
   [../pack-shared/subagents.md](../pack-shared/subagents.md): non-trivial
   research **must** use a Task; parallelize independent surfaces, then
   synthesize the evidence. A `/write-ticket` seed is often a short capture:
   still run the complete standard memo. Do not stub.
3. Post the doctrine memo (standard or review-remediation). Lead with a
   Mermaid diagram. Include an inline `/goal` seed when the work is
   buildable, except when a parent will write the ticket itself.

### Review remediation

Use this mode only for named Fix-now rows from `/code-review` or `/just-do-it`.
Present every selected stable-finding analysis before any promotion choice.
Do not add findings, reopen product discovery, or analyze Follow-up items
and nits.

### If a parent already owns the next step

Skip one-off hand-off Questions. Skip `/goal` promotion unless the parent
explicitly instructed `promote + start`. Return the memo to the parent.

- `/write-ticket`: return the memo; the parent drafts and writes the ticket.
- `/just-do-it` standard research: parent may instruct `promote + start`
  after the memo is shown.
- Review remediation: parent shows the complete memo, then promotes under
  its rules.

### If this is a user one-off

Ask one batch for real unknowns, then offer the explicit hand-off choices
in [doctrine.md](doctrine.md#apply) (Done / Sharpen / Promote / Write ticket /
Promote + start). Do not invent a parent brief or skip those Questions unless
the user already named the next step.

## Anti-patterns

- Offering hand-off Questions when a parent owns the next step
- Stubbing the memo because a `/write-ticket` seed is short or ungrilled
- Returning a memo with no diagram when the path can be drawn
- Broadening into product discovery during review remediation
- Creating tickets, implementing code, or writing tests

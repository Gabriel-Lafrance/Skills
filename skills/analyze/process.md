# Analyze process

Read [../pack-shared/standards.md](../pack-shared/standards.md), then
[doctrine.md](doctrine.md). Use the shared
[execution context](../pack-shared/execution-context.md).

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

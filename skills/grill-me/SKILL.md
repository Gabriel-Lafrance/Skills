---
name: grill-me
description: Use when the user asks to be grilled, to challenge or stress-test an idea, or to settle decisions before a plan. Interviews and locks decisions in chat; writes no code.
category: General
---

# Grill Me

Stress-test the request until its consequential decisions fit together across the affected flow. Research facts, challenge weak answers, and carry concrete contracts and honest remaining gaps into the execution context.

## Read when

- Settling a touched user flow or visible action, before proposing choices: [user-experience.md](../rules/user-experience.md#action-and-continuation). Backend-only work skips this.
- Before recommending an answer: [code-quality.md](../rules/code-quality.md), [code-structure.md](../rules/code-structure.md).
- Before the intent restatement: [doctrine.md](doctrine.md).
- Resuming, or working under a parent: the [execution context](../rules/planning.md#execution-context).
- Before sending Questions or Locked in: [Asking the user](../rules/writing-style.md#asking-the-user), [Plain language](../rules/writing-style.md#plain-language).

## Process

1. Establish or refresh a compact in-chat execution context from the ask and
   repository, ticket, PR, or diff facts, reusing a parent's brief. Re-announce
   only changed or missing facts and decisions. Before testing solution choices,
   show the [intent restatement](doctrine.md#intent-restatement), or reuse a
   parent's current one that meets that bar.
2. Sort facts and choices by the doctrine's [materiality bar](doctrine.md#what-to-discover):
   research facts, reuse the parent's decisions, and derive ordinary details
   without interviewing on them.
3. Under `/write-ticket`, surface consequential choices affecting behavior,
   data, contracts, delivery boundaries, dependencies, and authority. The
   parent derives child count, order, and file lanes from the settled choices.
4. Map choices and their prerequisites with the doctrine's
   [decision rounds](doctrine.md#decision-rounds). If consequential user-owned
   choices remain, send a **Questions-only** batch shaped as in
   [what to discover](doctrine.md#what-to-discover), then wait for the reply.
   If everything is settled, omit Questions.
5. Record answers, their reasons, rules that must stay true, corrections, and
   researched ownership paths in the execution context. Ask another batch for
   an incomplete answer, contradiction, or newly exposed consequential tradeoff
   under [answer pressure](doctrine.md#answer-pressure); a topic mentioned or
   recommendation offered is not a settled decision. Missing template
   categories never justify another interview.
6. Apply the [readiness check](doctrine.md#readiness-check) to the affected flow.
   Honor [pause, defer, and stop](doctrine.md#pause-defer-and-stop) without claiming
   unresolved work is ready. When material Questions are settled, announce the
   [Locked in](doctrine.md#output) message, keeping current decisions and their
   reasons and dropping superseded ones, or reuse a current parent lock.
7. Issue plans only after the Locked in message stands and every relevant rule
   has an enforcement and verification owner.

### If a parent already owns the next step

Follow [nested capabilities](../rules/planning.md#nested-capabilities). Return
only changed decisions, their reasons, and remaining material gaps to the
parent, which owns the next step: `/write-ticket` finishes the ticket with
`/task` unstarted; an execution skill continues its current lifecycle.

### If this is a user one-off

Stop after shared understanding unless the user asks for the next step. For an
authorized build use the Skills table in `AGENTS.md`:

- Structure unclear: investigate first, then the selected execution skill.
- Ready to build: `/task`. Carry settled decisions and test refusals.

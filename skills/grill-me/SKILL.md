---
name: grill-me
description: Stateless interview that pressures each decision that would change the plan, then locks the result in chat. Use when the user asks to be grilled, to challenge or stress-test an idea, or to settle decisions before a plan.
category: General
---

# Grill Me

Stress-test the request until its consequential decisions fit together across the affected flow. Research facts, question weak answers, and carry concrete contracts and honest remaining gaps into the execution context.

## Read when

- Settling a touched user flow or visible action? Open [user-experience.md](../rules/user-experience.md#action-and-continuation) before proposing choices. Infer routine details from the outcome and existing product; ask only material tradeoffs. Backend-only work skips this.
- About to recommend an answer? Open [code-quality.md](../rules/code-quality.md) and [code-structure.md](../rules/code-structure.md). Skip them and you recommend the option the rules forbid.
- Every run: open [doctrine.md](doctrine.md), the [execution context](../rules/planning.md#execution-context), and the [Asking the user](../rules/writing-style.md#asking-the-user) and [Plain language](../rules/writing-style.md#plain-language) sections of writing-style.md. Skip them and you mix Questions with Locked in, or ask what the repo already answers.

## Process

1. Establish or refresh a compact in-chat execution context from the ask and
   rediscovered repository, ticket, PR, or diff facts. If a parent already
   supplied an outcome, current slice, non-goals, area, and ticket/PR, reuse
   that brief. Re-announce only facts or user decisions that changed or were
   missing. Before testing solution choices, show the doctrine's
   [intent restatement](doctrine.md#intent-restatement) in your own words,
   one short plain-English bullet per idea. Reuse a parent's current
   restatement when it already meets that bar.
2. Separate researched facts, settled decisions, ordinary implementer choices,
   and unresolved consequential tradeoffs using the doctrine's materiality bar.
   Research factual gaps and reuse the parent's decisions. Derive ordinary
   implementation details from the evidence and applicable quality and
   structure rules; do not turn them into an interview.
3. When the parent is `/write-ticket`, focus on its ticket-preparation topics.
   Surface consequential choices affecting behavior, data, contracts, delivery
   boundaries, dependencies, and authority. The parent derives child count,
   order, and file lanes from the settled choices.
4. Map choices and their prerequisites using the doctrine's
   [decision rounds](doctrine.md#decision-rounds). If consequential user-owned choices remain, send a **Questions-only** batch
   (no Locked heading). Each question names one concrete choice, the relevant
   evidence or uncertainty, realistic alternatives, a recommendation with its
   reason, and practical consequences. Follow decision dependencies and ask
   the independent choices that can be answered now. Wait for the reply.
   If everything is settled, omit Questions.
5. Put answers, their reasons, rules that must stay true, corrections, and
   researched ownership paths directly in the execution context. Ask another
   batch for an incomplete answer, contradiction, or newly exposed consequential
   tradeoff. Apply [answer pressure](doctrine.md#answer-pressure); a topic mentioned
   or recommendation offered is not a settled decision. Missing template
   categories do not justify another interview.
6. Apply the [readiness check](doctrine.md#readiness-check) to the affected flow.
   Honor [pause, defer, and stop](doctrine.md#pause-defer-and-stop) without claiming
   unresolved work is ready. When material Questions are settled, announce
   **Locked in (tell me if this is wrong)** in a **separate** announce-only
   message. Include meaningful non-goals, derived split, and shared
   understanding. Put the corrected line-by-line intent restatement there,
   keeping current decisions and their reasons and dropping superseded ones.
   Reuse a current parent lock that already covers these decisions.
7. Issue plans only after the Locked in message stands and every relevant rule
   has an enforcement and verification owner.

Keep language, choices, rules, and progress in the chat. If the user wants a
durable artifact, ask for or honor an approved destination under the shared
[optional-persistence rule](../rules/planning.md#optional-persistence).

### If a parent already owns the next step

Follow [nested capabilities](../rules/planning.md#nested-capabilities). Return
only changed decisions, their reasons, and remaining material gaps to the
parent. It owns the next step; `/write-ticket` finishes the ticket, and the
selected execution skill continues its current lifecycle.

### If this is a user one-off

Stop after shared understanding unless the user explicitly asks for the next
step. For an authorized build use [AGENTS routing](../../AGENTS.md#skills):

- Structure needed: `/analyze`, then the selected execution skill.
- Ready to build: `/task-with-tests` by default; `/task` for an explicit
  command or no-tests request. Carry settled decisions and test refusals.

---
name: grill-me
description: Stateless interview that pressures each decision that would change the plan, then locks the result in chat. Use when the user asks to be grilled, to challenge or stress-test an idea, or to settle decisions before a plan.
category: General
---

# Grill Me

Discover product, behavioral, code quality, and code structure decisions through batched Questions, and keep locked decisions and rules that must stay true visible in the execution context.

## Read when

- About to recommend an answer? Open [code-quality.md](../rules/code-quality.md) and [code-structure.md](../rules/code-structure.md). Skip them and you recommend the option the rules forbid.
- Every run: open [doctrine.md](doctrine.md), the [execution context](../rules/planning.md#execution-context), and the [Asking the user](../rules/writing-style.md#asking-the-user) and [Plain language](../rules/writing-style.md#plain-language) sections of writing-style.md. Skip them and you mix Questions with Locked in, or ask what the repo already answers.

## Process

1. Establish or refresh a compact in-chat execution context from the ask and
   rediscovered repository, ticket, PR, or diff facts. If a parent already
   supplied an outcome, current slice, non-goals, area, and ticket/PR, reuse
   that brief. Re-announce only facts or user decisions that changed or were
   missing.
2. Apply the doctrine attack bar before sending: batch every unsettled
   load-bearing claim first, in the doctrine's batch order, then the rest of
   the sweep.
3. Include plan count and file area in that first batch.
4. When the parent is `/write-ticket`, interview only the topic list it
   supplied (Research or Plan) and skip implementation plan count and file
   area. The attack bar still applies to every load-bearing claim in that list.
5. Include the code-quality.md and code-structure.md topics in that batch:

   | When | Include in the batch |
   | --- | --- |
   | Always | [code-quality.md](../rules/code-quality.md) cite keys (`quality:keep-it-simple` and Named principles). If the slice needs config, lock reuse of existing env vars (`quality:reuse-env`): when `SITE_URL` already holds that job, skip the question about adding `FRONTEND_URL`. |
   | Always | [code-structure.md](../rules/code-structure.md) cite keys: who owns this job, the existing path, public entry, reuse versus a new one-job helper, folders, write path, who may act on that write, and whether to move old code. "Keep the existing structure" names that path and why a new folder would be a second owner. For a typo or pure rename, the path is the current file. |

6. Send a **Questions-only** batch for every real open decision (no Locked
   heading in that message). Each load-bearing question states the claim, the
   failure, one real rival, and why one option is recommended. Wait for the reply.
7. Put answers, rules that must stay true, corrections, and revised areas
   directly in the execution context.
8. On a non-trivial grill, if the rejected alternative, what would make the
   decision wrong, or the owner path is still unnamed, send another
   Questions-only batch.
9. If a correction exposes a new material unknown, send another
   Questions-only batch.
10. On a non-trivial grill, lock on a reply only when the rejected alternative,
    what would make the decision wrong, and the owner path are all named.
11. When material Questions are settled, announce
    **Locked in (tell me if this is wrong)** for non-goals, split, and shared
    understanding in a **separate** announce-only message: the Locked in
    message.
12. On a non-trivial grill, include the rejected alternative in the Locked in
    message.
13. Issue plans only after the Locked in message stands and every relevant rule
    has an enforcement and verification owner.

Keep language, choices, rules, and progress in the chat. If the user wants a
durable artifact, ask for or honor an approved destination under the shared
[optional-persistence rule](../rules/planning.md#optional-persistence).

### If a parent already owns the next step

Hand the inline context back to that parent. `/task` plans from it.
`/write-ticket` writes or promotes the ticket from it. Continue into the
parent's next step without waiting for the user to pick a next skill. Under
`/write-ticket`, the ticket step follows, not `/task`.

### If this is a user one-off

Stop after shared understanding unless the user explicitly asks for the next
step. `/task` receives the inline context; `/write-ticket` may receive the
relevant memo and decisions.

- Structure needed → `/analyze`, then `/task`.
- Ready to build → `/task`.

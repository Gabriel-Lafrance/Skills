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
   supplied an outcome, current slice, non-goals, lane, and ticket/PR, reuse
   that brief. Re-announce only facts or user decisions that changed or were
   missing.
2. Apply the doctrine attack bar before sending. Batch every unsettled
   load-bearing claim first, in the doctrine's batch order, then the rest of
   the sweep. Include plan count and file lane in that first batch. When the
   parent is `/write-ticket`, interview only the topic list it supplied
   (Research or Plan). The attack bar still applies to every load-bearing
   claim in that list. Skip implementation plan count and file lane.
3. Include the code-quality.md and code-structure.md topics in that batch:

   | When | Include in the batch |
   | --- | --- |
   | Always | [code-quality.md](../rules/code-quality.md) cite keys (`quality:keep-it-simple` and Named principles). If the slice needs config, lock reuse of existing env vars (`quality:reuse-env`); do not ask whether to add `FRONTEND_URL` when `SITE_URL` already holds that job. |
   | Always | [code-structure.md](../rules/code-structure.md) cite keys: who owns this job, the existing path, public entry, reuse versus a new one-job helper, folders, write path, who may act on that write, and whether to move old code. "Keep the existing structure" names that path and why a new folder would be a second owner. For a typo or pure rename, the path is the current file. |

4. Send a **Questions-only** batch for every real open decision (no Locked
   heading in that message). Each load-bearing question states the claim, the
   failure, one real rival, and why one option is recommended. Wait for the reply.
5. Put answers, rules that must stay true, corrections, and revised lanes directly in the
   execution context. On a non-trivial grill, if the rejected alternative, what
   would make the decision wrong, or the owner path is still unnamed, send
   another Questions-only batch. Do the same when a correction exposes a new
   material unknown. Do not lock on that reply while any of those three are open.
6. When material Questions are settled, announce **Locked in (tell me if this is wrong)**
   for non-goals, split, and shared understanding in a **separate**
   announce-only message. On a non-trivial grill, the rejected alternative,
   what would make the decision wrong, and the owner path are already named,
   and the message includes the rejected alternative. Do not issue plans until
   that Locked closure stands and every relevant rule has an enforcement and
   verification owner.

Do not create automatic files for language, choices, rules, or progress. If
the user wants a durable artifact, ask for or honor an approved destination
under the shared
[optional-persistence rule](../rules/planning.md#optional-persistence).

### If a parent already owns the next step

Hand the inline context back to that parent. `/task` plans from it.
`/write-ticket` writes or promotes the ticket from it. Do not stop to wait
for the user to pick a next skill. Do not start `/task` when `/write-ticket`
is the parent.

### If this is a user one-off

Stop after shared understanding unless the user explicitly asks for the next
step. `/task` receives the inline context; `/write-ticket` may receive the
relevant memo and decisions.

- Structure needed → `/analyze`, then `/task`.
- Ready to build → `/task`.

## Anti-patterns

- Handing off a hidden path instead of the inline context
- Writing plans before Locked closure
- Treating a user decision as recoverable from code alone
- Creating automatic artifacts to hold language, choices, rules, or progress
- Locking a non-trivial grill while the rejected alternative, what would make the decision wrong, or the owner path is unnamed
- A structure question that does not name the existing path

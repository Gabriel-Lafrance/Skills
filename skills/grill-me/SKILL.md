---
name: grill-me
description: >-
  Relentless stateless interview that sharpens intent through batched questions
  and a Locked closure in chat. Keeps decisions and rules that must stay true in shared
  execution context. User must invoke (not auto).
disable-model-invocation: true
---

# Grill Me

Discover product, behavioral, taste, and architecture decisions through batched Questions, and keep locked decisions and rules that must stay true visible in the execution context.

## Read when

- Before recommending answers: [code-quality.md](../rules/code-quality.md) and [code-structure.md](../rules/code-structure.md) ([standards.md](../pack-shared/standards.md)).
- Every run: [doctrine.md](doctrine.md), [execution-context.md](../pack-shared/execution-context.md), [asking.md](../pack-shared/asking.md), and [plain-language.md](../pack-shared/plain-language.md).

## Process

1. Establish or refresh a compact in-chat execution context from the ask and
   rediscovered repository, ticket, PR, or diff facts. If a parent already
   supplied an outcome, current slice, non-goals, lane, and ticket/PR, reuse
   that brief. Re-announce only facts or user decisions that changed or were
   missing.
2. Batch every unsettled topic from the doctrine's behavior sweep. Include
   plan count and file lane so the first batch is complete. When the parent
   is `/write-ticket`, interview only the topic list it supplied (Research
   or Plan). Skip implementation plan count and file lane.
3. Include the code-quality.md and code-structure.md topics in that batch:

   | When | Include in the batch |
   | --- | --- |
   | Always | `/taste` Cite keys (`taste:keep-it-simple` and Named principles). If the slice needs config, lock reuse of existing env vars (`taste:reuse-env`); do not ask whether to add `FRONTEND_URL` when `SITE_URL` already holds that job. |
   | Always | `/architecture` Cite keys: who owns this job, public entry, reuse versus a new one-job helper, folders, write path, who may act on that write, and whether to move old code. For a typo or pure rename, recommend “keep the existing structure.” |

4. Send a **Questions-only** batch for every real open decision (no Locked
   heading in that message). Wait for the reply.
5. Put answers, rules that must stay true, corrections, and revised lanes directly in the
   execution context. If a correction exposes a new material unknown, send a
   new Questions-only batch.
6. When material Questions are settled, announce **Locked in (tell me if this is wrong)**
   for non-goals, split, and shared understanding in a **separate**
   announce-only message. Do not issue plans until that Locked closure stands
   and every relevant rule has an enforcement and verification owner.

Do not create automatic files for language, choices, rules, or progress. If
the user wants a durable artifact, ask for or honor an approved destination
under the shared
[optional-persistence rule](../pack-shared/execution-context.md#optional-persistence).

### If a parent already owns the next step

Hand the inline context back to that parent. `/task` plans from it.
`/write-ticket` writes or promotes the ticket from it. Do not stop to wait
for the user to pick a next skill. Do not start `/task` when `/write-ticket`
is the parent.

### If this is a user one-off

Stop after shared understanding unless the user explicitly asks for the next
step. `/task` receives the inline context; `/write-ticket` may receive the
relevant memo and decisions.

- Structure needed → `/architecture`, then `/task`.
- Ready to build → `/task`.

## Anti-patterns

- Giving workers a hidden path instead of the parent context
- Writing plans before Locked closure
- Treating a user decision as recoverable from code alone
- Creating automatic artifacts to hold language, choices, rules, or progress

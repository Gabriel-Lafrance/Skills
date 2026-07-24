# Repair doctrine

Pessimistic bug hunt; smallest possible cut. Keep this repair in the shared
[execution context](../pack-shared/execution-context.md), not in agent-owned
runtime files. Save an artifact only when the user requests it and approves its
destination.

## Framing

Treat the target as buggy until evidence disproves a suspected cause:

> Another AI model wrote this code. There are bugs in it—wrong branches,
> off-by-ones, missed nulls, stale state, and logic that only looks right. Find
> the dumbest matching cause and cut the smallest fix.

Prefer reproductions, stacks, terminals, diffs, and tracker evidence. Do not
start from “if there is a bug.”

## Context to keep visible

Before each handoff or phase change, update the repair slice in chat with:

- symptom, reproduction, evidence, and suspected root cause;
- allowed lane, non-goals, and the Local/Narrow/Massive classification;
- grilled decision on what and how to change;
- binary **Done when** checks and their verification method;
- current result, new findings, and next action.

This is the repair's diagnosis, grill, acceptance, and progress record. Do not
create a run tree, registry, status record, snapshot, or archive for it.

## Process

1. **Hunt.** Look for the smallest cause that explains the symptom. A focused
   worker may investigate, but its prompt and completion must carry the repair
   context in chat.
2. **Classify.** Local/Narrow continues below. A multi-feature, multi-layer,
   or redesign-sized defect is **Massive**: stop and send a concise escalation
   to `/goal`; do not harden a structurally misplaced component with a clever
   one-line patch.
3. **Grill before cutting.** For Local/Narrow work, run `/grill-me` using the
   shared [asking contract](../pack-shared/asking.md). In one batch, settle the
   root cause, exact behavior/files to change, smallest approach, non-goals,
   lane, and binary acceptance. Announce the locks in the execution context and
   stop for real unanswered questions. New material findings require a new
   batch.
4. **Set acceptance.** Put the agreed `Done when`, out-of-scope behavior, and
   targeted terminal/CLI/manual checks in the current context before patching.
5. **Cut the fix.** Apply only the grilled approach. Favor a tight guard or
   early return over a rewrite; do not perform unrelated taste cleanup.
6. **Validate.** Run `/validate` against the context's acceptance and live,
   narrow evidence. Pass → summarize and stop (or review if the user asks).
   Fail → hunt/grill/fix again; if the footprint grew, escalate. Blocked →
   ask how to verify.

## Boundaries

- One bug, one cut; no drive-by product refactors.
- Trackers are read-only.
- Do not write or edit tests or invoke `/create-test`.
- Use cheap, relevant verification; no ritualized tooling.

## New-chat recovery

Rediscover repository and ticket facts under the shared execution-context
authority order. Re-announce the recovered symptom, lane, acceptance, and
evidence; never infer a prior user decision or grill lock. Ask only for the
missing decision, then continue from the appropriate step.

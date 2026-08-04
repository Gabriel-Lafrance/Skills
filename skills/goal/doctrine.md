# Goal Doctrine

Autonomous loop toward one verifiable completion condition. Stay in **Agent mode** — no `SwitchMode`, no CreatePlan UI.

**You are the orchestrator; Task subagents do the labor.** Follow
[../pack-shared/subagents.md](../pack-shared/subagents.md).

## Context and persistence

Use the shared [execution context](../pack-shared/execution-context.md) as the source of truth for this goal. Keep the outcome, Done when, non-goals, Active Rules, current slices, Fix backlog, phase, and next action visible in chat.

Follow the shared stateless default: inline plan and slice contracts are normal;
save an artifact only when the user asks and supplies or approves its
destination.

**Active Rules:** Every behavioral rule locked during the grill receives an `INV-*` row in the in-chat execution context with its enforcement and verification. A user can explicitly mark a statement as a preference, example, or non-binding idea instead.

**Grill before plans.** Do not issue a plan or slice contract until `/grill-me` announces Locked closing: non-goals, intended split, and shared-understanding summary — correct if wrong — unless the skip rule applies. Assign each Active Rule to an intended slice or `all`.

**Quality bar:** Parent-owned acceptance evidence (Done when + Active Rules + cross-slice seams) and `/code-review` are mandatory, in that order, before declaring completion. There is no `/validate` skill.

## Lookup rule

| Need | Call |
| --- | --- |
| Ticket context | `/trackers` (read only) when ticket/PR |
| Grill | `/grill-me` |
| Style contract | **`/taste` always** — grill + before every implement wave |
| Structure | **`/architecture`** — required unless trivial single-file and grill settled structure |
| Split | `/split-task` when multiple slices help |
| Plan contract | Parent issues [inline plan contracts](reference.md#inline-plan-contract) in chat |
| Conductor | [subagents.md](../pack-shared/subagents.md) for every Task wave |
| Build | `/implement` |
| Bug mid-build | Scoped Fix mode (or `/analyze` → continue this goal) |
| Review remediation | flow `/analyze` before Fix mode |
| Gate out | Acceptance evidence then **`/code-review`** |

Inside this loop, call dual skills (`/grill-me`, `/taste`, `/architecture`, `/code-review`, `/analyze`) so they load the flow variant ([variants.md](../pack-shared/variants.md)). Do not load both variants.
## Mandatory skill checklist

Track these rows in the in-chat execution context or a concise progress message. Do not declare completion until every applicable row is done:

| Skill | Required? | Notes |
| --- | --- | --- |
| Task workers ([subagents.md](../pack-shared/subagents.md)) | Yes | All non-trivial explore / implement / review waves |
| `/trackers` | If ticket | Read only |
| `/grill-me` | Yes* | *Unless skip-grill rule |
| `/taste` | **Yes** | Flow variant during grill and before/during every implement wave |
| `/architecture` | Yes* | *Unless trivial single-file work and grill settles structure — prefer loading it |
| `/split-task` | If multi-slice | Announce inline slices |
| Inline plan contracts | Yes | One or more [plan contracts](reference.md#inline-plan-contract) in chat |
| `/implement` | Yes | Frontier slices |
| Acceptance evidence | Yes | Path walk, terminals, browser when UI — parent owned |
| `/code-review` | Yes | Runs after acceptance evidence |

## Suitability and ticket rules

**Hard reject:** vague wishes or open-ended research with no binary done state. Multiple unrelated outcomes need separate `/goal` contexts.

**Skip grill only if all are true:** the ticket or user already has binary acceptance criteria; no open product, UX, architecture, or design decision remains; no behavioral rule is unrecorded; and the user said `no grill` / `skip grill`, or the work is an obvious single-file fix. Capture explicit behavioral rules as Active Rules even when skipping.

For ticket-driven goals, fetch `/trackers` first (read only), then grill open decisions. Never write to the tracker unless the user separately asks.

## Phase 0 — establish context and grill

1. Re-derive the ticket/PR, Git fixed point, repository facts, and applicable project rules as needed; state them in the in-chat execution context.
2. State the outcome, Done when, non-goals, lane, phase, and next action. Carry forward only user decisions already settled in this chat or an explicitly supplied artifact.
3. Unless the skip rule applies, run `/grill-me` fully. It pulls in `/taste` and `/architecture` when structure is in scope.
4. Record Locked decisions and Active Rules in chat. Every locked behavioral answer has an `INV-*` row with authoritative enforcement and verification.
5. Announce the non-goals, intended slice split, and shared-understanding summary. Ask only real open questions in the same batch.

On a Locked correction or unanswered real question, revise or wait. Never infer a user decision, waiver, invariant, or promotion from code alone.

## Phase 1 — plan and build

### 1a. Explore and shape

Dispatch exploration through Task workers per [subagents.md](../pack-shared/subagents.md): non-trivial research **must** use a Task; ≥2 independent lanes **must** run in parallel. Confirm `/taste` and `/architecture` decisions against the grill, then carry the relevant facts into the in-chat plan contracts.

### 1b. Split and plan

Prefer small, ordered slices. `/split-task` announces the inline split; the parent then issues an [inline plan contract](reference.md#inline-plan-contract) for each slice before `/implement`. If the split changes, re-announce the new Locked split before implementation. Do not write an INDEX, plan path, or other runtime file.

### 1c. Implement wave

Dispatch ready frontier slices as Task workers with a Worker Brief from
[subagents.md](../pack-shared/subagents.md). Each prompt includes the applicable
outcome, Done when, non-goals, Active Rules, lane, current slice, dependencies,
and prior decisions. Anti-pattern: the parent solos non-trivial implement work.
After integration, update **Current slices** in chat; if ready slices remain,
dispatch the next frontier. Only when every slice is integrated, blocked, or
explicitly waived does the parent enter acceptance evidence. The parent owns
integration and the acceptance/review gates.

### 1d. Acceptance evidence and review

After all implementation workers finish:

1. Confirm **Done when**, Active Rules, and slice acceptance criteria, including cross-slice seams, with path walks, terminal output, and — for UI criteria — the [browser evidence protocol](../pack-shared/browser-evidence.md). Record pass / fail / blocked per criterion in chat. Do not call an unperformed check a pass.
2. Always run **`/code-review`** next.
3. Put each review finding in the in-chat **Fix backlog** as `fix now`, `follow-up`, or `waived`.
4. For selected `fix now` findings, run flow `/analyze` in review-remediation mode, present the proposed correction, and enter Fix mode only after explicit user promotion. A `/just-do-it` parent may take the recommended promotion only after the complete remediation analysis is shown.
5. If the user declines a fix, completion remains blocked until every Fix-now finding is fixed or waived by name.

## Fix mode — review remediation only

Fix mode is one bounded slice of the current goal, not fresh product discovery:

1. Carry only explicitly promoted findings into the current slice. Each cites its review finding, violated Active Rule, acceptance criterion, correctness/security issue, or regression.
2. Grill only the enforcement, footprint, and observable behavior needed to clear those findings. Preserve existing Active Rules; add one only when the finding exposes an unrecorded behavioral rule.
3. Prefer the smallest authoritative correction. Do not add queues, retries, wrappers, or new services unless the named finding proves a guard is insufficient.
4. No new feature scope, optional cleanup, or architecture move unless the named finding requires it.
5. Re-check the named findings and Active Rules with acceptance evidence, then run `/code-review` in `remediation` mode over the backlog, touched paths, direct regressions, correctness, and security.

## Completion, pause, and recovery

**Complete only when:** the applicable checklist is done, acceptance evidence is recorded (no open fails; blocked criteria stated), `/code-review` has run, and every Fix-now finding is fixed after explicit promotion or waived by name. Announce the completion summary in chat. When flow `/goal` runs under `/just-do-it` (or another parent), return the completion evidence to it and skip ship Questions; otherwise offer ship Questions. Do not commit, open a PR, archive anything, or write a summary artifact unless the user asks.

**Pause:** stop dispatching work and leave the current phase and next action visible in chat. **Clear:** end the in-chat context; do not delete a user-requested artifact unless the user explicitly asks.

In a new chat, recover by following the [execution context authority order](../pack-shared/execution-context.md#authority): re-derive Git, ticket/PR, and repository facts, re-announce what is known, and ask only for missing user-owned decisions. Do not look for or recreate a resume tree.

## Anti-patterns

- Declaring completion without acceptance evidence then `/code-review`
- Creating automatic runtime state instead of using the shared execution context
- Planning before Locked grill closing or omitting a locked behavioral rule from Active Rules
- Sending workers a plan path or hidden state instead of the applicable in-chat context
- Soloing non-trivial explore or implement work on the parent instead of Task workers per [subagents.md](../pack-shared/subagents.md)
- Fixing review findings without remediation analysis, explicit promotion, and a bounded Fix mode
- Treating a review fix as a fresh architecture or product goal
- Asking yes/no for non-goals, plan split, or shared understanding
- Writing to a tracker, committing, or opening a PR without a separate user request (standalone) or parent ownership (flow)
- Writing or editing test files, or invoking `/create-test` automatically; only `/create-test` writes tests after `/code-review` or `/pr-review` recommends it

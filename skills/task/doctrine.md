# Task doctrine

## Job

Autonomous loop toward one verifiable completion condition. Stay in **Agent mode**. No `SwitchMode`, no CreatePlan UI.

## Owns

The orchestrator loop: execution context, grill-before-plans, behavior-lock suggestion after that grill, lookup table, mandatory skill checklist, suitability, skip-grill, completion, pause, and recovery rules. You are the orchestrator; Task subagents do the labor ([subagents.md](../pack-shared/subagents.md)).

## Does not own

- Taste and architecture bars: cite `taste:*` and `architecture:*`
- User-facing UI and `docs/design.md`: `/design`
- Review disposition: `/code-review`
- Test file contents: `/create-test` via `tester`, and only for briefs the user accepted
- Numbered lifecycle: [`reference.md`](reference.md#lifecycle) · [`SKILL.md`](SKILL.md)

## Cite keys

none (uses `taste:*` and `architecture:*`)

## Bars

Use the shared [execution context](../pack-shared/execution-context.md) as the source of truth for this task. Keep the outcome, Done when, non-goals, Active Rules, current slices, Fix backlog, phase, and next action visible in chat.

Follow the shared stateless default: inline plan and slice contracts are normal; save an artifact only when the user asks and supplies or approves its destination.

**Active Rules:** Every behavioral rule locked during the grill receives an `INV-*` row in the in-chat execution context with its enforcement and verification. A user can explicitly mark a statement as a preference, example, or non-binding idea instead.

**Grill before plans.** Do not issue a plan or slice contract until `/grill-me` announces Locked closing: non-goals, intended split, and shared-understanding summary (correct if wrong) unless the skip rule applies. Assign each Active Rule to an intended slice or `all`. Behavior-lock briefs come after that closing, never during the grill. A fuzzy rule is not a test: the observable outcome has to be specific before a brief can cite it.

**Quality bar:** Parent-owned acceptance evidence (Done when + Active Rules + cross-slice seams) and `/code-review` are mandatory, in that order, before declaring completion. There is no `/validate` skill.

### Lookup

| Need | Call |
| --- | --- |
| Ticket context | `/trackers` (read only) when ticket/PR |
| Grill | `/grill-me` |
| Style contract | **`/taste` always** (grill + before every implement wave) |
| Structure | **`/architecture` always** (grill + before every implement wave). For a typo or pure rename, load it and keep the existing structure |
| UX source of truth | **`/design`** when the slice is user-facing UI. Run Initialization first if `docs/design.md` is missing |
| Split | `/split-task` when multiple slices help |
| Plan contract | Parent issues [inline plan contracts](reference.md#inline-plan-contract) in chat |
| Conductor | [subagents.md](../pack-shared/subagents.md) for every Task wave (what vs how) |
| Find | `explorer` Tasks — main does not grep |
| Judge | `/analyze` via `analyzer` Tasks |
| Build | `/design` for user-facing UI; `/implement` for non-UI |
| Tests | After Locked grill, suggest locks that cite a grilled rule ([reference.md](reference.md#behavior-lock-suggestion)). The user may refuse every test. Accepted briefs go to `/create-test` via `tester`. Main never writes tests |
| Bug mid-build | Scoped Fix mode (or `/analyze` → continue this task) |
| Review remediation | `/analyze` before Fix mode |
| Gate out | Acceptance evidence then **`/code-review`** |

Inside this loop, call child skills (`/grill-me`, `/taste`, `/architecture`, `/design`, `/code-review`, `/analyze`). Each follows its [`SKILL.md`](SKILL.md); this parent already owns the next step.

### Mandatory skill checklist

Track these rows in the in-chat execution context or a concise progress message. Do not declare completion until every applicable row is done:

| Skill | Required? | Notes |
| --- | --- | --- |
| Task workers ([subagents.md](../pack-shared/subagents.md)) | Yes | Pick the specialist that owns the job. Main does not grep or write tests |
| `/trackers` | If ticket | Read only |
| `/grill-me` | Yes* | *Unless skip-grill rule |
| `/taste` | **Yes** | During grill and before/during every implement wave |
| `/architecture` | **Yes** | During grill and before/during every implement wave. Prefer loading even for a one-file fix |
| `/design` | If UI | User-facing slices. Initialization if `docs/design.md` is missing |
| `/split-task` | If multi-slice | Announce inline slices |
| Inline plan contracts | Yes | One or more [plan contracts](reference.md#inline-plan-contract) in chat |
| `/implement` | If non-UI | Frontier slices that are not user-facing |
| Acceptance evidence | Yes | Path walk, terminals. Parent owned |
| Behavior locks | When a complex public rule exists | After the plan names the public entry. Wait. Refusing every test is complete |
| `/code-review` | Yes | Runs after acceptance evidence. Standards and Spec. No Design axis |

### Suitability and skip grill

**Hard reject:** vague wishes or open-ended research with no binary done state. Multiple unrelated outcomes need separate `/task` contexts.

**Skip grill only if all are true:** the ticket or user already has binary acceptance criteria; no open product, UX, architecture, or design decision remains; no behavioral rule is unrecorded; and the user said `no grill` / `skip grill`, or the work is an obvious single-file fix. Capture explicit behavioral rules as Active Rules even when skipping.

For ticket-driven tasks, fetch `/trackers` first (read only), then grill open decisions. Never write to the tracker unless the user separately asks.

### Behavior locks

Suggest tests only from grilled Active Rules, using the `/create-test` bar for what is worth locking. Detail and the question template live in [reference.md](reference.md#behavior-lock-suggestion).

| Rule | Meaning |
| --- | --- |
| After the grill is locked | No brief until Locked closing, and until the plan names the public entry. A typo, rename, or other trivial skip offers nothing. When skip-grill applies because the rules are already specific, suggest from those rules |
| Cite a grilled rule | Why and What come from that rule's observable outcome. A brief with no rule is invalid |
| Same bar as `/create-test` | Offer a complex public surface that can silently drift: authorization, ownership, safe-to-retry, a domain rule, a facade, a stateful class, or a complex hook. Skip a thin wrapper, formatter, UI chrome, generated code, types-only file, coverage target, tautology, and quality-gate template |
| The user chooses | One Questions batch. Every brief has a no. Silence is not yes. A parent does not take `recommended` |
| A correction reopens the rule | "That is not the behavior" updates the rule and discards briefs that cited it. Do not build from the old rule |
| `tester` writes | An accepted brief is a `/create-test` slice after the public entry exists. The main agent does not write the file |
| A refusal sticks | `/code-review` and `/pr-review` do not re-offer that same claim unless the shipped public contract differs |

## Output

**Complete only when:** the applicable checklist is done, acceptance evidence is recorded (no open fails; blocked criteria stated), `/code-review` has run, and every Fix-now finding is fixed after explicit promotion or waived by name. Announce the completion summary in chat ([reference.md](reference.md#completion-summary)). When `/task` runs under a parent that owns shipping, return the completion evidence to it and skip ship Questions; otherwise offer ship Questions. Do not commit, open a PR, archive anything, or write a summary artifact unless the user asks.

**Pause:** stop dispatching work and leave the current phase and next action visible in chat. **Clear:** end the in-chat context; do not delete a user-requested artifact unless the user explicitly asks.

In a new chat, recover by following the [execution context authority order](../pack-shared/execution-context.md#authority): re-derive Git, ticket/PR, and repository facts, re-announce what is known, and ask only for missing user-owned decisions. Do not look for or recreate a resume tree.

## Apply

Run the [lifecycle](reference.md#lifecycle). If this chat owns shipping, offer ship Questions ([SKILL.md](SKILL.md)). If a parent already owns the ticket, branch, and PR, return evidence to that parent.

## Anti-patterns

- Declaring completion without acceptance evidence then `/code-review`
- Creating automatic runtime state instead of using the shared execution context
- Planning before Locked grill closing or omitting a locked behavioral rule from Active Rules
- Sending workers a plan path or hidden state instead of the applicable in-chat context
- Soloing non-trivial explore, implement, or review work on the parent instead of Task workers per [subagents.md](../pack-shared/subagents.md)
- Capping a wave at two Tasks when more independent surfaces are ready
- Fixing review findings without remediation analysis, explicit promotion, and a bounded Fix mode
- Treating a review fix as a fresh architecture or product outcome
- Asking yes/no for non-goals, plan split, or shared understanding
- Writing to a tracker, committing, or opening a PR without a separate user request (this chat owns shipping) or parent ownership (nested)
- Opening a PR without the Ship work rules and [pr-ship.md](../pack-shared/pr-ship.md)
- Writing or editing test files on this skill
- Suggesting a lock before grill Locked closing, or for behavior the grill did not record
- Treating silence, a refused brief, or a parent `recommended` default as acceptance
- Starting the implement wave while the lock question is still open

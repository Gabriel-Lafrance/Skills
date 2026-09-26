# Task doctrine

## Job

Autonomous loop toward one verifiable completion condition. Stay in **Agent mode**. No `SwitchMode`, no CreatePlan UI.

## Owns

The orchestrator loop: execution context, grill-before-plans, behavior-lock suggestion after that grill, lookup table, mandatory skill checklist, suitability, skip-grill, completion, pause, and recovery rules. The agent running `/task` does the work itself, one slice at a time.

## Does not own

- Code quality and structure bars: cite `quality:*` and `structure:*`
- UI and UX rules and `docs/design.md`: [user-experience.md](../rules/user-experience.md)
- Review disposition: `/review`
- How tests are written: [testing.md](../rules/testing.md), and only for briefs the user accepted
- Numbered lifecycle: [`reference.md`](reference.md#lifecycle) · [`SKILL.md`](SKILL.md)

## Cite keys

none (uses `quality:*` and `structure:*`)

## Bars

Use the shared [execution context](../rules/planning.md#execution-context) as the source of truth for this task. Keep the outcome, Done when, non-goals, rules that must stay true, current slices, Fix backlog, phase, and next action visible in chat.

Follow the shared stateless default: inline plan and slice contracts are normal; save an artifact only when the user asks and supplies or approves its destination.

**Rules that must stay true:** Every behavioral rule locked during the grill becomes a numbered rule (Rule 1, Rule 2) in the in-chat execution context with its enforcement and verification. A user can explicitly mark a statement as a preference, example, or non-binding idea instead.

**Grill before plans.** Do not issue a plan or slice contract until `/grill-me` announces Locked closing: non-goals, intended split, and shared-understanding summary (correct if wrong) unless the skip rule applies. Assign each rule to an intended slice or `all`. Behavior-lock briefs come after that closing, never during the grill. A fuzzy rule is not a test: the observable outcome has to be specific before a brief can cite it.

**Quality bar:** Acceptance evidence (Done when + rules that must stay true + cross-slice seams) and `/review` are mandatory, in that order, before declaring completion. There is no `/validate` skill.

### Lookup

| Need | Call |
| --- | --- |
| Ticket context | [Read the ticket or PR](#ticket-context) when there is one |
| Grill | `/grill-me` |
| Code quality | **[code-quality.md](../rules/code-quality.md) always** (grill + before every implement slice) |
| Structure | **[code-structure.md](../rules/code-structure.md) always** (grill + before every implement slice). For a typo or pure rename, apply it and keep the existing structure |
| UX source of truth | [user-experience.md](../rules/user-experience.md) and `docs/design.md` when the slice is user-facing UI. Write `docs/design.md` first if it is missing (`ux:initialization`) |
| Split | [Slice split](reference.md#slice-split) when multiple slices help |
| Plan contract | Issue [inline plan contracts](reference.md#inline-plan-contract) in chat |
| Judge | `/analyze` for how, impact, and risk |
| Build | This loop builds every slice itself; user-facing slices apply [user-experience.md](../rules/user-experience.md) ([Implement](reference.md#phase-1-plan-and-build)) |
| Tests | After Locked grill, suggest locks that cite a grilled rule ([reference.md](reference.md#behavior-lock-suggestion)). The user may refuse every test. Accepted briefs follow [testing.md](../rules/testing.md) |
| Bug mid-build | Scoped Fix mode (or `/analyze` → continue this task) |
| Review remediation | `/analyze` before Fix mode |
| Gate out | Acceptance evidence then **`/review`** |

Inside this loop, call child skills (`/grill-me`, `/review`, `/analyze`). Each follows its [`SKILL.md`](SKILL.md); this parent already owns the next step.

### Mandatory skill checklist

Track these rows in the in-chat execution context or a concise progress message. Do not declare completion until every applicable row is done:

| Skill | Required? | Notes |
| --- | --- | --- |
| Ticket or PR read | If ticket | [Read only](#ticket-context) |
| `/grill-me` | Yes* | *Unless skip-grill rule |
| Code quality rules | **Yes** | During grill and before/during every implement slice |
| Code structure rules | **Yes** | During grill and before/during every implement slice. Apply even for a one-file fix |
| User experience | If UI | Apply [user-experience.md](../rules/user-experience.md). Write `docs/design.md` first if it is missing |
| Slice split | If multi-slice | Announce inline slices ([reference.md](reference.md#slice-split)) |
| Inline plan contracts | Yes | One or more [plan contracts](reference.md#inline-plan-contract) in chat |
| Non-UI slices | If non-UI | Built by this loop; update **Current slices** after each |
| Acceptance evidence | Yes | Path walk, terminals |
| Behavior locks | When a complex public rule exists | After the plan names the public entry. Wait. Refusing every test is complete |
| `/review` | Yes | Runs after acceptance evidence. Standards and Spec. No Design axis |

### Suitability and skip grill

**Hard reject:** vague wishes or open-ended research with no binary done state. Multiple unrelated outcomes need separate `/task` contexts.

**Skip grill only if all are true:** the ticket or user already has a binary Done when; no open product, UX, architecture, or design decision remains; no behavioral rule is unrecorded; and the user said `no grill` / `skip grill`, or the work is an obvious single-file fix. Capture explicit behavioral rules as rules that must stay true even when skipping.

For ticket-driven tasks, read the ticket or PR first, then grill open decisions.

### Ticket context

Read a ticket or PR as plain context. Do not change status, comment, assign, or close unless the user asks in that turn. Closing is the user's job (by hand or on merge).

- **Detect:** `IN-1234` style ids and `linear.app` URLs are Linear. `#123`, `owner/repo#123`, and `github.com/.../issues/N` or `/pull/N` are GitHub. A bare number is ambiguous: ask once.
- **Read:** GitHub with the harness GitHub tool or `gh issue view` / `gh pr view`. Linear with its read tool or API. Keep the title, ask, Done when, constraints, and non-goals in the execution context. Link the source instead of pasting the body again.
- **No tool or not signed in:** say so, and ask the user to connect it or paste the body once. Never invent a ticket from its id.

### Behavior locks

Suggest tests only from grilled rules that must stay true, using the [testing.md](../rules/testing.md#when-a-test-is-worth-writing) bar for what is worth locking. Detail and the question template live in [reference.md](reference.md#behavior-lock-suggestion).

| Rule | Meaning |
| --- | --- |
| After the grill is locked | No brief until Locked closing, and until the plan names the public entry. A typo, rename, or other trivial skip offers nothing. When skip-grill applies because the rules are already specific, suggest from those rules |
| Cite a grilled rule | Why and What come from that rule's observable outcome. A brief with no rule is invalid |
| Same bar as [testing.md](../rules/testing.md#when-a-test-is-worth-writing) | Offer a complex public surface that can silently drift: authorization, ownership, safe-to-retry, a domain rule, a facade, a stateful class, or a complex hook. Skip a thin wrapper, formatter, UI chrome, generated code, types-only file, coverage target, and tautology |
| The user chooses | One Questions batch. Every brief has a no. Silence is not yes. A parent does not take `recommended` |
| A correction reopens the rule | "That is not the behavior" updates the rule and discards briefs that cited it. Do not build from the old rule |
| Written by testing.md | An accepted brief is a test slice after the public entry exists, written by following [testing.md](../rules/testing.md) |
| A refusal sticks | `/review` does not re-offer that same claim unless the shipped public contract differs |

## Output

**Complete only when:** the applicable checklist is done, acceptance evidence is recorded (no open fails; blocked criteria stated), `/review` has run, and every Fix-now finding is fixed after explicit promotion or waived by name. Announce the completion summary in chat ([reference.md](reference.md#completion-summary)). When `/task` runs under a parent that owns shipping, return the completion evidence to it and skip ship Questions; otherwise offer ship Questions. Do not commit, open a PR, archive anything, or write a summary artifact unless the user asks.

**Pause:** stop work and leave the current phase and next action visible in chat. **Clear:** end the in-chat context; do not delete a user-requested artifact unless the user explicitly asks.

In a new chat, recover by following the [execution context authority order](../rules/planning.md#authority): re-derive Git, ticket/PR, and repository facts, re-announce what is known, and ask only for missing user-owned decisions. Do not look for or recreate a resume tree.

## Apply

Run the [lifecycle](reference.md#lifecycle). If this chat owns shipping, offer ship Questions ([SKILL.md](SKILL.md)). If a parent already owns the ticket, branch, and PR, return evidence to that parent.

## Anti-patterns

- Declaring completion without acceptance evidence then `/review`
- Creating automatic runtime state instead of using the shared execution context
- Planning before Locked grill closing or omitting a locked behavioral rule from the rules that must stay true
- Implementing from a plan path or hidden state instead of the applicable in-chat context
- Fixing review findings without remediation analysis, explicit promotion, and a bounded Fix mode
- Treating a review fix as a fresh architecture or product outcome
- Asking yes/no for non-goals, plan split, or shared understanding
- Writing to a tracker, committing, or opening a PR without a separate user request (this chat owns shipping) or parent ownership (nested)
- Opening a PR without [shipping.md](../rules/shipping.md)
- Writing or editing a test the user did not accept
- Suggesting a lock before grill Locked closing, or for behavior the grill did not record
- Treating silence, a refused brief, or a parent `recommended` default as acceptance
- Starting implementation while the lock question is still open

# Task doctrine

## Job

Autonomous loop toward one verifiable completion condition. Stay in **Agent mode** (no `SwitchMode`, no CreatePlan UI).

## Owns

The orchestrator loop: execution context, grill before plans, behavior-lock suggestion, lookup table, skill checklist, suitability, skip-grill, completion, pause, and recovery. The agent running `/task` builds every slice itself, one at a time.

## Does not own

- Code quality and structure bars: cite `quality:*` and `structure:*`
- UI and UX rules and `docs/design.md`: [user-experience.md](../rules/user-experience.md)
- Review disposition: `/review`
- Verification method and scope: `/verification`
- How tests are written: [testing.md](../rules/testing.md), and only for briefs the user accepted
- Numbered lifecycle: [`reference.md`](reference.md#lifecycle) · [`SKILL.md`](SKILL.md)

## Bars

Use the shared [execution context](../rules/planning.md#execution-context) as the source of truth. Keep the outcome, Done when, non-goals, rules that must stay true, current slices, Fix backlog, phase, and next action visible in chat. Inline plan and slice contracts are normal. Save an artifact only when the user asks and approves its destination.

**Rules that must stay true.** Every behavioral rule locked during the grill becomes a numbered rule (Rule 1, Rule 2) in the execution context, with its enforcement and verification. The user can mark a statement as a preference, example, or non-binding idea instead.

**Grill before plans.** Issue a plan or slice contract only after `/grill-me` sends the Locked in message: non-goals, intended split, shared-understanding summary, and the rejected alternative (`none` only for a typo or pure rename). The skip-grill rule below is the one exception. Assign each rule to a slice or `all`. Send behavior-lock briefs after the Locked in message, never during the grill. Make each rule's observable outcome specific, because a brief cannot cite a fuzzy rule.

**Quality bar.** Two gates run before completion, in parallel, each in its own subagent:

- `/verification` gives the acceptance evidence for Done when, the rules that must stay true, and cross-slice seams, sized to what the work changed ([scope](../verification/doctrine.md#scope-to-the-change)).
- `/review` gives the Standards and Spec findings.

Launch both in one step so they run at the same time, then judge their handoffs here. If the harness has no subagent, run `/verification` and then `/review` in this context. There is no `/validate` skill.

### Lookup

| Need | Call |
| --- | --- |
| Ticket context | [Read the ticket or PR](#ticket-context) when there is one |
| Grill | `/grill-me` |
| Code quality | **[code-quality.md](../rules/code-quality.md) always** (grill and every implement slice) |
| Structure | **[code-structure.md](../rules/code-structure.md) always** (grill and every implement slice). For a typo or pure rename, apply it and keep the existing structure |
| UX source of truth | [user-experience.md](../rules/user-experience.md) and `docs/design.md` when the slice is user-facing UI. Write `docs/design.md` first if it is missing (`ux:initialization`) |
| Split | [Slice split](reference.md#slice-split) when multiple slices help |
| Plan contract | Issue [inline plan contracts](reference.md#inline-plan-contract) in chat |
| Judge | `/analyze` for how, impact, and risk |
| Build | This loop builds every slice itself; user-facing slices apply [user-experience.md](../rules/user-experience.md) ([Implement](reference.md#phase-1-plan-and-build)) |
| Tests | After the Locked in message, suggest locks that cite a grilled rule ([reference.md](reference.md#behavior-lock-suggestion)). The user may refuse every test. Accepted briefs follow [testing.md](../rules/testing.md) |
| Bug mid-build | Scoped Fix mode (or `/analyze` → continue this task) |
| Review remediation | `/analyze` before Fix mode |
| Gate out | **`/verification`** and **`/review`**, each in its own subagent, launched together |

Inside this loop, call child skills (`/grill-me`, `/verification`, `/review`, `/analyze`). Each follows its [`SKILL.md`](SKILL.md); this parent already owns the next step.

### Skill checklist

Track these rows in the execution context or a short progress message. Declare completion when every applicable row is done:

| Skill | Required? | Notes |
| --- | --- | --- |
| Ticket or PR read | If ticket | [Read only](#ticket-context) |
| `/grill-me` | Yes* | *Unless the skip-grill rule applies |
| Code quality rules | **Yes** | During the grill and every implement slice |
| Code structure rules | **Yes** | During the grill and every implement slice, even for a one-file fix |
| User experience | If UI | Apply [user-experience.md](../rules/user-experience.md). Write `docs/design.md` first if it is missing |
| Slice split | If multi-slice | Announce inline slices ([reference.md](reference.md#slice-split)) |
| Inline plan contracts | Yes | One or more [plan contracts](reference.md#inline-plan-contract) in chat |
| Non-UI slices | If non-UI | Built by this loop; update **Current slices** after each |
| Behavior locks | When a complex public rule exists | After the plan names the public entry. Wait for the answer. Refusing every test is a complete answer |
| `/verification` | Yes | Own subagent, parallel with `/review`. Its handoff is the acceptance evidence |
| `/review` | Yes | Own subagent, parallel with `/verification`. Standards and Spec, no Design axis |

### Suitability and skip grill

**Hard reject:** vague wishes or open-ended research with no binary done state. Give multiple unrelated outcomes separate `/task` contexts.

**Skip the grill only if all are true:** the ticket or user already has a binary Done when; no open product, UX, architecture, or design decision remains; no behavioral rule is unrecorded; and the user said `no grill` or `skip grill`, or the work is an obvious single-file fix. Record explicit behavioral rules as rules that must stay true even when skipping.

For a ticket-driven task, read the ticket or PR first, then grill the open decisions.

### Ticket context

Read a ticket or PR as plain context. Change its status, comment, assignee, or state only when the user asks in that turn. Closing is the user's job (by hand or on merge).

- **Detect:** `IN-1234` style ids and `linear.app` URLs are Linear. `#123`, `owner/repo#123`, and `github.com/.../issues/N` or `/pull/N` are GitHub. A bare number is ambiguous: ask once.
- **Read:** GitHub with the harness GitHub tool or `gh issue view` / `gh pr view`. Linear with its read tool or API. Keep the title, ask, Done when, constraints, and non-goals in the execution context. Link the source instead of pasting the body again.
- **No tool or not signed in:** say so, and ask the user to connect it or paste the body once. Take the ticket content only from its source.

### Behavior locks

Suggest tests only from grilled rules that must stay true, using the [testing.md](../rules/testing.md#when-a-test-is-worth-writing) bar. Detail and the question template are in [reference.md](reference.md#behavior-lock-suggestion).

| Rule | Meaning |
| --- | --- |
| Wait for the Locked in message | No brief until the Locked in message is sent and the plan names the public entry. A typo, rename, or other trivial change offers nothing. When skip-grill applies because the rules are already specific, suggest from those rules |
| Cite a grilled rule | Why and What come from that rule's observable outcome. A brief with no rule is invalid |
| Same bar as [testing.md](../rules/testing.md#when-a-test-is-worth-writing) | Offer a complex public surface that can silently drift: authorization, ownership, safe-to-retry, a domain rule, a facade, a stateful class, or a complex hook. Skip a thin wrapper, formatter, UI chrome, generated code, types-only file, coverage target, and tautology |
| The user chooses | One Questions batch. Every brief has a no. Silence is not yes. A parent does not take `recommended` |
| A correction reopens the rule | "That is not the behavior" updates the rule and discards briefs that cited it. Build from the corrected rule |
| Written by testing.md | An accepted brief is a test slice after the public entry exists, written by following [testing.md](../rules/testing.md) |
| A refusal sticks | `/review` re-offers that claim only when the shipped public contract differs |

## Output

**Complete when:** the checklist is done, both gate handoffs are in (no open fails; blocked criteria stated), and every Fix-now finding is fixed after explicit promotion or waived by name. Announce the completion summary in chat ([reference.md](reference.md#completion-summary)). Under a parent that owns shipping, return the completion evidence to it and skip ship Questions. Otherwise offer ship Questions. Commit, open a PR, archive, or write a summary artifact only when the user asks.

**Pause:** stop work and leave the current phase and next action visible in chat. **Clear:** end the in-chat context. Delete a user-requested artifact only when the user asks.

**Recover in a new chat** by following the [execution context authority order](../rules/planning.md#authority): re-derive Git, ticket/PR, and repository facts, re-announce what is known, and ask only for missing user-owned decisions.

## Apply

Run the [lifecycle](reference.md#lifecycle). If this chat owns shipping, offer ship Questions ([SKILL.md](SKILL.md)). If a parent already owns the ticket, branch, and PR, return evidence to that parent.

## Anti-patterns

- Declaring completion before both `/verification` and `/review` have returned
- Running `/verification` and `/review` one after the other when the harness has subagents
- Asking `/verification` to exercise layers the work did not touch
- Fixing review findings without remediation analysis, explicit promotion, and a bounded Fix mode
- Treating a review fix as a fresh architecture or product outcome
- Asking yes/no for non-goals, plan split, or shared understanding
- Suggesting a lock for behavior the grill did not record
- Treating silence, a refused brief, or a parent `recommended` default as acceptance
- Starting implementation while the lock question is open

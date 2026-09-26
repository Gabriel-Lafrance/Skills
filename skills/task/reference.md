# Task reference (in-chat templates)

Load when establishing or recovering a task, issuing a plan or slice contract, posting progress, or summarizing completion. Rules stay in [doctrine.md](doctrine.md).

## Stateless default

The shared [execution context](../pack-shared/execution-context.md) is the only
automatic state. Persist only a user-requested artifact at an approved
destination.

Plans, slices, grill outcomes, progress, and review findings stay in chat. If the user asks to save an analysis, plan, or summary and supplies or approves a destination, write only that artifact. It does not become hidden state or a requirement for recovery.

## Required execution context

Use the shared template, keeping only fields that matter to current work:

```markdown
## Execution context
**Outcome:** …
**Done when:** …
**Non-goals:** …
**Ticket / PR:** <reference | none>
**Fixed point:** <base...HEAD | none>
**Lane:** <allowed paths and symbols>
**Phase:** grill | plan | locks | implement | acceptance | review | fix | done
**Next:** …

### Locked decisions
- <user decision, waiver, or promotion>

### Rules that must stay true
| ID | Rule | How we enforce it | How we check it |
| --- | --- | --- | --- |
| Rule 1 | … | … | … |

### Behavior locks
- <none | waiting on the user | Rule N accepted | Rule N refused>

### Current slices
- <scope, done when, ownership, dependencies, and status>

### Fix backlog
- `finding-id`: fix now | follow-up | waived
```

Do not infer a user decision, waiver, invariant, or promotion from repository facts. Re-announce settled decisions when they matter to a later phase.

## Inline plan contract

`/task` produces this in chat for one slice (after Locked grill closing). It is not a file path or an instruction to write one.

```markdown
# Plan: <title>
**Slice:** <ordered ID>
**Status:** proposed | ready | implementing | done
**Blocked by:** <none | slice IDs>

## Outcome
<one verifiable slice result>

## Scope and lane
<allowed paths/symbols; explicit exclusions>

## Approach
<concrete implementation shape; no unresolved Option A/B>

## Taste
- **KISS / principles:** held | name the violation to fix in this slice
- **Sibling cited:** <good path | greenfield | correcting debt>

## Architecture
- **Service / public API:** <owns or calls>
- **Primitives:** <reuse | new inside which module | none>
- **Folder map:** <owning folder this slice must create or use; no mixed-parent dump>
- **Scalability:** <stored-on-write | none for this slice>

## User experience
- **User-facing:** yes (apply [user-experience.md](../rules/user-experience.md)) | no
- **File:** `docs/design.md` present | missing (write it first from the routes in code)

## Rules that must stay true
| ID | Role | How we enforce it | How we check it |
| --- | --- | --- | --- |
| Rule 1 | implement | … | … |

## Coordination
- **Owner:** …
- **Dependencies:** …
- **Handoffs / seams:** …
- **Must not touch:** …

## Done when
- [ ] …

## Out of scope
- …
```

Assign relevant rules that must stay true to each contract. Keep the frontier and dependencies under **Current slices** in the execution context.

## Slice split

A slice is small enough when it has one clear **what** (one seam, or even one function), 1 to 3 binary checks that verify it alone, and its contract plus working set stay around 30% of the context window. If it still needs "and then also", or building it means re-mapping the repo, split again. Keep independent slices separate. Prefer thin vertical slices over horizontal layers. For wide refactors: expand, migrate in small batches, then contract.

Announce the split in chat, blockers first:

```markdown
# Split: <parent title>

### 1: <imperative title>
- **Outcome:** <what becomes true>
- **Lane / entry / folder:** <paths; owning folder when files are added>
- **Rules that must stay true:** Rule 1, …
- **Done when:** <1 to 3 binary checks>
- **Blocked by:** none

**Frontier:** 1
```

## New-chat recovery

Do not search for a task directory, status file, archive, or resume tree. Follow the [authority order](../pack-shared/execution-context.md#authority):

1. Read the current request and decisions settled in this chat.
2. Re-derive named ticket/PR facts and comments.
3. Re-derive Git branch, diff, commits, and repository facts.
4. Read repository rules and committed project documentation.
5. Use a user-requested artifact only when its path was supplied.

State the recovered outcome, lane, fixed point, known rules, and phase in chat. Ask only for missing user-owned decisions; do not re-grill a decision carried by the request, ticket/PR, approved artifact, or repository rules merely because the chat is new.

## Progress and pause

After a phase change or finished slice, post one concise chat line:

```markdown
**Progress:** grill ✓ · slices 1/3 · implementing `02` · next: acceptance
```

For a pause, state the current phase, completed slices, blocker, and next action in chat. A later chat re-derives repository facts and asks only for decisions it cannot recover.

## Completion summary

After acceptance evidence is recorded and `/review` has run, report the outcome without archiving anything:

```markdown
# ✅ Task complete: <short title>

## What changed
- …

## Evidence
- Acceptance: <Done when / rules that must stay true / seams: path walk, terminal>
- `/review`: …

## Decisions and rules
- Rule 1: … verified by …

## Fix backlog
- <none | waived finding and user decision>

## Behavior locks
- <none offered | Rule N accepted, file, command | Rule N refused>

## Manual next steps
- <none | user action>
```

If review selected a Fix-now item, completion waits for remediation analysis,
explicit promotion, bounded Fix mode, re-checked acceptance evidence, and
`remediation` review, or a named user waiver.

## Ship questions

After the completion summary, ask once only when this chat owns shipping.
The default is no unless the user already asked to ship:

```markdown
## Questions
Reply like: 1b

1. Ship this work?
   - a) yes: cut a branch, commit, push, and draft a PR for your approval
   - b) no: leave the changes uncommitted ← recommended
```

Wait for the answer. On yes, follow the Process in [ship.md](../pack-shared/ship.md)
from its first step: branch, commit, push, PR draft, approval. When `/task`
runs under a parent that owns shipping, return the completion evidence to the
parent instead; it owns the branch, preflight, draft visibility, and PR
creation.

## Behavior-lock suggestion

Run this after grill Locked closing and after the inline plan names the public entry. Do not run it during an open grill, on a trivial skip (typo, rename, one-line fix), or during Fix mode. When skip-grill applies because the rules are already specific, suggest from those rules.

1. Walk each rule that must stay true. Offer a brief only when [`/create-test`](../create-test/doctrine.md) would lock it: a complex public surface whose behavior can silently drift (authorization, ownership, safe-to-retry, a domain rule, a facade, a stateful class, or a complex hook).
2. Skip a thin wrapper, formatter, UI chrome, generated code, types-only file, coverage target, tautology, typo, rename, one-line fix, and any statement the user called a preference, example, or non-binding idea.
3. Every brief cites one grilled rule. Why and What come from that rule. How names the public entry in the plan. If the plan has no public entry, offer nothing.
4. If no brief qualifies, record `Behavior locks: none` and continue. Do not ask.
5. If one or more qualify, send one Questions-only message and wait. This question is a hard stop. Silence is not a yes. Do not start implementation while it is open. The briefs are the last check that the grilled rule is the behavior the user wants locked.

```markdown
## Questions
Reply like: 1a 2b

1. Lock Rule 2 on `makeUserPay`? Why: a double submit could charge twice. What: the same retry key creates one charge. How: call `makeUserPay` twice with that key and assert one charge.
   - a) yes ← recommended
   - b) no, do not add this test
2. Lock Rule 3 on `refundPayment`? Why: a caller could refund someone else's payment. What: only the owner can refund. How: call `refundPayment` as a non-owner and assert it is rejected.
   - a) yes ← recommended
   - b) no, do not add this test
```

Recommend `yes` for a claim `/create-test` would lock. The user can answer `no` on every line.

A correction ("that is not the behavior") updates the rule, discards briefs that cited it, and suggests again from the corrected rule. Do not implement from the old rule.

`no` means no test. The rule still stands. Record the refusal. Do not ask again for that same claim in `/review` unless the shipped public contract differs.

`yes` adds a test slice after the product slice that creates the public entry. Write it by following `/create-test` with the accepted Why / What / How, the rule id, and the public entry. Acceptance evidence includes the [lock handoff](../create-test/reference.md#handoff).

## Lifecycle

Numbered process for `/task`. Rules stay in [doctrine.md](doctrine.md). Nested vs one-off shipping lives in [SKILL.md](SKILL.md).

### Phase 0: establish context and grill

1. Re-derive the ticket/PR, Git fixed point, repository facts, and applicable project rules as needed; state them in the in-chat execution context.
2. State the outcome, Done when, non-goals, lane, phase, and next action. Carry forward only user decisions already settled in this chat or an explicitly supplied artifact.
3. Unless the skip rule applies, run `/grill-me` fully. It applies the rules in [code-quality.md](../rules/code-quality.md) and [code-structure.md](../rules/code-structure.md) on every run ([standards.md](../pack-shared/standards.md)). For user-facing work it also applies [user-experience.md](../rules/user-experience.md) and the current `docs/design.md`.
4. Record Locked decisions and rules that must stay true in chat. Every locked behavioral answer becomes a numbered rule (Rule 1, Rule 2) with authoritative enforcement and verification. The observable outcome (who acts, what they do, what stays true, what a repeat or a bypass does) has to be specific. A fuzzy rule cannot become a test later.
5. Announce the non-goals, intended slice split, and shared-understanding summary. Ask only real open questions in the same batch.
6. Do not suggest tests in this phase.

On a Locked correction or unanswered real question, revise or wait. Never infer a user decision, waiver, invariant, or promotion from code alone.

### Phase 1: plan and build

**Explore and shape.** Find the relevant paths and snippets. Run `/analyze` when how, impact, or risk needs judging. Confirm Taste and Architecture decisions against the grill ([code-quality.md](../rules/code-quality.md) and [code-structure.md](../rules/code-structure.md) must already be applied this turn), and keep the locked structure excerpt in the plan contracts. For UI, also confirm the choices against [user-experience.md](../rules/user-experience.md) and `docs/design.md` (write the file first if it is missing).

**Split and plan.** Prefer small, ordered slices that meet the [slice split](#slice-split) bar; a what can be one function. Announce the split in the grill's Locked message (the agent owns it; do not ask yes/no). Then issue an [inline plan contract](#inline-plan-contract) for each slice. The contract states **what** and need-to-know, not how. If the split changes, re-announce the new Locked split before implementation. Do not write an INDEX, plan path, or other runtime file.

**Suggest behavior locks.** Run [Behavior-lock suggestion](#behavior-lock-suggestion). Phase is `locks` while the question is open. If the user corrects a rule, return to grill for that rule before implementing. If they accept or refuse without correcting the rule, record it and continue. If nothing qualifies, record none and continue.

**Implement.** Build ready frontier slices one at a time, in dependency order. User-facing slices (screens, components, styling, visible copy) apply [user-experience.md](../rules/user-experience.md) and `docs/design.md`. For each slice:

1. Stay in the slice's lane and follow its plan contract and the locked structure excerpt. Create the owning folder from the folder map before its files. Do a required behavior-preserving move before feature code and show the old behavior still holds.
2. Reuse existing services and one-job helpers. If the slice seems to need a new shared API, service, or lane, mark it `blocked` and name the smallest option instead of inventing one.
3. Gather slice-local evidence only: existing terminal output first, then one narrow command if needed.
4. Do not write tests in a product slice. After the public entry exists, write each accepted lock as its own slice through `/create-test`.
5. Update **Current slices** in chat with status, evidence, findings, and any changed interface. If acceptance, a dependency, or a structural decision is missing, mark the slice `blocked` and name the smallest decision needed.

If ready slices remain, start the next one. Enter acceptance evidence only when every slice is done, blocked, or explicitly waived.

**Acceptance evidence and review.** After every slice is implemented:

1. Confirm **Done when** (task and slice) and rules that must stay true, including cross-slice seams, with path walks and terminal output. When a lock was accepted, include the lock handoff and the focused test result. No browser validation, no screenshots. Record pass / fail / blocked per criterion in chat. Do not call an unperformed check a pass.
2. Always run **`/review`** next.
3. Put each review finding in the in-chat **Fix backlog** as `fix now`, `follow-up`, or `waived`.
4. For selected `fix now` findings, run `/analyze` in review-remediation mode, present the proposed correction, and enter Fix mode only after explicit user promotion.
5. If the user declines a fix, completion remains blocked until every Fix-now finding is fixed or waived by name.
6. Do not open a new behavior-lock suggestion here. A lock the review still wants follows the review contract, and the user starts `/create-test` for that one.

### Fix mode (review remediation only)

Fix mode is one bounded slice of the current task, not fresh product discovery:

1. Carry only explicitly promoted findings into the current slice. Each cites its review finding, violated rule that must stay true, Done when item, correctness/security issue, or regression.
2. Grill only the enforcement, footprint, and observable behavior needed to clear those findings. Preserve existing rules that must stay true; add one only when the finding exposes an unrecorded behavioral rule. Do not suggest a new test from Fix mode.
3. Prefer the smallest authoritative correction. Do not add queues, retries, wrappers, or new services unless the named finding proves a guard is insufficient.
4. No new feature scope, optional cleanup, or architecture move unless the named finding requires it.
5. Re-check the named findings and rules that must stay true with acceptance evidence, then run `/review` in `remediation` mode over the backlog, touched paths, direct regressions, correctness, and security.

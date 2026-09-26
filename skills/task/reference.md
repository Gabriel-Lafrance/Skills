# Task reference (in-chat templates)

Load when establishing or recovering a task, issuing a plan or slice contract, posting progress, or summarizing completion. Rules stay in [doctrine.md](doctrine.md).

## Execution context

Keep the [execution context](../pack-shared/execution-context.md#context-in-chat) in chat, with only the fields that matter to current work. It is the only automatic state. Plans, slices, grill outcomes, progress, and review findings stay in chat. Write an analysis, plan, or summary only when the user asks and supplies or approves the destination; it never becomes hidden state or a requirement for recovery.

Do not infer a user decision, waiver, invariant, or promotion from repository facts. Re-announce settled decisions when they matter to a later phase.

## Inline plan contract

One per slice, in chat, after Locked grill closing. It is not a file.

```markdown
# Plan: <title>
**Slice:** <ordered ID> · **Status:** proposed | ready | implementing | done · **Blocked by:** <none | slice IDs>

**Outcome:** <one verifiable slice result>
**Scope and lane:** <allowed paths/symbols; explicit exclusions>
**Approach:** <concrete implementation shape; no unresolved Option A/B>

## Code quality and structure
- **Keep it simple (KISS) / principles:** held | name the violation to fix in this slice
- **Sibling cited:** <good path | greenfield | correcting debt>
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
- **Owner:** … · **Dependencies:** … · **Handoffs / seams:** … · **Must not touch:** …

## Done when
- [ ] …

**Out of scope:** …
```

Keep the frontier and dependencies under **Current slices** in the execution context.

## Slice split

A slice is small enough when it has one clear **what** (one seam, or even one function), 1 to 3 binary checks that verify it alone, and its contract plus working set stay around 30% of the context window. If it still needs "and then also", or building it means re-mapping the repo, split again. Prefer thin vertical slices over horizontal layers. For wide refactors: expand, migrate in small batches, then contract.

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

Do not search for a task directory, status file, archive, or resume tree. Follow the [authority order](../pack-shared/execution-context.md#authority), then state the recovered outcome, lane, fixed point, known rules, and phase in chat. Ask only for missing user-owned decisions. Do not re-grill a decision the request, ticket/PR, approved artifact, or repository rules already carry.

## Progress and pause

After a phase change or finished slice, post one line:

```markdown
**Progress:** grill ✓ · slices 1/3 · implementing `02` · next: acceptance
```

For a pause, state the phase, completed slices, blocker, and next action.

## Completion summary

After acceptance evidence and `/review`, report the outcome without archiving anything:

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

A Fix-now item blocks completion until remediation analysis, explicit promotion, bounded Fix mode, re-checked acceptance evidence, and a `remediation` review, or a named user waiver.

## Ship questions

Ask once, after the completion summary, only when this chat owns shipping. Default is no unless the user already asked to ship:

```markdown
## Questions
Reply like: 1b

1. Ship this work?
   - a) yes: cut a branch, commit, push, and draft a PR for your approval
   - b) no: leave the changes uncommitted ← recommended
```

Wait. On yes, follow the Process in [ship.md](../pack-shared/ship.md) from its first step. Under a parent that owns shipping, return the completion evidence to the parent instead.

## Behavior-lock suggestion

Run after grill Locked closing, once the inline plan names the public entry. The bar is the [Behavior locks table](doctrine.md#behavior-locks) in the doctrine. Never during an open grill, a trivial skip, or Fix mode.

1. Walk each rule that must stay true. Offer a brief only when it passes the `/create-test` bar.
2. Every brief cites one grilled rule. Why and What come from that rule. How names the public entry in the plan. No public entry, no brief.
3. If no brief qualifies, record `Behavior locks: none` and continue without asking.
4. Otherwise send one Questions-only message and wait. It is a hard stop: silence is not yes, and implementation does not start while it is open.

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

- **Correction** ("that is not the behavior"): update the rule, discard its briefs, suggest again from the corrected rule.
- **No:** no test; the rule still stands. Record the refusal.
- **Yes:** add a test slice after the product slice that creates the public entry. Follow `/create-test` with the accepted Why / What / How, the rule id, and the public entry. Acceptance evidence includes the [lock handoff](../create-test/reference.md#handoff).

## Lifecycle

Numbered process for `/task`. Nested vs one-off shipping lives in [SKILL.md](SKILL.md).

### Phase 0: establish context and grill

1. Re-derive the ticket/PR, Git fixed point, repository facts, and project rules as needed. State outcome, Done when, non-goals, lane, phase, and next action in the execution context. Carry forward only user decisions settled in this chat or an explicitly supplied artifact.
2. Unless skip-grill applies, run `/grill-me` fully. It applies [code-quality.md](../rules/code-quality.md) and [code-structure.md](../rules/code-structure.md), plus [user-experience.md](../rules/user-experience.md) and `docs/design.md` for user-facing work.
3. Every locked behavioral answer becomes a numbered rule (Rule 1, Rule 2) with enforcement and verification. The observable outcome (who acts, what they do, what stays true, what a repeat or a bypass does) must be specific, or it cannot become a test later.
4. Announce non-goals, intended slice split, and the shared-understanding summary. Ask only real open questions in the same batch. Do not suggest tests yet.

On a Locked correction or unanswered question, revise or wait.

### Phase 1: plan and build

**Explore and shape.** Find the relevant paths. Run `/analyze` when how, impact, or risk needs judging. Confirm code quality and structure choices against the grill and keep the locked structure excerpt in the plan contracts. For UI, confirm against user-experience.md and `docs/design.md` (write it first if missing).

**Split and plan.** Announce a [slice split](#slice-split) in the grill's Locked message (the agent owns it; do not ask yes/no). Then issue an [inline plan contract](#inline-plan-contract) per slice, stating **what** and need-to-know, not how. If the split changes, re-announce it before implementing. No INDEX, plan path, or runtime file. Then run the [behavior-lock suggestion](#behavior-lock-suggestion); phase is `locks` while it is open, and a corrected rule returns to grill before implementing.

**Implement.** Build ready frontier slices one at a time, in dependency order. User-facing slices (screens, components, styling, visible copy) apply user-experience.md and `docs/design.md`. For each slice:

1. Stay in its lane and follow its contract and structure excerpt. Create the owning folder before its files. Do a required behavior-preserving move before feature code and show the old behavior still holds.
2. Reuse existing services and one-job helpers. If the slice seems to need a new shared API, service, or lane, mark it `blocked` and name the smallest option.
3. Gather slice-local evidence only: existing terminal output first, then one narrow command if needed.
4. No tests in a product slice. Each accepted lock is its own `/create-test` slice after the public entry exists.
5. Update **Current slices** with status, evidence, findings, and changed interfaces. Missing acceptance, dependency, or structural decision: mark `blocked` and name the smallest decision needed.

Enter acceptance evidence only when every slice is done, blocked, or explicitly waived.

**Acceptance evidence and review.**

1. Confirm **Done when** (task and slice) and rules that must stay true, including cross-slice seams, with path walks and terminal output. Include the lock handoff and focused test result for each accepted lock. No browser validation or screenshots. Record pass / fail / blocked per criterion; an unperformed check is not a pass.
2. Always run **`/review`** next. Put each finding in the **Fix backlog** as `fix now`, `follow-up`, or `waived`.
3. For selected `fix now` findings, run `/analyze` in review-remediation mode, present the correction, and enter Fix mode only after explicit user promotion. A declined fix blocks completion until it is fixed or waived by name.
4. Do not open a new behavior-lock suggestion here. A lock the review still wants follows the review contract, and the user starts `/create-test` for it.

### Fix mode (review remediation only)

One bounded slice of the current task, not fresh product discovery:

1. Carry only explicitly promoted findings. Each cites its review finding, violated rule that must stay true, Done when item, correctness/security issue, or regression.
2. Grill only the enforcement, footprint, and observable behavior needed to clear them. Keep existing rules; add one only when the finding exposes an unrecorded behavioral rule. No new test suggestion.
3. Prefer the smallest authoritative correction. No queues, retries, wrappers, new services, feature scope, optional cleanup, or structure move unless the named finding requires it.
4. Re-check the findings and rules with acceptance evidence, then run `/review` in `remediation` mode over the backlog, touched paths, direct regressions, correctness, and security.

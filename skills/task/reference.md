# Task reference (in-chat templates)

Load when establishing or recovering a task, issuing a plan or slice contract, posting progress, or summarizing completion. Rules stay in [doctrine.md](doctrine.md).

## Execution context

Keep the [execution context](../rules/planning.md#context-in-chat) in chat, with only the fields that matter to current work. It is the only automatic state. Plans, slices, grill outcomes, progress, and review findings stay in chat. Write an analysis, plan, or summary only when the user asks and supplies or approves the destination; it never becomes hidden state or a requirement for recovery.

Take user decisions, waivers and authority to promote fixes from the user, never from repository facts or a review verdict. The active orchestrator promotes bounded fixes under that authority. Re-announce settled decisions when they matter to a later phase.

## Inline plan contract

One per slice, in chat, after the Locked in message. It is not a file.

```markdown
# Plan: <title>
**Slice:** <ordered ID> · **Status:** proposed | ready | implementing | done · **Blocked by:** <none | slice IDs>

**Outcome:** <one verifiable slice result>
**Scope and lane:** <allowed paths/symbols; explicit exclusions>
**Approach:** <concrete implementation shape; no unresolved Option A/B>

## Code quality and structure
- **Keep it simple (KISS) / principles:** held | name the violation to fix in this slice
- **Example matched:** <example heading, plus the app sibling that matches it, if any | correcting debt>
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

Follow [recovery and completion](../rules/execution.md#recovery-and-completion), then state the recovered outcome, lane, fixed point, known rules and next action.

## Progress and pause

After a phase change or finished slice, post one line:

```markdown
**Progress:** grill ✓ · slices 1/3 · implementing `02` · next: acceptance
```

For a pause, state the phase, completed slices, blocker, and next action.

## Completion summary

After both gate handoffs are in, report the outcome in chat:

```markdown
# ✅ Task complete: <short title>

## What changed
- …

## Evidence
- `/verification`: <verified | failed | inconclusive, per Done when / rule / seam>
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

Apply the shared [remediation](../rules/execution.md#remediation) and [completion](../rules/execution.md#recovery-and-completion) contracts. Include stable acceptance, finding and evidence IDs and the checked revision/diff.

## Ship questions

Use this section only when this chat owns shipping and shipping is not already authorized. If the user already asked to ship, including the whole stack, follow [shipping.md](../rules/shipping.md) without this question. Otherwise ask once after the completion summary; default is no:

```markdown
## Questions
Reply like: 1b

1. Ship this work?
   - a) yes: cut a branch, commit, push, and draft a PR for your approval
   - b) no: leave the changes uncommitted ← recommended
```

Wait. On yes, follow the [Process in shipping.md](../rules/shipping.md#process) from its first step. Under a parent that owns shipping, return the completion evidence to the parent instead.

## Behavior-lock suggestion

Run after the Locked in message, once the inline plan names the public entry. The bar is the [Behavior locks table](doctrine.md#behavior-locks) in the doctrine. Skip it during an open grill, for a trivial change, and in Fix mode.

Carry forward explicit acceptances and refusals with their decision source. Offer only unsettled tests; if none remain, proceed without a prompt. For a whole-stack run, batch unsettled choices across children once.

1. Walk each rule that must stay true. Offer a brief only when it passes the [testing.md](../rules/testing.md#when-a-test-is-worth-writing) bar.
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
- **Yes:** add a test slice after the product slice that creates the public entry. Follow [testing.md](../rules/testing.md) with the accepted Why / What / How, the rule id, and the public entry. Acceptance evidence includes the [lock handoff](../rules/testing.md#handoff).

## Lifecycle

Numbered process for `/task`. Nested vs one-off shipping lives in [SKILL.md](SKILL.md).

### Phase 0: establish context and grill

1. Apply the shared [ready-ticket preflight](../rules/execution.md#ready-ticket-preflight). Reuse settled ticket and parent decisions with sources.
2. For remaining consequential gaps, call `/grill-me` within this context. Apply code quality, structure, and any Feature or UX rules while researching facts; a complete ticket needs no new interview.
3. Keep each behavioral rule under its existing ID, with enforcement and observable verification. Add IDs only for genuinely new rules.
4. Ask unresolved user choices in a Questions-only message. Once settled, separately announce or reuse the current Locked in message, including meaningful non-goals and shared understanding. Save test suggestions for after that lock.

On a Locked correction or unanswered question, revise or wait.

### Phase 1: plan and build

**Explore and shape.** Find the relevant paths. Run `/analyze` when how, impact, or risk needs judging. Confirm code quality and structure choices against the grill and keep the locked structure excerpt in the plan contracts. For UI, confirm against user-experience.md and `docs/design.md` (write it first if missing).

**Split and plan.** Announce a [slice split](#slice-split) in the Locked in message (the agent owns it; do not ask yes/no). Then issue an [inline plan contract](#inline-plan-contract) per slice, stating the outcome and the concrete approach needed to preserve settled choices; leave routine implementation details to the executor. If the split changes, re-announce it before implementing. Keep plans in chat. Then run the [behavior-lock suggestion](#behavior-lock-suggestion); phase is `locks` while it is open, and a corrected rule returns to the grill before implementing.

**Implement.** Build ready frontier slices one at a time, in dependency order. User-facing slices (screens, components, styling, visible copy) apply user-experience.md and `docs/design.md`. For each slice:

1. Stay in its lane and follow its contract and structure excerpt. Create the owning folder before its files. Do a required behavior-preserving move before feature code and show the old behavior still holds.
2. Reuse existing services and one-job helpers. If the slice seems to need a new shared API, service, or lane, mark it `blocked` and name the smallest option.
3. Gather slice-local evidence only: existing terminal output first, then one narrow command if needed.
4. No tests in a product slice. Each accepted lock is its own test slice ([testing.md](../rules/testing.md)) after the public entry exists.
5. Update **Current slices** with status, evidence, findings, and changed interfaces. Missing acceptance, dependency, or structural decision: mark `blocked` and name the smallest decision needed.

Start the gate when every slice is done, blocked, or explicitly waived.

**Verification and review gate.**

1. Launch two subagents in one step so they run at the same time:
   - `/verification`: give it Done when (task and slice), the rules that must stay true, cross-slice seams, the slices, and the diff. It runs all repository test suites and drives only the affected live paths ([scope](../verification/doctrine.md#scope-to-the-change)).
   - `/review`: give it the same handoff. It reviews the diff for Standards and Spec.

   If the harness has no subagent, run `/verification`, then `/review`, in this context.
2. Use the shared [handoff and evidence contract](../rules/execution.md#handoffs-and-evidence). Read the actual evidence before accepting a verdict.
3. Use the verification handoff as the acceptance evidence. Add the lock handoff and the focused test result for each accepted lock. Mark each criterion verified, failed, or inconclusive. An unperformed check is not a pass.
4. Put each `/review` finding and each failed verification check in the **Fix backlog** as `fix now`, `follow-up`, or `waived`. An inconclusive check names its missing prerequisite and blocks completion until it is driven or waived by name. Ask any proposed `docs/verification.md` edits in the next Questions batch.
5. As active orchestrator, apply [remediation](../rules/execution.md#remediation) once for selected findings. Enter bounded Fix mode under existing user authorization, or ask if it does not cover those fixes.
6. Leave behavior-lock suggestions closed here. A lock the review still wants follows the [review contract](../review/contract.md), and a test is written only if the user says yes to it ([testing.md](../rules/testing.md)).

### Fix mode (review remediation only)

Follow shared [remediation](../rules/execution.md#remediation). Retain the current outcome and rules, promote only named bounded fixes, and preserve test consent. Recheck invalidated evidence and run `/review` in remediation mode; final whole-result verification still covers the changed tree, all configured suites and applicable live checks.

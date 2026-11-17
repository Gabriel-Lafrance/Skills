# Task reference (in-chat templates)

## Execution context

Take user decisions, waivers and authority to promote fixes from the user, never from repository facts or a review verdict. Re-announce settled decisions when they matter to a later phase.

## Inline plan contract

One per slice, in chat, after the Locked in message.

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
- <For touched user flows only: carry the ticket's UX/UI contract or derive a compact one from [action and continuation](../rules/user-experience.md#action-and-continuation). Name entry/context, useful actions by state, carried inputs, result/next action, recovery, and existing component/hierarchy/responsive expectations.>
- **File:** `docs/design.md` present | missing (offer to write it when implementing UI)

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
Omit User experience for backend-only slices. Reuse settled interaction requirements; do not repeat design questions or copy the shared contract into every slice.

## Slice split

A slice is small enough when it has one clear **what** (one seam, or one function), 1 to 3 binary checks that verify it alone, and its contract plus working set stay around 30% of the context window. If it still needs "and then also", or building it means re-mapping the repo, split again. Prefer thin vertical slices over horizontal layers. For wide refactors: expand, migrate in small batches, then contract.

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

Follow [recovery and completion](../rules/execution.md#recovery-and-completion).

## Progress and pause

Follow [Working output](../rules/writing-style.md#working-output), and the [final report](../rules/writing-style.md#final-report) for a pause.

## Completion summary

After both gate handoffs are in, report the outcome in chat as a [final report](../rules/writing-style.md#final-report):

```markdown
✅ **Done: <short title>**
**State:** <what works, what was checked, where the change lives>
**Next:** <one step and who owns it>

## What changed
- …

## Evidence
- `/verification`: <verified | failed | inconclusive, per Done when / rule / seam>
- `/review`: …

## Decisions and rules
- Rule 1: … verified by …

## Fix backlog
- <none | waived finding and user decision>

## Tests worth keeping
- <none proposed | the `/verification` proposal, by number | written: file and command>

```

## Ship offer

Use this only when this chat owns shipping and shipping is not already authorized. Ask nothing: the completion report's **Next** line says where the work lives and offers it, such as "Uncommitted. Reply `ship` for a branch, commit, and draft PR." On that reply, follow the [Process in shipping.md](../rules/shipping.md#process) from its first step.

## Lifecycle

### Phase 0: establish context and grill

1. Apply the shared [ready-ticket preflight](../rules/execution.md#ready-ticket-preflight). Reuse settled ticket and parent decisions with sources.
2. For remaining consequential gaps, call `/grill-me` within this context. Apply code quality, structure, and any Feature or UX rules while researching facts.
3. Keep each behavioral rule under its existing ID, with enforcement and observable verification. Add IDs only for new rules.
4. Ask unresolved user choices in a Questions-only message. Once settled, separately announce or reuse the current Locked in message, including meaningful non-goals and shared understanding.

On a Locked correction or unanswered question, revise or wait.

### Phase 1: plan and build

**Explore and shape.** Investigate in place when how, impact, or risk needs judging. Confirm code quality and structure choices against the grill and keep the locked structure excerpt in the plan contracts.

**Split and plan.** Announce a [slice split](#slice-split) in the Locked in message (the agent owns it; do not ask yes/no). Then issue an [inline plan contract](#inline-plan-contract) per slice, stating the outcome and the concrete approach needed to preserve settled choices; leave routine implementation details to the executor. If the split changes, re-announce it before implementing.

**Implement.** Build ready frontier slices one at a time, in dependency order. For each slice:

1. Stay in its lane and follow its contract and structure excerpt. Create the owning folder before its files. Do a required behavior-preserving move before feature code and show the old behavior still holds.
   Check [responsibility boundaries](../rules/code-structure.md#responsibility-boundaries) in changed existing files too. Record justified extraction in the current Structure map; keep cohesive small behavior whole. Private placement needs no new user decision unless ownership, contract, scope, or behavior changes consequentially.
2. Reuse existing services and one-job helpers. If the slice seems to need a new shared API, service, or lane, mark it `blocked` and name the smallest option.
3. Gather slice-local evidence only: existing terminal output first, then one narrow command if needed.
4. Update **Current slices** with status, evidence, findings, and changed interfaces. Missing acceptance, dependency, or structural decision: mark `blocked` and name the smallest decision needed.

Start the gate when every slice is done, blocked, or explicitly waived.

**Verification and review gate.**

1. Select check scope and orchestration under [verification scope](../rules/execution.md#verification-scope). For substantial or high-risk work, launch two independent agents together when available:
   - `/verification`: give it Done when, invariants, affected seams, slices, diff, selected scope, and valid prior evidence. It runs applicable checks and relevant live paths ([scope](../verification/doctrine.md#scope-to-the-change)).
   - `/review`: use the [fresh combined-review context](../review/contract.md#fresh-combined-review-context), pinned to the same tree, without the implementation conversation or a prewritten verdict.

   If subagents are unavailable, run serially and disclose that limit.
2. Use the shared [handoff and evidence contract](../rules/execution.md#handoffs-and-evidence). Read the actual evidence before accepting a verdict.
3. Mark each criterion verified, failed, or inconclusive from the verification handoff. An unperformed check is not a pass.
4. Put each `/review` finding and each failed verification check in the **Fix backlog** as `fix now`, `follow-up`, or `waived`. An inconclusive check names its missing prerequisite and blocks completion until it is driven or waived by name. Ask any proposed `docs/verification.md` edits in the next Questions batch.
5. Apply [remediation](../rules/execution.md#remediation) once for selected findings. Enter bounded Fix mode under existing user authorization, or ask if it does not cover those fixes.

### Fix mode (review remediation only)

Follow shared [remediation](../rules/execution.md#remediation).

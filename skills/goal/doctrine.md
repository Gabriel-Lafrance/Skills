# Goal Doctrine

Autonomous loop toward one verifiable completion condition. Stay in **Agent mode** — no `SwitchMode`, no CreatePlan UI.

**You are the orchestrator; Task subagents do the labor.** Follow **`/orchestrate`**.

**Subagent model:** when launching Task workers, **omit `model`** so workers inherit this chat's parent model (see `/orchestrate`). Never hard-code a model unless the user asked for one.

**Workspace:** Resolve `goal_root` and `goals_container` per [../workspace-roots.md](../workspace-roots.md) before Phase 0. A caller-provided root wins; persist the resolved values in `STATUS.md` before invoking a child flow.

**Active Rules:** `GOAL.md` owns every behavioral rule locked during the grill. Each rule gets an `INV-*` row in **Active Rules (Invariants)** with its plan, authoritative enforcement point, and verification. A user can explicitly mark a statement as a preference, example, or non-binding idea instead.

**Grill before plans.** Do not write plan files until `/grill-me` **announces** Locked closing (non-goals + plan split + shared-understanding summary — correct if wrong) per [../asking.md](../asking.md) (unless the skip rule below applies). After grilling, produce **as many plans as the work needs** under `plans/` — not one vague mega-plan. The agent owns the split and the understanding recap; the user corrects only if needed.

**Quality bar:** every `/goal` must run the pack's quality skills — not skip straight from implement to "done". **`/validate` and `/code-review` are mandatory** before ACHIEVED. Skipping `/code-review` is an anti-pattern.

**Cross-plan seams:** `/validate` owns cross-plan link verification when INDEX has 2+ plans. `/goal` does **not** run a separate deep link-check step — go straight from implement workers to `/validate`.

## Lookup rule (inside this loop)

| Need | Call |
| --- | --- |
| Ticket context | `/trackers` (read only) when ticket/PR |
| Grill | `/grill-me` |
| Style contract | `/taste` (during grill + before implement) |
| Structure | `/architecture` |
| UI | `/design` when UI is in scope |
| Split | `/split-task` when INDEX needs shaping |
| Plan files | `/create-plan` |
| Conductor | `/orchestrate` for every Task wave |
| Build | `/implement` |
| Bug mid-build | `/repair` → `/validate` (grill + acceptance; massive → new `/goal`) |
| Review Fix-now backlog | `/analyze` review remediation mode before any Fix mode |
| Gate out | `/validate` then **`/code-review`** (required) |

Inside this loop, call dual skills (`/grill-me`, `/architecture`, `/design`, `/code-review`, `/repair`) so they load the **flow** variant ([variants.md](../variants.md)). Do not load both variants. Internals: `/validate`, `/create-plan`, `/implement`, `/orchestrate`, `/taste`, `/split-task`, `/trackers`.

## Mandatory skill checklist

Track these in `STATUS.md` as you go. Do not announce ACHIEVED until every required row is done:

| Skill | Required? | Notes |
| --- | --- | --- |
| `/orchestrate` | Yes | All Task workers |
| `/trackers` | If ticket | Read only |
| `/grill-me` | Yes* | *Unless skip-grill rule |
| `/taste` | Yes | During grill + before/during implement |
| `/architecture` | Yes* | *Unless trivial single-file and grill settled structure |
| `/design` | If UI | Design card into plans |
| `/split-task` | If multi-slice | Prefer when grill yields >1 plan |
| `/create-plan` | Yes | At least `plans/01-*.md` + INDEX |
| `/implement` | Yes | Frontier plans |
| `/validate` | Yes | Must pass — includes cross-plan seams when 2+ plans |
| `/code-review` | Yes | Must run after validate; Fix-now offer → review remediation `/analyze` → explicit promotion → Fix mode, or explicit waive |

## Ticket-driven goals

Fetch via `/trackers` first (**read only**). Still **grill** on open product decisions. On ACHIEVED do **not** write to the tracker; user closes the ticket / merges the PR.

## Suitability gate

**Hard reject:** vague wishes, open-ended research with no done state.

**Multiple unrelated outcomes:** start **separate** `/goal`s (separate ids).

**Skip grill only if all are true:** ticket/user already has binary AC, no open product/UX/architecture/design decisions, no unrecorded behavioral rules, and user said `no grill` / `skip grill` or the change is a single obvious file fix. Seed any explicit ticket/user behavioral rule into Active Rules even when skipping. **From `/analyze` promote:** use the full four-condition [skip-grill / resume checklist](../analyze/doctrine.md). Otherwise grill is **mandatory**.

## Phase 0 — Workspace + grill (blocking)

1. Allocate `goal-id`; resolve `goal_root` and `goals_container`.
2. Create `goal_root`; write draft `GOAL.md` + `STATUS.md` (`phase: grilling`, `last: grilling`, root fields); upsert `<goals_container>/REGISTRY.md`.
3. Seeded from `/analyze` promote? → pull Done when / Lane / Context from the supplied `analysis_root/ANALYSIS.md` (link that path in GOAL Context); do not re-research from scratch; apply analyze skip-grill checklist before choosing `resume_at`.
4. Ticket? → `/trackers` brief (link in GOAL).
5. **Unless the skip-grill rule applies, run `/grill-me` fully** — it must pull **`/taste`**, **`/architecture`**, and **`/design`** (if UI) into the interview; upsert `grills/{language,choice,rules}.md` when terms/choices/rules lock.
6. Persist **goal-scoped** locked answers in `GRILL.md` (pointer to Themes paths); do not dump shared glossary into goal `GRILL.md`. On a valid skip, write the concise ticket/user contract and Locked gates instead of re-interviewing.
7. Update `GOAL.md` Done when / Constraints **and Active Rules** from the grill, or on a valid skip from the ticket/user contract and analysis draft. Every locked behavioral answer has an `INV-*` row with authoritative enforcement and verification.
8. **Closing** — announce non-goals + split + shared-understanding summary in Locked; ask only remaining real opens via [../asking.md](../asking.md).
9. During the Locked split, assign each Active Rule to an intended plan (or `all`), then enter Phase 1. **Never** write `plans/*` before Active Rules are complete for the behavior in scope.

### Closing (announce — correct if wrong)

| Item | Mode |
| --- | --- |
| **Non-goals** | **Announce** in Locked — do not ask yes/no |
| **Split plan** | **Announce** intended plans in Locked — agent owns the split |
| **Shared understanding** | **Announce** a short outcome summary in Locked — not a confirm question |

On a Locked correction (or unanswered real Questions): revise / wait, then continue. Persist gate checkboxes in `GRILL.md` when each item is announced.

## Phase 1 — Plans then build

### 1a. Explore + structure

Parallel `explore` Tasks via `/orchestrate` → confirm `/taste` + `/architecture` (+ `/design` if UI) against grill decisions. Fold into plan drafts.

### 1b. Split into plans

Prefer **multiple small plans** (`/split-task` when helpful). Write `plans/INDEX.md` matching the announced split. For each entry run `/create-plan`. If INDEX diverges from the announced split, **re-announce** the new Locked plans (correct if wrong) before implementing — do not ask yes/no.

### 1c. Implement wave

Frontier plans: parallel `/implement` workers; each reads `GOAL.md` + **that** `plans/NN-*.md` only. Workers get `/taste` (+ Design card if UI) in the prompt.

### 1d. Validate + review (blocking — never skip)

After all implement workers finish:

1. **`/validate`** against GOAL Done when + Active Rules + plans AC — includes cross-plan seam check when INDEX has 2+ plans (doctrine in `/validate`)
2. **Always** run `/code-review` next. Do not ACHIEVED without it.
3. `/code-review` presents findings + **Fix backlog** → batched offer via [../asking.md](../asking.md)
4. **yes** → run goal-scoped `/analyze` in review remediation mode → present proposed fixes → only on explicit promotion enter **Fix mode** on this goal-id → findings grill → implement → `/validate` → targeted re-review until named blockers clear or are explicitly waived
5. **no** → only ACHIEVED if no Fix-now blockers remain, or the user waived each blocker by name
6. Update `STATUS.md` checklist rows

### Fix mode (review remediation only)

Fix mode is one bounded slice of the current goal, not fresh product discovery. It starts only after a review remediation `ANALYSIS.md` has described the selected findings and the user promoted them. Under a `/just-do-it` parent, autonomy may accept the recommended promotion only after that analysis exists:

1. Copy only the selected analysis `FIX-*` rows into the active plan/backlog. Each row must cite the source review finding, remediation analysis path, violated Active Rule, acceptance criterion, correctness/security issue, or regression.
2. Grill only the enforcement, footprint, and observable behavior needed to clear those findings. Keep existing Active Rules; add one only when the finding exposes an unrecorded behavioral rule.
3. Prefer the smallest authoritative correction. For example, if X is disabled while Y processes, preserve the UI state and reject the prohibited backend/state transition directly; do not add locks, queues, retries, wrappers, or a new service unless the named finding proves a guard is insufficient.
4. Use one tight plan (or a few tightly coupled rows). No new feature scope, product exploration, optional cleanup, or architecture move unless the named finding requires it.
5. Validate the named findings and their Active Rules, then run `/code-review` in **targeted re-review** mode: named backlog, touched paths, direct regressions, correctness, and security only.

## Phase 2 — Achieve or clear

**Achieved only when:** mandatory checklist complete, `/validate` pass (including cross-plan seams when applicable), `/code-review` run (Fix-now findings fixed after analysis → remediation `ANALYSIS.md` → explicit promotion → focused grill/Fix mode, or explicitly waived by name).

Then:

1. Move `goal_root` to `<goals_container>/achieved/<goal-id>/`; update `STATUS.md` `goal_root` and the scoped REGISTRY `status: achieved`, `workspace: achieved/<goal-id>`.
2. **Print the ACHIEVED summary** (required last message — see [reference.md](reference.md))
3. **Ship Questions** batch (commit? open PR?) — see reference; defaults no unless already asked

**Cleared:** REGISTRY/STATUS `cleared`; delete active or archived tree per clear rule above.

## Additional resources

- Schemas / ACHIEVED template: [reference.md](reference.md)

## Anti-patterns

- Announcing done **without** `/code-review`
- Fixing review findings without the analysis choice, review remediation `ANALYSIS.md`, explicit promotion, and focused grill
- Treating a review fix as a fresh architecture or product goal
- Loading both standalone and flow variants of a dual skill in one turn
- Writing `plans/*` before Locked closing (non-goals + split + shared understanding)
- Leaving a grill-locked behavioral rule out of `GOAL.md` Active Rules
- Asking yes/no for non-goals, plan split, or shared understanding
- Dripping grill questions one message at a time when multiple opens are known
- Running a separate cross-plan link-check in `/goal` instead of letting `/validate` own it
- Skipping `/taste` / `/architecture` / `/design` (when UI) during grill or plan
- Writing/closing Linear or GitHub via `/trackers`
- Convex MCP verify loops when terminals already have the signal
- `SwitchMode` / CreatePlan UI
- One-line ACHIEVED with no skill/changelog/manual-steps summary
- Deleting goal workspace on ACHIEVED instead of archiving to `achieved/<goal-id>/`
- Asking resume vs new when other goals are `running`/`paused` — parallel goals are normal; `/goal` starts a new id immediately
- Writing or editing test files, or invoking `/create-test` — only `/create-test` writes tests, and only after `/code-review` / `/pr-review` recommends (user starts it)

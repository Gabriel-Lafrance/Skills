# Goal Doctrine

Autonomous loop toward one verifiable completion condition. Stay in **Agent mode** — no `SwitchMode`, no CreatePlan UI.

**You are the orchestrator; Task subagents do the labor.** Follow **`/orchestrate`**.

**Subagent model:** when launching Task workers, **omit `model`** so workers inherit this chat's parent model (see `/orchestrate`). Never hard-code a model unless the user asked for one.

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
| `/code-review` | Yes | Must run after validate; batched fix offer → grill+fix on this goal or explicit waive |

## Ticket-driven goals

Fetch via `/trackers` first (**read only**). Still **grill** on open product decisions. On ACHIEVED do **not** write to the tracker; user closes the ticket / merges the PR.

## Suitability gate

**Hard reject:** vague wishes, open-ended research with no done state.

**Multiple unrelated outcomes:** start **separate** `/goal`s (separate ids).

**Skip grill only if all are true:** ticket/user already has binary AC, no open product/UX/architecture/design decisions, and user said `no grill` / `skip grill` or the change is a single obvious file fix. **From `/analyze` promote:** also see analyze doctrine skip-grill checklist (binary Done when + no open Risks + confirmation batch). Otherwise grill is **mandatory**.

## Phase 0 — Workspace + grill (blocking)

1. Allocate `goal-id`; create `.agents/temp/goals/<goal-id>/`
2. Write draft `GOAL.md` + `STATUS.md` (`phase: grilling`, `last: grilling`); upsert `REGISTRY.md`
3. Seeded from `/analyze` promote? → pull Done when / Lane / Context from `.agents/temp/analyses/<id>/ANALYSIS.md` (link that path in GOAL Context); do not re-research from scratch; apply analyze skip-grill checklist before choosing `resume_at`
4. Ticket? → `/trackers` brief (link in GOAL)
5. **Run `/grill-me` fully** — it must pull **`/taste`**, **`/architecture`**, and **`/design`** (if UI) into the interview; upsert `grills/{language,choice,rules}.md` when terms/choices/rules lock
6. Persist **goal-scoped** locked answers in `GRILL.md` (pointer to Themes paths); do not dump shared glossary into goal `GRILL.md`
7. Update `GOAL.md` Done when / Constraints from the grill
8. **Closing** — announce non-goals + split + shared-understanding summary in Locked; ask only remaining real opens via [../asking.md](../asking.md)
9. Only after Locked closing is written (and any co-batched Questions answered) enter Phase 1. **Never** write `plans/*` before that.

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

1. **`/validate`** against GOAL Done when + plans AC — includes cross-plan seam check when INDEX has 2+ plans (doctrine in `/validate`)
2. **Always** run `/code-review` next. Do not ACHIEVED without it.
3. `/code-review` presents findings + **Fix backlog** → batched offer via [../asking.md](../asking.md)
4. **yes** → findings grill on this goal-id → implement → `/validate` → `/code-review` again until clear or explicitly waived
5. **no** → only ACHIEVED if no critical/important blockers remain, or the user waived each blocker by name
6. Update `STATUS.md` checklist rows

## Phase 2 — Achieve or clear

**Achieved only when:** mandatory checklist complete, `/validate` pass (including cross-plan seams when applicable), `/code-review` run (findings fixed after yes/grill, or critical/important explicitly waived by name).

Then:

1. REGISTRY `status: achieved`, `workspace: achieved/<goal-id>`
2. **`mv .agents/temp/goals/<goal-id> .agents/temp/goals/achieved/<goal-id>`**
3. **Print the ACHIEVED summary** (required last message — see [reference.md](reference.md))
4. **Ship Questions** batch (commit? open PR?) — see reference; defaults no unless already asked

**Cleared:** REGISTRY/STATUS `cleared`; delete active or archived tree per clear rule above.

## Additional resources

- Schemas / ACHIEVED template: [reference.md](reference.md)

## Anti-patterns

- Announcing done **without** `/code-review`
- Fixing review findings without the fix yes/no + findings grill
- Loading both standalone and flow variants of a dual skill in one turn
- Writing `plans/*` before Locked closing (non-goals + split + shared understanding)
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

# Goal Doctrine

Autonomous loop toward one verifiable completion condition. Stay in **Agent mode** — no `SwitchMode`, no CreatePlan UI.

**You are the orchestrator; Task subagents do the labor.** Follow **`/orchestrate-flow`**.

**Subagent model:** when launching Task workers, **omit `model`** so workers inherit this chat's parent model (see `/orchestrate-flow`). Never hard-code a model unless the user asked for one.

**Grill before plans.** Do not write plan files until `/grill-me-flow` clears the three gates (non-goals, split, shared understanding) — asked in **one batched Questions message** per [../asking.md](../asking.md) (unless the skip rule below applies). After grilling, produce **as many plans as the work needs** under `plans/` — not one vague mega-plan.

**Quality bar:** every `/goal` must run the pack's quality skills — not skip straight from implement to "done". **`/validate-flow` and `/code-review-flow` are mandatory** before ACHIEVED. Skipping `/code-review-flow` is an anti-pattern.

**Cross-plan seams:** `/validate-flow` owns cross-plan link verification when INDEX has 2+ plans. `/goal` does **not** run a separate deep link-check step — go straight from implement workers to `/validate-flow`.

## Lookup rule (inside this loop)

| Need | Call |
| --- | --- |
| Ticket context | `/trackers-flow` (read only) when ticket/PR |
| Grill | `/grill-me-flow` |
| Style contract | `/taste-flow` (during grill + before implement) |
| Structure | `/architecture-flow` |
| UI | `/design-flow` when UI is in scope |
| Split | `/split-task-flow` when INDEX needs shaping |
| Plan files | `/create-plan-flow` |
| Conductor | `/orchestrate-flow` for every Task wave |
| Build | `/implement-flow` |
| Bug mid-build | `/repair-flow` → `/validate-flow` (grill + acceptance; massive → new `/goal`) |
| Gate out | `/validate-flow` then **`/code-review-flow`** (required) |

Do **not** call standalone `/grill-me`, `/architecture`, `/design`, `/code-review`, or `/repair` for in-loop steps — those are for users/agents outside `/goal`. Use `*-flow` / internals (`/validate-flow`, `/create-plan-flow`, …) inside the loop.

## Mandatory skill checklist

Track these in `STATUS.md` as you go. Do not announce ACHIEVED until every required row is done:

| Skill | Required? | Notes |
| --- | --- | --- |
| `/orchestrate-flow` | Yes | All Task workers |
| `/trackers-flow` | If ticket | Read only |
| `/grill-me-flow` | Yes* | *Unless skip-grill rule |
| `/taste-flow` | Yes | During grill + before/during implement |
| `/architecture-flow` | Yes* | *Unless trivial single-file and grill settled structure |
| `/design-flow` | If UI | Design card into plans |
| `/split-task-flow` | If multi-slice | Prefer when grill yields >1 plan |
| `/create-plan-flow` | Yes | At least `plans/01-*.md` + INDEX |
| `/implement-flow` | Yes | Frontier plans |
| `/validate-flow` | Yes | Must pass — includes cross-plan seams when 2+ plans |
| `/code-review-flow` | Yes | Must run after validate; batched fix offer → grill+fix on this goal or explicit waive |

## Workspace layout

```text
.agents/temp/grills/              # shared themes (survive across goals)
  REGISTRY.md
  language.md                     # ubiquitous language
  choice.md                       # locked A-over-B / package picks
  rules.md                        # app rules (actors + policies)

.agents/temp/goals/
  REGISTRY.md
  achieved/
    <goal-id>/              # archived on ACHIEVED
      GOAL.md
      STATUS.md
      GRILL.md              # goal-scoped only
      plans/
      pieces/
  <goal-id>/                  # active running/blocked goals
    GOAL.md
    STATUS.md
    GRILL.md                 # goal-scoped: outcome, gates, taste/arch/design — not shared glossary
    plans/
      INDEX.md
      01-<slug>.md
      02-<slug>.md
    pieces/
```

Goal artifacts under **`.agents/temp/goals/`**; shared grill themes under **`.agents/temp/grills/`** — never `.scratch/`. Language / choices / rules are upserted by `/grill-me` and `/grill-me-flow` into `grills/` (see `/grill-me` doctrine).

### Goal id

1. Ticket → `IN-1234` or `gh-42`
2. Else kebab slug + 4-hex suffix → `add-billing-a3f2`
3. Override → `/goal id:my-id …`

If dir exists and status is `running`/`blocked`, resume or pick a new id — never overwrite another running goal.

### REGISTRY.md

| id | status | ticket | title | workspace | updated |
| --- | --- | --- | --- | --- | --- |

Statuses: `running` | `blocked` | `achieved` | `cleared`

On **ACHIEVED**: move active tree to `.agents/temp/goals/achieved/<goal-id>/`; set registry `workspace: achieved/<goal-id>` and `status: achieved`. Do **not** delete the workspace on achieve — archive it.

On **`/goal clear [id]`**: set registry `status: cleared`; delete the active tree **or** the archived tree under `achieved/<id>/` if that goal was already achieved.

### Isolation

- All artifacts for a goal stay under `.agents/temp/goals/<goal-id>/` (active) or `.agents/temp/goals/achieved/<goal-id>/` (archived); shared language/choices/rules stay under `.agents/temp/grills/`
- Task prompts get **that** id's `GOAL.md` + relevant `plans/*.md` only
- Overlapping file lanes with another `running` goal → serialize or ask
- Bare `/goal` → this chat's id status + other `running` rows

## STATUS.md schema (required fields)

Every active goal must maintain `STATUS.md` with at least:

| Field | Values / meaning |
| --- | --- |
| `phase` | `grilling` \| `planning` \| `implementing` \| `validating` \| `reviewing` \| `achieved` \| `cleared` |
| `last` | Last major step completed (e.g. `grilling`, `plan-01-done`, `validate-pass`) |
| `plans_done` | Count of completed plans |
| `plans_total` | Total plans in INDEX |
| `blocked_on` | `user` \| `none` |
| `resume_at` | Step id to resume (`0-grill`, `1a-explore`, `1b-plans`, `1c-implement`, `1d-validate`, `1d-review`) |

Also track the mandatory skill checklist rows as they complete.

## Resume / interrupt

| User action | Do |
| --- | --- |
| Bare `/goal` or “status” | Read REGISTRY + this goal’s `STATUS.md`; print **Progress** line + `resume_at`; do **not** re-grill settled GRILL gates |
| “continue” / “resume” | Jump to `resume_at`; re-read GOAL/GRILL/INDEX/current plan only |
| “pause” / “stop here” | Set `blocked_on: user`, `phase: paused`; acknowledge; **no** new Tasks until continue |
| `/goal clear [id]` | REGISTRY `cleared`; **delete** active `<goal-id>/` **or** archived `achieved/<goal-id>/` |
| New `/goal …` while one is `paused`/`running` | Do **not** overwrite; Questions batch: resume id vs new id ([../asking.md](../asking.md)) |

Persist gate checkboxes in `GRILL.md` so resume never re-asks cleared gates.

## Progress chat line format

After **every** phase change (and after each Task wave), post **one** short chat line **and** update `STATUS.md`:

```markdown
**Progress:** `<goal-id>` · grilling ✓ · plans 2/3 · implementing `01` · next: validate
```

Compact form also OK: `[goal:<id>] phase=<phase> plans=<done>/<total> last=<last> blocked=<blocked_on> resume=<resume_at>`

## Ticket-driven goals

Fetch via `/trackers-flow` first (**read only**). Still **grill** on open product decisions. On ACHIEVED do **not** write to the tracker; user closes the ticket / merges the PR.

## Suitability gate

**Hard reject:** vague wishes, open-ended research with no done state.

**Multiple unrelated outcomes:** start **separate** `/goal`s (separate ids).

**Skip grill only if all are true:** ticket/user already has binary AC, no open product/UX/architecture/design decisions, and user said `no grill` / `skip grill` or the change is a single obvious file fix. Otherwise grill is **mandatory**.

## Phase 0 — Workspace + grill (blocking)

1. Allocate `goal-id`; create `.agents/temp/goals/<goal-id>/`
2. Write draft `GOAL.md` + `STATUS.md` (`phase: grilling`, `last: grilling`); upsert `REGISTRY.md`
3. Seeded from `/analyze` promote? → pull Done when / Lane / Context from `.agents/temp/analyses/<id>/ANALYSIS.md` (link that path in GOAL Context); do not re-research from scratch
4. Ticket? → `/trackers-flow` brief (link in GOAL)
5. **Run `/grill-me-flow` fully** — it must pull **`/taste-flow`**, **`/architecture-flow`**, and **`/design-flow`** (if UI) into the interview; upsert `grills/{language,choice,rules}.md` when terms/choices/rules lock
6. Persist **goal-scoped** locked answers in `GRILL.md` (pointer to Themes paths); do not dump shared glossary into goal `GRILL.md`
7. Update `GOAL.md` Done when / Constraints from the grill
8. **Closing gates in the grill batch** — one Questions message via [../asking.md](../asking.md) (recap new language/choices/rules)
9. Only after all three gate yeses enter Phase 1. **Never** write `plans/*` before that.

### Closing gates (same batch as other grill questions)

| Gate | Options (lettered in the batch) |
| --- | --- |
| **Non-goals** | `a) yes` / `b) no — say what to change` |
| **Split plan** | Recap intended plans / INDEX draft → `a) yes` / `b) no — …` |
| **Shared understanding** | Short outcome bullets → `a) yes — ready to write plans` / `b) no — …` |

On any no: revise that topic only, then a **follow-up batch** for unresolved gates. Persist checkboxes in `GRILL.md`.

## Phase 1 — Plans then build

### 1a. Explore + structure

Parallel `explore` Tasks via `/orchestrate-flow` → confirm `/taste-flow` + `/architecture-flow` (+ `/design-flow` if UI) against grill decisions. Fold into plan drafts.

### 1b. Split into plans

Prefer **multiple small plans** (`/split-task-flow` when helpful). Write `plans/INDEX.md` matching the approved split. For each entry run `/create-plan-flow`. If INDEX diverges from the split-gate yes, include a split re-confirm in the **next Questions batch** before implementing.

### 1c. Implement wave

Frontier plans: parallel `/implement-flow` workers; each reads `GOAL.md` + **that** `plans/NN-*.md` only. Workers get `/taste-flow` (+ Design card if UI) in the prompt.

### 1d. Validate + review (blocking — never skip)

After all implement workers finish:

1. **`/validate-flow`** against GOAL Done when + plans AC — includes cross-plan seam check when INDEX has 2+ plans (doctrine in validate-flow)
2. **Always** run `/code-review-flow` next. Do not ACHIEVED without it.
3. `/code-review-flow` presents findings + **Fix backlog** → batched offer via [../asking.md](../asking.md)
4. **yes** → findings grill on this goal-id → implement → `/validate-flow` → `/code-review-flow` again until clear or explicitly waived
5. **no** → only ACHIEVED if no critical/important blockers remain, or the user waived each blocker by name
6. Update `STATUS.md` checklist rows

## Phase 2 — Achieve or clear

**Achieved only when:** mandatory checklist complete, `/validate-flow` pass (including cross-plan seams when applicable), `/code-review-flow` run (findings fixed after yes/grill, or critical/important explicitly waived by name).

Then:

1. REGISTRY `status: achieved`, `workspace: achieved/<goal-id>`
2. **`mv .agents/temp/goals/<goal-id> .agents/temp/goals/achieved/<goal-id>`**
3. **Print the ACHIEVED summary** (required last message)

**Cleared:** REGISTRY/STATUS `cleared`; delete active or archived tree per clear rule above.

## ACHIEVED summary (required last message)

After archive, the main agent's **final** user-facing message must be a polished recap — not a one-liner. Use light emojis, keep it scannable:

```markdown
# ✅ Goal achieved: <short title>

**goal-id:** `<id>` · **Ticket:** <none | IN-1234 / #42> · **Archive:** `.agents/temp/goals/achieved/<id>/`

## What we did
- <2–5 bullets of outcome in user language>

## Skills run
| Skill | Role |
| --- | --- |
| `/grill-me-flow` | … |
| `/taste-flow` | … |
| `/architecture-flow` | … or _n/a_ |
| `/design-flow` | … or _n/a_ |
| `/split-task-flow` | … or _n/a_ |
| `/create-plan-flow` | plans: … |
| `/orchestrate-flow` + `/implement-flow` | … |
| `/validate-flow` | pass (incl. cross-plan seams if 2+ plans) |
| `/code-review-flow` | Standards / Spec / Routes highlights |

## What changed
- **Files / areas:** …
- **Behavior:** …
- **Evidence:** terminals / localhost cite (no MCP ritual)

## Decisions locked (grill)
- Goal: … (from `GRILL.md`)
- Themes: … (from `grills/language.md`, `choice.md`, `rules.md` — or _none new_)

## Manual next steps (you)
- [ ] Close / merge ticket or PR if any (trackers are read-only)
- [ ] …

## Open follow-ups (optional)
- …
```

If there are no manual steps, still say so under **Manual next steps** (`_None — you're done._`).

## Anti-patterns

- Announcing done **without** `/code-review-flow`
- Fixing review findings without the fix yes/no + findings grill
- Calling standalone `/code-review` / `/design` / `/grill-me` / etc. inside this loop instead of `*-flow`
- Writing `plans/*` before all three gate yeses
- Dripping grill questions one message at a time when multiple opens are known
- Running a separate cross-plan link-check in `/goal` instead of letting `/validate-flow` own it
- Skipping `/taste-flow` / `/architecture-flow` / `/design-flow` (when UI) during grill or plan
- Writing/closing Linear or GitHub via `/trackers-flow`
- Convex MCP verify loops when terminals already have the signal
- `SwitchMode` / CreatePlan UI
- One-line ACHIEVED with no skill/changelog/manual-steps summary
- Deleting goal workspace on ACHIEVED instead of archiving to `achieved/<goal-id>/`

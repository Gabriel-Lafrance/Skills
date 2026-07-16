---
name: goal
description: >-
  Autonomous Cursor goal loop: grill until shared understanding, then write one
  or more plans under .agents/temp/goals/<goal-id>/, orchestrate Task subagents,
  validate + code-review-flow until done, then a rich ACHIEVED summary. Concurrent
  goals isolated. Agents may auto-invoke. Use when the user says /goal, passes a
  ticket ID, keep going until, or wants subagent-driven progress. Looks up *-flow
  twins; never standalone /design or /code-review inside this loop.
---

# Goal (Cursor)

Autonomous loop toward one verifiable completion condition. Stay in **Agent mode** — no `SwitchMode`, no CreatePlan UI.

**You are the orchestrator; Task subagents do the labor.** Follow **`/orchestrate-flow`**.

**Subagent model:** when launching Task workers, **omit `model`** so workers inherit this chat’s parent model (see `/orchestrate-flow`). Never hard-code a model unless the user asked for one.

**Grill before plans.** Do not write plan files until `/grill-me-flow` reaches shared understanding (unless the skip rule below applies). After grilling, produce **as many plans as the work needs** under `plans/` — not one vague mega-plan.

**Quality bar:** every `/goal` must run the pack’s quality skills — not skip straight from implement to “done”. **`/validate-flow` and `/code-review-flow` are mandatory** before ACHIEVED. Skipping `/code-review-flow` is an anti-pattern.

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

Do **not** call standalone `/grill-me`, `/architecture`, `/design`, `/create-plan`, `/code-review`, or `/repair` for in-loop steps — those are for users/agents outside `/goal`. Use `*-flow` / internals (`/validate-flow`, …) inside the loop.

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
| `/validate-flow` | Yes | Must pass |
| `/code-review-flow` | Yes | Must run after validate; fix blockers → re-validate → re-review if needed |

## Workspace layout

```text
.agents/temp/goals/
  REGISTRY.md
  <goal-id>/
    GOAL.md
    STATUS.md
    GRILL.md                 # decisions locked during /grill-me-flow
    plans/
      INDEX.md
      01-<slug>.md
      02-<slug>.md
    pieces/
```

Base path is always **`.agents/temp/goals/`** — never `.scratch/`.

### Goal id

1. Ticket → `IN-1234` or `gh-42`
2. Else kebab slug + 4-hex suffix → `add-billing-a3f2`
3. Override → `/goal id:my-id …`

If dir exists and status is `running`/`blocked`, resume or pick a new id — never overwrite another running goal.

### REGISTRY.md

| id | status | ticket | title | workspace | updated |
| --- | --- | --- | --- | --- | --- |

Statuses: `running` | `blocked` | `achieved` | `cleared`

On **achieved**: delete `<goal-id>/`; registry row keeps `workspace: (deleted)`.

### Isolation

- All artifacts for a goal stay under `.agents/temp/goals/<goal-id>/`
- Task prompts get **that** id’s `GOAL.md` + relevant `plans/*.md` only
- Overlapping file lanes with another `running` goal → serialize or ask
- `/goal clear [id]` clears that workspace’s status (keep files unless user asks delete)
- Bare `/goal` → this chat’s id status + other `running` rows

## Ticket-driven goals

Fetch via `/trackers-flow` first (**read only**). Still **grill** on open product decisions. On ACHIEVED do **not** write to the tracker; user closes the ticket / merges the PR.

## Suitability gate

**Hard reject:** vague wishes, open-ended research with no done state.

**Multiple unrelated outcomes:** start **separate** `/goal`s (separate ids).

**Skip grill only if all are true:** ticket/user already has binary AC, no open product/UX/architecture/design decisions, and user said `no grill` / `skip grill` or the change is a single obvious file fix. Otherwise grill is **mandatory**.

## Phase 0 — Workspace + grill (blocking)

1. Allocate `goal-id`; create `.agents/temp/goals/<goal-id>/`
2. Write draft `GOAL.md` + `STATUS.md` (`last: grilling`); upsert `REGISTRY.md`
3. Ticket? → `/trackers-flow` brief (link in GOAL)
4. **Run `/grill-me-flow` fully** — it must pull **`/taste-flow`**, **`/architecture-flow`**, and **`/design-flow`** (if UI) into the interview so the user decides those topics **before** plans
5. Persist locked answers in `GRILL.md`
6. Update `GOAL.md` Done when / Constraints from the grill
7. **Stop** for explicit shared understanding — wait for yes
8. Only then enter Phase 1. **Never** write `plans/*` before that yes.

## Phase 1 — Plans (often multiple) then build

### 1a. Explore + structure

Parallel `explore` Tasks via `/orchestrate-flow` → confirm `/taste-flow` + `/architecture-flow` (+ `/design-flow` if UI) against grill decisions. Fold into plan drafts.

### 1b. Split into plans

Prefer **multiple small plans** (`/split-task-flow` when helpful). Write `plans/INDEX.md`. For each entry run `/create-plan-flow`. Quiz once on INDEX when more than one plan.

### 1c. Implement wave

Frontier plans: parallel `/implement-flow` workers; each reads `GOAL.md` + **that** `plans/NN-*.md` only. Workers get `/taste-flow` (+ Design card if UI) in the prompt.

### 1d. Validate + review (blocking — never skip)

1. `/validate-flow` against GOAL Done when + plans AC — terminals once, not Convex MCP
2. **Always** run `/code-review-flow` next (Standards + Spec + Routes). Do not ACHIEVED without it.
3. If Standards/Spec/Routes have hard failures → fix → `/validate-flow` again if behavior changed → `/code-review-flow` again until clear or user accepts documented exceptions
4. Update `STATUS.md` checklist rows

## Phase 2 — Achieve or clear

**Achieved only when:** mandatory checklist complete, `/validate-flow` pass, `/code-review-flow` run (blockers fixed or explicitly waived by user).

Then: REGISTRY `achieved` + `(deleted)` → **`rm -rf` this `<goal-id>/` only** → **print the ACHIEVED summary below** (this is the last message of the goal).

**Cleared:** REGISTRY/STATUS `cleared`; keep workspace unless user asks to delete.

## ACHIEVED summary (required last message)

After cleanup, the main agent’s **final** user-facing message must be a polished recap — not a one-liner. Use light emojis, keep it scannable:

```markdown
# ✅ Goal achieved: <short title>

**goal-id:** `<id>` · **Ticket:** <none | IN-1234 / #42>

## What we did
- <2–5 bullets of outcome in user language>

## Skills run
| Skill | Role |
| --- | --- |
| `/grill-me-flow` | … |
| `/taste-flow` | … |
| `/architecture-flow` | … |
| `/design-flow` | … or _n/a_ |
| `/split-task-flow` | … or _n/a_ |
| `/create-plan-flow` | plans: … |
| `/orchestrate-flow` + `/implement-flow` | … |
| `/validate-flow` | pass |
| `/code-review-flow` | Standards / Spec / Routes highlights |

## What changed
- **Files / areas:** …
- **Behavior:** …
- **Evidence:** terminals / localhost cite (no MCP ritual)

## Decisions locked (grill)
- …

## Manual next steps (you)
- [ ] Close / merge ticket or PR if any (trackers are read-only)
- [ ] …
- [ ] …

## Open follow-ups (optional)
- …
```

If there are no manual steps, still say so under **Manual next steps** (`_None — you’re done._`).

## Anti-patterns

- Announcing done **without** `/code-review-flow`
- Calling standalone `/code-review` / `/design` / `/grill-me` / etc. inside this loop instead of `*-flow`
- Writing `plans/*` before grill yes
- Skipping `/taste-flow` / `/architecture-flow` / `/design-flow` (when UI) during grill or plan
- Writing/closing Linear or GitHub via `/trackers-flow`
- Convex MCP verify loops when terminals already have the signal
- `SwitchMode` / CreatePlan UI
- One-line ACHIEVED with no skill/changelog/manual-steps summary

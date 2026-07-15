---
name: goal
description: >-
  Autonomous Cursor goal loop: grill until shared understanding, then write one
  or more plans under .agents/temp/goals/<goal-id>/, orchestrate Task subagents,
  validate until done. Concurrent goals isolated. Agents may auto-invoke. Use
  when the user says /goal, passes a ticket ID, keep going until, or wants
  subagent-driven progress. Looks up *-flow twins for dual skills; never
  standalone /design or /code-review inside this loop.
---

# Goal (Cursor)

Autonomous loop toward one verifiable completion condition. Stay in **Agent mode** — no `SwitchMode`, no CreatePlan UI.

**You are the orchestrator; Task subagents do the labor.** Follow **`/orchestrate-flow`**.

**Grill before plans.** Do not write plan files until `/grill-me-flow` reaches shared understanding (unless the skip rule below applies). After grilling, produce **as many plans as the work needs** under `plans/` — not one vague mega-plan.

**Lookup rule (inside this loop):**

| Need | Call |
| --- | --- |
| Grill | `/grill-me-flow` |
| Structure | `/architecture-flow` |
| UI | `/design-flow` |
| Plan files | `/create-plan-flow` |
| Review | `/code-review-flow` |
| Always internal | `/orchestrate-flow`, `/trackers-flow`, `/taste-flow`, `/split-task-flow`, `/implement-flow`, `/validate-flow` |

Do **not** call standalone `/grill-me`, `/architecture`, `/design`, `/create-plan`, or `/code-review` for in-loop steps — those are for users/agents outside `/goal`.

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

**Skip grill only if all are true:** ticket/user already has binary AC, no open product/UX/architecture decisions, and user said `no grill` / `skip grill` or the change is a single obvious file fix. Otherwise grill is **mandatory**.

## Phase 0 — Workspace + grill (blocking)

1. Allocate `goal-id`; create `.agents/temp/goals/<goal-id>/`
2. Write draft `GOAL.md` + `STATUS.md` (`last: grilling`); upsert `REGISTRY.md`
3. **Run `/grill-me-flow` fully**
4. Persist locked answers in `GRILL.md`
5. Update `GOAL.md` Done when / Constraints from the grill
6. **Stop** for explicit shared understanding — wait for yes
7. Only then enter Phase 1. **Never** write `plans/*` before that yes.

## Phase 1 — Plans (often multiple) then build

### 1a. Explore + structure

Parallel `explore` Tasks via `/orchestrate-flow` → `/taste-flow` + `/architecture-flow` (+ `/design-flow` if UI). Fold into plan drafts.

### 1b. Split into plans

Prefer **multiple small plans** (`/split-task-flow` spirit). Write `plans/INDEX.md`. For each entry run `/create-plan-flow`. Quiz once on INDEX when more than one plan.

### 1c. Implement wave

Frontier plans: parallel `/implement-flow` workers; each reads `GOAL.md` + **that** `plans/NN-*.md` only.

### 1d. Validate + review

- `/validate-flow` — terminals once, not Convex MCP
- `/code-review-flow` — goal Spec + Standards
- Fix → re-validate if the diff changed

## Phase 2 — Achieve or clear

**Achieved:** `/validate-flow` + `/code-review-flow` pass → REGISTRY `achieved` + `(deleted)` → **`rm -rf` this `<goal-id>/` only** → announce ACHIEVED (ticket close manual).

**Cleared:** REGISTRY/STATUS `cleared`; keep workspace unless user asks to delete.

## Anti-patterns

- Calling standalone `/code-review` / `/design` / `/grill-me` / etc. inside this loop instead of `*-flow`
- Writing `plans/*` before grill yes
- Writing/closing Linear or GitHub via `/trackers-flow`
- Convex MCP verify loops when terminals already have the signal
- `SwitchMode` / CreatePlan UI

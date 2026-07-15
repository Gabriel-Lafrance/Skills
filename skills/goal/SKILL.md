---
name: goal
description: >-
  Autonomous Cursor goal loop: grill until shared understanding, then write one
  or more plans under .agents/temp/goals/<goal-id>/, orchestrate Task subagents,
  validate until done. Concurrent goals isolated. Agents may auto-invoke. Use
  when the user says /goal, passes a ticket ID, keep going until, or wants
  subagent-driven progress. Looks up *-flow skills only — not standalone twins.
---

# Goal (Cursor)

Autonomous loop toward one verifiable completion condition. Stay in **Agent mode** — no `SwitchMode`, no CreatePlan UI.

**You are the orchestrator; Task subagents do the labor.** Follow **`/orchestrate-flow`**.

**Grill before plans.** Do not write plan files until `/grill-me-flow` reaches shared understanding (unless the skip rule below applies). After grilling, produce **as many plans as the work needs** under `plans/` — not one vague mega-plan.

**Lookup rule:** inside this loop, always use **`*-flow`** skills (`/design-flow`, `/create-plan-flow`, …). Do not call standalone `/design`, `/grill-me`, etc. for in-loop steps.

## Workspace layout

```text
.agents/temp/goals/
  REGISTRY.md
  <goal-id>/
    GOAL.md
    STATUS.md
    GRILL.md                 # decisions locked during /grill-me-flow
    plans/
      INDEX.md               # ordered list of plan files
      01-<slug>.md
      02-<slug>.md
    pieces/                  # optional extra briefs if needed
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

Fetch via `/trackers-flow` first. Still **grill** on open product decisions the ticket does not settle. On ACHIEVED → close-out after validate.

## Suitability gate

**Hard reject:** vague wishes, open-ended research with no done state.

**Multiple unrelated outcomes:** start **separate** `/goal`s (separate ids), do not cram into one.

**Skip grill only if all are true:**

- Ticket (or user) already has binary acceptance criteria, **and**
- No open product/UX/architecture decisions, **and**
- User said `no grill` / `skip grill`, **or** the change is a single obvious file fix

Otherwise grill is **mandatory**.

## Phase 0 — Workspace + grill (blocking)

1. Allocate `goal-id`; create `.agents/temp/goals/<goal-id>/`
2. Write draft `GOAL.md` + `STATUS.md` (`last: grilling`); upsert `REGISTRY.md`
3. **Run `/grill-me-flow` fully** (one question at a time, recommended answer first):
   - Outcome, non-goals, users, edge cases
   - Architecture entry shape (hook/class/facade) when multi-file/UI
   - Data/scale decisions when lists/metrics exist
   - What must be separate plans vs one plan
4. Persist locked answers in `GRILL.md`
5. Update `GOAL.md` Done when / Constraints from the grill
6. **Stop and get explicit shared understanding** — e.g. “Shared understanding — ready to write N plans?” Wait for yes.
7. Only then enter Phase 1 planning. **Never** write `plans/*` before that yes.

`GOAL.md` artifacts section:

```markdown
# Artifacts
- Workspace: `.agents/temp/goals/<goal-id>/`
- GRILL: `GRILL.md`
- Plans: `plans/INDEX.md` + `plans/NN-*.md`
```

## Phase 1 — Plans (often multiple) then build

### 1a. Explore + structure

Parallel `explore` Tasks via `/orchestrate-flow` → `/taste-flow` + `/architecture-flow` (+ `/design-flow` if UI). Fold into plan drafts.

### 1b. Split into plans

From grill + explore, decide how many plans:

- **Default:** prefer **multiple small plans** over one fat plan (same spirit as `/split-task-flow`)
- Each plan = one demoable vertical slice / one agent-sized unit
- Write `plans/INDEX.md` listing order + blockers between plans
- For each entry, run `/create-plan-flow` with **goal-id** + **plan-file** `plans/NN-<slug>.md`
- Quiz the user once on the **INDEX only** (granularity / merge / split) when more than one plan — then write files and continue (no Plan-mode UI)

`plans/INDEX.md` example:

```markdown
# Plans index
goal-id: <goal-id>

| # | file | title | blocked by | status |
| --- | --- | --- | --- | --- |
| 01 | plans/01-schema.md | … | — | pending |
| 02 | plans/02-api.md | … | 01 | pending |
```

### 1c. Implement wave

Work the frontier (plans with blockers done):

- Parallel `/implement-flow` workers for non-overlapping plans/lanes
- Each worker reads `GOAL.md` + **that** `plans/NN-*.md` only
- Mark INDEX statuses as you go

### 1d. Validate + review

- `/validate-flow` against GOAL Done when + completed plans’ AC — **read terminals once**, not Convex MCP
- `/code-review-flow` parallel axes
- Fix → re-validate only if the diff changed (re-read terminals; still no MCP ritual)
- Update `STATUS.md` each checkpoint

## Phase 2 — Achieve or clear

**Achieved:** validate pass → `/trackers-flow` close-out if Ticket → REGISTRY `achieved` + `(deleted)` → **`rm -rf` this `<goal-id>/` only** → announce ACHIEVED.

If close-out fails: leave workspace, `blocked`, ask.

**Cleared:** REGISTRY/STATUS `cleared`; **keep** workspace unless user asks to delete.

## Anti-patterns

- Writing under `.scratch/`
- Writing `plans/*` before grill shared-understanding yes
- Calling standalone `/design` / `/grill-me` / etc. inside this loop instead of `*-flow`
- One mega-plan when the grill revealed multiple slices
- Skipping grill on fuzzy/product work
- Global ACTIVE singletons
- Workers missing goal-id / wrong plan file
- Two goals writing the same files in parallel
- `SwitchMode` / CreatePlan UI
- **Convex MCP / CLI verify loops** when `convex dev` terminal already has the signal

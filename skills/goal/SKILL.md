---
name: goal
description: >-
  Autonomous Cursor goal loop as orchestrator with isolated workspaces so many
  goals can run at once without file conflicts. Writes per-goal GOAL.md/PLAN.md,
  spawns Task subagents, validates until done. Use when the user says /goal,
  passes a ticket ID, keep going until, or wants concurrent subagent-driven goals.
disable-model-invocation: true
---

# Goal (Cursor)

Autonomous loop toward one verifiable completion condition. Stay in **Agent mode** — no `SwitchMode`, no CreatePlan UI, no waiting for plan confirmation.

**You are the orchestrator; Task subagents do the labor.** Follow **`/orchestrate`**.

**Many goals may run at once.** Each goal owns an isolated workspace under `.scratch/goals/<goal-id>/`. Never use a global `ACTIVE.md` that other goals could overwrite.

## Workspace layout (no conflicts)

```text
.scratch/goals/
  REGISTRY.md                 # index of all goals (running / blocked / achieved / cleared)
  <goal-id>/
    GOAL.md                   # contract for this goal only
    PLAN.md                   # plan for this goal only (/create-plan)
    STATUS.md                 # status, checkpoints, blockers
    pieces/                   # optional /split-task briefs
      01-….md
```

### Goal id

Allocate **once** at start; never reuse an in-use id:

1. Ticket id if present → `IN-1234` or `gh-42` (normalize: uppercase Linear; `gh-<n>` for `#n`)
2. Else kebab slug from the outcome + short suffix → `add-billing-a3f2` (4 random hex or time suffix)
3. User override: `/goal id:my-id …` or `/goal --id my-id …`

If the directory already exists and `STATUS.md` is `running` or `blocked`, **do not overwrite** — either resume that id (same chat continuing) or pick a new id for a new goal.

### REGISTRY.md

Create/update on every status change:

```markdown
# Goal registry

| id | status | ticket | title | workspace | updated |
| --- | --- | --- | --- | --- | --- |
| IN-1234 | running | IN-1234 | … | `.scratch/goals/IN-1234/` | ISO |
| add-billing-a3f2 | running | — | … | `.scratch/goals/add-billing-a3f2/` | ISO |
```

Statuses: `running` | `blocked` | `achieved` | `cleared`

After **achieved**, the `<goal-id>/` directory is **deleted**. Keep a registry row with `workspace: (deleted)` so history remains without leftover files.

### Isolation rules

- All reads/writes for a goal stay under `.scratch/goals/<goal-id>/`
- Every Task prompt gets **that** goal’s `GOAL.md` + `PLAN.md` paths — never another goal’s
- Implement workers for goal A must list **Touch only** lanes from A’s plan; if two running goals share files, **serialize** those slices or ask the user — do not parallel-write the same paths from two goals
- `/goal clear` / `stop` / `off` / `cancel` without an id clears **this chat’s** bound goal-id; with an id clears that workspace only
- `/goal` with no args → status for this chat’s bound id, plus a one-line list from REGISTRY of other `running` goals

Bind `goal-id` in chat memory for the session after Phase 0.

## Ticket-driven goals

`/goal IN-1234`, `/goal #42`, `/goal owner/repo#42`, or issue URL → resolve that ticket; **goal-id** from the ticket.

1. `/trackers` fetch immediately
2. Build contract from the brief
3. On ACHIEVED → `/trackers` close-out after validate evidence

If fetch fails, stop — do not guess.

## Suitability gate

**Hard reject:** vague wishes, open-ended research, multiple unrelated objectives **inside one** goal-id (start separate `/goal`s instead).

**Warn then proceed:** subjective quality — force binary Done when.

Empty ticket AC: derive Done when from Ask; continue (one confirm only if Ask is ambiguous).

## Phase 0 — Shape and persist

1. Allocate `goal-id` (rules above); create `.scratch/goals/<goal-id>/`
2. Write `GOAL.md`, `STATUS.md` (`status: running`), upsert `REGISTRY.md`
3. Ask one clarifying question only for decisions you cannot look up

`GOAL.md`:

```markdown
# Goal
<one-line verifiable outcome>

# Goal id
<goal-id>

# Ticket
<none | IN-1234 | #42 — URL>

# Lane
<files / packages / area — avoid overlapping another running goal’s lane when possible>

# Context
- Workspace: `.scratch/goals/<goal-id>/`
- First reads: PLAN.md, ticket brief, CONTEXT.md, sibling paths

# Constraints
- Hard rules / out of scope
- File lanes claimed (for multi-goal safety)

# Done when
1. <binary check>
2. …
3. <if Ticket: tracker close-out>

# On block
After 3 failed attempts on the same check: set STATUS blocked, ask user.
Stop after <N> checkpoints (default 12) unless user set another bound.

# Artifacts
- GOAL: `.scratch/goals/<goal-id>/GOAL.md`
- PLAN: `.scratch/goals/<goal-id>/PLAN.md`
- STATUS: `.scratch/goals/<goal-id>/STATUS.md`
```

`STATUS.md`:

```markdown
# Status
status: running
goal-id: <goal-id>
checkpoints: 0
bound: <ISO>
last: Phase 0
blockers: none
```

Show goal-id + contract briefly, then **Phase 1** without waiting for “go.”

## Phase 1 — Autonomous checkpoint loop

Until Done when or On block. Pass **this** workspace paths to every worker.

1. **Ambiguous intent?** → `/grill-me`, then continue.
2. **Explore wave** → `/orchestrate` parallel `explore` (sibling, lane, seams).
3. **Structure / UI** → `/taste` + `/architecture` (+ `/design` Mode B if UI).
4. **No/stale PLAN.md?** → `/create-plan` with **goal-id** → writes `.scratch/goals/<goal-id>/PLAN.md` only. No confirmation wait.
5. **Too big?** → `/split-task` into `pieces/`; parallel `/implement` for non-overlapping pieces **and** non-overlapping with other running goals’ lanes.
6. **Implement** → `/orchestrate` workers; integrate.
7. **`/validate`** against this GOAL/PLAN.
8. **`/code-review`** parallel axes (artifacts = this workspace). Fix → validate again.
9. Update `STATUS.md` each checkpoint; re-evaluate Done when.

### Rules

- Gate in = this goal’s `PLAN.md`; gate out = `/validate`
- Subagents by default; parallel independent Tasks
- Stay in Agent mode
- You own user questions, ACHIEVED, On block
- Never write another goal’s files; never delete another goal’s workspace unless user names that id
- **Do** delete **this** goal’s workspace after ACHIEVED (see Phase 2)

### Status command

`/goal` bare: this id’s STATUS + Done when summary; list other `running` rows from REGISTRY.

## Phase 2 — Achieve or clear

**Achieved:**

1. Validate pass (evidence table complete)
2. If Ticket set → `/trackers` close-out
3. Upsert `REGISTRY.md`: `status: achieved`, `workspace: (deleted)`, `updated: ISO`
4. **Delete** `.scratch/goals/<goal-id>/` entirely (`rm -rf` that directory only — never touch other ids or `REGISTRY.md`)
5. Announce ACHIEVED + one-line summary (+ ticket URL if any). Note that the workspace was cleaned up.

Do not delete the workspace before validate + tracker close-out succeed. If close-out fails, leave the workspace, set `STATUS`/`REGISTRY` to `blocked` with the reason, and ask.

**Cleared:** `STATUS`/`REGISTRY` = `cleared`; stop; **keep** the workspace (unless the user asks to delete it). Leave code/ticket unless asked to revert.

## Anti-patterns

- Global `.scratch/goals/ACTIVE.md` or `.scratch/plans/ACTIVE.md`
- Overwriting an existing `running` workspace
- Two goals’ workers editing the same files in parallel
- Task prompts missing the **goal-id** paths
- `SwitchMode` / CreatePlan UI / plan confirmation waits
- Main agent solo-doing all explore/implement
- Closing tracker before validate evidence
- Stuffing unrelated objectives into one goal-id instead of a second `/goal`

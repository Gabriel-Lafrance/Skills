---
name: ask-gabriel
description: >-
  Ask which Cursor skill or flow fits your situation. Router over the skills in
  this pack. Use when unsure what to run next.
disable-model-invocation: true
---

# Ask Gabriel

You don't remember every skill — ask.

A **flow** is a path through the skills. Most work rides the **main flow**. On-ramps merge onto it.

## Main flow: idea → ship

1. **Substantial + verifiable end state?** → **`/goal`** (isolated `.scratch/goals/<goal-id>/`; many goals can run at once). Tickets: **`/goal IN-1234`** / **`/goal #42`**. See **`/orchestrate`**.
2. Otherwise sharpen with **`/grill-me`**. Structure → **`/architecture`**. UI → **`/design`** Mode B. Then **`/create-plan`** into that goal workspace.
3. **Multi-session or too big?** → **`/split-task`** into `pieces/`, then **`/implement`** with parallel workers (respect other running goals’ file lanes)
4. **`/validate`** / **`/code-review`** scoped to the same `goal-id`
5. **Ticket goal achieved?** → **`/trackers`** close-out

### Context hygiene

Keep grill → create-plan → split-task in one window when possible. Clear between implement pieces.

If the window is getting heavy before the split is done, hand off a short markdown summary and continue in a fresh chat.

## On-ramps

| Situation | Start with |
| --- | --- |
| Unsure which skill | Stay here — answer below |
| Keep going until X is true | `/goal` |
| Resolve Linear/GitHub ticket | `/goal IN-1234` or `/goal #42` |
| Misalignment / fuzzy idea | `/grill-me` |
| Hide complexity / folder structure | `/architecture` |
| Fix / polish current UI | `/design` |
| Creating UI inside a goal/plan | `/design` (Mode B) then continue flow |
| Coding style / "make it like I like" | `/taste` |
| Plan/task too big for one agent | `/split-task` |
| Plan file ready / continue build | `/implement` |
| Max subagents / how to delegate | `/orchestrate` |
| "Are we done?" | `/validate` |
| Review branch / PR | `/code-review` |

## Cursor rules (always)

- Stay in **Agent mode** — per-goal plans under `.scratch/goals/<goal-id>/PLAN.md`
- **Main orchestrates; subagents labor** — `/orchestrate`
- **Concurrent goals OK** — each has its own workspace + REGISTRY; never stomp another id
- Every Task prompt includes that **goal-id**’s GOAL.md + PLAN.md
- Prefer **throw + try/catch** over `success: false` in this author's projects
- Structure/naming → **`/taste`** + **`/architecture`**; UI → **`/design`**

## How to answer

1. Ask what they're trying to do in one sentence (if unclear).
2. Recommend **one** next skill and the next two steps of the flow.
3. Do not run the skill for them unless they say to.

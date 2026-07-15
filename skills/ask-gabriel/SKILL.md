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

1. **Substantial + verifiable end state?** → **`/goal`** (grill first → multiple `plans/` under `.agents/temp/goals/<goal-id>/`). Tickets: **`/goal IN-1234`** / **`/goal #42`**.
2. Standalone sharpen → **`/grill-me`**, then **`/architecture`** / **`/design`**, then **`/create-plan`**
3. **Too big?** → more plan files in INDEX + parallel **`/implement`** workers (file-lane safe)
4. **`/validate`** / **`/code-review`** on the same `goal-id`
5. **Ticket done?** → **`/trackers`** close-out

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

- Stay in **Agent mode** — artifacts under `.agents/temp/goals/<goal-id>/`
- **`/goal` must grill** before writing `plans/*`; prefer multiple small plans
- **Main orchestrates; subagents labor** — `/orchestrate`
- **Concurrent goals OK** — REGISTRY + isolated workspaces
- Task prompts include goal-id + specific `plans/NN-*.md`
- Prefer **throw + try/catch** over `success: false` in this author's projects
- Structure/naming → **`/taste`** + **`/architecture`**; UI → **`/design`**

## How to answer

1. Ask what they're trying to do in one sentence (if unclear).
2. Recommend **one** next skill and the next two steps of the flow.
3. Do not run the skill for them unless they say to.

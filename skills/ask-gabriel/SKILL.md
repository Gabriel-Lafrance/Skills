---
name: ask-gabriel
description: >-
  Ask which Cursor skill or flow fits your situation. Router over standalone
  skills and /goal. Agents may auto-invoke when the user is unsure what to run
  next.
---

# Ask Gabriel

You don't remember every skill — ask.

A **flow** is a path through skills. Most substantial work rides **`/goal`**, which looks up **`*-flow`** variants. One-shot work uses **standalone** skills (agents may auto-load those too).

## Main flow: idea → ship

1. **Substantial + verifiable end state?** → **`/goal`** (uses `*-flow` skills; grill first → multiple `plans/` under `.agents/temp/goals/<goal-id>/`). Tickets: **`/goal IN-1234`** / **`/goal #42`**.
2. Standalone sharpen → **`/grill-me`**, then **`/architecture`** / **`/design`**, then **`/create-plan`**
3. **Too big?** → **`/split-task`** (or under goal: `/split-task-flow` → INDEX) + parallel **`/implement`** / **`/implement-flow`**
4. **`/validate`** / **`/code-review`** (under goal: `*-flow`)
5. **Ticket context?** → `/goal` or `/code-review` loads **`/trackers`** (read only) — never run trackers alone or to close issues

### Context hygiene

Keep grill → create-plan → split-task in one window when possible. Clear between implement pieces.

If the window is getting heavy before the split is done, hand off a short markdown summary and continue in a fresh chat.

## On-ramps

| Situation | Start with |
| --- | --- |
| Unsure which skill | Stay here — answer below |
| Keep going until X is true | `/goal` |
| Resolve Linear/GitHub ticket | `/goal IN-1234` or `/goal #42` |
| Misalignment / fuzzy idea | `/grill-me` (in goal: `/grill-me-flow`) |
| Hide complexity / folder structure | `/architecture` (in goal: `/architecture-flow`) |
| Fix / polish current UI | `/design` |
| Creating UI inside a goal | `/design-flow` then continue `/goal` |
| Coding style / "make it like I like" | `/taste` (in goal: `/taste-flow`) |
| Plan/task too big for one agent | `/split-task` (in goal: `/split-task-flow`) |
| Plan file ready / continue build | `/implement` (in goal: `/implement-flow`) |
| Max subagents / how to delegate | `/orchestrate` (in goal: `/orchestrate-flow`) |
| "Are we done?" | `/validate` (in goal: `/validate-flow`) |
| Review branch / PR | `/code-review` (in goal: `/code-review-flow`) |

## Cursor rules (always)

- Stay in **Agent mode** — artifacts under `.agents/temp/goals/<goal-id>/`
- **`/goal` must grill** (`/grill-me-flow`) before writing `plans/*`; prefer multiple small plans
- **Main orchestrates; subagents labor** — `/orchestrate-flow` under goal
- **Concurrent goals OK** — REGISTRY + isolated workspaces
- Task prompts include goal-id + specific `plans/NN-*.md`
- Prefer **throw + try/catch** over `success: false` in this author's projects
- Structure/naming → **`/taste`** + **`/architecture`**; UI → **`/design`** (flow twins under `/goal`)

## How to answer

1. Ask what they're trying to do in one sentence (if unclear).
2. Recommend **one** next skill and the next two steps of the flow.
3. Do not run the skill for them unless they say to.

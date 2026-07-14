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

1. **Substantial + verifiable end state?** → **`/goal`** (shapes Done when, then drives the pack until evidence proves completion). Ticket IDs welcome: **`/goal IN-1234`** or **`/goal #42`**.
2. Otherwise sharpen with **`/grill-me`**. If structure matters (multi-file, extraction, UI state), run **`/architecture`** (after **`/taste`**). If UI is in scope, run **`/design`** Mode B, then **`/create-plan`** — Plan mode + CreatePlan, **wait for user confirmation**. Do not code before confirm.
3. **Multi-session or too big for one agent?**
   - **Yes** → **`/split-task`**, then fresh chat per piece with **`/implement`**
   - **No** → **`/implement`** in Agent mode after plan approval
4. **`/validate`** — Done when / plan acceptance criteria
5. **`/code-review`** — Standards + Spec via Cursor subagents
6. **Ticket goal achieved?** → **`/trackers`** close-out (comment + Done / close)

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
| Approved plan or piece ready | `/implement` |
| "Are we done?" | `/validate` |
| Review branch / PR | `/code-review` |

## Cursor rules (always)

- Prefer **Plan mode + CreatePlan** for non-trivial work
- **Never** start Agent implementation until the user confirms the plan
- Use **Task** subagents (`explore`, `bugbot`, `security-review`) instead of inventing parallel review rituals
- Prefer **throw + try/catch** over `success: false` return patterns when advising code style in this author's projects
- Structure and naming follow **`/taste`** + **`/architecture`**
- UI looks/feel follow **`/design`**

## How to answer

1. Ask what they're trying to do in one sentence (if unclear).
2. Recommend **one** next skill and the next two steps of the flow.
3. Do not run the skill for them unless they say to.

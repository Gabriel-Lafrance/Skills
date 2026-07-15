---
name: grill-me
description: >-
  Relentless interview to sharpen a plan or design until shared understanding.
  Required by /goal before any plans are written. Use when grilling, or when
  /goal needs product/architecture decisions settled.
disable-model-invocation: true
---

# Grill Me

Interview until you and the user share understanding. Under `/goal`, this is a **hard gate** before `plans/*` exist.

## Rules

1. Walk each branch of the decision tree. Resolve dependencies one by one.
2. For every question, give your **recommended answer** first (one-word accept).
3. Ask **one question at a time**. Wait.
4. Look up facts in the repo/tools — do not ask those.
5. Decisions are the user’s — wait for each answer.
6. Cover at least (skip only if already settled in ticket/GRILL):
   - Exact outcome and non-goals
   - Who it is for / critical edge cases
   - Entry shape when multi-file or UI (hook vs class vs facade — default from `/taste` + sibling)
   - Data/scale: anything counted/listed often → store on write?
   - **How many separate plans** the work should become (prefer more small plans)
   - File lanes / what must not be touched
7. Do **not** write `plans/*`, implement feature code, or skip to `/create-plan` until they confirm shared understanding.
8. When under `/goal`, write locked answers to `.agents/temp/goals/<goal-id>/GRILL.md` as you go (or once at the end before confirm).

## Closing

End with a short recap + explicit ask:

> Shared understanding: <bullets>. I will write **N** plans: <titles>. Proceed?

Wait for yes. Then hand off:

- Inside `/goal` → return to `/goal` Phase 1 (write INDEX + plans)
- Standalone → `/architecture` if needed, then `/create-plan` / `/goal`

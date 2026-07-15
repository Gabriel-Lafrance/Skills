---
name: grill-me
description: >-
  Relentless interview to sharpen a plan or design until shared understanding.
  Agents may auto-invoke. Use when grilling, clarifying fuzzy intent, or
  settling product/architecture decisions outside a goal. Under /goal use
  /grill-me-flow instead.
---

# Grill Me

Interview until you and the user share understanding.

Inside a `/goal` workspace, use **`/grill-me-flow`** instead of this skill.

## Rules

1. Walk each branch of the decision tree. Resolve dependencies one by one.
2. For every question, give your **recommended answer** first (one-word accept).
3. Ask **one question at a time**. Wait.
4. Look up facts in the repo/tools — do not ask those.
5. Decisions are the user’s — wait for each answer.
6. Cover at least (skip only if already settled):
   - Exact outcome and non-goals
   - Who it is for / critical edge cases
   - Entry shape when multi-file or UI (hook vs class vs facade — default from `/taste` + sibling)
   - Data/scale: anything counted/listed often → store on write?
   - **How many separate plans** the work should become (prefer more small plans)
   - File lanes / what must not be touched
7. Do **not** write `plans/*`, implement feature code, or skip to `/create-plan` until they confirm shared understanding.

## Closing

End with a short recap + explicit ask:

> Shared understanding: <bullets>. Next: <architecture / create-plan / goal>. Proceed?

Wait for yes. Then hand off:

- Structure needed → `/architecture`, then `/create-plan` or `/goal`
- Ready to build a loop → `/goal`
- Ready for one plan file → `/create-plan`

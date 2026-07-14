---
name: create-plan
description: >-
  Turn the current conversation into a concrete Cursor plan via Plan mode and
  CreatePlan. The user must confirm before any implementation. Use after grilling
  or when the user asks to plan a non-trivial change.
disable-model-invocation: true
---

# Create Plan (Cursor)

This skill is the **validation gate**. Implementation starts only after the user confirms the plan in Cursor.

## Process

### 1. Stay in / switch to Plan mode

If not already in Plan mode, call `SwitchMode` with `target_mode_id: "plan"` and a short explanation.

Do **not** edit application code in this skill.

### 2. Gather enough context (read-only)

- Read **`/taste`** — plans must not propose shapes that violate it
- If a Linear/GitHub ticket is in play, use the `/trackers` brief (fetch first if missing)
- Read `CONTEXT.md` and relevant ADRs if present
- Explore only what is needed for an accurate plan; **cite a sibling** feature when one exists
- Prefer existing seams over new ones; fewest seams wins (ideal: one)
- If the change adds more than one file, extracts logic, or touches UI state: follow `/architecture` and draft the structure card first
- If the change creates or substantially changes UI: follow **`/design`** Mode B and include a Design card

If test seams or the entry-point shape are unclear, confirm with the user **before** CreatePlan (one question).

### 3. Call CreatePlan

Use the CreatePlan tool with:

- **name**: short plan title
- **overview**: 1–2 sentences
- **plan**: concise, actionable markdown
- **todos**: concrete implementation todos when the work has multiple steps

Plan body must include:

1. **Problem** — user perspective (ticket Ask when present)  
2. **Approach** — concrete chosen approach (no Option A/B left open); must fit `/taste`  
3. **Structure** — from `/architecture`: entry point, folder map, extension seam when big, **Scalability** (stored on write / indexes / not recomputed on render)  
4. **Design** — from `/design` Mode B when UI is in scope (job, hierarchy, surfaces, depth, states, ethical psychology)  
5. **Key files** — markdown links under that folder map (Convex names without `-`/`_`)  
6. **Seams / tests** — verify at the entry point when possible; prefer running localhost + Convex as the check, not ritual lint  
7. **Acceptance criteria** — checklist `/validate` will use later, including an explicit scalable-data row when metrics/lists/stats exist  
8. **Out of scope** — explicit non-goals  
9. **Ticket** — ID + URL when the plan resolves a tracker issue  
10. **Sibling** — path of the pattern being mirrored, or "greenfield"  

Cite essential snippets only. Use mermaid only when it clarifies architecture or flow.

### 4. Stop for confirmation

After CreatePlan succeeds, tell the user the plan is ready for review in the plan UI.

**Do not:**

- Switch to Agent and start coding
- Split the work yet (that is `/split-task`)
- Claim the work is approved

When they confirm / ask to implement:

- Multi-session or large → recommend `/split-task` then `/implement` per piece  
- Small → `/implement` (Agent mode) using the approved plan  

## Anti-patterns

- Freeform mega-plan in chat instead of CreatePlan
- Leaving open alternatives inside the plan
- Coding “just a little” before confirmation
- Skipping acceptance criteria (breaks `/validate`)
- Listing loose files with no folder map or entry point
- Proposing `{ success: false }` APIs, dynamic imports, or Convex files with `-`/`_`

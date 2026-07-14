---
name: implement
description: >-
  Implement approved plan or ticket work in Cursor Agent mode, then validate and
  review. Use when the user confirms a plan, hands you a Linear/GitHub ticket
  piece, or /goal reaches an approved implementation checkpoint.
disable-model-invocation: true
---

# Implement

Build the work described by an **approved** Cursor plan or a ready ticket piece.

## Preconditions

1. Plan was confirmed **or** a `/trackers` brief + approved plan/piece exists
2. If still in Plan mode and work is approved, switch to Agent (`SwitchMode` → `agent`)
3. Read **`/taste`** (required); if UI work, also read **`/design`**. Read `CONTEXT.md` / ADRs when present
4. If implementing against Linear/GitHub and the brief is missing, `/trackers` fetch first

If there is no approved plan and the change is non-trivial, stop and run `/create-plan` first.

## Process

1. **Structure first** — if the plan lacks a Structure card, or you are about to add multiple files, run `/architecture` before coding
2. **Design first (UI)** — if creating/changing UI and no Design card, run `/design` Mode B; if user only asked to polish existing UI, that is `/design` Mode A (standalone)
3. **Cite a sibling** — open one nearby feature and mirror its shape (or note greenfield)
4. **Build in thin vertical slices** — one demoable path at a time behind the agreed entry point
5. **Folders before files** — create the feature/domain folder, then collaborators; no flat dumps; no anonymous `utils` bags
6. **Taste (+ design) self-check** after each slice — fail any box → fix before continuing
7. **Verify via running stack** — read frontend localhost + Convex dev terminal output (see `/taste` Verify). Do **not** ritual-run lint/typecheck/full tests; CI owns those. Only run a deep check if those servers error on this change or the user asks
8. **`/validate`** — acceptance criteria from the plan, ticket brief, or active `/goal` Done when must pass (includes taste rows when present)
9. **`/code-review`** — Standards (`/taste` + smells) + Spec + structure
10. **Tracker** — do not close the issue here; `/goal` or an explicit `/trackers` close-out does that after validate
11. **Commit** only if the user asked (follow their git rules)

### Diff budget

Prefer one feature folder and one entry point per session. If the slice grows past that, stop and `/split-task` rather than sprawling.

## Cursor notes

- Do not reopen Plan mode mid-implementation unless scope changed and needs re-approval
- Prefer Task `explore` for unfamiliar areas instead of blind edits
- One ticket piece per context window when working a split queue
- When driven by `/goal`, surface evidence from running servers / Convex logs after each slice (not lint spam)
- Call sites should import the simple entry (hook / class / facade), not internals

## Done means

- Acceptance criteria checked via `/validate`
- `/taste` self-check passed on the final diff
- Structure self-check from `/architecture` passes (including scalability / write-path aggregates)
- UI work matches `/design` card (or Mode A fix intent) when applicable
- Review findings addressed or explicitly waived by the user
- No silent scope creep beyond the plan/ticket/goal

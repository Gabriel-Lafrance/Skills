---
name: split-task
description: >-
  Split a task or goal into the smallest agent-sized pieces that still stay in
  the smart zone. Prefer over-splitting: smaller tasks make agents more reliable.
  Use when work is too big for one session, the user asks to break down / chunk /
  decompose a goal or task, or before multi-step implement work.
disable-model-invocation: true
---

# Split Task

Take one task or goal and split it into **multiple smaller tasks or goals**.

**Priority:** keep agents in their smart zone. The smaller the task, the better agents are. Prefer over-splitting over under-splitting.

## Smart zone

A piece is in the smart zone when:

- One clear outcome a fresh agent can finish without rediscovering the whole plan
- Fits **one** focused session / context window
- Verifiable alone (command, artifact, or binary Done when)
- Touches a **narrow** lane (few files / one seam) — not a tour of the codebase
- Needs little prior chat history beyond its own brief + blockers

If a piece still needs "and then also…" — split again.

## Process

### 1. Capture the parent

Normalize what was given into one parent statement. Resolve **`goal-id`** and read `.agents/temp/goals/<goal-id>/GOAL.md` + `GRILL.md` + `plans/INDEX.md`. Prefer producing **multiple `plans/NN-*.md` via `/create-plan`** (update INDEX) over loose pieces. Optional extras go under `pieces/`. If the parent is a Linear/GitHub ticket, keep the same **Ticket ID** on every child and use the `/trackers` brief as the Ask.

```markdown
# Parent
<one-line outcome>

# Ticket
<none | IN-1234 | #42>

# Lane
<area / packages / apps>

# Done when (parent)
1. <binary check>
```

If the parent is still vague, ask **one** clarifying question, then continue. Do not invent scope.

### 2. Split ruthlessly

Break the parent into the **smallest** ordered pieces that still deliver value.

Each child:

| Field | Rule |
| --- | --- |
| **Title** | Imperative, specific ("Add auth middleware to API routes" not "Auth") |
| **Outcome** | One sentence — what is true when this piece alone is done |
| **Lane** | Narrower than the parent when possible |
| **Entry / folder** | Expected entry point + folder (from `/architecture` + `/taste`) when the piece adds files |
| **Done when** | 1–3 binary checks for *this* piece only |
| **Blocked by** | Earlier piece IDs, or none |
| **Why this size** | One line — why it fits the smart zone (or why it cannot shrink further) |

**Split further when** a piece:

- Touches more than one major concern (schema + UI + infra, etc.)
- Needs more than ~one explore pass to understand
- Has multiple independent Done when rows that could land separately
- Would force the agent to hold a long plan in working memory

**Do not merge** for "efficiency." Parallel-ready pieces with no blockers are a feature.

**Wide refactors:** expand → migrate in small batches → contract. Each batch is its own piece.

### 3. Order by blockers

List pieces so blockers come first. Mark the **frontier** (Blocked by: none) — those can start immediately, preferably in **separate fresh chats**.

### 4. Quiz the user

Show a numbered list. Ask only what changes the split:

1. Anything still too big for one agent session?
2. Wrong edges (merge / split / re-block)?
3. Missing piece or out-of-scope creep?

Iterate until they approve. Do not start `/implement` or `/goal` on children unless asked.

### 5. Hand off

After approval, for each approved child:

- Small, single-session → `/implement` (or `/goal` if they want a completion loop) in a **fresh chat**
- Still fuzzy → `/grill-me` then `/create-plan` on that child only

One child per fresh chat when possible. Do not stack the whole decomposition into one implement window.

## Output template

```markdown
# Split: <parent title>

## Parent Done when
1. …

## Pieces

### 1 — <title>
- **Ticket:** <same parent ID or none>
- **Outcome:** …
- **Lane:** …
- **Entry / folder:** …
- **Done when:** …
- **Blocked by:** none
- **Why this size:** …

### 2 — <title>
- **Outcome:** …
- **Lane:** …
- **Done when:** …
- **Blocked by:** 1
- **Why this size:** …

## Frontier
- 1 — ready now
```

## Anti-patterns

- Horizontal layers ("all schema, then all UI") when vertical thin slices fit
- Mega-pieces that "save context switching" — they push agents out of the smart zone
- Vague titles without Done when
- Publishing to a tracker unless the user asks (this skill is decomposition, not triage)
- Implementing before the user accepts the split

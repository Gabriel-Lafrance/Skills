---
name: split-task-flow
description: >-
  Internal split: turn work into plans/INDEX rows under
  .agents/temp/goals/<goal-id>/. Looked up by /goal. Never for users or
  auto-invocation.
disable-model-invocation: true
---

# Split Task Flow

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

Normalize what was given into one parent statement.

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

If the parent is still vague, include clarifying items in a **Questions batch** ([../asking.md](../asking.md)), then continue. Do not invent scope.

### 2. Split ruthlessly

Break the parent into the **smallest** ordered pieces that still deliver value.

Each child:

| Field | Rule |
| --- | --- |
| **Title** | Imperative, specific ("Add auth middleware to API routes" not "Auth") |
| **Outcome** | One sentence — what is true when this piece alone is done |
| **Lane** | Narrower than the parent when possible |
| **Entry / folder** | Expected entry point + folder (from `/architecture` + `/taste-flow`) when the piece adds files |
| **Done when** | 1–3 binary checks for *this* piece only |
| **Blocked by** | Earlier piece IDs, or none |
| **Why this size** | One line — why it fits the smart zone (or why it cannot shrink further) |

**Split further when** a piece touches more than one major concern, needs more than ~one explore pass, has multiple independent Done when rows, or would force a long plan in working memory.

**Do not merge** for "efficiency." Parallel-ready pieces with no blockers are a feature.

**Wide refactors:** expand → migrate in small batches → contract. Each batch is its own piece.

### 3. Order by blockers

List pieces so blockers come first. Mark the **frontier** (Blocked by: none).

### 4. Quiz the user (batched)

Show the numbered split list, then ask with [../asking.md](../asking.md). Include the split confirm **and** any other known opens in **one** Questions batch (e.g. non-goals / shared understanding when those gates are still open in `/grill-me-flow` / `/goal`).

Example item: `Split into these N plans?` → `a) yes` / `b) no — say what changes (too big / wrong edges / missing)`.

On no: revise, then a follow-up batch for unresolved items. Iterate until the split gate is yes. Do not start `/implement-flow` unless `/goal` asks.

### 5. Hand off

After approval:

- Prefer updating `plans/INDEX.md` + `/create-plan-flow` under the active `/goal`
- Still fuzzy → `/grill-me` then continue `/goal`

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

- Horizontal layers when vertical thin slices fit
- Mega-pieces that push agents out of the smart zone
- Vague titles without Done when
- Publishing to a tracker unless the user asks
- Implementing before the user accepts the split

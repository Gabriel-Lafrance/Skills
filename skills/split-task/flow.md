# Split Task Flow

Split one task or goal into **small, ordered inline slice contracts**. Keep the result in chat under the shared [execution context](../pack-shared/execution-context.md); do not write an INDEX, plan path, status file, or workspace state.

If the user explicitly asks to save the split, get or honor an approved destination and write only that requested artifact.

## Smart zone

A slice fits the smart zone when it has:

- one clear outcome a fresh agent can finish without rediscovering the goal;
- one focused session or context window of work;
- 1–3 binary checks that verify it alone;
- a narrow lane with few files or one seam;
- little needed history beyond its contract and blockers.

If it still needs “and then also…”, split it again. Parallel-ready slices with no blockers are useful; do not merge them merely for efficiency.

## Process

### 1. Capture the parent in chat

Normalize the request using the active execution context:

```markdown
# Parent
**Outcome:** <one-line verifiable outcome>
**Ticket / PR:** <reference | none>
**Lane:** <areas, paths, or symbols>
**Non-goals:** <explicit exclusions>
**Done when:**
1. <binary check>
**Active Rules:** <relevant INV IDs>
```

If the parent is vague, batch only the real clarifying questions using [asking.md](../pack-shared/asking.md). Do not invent scope.

### 2. Split ruthlessly

Break the parent into the smallest ordered slices that still deliver value. Each inline slice contract includes:

| Field | Rule |
| --- | --- |
| **Title** | Imperative and specific |
| **Outcome** | One sentence: what becomes true when this slice is done |
| **Lane** | Narrower than the parent when possible |
| **Entry / folder** | Expected entry point and folder when files are added |
| **Active Rules** | Rules implemented or preserved by this slice |
| **Done when** | 1–3 binary checks for this slice only |
| **Blocked by** | Earlier slice IDs, or none |
| **Why this size** | Why it fits the smart zone or cannot shrink further |

Split further when a slice touches more than one major concern, needs more than one explore pass, has independent Done-when rows, or would force a long plan into working memory. For wide refactors, expand, migrate in small batches, then contract.

### 3. Order and announce

List blockers first and mark the frontier. The agent owns the split, so do not
ask yes/no for it. If other real product, UX, architecture, or taste questions
remain, send a **Questions-only** batch per [asking.md](../pack-shared/asking.md)
(no Locked heading). After those are settled — or immediately when nothing is
open — announce the numbered split in a separate **Locked (correct if wrong)**
message.

If the user corrects the split, revise the in-chat contracts and continue. Do not implement until `/goal` asks.

### 4. Hand off

Copy the frontier and dependencies into **Current slices** of the execution context. Expand implementation-ready slices with an [inline plan contract](../goal/reference.md#inline-plan-contract), then `/implement` only for frontier work. Do not create an INDEX or rely on an automatic artifact.

## Output template

```markdown
# Split: <parent title>

## Parent Done when
1. …

## Slices

### 1 — <title>
- **Outcome:** …
- **Lane:** …
- **Entry / folder:** …
- **Active Rules:** `INV-1`, …
- **Done when:** …
- **Blocked by:** none
- **Why this size:** …

### 2 — <title>
- **Outcome:** …
- **Lane:** …
- **Active Rules:** `INV-2`, …
- **Done when:** …
- **Blocked by:** 1
- **Why this size:** …

## Frontier
- 1 — ready now
```

## Anti-patterns

- Horizontal layers when vertical thin slices fit
- Mega-slices that push workers out of the smart zone
- Vague titles without binary Done when
- Writing an automatic INDEX, plan file, status file, or resume state
- Implementing before the split is announced and any Questions-only batch is answered
- Asking yes/no to confirm the split
- Publishing to a tracker unless the user asks

---
name: split-task
description: >-
  Split a bounded outcome into small, ordered inline slice contracts in shared
  execution context for a parent orchestrator.
disable-model-invocation: true
---

# Split Task

**Must read:** [../pack-shared/standards.md](../pack-shared/standards.md) — Read `/taste` and `/architecture` doctrines this turn before splitting lanes or folders. Do not skip.

**Ask style:** [../pack-shared/asking.md](../pack-shared/asking.md)

This skill is a worker step for `/task` or `/just-do-it`, not a typical user start.

Split one task or goal into **small, ordered inline slice contracts**. Keep the result in chat under the shared [execution context](../pack-shared/execution-context.md); do not write an INDEX, plan path, status file, or workspace state.

Slices must name entry/folder per architecture; do not split in a way that forks a service or primitive.

If the user explicitly asks to save the split, get or honor an approved destination and write only that requested artifact.

## Smart zone

A slice fits the smart zone when:

- one clear **what** a specialist can finish without rediscovering the goal;
- the job is one seam or even **one function**;
- 1–3 binary checks that verify it alone;
- the **brief plus working set** stay around **30% of the context window**
  after harness, skills, rules, and MCP (already about half);
- little needed history beyond the injected brief and blockers.

The slice names **what**, not how. If it still needs “and then also…”, or the
worker would have to re-map the repo, split it again. Parallel-ready slices
with no blockers are useful; do not merge them merely for efficiency.

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
open — announce the numbered split in a separate **Locked in (tell me if this is wrong)**
message.

If the user corrects the split, revise the in-chat contracts and continue. Do not implement until `/task` asks.

### 4. Hand off

Copy the frontier and dependencies into **Current slices** of the execution context. Expand implementation-ready slices with an [inline plan contract](../task/reference.md#inline-plan-contract), then `/implement` only for frontier work. Do not create an INDEX or rely on an automatic artifact.

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
- **Rules that must stay true:** Rule 1, …
- **Done when:** …
- **Blocked by:** none
- **Why this size:** …

### 2 — <title>
- **Outcome:** …
- **Lane:** …
- **Rules that must stay true:** Rule 2, …
- **Done when:** …
- **Blocked by:** 1
- **Why this size:** …

## Frontier
- 1 — ready now
```

## Anti-patterns

- Horizontal layers when vertical thin slices fit
- Mega-slices that push workers out of the smart zone
- Slice contracts that prescribe how (step lists, patches) instead of what
- Vague titles without binary Done when
- Writing an automatic INDEX, plan file, status file, or resume state
- Implementing before the split is announced and any Questions-only batch is answered
- Asking yes/no to confirm the split
- Publishing to a tracker unless the user asks

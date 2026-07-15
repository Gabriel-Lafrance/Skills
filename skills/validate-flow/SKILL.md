---
name: validate-flow
description: >-
  Internal validate: GOAL Done when + plans INDEX under
  .agents/temp/goals/<goal-id>/. Looked up by /goal. Never for users or
  auto-invocation.
disable-model-invocation: true
---

# Validate Flow

Close the loop: the on-disk plan / goal contract was the **gate in**; this skill is the **gate out**.

## Inputs

Criteria from, in order (resolve **`goal-id`** when workspace-based):

1. `.agents/temp/goals/<goal-id>/GOAL.md` **Done when** rows
2. The `/trackers-flow` ticket brief acceptance checklist (Linear / GitHub)
3. Completed rows in `plans/INDEX.md` → each `plans/NN-*.md` acceptance criteria
4. Explicit criteria the user pasted in chat

Do not mix criteria from another goal-id’s workspace.

Also run:

- **`/taste-flow` implement self-check** on the diff — failures are **fail**, not optional nits
- **Scalability check** (required — see below) — failures are **fail**
- **`/design-flow`** checks when UI was in scope

If none of 1–4 exist, stop and ask — do not invent a vague "looks good."

## Process

### 1. Restate the bar

List each acceptance criterion as a checkbox. No new scope.

### 2. Evidence pass (cheap — one terminals read)

You **judge** pass/fail. **Do not** open Convex MCP or re-run Convex CLI for routine validate.

Gather evidence **once** in this order (`/taste-flow` Verify):

1. **Read the terminals folder** for already-running frontend + `convex dev` (prefer a single pass; cite `terminals/<id>.txt`)
2. Diff / structural checks (files, APIs, entry point)
3. UI criterion → existing localhost behavior if needed; mark **blocked** if you cannot see it — don’t invent MCP checks

**Forbidden as default validate steps:** Convex MCP (`logs`, `data`, `status`, `run`, …), second `convex dev`, ritual `lint`/`tsc`/full suites, a subagent whose only job is “verify via MCP”.

**Allowed exceptions:** terminals show an error you must diagnose; user asked for MCP/CLI; no Convex terminal and you said so first.

Optional: one `shell`/read Task to **summarize existing terminal files** — still no MCP.

### 3. Scalability check (required)

Ask and answer explicitly: **Does this code scale?**

Inspect the diff for `/architecture` scale rules. Mark **fail** if any hot path does the following without a documented, bounded exception:

| Red flag | What to require instead |
| --- | --- |
| Metrics/counts/totals computed on every render or every query by scanning children | Stored columns / summary table / parent fields updated **on insert/update/delete** |
| Unbounded `.collect()` / full table scan for a product UI | Indexes + pagination or pre-aggregation |
| Client-side reduce over large lists for dashboards | Server/materialized aggregates |
| N+1 fetches in list views | Batch or denormalize |

State the write path: *“When X is inserted, Y aggregate is updated here: …”*  
If there is no aggregate to store, say **N/A — no derived metrics** and why.

Scalability **fail** blocks “done” the same way a failed acceptance criterion does.

### 4. Report

```markdown
## Validation

| Criterion | Status | Evidence |
| --- | --- | --- |
| … | pass / fail / blocked | … |

### Scalability (required)
| Question | Status | Evidence |
| --- | --- | --- |
| Does this code scale? | pass / fail / N/A | write-path aggregates / indexes / or why N/A |
| No compute-on-render/read for metrics? | pass / fail / N/A | … |
| Hot reads use indexes / pagination? | pass / fail / N/A | … |

### Taste
| Check | Status | Evidence |
| --- | --- | --- |
| Sibling / entry / naming / errors / nesting | pass / fail | … |

### Design (if UI)
| Check | Status | Evidence |
| --- | --- | --- |
| Hierarchy / surfaces / depth / states / ethics | pass / fail | localhost or diff |

### Failures
- What failed and the smallest fix

### Scope creep
- Anything in the diff not asked for by the plan/ticket
```

### 5. Next step

- **All pass** (including scalability) → recommend `/code-review-flow` (or hand back to `/goal`). Never ask `/trackers-flow` to close tickets.
- **Any fail** → fix in Agent mode, then re-run `/validate-flow` (do not skip)
- **Blocked** → ask the user how to verify

## Anti-patterns

- Marking done because tests pass but criteria were never checked
- Skipping the scalability section or waving through scan-on-read metrics
- Ritual `lint` / `tsc` / full suite when localhost + Convex terminals are already the signal
- **Convex MCP verify loops** after every slice when `convex dev` terminal already shows push/ok or the error
- Expanding acceptance criteria mid-flight without re-planning
- Silent "LGTM" without evidence rows
- Passing validate while `/taste-flow` self-check fails
- Re-running validate with fresh MCP calls when nothing in the diff changed since the last terminals read

---
name: validate
description: >-
  Validate implemented work against plan/ticket acceptance criteria, taste,
  design (if UI), and scalability (no compute-on-render aggregates). Use before
  claiming done, before review, or when the user asks if the work is complete.
disable-model-invocation: true
---

# Validate

Close the loop: the on-disk plan / goal contract was the **gate in**; this skill is the **gate out**.

## Inputs

Resolve **`goal-id`** first (chat binding, user, or path). Then criteria from, in order:

1. `.scratch/goals/<goal-id>/GOAL.md` **Done when** rows
2. The `/trackers` ticket brief acceptance checklist (Linear / GitHub)
3. `.scratch/goals/<goal-id>/PLAN.md` acceptance criteria
4. Explicit criteria the user pasted in chat

Do not mix criteria from another goal-id’s workspace.

Also run:

- **`/taste` implement self-check** on the diff — failures are **fail**, not optional nits
- **Scalability check** (required — see below) — failures are **fail**
- **`/design`** checks when UI was in scope

If none of 1–4 exist, stop and ask — do not invent a vague "looks good."

## Process

### 1. Restate the bar

List each acceptance criterion as a checkbox. No new scope.

### 2. Evidence pass

You **judge** pass/fail. Optionally dispatch a `shell` / `explore` Task (see `/orchestrate`) to collect logs or summarize the diff — still you fill the table.

For each criterion, gather evidence **in this order** (see `/taste` Verify):

1. Running **frontend localhost** and **Convex dev** terminal output — compile errors, push failures, runtime stacks
2. Diff / structural checks (files, APIs, copy, entry point)
3. Behavior via the running app when relevant

**Do not** default to `lint`, `tsc`, or full test suites. CI covers type and lint. Run those commands only if local servers error on this change, the criterion explicitly requires a command, or the user asks.

If a criterion needs a browser path you cannot reach, say so and mark it **blocked**, not passed. Prefer reading existing terminal output over starting new processes.

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

- **All pass** (including scalability) → recommend `/code-review` (or `/trackers` close-out when a ticket goal already reviewed; or commit if user asked and review already done)
- **Any fail** → fix in Agent mode, then re-run `/validate` (do not skip)
- **Blocked** → ask the user how to verify

## Anti-patterns

- Marking done because tests pass but criteria were never checked
- Skipping the scalability section or waving through scan-on-read metrics
- Ritual `lint` / `tsc` / full suite when localhost + Convex are already the signal
- Expanding acceptance criteria mid-flight without re-planning
- Silent "LGTM" without evidence rows
- Passing validate while `/taste` self-check fails

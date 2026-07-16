---
name: validate-flow
description: >-
  Internal gate-out: prove acceptance criteria with live evidence (any terminal,
  fast CLI) and an out-loud code-path walk for linking gaps. Criteria from goal
  workspaces, repair ACCEPTANCE.md, tickets, or pasted Done when. Pessimistic —
  do not assume it works. May call repair-flow / taste / architecture / design.
  Looked up by /goal, /repair, /repair-flow. Never for users or auto-invocation.
disable-model-invocation: true
---

# Validate Flow

**Gate out.** The contract (goal / repair acceptance / ticket / paste) was the gate in; this skill judges whether the change actually meets it.

## Framing (pessimistic — required)

Do **not** assume the change works. Start from: it may still be wrong, incomplete, unlinked, or off-criteria. Every row needs **evidence**. Silent “LGTM” is a process fail.

Say out loud (in the report) whether each critical path **will work**, **won’t**, or is **missing a link** (import, route, schema, env, caller, export).

## Criteria sources

Collect Done when from (merge extras; never invent):

1. **Repair:** `.agents/temp/repairs/<repair-id>/ACCEPTANCE.md` or goal-nested `…/goals/<id>/repairs/<repair-id>/ACCEPTANCE.md`
2. **Goal:** `.agents/temp/goals/<goal-id>/GOAL.md` Done when + completed `plans/NN-*.md` AC
3. **`/trackers-flow`** ticket acceptance (read only)
4. Explicit criteria the user pasted

If none exist, **stop and ask**.

Also pull other skills when relevant — don’t fake their checks:

| Check | When | Skill |
| --- | --- | --- |
| Taste self-check | Code diffs | `/taste-flow` |
| Scalability | Lists, metrics, queries, dashboards | `/architecture` / `/architecture-flow` write-path rules |
| Design | UI in scope | `/design-flow` (or `/design` topics) |
| Still broken | Failures look like defects | `/repair-flow` or `/repair` |

Under `/goal`, prefer `*-flow` twins. Do not mix another goal-id’s criteria.

## Live evidence (terminals + fast CLI)

Point is **live state** about what you’re validating — types, lint, error logs, server push, UI runtime — not a Convex-only ritual.

### Prefer read first

1. **Any terminal** in the project terminals folder — frontend, backend, `convex dev`, workers, test watchers, typecheck watchers, whatever is already running
2. Cite `terminals/<id>.txt` (or equivalent) with the signal that matters
3. Match the criterion: type errors → typecheck/tsc terminal; UI crash → frontend terminal + localhost; API fail → API/server logs; Convex push fail → Convex terminal — **not** “always read Convex”

### Fast CLI when terminals aren’t enough

Run **narrow, fast** commands only when they answer a criterion and live output isn’t already there:

- Targeted `tsc --noEmit` / project typecheck script
- Targeted lint on touched files
- A single failing test / one smoke curl
- Repo scripts the user already uses for “is this healthy?”

**Do:** one purposeful command per gap in evidence.  
**Don’t:** ritual full-suite / lint-everything / second long-lived `convex dev` / Convex MCP verify loops as the default path.

**Forbidden as default:** Convex MCP (`logs`, `data`, `status`, `run`, …) when a terminal already shows push/ok or the error. Allowed only if terminals show an error you must diagnose, user asked for MCP, or no relevant terminal exists and you said so first.

## Process

### 1. Restate the bar

List each acceptance criterion as a checkbox. No new scope.

### 2. Code-path walk (required — out loud)

For each Done when (or each feature slice under validate), narrate the **runtime path**:

```markdown
### Path: <criterion or feature>
1. Entry: <route / UI / CLI / mutation caller>
2. → <module / function> (linked? yes/no — import, export, registration)
3. → <data / API / schema>
4. → <response / UI state>
**Verdict:** works | won’t work | missing link (<what>) | blocked (<why>)
```

Hunt specifically for **missing linking**:

- Export never imported / never registered (router, Convex `api`, plugin, cron)
- Schema field written but never read (or reverse)
- Env var required but unset / unread
- Button/handler with no action; action with no UI
- Plan file lane files never wired into the app entry

A missing link is **fail**, not a nit.

### 3. Evidence pass

Gather live evidence for each criterion (terminals first, fast CLI if needed). Mark **blocked** if you cannot see required UI/runtime and say what you need.

### 4. Scalability (when relevant)

If the diff touches lists/metrics/aggregates/hot queries: **Does this code scale?** Fail = fail validate. If N/A, say why.

### 5. Taste / design

`/taste-flow` implement self-check on the diff — failures are **fail**.  
UI in scope → `/design-flow` checks.

### 6. Report

```markdown
## Validation

**Context:** goal `<id>` | repair `<id>` | ad-hoc

| Criterion | Status | Evidence |
| --- | --- | --- |
| … | pass / fail / blocked | terminal `…` / CLI `…` / path walk |

### Code paths
| Path | Verdict | Missing link? |
| --- | --- | --- |
| … | works / won’t / missing link / blocked | … |

### Live signals
| Source | What it showed |
| --- | --- |
| terminals/<id>.txt | … |
| CLI: `<cmd>` | … |

### Taste
| Check | Status | Evidence |
| --- | --- | --- |
| … | pass / fail | … |

### Scalability
| Question | Status | Evidence |
| --- | --- | --- |
| Does this code scale? | pass / fail / N/A | … |

### Design (if UI)
| Check | Status | Evidence |
| --- | --- | --- |
| … | pass / fail | … |

### Failures
- …

### Scope creep
- …
```

### 7. Next step

| Result | Next |
| --- | --- |
| **All pass** | Closing a goal wave → `/code-review-flow`. After mid-goal `/repair-flow` → return to implement. After standalone `/repair` → done (or `/code-review` if asked) |
| **Fail** | Prefer **`/repair-flow`** / **`/repair`** (smallest) using the failure list → re-run `/validate-flow`. Massive → `/goal` / expand plans |
| **Blocked** | Ask how to verify |

## Anti-patterns

- Optimistic “it should be fine” / silent LGTM
- Only looking at Convex terminals when the criterion is types, lint, or frontend logs
- Skipping the code-path walk
- Passing while imports/routes/schema/callers are unlinked
- Ritual MCP / full lint+tsc when live terminals already answer
- Mixing another goal-id’s criteria
- Expanding criteria mid-flight without re-grill/re-plan
- Skipping `/code-review-flow` at goal ACHIEVED after a green validate
- Skipping re-validate after a repair patch

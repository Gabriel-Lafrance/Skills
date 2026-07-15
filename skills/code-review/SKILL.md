---
name: code-review
description: >-
  Two-axis review (Standards + Spec) of a git diff since a fixed point the user
  names (default main/master). Standards = taste-flow + architecture examples +
  thermonuclear maintainability. Agents may auto-invoke. Use for branch/PR
  review outside /goal. Under /goal use /code-review-flow.
---

# Code Review

**Standalone** review of whatever the user asked to review — typically `main...HEAD` (or another fixed point they name). Not the goal-loop reviewer; that is **`/code-review-flow`**.

Review along **two axes** (Matt Pocock style). Do not merge findings into one ranked list.

- **Standards** — `/taste-flow` + `/architecture` examples + thermonuclear maintainability
- **Spec** — does the change match the ticket / PR / PRD / what the user said?

Run axes as **parallel Cursor Task subagents**, then you aggregate. Do not solo-review a large diff when workers can.

If you need issue/PR/comment context, load **`/trackers-flow`** (read only). Never write to trackers.

## Process

### 1. Pin the fixed point

Prefer what the user named. If missing, default to **`main`** (or `master` if that is the default branch). Confirm:

```bash
git rev-parse <fixed-point>
git diff <fixed-point>...HEAD
git log <fixed-point>..HEAD --oneline
```

Fail early on bad ref or empty diff.

### 2. Spec source

In order (standalone — **not** a goal workspace unless the user points at one):

1. What the user pasted or asked to verify against
2. Linked PR / issue via `/trackers-flow` (read: body, comments, QA checklists)
3. Issue refs in commits (`#123`, `IN-1234`) — fetch via `/trackers-flow`
4. Path the user passed (`docs/`, `specs/`, …)
5. Ask; if none, Spec axis reports "no spec available"

### 3. Standards sources (force order)

1. **`/taste-flow`** + [examples.md](../taste-flow/examples.md) — hard; paste non-negotiables + naming into the Standards prompt
2. **`/architecture`** + [examples.md](../architecture/examples.md) — hard; entry points, folders, write-path aggregates
3. Repo `AGENTS.md` / `.cursor/rules/` when present — **repo wins** on conflict
4. Optional extras only if present — **do not** require `CODING_STANDARDS.md`
5. Smell baseline + **thermonuclear maintainability** below

### 4. Smell baseline (judgement calls)

Mysterious Name, Duplicated Code, Feature Envy, Data Clumps, Primitive Obsession, Repeated Switches, Shotgun Surgery, Divergent Change, Speculative Generality, Message Chains, Middle Man, Refused Bequest — skip what tooling already enforces.

### 5. Architecture + taste checks (hard unless repo docs contradict)

Flat file dump; missing simple entry point; leaking internals; anonymous `utils` bags; god files; nesting pyramids / `{ success: false }` / dynamic `import()`; wrong Convex/app naming; speculative ceremony; missing foundation seam on big features; mixed responsibility; class/interface depth > 2; compute-on-read metrics; unbounded collects / missing indexes.

### 6. Thermonuclear maintainability (Standards — not a third axis)

Be **ambitious** about structure. Search for **code judo**: preserve behavior while making the implementation dramatically simpler. Prefer deleting complexity over rearranging it.

**Non-negotiable additional standards:**

0. Ambitious structural simplification — whole branches/helpers/layers disappear when possible
1. **1000-line file rule** — do not push a file from under 1k to over 1k without a strong reason (presumptive blocker)
2. No spaghetti growth — ad-hoc conditionals bolted onto unrelated flows
3. Clean design > “it works”
4. Direct over magic / thin wrappers / identity abstractions
5. Type and boundary cleanliness — `any` / casts / muddy optionality
6. Canonical layer + reuse existing helpers
7. Avoid needless sequential orchestration / half-applied state when atomic structure is obvious

**Prioritize:** structural regressions → missed judo → spaghetti → boundaries/types → file size → modularity → legibility. Prefer fewer high-conviction comments over nit floods.

**Approval bar:** behavior-correct is **not** enough. Presumptive blockers: visible judo path ignored; file crosses 1k lines; ad-hoc branching; feature checks in shared code; unnecessary wrapper/cast churn; wrong layer / duplicate helper.

### 7. Parallel Task subagents

Launch Standards + Spec Tasks in one message (`generalPurpose` or `explore`). Optionally `bugbot` / `security-review` only if the user asked.

**Standards prompt** — diff + commits; `/taste-flow` non-negotiables; taste/architecture examples; thermonuclear rules; hard vs judgement; under ~400–500 words.

**Spec prompt** — diff + commits + spec path/contents; missing/partial requirements, scope creep, wrong implementations; under 400 words. Skip Spec if no spec.

### 8. Aggregate

Present `## Standards` and `## Spec` separately. One-line summary per axis. Do not pick a cross-axis winner.

Do **not** flag missing eslint/tsc or Convex MCP as Standards failures — CI owns lint/type; `/taste-flow` Verify is **read existing terminals**.

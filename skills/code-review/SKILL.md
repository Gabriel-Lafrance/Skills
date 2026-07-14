---
name: code-review
description: >-
  Two-axis review (Standards + Spec) of changes since a fixed point, using
  Cursor Task subagents in parallel. Use when reviewing a branch, PR, or
  work-in-progress after implement/validate.
---

# Code Review

Review the diff between `HEAD` and a fixed point along two axes (plus structure checks on Standards):

- **Standards** — coding standards + smell baseline + `/architecture` structure
- **Spec** — does the change match the plan / ticket / PRD?

Run axes as **parallel Cursor Task subagents**, then aggregate. Do not merge findings into one ranked list.

If you need issue context, run `/trackers` (Linear MCP or `gh`). Do not invent the ticket body.

## Process

### 1. Pin the fixed point

User supplies commit, branch, tag, `main`, etc. If missing, ask.

Confirm:

```bash
git rev-parse <fixed-point>
git diff <fixed-point>...HEAD
git log <fixed-point>..HEAD --oneline
```

Fail early on bad ref or empty diff.

### 2. Spec source

In order:

1. Active `/goal` ticket brief from `/trackers`
2. Issue refs in commits (`#123`, `IN-1234`) — fetch via `/trackers`
3. Path the user passed
4. Approved plan / file under `docs/`, `specs/`
5. Ask; if none, Spec axis reports "no spec available"

### 3. Standards sources

In order of force:

1. Repo docs (`CODING_STANDARDS.md`, `CONTRIBUTING.md`, `.cursor/rules/`, `AGENTS.md`) when present
2. **`/taste`** (pack contract — treat as hard; paste non-negotiables + naming into the Standards prompt)
3. Smell baseline below (judgement calls; skip what tooling already enforces)

**Smell baseline:**

- Mysterious Name → rename or redesign
- Duplicated Code → extract shared shape
- Feature Envy → move behavior to the data
- Data Clumps → introduce a type
- Primitive Obsession → small domain type
- Repeated Switches → polymorphism or shared map
- Shotgun Surgery → gather what changes together
- Divergent Change → split by reason to change
- Speculative Generality → delete unused abstraction
- Message Chains → hide the walk
- Middle Man → remove needless delegation
- Refused Bequest → prefer composition

**Architecture + taste checks** (hard unless repo docs contradict):

- Flat file dump — related new files with no feature/domain folder
- Missing simple entry point — callers must orchestrate helpers themselves
- Leaking internals — call sites import collaborators that should stay hidden
- Anonymous `utils` / `helpers` bags with no coherent concept
- God component/file — complexity at the call site instead of behind a hook/class/facade
- Nesting pyramids / `{ success: false }` bags / dynamic `import()`
- Wrong naming: hyphens in `convex/` filenames, or ignoring kebab-case in app/UI
- Speculative ceremony on tiny glue (factory theater for one-liners)
- Missing foundation seam on a big feature (callers must break to add the next variant)
- Mixed responsibility (e.g. logger that also sends notifications)
- Class/interface inheritance deeper than two levels
- SOLID-maximalist boilerplate that hurts readability without buying an extension seam
- **Compute-on-read/render metrics** — scanning children to derive counts/totals on every query instead of updating stored aggregates on write
- Unbounded collects / missing indexes on hot list paths

### 4. Parallel Task subagents

In one message, launch two Task agents (`subagent_type: "generalPurpose"` or `"explore"` for read-only). Optionally add `bugbot` / `security-review` only when the user asked for those reviews.

**Standards prompt** — include full diff command, commit list, `/taste` non-negotiables + naming rules pasted in full, standards file paths, smell baseline, and architecture/taste checks. Ask for: documented violations (cite rule) + baseline smells + architecture/taste findings (name + hunk). Under 400 words. Hard vs judgement call.

**Spec prompt** — include diff command, commit list, and spec contents/path. Ask for: missing/partial requirements, scope creep, wrong implementations — quote spec lines. Under 400 words.

Skip Spec agent if no spec.

### 5. Aggregate

Present `## Standards` and `## Spec` separately (verbatim or lightly cleaned). One-line summary per axis: count + worst issue. Do not pick a cross-axis winner.

## Why two axes

Standards-clean wrong feature ≠ done. Spec-perfect mess ≠ done. Keep axes separate so one cannot mask the other.

Do **not** flag “agent didn’t run eslint/tsc” as a Standards failure — CI owns lint/type; `/taste` Verify prefers running localhost + Convex output.

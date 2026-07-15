---
name: code-review
description: >-
  Two-axis review (Standards + Spec) of changes since a fixed point, using
  Cursor Task subagents in parallel. Standards = taste + architecture examples
  plus thermonuclear maintainability (code judo, 1k-line rule, spaghetti).
  Agents may auto-invoke. Use when reviewing a branch, PR, or work-in-progress
  after implement/validate. Under /goal use /code-review-flow.
---

# Code Review

Review the diff between `HEAD` and a fixed point along **two axes** (Matt Pocock style). Do not merge findings into one ranked list.

- **Standards** — `/taste` + `/architecture` (and their `examples.md`) + thermonuclear maintainability
- **Spec** — does the change match the plan / ticket / PRD?

Run axes as **parallel Cursor Task subagents** (required — see `/orchestrate`), then you aggregate. Do not solo-review a large diff when workers can.

Inside an active `/goal` loop, use **`/code-review-flow`** instead.

If you need issue/PR/comment context, load **`/trackers`** (read only). Do not invent the ticket body. Never write to trackers.

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

1. `.agents/temp/goals/<goal-id>/GOAL.md` + `GRILL.md` + `plans/INDEX.md` + relevant `plans/NN-*.md`
2. Active ticket brief from `/trackers` (read: issue, PR, comments, QA checklists)
3. Issue refs in commits (`#123`, `IN-1234`) — fetch via `/trackers`
4. Path the user passed
5. Plan / file under `docs/`, `specs/`
6. Ask; if none, Spec axis reports "no spec available"

Tell Spec/Standards Task subagents to **read that goal-id’s paths only** — never another workspace.

### 3. Standards sources (force order)

1. **`/taste`** + taste [examples.md](../taste/examples.md) — hard; paste non-negotiables + naming into the Standards prompt; cite good/bad pairs when relevant
2. **`/architecture`** + architecture [examples.md](../architecture/examples.md) — hard; entry points, folders, write-path aggregates / scale
3. Repo `AGENTS.md` / `.cursor/rules/` when present — **repo wins** on conflict with pack taste
4. Optional extras only if present (`CONTRIBUTING.md`, etc.) — **do not** require or prefer `CODING_STANDARDS.md`
5. Smell baseline + **thermonuclear maintainability** below

There is **no** project `CODING_STANDARDS.md` contract in this pack — Standards are taste + architecture examples + thermonuclear bar.

### 4. Smell baseline (judgement calls)

Skip what tooling already enforces:

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

### 5. Architecture + taste checks (hard unless repo docs contradict)

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

### 6. Thermonuclear maintainability (Standards — not a third axis)

Be **ambitious** about structure. Do not stop at local cleanup. Search for **code judo**: restructurings that preserve behavior while making the implementation dramatically simpler, smaller, more direct, and more elegant. Prefer deleting complexity over rearranging it.

**Non-negotiable additional standards:**

0. **Ambitious structural simplification** — look for paths where whole branches, helpers, modes, or layers disappear; prefer the solution that feels inevitable in hindsight.
1. **1000-line file rule** — do not let a PR push a file from under 1k lines to over 1k without a very strong reason. Prefer extract helpers/modules first. Crossing that threshold is a presumptive blocker unless clearly justified and still well organized.
2. **No spaghetti growth** — be highly suspicious of new ad-hoc conditionals, scattered special cases, or one-off branches bolted onto unrelated flows. Prefer a dedicated abstraction, helper, state machine, or module.
3. **Clean design > “it works”** — do not rubber-stamp working code that leaves the codebase messier.
4. **Direct over magic** — flag brittle/hacky behavior, thin wrappers, identity abstractions, and generic mechanisms that hide simple data-shape assumptions.
5. **Type and boundary cleanliness** — question unnecessary optionality, `any` / `unknown`, cast-heavy code, and silent fallbacks that paper over unclear invariants.
6. **Canonical layer + reuse** — call out feature logic in shared paths, details leaking through APIs, and bespoke helpers when a canonical utility already exists.
7. **Orchestration** — flag needless sequential async when independent work could stay simpler in parallel; flag partial-update flows when a more atomic structure is obvious (not micro-optimization nits).

**Primary review questions** (every meaningful change):

- Is there a code-judo move that would make this dramatically simpler?
- Can this be reframed with fewer concepts, branches, or helper layers?
- Does this improve or worsen local architecture?
- Did branching grow where a better abstraction should exist?
- Did a cohesive module become more coupled, stateful, or harder to scan?
- Is logic in the right file/layer? Did a file cross a healthy size boundary?
- Repeated conditionals → missing model/helper? Direct vs special-case control flow?
- Is the abstraction earning its keep, or just a wrapper?
- Casts / optionality / ad-hoc shapes obscuring the real invariant?
- Sequential or less atomic than it needs to be?

**Flag aggressively:** complicated implementations with a clearer reframing; refactors that move complexity without deleting concepts; file past 1k lines; bolted-on conditionals; one-off booleans/nullable modes; feature logic in general-purpose modules; magic generics; thin wrappers; unnecessary casts/`any`; copy-paste instead of helpers; edge-case handling mid busy function; “temporary” branching debt; wrong-layer logic; needless sequential/partial updates.

**Preferred remedies:** delete a layer of indirection; reframe state so conditionals disappear; change ownership so the feature extends an existing abstraction; simpler default with fewer exceptions; extract helper/pure function; split large files; typed model or dispatcher; separate orchestration from business logic; collapse duplicate branches; delete useless wrappers; reuse canonical helpers; explicit type boundaries; move logic to the owning package; parallelize when that simplifies; more atomic updates.

**Tone:** direct, serious, demanding about quality — not rude. Do not soften major maintainability issues into mild suggestions. Prefer fewer high-conviction structural comments over nit floods.

**Prioritize findings:** (1) structural regressions (2) missed judo / dramatic simplification (3) spaghetti / branching (4) boundary / abstraction / type contracts (5) file size / decomposition (6) modularity (7) legibility.

**Standards approval bar** — do **not** approve merely because behavior seems correct:

- no clear structural regression
- no obvious missed judo move when a simpler path is visible
- no unjustified file-size explosion past 1k lines
- no obvious spaghetti growth from special-case branching
- no hacky/magical abstraction that hurts reasoning
- no unnecessary wrapper/cast/optionality churn
- no clear architecture-boundary leak or avoidable helper duplication
- no missed obvious decomposition that would materially improve maintainability

Treat as **presumptive blockers** unless the author justifies clearly: preserved incidental complexity with a visible judo path; file crosses 1k lines; ad-hoc branching tangling an existing flow; feature checks scattered across shared code; unnecessary abstraction/wrapper/cast-heavy contract; duplicate helper or wrong layer.

### 7. Parallel Task subagents

In one message, launch two Task agents (`subagent_type: "generalPurpose"` or `"explore"` for read-only). Optionally add `bugbot` / `security-review` only when the user asked for those reviews.

**Standards prompt** — include:

- Full diff command + commit list
- `/taste` non-negotiables + naming rules pasted in full
- Instruct worker to read taste + architecture `examples.md` and cite matching good/bad when flagging
- Architecture/taste hard checks + smell baseline
- Thermonuclear rules (code judo, 1k lines, spaghetti, wrappers, boundaries, approval bar)
- Ask for: documented violations (cite taste/architecture/example or thermonuclear rule) + baseline smells + structural/judo findings (name + hunk). Mark **hard** vs judgement. Prioritize structural. Under ~400–500 words.

**Spec prompt** — include diff command, commit list, and spec contents/path (from plans and/or `/trackers` brief). Ask for: missing/partial requirements, scope creep, wrong implementations — quote spec lines. Under 400 words.

Skip Spec agent if no spec.

### 8. Aggregate

Present `## Standards` and `## Spec` separately (verbatim or lightly cleaned). One-line summary per axis: count + worst issue. Do not pick a cross-axis winner.

## Why two axes

Standards-clean wrong feature ≠ done. Spec-perfect mess ≠ done. Keep axes separate so one cannot mask the other.

Do **not** flag “agent didn’t run eslint/tsc” or “didn’t call Convex MCP” as a Standards failure — CI owns lint/type; `/taste` Verify is **read existing terminals**, not MCP.

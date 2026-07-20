# Code Review Doctrine

Review along **three axes** (do not merge findings into one ranked list):

- **Standards** — `/taste` + `/architecture` examples + thermonuclear maintainability
- **Spec** — does the change match the ticket / PR / PRD / what the user said?
- **Routes** — top-down codepath walk: loose parts, wrong callers, dead ends, missing links

`/pr-review` reuses these axes for posting on GitHub; this doctrine owns axis mechanics. `/pr-review` owns PR comment craft.

## Stance (A+ exam)

**Operational stance — not chat roleplay.** Behave with exam intensity; do not narrate as a student in chat. Findings stay factual.

You are the examinee. `/pr-review` is the hardcore grader. Assume anything you miss becomes a failure on the PR.

- **Stress-driven thoroughness** — re-walk paths, re-check taste/architecture, treat "it works" as not enough. Keep a 100% A+ average by catching defects before the teacher does.
- **Same bar as the teacher** — self-grade against thermonuclear, should-have-moved, complexity/entropy, and Routes critical/important (the same defects `/pr-review` will mark Blocking).
- **Prefer over-finding** on the Fix backlog over a clean rubber stamp. Nits stay optional.
- **Anti-patterns:** casual pass; waiving structural debt without naming it; solo shallow skim when Tasks can run.

Run axes as **parallel Cursor Task subagents**, then you aggregate. Do not solo-review a large diff when workers can.

If you need issue/PR/comment context, load **`/trackers`** (read only). Never write to trackers.

## Pin the fixed point

Prefer what the user named. If missing, default to **`main`** (or `master` if that is the default branch). Confirm:

```bash
git rev-parse <fixed-point>
git diff <fixed-point>...HEAD
git log <fixed-point>..HEAD --oneline
```

Fail early on bad ref or empty diff.

## Spec source

In order (standalone — **not** a goal workspace unless the user points at one):

1. What the user pasted or asked to verify against
2. Linked PR / issue via `/trackers` (read: body, comments, QA checklists)
3. Issue refs in commits (`#123`, `IN-1234`) — fetch via `/trackers`
4. Path the user passed (`docs/`, `specs/`, …)
5. Ask; if none, Spec axis reports "no spec available"

## Standards sources (force order)

1. **`/taste`** + [examples.md](../taste/examples.md) — hard; paste non-negotiables + naming into the Standards prompt
2. **`/architecture`** + [examples.md](../architecture/examples.md) — hard; entry points, folders, write-path aggregates
3. Repo `AGENTS.md` / `.cursor/rules/` when present — **repo wins** on conflict
4. Optional extras only if present — **do not** require `CODING_STANDARDS.md`
5. Smell baseline + **thermonuclear maintainability** below

## Smell baseline (judgement calls)

Mysterious Name, Duplicated Code, Feature Envy, Data Clumps, Primitive Obsession, Repeated Switches, Shotgun Surgery, Divergent Change, Speculative Generality, Message Chains, Middle Man, Refused Bequest — skip what tooling already enforces.

## Architecture + taste checks (hard unless repo docs contradict)

Flat file dump; missing simple entry point / **shallow modules**; leaking internals; anonymous `utils` bags; god files; nesting pyramids / `{ success: false }` / dynamic `import()`; wrong Convex/app naming; speculative ceremony; missing foundation seam on big services; **feature reimplements a domain service** (billing/auth/… forked instead of calling the public API); **bolting onto wrong placement / copying a bad sibling instead of a behavior-preserving move** (`/architecture` §3 — entropy); **complexity regression** or **entropy growth** (`/taste`); mixed responsibility; class/interface depth > 2; compute-on-read metrics; unbounded collects / missing indexes.

## Thermonuclear maintainability (Standards — not Routes)

Be **ambitious** about structure. Search for **code judo**: preserve behavior while making the implementation dramatically simpler. Prefer deleting complexity over rearranging it. **Builders** apply the same courage via `/architecture` prior-mistakes — not only at review time.

Lens (from `/taste`): **complexity** (hard to understand/change) and **entropy** (disorder that spreads when copied or left in a touched dirty lane).

**Non-negotiable additional standards:**

0. Ambitious structural simplification — whole branches/helpers/layers disappear when possible
1. **1000-line file rule** — do not push a file from under 1k to over 1k without a strong reason (presumptive blocker)
2. No spaghetti growth — ad-hoc conditionals bolted onto unrelated flows
3. Clean design > "it works"
4. Direct over magic / thin wrappers / identity abstractions
5. Type and boundary cleanliness — `any` / casts / muddy optionality
6. Canonical layer + reuse existing helpers
7. Avoid needless sequential orchestration / half-applied state when atomic structure is obvious
8. **Should-have-moved** — prior debt in the touched lane left in place (or copied) when a clear behavior-preserving relocation exists
9. **Complexity regression** — shallower interfaces, more call-site branching, unknown unknowns added without pulling complexity down behind a deep entry
10. **Entropy growth** — bolting onto a known-bad shape; copying debt; half-moves left live

**Prioritize:** structural regressions → complexity/entropy regressions → missed judo / missed moves → spaghetti → boundaries/types → file size → modularity → legibility. Prefer fewer high-conviction comments over nit floods.

**Approval bar:** behavior-correct is **not** enough. Presumptive blockers: visible judo path ignored; **should-have-moved debt ignored**; **clear complexity or entropy regression**; file crosses 1k lines; ad-hoc branching; feature checks in shared code; unnecessary wrapper/cast churn; wrong layer / duplicate helper.

## Routes axis (codepath walk — out loud)

Hunt **call-graph / wiring** problems in the diff's changed surface — not taste, not ticket wording.

**Start at the top**, walk **down** every relevant runtime path the change touches. Narrate **out loud** so a human can follow the trail (same spirit as `/validate` path walk, but review-focused).

**Hunt for:**

- Loose / public surfaces that can be called with the wrong args, wrong auth, wrong order, or from the wrong layer
- Dead ends — export never imported, handler never registered, branch that returns nothing useful, unreachable after a guard
- Missing links — UI → action, action → mutation, schema write ↔ read, env required but unread
- Ambiguous entry points — two ways in with different invariants; optional params that skip critical checks
- Wrong composition — helper safe alone but dangerous when this caller wires it
- **Half-moves** — old path still live alongside the new service/API (both wired or callers split incorrectly)

**Severity (required on every finding):**

| Tag | Use when |
| --- | --- |
| **critical** | Broken path, wrong caller can corrupt/leak/skip auth, dead end on a shipped flow |
| **important** | Real risk under plausible misuse or incomplete wiring; should fix before merge |
| **nit** | Clarity / naming / minor dead code that does not break a path |

**Routes Task output shape** (worker must use this):

```markdown
## Path: <entry → outcome name>
### Walk (out loud)
1. Entry: <route / UI / CLI / exported API>
2. → <fn/module> — <what it assumes / guards>
3. → <next hop> — <linked? how?>
4. → <terminal: DB / response / side effect>
### Summary
<2–4 sentences: what this path does and where it is fragile>
### Findings
- **critical|important|nit**: <issue> @ <file/symbol>
```

One Task may cover multiple paths. Prefer fewer high-conviction path summaries over listing every private helper.

## Parallel Task subagents

Launch **Standards + Spec + Routes** Tasks in one message (`generalPurpose` or `explore`). Skip Spec only if no spec. Optionally `bugbot` / `security-review` only if the user asked.

**Model:** omit Task `model` — inherit the parent chat model. Do not pick a slug unless the user asked.

**Standards prompt** — diff + commits; `/taste` non-negotiables + **complexity/entropy definition**; taste/architecture examples; thermonuclear rules; hunt **should-have-moved**, **complexity regressions**, and **entropy growth** in the touched lane and propose the relocation/judo (not "nit: consider later"); hard vs judgement; **exam posture:** hunt as if a hardcore teacher will fail this PR for anything you miss; under ~400–500 words.

**Spec prompt** — diff + commits + spec path/contents; missing/partial requirements, scope creep, wrong implementations; **exam posture:** hunt as if a hardcore teacher will fail this PR for anything you miss; under 400 words. Skip Spec if no spec.

**Routes prompt** — diff + commits; entry points touched by the change; instruct: start top-down, narrate walk out loud, summarize each path, tag every finding critical/important/nit; **exam posture:** hunt as if a hardcore teacher will fail this PR for anything you miss; under ~400–500 words. Do not re-litigate taste or ticket AC here.

## Aggregate

Present `## Standards`, `## Spec`, and `## Routes` separately. One-line summary per axis. Do not pick a cross-axis winner. Under Routes, keep the path walk summaries readable — do not collapse them into a flat severity list only.

## Behavior-lock recommendations (tell the user — do not run)

After the axes, if the diff touches a **complex architectural part** whose deep behavior is easy to break from the outside (complex hooks, domain/business logic, facades, stateful classes) and there is **no durable behavior lock**, add a short section:

```markdown
## Needs /create-test
- `path/to/symbol` — <one-line why a lock matters>
```

**Tell the user** to run `/create-test` on those subjects. Do **not** invoke `/create-test` yourself. Do not recommend locks for trivial wrappers, UI chrome, or coverage theater.

**Persist follow-ups:** when a goal workspace is in play, append each Needs `/create-test` row to `.agents/temp/goals/<goal-id>/FOLLOWUPS.md` (create if missing) as unchecked items, and mirror a one-line pointer in `STATUS.md`. ACHIEVED **Manual next steps** must list open FOLLOWUPS until the user runs `/create-test` or waives each by name.

Do **not** flag missing eslint/tsc or Convex MCP as Standards failures — CI owns lint/type; `/taste` Verify is **read existing terminals**.

## Offer to fix (batch ask → grill → `/goal`)

After the axes (and Needs `/create-test` if any), if there is **anything actionable** to fix — any **critical** / **important** Routes finding, Standards/Spec failure, or thermonuclear blocker (not pure nits-only):

1. Present a short **Fix backlog** (do not re-dump the whole review):

```markdown
## Fix backlog
1. **critical|important|standards|spec** — <one-line issue> @ <file/symbol>
2. **important** — move Stripe calls from `features/checkout` into `billing.makeUserPay` (behavior-preserving)
3. …
```

Relocation / should-have-moved items are **normal backlog** — not "out of scope refactor." Nits may be listed under `_Optional nits (skip unless you say otherwise)_` — they are **not** in the default backlog.

2. Ask with **`/grill-me`** — follow [../asking.md](../asking.md); one Questions batch. Include every decision you need now (fix offer, optional nits, `/create-test` subjects if listed). Example:

```markdown
## Questions
Reply like: `1a, 2b`

1. Fix the Fix backlog?
   - a) yes — start /goal to clear it ← recommended
   - b) no — leave findings as-is
2. (If Needs /create-test) Run /create-test on the listed subjects after fixes?
   - a) yes — remind me
   - b) no / later
```

3. **On fix = no:** stop. Review is done. Do not start coding or `/goal`.

4. **On fix = yes:** start **`/goal`** whose outcome is clearing that backlog — treat it like a goal to fix the review, not a silent drive-by patch:

| Step | Do |
| --- | --- |
| Goal contract | Goal = fix the Fix backlog; Done when = binary check per backlog item (or tight groups); Context = this review + fixed-point diff; Constraints = no unrelated product scope — **behavior-preserving moves listed in the backlog are in scope** |
| Grill | Run **`/grill-me`** (via `/goal` Phase 0) focused on the findings — **one batched Questions** for what/how/footprint/non-goals/split; **recommend moves** when debt is in the backlog (see `/grill-me` + `/architecture` §3) |
| Gates | Non-goals + split + shared understanding in that same batch |
| Build | Continue `/goal` Phase 1 (plans → implement → link checkup → validate → `/code-review`) |

Do **not** start coding between "yes" and grill shared-understanding. Do **not** silently pick approaches — grill first (batched).

If the backlog is a **single tiny defect** and the user already said how to fix it in the batch notes, you may still open `/goal` with skip-grill only when `/goal`'s skip-grill rule fully applies — default is grill.

**Empty backlog** (nits only, or clean review): skip this section; optionally note `_Nothing actionable to fix._`

## Anti-patterns

- Casual pass / rubber stamp while defects remain that `/pr-review` would Blocking
- Ending the review without the Fix backlog + Questions batch when critical/important/Standards/Spec failures exist
- Coding fixes immediately on "yes" without `/goal` + grill
- Dripping one review follow-up question per message when several are known
- Treating nits as mandatory backlog items unless the user asked
- Waiving structural debt as "pre-existing, leave it"; approving "it works" while the shape violates `/architecture` services / prior-mistakes doctrine or `/taste` complexity/entropy
- Treating relocation backlog items as out-of-scope refactors
- Writing to Linear/GitHub from this skill
- Auto-running `/create-test` instead of recommending it
- Narrating exam roleplay in chat ("I'm the stressed student…") instead of factual findings

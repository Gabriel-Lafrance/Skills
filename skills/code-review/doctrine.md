# Code Review Doctrine

Review along **five axes** (do not merge findings into one ranked list):

- **Standards** — `/taste` + `/architecture` examples + thermonuclear maintainability
- **Spec** — does the change match the ticket / PR / PRD / what the user said?
- **Routes** — top-down codepath walk **plus blast radius**: loose parts, wrong callers, dead ends, missing links, outside-diff callers, half-moves
- **BigPicture** — holistic fit: feature coherence vs product/domain shape, cross-cutting consistency, missing sibling seams
- **Risk** — security flaws, correctness bugs, non-scalable algorithms (Big-O, unbounded work, N+1, hot-path scans), authz/race holes

`/pr-review` reuses these axes for posting on GitHub; this doctrine owns axis mechanics. `/pr-review` owns PR comment craft.

## Stance (A+ exam)

**Operational stance — not chat roleplay.** Behave with exam intensity; do not narrate as a student in chat. Findings stay factual.

You are the examinee. `/pr-review` is the hardcore grader. Assume anything you miss becomes a failure on the PR.

- **Stress-driven thoroughness** — re-walk paths, re-check taste/architecture, treat "it works" as not enough. Keep a 100% A+ average by catching defects before the teacher does.
- **Same bar as the teacher** — self-grade against thermonuclear, should-have-moved, complexity/entropy, Routes critical/important, BigPicture coherence failures, and Risk security/bug/scale findings (the same defects `/pr-review` will mark Blocking).
- **Prefer over-finding** on the Fix backlog over a clean rubber stamp. Nits stay optional on the default backlog — but **list every real defect**; there is **no findings cap**. A shitty PR should surface everything shitty about it.
- **Anti-patterns:** casual pass; waiving structural debt without naming it; solo shallow skim when Tasks can run; skipping Wave 2.

Run **Wave 1** (five parallel Tasks) then **Wave 2** (adversarial). Do not solo-review a large diff when workers can.

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

When UI files are in the diff, also load **`/design`** into Standards (and BigPicture) — same gate as `/pr-review`.

## Smell baseline (judgement calls)

Mysterious Name, Duplicated Code, Feature Envy, Data Clumps, Primitive Obsession, Repeated Switches, Shotgun Surgery, Divergent Change, Speculative Generality, Message Chains, Middle Man, Refused Bequest — skip what tooling already enforces.

## Architecture + taste checks (hard unless repo docs contradict)

Flat file dump; missing simple entry point / **shallow modules**; leaking internals; anonymous `utils` bags; god files; nesting pyramids / `{ success: false }` / dynamic `import()`; wrong Convex/app naming; speculative ceremony; missing foundation seam on big services; **feature reimplements a domain service** (billing/auth/… forked instead of calling the public API); **forking or bypassing an existing primitive's one job** (`/architecture` §3 — complexity + entropy); **bolting onto wrong placement / copying a bad sibling instead of a behavior-preserving move** (`/architecture` §4 — entropy); **complexity regression** or **entropy growth** (`/taste`); mixed responsibility; class/interface depth > 2; compute-on-read metrics; unbounded collects / missing indexes.

## Thermonuclear maintainability (Standards — not Routes)

Be **ambitious** about structure. Search for **code judo**: preserve behavior while making the implementation dramatically simpler. Prefer deleting complexity over rearranging it. **Builders** apply the same courage via `/architecture` prior-mistakes — not only at review time.

Lens (from `/taste`): **complexity** (hard to understand/change) and **entropy** (disorder that spreads when copied or left in a touched dirty lane).

**Non-negotiable additional standards:**

0. Ambitious structural simplification — whole branches/helpers/layers disappear when possible
1. **1000-line file rule** — do not push a file from under 1k to over 1k without a strong reason (presumptive blocker)
2. No spaghetti growth — ad-hoc conditionals bolted onto unrelated flows
3. Clean design > "it works"
4. Direct over magic / thin wrappers / identity abstractions — **strong primitives** (`/architecture` §3) are deep one-job blocks inside services/modules; identity wrappers still fail
5. Type and boundary cleanliness — `any` / casts / muddy optionality
6. Canonical layer + reuse existing helpers **and primitives**
7. Avoid needless sequential orchestration / half-applied state when atomic structure is obvious
8. **Should-have-moved** — prior debt in the touched lane left in place (or copied) when a clear behavior-preserving relocation exists
9. **Complexity regression** — shallower interfaces, more call-site branching, unknown unknowns added without pulling complexity down behind a deep entry; **forking a primitive's job**
10. **Entropy growth** — bolting onto a known-bad shape; copying debt; half-moves left live; **bypassing an existing primitive**

**Prioritize:** structural regressions → complexity/entropy regressions → missed judo / missed moves → spaghetti → boundaries/types → file size → modularity → legibility. Still list **every** real defect (no findings cap); severity tags separate blockers from nits.

**Approval bar:** behavior-correct is **not** enough. Presumptive blockers: visible judo path ignored; **should-have-moved debt ignored**; **clear complexity or entropy regression**; file crosses 1k lines; ad-hoc branching; feature checks in shared code; unnecessary wrapper/cast churn; wrong layer / duplicate helper.

## Artifact contracts (fill-or-fail)

Parent **rejects and relaunches** a worker that returns free-form narrative without the required shape. **No findings cap** — list every real defect. Keep “real defects only / no invented issues.”

### Standards output shape

```markdown
## Standards findings
- **hard|judgement**: <issue> @ <file/symbol> — cite <taste|architecture|thermonuclear|smell|design>
```

### Spec output shape

```markdown
## AC matrix
| AC / checklist row | Status | Evidence |
| --- | --- | --- |
| <Done-when / checklist item> | met \| partial \| missing \| n/a | <hunk / symbol / "absent"> |

## Scope / wrong impl
- <scope creep or wrong implementation> @ <file/symbol>
```

If no spec: report `## Spec — no spec available` and stop (do not invent AC).

### Routes output shape

Path walks **plus** blast radius (required):

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

## Blast radius
- Touched shared symbol: `<symbol>` @ `<file>`
  - Outside-diff callers at risk: <list or "none found">
  - Half-move / duplicate wiring: <yes/no + detail>
  - Wrong-layer callers: <yes/no + detail>
### Blast findings
- **critical|important|nit**: <issue> @ <file/symbol>
```

One Task may cover multiple paths. Cover every relevant shipped path and every touched shared symbol with real callers — do not skim to stay short.

### BigPicture output shape

```markdown
## System read
<3–6 sentences: what this change is trying to be in the product/domain>

## Coherence findings
- **critical|important|nit**: <issue> @ <file/symbol or seam>

## Missing big-picture links
- <sibling seam / cross-cutting concern that should connect and does not>
```

BigPicture owns holistic fit — not line-by-line hunk nits (defer those to Standards/Routes).

### Risk output shape

```markdown
## Risk findings
- **security|bug|scale** · **critical|important|nit**: <issue> @ <file/symbol> — <why it fails under load/abuse>
```

Risk owns security, correctness bugs, Big-O / unbounded collects / N+1 / hot-path scans, obvious race/authz holes. Not style/naming unless it causes a real risk.

## Routes axis (codepath walk + blast radius)

Hunt **call-graph / wiring** problems in the diff's changed surface — not taste, not ticket wording.

**Start at the top**, walk **down** every relevant runtime path the change touches. Narrate **out loud** so a human can follow the trail (same spirit as `/validate` path walk, but review-focused).

**Hunt for (paths):**

- Loose / public surfaces that can be called with the wrong args, wrong auth, wrong order, or from the wrong layer
- Dead ends — export never imported, handler never registered, branch that returns nothing useful, unreachable after a guard
- Missing links — UI → action, action → mutation, schema write ↔ read, env required but unread
- Ambiguous entry points — two ways in with different invariants; optional params that skip critical checks
- Wrong composition — helper safe alone but dangerous when this caller wires it
- **Half-moves** — old path still live alongside the new service/API (both wired or callers split incorrectly)

**Hunt for (blast radius — required):**

- Touched shared modules/symbols → who else calls them **outside the diff**
- Shared-module impact — a “local” change that breaks sibling features
- Half-moves left live; wrong-layer callers; dead/duplicate wiring across the blast surface

**Severity (required on every Routes finding):**

| Tag | Use when |
| --- | --- |
| **critical** | Broken path, wrong caller can corrupt/leak/skip auth, dead end on a shipped flow, blast breaks a live sibling |
| **important** | Real risk under plausible misuse or incomplete wiring; should fix before merge |
| **nit** | Clarity / naming / minor dead code that does not break a path |

## BigPicture axis

Zoom out beyond hunks. Ask: does this change make sense as a whole in the product/domain? Are cross-cutting concerns consistent? Are sibling seams missing?

When UI is in the diff, check coherence against `/design` at the product-surface level (not pixel nits — those stay Standards).

**Severity:** same critical / important / nit tags as Routes.

## Risk axis

Hunt defects that hurt users or the system under abuse/load — not taste.

**Hunt for:**

- Security — authz holes, injection, secret leakage, SSRF, unsafe deserialization, missing auth on public surfaces
- Bugs — incorrect invariants, off-by-one, race conditions, null/undefined traps on shipped paths
- Scale — Big-O blowups, unbounded `.collect()`, N+1 queries, compute-on-read on hot paths, scans that will not survive growth

**Severity:** same critical / important / nit tags. Tag every finding `security` | `bug` | `scale`.

Risk **replaces** default reliance on Cursor `bugbot` / `security-review` subagent types. Launch those tools **only** if the user explicitly asks.

## Wave 1 — five parallel Tasks

Launch **Standards + Spec + Routes + BigPicture + Risk** in **one** message (`generalPurpose` or `explore`). Skip Spec only if no spec.

**Model:** omit Task `model` — inherit the parent chat model. Do not pick a slug unless the user asked.

**Standards prompt** — diff + commits; `/taste` non-negotiables + **complexity/entropy definition**; taste/architecture examples; thermonuclear rules; `/design` when UI; hunt **should-have-moved**, **complexity regressions**, and **entropy growth** in the touched lane and propose the relocation/judo (not "nit: consider later"); hard vs judgement; require Standards artifact shape; **exam posture:** hunt as if a hardcore teacher will fail this PR for anything you miss; **no findings cap / no word cap**.

**Spec prompt** — diff + commits + spec path/contents; require AC matrix artifact; missing/partial requirements, scope creep, wrong implementations; **exam posture**; **no findings cap / no word cap**. Skip Spec if no spec.

**Routes prompt** — diff + commits; entry points touched by the change; start top-down, narrate walk out loud, summarize each path, **required Blast radius section**, tag every finding critical/important/nit; require Routes artifact shape; **exam posture**; **no findings cap / no word cap**. Do not re-litigate taste or ticket AC here.

**BigPicture prompt** — diff + commits; product/domain context from spec if any; require BigPicture artifact shape; holistic coherence + missing sibling seams; **exam posture**; **no findings cap / no word cap**. Do not line-nit hunks.

**Risk prompt** — diff + commits; require Risk artifact shape; hunt security, bugs, scale (Big-O / unbounded / N+1 / hot-path); tag `security|bug|scale` + severity; **exam posture**; **no findings cap / no word cap**. Do not re-litigate taste or ticket AC.

Parent: if any worker returns narrative without its artifact shape → **reject and relaunch** that axis.

## Aggregate (after Wave 1)

Present `## Standards`, `## Spec`, `## Routes`, `## BigPicture`, and `## Risk` separately. One-line summary per axis. Do not pick a cross-axis winner. Under Routes, keep path walks **and** blast radius readable — do not collapse them into a flat severity list only.

Keep Wave 1 axis summaries ready to feed Wave 2 (compact, factual).

## Wave 2 — adversarial (always)

**Always** run after Wave 1 aggregate — even when Wave 1 found many issues.

Launch **fresh** Task(s) in one message (`generalPurpose` or `explore`). **Omit Task `model`** unless the user asked.

**Input:** fixed-point diff + commits + **Wave 1 axis summaries** (not full chat fluff).

**Job:** prove Wave 1 missed real defects; hunt contradictions between axes; do **not** restate Wave 1 findings unless disagreeing with them.

**Output shape:**

```markdown
## Adversarial findings
- **standards|spec|routes|bigpicture|risk|cross-axis** · **critical|important|nit**: <new issue> @ <file/symbol> — <why Wave 1 missed it>
```

Parent merges unique hits into the five axis sections (or show a short `## Adversarial addenda` then fold into Fix backlog / PR drafts). Drop duplicates of Wave 1.

Same exam posture. Real defects only — invent nothing.

## Behavior-lock recommendations (tell the user — do not run)

After Wave 1 + Wave 2 (and Needs `/create-test` if any), if the diff touches a **complex architectural part** whose deep behavior is easy to break from the outside (complex hooks, domain/business logic, facades, stateful classes) and there is **no durable behavior lock**, add a short section:

```markdown
## Needs /create-test
- `path/to/symbol` — <one-line why a lock matters>
```

**Tell the user** to run `/create-test` on those subjects. Do **not** invoke `/create-test` yourself. Do **not** write test files from this skill. Do not recommend locks for trivial wrappers, UI chrome, or coverage theater.

**Who may recommend:** only `/code-review` and `/pr-review`. Other pack skills must not recommend or start `/create-test`.

**Persist follow-ups:** when a goal workspace is in play, append each Needs `/create-test` row to `.agents/temp/goals/<goal-id>/FOLLOWUPS.md` (create if missing) as unchecked items, and mirror a one-line pointer in `STATUS.md`. ACHIEVED **Manual next steps** must list open FOLLOWUPS until the user runs `/create-test` or waives each by name.

Do **not** flag missing eslint/tsc or Convex MCP as Standards failures — CI owns lint/type; `/taste` Verify is **read existing terminals**.

## Offer to fix (batch ask → grill → `/goal`)

After Wave 1 + Wave 2 (and Needs `/create-test` if any), if there is **anything actionable** to fix — any **critical** / **important** Routes, BigPicture, or Risk finding, Standards/Spec failure, or thermonuclear blocker (not pure nits-only):

1. Present a short **Fix backlog** (do not re-dump the whole review):

```markdown
## Fix backlog
1. **critical|important|standards|spec|bigpicture|risk** — <one-line issue> @ <file/symbol>
2. **important** — move Stripe calls from `features/checkout` into `billing.makeUserPay` (behavior-preserving)
3. …
```

Relocation / should-have-moved items are **normal backlog** — not "out of scope refactor." Nits may be listed under `_Optional nits (skip unless you say otherwise)_` — they are **not** in the default backlog.

2. Ask with **`/grill-me`** — follow [../asking.md](../asking.md); one Questions batch. Include every decision you need now (fix offer, optional nits, `/create-test` subjects if listed). Example:

```markdown
## Questions
Reply like: 1a 2b

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
| Grill | Run **`/grill-me`** (via `/goal` Phase 0) focused on the findings — Questions only for real what/how/footprint opens; **announce** non-goals + split + shared-understanding summary in Locked; **recommend moves** when debt is in the backlog (see `/grill-me` + `/architecture` §4) |
| Gates | Announce non-goals + split + shared understanding (correct if wrong) |
| Build | Continue `/goal` Phase 1 (plans → implement → link checkup → validate → `/code-review`) |

Do **not** start coding between "yes" and grill shared-understanding. Do **not** silently pick approaches — grill first (batched).

If the backlog is a **single tiny defect** and the user already said how to fix it in the batch notes, you may still open `/goal` with skip-grill only when `/goal`'s skip-grill rule fully applies — default is grill.

**Empty backlog** (nits only, or clean review): skip this section; optionally note `_Nothing actionable to fix._`

## Anti-patterns

- Casual pass / rubber stamp while defects remain that `/pr-review` would Blocking
- Skipping Wave 2 or solo-reviewing when five Wave 1 Tasks can run
- Accepting a worker report that skips its artifact shape
- Capping findings or word-limiting workers so defects stay hidden
- Ending the review without the Fix backlog + Questions batch when critical/important/Standards/Spec/BigPicture/Risk failures exist
- Coding fixes immediately on "yes" without `/goal` + grill
- Dripping one review follow-up question per message when several are known
- Treating nits as mandatory backlog items unless the user asked
- Waiving structural debt as "pre-existing, leave it"; approving "it works" while the shape violates `/architecture` services / prior-mistakes doctrine or `/taste` complexity/entropy
- Treating relocation backlog items as out-of-scope refactors
- Writing to Linear/GitHub from this skill
- Auto-running `/create-test` instead of recommending it
- Writing or editing test files from this skill (only `/create-test` writes tests)
- Auto-launching `bugbot` / `security-review` when the user did not ask (Risk axis covers that)
- Narrating exam roleplay in chat ("I'm the stressed student…") instead of factual findings

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

- **Stress-driven thoroughness** — re-walk paths, re-check taste/architecture, and catch defects before the teacher does. Thoroughness means better evidence, not inventing hypothetical failures.
- **Same bar as the teacher** — self-grade against thermonuclear, should-have-moved, complexity/entropy, Routes critical/important, BigPicture coherence failures, and Risk security/bug/scale findings. Then classify each real finding as Fix now, Follow-up, or optional nit rather than treating all structure as a blocker.
- **Complete real coverage** over a clean rubber stamp on an initial review. List every evidenced defect; there is **no findings cap**. Do not turn a remote theoretical possibility into a finding.
- **Anti-patterns:** casual pass; hiding structural debt; solo shallow skim when Tasks can run; skipping Wave 2 on an initial review.

For an **initial review**, run **Wave 1** (five parallel Tasks) then **Wave 2** (adversarial). Do not solo-review a large diff when workers can.

If you need issue/PR/comment context, load **`/trackers`** (read only). Never write to trackers.

## Evidence-based failure policy

A reviewer may flag a failure, race, missing guard, error path, retry, queue, or other hardening need only when the finding has all of the following:

1. **Reachable trigger** — a concrete caller, state transition, input, external response, or load path can reach the failure.
2. **Evidence** — a code-path walk, hunk, violated `INV-*` rule, existing production/test signal, or directly provable exploit demonstrates the trigger.
3. **Material impact** — the reachable outcome can break correctness, security, data integrity, availability, or a named acceptance rule.
4. **Proportional remedy** — the finding proposes the smallest direct control at the authoritative boundary first.

Do not assign fictional numerical probabilities. A rare but directly exploitable security path or invariant violation is still actionable; an unproven “this might fail someday” scenario is not. Do not add it to Fix now, Follow-up, a PR comment, or a risk report unless the user explicitly asks for speculative threat modeling.

### Defensive-code budget

- Add an `if` only for a reachable invalid state, input, or locked invariant. Do not duplicate a guard already enforced at the authoritative boundary.
- Add `try/catch` only at a boundary that can recover, translate, add actionable context, or clean up. Do not request catch-and-rethrow wrappers around local code.
- Add retries only for an evidenced transient external failure and an idempotent operation with a defined limit.
- Add queues, locks, error queues, or new coordination systems only when evidence shows an authoritative guard cannot preserve the required ordering, durability, concurrency, or backpressure behavior.

If those facts are absent, omit the finding. Review the implementation that exists, not an imagined distributed system around it.

## Review modes

| Mode | Scope | Required depth |
| --- | --- | --- |
| **Initial review** | Full shipped diff and goal/ticket contract | Full five axes plus adversarial Wave 2 |
| **Targeted re-review** | Named `Fix now` backlog, fix diff, touched paths, direct callers, and relevant Active Rules | Verify the named blocker is cleared; hunt only regressions, correctness, and security in the touched surface |

Targeted re-review is deliberately not another thermonuclear architecture hunt. Do not create a new optional structural finding during a re-review unless it is required to clear a named blocker, is a regression from the fix, or is a correctness/security failure in a touched path. Put valuable but non-blocking cleanup in **Follow-up**.

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

## Active Rules as binding spec

For a goal-scoped review, read `GOAL.md` **Active Rules (Invariants)** before dispatching workers. They are binding behavioral specification, not background context. A finding that violates one must cite its `INV-*` ID and say whether the authoritative enforcement point is missing, bypassable, or unverified.

For findings that do not violate an Active Rule, cite the relevant Done-when, acceptance criterion, correctness/security condition, or state `rule: none`. Do not invent an invariant after the fact to make an optional cleanup sound blocking.

## Standards sources (force order)

1. **`/taste`** + [examples.md](../taste/examples.md) — hard; paste non-negotiables + naming into the Standards prompt
2. **`/architecture`** + [examples.md](../architecture/examples.md) — hard; entry points, folders, write-path aggregates
3. Repo `AGENTS.md` / `.cursor/rules/` when present — **repo wins** on conflict
4. Optional extras only if present — **do not** require `CODING_STANDARDS.md`
5. Smell baseline + **thermonuclear maintainability** below

When UI files are in the diff, also load **`/design`** into Standards (and BigPicture) — same gate as `/pr-review`. When a reachable local or approved preview and Browser capability are available, use the [Browser validation reference](../validate/reference.md) for targeted visual and interaction review. If they are unavailable, report that visual confirmation was not performed; static review is not visual proof.

## Smell baseline (judgement calls)

Mysterious Name, Duplicated Code, Feature Envy, Data Clumps, Primitive Obsession, Repeated Switches, Shotgun Surgery, Divergent Change, Speculative Generality, Message Chains, Middle Man, Refused Bequest — skip what tooling already enforces.

## Architecture + taste checks (hard unless repo docs contradict)

Flat file dump; missing simple entry point / **shallow modules**; leaking internals; anonymous `utils` bags; god files; nesting pyramids / `{ success: false }` / dynamic `import()`; wrong Convex/app naming; speculative ceremony; missing foundation seam on big services; **feature reimplements a domain service** (billing/auth/… forked instead of calling the public API); **forking or bypassing an existing primitive's one job** (`/architecture` §3 — complexity + entropy); **bolting onto wrong placement / copying a bad sibling instead of a behavior-preserving move** (`/architecture` §4 — entropy); **complexity regression** or **entropy growth** (`/taste`); mixed responsibility; class/interface depth > 2; compute-on-read metrics; unbounded collects / missing indexes.

## Thermonuclear maintainability (Standards — not Routes)

In an **initial review**, be ambitious about structure. Search for **code judo**: preserve behavior while making the implementation dramatically simpler. Prefer deleting complexity over rearranging it. In a **targeted re-review**, inspect structural changes only when they are needed to clear a named blocker, prevent a regression, or correct a touched correctness/security failure.

Lens (from `/taste`): **complexity** (hard to understand/change) and **entropy** (disorder that spreads when copied or left in a touched dirty lane).

**Additional standards to evaluate on an initial review:**

0. Ambitious structural simplification — whole branches/helpers/layers disappear when needed to clear a current blocker
1. **1000-line file rule** — do not push a file from under 1k to over 1k without a strong reason (presumptive finding; disposition per the bar below)
2. No spaghetti growth — ad-hoc conditionals bolted onto unrelated flows
3. Clean design > "it works"
4. Direct over magic / thin wrappers / identity abstractions — **strong primitives** (`/architecture` §3) are deep one-job blocks inside services/modules; identity wrappers still fail
5. Type and boundary cleanliness — `any` / casts / muddy optionality
6. Canonical layer + reuse existing helpers **and primitives**
7. Avoid needless sequential orchestration / half-applied state when atomic structure is obvious
8. **Should-have-moved** — prior debt in the touched lane left in place (or copied) when a clear behavior-preserving relocation is required to clear a current blocker
9. **Complexity regression** — shallower interfaces, more call-site branching, unknown unknowns added without pulling complexity down behind a deep entry; **forking a primitive's job**
10. **Entropy growth** — bolting onto a known-bad shape; copying debt; half-moves left live; **bypassing an existing primitive**

**Prioritize:** correctness/security and Active Rule failures → clear complexity/entropy regressions → missed judo / missed moves → spaghetti → boundaries/types → file size → modularity → legibility. Still list every real defect on an initial review; severity and disposition separate blockers from follow-ups.

**Disposition bar:** behavior-correct is not always enough, but a valuable structural improvement is not automatically a current-goal blocker. Put an item in **Fix now** only when it violates a spec or `INV-*` rule, causes a correctness/security failure, is a regression, or a named finding proves the structural change is necessary. Otherwise keep it visible in **Follow-up**. A file crossing 1k lines, needless wrapper, clear complexity regression, or duplicate helper is a Fix-now item only when it meets that threshold.

## Artifact contracts (fill-or-fail)

Parent **rejects and relaunches** a worker that returns free-form narrative without the required shape. **No findings cap** — list every real defect. Keep “real defects only / no invented issues.”

### Standards output shape

```markdown
## Standards findings
- **hard|judgement**: <issue> @ <file/symbol> — rule: <INV-1 | Done-when | AC | none>; cite <taste|architecture|thermonuclear|smell|design>
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
- **critical|important|nit**: <issue> @ <file/symbol> — rule: <INV-1 | Done-when | AC | none>

## Blast radius
- Touched shared symbol: `<symbol>` @ `<file>`
  - Outside-diff callers at risk: <list or "none found">
  - Half-move / duplicate wiring: <yes/no + detail>
  - Wrong-layer callers: <yes/no + detail>
### Blast findings
- **critical|important|nit**: <issue> @ <file/symbol> — rule: <INV-1 | Done-when | AC | none>
```

One Task may cover multiple paths. Cover every relevant shipped path and every touched shared symbol with real callers — do not skim to stay short.

### BigPicture output shape

```markdown
## System read
<3–6 sentences: what this change is trying to be in the product/domain>

## Coherence findings
- **critical|important|nit**: <issue> @ <file/symbol or seam> — rule: <INV-1 | Done-when | AC | none>

## Missing big-picture links
- <sibling seam / cross-cutting concern that should connect and does not>
```

BigPicture owns holistic fit — not line-by-line hunk nits (defer those to Standards/Routes).

### Risk output shape

```markdown
## Risk findings
- **security|bug|scale** · **critical|important|nit**: <issue> @ <file/symbol>
  - **Trigger:** <reachable caller, state, input, response, or load path>
  - **Evidence:** <path walk, hunk, violated INV, signal, or exploit proof>
  - **Impact:** <concrete consequence>
  - **Smallest fix:** <direct guard or correction>
  - **Why not heavier machinery:** <why no retry/queue/lock/wrapper is needed, or concrete evidence it is>
```

Risk owns security, correctness bugs, Big-O / unbounded collects / N+1 / hot-path scans, and evidenced race/authz holes. Not style/naming unless it causes a real risk. A hypothetical concern with no reachable trigger and evidence is not a Risk finding.

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

Hunt evidenced defects that hurt users or the system under abuse/load — not taste. Apply the Evidence-based failure policy before emitting a finding.

**Hunt for:**

- Security — authz holes, injection, secret leakage, SSRF, unsafe deserialization, missing auth on public surfaces
- Bugs — incorrect invariants, off-by-one, race conditions, null/undefined traps on shipped paths
- Scale — Big-O blowups, unbounded `.collect()`, N+1 queries, compute-on-read on hot paths, scans that will not survive growth

Do not flag absent `if` statements, `try/catch`, retries, queues, locks, or error systems merely because such a mechanism could theoretically be useful. Show the trigger and why the smallest direct control cannot already handle it.

**Severity:** same critical / important / nit tags. Tag every finding `security` | `bug` | `scale`.

Risk **replaces** default reliance on Cursor `bugbot` / `security-review` subagent types. Launch those tools **only** if the user explicitly asks.

## Remedies: simplest authority first

For a correctness or race-risk finding, recommend the least invasive enforcement at the authority that owns the state. Explain why a stronger system is necessary before recommending it.

Example: `INV-1 — X is unavailable while Y processes`.

1. UI disables X while Y is processing for immediate feedback.
2. The backend mutation or state transition checks Y's current status and rejects X directly when it is processing.
3. A queue, lock, retry loop, wrapper, or new service is justified only if the review shows that this direct authoritative guard cannot make the transition safe.

Do not turn a simple guard into architecture theater. The review must name the trigger, rule, direct guard, and evidence; extra machinery needs concrete failure evidence. If it cannot, omit the finding.

## Wave 1 — initial full scan

For an **initial review**, launch **Standards + Spec + Routes + BigPicture + Risk** in **one** message (`generalPurpose` or `explore`). Skip Spec only if no spec. Include the goal's relevant Active Rules in every worker brief.

**Model:** omit Task `model` — inherit the parent chat model. Do not pick a slug unless the user asked.

**Standards prompt** — diff + commits; relevant Active Rules; `/taste` non-negotiables + **complexity/entropy definition**; taste/architecture examples; thermonuclear rules; `/design` when UI; hunt **should-have-moved**, **complexity regressions**, and **entropy growth** in the touched lane; classify a relocation/judo as Fix now only when it is required to clear a blocker, otherwise Follow-up; hard vs judgement; require Standards artifact shape; **exam posture:** hunt as if a hardcore teacher will fail this PR for anything you miss; **no findings cap / no word cap**.

**Spec prompt** — diff + commits + spec path/contents; require AC matrix artifact; missing/partial requirements, scope creep, wrong implementations; **exam posture**; **no findings cap / no word cap**. Skip Spec if no spec.

**Routes prompt** — diff + commits; entry points touched by the change; start top-down, narrate walk out loud, summarize each path, **required Blast radius section**, tag every finding critical/important/nit with a reachable path and code evidence; require Routes artifact shape; **exam posture**; **no findings cap / no word cap**. Do not re-litigate taste or ticket AC here.

**BigPicture prompt** — diff + commits; product/domain context from spec if any; require BigPicture artifact shape; holistic coherence + missing sibling seams; **exam posture**; **no findings cap / no word cap**. Do not line-nit hunks.

**Risk prompt** — diff + commits; require Risk artifact shape; hunt security, bugs, scale (Big-O / unbounded / N+1 / hot-path); tag `security|bug|scale` + severity. Every finding must state a reachable trigger, code evidence, impact, smallest fix, and why heavier machinery is or is not needed. Do not report hypothetical missing guards, catches, retries, queues, locks, or error systems. **Exam posture**; **no findings cap / no word cap**. Do not re-litigate taste or ticket AC.

Parent: if any worker returns narrative without its artifact shape → **reject and relaunch** that axis.

## Aggregate (after Wave 1)

Present `## Standards`, `## Spec`, `## Routes`, `## BigPicture`, and `## Risk` separately. One-line summary per axis. Do not pick a cross-axis winner. Under Routes, keep path walks **and** blast radius readable — do not collapse them into a flat severity list only.

Keep Wave 1 axis summaries ready to feed Wave 2 (compact, factual).

## Wave 2 — adversarial (initial review only)

**Always** run after an initial Wave 1 aggregate — even when Wave 1 found many issues. Do not use this broad adversarial scan for a targeted re-review.

Launch **fresh** Task(s) in one message (`generalPurpose` or `explore`). **Omit Task `model`** unless the user asked.

**Input:** fixed-point diff + commits + **Wave 1 axis summaries** (not full chat fluff).

**Job:** prove Wave 1 missed real defects; hunt contradictions between axes; do **not** restate Wave 1 findings unless disagreeing with them.

**Output shape:**

```markdown
## Adversarial findings
- **standards|spec|routes|bigpicture|risk|cross-axis** · **critical|important|nit**: <new issue> @ <file/symbol> — <why Wave 1 missed it>
```

Parent merges unique hits into the five axis sections (or show a short `## Adversarial addenda` then fold into remediation disposition / PR drafts). Drop duplicates of Wave 1.

Same exam posture. Real defects only — invent nothing.

## Targeted re-review

Use this after a Fix mode change. Start with the named `Fix now` rows, their cited `INV-*` rules or acceptance criteria, the fix diff, touched paths, and direct callers.

1. Verify each named finding is actually cleared at its authoritative enforcement point.
2. Re-walk only paths touched by the fix and the direct callers that could regress.
3. Run Risk for correctness/security on that surface; run Standards only for the changed shape when needed.
4. Do not run a fresh BigPicture hunt or broad Wave 2. New optional structural cleanup goes to Follow-up.

Report `cleared | still open | regression | new correctness/security issue` per named row.

## Behavior-lock recommendations (tell the user — do not run)

After Wave 1 + Wave 2 (and Needs `/create-test` if any), if the diff touches a **complex architectural part** whose deep behavior is easy to break from the outside (complex hooks, domain/business logic, facades, stateful classes) and there is **no durable behavior lock**, add a short section:

```markdown
## Needs /create-test
- `path/to/symbol` — <one-line why a lock matters>
```

**Tell the user** to run `/create-test` on those subjects. Do **not** invoke `/create-test` yourself. Do **not** write test files from this skill. Do not recommend locks for trivial wrappers, UI chrome, or coverage theater.

**Who may recommend:** only `/code-review` and `/pr-review`. Other pack skills must not recommend or start `/create-test`.

**Persist follow-ups:** when a goal workspace is in play, resolve `goal_root` per [../pack-shared/workspace-roots.md](../pack-shared/workspace-roots.md), append each Needs `/create-test` row to `<goal-root>/FOLLOWUPS.md` (create if missing), and mirror a one-line pointer in `<goal-root>/STATUS.md`. ACHIEVED **Manual next steps** must list open FOLLOWUPS until the user runs `/create-test` or waives each by name.

Do **not** flag missing eslint/tsc or Convex MCP as Standards failures — CI owns lint/type; `/taste` Verify is **read existing terminals**.

## Remediation disposition (batch ask → analyze → bounded fix)

After an initial review (and Needs `/create-test` if any), classify every actionable finding before offering work:

- **Fix now:** a spec or `INV-*` violation, correctness/security defect, regression, or structural change demonstrably required to clear one of those blockers.
- **Follow-up:** useful architecture, readability, move, or cleanup work that is not required by the current goal. Persist it in `FOLLOWUPS.md` for a goal, or list it clearly for standalone review.
- **Optional nits:** non-blocking small improvements; never enter the default fix offer.

Present a short backlog without re-dumping the review:

```markdown
## Fix backlog

### Fix now
1. **important · risk** — `INV-1`: backend permits X while Y is processing @ `orders.ts` — add the direct transition guard

### Follow-up
- Extract the adjacent formatting helper after this goal; no current rule or defect requires it

### Optional nits
- …
```

Ask only about **Fix now**:

```markdown
## Questions
Reply like: 1a 2b

1. Analyze the named Fix-now backlog before deciding how to fix it?
   - a) yes — inspect each issue and propose the smallest fix ← recommended
   - b) no — leave findings as-is
2. (If Needs /create-test) Run /create-test on the listed subjects after fixes?
   - a) yes — remind me
   - b) no / later
```

On **analysis = no:** stop. Review is done. Do not start coding or `/goal`.

On **analysis = yes:** invoke `/analyze` in **review remediation analysis** mode with the selected Fix-now rows, cited `INV-*`/criteria, review pass, fixed-point diff, and permitted lane. For a goal review, pass `analyses_container: <goal-root>/analyses` and a resolved `analysis_root`; otherwise use the normal analysis root contract. It must write an `ANALYSIS.md` that describes the issue/current behavior, root cause, smallest proposed fix, touch surface, non-goals, and verification for every selected row.

`/analyze` then presents its explicit promotion choice. Only on promotion use the current goal's Fix mode when a goal workspace is active; otherwise create a bounded `/goal`. Its contract is:

| Step | Do |
| --- | --- |
| Goal contract | Goal = clear the selected analysis `FIX-*` rows only; Done when = binary check per row; Context = review + remediation `ANALYSIS.md` + fixed-point diff; Constraints = no new product scope, unrelated cleanup, or architecture work |
| Active Rules | Cite the violated `INV-*` rows; add a row only when the finding reveals a user-locked behavior that was absent from the ledger |
| Grill | Focus only on enforcement, footprint, and observable behavior needed for the named findings; announce non-goals + split + shared understanding |
| Build | Use the smallest authoritative correction; a move is in scope only if the named finding requires it |
| Re-review | `/validate`, then targeted re-review of the named rows, touched paths, direct regressions, correctness, and security |

Do **not** start coding after the review answer. Analyze first, then wait for explicit promotion before a focused grill and implementation. Do not silently pick approaches.

Do not skip review remediation analysis for a tiny defect unless the user explicitly says to skip analysis and `/goal`'s skip-grill rule fully applies.

When Fix now is empty, do not start a loop. Report `_Nothing required for the current goal._` plus any Follow-up items.

## Anti-patterns

- Casual pass / rubber stamp while defects remain that `/pr-review` would Blocking
- Skipping Wave 2 on an initial review or solo-reviewing a large initial diff when five Wave 1 Tasks can run
- Accepting a worker report that skips its artifact shape
- Capping findings or word-limiting workers so defects stay hidden
- Calling a theoretical failure a defect without a reachable trigger, evidence, and material impact
- Recommending defensive `if` blocks, catch wrappers, retries, queues, locks, or error systems without evidence that the smallest authoritative control is insufficient
- Ending the review without a Fix-now backlog + Questions batch when current-goal blockers exist
- Coding fixes after a review answer without review remediation analysis and explicit promotion
- Dripping one review follow-up question per message when several are known
- Treating nits as mandatory backlog items unless the user asked
- Hiding structural debt instead of classifying it as Fix now or Follow-up
- Treating every relocation or cleanup as a mandatory current-goal refactor without evidence that it clears a named blocker
- Running a new thermonuclear architecture hunt during targeted re-review
- Writing to Linear/GitHub from this skill
- Auto-running `/create-test` instead of recommending it
- Writing or editing test files from this skill (only `/create-test` writes tests)
- Auto-launching `bugbot` / `security-review` when the user did not ask (Risk axis covers that)
- Narrating exam roleplay in chat ("I'm the stressed student…") instead of factual findings

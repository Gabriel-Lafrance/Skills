# Review contract

## Job

Review a shipped diff (a local branch or an open GitHub PR) for quality and whether it matches the request. `/review` owns findings and posting; the [active orchestrator](../rules/execution.md#remediation) owns remediation dispatch. There is no Design-review skill and no Design axis.

## Owns

Inputs, modes, the two axes (Standards vs Spec), blocker vs follow-up judgment per principle, naming alignment, folder placement, env-var reuse, static checks, PR extras, evidence bar, finding record, the review output fence, the Correctness hunt, baseline defects, severity mapping, when to recommend a behavior-lock test, and the PR publish decision (Pass A/B, stale-head guard, one-topic comments, one publish question).

## Does not own

- Code quality and structure bars: cite `quality:*` and `structure:*`
- UX rules and `docs/design.md`: [`../rules/user-experience.md`](../rules/user-experience.md) owns them; review applies them within Standards and Spec
- Remediation adjudication, analysis requests, and fix dispatch: [active orchestrator](../rules/execution.md#remediation)
- How an accepted test is written: [`../rules/testing.md`](../rules/testing.md)
- Numbered steps: [`SKILL.md`](SKILL.md); PR drafting, Pass A/B, and posting steps: [`reference.md`](reference.md)

## Inputs

Pin a fixed point and inspect the diff. Spec comes from the current user request, ticket, PR body, committed repository docs, and execution context a parent supplied. Hidden review files are never a source.

### Fresh combined review context

The existing combined-result reviewer starts in fresh context. Give it the pinned base, current revision and working-diff boundary, ticket/spec and acceptance IDs, settled decisions, relevant caller pointers, applicable standards, test consent and safety/permission constraints. Include factual check results with their checked revision and limits. Do not forward the implementation conversation, worker self-review verdicts, or a prewritten conclusion. The reviewer reads the actual diff and callers and forms its own Standards and Spec findings.

This focuses the existing combined review; it adds no reviewer to each slice and does not replace an implementing worker's self-review or the main agent's independent acceptance. Keep essential architecture, acceptance, safety and permission constraints available to implementers. Fresh context is a review boundary, not permission to withhold governing rules from workers.

The reviewer returns findings to the active orchestrator. It gains no write, commit, fix-dispatch or shipping authority. Named remediation findings and their evidence remain valid inputs for a scoped re-review. If fresh context is unavailable, report that limit and follow the selected route's existing fallback without claiming an independent pass ran.

## Modes

| Mode | Scope | Required work |
| --- | --- | --- |
| `initial` | Full shipped diff and available spec | Standards pass + Spec pass |
| `remediation` | Named findings, fix diff, touched paths, direct callers | Verify named findings, regressions, and correctness in the changed code |
| `full-rescan` | Full diff after meaningful change or user request | `initial` depth again; adjudicate prior PR threads when present |

### Follow-up partition (PR)

On a GitHub PR follow-up, after historical Pass A:

1. Partition `previousReviewedHead..currentHead`.
2. Apply `remediation` to the addressed-findings code in that range.
3. Apply `initial` depth to **newly introduced** files/hunks in that range outside the remediation set.
4. Use `full-rescan` only on explicit user request or material scope expansion.

Remediation stays narrow, with no broad architecture hunt. New commits outside the remediation set still get reviewed. Bind finding and acceptance evidence to the reviewed revision and scope under [handoffs and evidence](../rules/execution.md#handoffs-and-evidence). A prior pass does not clear changed behavior or stale verification; report invalidated evidence to the parent, which owns whole-result completeness.

## Bars

Each review key names the section below with the same title (`review:axes`, `review:blocker-vs-follow-up`, `review:naming-alignment`, `review:folder-placement`, `review:env-reuse`, `review:foundation`), except the last four (`review:body-vs-diff`, `review:historical-thread`, `review:migration-backfill`, `review:breaking-public-api`), which are sections of "PR extras".

### Axes

Review along independent axes; present them separately.

- **Standards:** maintainability, architecture, repository conventions, and reachable bugs in the shipped diff (Correctness hunt).
- **Spec:** whether the shipped change satisfies the user request, ticket, PR, and accepted requirements.

UX rules (`ux:*` in [user-experience.md](../rules/user-experience.md)) are Standards for touched user flows; the agreed interaction contract is Spec. Review has no separate Design axis, matrix, or skill.

Use an A+ exam bar: report every evidenced defect on an initial review or full rescan; there is **no findings cap**. Review strictly but factually: assess the diff and reachable behavior, not the author. Thoroughness means stronger path walks and better evidence, and only defects the evidence shows.

Resolve instruction conflicts through the Conflict section of `AGENTS.md`. Review these Standards sources:

1. [code-quality.md](../rules/code-quality.md) (`quality:*` rules)
2. [code-structure.md](../rules/code-structure.md) (`structure:*` rules)
3. Repository rules and committed project documentation (additional constraints)
4. Optional project standards when present (no particular standards file is required)
5. Baseline defects in the review contract
6. For touched user flows, [user-experience.md](../rules/user-experience.md) and the product's `docs/design.md` when present

Treat the first two sources as **hard** unless explicitly overridden by the user. Repository rules cannot weaken them. Redo Standards output that skipped either section.

### Interaction review

For touched user flows, trace the real entry and known context through each changed action to its useful result and continuation. Apply [action and continuation](../rules/user-experience.md#action-and-continuation). Cite concrete redundant effort, required data re-entry, lost edits/state, unprepared continuation, or hierarchy/component reuse violations as defects under the existing finding and severity rules. Distinguish product conventions and accepted tradeoffs from personal aesthetic preferences. A working click or attractive screenshot alone does not prove the flow meets the contract.

Use source and existing evidence for the path walk; cite `/verification` browser and screenshot evidence when available. Missing live evidence remains a named gap, not an invented pass or defect. Review does not start another design workflow or ask backend-only work for UI decisions.

### Blocker vs follow-up

For the shipped diff, check each named principle in [code-quality.md](../rules/code-quality.md#named-principles). Cite the principle as **plain (Classic)** (`keep jobs apart (SoC)`) and the cite key in the finding **Rule** field when violated. Always pair the plain phrase with the classic name. The user-facing sentence must still explain the problem in ordinary words ([Plain language](../rules/writing-style.md#plain-language)).

| Principle | Blocker when | Follow-up when |
| --- | --- | --- |
| **Keep it simple (KISS)** | New ceremony without evidence it is required for Done when / rules that must stay true. A seam (a named extension point where a new variant plugs in) on a named area of modularity is evidence | Slightly overbuilt but still correct |
| **Keep jobs apart (SoC)** | UI/feature owns Stripe, JWT, email, or mixed jobs in one unit | Mild mixing with a clear later split |
| **One altitude (SLAP)** | One function both coordinates and does low-level detail in a way that hides bugs | Long but still readable |
| **Light to read (Minimize reader load)** | New one-caller wrapper that only forwards or renames, pass-through layer, or hidden state a reader must hold to say where a value comes from | Evidenced reader burden outside the required change; a useful behavior-owning collaborator alone is no finding |
| **Read or write, not both (CQS)** | A read also writes, or a command hides writes behind a "get" | Mild naming oddity on an otherwise correct command/query |
| **Fail fast (Fail Fast)** | Invalid input accepted past the boundary into partial side effects, or a re-check inside after the boundary already parsed | Late check that still prevents bad writes |
| **Leave it cleaner (Boy Scout Rule)** | Diff copies or extends a known-wrong shape in the touched area | Cleanup opportunity not required for this change |
| **Subtract first (Subtract before you add)** | The diff adds a path beside code this change should have deleted, or leaves a stub with no new content | Dead code outside the path this change extends |
| **Related together (Cohesion / Law of Demeter)** | Callers reach service internals; unrelated jobs jammed into one module | Coupling that works but should tighten |
| **Safe to retry (Idempotency)** | Replay, double-submit, or a resume after a crash can duplicate charges, rows, or side effects, or the end state depends on leftover partial state | Missing key where risk is low |
| **Say what happens (explicit over implicit)** | Hidden globals, surprise side effects, or control flow a reader cannot see | Minor magic with local clarity |
| **No surprises (PoLA)** | Surprising API/UI behavior vs name or docs | Slightly awkward but documented behavior |
| **Honest names (intention-revealing names)** | Diff changes the job but leaves a stale **file path**, **export**, **type**, or **widely used symbol** | Local helper mildly stale but still navigable |
| **Trust the server (never trust the client)** | Public write trusts the client or a UI-only guard; identity or ownership missing | Extra client check that duplicates a real server lock |
| **Types tell the truth (make illegal states unrepresentable)** | New public surface uses `any`, skips validators, marks required data optional, allows a contradictory field bag, mixes branded ids, casts to silence the checker, or matches a variant in a way that still compiles when a case is added | Local private helper loosely typed but not on a boundary |

Treat a concrete hard-standard or named-principle violation introduced or extended in the touched area as a blocker candidate (especially `quality:fail-fast`, `quality:safe-to-retry`, `quality:trust-the-server`, `quality:related-together` through internals, `quality:honest-names` after a rename, and `quality:types-tell-the-truth` on a public surface). A useful cleanup remains a **Follow-up**. That changes only when it violates the spec or a rule that must stay true, causes a correctness or security defect, regresses behavior, or is necessary to clear a named finding. A public write without identity or ownership is a blocker candidate, not a nit.

Prefer a direct guard at the state-owning boundary over extra coordination. Request an `if` only for a reachable invalid state or a missing authoritative invariant. Request `try/catch` only where it recovers, translates, adds actionable context, or cleans up. Request retries only for an evidenced transient external failure with an idempotent, bounded operation. Request queues, locks, or other coordination only when evidence shows a direct authority cannot preserve the needed behavior. Report a failure only with evidence, not because it "might fail someday".

### Naming alignment

On every `initial` or `full-rescan` Standards pass, after the principles checklist, walk the shipped diff for **stale names after rename/scope change**:

1. **File paths:** if responsibility moved (new domain word in symbols, comments, ticket, or hunks), the filename/folder must match (rename `checkout-total.ts` once it owns payment-intent logic).
2. **Exports and primary symbols:** exported functions, classes, types, React components, and Convex handlers must match the current job; rename in the same change as the scope shift.
3. **Call sites and variables:** update imports, identifiers, and locals that still describe the old concept when the touched area changed meaning.
4. **Half-moves:** a move/rename that updates content but keeps the old path (or the reverse) is a defect, not a style preference.

Cite `quality:honest-names` on findings. Naming alignment is part of the Standards pass, not a later pass. Remediation of an honest-names finding must clear the path **and** the symbols in the named surface, not only one of them.

### Folder placement

On every `initial` or `full-rescan` Standards pass, walk **new files** against `structure:folders` and introduced responsibilities in **changed existing files** against [responsibility boundaries](../rules/code-structure.md#responsibility-boundaries):

1. Related new files must sit in a named owning folder, not as mixed siblings of unrelated code in `src/`, `app/`, `convex/`, or a route folder that already holds a different slice.
2. A new concern gets a folder even for the first file, before five siblings exist.
3. Reject `quality:never-nest` and `quality:keep-it-simple` as defenses. Never-nest is control flow.
4. Pre-existing mixed siblings left untouched are Follow-up unless the goal or a named finding requires a move (`structure:prior-mistakes`).

Check whether the diff appends an independent job to an existing owner or
fragments cohesive work into shallow files. Name the actual responsibility,
dependencies, and caller burden. Apply the retrieval/change-locality check;
do not fail a cohesive file on length or export count alone. Meaningful private
single-consumer collaborators and cohesive/framework exports follow the
canonical rules. Routine placement does not require another interview.

Cite `structure:folders` for placement and `structure:responsibility-boundaries` for incoherent jobs or shallow fragmentation. A shipped-diff folder-map miss is **Fix now**. Relocating untouched old flats is Follow-up unless required.

### Env reuse

On every `initial` or `full-rescan` Standards pass, walk **new environment variables** in the shipped diff against `quality:reuse-env`:

1. Inventory names already in `.env.example`, committed `.env*` templates, and `process.env` / `import.meta.env` usages in the repo (and the platform env list when the diff sets dashboard/CLI vars).
2. A new name whose **job or value** an existing var already holds (`FRONTEND_URL` while `SITE_URL` exists) is a finding. Cite `quality:reuse-env`.
3. Mapping in code from the existing name is correct. Duplicating the value under a synonym is not. A required platform prefix must use the existing name (`NEXT_PUBLIC_SITE_URL`), not a third synonym.

A shipped-diff synonym is **Fix now**. Untouched historical aliases left in files the diff did not add are Follow-up unless the goal or a named finding requires a move.

### Foundation

On every `initial` or `full-rescan` Standards pass on a Feature diff, check it against `quality:strong-foundation` ([strong-foundation.md](../rules/strong-foundation.md)):

1. Take the areas of modularity from the spec: the ticket's `## Foundation`, `## Areas of modularity`, or settled decisions, the Structure card, or the grill's Locked in message.
2. An area the spec named that ships hardcoded (no seam, the first provider inlined at callers, an `if` or `switch` on the variant) is a **blocker**.
3. A seam on an area nobody named is a keep it simple (KISS) finding, not foundation.
4. An obvious area nobody named (a domain that usually multiplies, a second variant already in the repo) is a **follow-up** note that asks whether it should have been named. It never blocks.
5. A diff that extends an existing seam must add a collaborator and its registration, not a special case in the foundation.

Cite `quality:strong-foundation`. A Tweak, Bug, or Chore diff with no named area skips this check.

### Test claim review

When changed tests or existing tests support an important acceptance claim, apply the mandatory [No tautological tests](../rules/testing.md#no-tautological-tests) rule, [authoring gate](../rules/testing.md#authoring-gate), [junk patterns](../rules/testing.md#junk-patterns), and [retention bar](../rules/testing.md#retention-bar). For each such claim, inspect the real public entry and assertion: what plausible wrong behavior would fail this test, do its mocks suppress the relevant failure modes, and would a behavior-preserving refactor survive? Trace setup, dependencies and assertions instead of treating a green result as proof. Record the concrete answer and evidence limit in the relevant Spec matrix row; use the existing finding record for a defect.

Judge mocks by which behavior they remove from observation, including policy, ordering, persistence and failures the owner must handle. A mock at a true external boundary can still hide the claimed behavior. Recommend the smallest correction at its owning boundary under the [test consent rules](../rules/no-unrequested-tests.md); review grants no permission to add a test, change an accepted assertion or delete an existing contract test. An unrun check or insufficient artifact is an evidence gap, not an invented defect. See the [mock example](examples.md#green-test-with-a-hidden-failure).

### Static checks

On `initial` or `full-rescan`, assess dead code and the complexity cap on the changed surface and affected callers. Select existing static commands under [verification scope](../rules/execution.md#verification-scope); reuse valid evidence and run broad Knip only when required or justified by reachability/dependency changes. A local behavior fix need not install a checker or scan the whole repository. See [static-checks.md](static-checks.md), cite `quality:no-dead-code` and `quality:cyclomatic-cap`, and report evidence limits. Introduced defects are **Fix now**; untouched baseline defects are Follow-up. Operational Git sync does not automatically start this review.

### PR extras

On a GitHub PR, the shared hunt already covers secrets. The review **must** also inspect:

| Extra | Blocker when | Otherwise |
| --- | --- | --- |
| **Body vs diff** | Done-when in the PR/ticket is unmet, or the diff ships extra product scope the body does not mention | Small leftover comment or typo |
| **Historical thread** | A prior Blocking thread is still broken on `currentHead` | Thread is fixed or genuinely moot (Pass A) |
| **Migration / backfill** | Schema or data change with no path for existing rows, or dual-write skipped when reads would break | Additive nullable field with a safe default |
| **Breaking public API** | Exported contract changes with no call-site update and no mention in the PR | Internal rename with callers updated |
| **How to QA** | Chat note only: if claimed behavior cannot be checked from the PR body and the diff is user-facing, say so in chat | Never a blocker |

Add the first four rows to the PR extras table in the [review output](#review-output) fence. How to QA is that chat note, not a hunt-table row.

## Review budget

Repeated review/remediation uses a default budget of **three review rounds**
per outcome. Count the initial review and each remediation or full-rescan as
a round; parallel Standards/Spec passes for the same pinned result are one
round. Carry consumed rounds through handoffs/resume and nested skill changes.
Transport retries of the same request do not buy another completed round, but
must be bounded; errors/timeouts never count as a successful review.

The active owner keeps stable finding IDs, evidence, disposition, correction
and remaining disagreement in the existing chat backlog. Reuse valid evidence
under [handoffs and evidence](../rules/execution.md#handoffs-and-evidence).
After fixes, review named findings and direct regressions; inspect newly
introduced surface under [follow-up partition](#follow-up-partition-pr).
Do not restart a broad hunt for each small correction or add duplicate reviewers.

Stop when applicable required findings and acceptance checks are satisfied,
when only optional nits remain, when progress stalls on an evidenced dispute,
or when the budget ends. A nit is a non-material preference without a violated
requirement. Reachable security, data-loss or other material correctness bugs
remain findings even when rare. Rarity alone never makes a defect a nit.
Do not waive hard standards or required fixes merely to finish the loop.

For unresolved high-risk work, the owner may extend once, by **at most two
additional rounds**, with a stated risk, new evidence or specific correction
to verify, and a finite stop condition. A user's explicit smaller/hard cap
wins; extending it requires that user's decision. Routine nits, repeated
unchanged objections, and a desire for approval do not justify extension.
At exhaustion, stalled dispute, or blocked authority, report rounds used,
unresolved IDs and evidence, competing reasoning, missing checks and the next
decision. Never manufacture approval or call required findings resolved.

This budget applies to `/review-loop` and repeated build remediation. It adds
no loop to a standalone review, changes no route's gate order, and grants no
fix, comment, push or merge authority. `/review` returns findings; the one
[active orchestrator](../rules/execution.md#remediation) owns correction.

## Evidence bar

A blocker about a runtime failure, guard, concurrency, error path, retry, queue, lock, or hardening need requires all of:

1. A reachable trigger.
2. Concrete evidence: the diff, a path walk, a violated rule, a signal, or a directly provable exploit.
3. Material correctness, security, data, availability, or acceptance impact.
4. The smallest authoritative fix.

These **are** reachable triggers, not theory:

- A public write touching user data with no identity check
- A patch/delete/read of another row with no ownership or tenant check
- A UI-only guard (disabled button, hidden route, client `if`) while the public write still runs
- A webhook, payment, or insert that can duplicate on replay
- `Date.now()` / randomness inside a query
- An un-awaited write (`ctx.db.patch` / `insert` / `scheduler.runAfter` without `await`)
- Unbounded `collect()` or `.filter` scan on a growing table
- A `catch` that swallows or logs-and-continues at a boundary that should fail
- A secret, token, or private key in the shipped diff

Report only evidenced failures, and recommend coordination machinery only with evidence that a direct guard is insufficient.

## Finding record

Stable id grammar: `axis-rule-location` (example: `standards-never-nest-checkout-place-order`).

```markdown
- **<id>** · **standards|spec|cross** · **blocker|follow-up|nit**
  - **Where:** `path` (symbol or line)
  - **Rule:** Rule N | Done when item | doctrine | none
  - **Trigger:** <required for runtime-risk findings>
  - **Evidence:** <hunk, path walk, or signal>
  - **Impact:** <why it matters>
  - **Fix:** <smallest authoritative direction>
```

Fold sites with the same root cause and fix shape into one record; different root causes get separate records. Drop duplicates by id. On a PR, the final comment carries `**Finding:** \`<id>\``; the GitHub thread and that id are the durable record.

## Output

**Standards pass** (`initial` / `full-rescan`): apply [code-quality.md](../rules/code-quality.md) and [code-structure.md](../rules/code-structure.md) this turn. Scope static checks under [static-checks.md](static-checks.md). Inspect the relevant Principles, naming, Architecture, Correctness, and Baseline concerns across the changed surface and affected consumers. A small diff does not excuse missing a consequential authorization or data-integrity concern.

Cite principles as **plain (Classic)** (`keep jobs apart (SoC)`) in notes and in the finding **Rule** field, always with both names. User-facing notes are ordinary sentences ([Plain language](../rules/writing-style.md#plain-language)).

**Spec pass**: cover each Done-when item, rule that must stay true, user-visible state the diff touches (enabled, disabled, loading, empty, error), and named unchanged behavior. Use one Spec matrix row per item in the full output, or equivalent concise evidence in focused output. With no spec, say so and add no rows; Standards still runs the Correctness hunt.

Cover every independent part of the diff. For focused low-risk work, report scope, findings, relevant checks, and evidence limits concisely; do not manufacture empty tables. Substantial/high-risk work or an explicitly requested full review uses the output below. Mark each row `clear`, `finding` (with id), or `none` when the check has nothing to inspect. One pass: no second adversarial pass, no hunt re-inspect. Secrets stay in the Correctness hunt, not PR extras.

Return the [review output](#review-output) fence, including the four PR extras rows on a GitHub PR. Use the shared finding record; IDs remain stable across follow-up discussion. Map shared severity with the contract table, without re-explaining it.

**Local branch diff:** show Fix now, Follow-up, and Optional nit in chat after an initial review or full rescan. A user can explicitly waive a named finding in chat; that is a decision, not proof that the issue is fixed.

**GitHub PR:** show every full new draft in chat before posting, then ask exactly one publish question for the batch. With no drafts and no unresolved blocker, ask once whether to approve. A `blocker` becomes **Blocking**; a `follow-up` or `nit` becomes **Nit** only when a public comment is useful, otherwise it stays in chat. Public comment severities are **Blocking** and **Nit** only. Post findings only, one comment per root-cause topic, with no summary, announcement, index, or pass-status comment. On a follow-up, Pass A precedes new review work, then Pass B; the stale-head guard runs before any publish. Steps and comment shape: [reference.md](reference.md).

### Review output

```markdown
## Standards findings
- <finding record>

## Principles sweep
| Principle | Status | Note |
| --- | --- | --- |
| Keep it simple (KISS) | clear \| finding | … |
| Keep jobs apart (SoC) | clear \| finding | … |
| One altitude (SLAP) | clear \| finding | … |
| Light to read (Minimize reader load) | clear \| finding | … |
| Read or write, not both (CQS) | clear \| finding | … |
| Fail fast (Fail Fast) | clear \| finding | … |
| Leave it cleaner (Boy Scout Rule) | clear \| finding | … |
| Subtract first (Subtract before you add) | clear \| finding | … |
| Related together (Cohesion / Law of Demeter) | clear \| finding | … |
| Safe to retry (Idempotency) | clear \| finding \| none | … |
| Say what happens (explicit over implicit) | clear \| finding | … |
| No surprises (PoLA) | clear \| finding | … |
| Honest names (intention-revealing names) | clear \| finding | … |
| Trust the server (never trust the client) | clear \| finding \| none | … |
| Types tell the truth (make illegal states unrepresentable) | clear \| finding \| none | … |
| Don't repeat yourself (DRY) | clear \| finding \| none | … |

## Architecture sweep
| Check | Status | Note |
| --- | --- | --- |
| Services / public API | clear \| finding \| none | … |
| Simple public surface | clear \| finding \| none | … |
| One-job helpers (reuse, not copy) | clear \| finding \| none | … |
| Env var reuse (no synonym) | clear \| finding \| none | … |
| Folders / placement | clear \| finding \| none | … |
| Cheap reads (store on write) | clear \| finding \| none | … |
| Indexes / no scan | clear \| finding \| none | … |
| Pagination / no unbounded collect | clear \| finding \| none | … |
| Deterministic queries | clear \| finding \| none | … |
| Authority on the write | clear \| finding \| none | … |
| Safe to retry writes | clear \| finding \| none | … |
| Prior mistakes not copied | clear \| finding \| none | … |

## Correctness hunt
| Class | Status | Note |
| --- | --- | --- |
| Identity on public writes | clear \| finding \| none | … |
| Ownership / tenant | clear \| finding \| none | … |
| Client-only guard | clear \| finding \| none | … |
| Replay / double-submit | clear \| finding \| none | … |
| Race / lost update | clear \| finding \| none | … |
| Un-awaited write | clear \| finding \| none | … |
| Swallowed error | clear \| finding \| none | … |
| Null / empty / off-by-one on the happy path | clear \| finding \| none | … |
| Cross-file stale caller | clear \| finding \| none | … |
| Secrets in the diff | clear \| finding \| none | … |

## Spec matrix
| Requirement | Status | Evidence |
| --- | --- | --- |
| <Done when / rule / state / unchanged> | met \| gap \| none | … |

## PR extras (GitHub PR only)
| Extra | Status | Note |
| --- | --- | --- |
| Body vs diff | clear \| finding \| none | … |
| Historical thread | clear \| finding \| none | … |
| Migration / backfill | clear \| finding \| none | … |
| Breaking public API | clear \| finding \| none | … |
```

### Baseline defects (Standards, after the tables)

Each of these in the shipped diff is a finding, cited by key and spoken **plain (Classic)**. Identity on public writes and clock/randomness in queries are covered by the Correctness hunt and Architecture sweep above.

| Defect | Key |
| --- | --- |
| Nested control-flow pyramids | `quality:never-nest` |
| New related files as mixed siblings with no owning folder | `structure:folders` |
| A function with more than six independent paths (cyclomatic complexity (McCabe)) | `quality:cyclomatic-cap` |
| Copy-paste twin of a concept already in the repo | `quality:dont-repeat-yourself` |
| New env var whose job an existing var does (`FRONTEND_URL` while `SITE_URL` exists) | `quality:reuse-env` |
| `{ success: false }` / Result bags for expected failure (fail fast (Fail Fast)) | `quality:throw-at-boundaries` |
| `any` or Convex `v.any` on a public surface | types tell the truth (make illegal states unrepresentable) |
| Unused files, exports, or dependencies in the diff | `quality:no-dead-code` |
| Dynamic `import()` | `quality:static-imports` |
| Unrelated exported responsibilities sharing a changed file, excluding cohesive public operations/types and framework-required exports | `quality:one-export-per-file` ([cohesive exports](../rules/code-quality.md#cohesive-exports)) |
| Class or interface chain deeper than two | `quality:oop-depth-cap` |
| Magic policy number at a call site that should be a named invariant | `quality:keep-it-simple` |

## Severity mapping

| Canonical severity | Local branch | GitHub PR |
| --- | --- | --- |
| `blocker` | Fix now | `Blocking` |
| `follow-up` | Follow-up | Chat-only by default; `Nit` only when a PR comment is useful |
| `nit` | Optional nit | `Nit` only when useful |

Severity has only these three levels, with no `important` middle. A GitHub PR review posts only `Blocking` or `Nit`. Adapters use this map without re-explaining it.

## Behavior-lock recommendation

After an `initial` or `full-rescan` review, recommend a behavior-lock test only for a complex architectural boundary with externally observable behavior and no durable lock (authorization, ownership, safe-to-retry writes). Tell the user, and write no tests. If the user says yes, the test is written by following [testing.md](../rules/testing.md). Skip a claim the user accepted or refused in the current `/task` lock batch, unless the shipped public contract differs from that brief.

## Apply

After an initial review or full rescan, recommend a behavior-lock test only per the [review contract](#behavior-lock-recommendation) rule. Tell the user why the lock matters. Skip a claim the user already accepted or refused in the current `/task` lock batch, unless the shipped public contract differs from that brief. This skill recommends only; if the user says yes, the test is written by following [testing.md](../rules/testing.md).

For UI changes, apply [React and UI](../rules/user-experience.md#react-and-ui) and `docs/design.md` (`ux:source-of-truth`). Judge UI from the diff and existing terminal/test output. Running the app, a browser, or screenshots is [`/verification`](../verification/SKILL.md); when its handoff exists, cite its evidence in Spec matrix rows.

**Local branch diff:**

- Remediation stays narrow: it is not a broad architecture hunt and does not reopen the full initial review. Upgrade it to a full rescan only on an explicit request or material scope expansion.
- Return findings to the [active orchestrator](../rules/execution.md#remediation), which owns adjudication, any bounded analysis, and fix dispatch. Review never promotes or dispatches fixes. A standalone review stops unless fixes were requested; then hand off explicitly under [SKILL.md](SKILL.md#if-this-is-a-user-one-off).
- If Fix now is empty, end the review without starting a fix loop. Do not write external tracker or PR updates in this mode.

**GitHub PR:**

- This mode is a user start, outside `/task`. After publishing, start a local fix or `/task` lifecycle only when the user asks.
- Review is stateless. Re-run the shared hunts on the GitHub diff even when a local review already judged the branch.
- Durable specification sources are the PR title/body, linked ticket, and user-approved committed repository documentation. Follow the shared [execution context](../rules/planning.md#execution-context): rediscover facts from the PR and repository instead of depending on local `/task`, workspace, cache, temp, registry, or review-snapshot artifacts.
- A linked GitHub issue or Linear ticket is **read-only** context. Post only on the PR, never on the ticket or Linear.
- Use the harness pull-request / GitHub tool for GitHub reads and writes when the harness has one; otherwise use `gh` or `gh api`.
- Prepare and publish the review from chat and tool calls alone, with no helper scripts or repository files.
- Keep the shared finding ID internally and reuse the matching GitHub thread for an existing issue, instead of duplicating an open finding as a new comment.

## Anti-patterns

- Skipping the Spec pass, Pass A, or new-surface review because the Standards pass looked clean
- Treating Follow-ups or Optional nits as default fix scope
- Adding a second adversarial review or hunt re-inspect after the Standards and Spec passes

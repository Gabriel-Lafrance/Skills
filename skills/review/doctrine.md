# Review doctrine

## Job

Review a shipped diff (a local branch or an open GitHub PR) for quality and whether it matches the request.

## Owns

Two axes (Standards vs Spec), blocker vs follow-up judgment per principle, naming alignment, folder placement, env-var reuse, static checks, PR extras, the PR publish decision (Pass A/B, stale-head guard, one-topic comments, one publish question).

## Does not own

- Evidence bar, modes, finding record, review output fence, severity map: [`contract.md`](contract.md)
- Code quality and structure bars: cite `quality:*` and `structure:*`
- UX rules and `docs/design.md`: [`../rules/user-experience.md`](../rules/user-experience.md) (applied while building, not as a review axis)
- Remediation adjudication, analysis requests, and fix dispatch: [active orchestrator](../rules/execution.md#remediation)
- Test writing: [`../rules/testing.md`](../rules/testing.md)
- Numbered steps: [`SKILL.md`](SKILL.md); PR drafting, follow-up passes, and posting steps: [`reference.md`](reference.md)

## Bars

Each review key names the section below with the same title (`review:axes`, `review:blocker-vs-follow-up`, `review:naming-alignment`, `review:folder-placement`, `review:env-reuse`, `review:foundation`), except the last four (`review:body-vs-diff`, `review:historical-thread`, `review:migration-backfill`, `review:breaking-public-api`), which are sections of "PR extras".

### Axes

Review along independent axes; present them separately.

- **Standards:** maintainability, architecture, repository conventions, and reachable bugs in the shipped diff (Correctness hunt).
- **Spec:** whether the shipped change satisfies the user request, ticket, PR, and accepted requirements.

UX rules (`ux:*` in [user-experience.md](../rules/user-experience.md)) apply while building; review has no Design axis, Design matrix, Experience floor, Craft floor, or `/design-review` skill.

Use an A+ exam bar: report every evidenced defect on an initial review or full rescan; there is **no findings cap**. Review strictly but factually: assess the diff and reachable behavior, not the author. Thoroughness means stronger path walks and better evidence, and only defects the evidence shows.

Resolve instruction conflicts through [AGENTS.md](../../AGENTS.md#conflict). Review these Standards sources:

1. [code-quality.md](../rules/code-quality.md) (`quality:*` rules)
2. [code-structure.md](../rules/code-structure.md) (`structure:*` rules)
3. Repository rules and committed project documentation (additional constraints)
4. Optional project standards when present (no particular standards file is required)
5. Baseline defects in the review contract

Treat the first two sources as **hard** unless explicitly overridden by the user. Repository rules cannot weaken them. Redo Standards output that skipped either section.

### Blocker vs follow-up

For the shipped diff, check each named principle in [code-quality.md](../rules/code-quality.md#named-principles). Cite the principle as **plain (Classic)** (`keep jobs apart (SoC)`) and the cite key in the finding **Rule** field when violated. Always pair the plain phrase with the classic name. The user-facing sentence must still explain the problem in ordinary words ([Plain language](../rules/writing-style.md#plain-language)).

| Principle | Blocker when | Follow-up when |
| --- | --- | --- |
| **Keep it simple (KISS)** | New ceremony without evidence it is required for Done when / rules that must stay true. A seam (a named extension point where a new variant plugs in) on a named area of modularity is evidence | Slightly overbuilt but still correct |
| **Keep jobs apart (SoC)** | UI/feature owns Stripe, JWT, email, or mixed jobs in one unit | Mild mixing with a clear later split |
| **One altitude (SLAP)** | One function both coordinates and does low-level detail in a way that hides bugs | Long but still readable |
| **Light to read (Minimize reader load)** | New one-caller wrapper, pass-through layer, or hidden state a reader must hold to say where a value comes from | A deep entry that hides real work |
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

On every `initial` or `full-rescan` Standards pass, walk **new files** in the shipped diff against `structure:folders`:

1. Related new files must sit in a named owning folder, not as mixed siblings of unrelated code in `src/`, `app/`, `convex/`, or a route folder that already holds a different slice.
2. A new concern gets a folder even for the first file, before five siblings exist.
3. Reject `quality:never-nest` and `quality:keep-it-simple` as defenses. Never-nest is control flow.
4. Pre-existing mixed siblings left untouched are Follow-up unless the goal or a named finding requires a move (`structure:prior-mistakes`).

Cite `structure:folders`. A shipped-diff folder-map miss is **Fix now**. Relocating untouched old flats is Follow-up unless required.

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

When changed tests or existing tests support an important acceptance claim, apply the [authoring gate](../rules/testing.md#authoring-gate), [junk patterns](../rules/testing.md#junk-patterns), and [retention bar](../rules/testing.md#retention-bar). For each such claim, inspect the real public entry and assertion: what plausible wrong behavior would fail this test, do its mocks suppress the relevant failure modes, and would a behavior-preserving refactor survive? Trace setup, dependencies and assertions instead of treating a green result as proof. Record the concrete answer and evidence limit in the relevant Spec matrix row; use the existing finding record for a defect.

Judge mocks by which behavior they remove from observation, including policy, ordering, persistence and failures the owner must handle. A mock at a true external boundary can still hide the claimed behavior. Recommend the smallest correction at its owning boundary under the [test consent rules](../rules/no-unrequested-tests.md); review grants no permission to add a test, change an accepted assertion or delete an existing contract test. An unrun check or insufficient artifact is an evidence gap, not an invented defect. See the [mock example](examples.md#green-test-with-a-hidden-failure).

### Static checks

On every `initial` or `full-rescan` Standards pass, make sure Knip is clean (no unused files, exports, or dependencies) and no function has cyclomatic complexity above 5. If you do not know how to check those, see [static-checks.md](static-checks.md). Cite `quality:no-dead-code` and `quality:cyclomatic-cap`. A finding the diff introduced is **Fix now**; a pre-existing one is Follow-up.

### PR extras

On a GitHub PR, the shared hunt already covers secrets. The review **must** also inspect:

| Extra | Blocker when | Otherwise |
| --- | --- | --- |
| **Body vs diff** | Done-when in the PR/ticket is unmet, or the diff ships extra product scope the body does not mention | Small leftover comment or typo |
| **Historical thread** | A prior Blocking thread is still broken on `currentHead` | Thread is fixed or genuinely moot (Pass A) |
| **Migration / backfill** | Schema or data change with no path for existing rows, or dual-write skipped when reads would break | Additive nullable field with a safe default |
| **Breaking public API** | Exported contract changes with no call-site update and no mention in the PR | Internal rename with callers updated |
| **How to QA** | Chat note only: if claimed behavior cannot be checked from the PR body and the diff is user-facing, say so in chat | Never a blocker |

Add the first four rows to the review output fence on a PR (review contract PR extras table). How to QA is that chat note, not a hunt-table row.

## Output

Return the review output fence from the [review contract](contract.md#output), including the four PR extras rows on a GitHub PR. Use the shared finding record; IDs remain stable across follow-up discussion. Map shared severity with the contract table, without re-explaining it.

**Local branch diff:** show Fix now, Follow-up, and Optional nit in chat after an initial review or full rescan. A user can explicitly waive a named finding in chat; that is a decision, not proof that the issue is fixed.

**GitHub PR:** show every full new draft in chat before posting, then ask exactly one publish question for the batch. With no drafts and no unresolved blocker, ask once whether to approve. A `blocker` becomes **Blocking**; a `follow-up` or `nit` becomes **Nit** only when a public comment is useful, otherwise it stays in chat. Public comment severities are **Blocking** and **Nit** only. Post findings only, one comment per root-cause topic, with no summary, announcement, index, or pass-status comment. On a follow-up, Pass A precedes new review work, then Pass B; the stale-head guard runs before any publish. Steps and comment shape: [reference.md](reference.md).

## Apply

After an initial review or full rescan, recommend a behavior-lock test only per the [review contract](contract.md#behavior-lock-recommendation) rule. Tell the user why the lock matters. Skip a claim the user already accepted or refused in the current `/task` lock batch, unless the shipped public contract differs from that brief. This skill recommends only; if the user says yes, the test is written by following [testing.md](../rules/testing.md).

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

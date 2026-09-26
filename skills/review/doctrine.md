# Review doctrine

## Job

Review a shipped diff (a local branch or an open GitHub PR) for quality and whether it matches the request.

## Owns

Two axes (Standards vs Spec), blocker vs follow-up judgment per principle, naming alignment, folder placement, env-var reuse, static checks, PR extras, the local remediation/promotion boundary, and the PR publish decision (Pass A/B, stale-head guard, one-topic comments, one publish question).

## Does not own

- Evidence bar, modes, finding record, review output fence, severity map: [`contract.md`](contract.md)
- Code quality and structure bars: cite `quality:*` and `structure:*`
- UX rules and `docs/design.md`: [`../rules/user-experience.md`](../rules/user-experience.md) (applied while building, not as a review axis)
- Fix-now remediation analysis: [`../analyze/doctrine.md`](../analyze/doctrine.md)
- Test writing: [`../rules/testing.md`](../rules/testing.md)
- Numbered steps: [`SKILL.md`](SKILL.md); PR drafting, follow-up passes, and posting steps: [`reference.md`](reference.md)

## Cite keys

| Key | Heading |
| --- | --- |
| `review:axes` | Axes |
| `review:blocker-vs-follow-up` | Blocker vs follow-up |
| `review:naming-alignment` | Naming alignment |
| `review:folder-placement` | Folder placement |
| `review:env-reuse` | Env reuse |
| `review:body-vs-diff` | PR extras |
| `review:historical-thread` | PR extras |
| `review:migration-backfill` | PR extras |
| `review:breaking-public-api` | PR extras |

## Bars

### Axes

Review along independent axes; present them separately.

- **Standards:** maintainability, architecture, repository conventions, and reachable bugs in the shipped diff (Correctness hunt).
- **Spec:** whether the shipped change satisfies the user request, ticket, PR, and accepted requirements.

UX rules (`ux:*` in [user-experience.md](../rules/user-experience.md)) apply while building. Do not add a Design axis, Design matrix, Experience floor, Craft floor, or `/design-review` skill.

Use an A+ exam bar: report every evidenced defect on an initial review or full rescan; there is **no findings cap**. Review strictly but factually: assess the diff and reachable behavior, not the author. Thoroughness means stronger path walks and better evidence, never hypothetical failures or a defect manufactured to look thorough.

Resolve Standards in this order:

1. [code-quality.md](../rules/code-quality.md) (Cite keys)
2. [code-structure.md](../rules/code-structure.md) (Cite keys)
3. Repository rules and committed project documentation (these win on conflict)
4. Optional project standards when present; do not require a particular standards file
5. Baseline defects in the review contract

Treat the first two sources as **hard** unless repository rules conflict. Reject Standards output that skipped either section.

### Blocker vs follow-up

For the shipped diff, check each named principle in [code-quality.md](../rules/code-quality.md#named-principles). Cite the principle as **plain (Classic)** (`keep jobs apart (SoC)`) and the cite key in the finding **Rule** field when violated. Never acronym-only and never the paraphrase without the classic name. The user-facing sentence must still explain the problem in ordinary words ([Plain language](../rules/writing-style.md#plain-language)).

| Principle | Blocker when | Follow-up when |
| --- | --- | --- |
| **Keep it simple (KISS)** | New ceremony without evidence it is required for Done when / rules that must stay true | Slightly overbuilt but still correct |
| **Keep jobs apart (SoC)** | UI/feature owns Stripe, JWT, email, or mixed jobs in one unit | Mild mixing with a clear later split |
| **One altitude (SLAP)** | One function both coordinates and does low-level detail in a way that hides bugs | Long but still readable |
| **Read or write, not both (CQS)** | A read also writes, or a command hides writes behind a "get" | Mild naming oddity on an otherwise correct command/query |
| **Fail fast (Fail Fast)** | Invalid input accepted past the boundary into partial side effects | Late check that still prevents bad writes |
| **Leave it cleaner (Boy Scout Rule)** | Diff copies or extends a known-wrong shape in the touched lane | Cleanup opportunity not required for this change |
| **Related together (Cohesion / Law of Demeter)** | Callers reach service internals; unrelated jobs jammed into one module | Coupling that works but should tighten |
| **Safe to retry (Idempotency)** | Replay/double-submit can duplicate charges, rows, or side effects | Missing key where risk is low |
| **Say what happens (explicit over implicit)** | Hidden globals, surprise side effects, or control flow a reader cannot see | Minor magic with local clarity |
| **No surprises (PoLA)** | Surprising API/UI behavior vs name or docs | Slightly awkward but documented behavior |
| **Honest names (intention-revealing names)** | Diff changes the job but leaves a stale **file path**, **export**, **type**, or **widely used symbol** | Local helper mildly stale but still navigable |
| **Trust the server (never trust the client)** | Public write trusts the client or a UI-only guard; identity or ownership missing | Extra client check that duplicates a real server lock |
| **Types tell the truth (make illegal states unrepresentable)** | New public surface uses `any`, skips validators, or marks required data optional | Local private helper loosely typed but not on a boundary |

Treat a concrete hard-standard or named-principle violation introduced or extended in the touched lane as a blocker candidate (especially `quality:fail-fast`, `quality:safe-to-retry`, `quality:trust-the-server`, `quality:related-together` through internals, `quality:honest-names` after a rename, and `quality:types-tell-the-truth` on a public surface). A useful cleanup remains a **Follow-up** unless it violates the spec or a rule that must stay true, causes a correctness or security defect, regresses behavior, or is necessary to clear a named finding. A public write without identity or ownership is a blocker candidate, not a nit.

Prefer a direct guard at the state-owning boundary over extra coordination. Request an `if` only for a reachable invalid state or a missing authoritative invariant. Request `try/catch` only where it recovers, translates, adds actionable context, or cleans up. Request retries only for an evidenced transient external failure with an idempotent, bounded operation. Request queues, locks, or other coordination only when evidence shows a direct authority cannot preserve the needed behavior. Do not turn "might fail someday" into a finding.

### Naming alignment

On every `initial` or `full-rescan` Standards pass, after the principles checklist, walk the shipped diff for **stale names after rename/scope change**:

1. **File paths:** if responsibility moved (new domain word in symbols, comments, ticket, or hunks), the filename/folder must match; do not leave `checkout-total.ts` owning payment-intent logic.
2. **Exports and primary symbols:** exported functions, classes, types, React components, and Convex handlers must match the current job; rename in the same change as the scope shift.
3. **Call sites and variables:** update imports, identifiers, and locals that still describe the old concept when the touched lane changed meaning.
4. **Half-moves:** a move/rename that updates content but keeps the old path (or the reverse) is a defect, not a style preference.

Cite `quality:honest-names` on findings. Naming alignment is part of the Standards pass, not a later pass. Remediation of an honest-names finding must clear the path **and** the symbols in the named surface, not only one of them.

### Folder placement

On every `initial` or `full-rescan` Standards pass, walk **new files** in the shipped diff against `structure:folders`:

1. Related new files must sit in a named owning folder, not as mixed siblings of unrelated code in `src/`, `app/`, `convex/`, or a route folder that already holds a different slice.
2. A new concern gets a folder even for the first file. Do not wait for five siblings.
3. `quality:never-nest` and `quality:keep-it-simple` are not a defense. Never-nest is control flow.
4. Pre-existing mixed siblings left untouched are Follow-up unless the goal or a named finding requires a move (`structure:prior-mistakes`).

Cite `structure:folders`. A shipped-diff folder-map miss is **Fix now**. Relocating untouched old flats is Follow-up unless required.

### Env reuse

On every `initial` or `full-rescan` Standards pass, walk **new environment variables** in the shipped diff against `quality:reuse-env`:

1. Inventory names already in `.env.example`, committed `.env*` templates, and `process.env` / `import.meta.env` usages in the repo (and the platform env list when the diff sets dashboard/CLI vars).
2. A new name whose **job or value** an existing var already holds (`FRONTEND_URL` while `SITE_URL` exists) is a finding. Cite `quality:reuse-env`.
3. Mapping in code from the existing name is correct. Duplicating the value under a synonym is not. A required platform prefix must use the existing name (`NEXT_PUBLIC_SITE_URL`), not a third synonym.

A shipped-diff synonym is **Fix now**. Untouched historical aliases left in files the diff did not add are Follow-up unless the goal or a named finding requires a move.

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

Return the review output fence from the [review contract](contract.md#output), including the four PR extras rows on a GitHub PR. Use the shared finding record; IDs remain stable across follow-up discussion. Map shared severity with the contract table; do not re-explain it.

**Local branch diff:** show Fix now, Follow-up, and Optional nit in chat after an initial review or full rescan. A user can explicitly waive a named finding in chat; that is a decision, not proof that the issue is fixed.

**GitHub PR:** show every full new draft in chat before posting, then ask exactly one publish question for the batch. With no drafts and no unresolved blocker, ask once whether to approve. A `blocker` becomes **Blocking**; a `follow-up` or `nit` becomes **Nit** only when a public comment is useful, otherwise it stays in chat. Public comment severities are **Blocking** and **Nit** only. Never post a summary, announcement, index, or pass-status comment. One root-cause topic gets one comment. On a follow-up, Pass A precedes new review work, then Pass B; the stale-head guard runs before any publish. Steps and comment shape: [reference.md](reference.md).

## Apply

After an initial review or full rescan, recommend a behavior-lock test only per the [review contract](contract.md#behavior-lock-recommendation) rule. Tell the user why the lock matters. Skip a claim the user already accepted or refused in the current `/task` lock batch, unless the shipped public contract differs from that brief. Never write tests or edit test files from this skill. If the user says yes, the test is written by following [testing.md](../rules/testing.md).

For UI changes, apply [React and UI](../rules/user-experience.md#react-and-ui) and `docs/design.md` (`ux:source-of-truth`). Judge UI from the diff and existing terminal/test output; do not open a browser or capture screenshots. Do not run a Design review pass.

**Local branch diff:**

- Remediation is never a broad architecture hunt and never reopens the full initial review. Do not silently upgrade a remediation pass to a full rescan.
- Before any fix work, send selected **Fix now** findings to `/analyze` in review-remediation mode. Its remediation analysis returns one section keyed to each stable finding ID. Then require explicit promotion of the selected finding IDs before implementation begins. Promotion bounds work to those findings, the stated touch surface, and stated non-goals.
- If Fix now is empty, end the review without starting a fix loop. Do not write external tracker or PR updates in this mode.

**GitHub PR:**

- This mode is a user start. Do not nest it under `/task`, and do not automatically start a local fix or `/task` lifecycle after publishing.
- Review is stateless. Re-run the shared hunts on the GitHub diff even when a local review already judged the branch.
- Durable specification sources are the PR title/body, linked ticket, and user-approved committed repository documentation. Follow the shared [execution context](../rules/planning.md#execution-context): rediscover facts from the PR and repository instead of depending on local `/task`, workspace, cache, temp, registry, or review-snapshot artifacts.
- A linked GitHub issue or Linear ticket is **read-only** context. Post only on the PR, never on the ticket or Linear.
- Use the harness pull-request / GitHub tool for GitHub reads and writes when the harness has one; otherwise use `gh` or `gh api`.
- Do not create helper scripts or repository files to prepare or publish a review.
- Keep the shared finding ID internally and reuse the matching GitHub thread for an existing issue. Do not duplicate an open finding as a new comment.

## Anti-patterns

- Merging Standards and Spec into one undifferentiated ranking
- Skipping the Spec pass, Pass A, or new-surface review because the Standards pass looked clean
- Running a second adversarial review or hunt re-inspect after the Standards and Spec passes
- Inventing a `/design-review` skill or a Design review axis
- Skipping [code-quality.md](../rules/code-quality.md) and [code-structure.md](../rules/code-structure.md) because the diff or PR looks small
- Skipping Cite-key sweeps or accepting Standards output without Principles, Architecture, or Correctness tables
- Skipping naming alignment or treating stale file/symbol names after a rename as Optional nits
- Treating a mixed-parent file dump in the shipped diff as Optional nit or as "keep it simple"
- Treating a new `FRONTEND_URL` (or other synonym) as Optional nit when `SITE_URL` already holds that job
- Treating a public write without identity/ownership as Optional nit
- Soft-pedaling `quality:keep-jobs-apart`, `quality:fail-fast`, `quality:safe-to-retry`, or `quality:trust-the-server` as Nit when they introduce or extend a correctness or security risk
- Capping findings, reporting without the review output fence, or reporting speculation
- Running a broad rescan during remediation
- Fixing before remediation analysis and explicit promotion
- Treating Follow-ups or Optional nits as default fix scope
- Persisting hidden review state instead of keeping decisions and findings in chat (local) or the GitHub thread (PR)
- Writing test files, or starting a test the user did not accept
- On a PR: approving or commenting without the review output fence or PR extras
- On a PR: skipping PR extras (body vs diff, historical threads, migration, breaking API)
- On a PR: posting a summary comment instead of one-topic findings

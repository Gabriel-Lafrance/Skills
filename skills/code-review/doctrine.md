# Code Review doctrine

## Job

Review a shipped diff for quality and whether it matches the request.

## Owns

Two axes (Standards vs Spec), a Design axis when the diff is user-visible, blocker vs follow-up judgment per principle, naming alignment, and the local remediation/promotion boundary.

## Does not own

- Evidence bar, modes, finding record, review output fence, severity map: [`../pack-shared/review-contract.md`](../pack-shared/review-contract.md)
- Taste and architecture bars: cite `taste:*` and `architecture:*`
- Design file bars: cite `design:*`
- GitHub posting, Pass A/B, PR extras: [`../pr-review/doctrine.md`](../pr-review/doctrine.md)
- Test writing: [`../create-test/doctrine.md`](../create-test/doctrine.md)
- Numbered parent dispatch: [`SKILL.md`](SKILL.md)

## Cite keys

| Key | Heading |
| --- | --- |
| `code-review:axes` | Axes |
| `code-review:blocker-vs-follow-up` | Blocker vs follow-up |
| `code-review:naming-alignment` | Naming alignment |
| `code-review:design-axis` | Design axis |

## Bars

### Axes

Review along independent axes; present them separately. Add Design when the shipped diff is user-visible UI (`code-review:design-axis`).

- **Standards:** maintainability, architecture, repository conventions, design quality, and reachable bugs in the shipped diff (Correctness hunt).
- **Spec:** whether the shipped change satisfies the user request, ticket, PR, and accepted requirements.
- **Design:** whether the touched UI respects `docs/design.md`. Not a separate skill. Parallel Task like Spec.

Use an A+ exam bar: report every evidenced defect on an initial review or full rescan; there is **no findings cap**. Keep findings factual, not roleplay. Thoroughness means stronger path walks and better evidence, never hypothetical failures.

Resolve Standards in this order:

1. `/taste` doctrine (Cite keys)
2. `/architecture` doctrine (Cite keys)
3. Repository rules and committed project documentation (these win on conflict)
4. Optional project standards when present; do not require a particular standards file
5. Baseline defects in the review contract

Treat the first two sources as **hard** unless repository rules conflict. On every `initial` or `full-rescan`, **Read** both doctrines before adjudicating Standards ([standards.md](../pack-shared/standards.md)). Reject Standards output that skipped either Read.

### Blocker vs follow-up

For the shipped diff, check each taste named principle. Cite the principle’s **plain name** and cite key in the finding **Rule** field when violated. The user-facing sentence must still explain the problem in ordinary words ([plain-language.md](../pack-shared/plain-language.md)).

| Principle | Blocker when | Follow-up when |
| --- | --- | --- |
| **Keep it simple** | New ceremony without evidence it is required for Done when / rules that must stay true | Slightly overbuilt but still correct |
| **Keep jobs apart** | UI/feature owns Stripe, JWT, email, or mixed jobs in one unit | Mild mixing with a clear later split |
| **One altitude** | One function both coordinates and does low-level detail in a way that hides bugs | Long but still readable |
| **Read or write, not both** | A read also writes, or a command hides writes behind a “get” | Mild naming oddity on an otherwise correct command/query |
| **Fail fast** | Invalid input accepted past the boundary into partial side effects | Late check that still prevents bad writes |
| **Leave it cleaner** | Diff copies or extends a known-wrong shape in the touched lane | Cleanup opportunity not required for this PR |
| **Related together** | Callers reach service internals; unrelated jobs jammed into one module | Coupling that works but should tighten |
| **Safe to retry** | Replay/double-submit can duplicate charges, rows, or side effects | Missing key where risk is low |
| **Say what happens** | Hidden globals, surprise side effects, or control flow a reader cannot see | Minor magic with local clarity |
| **No surprises** | Surprising API/UI behavior vs name or docs | Slightly awkward but documented behavior |
| **Honest names** | Diff changes the job but leaves a stale **file path**, **export**, **type**, or **widely used symbol** | Local helper mildly stale but still navigable |
| **Trust the server** | Public write trusts the client or a UI-only guard; identity or ownership missing | Extra client check that duplicates a real server lock |
| **Types tell the truth** | New public surface uses `any`, skips validators, or marks required data optional | Local private helper loosely typed but not on a boundary |

A useful cleanup remains a **Follow-up** unless it violates the spec or an Active Rule, causes a correctness or security defect, regresses behavior, or is necessary to clear a named finding. A public write without identity or ownership is a blocker candidate, not a nit.

Prefer a direct guard at the state-owning boundary over extra coordination. Request an `if` only for a reachable invalid state or a missing authoritative invariant. Request `try/catch` only where it recovers, translates, adds actionable context, or cleans up. Request retries only for an evidenced transient external failure with an idempotent, bounded operation. Request queues, locks, or other coordination only when evidence shows a direct authority cannot preserve the needed behavior. Do not turn “might fail someday” into a finding.

### Naming alignment

On every `initial` or `full-rescan` Standards pass, after the principles checklist, walk the shipped diff for **stale names after rename/scope change**:

1. **File paths:** if responsibility moved (new domain word in symbols, comments, ticket, or hunks), the filename/folder must match; do not leave `checkout-total.ts` owning payment-intent logic.
2. **Exports and primary symbols:** exported functions, classes, types, React components, and Convex handlers must match the current job; rename in the same change as the scope shift.
3. **Call sites and variables:** update imports, identifiers, and locals that still describe the old concept when the touched lane changed meaning.
4. **Half-moves:** a move/rename that updates content but keeps the old path (or the reverse) is a defect, not a style preference.

Cite `taste:honest-names` on findings. Naming alignment is part of the Standards pass, not a later wave. Remediation of an honest-names finding must clear the path **and** the symbols in the named surface, not only one of them.

### Design axis

When the shipped diff is user-visible UI, dispatch a Design Task beside Standards and Spec. The worker Reads `docs/design.md` and `/design` doctrine. Skip Design when the file is missing or the diff has no UI; report that absence.

Do not auto-map `diverges` or `undocumented` to Fix now. The parent asks whether the live UI is normal ([asking.md](../pack-shared/asking.md)):

- **No:** Fix now. The UI must match `docs/design.md`. `/design` implements the fix.
- **Yes:** `/design` updates `docs/design.md` with the common-sense why, usually fewer clicks or keystrokes (`design:fewer-clicks`). That is not a UI defect.

Do not invent UX rules the file does not state. Do not ship a `/design-review` skill.

## Output

Return the review output fence from the [review contract](../pack-shared/review-contract.md#output). Show Fix now, Follow-up, and Optional nit after an initial review or full rescan. A user can explicitly waive a named finding in chat; that is a decision, not proof that the issue is fixed.

Use the shared finding record in chat. IDs remain stable across follow-up discussion. Map shared severity with the contract table; do not re-explain it.

## Apply

Remediation is never a broad architecture hunt and never reopens the full initial review. Do not silently upgrade a remediation pass to a full rescan.

Before any fix work, send selected **Fix now** findings to `/analyze` in review-remediation mode. Its remediation analysis returns one section keyed to each stable finding ID. Then require explicit promotion of the selected finding IDs before implementation begins. A `/just-do-it` parent may take the recommended promotion only after the complete analysis is shown. Promotion bounds work to those findings, the stated touch surface, and stated non-goals.

If Fix now is empty, end the review without starting a fix loop. Do not write external tracker or PR updates from this skill.

After an initial review or full rescan, recommend `/create-test` only per the review-contract behavior-lock rule. Tell the user why the lock matters. Never invoke `/create-test`, write tests, or edit test files from this skill.

For UI changes, apply `/taste` React and UI guidance ([`../taste/reference.md`](../taste/reference.md)) and `docs/design.md` (`design:source-of-truth`). Use available browser validation for targeted visual or interaction evidence, and state when visual confirmation was unavailable. Run `code-review:design-axis` when the diff is user-visible.

## Anti-patterns

- Merging Standards and Spec into one undifferentiated ranking
- Soloing Standards/Spec/Design on the main agent instead of parallel Task workers
- Running a second adversarial review or hunt re-inspect after the parallel pass
- Auto-failing or auto-passing Design mismatches without asking if they are normal
- Inventing a `/design-review` skill
- Skipping Cite-key sweeps or accepting Standards output without Principles, Architecture, or Correctness tables
- Skipping naming alignment or treating stale file/symbol names after a rename as Optional nits
- Treating a public write without identity/ownership as Optional nit
- Capping findings, accepting unstructured worker output, or reporting speculation
- Running a broad rescan during remediation
- Fixing before remediation analysis and explicit promotion
- Treating Follow-ups or Optional nits as default fix scope
- Persisting hidden review state instead of keeping decisions and findings in chat
- Auto-running `/create-test` or writing test files

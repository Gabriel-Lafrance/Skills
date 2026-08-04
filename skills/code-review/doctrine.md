# Code Review Doctrine

**Authoritative shared contracts:** [review contract](../pack-shared/review-contract.md) · [execution context](../pack-shared/execution-context.md) · [subagents](../pack-shared/subagents.md). They define modes, evidence, finding shape, severity, worker output, Task dispatch, and stateless operation. This adapter defines the `/code-review` axes and remediation boundary.

## Review posture

Review along two independent axes; present them separately:

- **Standards** — maintainability, architecture, repository conventions, and design quality.
- **Spec** — whether the shipped change satisfies the user request, ticket, PR, and accepted requirements.

Use an A+ exam bar: report every evidenced defect on an initial review or full rescan; there is **no findings cap**. Keep findings factual, not roleplay. Thoroughness means stronger path walks and better evidence, never hypothetical failures.

## Standards sources and judgment

Resolve Standards in this order:

1. `/taste` — [KISS](../taste/doctrine.md#kiss--keep-it-stupid-simple), [Named principles](../taste/doctrine.md#named-principles), complexity/entropy, non-negotiables, and [examples](../taste/examples.md)
2. `/architecture` — services, deep surfaces, SoC / cohesion / coupling / idempotent writes, and [examples](../architecture/examples.md)
3. Repository rules and committed project documentation — these win on conflict
4. Optional project standards when present; do not require a particular standards file
5. Smell baseline plus thermonuclear maintainability

Treat the first two sources as **hard** unless repository rules conflict. On every
`initial` or `full-rescan`, **Read** `/taste` doctrine (at least KISS + Named
principles) and `/architecture` doctrine before adjudating Standards. Do not
treat principles as optional flavor text.

### Named principles checklist (required on Standards)

For the shipped diff, actively check each principle. Cite the principle name in
the finding **Rule** field when violated (e.g. `taste:KISS`, `taste:SoC`,
`taste:fail-fast`, `architecture:idempotency`).

| Principle | Blocker when | Follow-up when |
| --- | --- | --- |
| **KISS** | New ceremony/machinery without evidence it is required for Done when / Active Rules | Slightly overbuilt but still correct |
| **SoC** | UI/feature owns domain I/O (Stripe, JWT, email, …) or mixed reasons-to-change in one unit | Mild mixing with a clear later split |
| **SLAP** | One function both orchestrates and does low-level detail in a way that hides bugs | Long but still readable |
| **CQS** | Query mutates state, or command hides surprising writes behind a “get” | Mild naming oddity on an otherwise correct command/query |
| **Fail fast** | Invalid input accepted past the boundary into partial side effects | Late check that still prevents bad writes |
| **Boy Scout** | Diff copies or extends known-wrong shape in the touched lane | Cleanup opportunity not required for this PR |
| **High cohesion / low coupling** | Callers reach service internals; unrelated jobs jammed into one module | Coupling that works but should tighten |
| **Idempotency** | Replay/double-submit can duplicate charges, rows, or side effects on write/webhook/retry paths | Missing key where risk is low/non-replayable |
| **Explicit over implicit** | Hidden globals, ambient side effects, or control flow a reader cannot see | Minor magic with local clarity |
| **PoLA** | Surprising API/UI behavior vs name or docs (wrong return, silent catch-all) | Slightly awkward but documented behavior |
| **Honest names** | Diff renames/repurposes a concern (or lands a new primary job) but leaves a stale **file path**, **primary export**, **type**, or **widely used symbol**; or keeps writing new logic into a file whose name describes a different concern | Local helper/var mildly stale but still navigable; casing-only convention issues |

### Naming alignment pass (required on Standards)

On every `initial` or `full-rescan` Standards pass, after the principles checklist,
walk the shipped diff specifically for **stale names after rename/scope change**:

1. **File paths** — if responsibility moved (new domain word in symbols, comments, ticket, or hunks), the filename/folder must match; do not leave `checkout-total.ts` owning payment-intent logic.
2. **Exports and primary symbols** — exported functions, classes, types, React components, and Convex handlers must match the current job; rename in the same change as the scope shift.
3. **Call sites and variables** — update imports, identifiers, and locals that still describe the old concept when the touched lane changed meaning.
4. **Half-moves** — a move/rename that updates content but keeps the old path (or the reverse) is a defect, not a style preference.

Cite `taste:honest-names` on findings. Wave 2 must look for naming drift Wave 1
missed. Remediation of an honest-names finding must clear the path **and** the
symbols in the named surface — not only one of them.

Also inspect placement and public entry points, reuse of existing domain
authorities, complexity and entropy, nesting and needless wrappers, boundary
types and error handling, data access, and UI behavior when applicable. For UI
changes, apply `/taste` React & UI guidance; use available browser validation for
targeted visual or interaction evidence, and state when visual confirmation was
unavailable.

On an initial review or full rescan, actively look for behavior-preserving
simplification (**KISS**, **Boy Scout**) and missed moves. A useful cleanup
remains a **Follow-up** unless it violates the spec or an Active Rule, causes a
correctness or security defect, regresses behavior, or is necessary to clear a
named finding.

## Evidence and safe remedies

Apply the shared [evidence bar](../pack-shared/review-contract.md#evidence-bar) to every runtime-risk or hardening finding. A reachable trigger, concrete evidence, material impact, and the smallest authoritative fix are all required.

- Prefer a direct guard at the state-owning boundary over extra coordination.
- Request an `if` only for a reachable invalid state or a missing authoritative invariant.
- Request `try/catch` only where it recovers, translates, adds actionable context, or cleans up.
- Request retries only for an evidenced transient external failure with an idempotent, bounded operation.
- Request queues, locks, or other coordination only when evidence shows a direct authority cannot preserve the needed behavior.

Do not turn “might fail someday” into a finding or invent defensive machinery.

## Modes and quality gates

Use the shared mode names exactly:

| Mode | `/code-review` work |
| --- | --- |
| `initial` | Full shipped diff and available specification; run both axes, then adversarial Wave 2. |
| `remediation` | Only named finding IDs, fix diff, touched direct paths, and direct callers; verify clearance and regressions in that surface. |
| `full-rescan` | Repeat initial depth only when the parent or user explicitly opens a full rescan for a meaningful change. |

Remediation is never a broad architecture hunt and never gets a broad Wave 2. Do not silently upgrade a remediation pass to a full rescan.

For an `initial` review or `full-rescan`, the parent:

1. Pins the fixed point, inspects the diff, resolves the available spec, and supplies relevant Active Rules.
2. Runs **Wave 1** Standards and Spec as **parallel Task workers** (not sequential solo on the main agent). Skip Spec only when no specification is available; report that absence rather than inventing acceptance criteria. Follow [subagents.md](../pack-shared/subagents.md).
3. Keeps worker output in the shared contract shape; rejects and relaunches a narrative-only result once.
4. Aggregates Standards and Spec separately, deduplicates stable finding IDs, then runs adversarial **Wave 2** (may be a follow-up Task) to find genuinely missed defects. Reject Standards output that lacks the **Principles sweep** table.
5. Applies the evidence bar, severity mapping, and remediation disposition before proposing any fix work.

The parent controls worker dispatch plus acceptance evidence and review gates. Implementation workers receive the supplied lane and context; they do not run acceptance or review gates, select a review mode, or expand the review scope. Do not add specialist review axes unless the user asks; report unavailable browser evidence as a gap, not a Standards finding.

## Findings and disposition

Use the shared [finding record](../pack-shared/review-contract.md#finding-record) in chat. IDs remain stable across follow-up discussion and are based on axis, violated rule or root cause, and strongest location. Fold recurring sites with the same root cause and fix shape into one ID; do not persist local review records.

Map shared severity directly:

| Canonical severity | `/code-review` disposition |
| --- | --- |
| `blocker` | **Fix now** |
| `follow-up` | **Follow-up** |
| `nit` | **Optional nit** |

Show the Fix now, Follow-up, and Optional nit sections after an initial review or full rescan. A user can explicitly waive a named finding in chat; that is a decision, not proof that the issue is fixed.

## Behavior locks

After an initial review or full rescan, recommend `/create-test` only for a complex architectural boundary with externally observable behavior and no durable behavior lock. Tell the user why the lock matters. Never invoke `/create-test`, write tests, or edit test files from this skill.

## Remediation analysis and promotion

Before any fix work, send selected **Fix now** findings to **flow** `/analyze` in
review-remediation mode. Its
[remediation analysis](../analyze/doctrine.md#review-remediation-analysis)
returns one section keyed to each stable finding ID, with current behavior,
root cause, smallest fix, touch surface, non-goals, and verification.

Then require explicit promotion of the selected finding IDs before
implementation begins. A `/just-do-it` parent may take the recommended
promotion only after the complete analysis is shown. Promotion bounds work to
those findings, the stated touch surface, and stated non-goals; it does not
authorize unrelated cleanup. The parent subsequently owns acceptance evidence
and the `remediation` review gate.

If Fix now is empty, end the review without starting a fix loop. Do not write external tracker or PR updates from this skill.

## Anti-patterns

- Merging Standards and Spec into one undifferentiated ranking
- Soloing Wave 1 Standards/Spec on the main agent instead of parallel Task workers
- Skipping Wave 2 for an initial review or full rescan
- Skipping the Named principles checklist or accepting Standards output without a **Principles sweep**
- Skipping the **Naming alignment pass** or treating stale file/symbol names after a rename as Optional nits
- Capping findings, accepting unstructured worker output, or reporting speculation
- Running a broad rescan during remediation
- Fixing before remediation analysis and explicit promotion
- Treating Follow-ups or Optional nits as default fix scope
- Persisting hidden review state instead of keeping decisions and findings in chat
- Auto-running `/create-test` or writing test files

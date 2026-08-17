# UX Review Doctrine

**Authoritative shared contracts:** [review contract](../pack-shared/review-contract.md) · [execution context](../pack-shared/execution-context.md) · [subagents](../pack-shared/subagents.md) · [browser evidence](../pack-shared/browser-evidence.md). They define modes, evidence, finding shape, severity, worker output, Task dispatch, and stateless operation. This adapter defines the `/ux-review` axes, Job card protocol, and remediation boundary.

## Review posture

This skill is a **judge**, not a builder. Review along two independent axes;
present them separately:

- **Flow** — whether a first-timer in the derived role can complete the primary job without being told how.
- **Craft** — hierarchy, signifiers, states, microcopy, accessibility, and repository visual rules on the touched UI.

Use an A+ exam bar: report every evidenced defect on an initial review or full rescan; there is **no findings cap**. Keep findings factual, not taste roleplay. Thoroughness means walking the user path and citing screens/code, never hypothetical users.

Do not run `/goal`, `/code-review`, or `/pr-review` from this skill. Hand off:

| Concern                                  | Owner                            |
| ---------------------------------------- | -------------------------------- |
| Implement or polish the UI               | `/goal` after explicit promotion |
| Code correctness, architecture, security | `/code-review`                   |
| Publish GitHub review comments           | `/pr-review`                     |

A motion issue that **blocks the job** (hidden control, unskippable delay on a frequent action) stays a Flow finding here. Pure feel/timing nits are not `/ux-review` findings.

## Job card protocol

Compile the Job card **before** Wave 1. Workers receive it; they do not invent it.

Resolve context in the shared [authority order](../pack-shared/execution-context.md#authority). Durable spec sources are the user request, ticket, PR body (read-only), and committed documentation.

```markdown
## Job card

**User:** <role from ticket/docs/routes — not an invented persona>
**Job of this screen:** one sentence
**Primary action:** …
**Happy path:** 1 → n
**Other states:** empty / loading / error / success / no-permission
**Out of scope:** …
```

Reuse a parent-supplied job, primary action, and states from `/goal` or `/analyze` when they already exist. Do not invent a user, use case, or step. If the job or user cannot be derived, say so and skip the Flow axis — same rule as `/code-review` skipping Spec.

## Flow axis

Ask: can this user finish the job on the shipped UI?

Walk the happy path and the Job card's other states. A Flow blocker needs a reachable step, evidence from the UI/diff/browser, and material impact on completing the job.

Typical blockers:

- The next step is missing, mislabeled, or visually secondary at the moment the user needs it
- Empty, error, or no-permission states strand the user with no recovery action
- Copy that names the wrong product concept (repository terminology rules win)
- A control that does not do what its label promises
- A first-run or frequent path that requires an instruction wall

Not a Flow finding: an adjacent screen outside the Job card, a backend-only defect with no UI path, or a missing persona you speculated.

## Craft axis

Ask: does the touched UI meet repository visual/interaction rules and basic usability on this screen?

Resolve Craft sources in this order:

1. Repository rules and committed design/docs — these win on conflict (tokens, contrast, i18n, product wording)
2. `/taste` React & UI guidance (and `/architecture` when structure is in play) when no repo rule applies
3. Obvious accessibility floors: visible focus, keyboard reachability of the primary action, `prefers-reduced-motion` when movement is introduced, contrast of shipped colors

Do not invent a palette, type pairing, or brand direction. Do not treat "could be prettier" as a blocker.

Typical blockers:

- Unreadable contrast or a banned color pairing introduced in the lane
- Missing default / hover / active / disabled / loading / error on a control the Job card depends on
- Primary action visually equal to every secondary action
- User-facing strings that violate repository i18n or terminology rules

A valuable visual cleanup that does not block the job or violate a repo rule remains a **Follow-up**.

## Visual evidence

When Cursor's native Browser is available, follow the [browser evidence protocol](../pack-shared/browser-evidence.md): reuse the running app, trace the happy path, and capture each Job card step. Record URL, viewport, and what the step showed.

If Browser access, credentials, or a reachable preview is unavailable, mark visual confirmation as a **gap**, not a Craft finding. Terminal and code-path evidence remain valid for copy, state branches, and contrast tokens.

## Evidence and safe remedies

Apply the shared [evidence bar](../pack-shared/review-contract.md#evidence-bar) to every blocker. A reachable trigger, concrete evidence, material impact, and the smallest authoritative fix are all required.

- Prefer the smallest UI change that restores the next step (label, hierarchy, missing state, one control)
- Do not request a redesign, new design system, or animation pass to clear a Flow blocker
- Do not turn "users might be confused someday" into a finding without a path walk

## Modes and quality gates

Use the shared mode names exactly:

| Mode          | `/ux-review` work                                                                       |
| ------------- | --------------------------------------------------------------------------------------- |
| `initial`     | Full shipped UI surface and available Job card; run both axes, then adversarial Wave 2. |
| `remediation` | Only named finding IDs, fix diff, touched direct paths, and the same Job card.          |
| `full-rescan` | Repeat initial depth only when the parent or user explicitly opens a full rescan.       |

Remediation is never a broad visual hunt and never gets a broad Wave 2. Do not silently upgrade a remediation pass to a full rescan.

For an `initial` review or `full-rescan`, the parent:

1. Pins the fixed point, inspects the UI diff or named screen, compiles the Job card, and supplies relevant Active Rules.
2. Runs **Wave 1** Flow and Craft work in parallel. Skip Flow only when no job/user is available; report that absence.
3. Keeps worker output in the shape below; rejects and relaunches a narrative-only result once.
4. Aggregates Flow and Craft separately, deduplicates stable finding IDs, then runs adversarial **Wave 2** to find genuinely missed defects.
5. Applies the evidence bar, severity mapping, and remediation disposition before proposing any fix work.

The parent controls worker dispatch plus validation and review gates. Implementation workers receive the supplied lane, Job card, and context; they do not run validation or review gates, select a review mode, or expand the review scope.

## Worker artifacts

```markdown
## Job card

<parent-supplied card, echoed>

## Flow findings

- <finding record>

## Spec matrix

| Job-card step / state | Status                         | Evidence |
| --------------------- | ------------------------------ | -------- |
| …                     | met \| unmet \| blocked \| n/a | …        |

## Craft findings

- <finding record>

## Adversarial findings

- <new finding record and why Wave 1 missed it>
```

Workers report no finding explicitly when their axis is clean. Finding axis values are `flow`, `craft`, or `cross`. IDs stay stable, for example `flow-empty-state-no-primary-action`.

## Findings and disposition

Use the shared [finding record](../pack-shared/review-contract.md#finding-record) in chat, with axis `flow|craft|cross`. **Where** must name a file/symbol **and** the Job card step when Flow is involved.

Map shared severity like `/code-review`:

| Canonical severity | `/ux-review` disposition |
| ------------------ | ------------------------ |
| `blocker`          | **Fix now**              |
| `follow-up`        | **Follow-up**            |
| `nit`              | **Optional nit**         |

Show the Fix now, Follow-up, and Optional nit sections after an initial review or full rescan. A user can explicitly waive a named finding in chat; that is a decision, not proof that the issue is fixed.

Do not post GitHub comments. If the surface is an open PR, `/pr-review` remains the publication skill; this skill may recommend invoking it.

## Remediation analysis and promotion

Before any fix work, send selected **Fix now** findings to `/analyze` in
review-remediation mode. Then require explicit promotion of the selected finding
IDs. Promotion bounds work to those findings and the stated touch surface. The
parent subsequently owns validation and the `remediation` review gate.

If Fix now is empty, end the review without starting a fix loop. Do not write
external tracker or PR updates from this skill. Do not invoke `/goal` or
edit UI files from this skill.

## Anti-patterns

- Judging pixels before compiling a Job card
- Inventing personas, use cases, or steps not in the spec sources
- Merging Flow and Craft into one undifferentiated ranking
- Skipping Wave 2 for an initial review or full rescan
- Calling missing browser access a Craft defect
- Builder (`/goal`) and judge (`/ux-review`) in the same turn on the same surface
- Posting PR comments, auto-fixing, or persisting hidden review state
- Treating Follow-ups or Optional nits as default fix scope
- Inventing brand tokens, palettes, or type to "improve" repository design
- Recommending or writing tests (`/create-test` is owned by `/code-review` / `/pr-review`)

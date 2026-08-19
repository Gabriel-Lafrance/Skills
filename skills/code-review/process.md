# Code Review process

**Read:** [../pack-shared/standards.md](../pack-shared/standards.md) ·
[doctrine](doctrine.md) · [review contract](../pack-shared/review-contract.md) ·
[execution context](../pack-shared/execution-context.md)

## Inputs

Pin the requested fixed point and inspect its shipped diff.

If a parent already supplied outcome, done-when, non-goals, ticket or PR,
fixed point, lane, phase, Active Rules, current slices, and fix backlog,
treat that chat context as the binding handoff. Do not reconstruct intent
from hidden files.

Otherwise derive the Spec axis from, in order:

1. The user's stated outcome and acceptance criteria
2. A named PR, ticket, and their available discussion
3. Relevant repository code, rules, and committed documentation

If no specification is available, say so and run Standards without inventing
requirements. Keep all findings, decisions, and remediation memos in chat.

Cite an Active Rule only when it is actually violated; otherwise cite the
relevant acceptance criterion or state that no rule applies.

## Scope

Select the shared review mode deliberately:

- `initial` reviews the complete shipped diff with Standards and Spec, then Wave 2.
- `remediation` receives named finding IDs, the fix diff, touched direct paths, and direct callers only.
- `full-rescan` requires an explicit request to re-open full-review depth after a meaningful change.

Apply `code-review:axes`, `code-review:blocker-vs-follow-up`,
`code-review:naming-alignment`, the review-contract evidence bar, and
remediation analysis before any fix work. Standards workers must return the
Wave 1 fences. Wave 2 must return the hunt re-inspect. Standards must Read
`/taste` and `/architecture` this turn.

For `remediation`, verify those findings and regressions in that surface; do
not reopen a broad review.

## Handoff

The parent (this chat, or `/goal` / `/just-do-it` when nested) owns
fixed-point setup, worker dispatch, acceptance evidence, and review gates.
Implementation workers do not run those gates or broaden a remediation
review. Report stable finding IDs and the Fix now / Follow-up / Optional nit
disposition in chat.

### If a parent already owns the next step

Before any fix work, send selected Fix now findings to `/analyze` in
review-remediation mode. Its memo stays keyed to the stable finding IDs,
then requires explicit promotion (or the documented `/just-do-it`
exception). The promoted lane remains bounded to those findings and the
supplied current slices.

### If this is a user one-off

Report the disposition in chat. Do not invent a parent wave or promote
fixes unless the user asked for that next step.

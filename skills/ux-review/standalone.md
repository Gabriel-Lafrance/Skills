# Standalone UX Review

**Read:** [../pack-shared/standards.md](../pack-shared/standards.md) ·
[doctrine](doctrine.md) · [review contract](../pack-shared/review-contract.md) ·
[execution context](../pack-shared/execution-context.md)

## Inputs

Pin the requested fixed point and inspect its shipped UI diff (or named screen
when the user points at a route/component without a diff). Derive the Job card
from, in order:

1. The user's stated outcome, users, and acceptance criteria
2. A named PR, ticket, and their available discussion (read-only)
3. Relevant repository code, routes, rules, and committed documentation

Do not invent a user, use case, or flow. If the job or user cannot be derived,
say so and run Craft without inventing Flow requirements. Keep all findings,
decisions, and remediation memos in chat; do not require a saved review artifact.

## Scope

Select the shared review mode deliberately:

- `initial` reviews the complete shipped UI surface with Flow and Craft, then Wave 2.
- `remediation` receives named finding IDs, the fix diff, touched direct paths, and the same Job card.
- `full-rescan` requires an explicit request to re-open full-review depth after a meaningful change.

Apply the doctrine's Job card protocol, separate axes, evidence bar, severity
mapping, and remediation analysis before any fix work. Do not post GitHub
comments; `/pr-review` owns publication.

## Handoff

The parent owns fixed-point setup, Job card compilation, worker dispatch,
validation, and review gates. Implementation workers do not run those gates or
broaden a remediation review. Report stable finding IDs and the Fix now /
Follow-up / Optional nit disposition in chat.

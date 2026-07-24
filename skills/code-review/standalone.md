# Standalone Code Review

**Read:** [doctrine](doctrine.md) · [review contract](../pack-shared/review-contract.md) · [execution context](../pack-shared/execution-context.md)

## Inputs

Pin the requested fixed point and inspect its shipped diff. Derive the Spec axis from, in order:

1. The user's stated outcome and acceptance criteria
2. A named PR, ticket, and their available discussion
3. Relevant repository code, rules, and committed documentation

If no specification is available, say so and run Standards without inventing requirements. Keep all findings, decisions, and remediation memos in chat; do not require a saved review artifact.

## Scope

Select the shared review mode deliberately:

- `initial` reviews the complete shipped diff with Standards and Spec, then Wave 2.
- `remediation` receives named finding IDs, the fix diff, touched direct paths, and direct callers only.
- `full-rescan` requires an explicit request to re-open full-review depth after a meaningful change.

Apply the doctrine's separate axes, evidence bar, severity mapping, behavior-lock recommendation, and remediation analysis before any fix work.

## Handoff

The parent owns fixed-point setup, worker dispatch, validation, and review gates. Implementation workers do not run those gates or broaden a remediation review. Report stable finding IDs and the Fix now / Follow-up / Optional nit disposition in chat.

# Flow Code Review

**Read:** [doctrine](doctrine.md) · [review contract](../pack-shared/review-contract.md) · [execution context](../pack-shared/execution-context.md)

## Parent-supplied context

The parent supplies the relevant inline execution context before dispatching review work. It includes the outcome, done-when criteria, non-goals, ticket or PR, fixed point, lane, phase, applicable **Active Rules**, current slices, and fix backlog when they matter.

Treat that chat context as the binding handoff. Do not reconstruct intent from hidden files or require persisted review state. Cite an Active Rule only when it is actually violated; otherwise cite the relevant acceptance criterion or state that no rule applies.

## Flow

1. The parent opens the review gate and selects `initial`, `remediation`, or an explicit `full-rescan` under the shared review contract.
2. For `initial` and `full-rescan`, it provides the fixed-point diff, relevant spec, Active Rules, and current slice to separate Standards and Spec work, then requires adversarial Wave 2. Standards must run the Named principles checklist, the **Naming alignment pass**, and return the **Principles sweep** table (including Honest names).
3. For `remediation`, it provides only named finding IDs, the fix diff, touched direct paths, direct callers, and relevant rules. Verify those findings and regressions in that surface; do not reopen a broad review.
4. The parent aggregates stable chat finding IDs, maps them to Fix now / Follow-up / Optional nit, and applies the doctrine's behavior-lock and remediation-analysis rules.
5. Before any fix work, send selected Fix now findings to **flow** `/analyze` in
   review-remediation mode. Its memo stays keyed to the stable finding IDs,
   then requires explicit promotion (or the documented `/just-do-it`
   exception). The promoted lane remains bounded to those findings and the
   supplied current slices.

The parent controls worker dispatch, acceptance evidence, and review gates. Implementation workers do not run those gates or promote, rescan, or widen review scope.

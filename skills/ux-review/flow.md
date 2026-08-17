# Flow UX Review

**Read:** [../pack-shared/standards.md](../pack-shared/standards.md) ·
[doctrine](doctrine.md) · [review contract](../pack-shared/review-contract.md) ·
[execution context](../pack-shared/execution-context.md)

## Parent-supplied context

The parent supplies the relevant inline execution context before dispatching
review work. It includes the outcome, done-when criteria, non-goals, ticket or
PR, fixed point, lane, phase, applicable **Active Rules**, current slices, and
fix backlog when they matter.

When a job, primary action, and states already exist from `/goal` or
`/analyze`, reuse them as the Job card seed. Do not rebuild product intent from
hidden files.

Treat that chat context as the binding handoff. Cite an Active Rule only when
it is actually violated; otherwise cite the relevant acceptance criterion or
state that no rule applies.

## Flow

1. The parent opens the UX review gate after a UI slice (typically after
   `/goal` or implementation, before or beside `/code-review`) and selects
   `initial`, `remediation`, or an explicit `full-rescan`.
2. It compiles the Job card, pins the UI fixed point, and for `initial` /
   `full-rescan` dispatches Flow and Craft work in parallel, then requires
   adversarial Wave 2. Skip Flow only when the job/user cannot be derived;
   report that absence rather than inventing users.
3. For `remediation`, it provides only named finding IDs, the fix diff, touched
   direct paths, the same Job card, and relevant rules. Verify those findings
   and flow regressions in that surface; do not reopen a broad review.
4. The parent aggregates stable chat finding IDs, maps them to Fix now /
   Follow-up / Optional nit, and applies the doctrine's remediation-analysis
   rules.
5. Before any fix work, send selected Fix now findings to **flow** `/analyze` in
   review-remediation mode. Its memo stays keyed to the stable finding IDs,
   then requires explicit promotion (or the documented `/just-do-it`
   exception). The promoted lane remains bounded to those findings and the
   supplied current slices.

The parent controls worker dispatch, validation, and review gates.
Implementation workers do not run those gates or promote, rescan, or widen
review scope. Do not post GitHub comments from this skill.

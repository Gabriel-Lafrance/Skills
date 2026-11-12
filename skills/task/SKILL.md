---
name: task
description: Default build skill. Use when the user asks to build, implement, add, or fix a feature or a bug, refactor, upgrade, speed something up, or resume a build. Writes no tests.
category: Code
---

# Task

Orchestrate one verifiable outcome end to end.

## Read when

- Before starting web services or debugging a browser preview: [development-server logs](../rules/dev-server-logs.md).
- Before grilling: [doctrine.md](doctrine.md), [execution context](../rules/planning.md#execution-context).
- At a step that names a section: [reference.md](reference.md).

## Process

1. Apply the shared [ready-ticket preflight](../rules/execution.md#ready-ticket-preflight), then establish or refresh the in-chat execution context. Accept a parent's brief when it already supplies ticket, lane, Done when, non-goals, rules, fixed point and slice bounds; the parent keeps ticket and branch ownership. For a request to implement a parent ticket's children, use the [whole-stack handoff](doctrine.md#whole-stack-ticket-handoff).
2. Run the [lifecycle](reference.md#lifecycle) in this order:
   1. Reuse the ready ticket lock; grill only unresolved consequential choices.
   2. Plan.
   3. Implement. Apply [code-quality.md](../rules/code-quality.md) and [code-structure.md](../rules/code-structure.md) before every slice, and [user-experience.md](../rules/user-experience.md) before every user-facing slice.
   4. Gate: pick checks under [verification scope](../rules/execution.md#verification-scope). Localized low-risk work gets focused checks and a diff review here. Substantial or high-risk work, or a request for it, gets independent `/verification` and `/review` agents together; judge their handoffs here.
   5. [Fix mode](reference.md#fix-mode-review-remediation-only), as needed.
3. Write no tests: [no unrequested tests](../rules/no-unrequested-tests.md).
4. Announce completion.

### If a parent already owns the ticket, branch, and PR

Return the completion summary and evidence to the parent. The parent ships under the user's existing authorization.

### If this chat owns shipping

After all gates pass, follow [shipping.md](../rules/shipping.md) when the user already authorized shipping, including stacked PRs. Otherwise end with the [ship offer](reference.md#ship-offer) and wait.

## Anti-patterns

- Offering to ship, pushing, or opening a PR when a parent owns shipping

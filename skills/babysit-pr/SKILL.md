---
name: babysit-pr
description: Use when the user asks to babysit, watch, or monitor a PR until checks or reviews change, or report when it is ready. Watch and report by default; fixes and other mutations need their own authorization.
category: Code
---

# Babysit a PR

Every run applies [code quality](../rules/code-quality.md),
[code structure](../rules/code-structure.md), and
[Plain language](../rules/writing-style.md#plain-language).
Before a decision, use [Asking the user](../rules/writing-style.md#asking-the-user).
Keep ownership and evidence in the existing
[execution context](../rules/planning.md#execution-context).

1. Identify repository, PR and parent/owner. Read
   [PR lifecycle](../rules/pr-lifecycle.md),
   [tool discovery](../rules/tooling.md#harness-first-discovery), and
   [execution evidence](../rules/execution.md#handoffs-and-evidence).
2. Establish authority and inspect existing findings before registering a watch
   under [watch lifecycle](../rules/pr-lifecycle.md#watch-lifecycle).
3. Resolve authorized actionable work through the current orchestrator's
   [remediation](../rules/execution.md#remediation).
4. If still waiting, let only the owner watch. On each wake reconcile state
   and apply [latest-head readiness](../rules/pr-lifecycle.md#latest-head-readiness).
5. Cleanly unwatch before questions, handoff or completion. Report head, actual
   checks/reviews, blockers, readiness and cleanup state. Default stop unmerged.

When nested, return to the existing parent; do not create another watcher,
review dispatcher, or shipping lifecycle.

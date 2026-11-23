---
name: review-loop
description: Use when the user asks for repeated review and correction rounds on a branch or PR, five rounds by default. A single pass goes to review.
category: Code
---

# Review loop

Keep the budget and backlog in the
[execution context](../rules/planning.md#execution-context).

1. Identify the pinned diff/base, outcome, current owner and authorized actions.
   Read [review budget](../review/contract.md#review-budget),
   [review](../review/SKILL.md), and
   [execution remediation](../rules/execution.md#remediation).
2. Reuse the parent's context and consumed rounds, or establish the default
   budget. Select a reviewer under
   [main-context.md](../rules/main-context.md#subagent-roles) and follow its
   [delegation lifecycle](../rules/main-context.md#delegation-lifecycle).
   Reviewers use the [review affinity](../rules/main-context.md#task-affinity)
   (Codex Astra at `xhigh`); set it under
   [apply and verify controls](../rules/main-context.md#apply-and-verify-controls).
3. Run the applicable review mode on a fixed scope. Keep stable IDs and evidence;
   return findings to the one owner. PR comments retain `/review`'s publish gate.
4. Triage findings and severity under [remediation](../rules/execution.md#remediation).
   Fix only required findings within authority. Recheck affected acceptance,
   then review the fixes and new surface.
5. Apply the review budget after every round. Include resolved, rejected and
   deferred IDs in the report.

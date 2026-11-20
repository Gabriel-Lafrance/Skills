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
   Reviewers run at `xhigh` unless the user names another effort; set it under
   [apply and verify controls](../rules/main-context.md#apply-and-verify-controls).
3. Run the applicable review mode on a fixed scope. Keep stable IDs and evidence;
   return findings to the one owner. PR comments retain `/review`'s publish gate.
4. Adjudicate once under [remediation](../rules/execution.md#remediation);
   fix only accepted findings within authority. Recheck affected acceptance,
   then use focused remediation review and review new surface as required.
5. Apply the review budget's stopping, reporting and extension rules after
   every round, and also report resolved and rejected IDs. Completion is a verdict on the
   checked scope, never automatic approval, comment publication, push or merge.

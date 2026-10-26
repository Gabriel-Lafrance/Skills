---
name: review-loop
description: Use when the user asks for repeated review and correction of a branch or PR with a finite budget. Reuses review findings and execution remediation; defaults to three rounds and reports unresolved disputes or exhausted budget.
category: Code
---

# Review loop

Every run applies [code quality](../rules/code-quality.md),
[code structure](../rules/code-structure.md), and
[Plain language](../rules/writing-style.md#plain-language).
Before a decision, use [Asking the user](../rules/writing-style.md#asking-the-user).
Keep the budget and backlog in the existing
[execution context](../rules/planning.md#execution-context).

1. Identify the pinned diff/base, outcome, current owner and authorized actions.
   Read [review budget](../review/contract.md#review-budget),
   [review](../review/SKILL.md), and
   [execution remediation](../rules/execution.md#remediation).
2. Reuse the parent's context and consumed rounds, or establish the default
   budget. Select a reviewer under
   [main-context.md](../rules/main-context.md#subagent-roles) and follow its
   [delegation lifecycle](../rules/main-context.md#delegation-lifecycle).
3. Run the applicable review mode on a fixed scope. Keep stable IDs and evidence;
   return findings to the one owner. PR comments retain `/review`'s publish gate.
4. Adjudicate once and fix only within authority. Recheck affected acceptance,
   then use focused remediation review and review new surface as required.
5. Apply the budget's stopping rules after every round. Report rounds used,
   resolved and unresolved IDs, disagreements, checks and evidence limits.
   Completion is a verdict on the checked scope, never automatic approval,
   comment publication, push or merge.

When nested, this is the current owner's bounded review/remediation phase,
not another build orchestrator or a new reviewer per worker slice.

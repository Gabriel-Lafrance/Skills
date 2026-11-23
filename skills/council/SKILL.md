---
name: council
description: Use when the user asks for a council or a panel of models to review code, compare alternatives, or give feedback.
category: Code
---

# Council

Adapted from Theo's [tstack council](https://github.com/t3dotgg/tstack/blob/1085050f3baed1ac724caa4a8166145fb2ac88af/skills/council/SKILL.md).
The parent owns the decision; delegates supply evidence and disagreements, not
write or shipping authority. Then the [Astra challenger](challenger.md) tests the
proposed conclusion, completed work and reported results.

## Panel

This roster overrides [default model selection](../rules/main-context.md#model-and-effort-selection)
for council members.

| Provider | Model family | Effort key | Assessment | Hillclimb rerating |
| --- | --- | --- | --- | --- |
| Claude | Opus | `effort` | `xhigh` | `high` |
| Codex | Sol | `reasoningEffort` | `xhigh` | `high` |
| Grok | Grok | `reasoningEffort` | `xhigh` | `high` |
| Antigravity | Gemini Neon | `thought_level` | `xhigh` | `high` |

All four rate every round. **Assessment** covers standalone councils and
hillclimb round 0. **Hillclimb rerating** covers later rounds.

Resolve the latest available release of each named family from the live
catalog at run start. Require support for the requested effort. If release
order or support is unclear, report the gap. Never silently substitute an
older release or sibling variant, including Grok Fast or another Gemini variant.
Keep the resolved IDs fixed across rounds. In T3 Code, pass each exact ID
and explicit effort through `delegate_task` using `target.model` and `target.options`.
Never inherit the catalog's effort default.

## Read when

- Before judging code or alternatives: [code quality](../rules/code-quality.md),
  [code structure](../rules/code-structure.md).
- Recording the roster and run state: [execution context](../rules/planning.md#execution-context).
- Code review: [review contract](../review/contract.md). Council supplies
  multiple reviewers under its existing Standards and Spec axes, not a new axis.
- Rendered UI feedback: [UI evidence and judgment](../hillclimb/variants/ui.md).
  Obtain live evidence through [verification](../verification/SKILL.md).

## Process

1. **Prepare the scope.** Pin the request, constraints, revision and working
   diff (including untracked files), or the alternatives and evidence to judge.
   Address known issues and relevant checks before an audit only when fixes
   are already authorized. A feedback-only request stays read-only. Skip fixes
   to an implementation the user wants replaced. Do not import unrelated work.
2. **Select the panel.** Apply [panel](#panel) defaults unless the user overrides
   them. Record the harness, provider, exact model ID, requested effort and
   observable effective settings in the execution context. Report any missing
   member and mark the council incomplete.
3. **Ask independently.** Start members in parallel through the supported
   native or cross-provider route. Give each the same factual brief, pinned
   evidence, rules, test consent and bounded return contract. Use fresh context;
   withhold the parent's preferred answer, prior ratings, other members'
   conclusions and the target score, never requirements or safety
   constraints. Delegates are read-only, do not ask the
   user, and do not spawn agents. Freeze the scoped result while review runs.
   A timeout or error is not approval.
4. **Collect judgments.** For code, request Standards and Spec findings with
   stable IDs, file/line evidence, severity, suggested correction and verdict.
   For alternatives, request a preference, reasons, tradeoffs and uncertainties.
   For code or UI feedback, request a rating out of 10 using the same stated
   rubric for each member. Label ratings as subjective judgments, not measured
   correctness or user preference. A missing rating is `no score`, never an
   inferred value. Ratings cannot clear a required finding or replace the
   variant's evidence and keep bar.
5. **Form a proposed conclusion.** Check each member's claims against the
   actual evidence as that member returns, not after the last one, so the
   challenger can start as soon as the panel is complete. Combine duplicates
   under stable IDs, and record agree/fix, disagree with evidence, or
   follow-up. Preserve dissent and missing evidence; majority votes and score
   averages cannot waive a required fix. Prepare the proposed verdict and
   bounded corrections without dispatching them yet.
6. **Challenge the work and results.** Run the [challenger](challenger.md) on the
   same pinned result. The
   owner adjudicates its objections with evidence, then chooses corrections
   under existing authority and [test consent](../rules/no-unrequested-tests.md).
   Inside a hillclimb, skip this step; its Astra review runs once before any PR push.
   Standalone feedback ends here unless the user also requested corrections
   or iteration. Nested council returns findings to its parent, which owns
   dispatch and acceptance; it never starts another build or review loop.
7. **Recheck within budget.** Use the [review budget](../review/contract.md#review-budget).
   The panel and its challenger on one pinned result consume one shared review
   round, not one round per member or phase. Use the parent's remaining
   allowance; never start a second counter when entering council. Reserve a
   round to review a correction before dispatching it. Also stop on unavailable
   evidence. Never chase unanimity or manufacture approval because a score
   target was reached.

## Report

Return members and actual routing, rounds used, findings and dispositions,
disagreements, evidence limits, and the next action. Include the actual ratings
by member and round, or `no score` / `not run`; never fill a missing cell with
an earlier rating. Include the challenger's actual
routing and settings, verdict, objections and the owner's dispositions, or the
reason its pass was unavailable. Never count it toward provider diversity or
average its findings into panel ratings.

If a PR description update is already authorized, include the panel results
there under Council review; otherwise report in chat only. Council grants no
comment, commit, push, PR update or merge permission; use the
[shipping contract](../rules/shipping.md) for authorized shipping.

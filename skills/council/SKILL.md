---
name: council
description: Use when the user asks for a council or a panel of models to review code, compare alternatives, or give feedback.
category: Code
---

# Council

Adapted from Theo's [tstack council](https://github.com/t3dotgg/tstack/blob/1085050f3baed1ac724caa4a8166145fb2ac88af/skills/council/SKILL.md).
The parent owns the decision; delegates supply evidence and disagreements, not
write or shipping authority. Then the [Sol challenger](challenger.md) tests the
proposed conclusion, completed work and reported results.

## Panel

The panel is the models below, an explicit user selection that overrides the
tier table in
[model and effort selection](../rules/main-context.md#model-and-effort-selection)
for council members only.

| Provider | Model | Effort key | Assessment | Hillclimb rerating |
| --- | --- | --- | --- | --- |
| Claude | `claude-opus-5-5` | `effort` | `xhigh` | `high` |
| Codex | `gpt-6.1-sol` | `reasoningEffort` | `xhigh` | `high` |
| Grok | `grok-4.7` | `reasoningEffort` | `xhigh` | `high` |
| Muse | `muse-wonder-full-1.0` | `reasoningEffort` | `xhigh` | `high` |

**Assessment** is a standalone council and a hillclimb's round 0.
**Hillclimb rerating** is every later hillclimb round. All four rate in both
phases. Record the roster, model IDs and efforts in the execution context so
they survive compaction.

Never substitute a sibling (Sonnet, Haiku, Fable, Astra, Terra, Grok Fast,
Muse Wonder, Spark) or the parent's model. Set effort explicitly on every
member: Muse's catalog default is `max`, which is never allowed. In T3 Code,
start every member through `delegate_task` with `target.model` and
`target.options`, not a model request in prompt text.

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
2. **Select the panel.** Use the [panel](#panel) members and efforts for
   the phase unless the user names others for this run. Confirm each model and
   its effort option in the live catalog. Record the harness, provider, model,
   requested settings and observable effective settings. Multiple sessions of
   one model are not provider diversity. If a member cannot be reached, report
   the missing capability; never silently substitute, shrink the panel, or
   claim a full council ran.
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
   Inside a hillclimb, skip this step; its Sol review runs once before any PR push.
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

---
name: hillclimb
description: Use when the user asks to hillclimb, or to raise one UI, performance, or evaluation target to a score or goal over repeated rounds, such as "get this page to 9/10". A one-off polish, speed-up, or fix goes to task.
category: Code
---

# Hillclimb

One run improves one target through reviewed, evidenced rounds. Inside that
target nothing is off limits, including a full redesign or rewrite when the
[change size](#change-size) calls for it. The rest of the app, new doctrine and
new review axes stay out.

## Read when

- After picking the variant: its file, including its Read when list.
- Before baseline or candidate evidence: [verification](../verification/SKILL.md).
- Recording run state: [execution context](../rules/planning.md#execution-context).

## Variants

| Variant | Improves | File |
| --- | --- | --- |
| UI and experience | How a journey looks and feels to use | [variants/ui.md](variants/ui.md) |
| Performance | Speed, size, or resource use of a named path | [variants/performance.md](variants/performance.md) |
| Evaluation | Behavior against a pinned evaluator, then optionally cost or instruction size | [variants/evaluation.md](variants/evaluation.md) |

Pick one variant per run:

1. A variant the user names wins (`/hillclimb performance on checkout`).
2. Otherwise match the goal, and how the user will judge it, to each variant's
   **Picks it** section.
3. A goal that fits two variants gets one question: which runs first, with a
   recommendation for the one with the stronger evidence of cost. Offer the
   other as the next run; one run never mixes two keep bars.
4. A goal no variant fits: stop before the baseline and say so. Name the
   closest variant only as an option the user can take by restating the goal.
   Never invent a lens mid-run.

Say the chosen variant and the reason in the run's first message.

Each variant file has at least these sections: **Picks it**, **Read when**,
**Roles**, **Evidence**, **Lens**, and **Keep or reject**. A new variant is one
such file in `variants/` plus one row in the table above; the loop below does
not change.

## Change size

The lower the score, the bigger the changes. Size each round from the latest
rating, or from the distance to the target when the variant has no ratings.

## Ownership and limits

The parent owns scope, authority, round count, finding dispositions, handoffs
and final evidence.

**Who judges depends on the variant.** A scored variant (Evaluation) is judged
by its evaluator, a number and not an opinion: the parent runs it, makes the
changes, and keeps or drops each numbered change by the variant's **Keep or
reject** bar. It starts no reviewer and no council. In the Process, its
case-level results take the place of the ratings, the two lists and the
reviewer verdicts, and the parent runs the evaluator where the steps name
`/verification`.

A rated variant (UI, Performance) is judged by a **reviewer**, always a
separate agent in the [shared role](../rules/main-context.md#subagent-roles)
the variant's Roles section names. The **implementer** is the parent by
default, working in that role's lens. Delegate implementation only when the user asks or the parent's
context is too full to hold the change. If a separate reviewer is unavailable,
report the blocked workflow; never claim the independent loop ran through a
single agent.

When the user asks for a council, use [council](../council/SKILL.md) for the
reviewer slot: its assessment panel rates round 0 and its rerating panel rates
every later round. Skip the council's challenger in every round: [Sol review](../council/challenger.md)
runs once, as `/review-loop` on the final diff before any PR push. The parent
gives each read-only member the same `/verification` evidence and adjudicates
the panel's findings. Council replaces the single reviewer, not the implementer
or evidence owner.

The reviewer judges the variant's evidence, reports stable
[finding records](../review/contract.md#finding-record), and rereviews fixes.
All running of the app, browser driving, screenshots and measurements belong to
`/verification`, which the reviewer invokes in its context or receives as a
fresh evidence handoff. The implementer changes only the parent-promoted
finding set and records its bounded diff and checks; a delegated implementer
does not gather evidence or dispatch another loop. No scoped edits while review runs.

Budget: the shared [review budget](../review/contract.md#review-budget),
where a user's explicit budget or hard cap wins. Hillclimb differences: charge
a round at dispatch, including dropped changes and failed or replaced review
attempts. One implementation batch belongs to the current round; restarting or
replacing it consumes another round. Reserve a remaining round to review a
correction before dispatching it. Carry spent allowance across delegates,
retries, resume and rejected changes.

## Process

1. **Bound the target.** Pin
   baseline revision, working/index changes and
   owners. Name the target, the conditions the variant's Evidence section
   requires, and success and regression criteria. Default to scoped autonomous
   corrections within this invocation; honor proposal-first or narrower
   authority. In proposal-first, show findings and the round's proposed
   changes, then wait for approval before implementation. When ratings are
   used, record the user's target score and acceptable floor (such as 10, 9.5
   acceptable) as a stop condition; without one, the budget and keep bar
   decide. Never infer merge, deployment, external communications or unrelated
   redesign permission.
2. **Round 0: assess the current state.** The reviewer, or the council's
   assessment panel, gets baseline evidence through `/verification` on a safe
   target, as the variant's Evidence section defines, and rates it against a
   rubric frozen for the run. Every later round is compared against that
   rating.
   Preserve repository Playwright, benchmark and CI checks. When a capture
   route fails, try the next permitted one (for UI in T3 Code, the preview
   tools, then a direct capture from the running server) before calling
   evidence blocked. Round 0 settles one capture command, preferring a capture
   script the repository already has, and records it in the execution context;
   every later round reuses it. Drop a route for the run after it times out
   twice. If evidence stays blocked, report inconclusive or static-only
   findings and stop the affected loop; never bypass restrictions or invent a
   pass.

   **After every blind rating**, this round and each later one, give the
   reviewer the target score and ask for two short lists, sized by
   [change size](#change-size): up to three things that drive its rating down,
   each with evidence (where, and what it costs the user), and up to three
   changes that would raise it most, each with the expected effect. The parent
   merges the lists across reviewers and ranks them by agreement and impact.
3. **Promote the round's changes.** The parent selects the highest-ranked
   items from the merged lists, checks their evidence, and states an observable
   improvement hypothesis for each. Reuse stable IDs and remediate once. The
   implementer makes them as **numbered changes** at the round's
   [change size](#change-size), each undoable on its own, and records which
   files and hunks belong to each number. The same numbers label the
   highlighted before/after. Give a delegated implementer allowed paths,
   unchanged behavior, evidence, rollback boundary and checks. Use existing
   tests; a new one needs [test consent](../rules/no-unrequested-tests.md).
   Never run `/task` or a whole `/review-loop` per correction.
4. **Compare and rereview.** Freeze the candidate diff. `/verification` gathers
   candidate evidence under the same conditions as the baseline. Then the
   reviewer checks named fixes, direct regressions and the variant's guards,
   reviewing new surface under the shared partition, then rates the result
   blind and returns the two lists from step 2. Make no claim the variant's Evidence section rules out.
5. **The reviewers decide each change.** Every reviewer, or council member,
   gives each numbered change a verdict: **keep**, **fix** (with the defect
   and its evidence) or **drop** (with the reason). The parent tallies them
   and checks the evidence behind each fix or drop:
   - Most say keep, and no one shows an evidenced break of the variant's keep
     bar or guards: keep it.
   - Anyone shows such a break: fix it forward in this round, then the members
     who raised it recheck it on fresh `/verification` evidence. Drop it if
     the fix fails that recheck. A majority never overrides the evidence.
   - Most say drop: undo only that change.
   - A tie: the parent decides and states why; dissent stays in the report.

   A round is never discarded as a whole. The rechecks belong to the current
   round, so the final round may fix forward too. When the variant's evidence
   cannot separate the changes (one measurement for the whole round), the round
   is one change. Undo only a dropped change's owned hunks, including partial
   delegated changes, preserving accepted work and user edits. Never hard-reset
   or restore whole files over unrelated work. Concurrent changes invalidate
   affected evidence: reconcile before writing or reversing, and stop if
   ownership cannot be separated.
   A blocked comparison is inconclusive, not an improvement. Keep an unverified
   change only on explicit user direction and report that limit.
6. **Stop and hand off.** Stop at the scoped outcome or target score, budget
   exhaustion, no worthwhile evidenced improvement, stalled dispute or blocker.
   Report the variant, rounds used, a rating table by member and round with
   the change from round 0, each numbered change with its verdicts and outcome
   (kept, fixed, dropped), stable unresolved findings,
   comparable evidence, limitations, remaining candidate changes and next
   decision. Never claim a perfect/pristine pass because the budget ended.
7. **Review loop before any PR push.** Before any push, including one the
   user asks for mid-run, pass the [review loop gate](../rules/shipping.md#review-loop-gate)
   on the final diff with this run's correction authority. It is the run's only
   Sol review and has its own round budget. Pushing still needs
   [shipping authorization](../rules/shipping.md); never merge or deploy
   automatically.

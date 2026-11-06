---
name: hillclimb
description: Use only when the user types /hillclimb or explicitly asks to hillclimb one scoped UI, performance, or evaluation target over a finite round budget. Never start it for ordinary polish, speed-up, or skill-editing requests; those go to task.
category: Code
disable-model-invocation: true
---

# Hillclimb

User start only, by name in the thread. Creating or discussing this skill does
not authorize edits to an application. One run improves one target through
reviewed, evidenced rounds. Inside that target nothing is off limits, including
a full redesign or rewrite when the [change size](#change-size) calls for it.
The rest of the app, new doctrine and new review axes stay out.

## Read when

Read these once per run. After a context compaction, reread only what is no
longer in context, not the whole list each round.

- Every run: [code quality](../rules/code-quality.md),
  [code structure](../rules/code-structure.md), and the chosen
  [variant](#variants) file, including its Read when list.
- Before delegation: [role/model/effort routing](../rules/main-context.md#subagent-roles)
  and [delegation lifecycle](../rules/main-context.md#delegation-lifecycle).
- Baseline or candidate evidence: [verification](../verification/SKILL.md)
  and [harness-first tools](../rules/tooling.md#harness-first-discovery).
- Ownership and evidence: [execution context](../rules/planning.md#execution-context),
  [handoffs](../rules/execution.md#handoffs-and-evidence),
  [remediation](../rules/execution.md#remediation), and
  [review modes/budget](../review/contract.md#review-budget).
- Replies and decisions: [Plain language](../rules/writing-style.md#plain-language)
  and [Asking the user](../rules/writing-style.md#asking-the-user).

## Variants

| Variant | Improves | File |
| --- | --- | --- |
| UI and experience | How a journey looks and feels to use: alignment, hierarchy, clutter, friction, states | [variants/ui.md](variants/ui.md) |
| Performance | Speed, size, or resource use of a named path: load time, latency, throughput, bundle size, memory, query or build time | [variants/performance.md](variants/performance.md) |
| Evaluation | Behavior against a pinned evaluator, optionally followed by reducing cost or instruction size while preserving its requirements | [variants/evaluation.md](variants/evaluation.md) |

Pick one variant per run:

1. A variant the user names wins (`/hillclimb performance on checkout`).
2. Otherwise match the goal, and how the user will judge it, to each variant's
   **Picks it** section. "Feels cramped" or "too many clicks" is UI; "slow",
   "p95" or "bundle too big" is Performance. Passing behavioral cases, choosing
   tools correctly, or shrinking instructions while preserving eval results is
   Evaluation.
3. A goal that fits two variants gets one question: which runs first, with a
   recommendation for the one with the stronger evidence of cost. Offer the
   other as the next run; one run never mixes two keep bars.
4. A goal no variant fits: stop before the baseline and say so. Name the
   closest variant only as an option the user can take by restating the goal.
   Never run the closest variant anyway or invent a lens mid-run.

Say the chosen variant and the reason in the run's first message.

Each variant file has the same sections: **Picks it**, **Read when**,
**Roles**, **Evidence**, **Lens**, and **Keep or reject**. A new variant is one
file in `variants/` with those sections plus one row in the table above; the
loop below does not change.

## Change size

The lower the score, the bigger the changes often need to be. Size each round
from the latest rating, or from the distance to the target when the variant
has no ratings.

## Ownership and limits

The parent owns scope, authority, round count, finding dispositions, handoffs
and final evidence. The **reviewer** is always a separate agent in the
[shared role](../rules/main-context.md#subagent-roles) the variant's Roles
section names; independence comes from the reviewer. The **implementer** is the
parent by default, working in that role's lens; switching the parent's model
switches the implementer. Delegate implementation only when the user asks or
the parent's context is too full to hold the change. If a separate reviewer is
unavailable, report the blocked workflow; do not claim the requested
independent loop ran through a single agent.

When the user asks for a council, use [council](../council/SKILL.md) for the
reviewer slot: its assessment panel rates round 0 and its rerating panel rates
every later round. Skip the council's challenger in every round: Sol review
runs once, as `/review-loop` on the final diff before any PR push. The parent
supplies the
same `/verification` evidence to each read-only member and adjudicates the
panel's findings. Council replaces the single reviewer, not the implementer or
evidence owner. Reuse the parent round counter and the chosen variant's keep
bar; do not launch nested review loops. Without a council request, retain the
single reviewer.

The reviewer judges the variant's evidence, reports stable
[finding records](../review/contract.md#finding-record), and rereviews fixes.
All running of the app, browser driving, screenshots and measurements belong to
`/verification`, which the reviewer invokes in its context or receives as a
fresh evidence handoff. This keeps the reviewer informed by real runs without
bypassing that ownership. The implementer changes only the parent-promoted
finding set and records its bounded diff and checks; a delegated implementer
does not gather evidence or dispatch another loop. No scoped edits while review runs.

Default budget: **five review rounds**, including initial review and focused
rereviews. This is configurable, not a user-chosen number. Charge a round at
dispatch, including dropped changes and failed/replaced review attempts.
One implementation batch belongs to the current round; restarting/replacing
that batch consumes another round. Reserve a remaining round to review its
result before dispatching a correction. Carry spent allowance across delegates,
retries, resume and rejected changes. Use the shared budget's stopping and
user-approved continuation rules; never reset it by changing agents or skills.

## Process

1. **Bound the target.** Reuse the user's outcome, scope and decisions. Pick the
   [variant](#variants). Pin baseline revision, working/index changes and
   owners. Name the target, the conditions the variant's Evidence section
   requires, and success and regression criteria. Default to scoped autonomous
   corrections within this invocation; honor proposal-first or narrower
   authority. In proposal-first, show findings and the round's proposed
   changes, then wait for approval before implementation. When ratings are used, record the
   user's target score and acceptable floor (such as 10, 9.5 acceptable) as a
   stop condition; without one, the budget and keep bar decide. Do not infer merge, deployment, external
   communications or unrelated redesign permission.
2. **Round 0: assess the current state.** The reviewer, or the council's
   assessment panel, gets baseline evidence through `/verification` on a safe
   target, as the variant's Evidence section defines, and rates it against a
   rubric frozen for the run. That rating is the baseline every later round is
   compared against. Reuse running services and logs and the user's open page
   or server. Preserve repository Playwright, benchmark and CI checks. When a
   capture route fails, try the next permitted one (for UI in T3 Code, the
   preview tools, then a direct capture from the running server) before calling
   evidence blocked. Round 0 settles one capture command, preferring a capture
   script the repository already has, and records it in the execution context;
   every later round reuses it. Drop a route for the run after it times out
   twice. If it is still blocked, report inconclusive/static-only
   findings and stop the affected loop; do not bypass restrictions or invent a
   pass. Apply the
   variant's Lens to the bounded target, not the whole app. Ask each reviewer
   for the moves it would take to reach the target score, sized by
   [change size](#change-size), not only for defects.
3. **Promote the round's changes.** The parent selects the highest-impact
   evidenced findings and an observable improvement hypothesis for each. Reuse
   stable IDs and remediate once. The implementer makes them as **numbered
   changes** at the round's [change size](#change-size), each undoable on its
   own, and records which files and hunks belong to each number. The same
   numbers label the highlighted before/after. Give a delegated implementer
   allowed paths, unchanged behavior, evidence, rollback boundary and checks.
   Use existing tests, and preserve
   [new-test consent](../rules/no-unrequested-tests.md). Do not recursively run
   `/task` or a whole `/review-loop` for every correction.
4. **Compare and rereview.** Freeze the candidate diff. `/verification` gathers
   candidate evidence under the same conditions as the baseline. Then the
   reviewer checks named fixes, direct regressions and the variant's guards,
   reviewing new surface under the shared partition. Full rescans require
   material scope change or explicit request. Distinguish observation, judgment
   and unknowns; make no claim the variant's Evidence section rules out.
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

   A round is never discarded as a whole; kept changes stay while dropped ones
   go. The rechecks belong to the current round, so the final round may fix
   forward too. When the variant's evidence cannot separate the changes (one
   measurement for the whole round), the round is one change. Undo safely:
   only a dropped change's owned hunks, including partial delegated changes,
   preserving accepted work and user edits. Never hard-reset or restore whole
   files over unrelated work. Concurrent changes invalidate affected evidence:
   reconcile before writing/reversing, and stop if ownership cannot be separated.
   A blocked comparison is inconclusive, not an improvement. Keep an unverified
   change only on explicit user direction and report that limit.
6. **Stop and hand off.** Stop at the scoped outcome or target score, budget
   exhaustion, no worthwhile evidenced improvement, stalled dispute or blocker.
   Report the variant, rounds used, a rating table by member and round with
   the change from round 0, each numbered change with its verdicts and outcome
   (kept, fixed, dropped), stable unresolved findings,
   comparable evidence, limitations, remaining candidate changes and next
   decision. Never claim a perfect/pristine pass because the budget ended.
7. **Review loop before any PR push.** Before the run's changes are pushed,
   pass the [review loop gate](../rules/shipping.md#review-loop-gate)
   automatically on the final diff, with this run's correction authority. It
   is the only Sol review for the whole run and has its own round budget. A
   push the user asks for mid-run passes it first. Pushing still needs
   [shipping authorization](../rules/shipping.md); no automatic merge or deploy.

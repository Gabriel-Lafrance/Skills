---
name: hillclimb
description: Run only when the user explicitly invokes hillclimb to improve one scoped target, such as a UI journey or a slow path, through separate reviewer and implementation agents. Picks the variant (UI and experience, or performance) from the goal, owns a finite round budget, and keeps only changes the evidence supports. Never auto-starts for ordinary UI or speed-up work.
category: Code
disable-model-invocation: true
---

# Hillclimb

User start only, by name in the thread. Creating or discussing this skill does
not authorize edits to an application. One run improves one target through
reviewed, evidenced rounds; it is not a new doctrine, a general redesign, a
rewrite, or a new review axis.

## Read when

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

Pick one variant per run:

1. A variant the user names wins (`/hillclimb performance on checkout`).
2. Otherwise match the goal, and how the user will judge it, to each variant's
   **Picks it** section. "Feels cramped" or "too many clicks" is UI; "slow",
   "p95" or "bundle too big" is Performance.
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

## Ownership and limits

The parent owns scope, authority, round count, finding dispositions, handoffs
and final evidence. Use separate agents: a **reviewer** and an **implementer**,
in the [shared roles](../rules/main-context.md#subagent-roles) the variant's
Roles section names. Select supported provider/model/effort per job, not
hardcoded models. If separate agents are unavailable, report the blocked
workflow; do not claim the requested independent loop ran through a single
agent.

The reviewer judges the variant's evidence, reports stable
[finding records](../review/contract.md#finding-record), and rereviews fixes.
All running of the app, browser driving, screenshots and measurements belong to
`/verification`, which the reviewer invokes in its context or receives as a
fresh evidence handoff. This keeps the reviewer informed by real runs without
bypassing that ownership. The implementer changes only the parent-promoted
finding set, returns its bounded diff and checks, and does not gather evidence
or dispatch another loop. No scoped edits while review runs.

Default budget: **three review rounds**, including initial review and focused
rereviews. This is configurable, not a user-chosen number. Charge a round at
dispatch, including rejected candidates and failed/replaced review attempts.
One implementation batch belongs to the current round; restarting/replacing
that batch consumes another round. Reserve a remaining round to review its
result before dispatching a correction. Carry spent allowance across delegates,
retries, resume and rejected changes. Use the shared budget's stopping and
justified finite-extension rules; never reset it by changing agents or skills.

## Process

1. **Bound the target.** Reuse the user's outcome, scope and decisions. Pick the
   [variant](#variants). Pin baseline revision, working/index changes and
   owners. Name the target, the conditions the variant's Evidence section
   requires, and success and regression criteria. Default to scoped autonomous
   corrections within this invocation; honor proposal-first or narrower
   authority. In proposal-first, show findings and a focused fix, then wait for
   its approval before implementation. Do not infer merge, deployment, external
   communications or unrelated redesign permission.
2. **Baseline and review.** The reviewer gets baseline evidence through
   `/verification` on a safe target, as the variant's Evidence section defines,
   reusing supported services/logs and preferring suitable permitted harness
   tools. Preserve repository Playwright, benchmark and CI checks. If required
   evidence is blocked, report inconclusive/static-only findings and stop the
   affected loop; do not bypass restrictions or invent a pass. Apply the
   variant's Lens to the bounded target, not the whole app.
3. **Promote one focused correction.** The parent selects the highest-impact
   evidenced finding/root cause and an observable improvement hypothesis.
   Reuse stable IDs and remediate once. Give the separate implementer allowed
   paths, unchanged behavior, evidence, rollback boundary and checks. Use
   existing tests, and preserve
   [new-test consent](../rules/no-unrequested-tests.md). Do not recursively run
   `/task` or a whole `/review-loop` for every correction.
4. **Compare and rereview.** Freeze the candidate diff. `/verification` gathers
   candidate evidence under the same conditions as the baseline. Then the
   reviewer checks named fixes, direct regressions and the variant's guards,
   reviewing new surface under the shared partition. Full rescans require
   material scope change or explicit request. Distinguish observation, judgment
   and unknowns; make no claim the variant's Evidence section rules out.
5. **Keep or reject.** Retain a correction only when evidence supports its
   hypothesis, it meets the variant's keep bar, and required regression checks
   pass. Otherwise safely undo only
   that candidate's owned changes, including its partial delegated changes,
   preserving accepted work and user edits. Never hard-reset or restore whole
   files over unrelated work. Concurrent changes invalidate affected evidence:
   reconcile before writing/reversing, and stop if ownership cannot be separated.
   A blocked comparison is inconclusive, not an improvement. Keep an unverified
   candidate only on explicit user direction and report that limit.
6. **Stop and hand off.** Stop at the scoped outcome, budget exhaustion, no
   worthwhile evidenced improvement, stalled dispute or blocker. Report the
   variant, rounds used, kept/rejected changes, stable unresolved findings,
   comparable evidence, limitations, remaining candidate changes and next
   decision. Never claim a perfect/pristine pass because the budget ended.
   Shipping follows existing [authorization and gates](../rules/shipping.md);
   no automatic merge/deploy.

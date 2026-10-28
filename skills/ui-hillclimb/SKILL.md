---
name: ui-hillclimb
description: Run only when the user explicitly invokes ui-hillclimb to iteratively improve a scoped UI journey through separate visual-and-experience reviewer and implementation agents. Own a finite review/correction budget and compare rendered flows through verification; do not auto-start for ordinary UI work.
category: Design
disable-model-invocation: true
---

# UI hillclimb

User start only, by name in the thread. Creating or discussing this skill does
not authorize edits to an application. This is a review-and-correction loop,
not a new UX doctrine, a general redesign, or a new review axis.

## Read when

- Every run: [code quality](../rules/code-quality.md),
  [code structure](../rules/code-structure.md),
  [user experience](../rules/user-experience.md), and existing `docs/design.md`.
  Reuse components/tokens, brand and interaction constraints, including the
  [no-obvious-copy rule](../rules/user-experience.md#dont-tell-the-obvious):
  do not add unnecessary heading subtitles.
- Before delegation: [role/model/effort routing](../rules/main-context.md#subagent-roles)
  and [delegation lifecycle](../rules/main-context.md#delegation-lifecycle).
- Live baseline or candidate evidence: [verification](../verification/SKILL.md)
  and [harness-first tools](../rules/tooling.md#harness-first-discovery).
- Ownership and evidence: [execution context](../rules/planning.md#execution-context),
  [handoffs](../rules/execution.md#handoffs-and-evidence),
  [remediation](../rules/execution.md#remediation), and
  [review modes/budget](../review/contract.md#review-budget).
- Replies and decisions: [Plain language](../rules/writing-style.md#plain-language)
  and [Asking the user](../rules/writing-style.md#asking-the-user).

## Ownership and limits

The parent owns scope, authority, round count, finding dispositions, handoffs
and final evidence. Use separate agents: a **visual-and-experience reviewer**
(the shared reviewer role) and an **implementer** (the shared designer role for
UI code). Select supported provider/model/effort per job, not hardcoded models.
If separate agents are unavailable, report the blocked workflow; do not claim
the requested independent loop ran through a single agent.

The reviewer evaluates actual rendered actions, states and continuations,
reports stable [finding records](../review/contract.md#finding-record), and
rereviews fixes. It inspects rendered views or captured images alongside
action/result observations; text-only summaries do not establish visual polish.
All manual browser driving and screenshots belong to
`/verification`, which the reviewer invokes in its context or receives as a
fresh evidence handoff. This keeps the reviewer informed by rendered flows
without bypassing browser ownership. The implementer changes only the parent-
promoted finding set, returns its bounded diff and checks, and does not drive
the browser or dispatch another loop. No scoped edits while review runs.

Default budget: **three review rounds**, including initial review and focused
rereviews. This is configurable, not a user-chosen number. Charge a round at
dispatch, including rejected candidates and failed/replaced review attempts.
One implementation batch belongs to the current round; restarting/replacing
that batch consumes another round. Reserve a remaining round to review its
result before dispatching a correction. Carry spent allowance across delegates,
retries, resume and rejected changes. Use the shared budget's stopping and
justified finite-extension rules; never reset it by changing agents or skills.

## Process

1. **Bound the journey.** Reuse the user's outcome, scope and decisions. Pin
   baseline revision, working/index changes and owners. Name the journey,
   relevant data/viewports/states, success and regression criteria. Default to
   scoped autonomous corrections within this invocation; honor proposal-first
   or narrower authority. In proposal-first, show findings and a focused fix,
   then wait for its approval before implementation. Do not infer merge,
   deployment, external communications or unrelated redesign permission.
2. **Observe and review.** The reviewer invokes `/verification` for baseline
   live evidence on a safe target, reusing supported services/logs and preferring
   suitable permitted harness tools. Preserve repository Playwright/CI checks.
   If required browser evidence is blocked, report inconclusive/static-only
   findings and stop the affected loop; do not bypass restrictions or invent a
   visual pass. Apply the lens below to the observed journey, not the whole app.
3. **Promote one focused correction.** The parent selects the highest-impact
   evidenced friction/root cause and an observable improvement hypothesis.
   Reuse stable IDs and remediate once. Give the separate implementer allowed
   paths, unchanged behavior, evidence, rollback boundary and checks. Apply
   [design initialization/blending](../rules/user-experience.md#initialization)
   when needed; use existing tests, and preserve
   [new-test consent](../rules/no-unrequested-tests.md). Do not recursively run
   `/task` or a whole `/review-loop` for every correction.
4. **Compare and rereview.** Freeze the candidate diff. `/verification` records
   action/result evidence under comparable data, viewport, build and meaningful
   states, including touched keyboard/focus, responsive, loading/empty/error,
   cancel/retry and continuation paths. Then the reviewer checks named fixes
   and direct regressions, reviewing new surface under the shared partition.
   Full rescans require material scope change or explicit request. No invented
   numerical UX score, real-user preference or conversion claim from screenshots
   or reviewer opinion; distinguish observation, design judgment and unknowns.
5. **Keep or reject.** Retain a correction only when evidence supports the
   hypothesis and required regression checks pass. Otherwise safely undo only
   that candidate's owned changes, including its partial delegated changes,
   preserving accepted work and user edits. Never hard-reset or restore whole
   files over unrelated work. Concurrent changes invalidate affected evidence:
   reconcile before writing/reversing, and stop if ownership cannot be separated.
   A blocked comparison is inconclusive, not an improvement. Keep an unverified
   candidate only on explicit user direction and report that limit.
6. **Stop and hand off.** Stop at the scoped outcome, budget exhaustion, no
   worthwhile evidenced improvement, stalled dispute or blocker. Report rounds
   used, kept/rejected changes, stable unresolved findings, comparable evidence,
   limitations, remaining candidate changes and next decision. Never claim a
   perfect/pristine pass because the budget ended. Shipping follows existing
   [authorization and gates](../rules/shipping.md); no automatic merge/deploy.

## Visual and experience lens

Judge a premium, sleek, comfortable result within the product's own identity:

- Alignment, consistent spacing/padding, typography and hierarchy: cite the
  affected rendered state and task impact rather than imposing a new aesthetic.
- Restrained surfaces and grouping: flag nested-card clutter without deleting
  meaningful structure or expert capability.
- No new modals unless the user asks. Flag friction in existing modals and scope
  any change; preserve necessary confirmation/recovery flows.
- Clean transitions and icon-state changes that explain state. Preserve
  responsiveness and reduced motion; avoid decorative animation overload.
- Comfortable keyboard/focus, readable states, overflow and responsive layouts;
  preserve data and continuity through loading, error, empty, cancel and retry.
- Preserve meaningful behavior, accessibility and developer/agent experience.
  A prettier screenshot does not excuse a harder task or a hidden regression.

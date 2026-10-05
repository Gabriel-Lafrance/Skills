# Shared execution contracts

`/task`, `/task-with-tests`, and `/gabriel-mode` own their distinct build order. This file owns their common intake, handoff, remediation, and completion rules. It creates no extra phase, artifact, or agent.

## Git sync only

A request to fetch, merge main into a working branch, or otherwise synchronize
Git state is operational work, not a feature build. It does not start grilling,
planning, test proposals, or automatic review/verification subagents, even on a
branch with an open PR. An explicitly requested review, verification, or build
still follows its selected route.

Confirm the intended branch and incoming ref, inspect status, and preserve
unrelated working/index changes. Record the before and incoming revisions.
Use ordinary safe Git operations; no automatic discard, force push, protected
branch commit, or hook bypass. After incorporation, inspect the resulting Git
state, confirm the requested revision is included, and check for unresolved
conflicts and unexpected changes. A clean local sync then stops. Report what
was incorporated and that application behavior was not tested.

If conflict resolution changes meaningful behavior, inspect the resolved paths
and their consumers and apply [verification scope](#verification-scope) to that
resolution, not automatically the entire branch. Escalate for shared/high-risk
effects or uncertainty. Purely mechanical conflicts need only applicable
structural checks. Shipping, explicit user checks, and repository-mandated
local hooks/checks remain applicable when requested or required.

## Verification scope

Select checks from changed behavior, contracts, dependency reach, failure cost,
and uncertainty. File count, diff size, or a label such as "small bug" cannot
establish low risk. Use known entry points, callers, suites, and CI requirements;
research uncertainty before narrowing. Choose the scope yourself within the
request and rules, with a short reason, not a mandatory user questionnaire.

| Work and actual impact | Applicable evidence |
| --- | --- |
| Clean operational Git sync | Git safety, incorporation, conflict/status checks; stop under [Git sync only](#git-sync-only) |
| Meaningful conflict resolution | Resolved behavior and relevant consumers/tests/checkers; widen for shared effects |
| Localized bug with bounded consumers | Reproduce/check the changed behavior, relevant existing tests, and affected lint/type checks when configured; check direct regressions |
| Docs/copy/types/config | Links, syntax, rendering or consuming checks as relevant; types/config can have broad runtime or consumer impact, so inspect that reach |
| Auth, permissions, money, shared infrastructure/contracts, schema or migration | Broader integration and affected consumer/failure/recovery checks; full suites when coupling or uncertainty warrants them |
| Explicit request for full verification/all suites | Inventory and run every configured suite requested, reporting unavailable checks; do not silently substitute a narrow pass |

Run existing checks with supported package/path/project selection when it
preserves their meaning. If a checker cannot be scoped safely, use its standard
command or disclose the gap; do not invent unsupported filters. Expand after
failures or newly discovered shared impact. Required repository checks,
security rules, hooks, and remote CI still apply; scope selection never waives
them or changes CI/branch protection. Running existing tests needs no new-test
consent; writing or changing tests still follows no-unrequested-tests.md.

Reuse evidence only when the relevant code, contracts, dependencies, command,
build, configuration, and environment remain valid. A new merge/revision can
invalidate relevant evidence; a different SHA alone does not invalidate checks
of unchanged independent behavior. Explain retained evidence and recheck affected
claims under [handoffs and evidence](#handoffs-and-evidence). Report actual checks
and results, reused evidence, omitted/unavailable scope and reasons. A focused
pass proves its bounded claim, not all application behavior or unrun suites.

## Ready-ticket preflight

First classify operational sync under [Git sync only](#git-sync-only); it stops
there rather than entering ticket execution. A build uses the preflight below.

Read the requested ticket and prerequisite contracts, current Git state, relevant code and governing rules. Apply the [fresh-executor readiness bar](../write-ticket/doctrine.md#fresh-executor-handoff) to the work being executed. This reuses readiness criteria; it does not rerun the authoring checker or preparation session. Verify live entry points, schemas, callers, dependency bases and other facts needed for its items; preparation evidence is a pointer, not proof that the repository has not changed.

Reuse settled intent, technical choices, meaningful exclusions, and explicit test acceptances or refusals with their decision sources. Preserve exact agreed signatures, types, payloads, examples, and values in their canonical contract blocks through execution and handoffs, with their rationale and constraints. Proposed tests are not accepted tests. Keep the same acceptance and rule IDs when taking over a ticket or child. Research factual gaps and own routine implementation details. Ask through `/grill-me` only about newly discovered material user choices; pause affected work while they remain open. A changed repository fact alone is not a reason to repeat the interview.

When the ticket is ready, announce or reuse its current lock and proceed in the selected route. Do not restart `/write-ticket`, require a fresh Questions batch, or require the user to say `skip grill`. For an unprepared request, settle only the missing consequential decisions before planning. Keep Questions and Locked in in separate messages under [Asking the user](writing-style.md#asking-the-user). The selected route still owns test timing; no route can reinterpret a refusal or change an accepted assertion without the user's decision.

## Handoffs and evidence

For touched user flows, carry the settled [interaction contract](../write-ticket/reference.md#plan) into the relevant slice and handoff: entry context, carried data, result/continuation, recovery, and component reuse. Revalidate those facts under [action and continuation](user-experience.md#action-and-continuation). Completion evidence must cover the meaningful continuation, not merely a control opening. Backend-only work adds no UX ceremony.

The active orchestrator owns the outcome, decomposition, acceptance and next action. A nested skill returns its requested evidence or decision update to that owner; it does not start another complete lifecycle, select a new route, ship, or demand a standalone output template.

Use the existing [execution context](planning.md#execution-context) and [slice contract](../task/reference.md#inline-plan-contract). Each handoff carries only what its receiver needs: outcome and item/acceptance IDs, slice and owner, dependency contracts, allowed paths and exclusions, current decisions and test consent sources, governing rule paths, Done when, and the exact question or action. Pin the base, current revision and working-diff boundary, including pre-existing changes; a commit alone does not identify uncommitted work.

Return the bounded contribution, stable finding IDs, checks and evidence IDs tied to acceptance IDs, actual checked revision/diff and environment, result, and concrete blockers. Reuse IDs across fixes so old and new evidence can be compared; do not rename an unresolved finding into a new success. This is an in-chat handoff, not a required registry.

For the selected route's combined review, use the [fresh review context](../review/contract.md#fresh-combined-review-context). Preserve its existing gate order and implementer constraints; the focused reviewer does not add a per-slice gate or acquire remediation ownership.

After a change, identify which claims depend on changed code, contracts, dependencies, fixtures or environment. Invalidate that evidence and recheck the affected claims and seams. Explain why any retained evidence still applies. A scoped remediation review covers named findings, touched paths and direct regressions; broaden it when the fix changes another contract or scope. Scoped re-review never replaces whole-result acceptance. Final acceptance covers the combined result with applicable checks selected under [verification scope](#verification-scope), including valid retained evidence; an earlier pass cannot certify affected later edits.

## Remediation

Review owns stable findings and their evidence. The active orchestrator alone adjudicates them, maintains the fix backlog, and dispatches work. Standalone `/review` stops after its findings unless fixes were requested.

For an actionable finding set, the orchestrator requests `/analyze` review-remediation once when cause, impact or correction needs investigation, reusing an existing adequate analysis rather than triggering a second dispatch from review. Promote the selected set once for the current evidence and fix decision, explicitly naming finding IDs with their correction, touch surface, non-goals, acceptance and owner under the user's existing authorization. If that authorization does not cover fixes, ask before implementing. New scope, waivers and changed test assertions still need the user's decision.

Fix mode is a bounded slice of the current outcome. Prefer the smallest authoritative correction; no new product discovery, optional cleanup or test suggestion. Return findings to their responsible worker where the selected route uses workers. Recheck under [Handoffs and evidence](#handoffs-and-evidence), then the route's gate order. Reanalyze only when new evidence or a failed approach changes the diagnosis. A blocked or declined required fix stays blocking unless the user explicitly waives it by name.

Under existing authorization, deliver the corrected artifact with renewed evidence before handing the result to human review. A list of actionable comments is not completion of an authorized fix. Report findings outside authorization or blocked by a required decision explicitly; do not silently implement them or call them resolved.

## Recovery and completion

On resume, use the [context authority order](planning.md#authority), inspect actual Git state and live prerequisite contracts, recover settled user decisions with their sources, and reconcile current slice/finding status. A saved process record is a coordination aid, not authority or proof. Preserve unrelated changes and invalidate stale evidence before continuing.

Complete only when every applicable acceptance item, test decision, review finding and required check is accounted for on the final result. Report passed, failed, inconclusive and unrun checks separately, with the checked revision/diff, evidence and any named user waiver. Missing access or infrastructure is a blocker, not a pass. Repeated failure requires reassessing the approach; pause affected work when a new user decision or prerequisite is needed.

Use the [completion summary](../task/reference.md#completion-summary). The parent keeps ticket, branch and shipping ownership when delegated. Shipping always follows separate existing authorization and [shipping.md](shipping.md); completion grants none.

# Shared execution contracts

`/task`, `/task-with-tests`, and `/gabriel-mode` own their distinct build order. This file owns their common intake, handoff, remediation, and completion rules. It creates no extra phase, artifact, or agent.

## Ready-ticket preflight

Read the requested ticket and prerequisite contracts, current Git state, relevant code and governing rules. Apply the [fresh-executor readiness bar](../write-ticket/doctrine.md#fresh-executor-handoff) to the work being executed. This reuses readiness criteria; it does not rerun the authoring checker or preparation session. Verify live entry points, schemas, callers, dependency bases and other facts needed for its items; preparation evidence is a pointer, not proof that the repository has not changed.

Reuse settled intent, technical choices, meaningful exclusions, and explicit test acceptances or refusals with their decision sources. Proposed tests are not accepted tests. Keep the same acceptance and rule IDs when taking over a ticket or child. Research factual gaps and own routine implementation details. Ask through `/grill-me` only about newly discovered material user choices; pause affected work while they remain open. A changed repository fact alone is not a reason to repeat the interview.

When the ticket is ready, announce or reuse its current lock and proceed in the selected route. Do not restart `/write-ticket`, require a fresh Questions batch, or require the user to say `skip grill`. For an unprepared request, settle only the missing consequential decisions before planning. Keep Questions and Locked in in separate messages under [Asking the user](writing-style.md#asking-the-user). The selected route still owns test timing; no route can reinterpret a refusal or change an accepted assertion without the user's decision.

## Handoffs and evidence

The active orchestrator owns the outcome, decomposition, acceptance and next action. A nested skill returns its requested evidence or decision update to that owner; it does not start another complete lifecycle, select a new route, ship, or demand a standalone output template.

Use the existing [execution context](planning.md#execution-context) and [slice contract](../task/reference.md#inline-plan-contract). Each handoff carries only what its receiver needs: outcome and item/acceptance IDs, slice and owner, dependency contracts, allowed paths and exclusions, current decisions and test consent sources, governing rule paths, Done when, and the exact question or action. Pin the base, current revision and working-diff boundary, including pre-existing changes; a commit alone does not identify uncommitted work.

Return the bounded contribution, stable finding IDs, checks and evidence IDs tied to acceptance IDs, actual checked revision/diff and environment, result, and concrete blockers. Reuse IDs across fixes so old and new evidence can be compared; do not rename an unresolved finding into a new success. This is an in-chat handoff, not a required registry.

After a change, identify which claims depend on changed code, contracts, dependencies, fixtures or environment. Invalidate that evidence and recheck the affected claims and seams. Explain why any retained evidence still applies. A scoped remediation review covers named findings, touched paths and direct regressions; broaden it when the fix changes another contract or scope. Scoped re-review never replaces whole-result acceptance. Final verification must cover the final combined tree, including all configured suites and applicable real-path checks; an earlier pass cannot certify later edits.

## Remediation

Review owns stable findings and their evidence. The active orchestrator alone adjudicates them, maintains the fix backlog, and dispatches work. Standalone `/review` stops after its findings unless fixes were requested.

For an actionable finding set, the orchestrator requests `/analyze` review-remediation once when cause, impact or correction needs investigation, reusing an existing adequate analysis rather than triggering a second dispatch from review. Promote the selected set once for the current evidence and fix decision, explicitly naming finding IDs with their correction, touch surface, non-goals, acceptance and owner under the user's existing authorization. If that authorization does not cover fixes, ask before implementing. New scope, waivers and changed test assertions still need the user's decision.

Fix mode is a bounded slice of the current outcome. Prefer the smallest authoritative correction; no new product discovery, optional cleanup or test suggestion. Return findings to their responsible worker where the selected route uses workers. Recheck under [Handoffs and evidence](#handoffs-and-evidence), then the route's gate order. Reanalyze only when new evidence or a failed approach changes the diagnosis. A blocked or declined required fix stays blocking unless the user explicitly waives it by name.

## Recovery and completion

On resume, use the [context authority order](planning.md#authority), inspect actual Git state and live prerequisite contracts, recover settled user decisions with their sources, and reconcile current slice/finding status. A saved process record is a coordination aid, not authority or proof. Preserve unrelated changes and invalidate stale evidence before continuing.

Complete only when every applicable acceptance item, test decision, review finding and required check is accounted for on the final result. Report passed, failed, inconclusive and unrun checks separately, with the checked revision/diff, evidence and any named user waiver. Missing access or infrastructure is a blocker, not a pass. Repeated failure requires reassessing the approach; pause affected work when a new user decision or prerequisite is needed.

Use the [completion summary](../task/reference.md#completion-summary). The parent keeps ticket, branch and shipping ownership when delegated. Shipping always follows separate existing authorization and [shipping.md](shipping.md); completion grants none.

# Shared execution contracts

## Git sync only

Fetching, merging main into a working branch, or otherwise syncing Git state
is operational work, not a build: no grilling, planning, test proposals, or
automatic review or verification subagents, even with an open PR. An explicitly
requested review, verification, or build still follows its route.

Confirm the branch and incoming ref, record both revisions, and preserve
unrelated working and index changes. No automatic discard, force push,
protected branch commit, or hook bypass. Then confirm the incoming revision is
included, with no unresolved conflicts or unexpected changes. A clean sync
stops there: report what was incorporated and that app behavior was not tested.

If conflict resolution changes behavior, apply [verification scope](#verification-scope)
to the resolved paths and their consumers, not the whole branch, and escalate
shared or high-risk effects or uncertainty. Purely mechanical conflicts need
only applicable structural checks. Requested or required shipping, user checks,
and repository hooks still apply.

## Verification scope

Select checks from changed behavior, contracts, dependency reach, failure cost,
and uncertainty. File count, diff size, or a label such as "small bug" cannot
establish low risk. Use known entry points, callers, suites, and CI requirements;
research uncertainty before narrowing. Choose the scope yourself, with a short
reason, not a user questionnaire.

| Work and actual impact | Applicable evidence |
| --- | --- |
| Clean operational Git sync | Git safety, incorporation, conflict/status checks; stop under [Git sync only](#git-sync-only) |
| Meaningful conflict resolution | Resolved behavior and relevant consumers/tests/checkers; widen for shared effects |
| Localized bug with bounded consumers | Reproduce/check the changed behavior, relevant existing tests, and affected lint/type checks when configured; check direct regressions |
| Docs/copy/types/config | Links, syntax, rendering or consuming checks as relevant; inspect the runtime or consumer reach of types/config |
| Auth, permissions, money, shared infrastructure/contracts, schema or migration | Broader integration and affected consumer/failure/recovery checks; full suites when coupling or uncertainty warrants them |
| Explicit request for full verification/all suites | Inventory and run every configured suite requested, reporting unavailable checks; do not silently substitute a narrow pass |

Run existing checks with supported package/path/project selection when it preserves their meaning. If a checker cannot be scoped safely, use its standard command or disclose the gap; do not invent unsupported filters. Expand after failures or newly discovered shared impact. Required repository checks, security rules, hooks, and remote CI still apply; scope selection never waives them or changes CI/branch protection.

Reuse evidence only while the relevant code, contracts, dependencies, command,
build, configuration, and environment are unchanged; a different SHA alone does
not invalidate checks of unchanged independent behavior. Report actual checks
and results, reused evidence, and omitted or unavailable scope with reasons. A
focused pass proves its bounded claim, not all application behavior or unrun suites.

## Ready-ticket preflight

Read the requested ticket and prerequisite contracts, current Git state, relevant code and governing rules. Apply the [fresh-executor readiness bar](../write-ticket/doctrine.md#fresh-executor-handoff) to the work being executed; do not rerun the authoring checker or preparation session. Verify live entry points, schemas, callers, dependency bases and other facts its items need; preparation evidence is a pointer, not proof the repository is unchanged.

Reuse settled intent, technical choices, meaningful exclusions, and explicit test acceptances or refusals with their decision sources. Preserve exact agreed signatures, types, payloads, examples, and values in their canonical contract blocks through execution and handoffs, with their rationale and constraints. Keep the same acceptance and rule IDs when taking over a ticket or child. Ask through `/grill-me` only about newly discovered material user choices; pause affected work while they remain open. A changed repository fact alone does not reopen the interview.

When the ticket is ready, announce or reuse its current lock and proceed in the selected route. Do not restart `/write-ticket`, require a fresh Questions batch, or require the user to say `skip grill`.

## Handoffs and evidence

For touched user flows, carry the settled [interaction contract](../write-ticket/reference.md#plan) into the relevant slice and handoff: entry context, carried data, result/continuation, recovery, and component reuse. Revalidate those facts under [action and continuation](user-experience.md#action-and-continuation). Completion evidence must cover the meaningful continuation, not merely a control opening. Backend-only work adds no UX ceremony.

Use the existing [execution context](planning.md#execution-context) and [slice contract](../task/reference.md#inline-plan-contract). Each handoff carries only what its receiver needs: outcome and item/acceptance IDs, slice and owner, dependency contracts, allowed paths and exclusions, current decisions and test consent sources, governing rule paths, Done when, and the exact question or action. Pin the base, current revision and working-diff boundary, including pre-existing changes; a commit alone does not identify uncommitted work.

Return the bounded contribution, stable finding IDs, checks and evidence IDs tied to acceptance IDs, actual checked revision/diff and environment, result, and concrete blockers. Reuse IDs across fixes so old and new evidence compare; never rename an unresolved finding into a new success.

For the selected route's combined review, use the [fresh review context](../review/contract.md#fresh-combined-review-context). Preserve its gate order and implementer constraints; the focused reviewer adds no per-slice gate and gains no remediation ownership.

After a change, identify which claims depend on changed code, contracts, dependencies, fixtures or environment. Invalidate that evidence and recheck the affected claims and seams. Explain why any retained evidence still applies. A scoped remediation review covers named findings, touched paths and direct regressions; broaden it when the fix changes another contract or scope. Scoped re-review never replaces whole-result acceptance. Final acceptance covers the combined result with applicable checks selected under [verification scope](#verification-scope), including valid retained evidence; an earlier pass cannot certify affected later edits.

## Remediation

Review owns stable findings and their evidence. The active orchestrator alone adjudicates them, maintains the fix backlog, and dispatches work. Standalone `/review` stops after its findings unless fixes were requested.

Repeated correction and re-review follows the shared
[review budget](../review/contract.md#review-budget), kept with stable findings
across skill handoffs; exhaustion or an unresolved dispute is a reported
blocker, not approval.

When cause, impact or correction of an actionable finding set is unclear, the orchestrator investigates once per finding set, reusing an adequate existing investigation. The investigation gives, per stable finding ID, root cause, smallest fix, touch surface, uncertainty, and verification; it adds no findings, product discovery, or follow-ups. Promote the selected set once for the current evidence and fix decision, naming finding IDs with their correction, touch surface, non-goals, acceptance and owner under the user's existing authorization. If that authorization does not cover fixes, ask before implementing. New scope, waivers and changed test assertions still need the user's decision.

Fix mode is a bounded slice of the current outcome. Prefer the smallest authoritative correction; no new product discovery, optional cleanup or test suggestion. Return findings to their responsible worker where the selected route uses workers. Recheck under [Handoffs and evidence](#handoffs-and-evidence), then the route's gate order. Reinvestigate only when new evidence or a failed approach changes the diagnosis. A blocked or declined required fix stays blocking unless the user waives it by name.

Under existing authorization, deliver the corrected artifact with renewed evidence before handing the result to human review. A list of actionable comments does not complete an authorized fix. Report findings outside authorization or blocked by a required decision; never silently implement them or call them resolved.

## Recovery and completion

On resume, use the [context authority order](planning.md#authority), inspect actual Git state and live prerequisite contracts, recover settled user decisions with their sources, and reconcile current slice/finding status. A saved process record is a coordination aid, not authority or proof. Preserve unrelated changes and invalidate stale evidence before continuing.

Complete only when every applicable acceptance item, test decision, review finding and required check is accounted for on the final result. Report passed, failed, inconclusive and unrun checks separately, with the checked revision/diff, evidence and any named user waiver. Missing access or infrastructure is a blocker, not a pass. Repeated failure means reassess the approach; pause affected work when a new user decision or prerequisite is needed.

Use the [completion summary](../task/reference.md#completion-summary). The parent keeps ticket, branch and shipping ownership when delegated. Shipping needs separate existing authorization and follows [shipping.md](shipping.md); completion grants none.

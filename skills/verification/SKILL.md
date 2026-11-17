---
name: verification
description: Use when the user asks to verify or prove a change works, to write or add tests, to run all repository tests, to prove the running app, a migration, an endpoint, or a job, or to audit the verification recipe and feature map, or a build reaches its verification gate.
category: Code
---

# Verification

It also owns writing tests ([testing.md](../rules/testing.md)).

Proof standards, the recipe and feature map shape, and the maintenance pass are adapted from pstack's [create-verification-skill](https://github.com/cursor/plugins/tree/b4a4f6151b8e77f8d71045f09f553a733cf0ed37/pstack/skills/create-verification-skill), [maintain-verification-skill](https://github.com/cursor/plugins/tree/b4a4f6151b8e77f8d71045f09f553a733cf0ed37/pstack/skills/maintain-verification-skill), and [prove-it-works](https://github.com/cursor/plugins/tree/b4a4f6151b8e77f8d71045f09f553a733cf0ed37/pstack/skills/principle-prove-it-works) (MIT). The no-fallback rule and the saved recipe follow Claude Code's [`/verify`](https://code.claude.com/docs/en/skills).

## Read when

- Every run: [doctrine.md](doctrine.md).
- Picking checks: [ways to verify](reference.md#ways-to-verify). Finding and running suites: [repository test suites](reference.md#repository-test-suites). Writing or updating the app recipe: [recipe template](reference.md#recipe-template).
- UI checks: [user-experience.md](../rules/user-experience.md) and `docs/design.md` (`ux:source-of-truth`, `ux:quality-floor`).

## Pick the target

- **Started by an execution skill**: use the parent's pinned revision/diff, Done when, rules that must stay true, slices, and test decisions. Follow that skill's review/verification ordering.
- **Started by the user**: verify the current work, a branch, or a PR checkout. Take Done when from the user, then the ticket or PR, then the diff. If none exists, ask once. For a request to write tests, verify the behavior first, then code those checks.

## Process

1. **Checks.** Identify changed behavior, dependencies, Done when, and risk. Select the relevant [repository test suites](reference.md#repository-test-suites), lint/type/consuming checks, and [ways to verify](reference.md#ways-to-verify). Record a compact scope and reason, valid reused evidence, and meaningful exclusions. For full verification, inventory every configured suite.
2. **Recipe.** Read `docs/verification.md` if it exists. Otherwise infer launch and test commands from running terminals, manifests, CI, and the README.
3. **Launch or reuse.** When selected checks need a running process, reuse the dev server, `convex dev`, or worker shown in the terminals. For web startup or debugging, apply [development-server logs](../rules/dev-server-logs.md) before launch. Start only what those checks need, on a local or disposable environment ([safe targets](doctrine.md#safe-targets)).
4. **Doctor.** Before a live drive and after any surprise, check its prerequisites read-only: process up, right build, owned port, and seed sign-in when applicable.
5. **Suites.** Run selected checks with scoped commands, or full commands for broad or full verification ([repository test suites](reference.md#repository-test-suites)). Use [isolated runners](doctrine.md#isolated-runners) only for independent expensive checks. Broaden for newly discovered impact or failures.
6. **Drive.** Run each live check through the real path a user or system takes: the UI flow in a browser, the HTTP call, the CLI command, the job trigger.
   - If an execution skill started this run as an independent subagent, drive here. This subagent did not write the code.
   - For substantial or high-risk changes authored here, hand the drive to a fresh subagent with the selected checks and recipe when available. Focused low-risk checks can run here. Ask for evidence per check, not a summary; preserve an explicitly requested independent workflow.
7. **Judge.** Reconcile every suite and live check against the inventory and pinned target, then mark each verified, failed, or inconclusive ([outcomes](doctrine.md#outcomes)). Read delegated evidence yourself.
8. **Code what is worth keeping.** For each verified check that guards a rule likely to break silently and has no test yet, add it to the [proposal](../rules/testing.md#proposal), end to end first. Write only accepted tests ([no unrequested tests](../rules/no-unrequested-tests.md)), following [testing.md](../rules/testing.md); otherwise propose and keep going.
9. **Cleanup.** Stop only what this run started. Evidence survives cleanup.
10. **Recipe upkeep.** [Propose recipe edits](doctrine.md#recipe) and keep going. Write them when the user replies. When the user asks to audit the recipe or feature map itself, run the [maintenance pass](#maintenance-pass) instead of steps 1 to 9.
11. **Hand off** with the [handoff](reference.md#handoff).

When a change touches ordering, retries, concurrency, or a state machine and no test can reach the breaking case, say so in the handoff and name [`/create-formal-verification-skill`](../create-formal-verification-skill/SKILL.md) and [`/statechart`](../statechart/SKILL.md) as the way to prove it. Both need their own user start; never generate a formal check from here unasked. When the repo already has a project-local formal verify skill covering the changed code, run it as one of the selected checks.

## Maintenance pass

Check `docs/verification.md` and its feature files against source and live behavior. Report **blocked** for incomplete coverage, with the exact blocker. After full coverage, report **clean** if no corrections are needed or **changed** if corrections are confirmed. For each correction, say whether it was applied or awaits consent. Edits are limited to recipe, feature files, and recipe-owned harness scripts.

1. **Check the index.** If no recipe exists, offer a normal run. Include legacy inline Features entries in coverage and propose moving them to feature files. Record broken or duplicate entries.
2. **Source wave.** One read-only scout per feature, launched together when delegation is available. Each explains how the feature works from source, flags likely drift with citations, and returns one concise live recipe. Scouts never drive the app and never edit.
3. **Reconcile.** Require a source summary per feature. Merge overlapping recipes into as few app states as practical. Spot-check cited drift; do not re-prove clean claims. Sweep recent churn for user-facing surfaces missing from the map, and require a concrete source path before calling one missing.
4. **Live pass.** Required even when source looks clean. The coordinator owns all driving, exercises every feature at least once, and holds the [live-pass invariants](reference.md#maintenance-pass-detail): doctor again after anything surprising, evidence checked at its named place after every cleanup, nothing a drive started outlives the drive. A feature that cannot be reached is `inconclusive` under [outcomes](doctrine.md#outcomes), with the concrete prerequisite and the route attempted.
5. **Triage.** Propose corrections for doc drift and harness gaps. Try harness corrections in scratch and re-drive before counting them as proven. Apply persistent corrections only with recipe-write consent. Report product gaps without documenting them as expected behavior.
6. **Report.** Outcome, features covered, unreachable prerequisites, confirmed drift, and product gaps, in the [handoff](reference.md#handoff) shape. Keep run notes in a scratch location; never commit them.

## If a parent already owns the next step

Follow [nested capabilities](../rules/planning.md#nested-capabilities) and return the handoff. The parent puts failed checks in the Fix backlog next to the `/review` findings, owns remediation, and carries the test proposal and recipe edits into its final report.

## Anti-patterns

- Committing screenshots, traces, or scratch scripts

---
name: verification
description: Use when the user asks to verify or prove a change works, to write or add tests, to run all repository tests, or to prove the running app, a migration, an endpoint, or a job works, or when a build skill reaches its verification gate. Proposes e2e and integration tests worth keeping.
category: Code
---

# Verification

`/review` reads the diff and asks "is the code right?". `/verification` runs the work and asks "does it do what was asked?". It selects tests and real-path checks by [verification scope](../rules/execution.md#verification-scope). A passing suite alone does not prove a changed user flow works.

It also owns writing tests. A test is a verification step written as code, so the checks worth repeating become tests: end to end first, integration next, unit only in rare cases ([testing.md](../rules/testing.md)).

Proof standards and the recipe shape are adapted from pstack's [create-verification-skill](https://github.com/backnotprop/pstack/tree/main/skills/create-verification-skill), [maintain-verification-skill](https://github.com/backnotprop/pstack/tree/main/skills/maintain-verification-skill), and [prove-it-works](https://github.com/backnotprop/pstack/tree/main/skills/principle-prove-it-works) (MIT). The no-fallback rule and the saved recipe follow Claude Code's [`/verify`](https://code.claude.com/docs/en/skills).

## Read when

- Every run: [doctrine.md](doctrine.md).
- Picking checks: the [ways to verify](reference.md#ways-to-verify). Finding and running suites: [repository test suites](reference.md#repository-test-suites). Writing or updating the app recipe: the [recipe template](reference.md#recipe-template).
- UI checks: [user-experience.md](../rules/user-experience.md) and `docs/design.md` (`ux:source-of-truth`, `ux:quality-floor`).
- Proposing or writing a test: [testing.md](../rules/testing.md) and [no-unrequested-tests.md](../rules/no-unrequested-tests.md).
- Reading terminals and logs: [Verify terminals first](../rules/tooling.md#verify-terminals-first).
- Before asking the user anything: [Asking the user](../rules/writing-style.md#asking-the-user). Write reports in [plain language](../rules/writing-style.md#plain-language).

## Pick the target

- **Started by an execution skill**: use the parent's pinned revision/diff, Done when, rules that must stay true, slices, and test decisions. Follow that skill's review/verification ordering and return the handoff to that parent.
- **Started by the user**: verify the current work, a branch, or a PR checkout. Take Done when from the user, then the ticket or PR, then the diff. If none exists, ask once. A request to write tests accepts the tests it names; verify the behavior first, then code those checks.

Use [Git sync only](../rules/execution.md#git-sync-only) for operational synchronization. Otherwise size checks to the affected behavior and risk ([scope](doctrine.md#scope-to-the-change)); honor explicit full-verification requests.

## Process

1. **Checks.** Identify changed behavior, dependencies, Done when, and risk. Select the relevant [repository test suites](reference.md#repository-test-suites), lint/type/consuming checks, and [ways to verify](reference.md#ways-to-verify). Record a compact scope and reason, valid reused evidence, and meaningful exclusions. For full verification, inventory every configured suite.
2. **Recipe.** Read `docs/verification.md` if it exists. Otherwise infer the launch and test commands from running terminals, workspace manifests, CI configuration, runner configuration, the README, `Makefile`, `docker-compose`, and env examples.
3. **Launch or reuse.** When selected checks need a running process, reuse the dev server, `convex dev`, or worker shown in the terminals. For web startup/debugging, apply [development-server logs](../rules/dev-server-logs.md) before launch. Start only what those checks need, on a local or disposable environment ([safe targets](doctrine.md#safe-targets)). Docs or Git checks need no app launch.
4. **Doctor.** Before a live drive and after any surprise, check its prerequisites read-only: process up, right build, owned port, and seed sign-in when applicable. Checks without a live process need no app doctor.
5. **Suites.** Run selected checks with supported scoped commands, or full commands for broad/full verification. Avoid duplicate runs and reuse valid evidence. Use [isolated runners](doctrine.md#isolated-runners) only for independent expensive checks; otherwise run directly. Keep data local/disposable; record commands, exit status, counts, failures, unavailable checks, and scope not selected. Broaden for newly discovered impact or failures.
6. **Drive.** Run each live check through the real path a user or system takes: the UI flow in a browser, the HTTP call, the CLI command, the job trigger.
   - If an execution skill started this run as an independent subagent, drive here. This subagent did not write the code.
   - For substantial or high-risk changes authored here, hand the drive to a fresh subagent with the selected checks and recipe when available. Focused low-risk checks can run here. Ask for evidence per check, not a summary; preserve an explicitly requested independent workflow.
7. **Judge.** Reconcile every suite and live check against the inventory and pinned target, then mark each verified, failed, or inconclusive ([outcomes](doctrine.md#outcomes)). Read delegated evidence yourself. A missing, stale, or blocked check is not a pass.
8. **Code what is worth keeping.** For each verified check that guards a rule likely to break silently and has no test yet, add it to the [proposal](../rules/testing.md#proposal), end to end first. Write only the tests the user named or asked for, following [testing.md](../rules/testing.md); otherwise propose and keep going.
9. **Cleanup.** Stop only what this run started. Evidence survives cleanup.
10. **Recipe upkeep.** If the run inferred launch or test commands that worked, or found `docs/verification.md` wrong or missing a feature, list the exact edits in the report and keep going. Write them when the user replies.
11. **Hand off** with the [handoff](reference.md#handoff).

## If a parent already owns the next step

Return the handoff. The parent puts failed checks in the Fix backlog next to the `/review` findings and owns remediation. The parent carries the test proposal and recipe edits into its final report.

## Anti-patterns

- Using a green test, type check, build, or diff as the only proof of a changed live flow
- Narrowing checks despite shared/high-risk impact or an explicit full-verification request
- Treating a skipped or blocked suite as passed
- Accepting a drive subagent's verdict without reading its evidence
- Driving unrelated live layers to make the manual pass look thorough
- Committing screenshots, traces, or scratch scripts

---
name: verification
description: >-
  Prove finished work does what was asked by running the real app like a
  manual QA pass: drive the changed UI flow, catch dead buttons, layout
  shift, and console errors, and exercise migrations, endpoints, workers, and
  cron jobs. Reports verified, failed, or inconclusive with evidence. Sibling
  of /review; /task runs both in parallel. User must invoke.
disable-model-invocation: true
---

# Verification

`/review` reads the diff and asks "is the code right?". `/verification` runs the work and asks "does it do what was asked?". It proves each check against the running work, never with tests or type checks.

Proof standards and the recipe shape are adapted from pstack's [create-verification-skill](https://github.com/backnotprop/pstack/tree/main/skills/create-verification-skill), [maintain-verification-skill](https://github.com/backnotprop/pstack/tree/main/skills/maintain-verification-skill), and [prove-it-works](https://github.com/backnotprop/pstack/tree/main/skills/principle-prove-it-works) (MIT). The no-fallback rule and the saved recipe follow Claude Code's [`/verify`](https://code.claude.com/docs/en/skills).

## Read when

- Every run: [doctrine.md](doctrine.md).
- Picking checks: the [ways to verify](reference.md#ways-to-verify). Writing or updating the app recipe: the [recipe template](reference.md#recipe-template).
- UI checks: [user-experience.md](../rules/user-experience.md) and `docs/design.md` (`ux:source-of-truth`, `ux:quality-floor`).
- Reading terminals and logs: [Verify terminals first](../rules/tooling.md#verify-terminals-first).
- Before asking the user anything: [Asking the user](../rules/writing-style.md#asking-the-user). Write reports in [plain language](../rules/writing-style.md#plain-language).

## Pick the target

- **Started by `/task`**: `/task` launched this run as its own subagent, next to a `/review` subagent, with Done when, the rules that must stay true, the slices, and the diff. Return the handoff to `/task`.
- **Started by the user**: verify the current work, a branch, or a PR checkout. Take Done when from the user, then the ticket or PR, then the diff. If none exists, ask once.

Verify every change, sized to what was done ([scope](doctrine.md#scope-to-the-change)).

## Process

1. **Checks.** List what the work did (diff, slices, Done when, rules that must stay true). For each item, pick the few [ways to verify](reference.md#ways-to-verify) that show it works, and only those. Name the layers the change did not touch. Record the list before driving.
2. **Recipe.** Read `docs/verification.md` if it exists. Otherwise infer the launch from running terminals first, then `package.json`, the README, `Makefile`, `docker-compose`, and env examples.
3. **Launch or reuse.** Reuse the dev server, `convex dev`, or worker that the terminals show is running. Start only what is missing, on a local or disposable environment ([safe targets](doctrine.md#safe-targets)).
4. **Doctor.** Run one read-only check before the first drive and after any surprise: process up, right build, the port is ours, the seed user can sign in.
5. **Drive.** Run each check through the real path a user or system takes: the UI flow in a browser, the HTTP call, the CLI command, the job trigger.
   - If `/task` started this run, drive here. This subagent did not write the code.
   - If the user started this run in the chat that wrote the code, hand the drive to a fresh subagent with the check list and recipe. Ask for evidence per check, not a summary.
6. **Judge.** Read the evidence, then mark each check verified, failed, or inconclusive ([outcomes](doctrine.md#outcomes)).
7. **Cleanup.** Stop only what this run started. Evidence survives cleanup.
8. **Recipe upkeep.** If the run inferred a launch that worked, or found `docs/verification.md` wrong or missing a feature, list the exact edits in the handoff and ask. Write them after the user says yes.
9. **Hand off** with the [handoff](reference.md#handoff).

## If a parent already owns the next step

Return the handoff. The parent puts failed checks in the Fix backlog next to the `/review` findings and owns remediation. The parent asks about recipe edits in its next Questions batch.

## Anti-patterns

- Passing a check from a green test, a type check, a build, or the diff
- Accepting a drive subagent's verdict without reading its evidence
- Running a backend pass for a UI-only change, or any layer the work did not touch
- Committing screenshots, traces, or scratch scripts

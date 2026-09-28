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

`/review` reads the diff and asks "is the code right?". `/verification` runs the work and asks "does it do what was asked?". It never falls back to tests or type checks.

Proof standards and the recipe shape are adapted from pstack's [create-verification-skill](https://github.com/backnotprop/pstack/tree/main/skills/create-verification-skill), [maintain-verification-skill](https://github.com/backnotprop/pstack/tree/main/skills/maintain-verification-skill), and [prove-it-works](https://github.com/backnotprop/pstack/tree/main/skills/principle-prove-it-works) (MIT). The no-fallback rule and the saved recipe follow Claude Code's [`/verify`](https://code.claude.com/docs/en/skills).

## Read when

- Every run: [doctrine.md](doctrine.md), [code-quality.md](../rules/code-quality.md), and [code-structure.md](../rules/code-structure.md).
- Picking checks: the [ways to verify](reference.md#ways-to-verify). Writing or updating the app recipe: the [recipe template](reference.md#recipe-template).
- UI checks: [user-experience.md](../rules/user-experience.md) and `docs/design.md` (`ux:source-of-truth`, `ux:quality-floor`).
- Throughout: stay in your smart zone (hard rule 9 in `AGENTS.md`). The drive runs in a subagent; the coordinator judges its evidence.
- Before asking the user anything: [Asking the user](../rules/writing-style.md#asking-the-user). Reports follow [Plain language](../rules/writing-style.md#plain-language).
- Reading terminals and logs: [Verify terminals first](../rules/tooling.md#verify-terminals-first).

## Pick the target

- **Nested under `/task`**: the parent passes Done when, rules that must stay true, and the diff. `/task` runs this in a subagent while `/review` runs. Return the handoff to the parent.
- **User start**: the current work, a branch, or a PR checkout. Derive Done when from the user, the ticket or PR, then the diff. If none can be derived, ask once.

Every change gets verified, sized to what was done ([scope](doctrine.md#scope-to-the-change)).

## Process

1. **Checks.** List what the work did (diff, slices, Done when, rules that must stay true). For each item, pick the few [ways to verify](reference.md#ways-to-verify) that would show it works, and only those. Name the layers the change did not touch. Record the list before driving.
2. **Recipe.** Read `docs/verification.md` if it exists. Otherwise infer the launch from running terminals first, then `package.json`, the README, `Makefile`, `docker-compose`, and env examples.
3. **Launch or reuse.** Reuse the dev server, `convex dev`, or worker that terminals show is running. Start only what is missing, on a local or disposable environment ([safe targets](doctrine.md#safe-targets)).
4. **Doctor.** One read-only check before the first drive and after any surprise: process up, right build, the port is ours, the seed user can sign in.
5. **Drive.** Run each check through the real path a user or system takes: the UI flow in a browser, the HTTP call, the CLI command, the job trigger. Hand the drive to a fresh subagent with the check list and recipe; ask for evidence per check, not a summary.
6. **Judge.** Read the evidence, not the subagent's verdict. Mark each check verified, failed, or inconclusive ([outcomes](doctrine.md#outcomes)).
7. **Cleanup.** Stop only what this run started. Evidence survives cleanup.
8. **Recipe upkeep.** If the run inferred a launch that worked, or found `docs/verification.md` wrong or missing a feature, list the exact edits in the handoff and ask. Write them only on yes.
9. **Hand off** with the [handoff](reference.md#handoff).

## If a parent already owns the next step

Return the handoff. Failed checks become Fix backlog input next to `/review` findings; the parent owns remediation. Recipe edits still wait for the user's yes, asked by the parent in its next Questions batch.

## Anti-patterns

- Passing a check from a green test, a type check, a build, or the diff
- Trusting the drive subagent's verdict without reading its evidence
- Fixing product code during the run
- Running a backend pass for a UI-only change, or any layer the work did not touch
- Touching production or shared data
- Writing `docs/verification.md` without a yes
- Committing screenshots, traces, or scratch scripts

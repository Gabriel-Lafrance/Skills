---
name: task-with-tests
description: Default build skill. After the grill locks, proposes tests, writes only the ones the user accepts before any code, then builds until they pass. Use when the user asks to build, implement, add, or fix a feature or bug. The user may refuse every test.
category: Code
---

# Task with tests

Same loop as [`/task`](../task/SKILL.md), with one change: the tests come first. After the grill locks, the user picks tests. The accepted tests are written before any plan or product code, and they define the cage the code must fit. The build is done when they pass.

## Read when

- Everything [`/task`](../task/SKILL.md#read-when) opens, at the same moments, plus its [doctrine](../task/doctrine.md) and [reference](../task/reference.md). This skill only replaces the test phase.
- About to send the tests prompt or write a test? Open [no-unrequested-tests.md](../rules/no-unrequested-tests.md), [testing.md](../rules/testing.md), and [reference.md](reference.md). Skip them and you write a test the user never said yes to.
- About to ask the user anything? Open [Asking the user](../rules/writing-style.md#asking-the-user). Skip it and you send questions with no options and no recommendation.

## Process

1. Establish the execution context and run [Phase 0 of the `/task` lifecycle](../task/reference.md#phase-0-establish-context-and-grill). The Locked message must name the public entry (function, hook, mutation, handler) that each rule that must stay true runs through.
2. If no public entry can be named, say so and recommend plain `/task`. Stop.
3. Send the [tests prompt](reference.md#tests-prompt) right after Locked, before any plan. Wait. Silence is not yes. A correction to a rule goes back to the grill.
4. If the user refused every test, say the work continues as plain `/task` and follow its lifecycle from the plan.
5. Write the accepted tests as the first slice, following [testing.md](../rules/testing.md). Run them and record the [red baseline](reference.md#red-baseline).
6. Plan and build with the [`/task` Phase 1](../task/reference.md#phase-1-plan-and-build) steps. Each plan contract's Done when names the tests that must turn green. During the build, follow the [cage rules](reference.md#cage-rules).
7. Acceptance evidence: the `/task` gate (`/verification` in parallel with `/review`), plus the focused run showing every accepted test green and the [cage check](reference.md#cage-check). Fix mode as in `/task`.
8. Announce completion with the `/task` [completion summary](../task/reference.md#completion-summary).

### If a parent already owns the ticket, branch, and PR

Same as `/task`: no ship Questions, no commit, no PR. Return the completion summary and evidence to the parent.

### If this chat owns shipping

Same as `/task`: offer [ship Questions](../task/reference.md#ship-questions) only after all gates pass.

## Anti-patterns

- Planning or writing product code before the tests prompt is answered and the accepted tests exist
- Offering a test with no public entry, or for a rule the grill did not record
- Changing what a test asserts during the build without the user's yes
- Calling the build done while any accepted test is red
- Copying `/task` steps into this skill instead of linking them

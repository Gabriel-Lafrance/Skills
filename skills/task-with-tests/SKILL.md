---
name: task-with-tests
description: Default build skill. After the grill locks, proposes tests, writes only the ones the user accepts before any code, then builds until they pass. Use when the user asks to build, implement, add, or fix a feature or bug. The user may refuse every test.
category: Code
---

# Task with tests

Same loop as [`/task`](../task/SKILL.md), with one change: the tests come first. After the grill locks, the user picks tests. The accepted tests are written before any plan or product code, and the code must fit them. The build is done when they pass.

## Read when

- Everything [`/task`](../task/SKILL.md#read-when) opens, at the same moments, plus its [doctrine](../task/doctrine.md) and [reference](../task/reference.md). This skill only replaces the test phase.
- About to send the tests prompt or write a test? Open [no-unrequested-tests.md](../rules/no-unrequested-tests.md), [testing.md](../rules/testing.md), and [reference.md](reference.md). Skip them and you write a test the user never said yes to.
- About to ask the user anything? Open [Asking the user](../rules/writing-style.md#asking-the-user).

## Process

1. Apply the shared [ready-ticket preflight](../rules/execution.md#ready-ticket-preflight), then establish the execution context and run [Phase 0 of the `/task` lifecycle](../task/reference.md#phase-0-establish-context-and-grill). In the reused or updated lock, name the public entry (function, hook, mutation, handler) that each rule that must stay true runs through.
2. If all tests were explicitly refused, continue as plain `/task` from the plan without another prompt. Otherwise, if a required test has no public entry, resolve that blocker before writing it; do not invent an entry or acceptance.
3. Use the [tests prompt](reference.md#tests-prompt) for unsettled tests after the current lock, before any product plan. Carry forward explicit acceptances and refusals; ask only about unsettled tests, batching them across children in a [whole-stack run](../task/doctrine.md#whole-stack-ticket-handoff). Wait for those answers. Silence is not yes. Send a corrected rule back to the grill.
4. If the user refused every test, say the work continues as plain `/task`, and follow its lifecycle from the plan.
5. Write the accepted tests as the first slice, following [testing.md](../rules/testing.md). Run them and record the [red baseline](reference.md#red-baseline).
6. Plan and build with the [`/task` Phase 1](../task/reference.md#phase-1-plan-and-build) steps. Each plan contract's Done when names the tests that must turn green. During the build, follow the [test rules](reference.md#test-rules).
7. Gate: run the scoped [`/task` gate](../task/reference.md#phase-1-plan-and-build), using independent agents when risk or an explicit workflow warrants them. Add the focused run showing every accepted test green and the [fixed-test check](reference.md#fixed-test-check). No unrelated suite is mandatory solely because tests were accepted. Use Fix mode as in `/task`.
8. Announce completion with the `/task` [completion summary](../task/reference.md#completion-summary).

### If a parent already owns the ticket, branch, and PR

Same as `/task`: return the completion summary and evidence to the parent, which handles shipping under the user's existing authorization.

### If this chat owns shipping

Same as `/task`: after all gates pass, ship when already authorized; otherwise offer [ship Questions](../task/reference.md#ship-questions).

## Anti-patterns

- Planning or writing product code while test choices remain open or before accepted tests exist
- Offering a test with no public entry, or for a rule the grill did not record
- Changing what a test asserts during the build without the user's yes
- Calling the build done while any accepted test is red
- Copying `/task` steps into this skill instead of linking them

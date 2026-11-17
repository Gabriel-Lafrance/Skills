# No unrequested tests

## Rule

No tests unless the user accepted that test. Changing code is not a reason to add a test.

Leave test files unchanged for a small tweak, copy change, rename, comment, type-only edit, wiring change, formatter, UI chrome, generated code, or a one-line fix. Skip a test that chases coverage, violates [No tautological tests](testing.md#no-tautological-tests), or exists because the suite should cover this.

Running tests that already exist is fine. Fix an existing assertion only when this change made that assertion lie, and add no new case beside it. When that assertion belongs to a test the user accepted, changing it needs the user's decision.

## Accepted means

The user accepted a test when:

- they explicitly asked for it, or
- they named it from a `/verification` [proposal](testing.md#proposal), such as `tests 1 3`, or
- they said yes after `/review` recommended one for a complex public surface (authorization, ownership, safe-to-retry, a domain rule that can silently drift), or
- they gave a blanket yes ("do all the tests"), which accepts each test `/verification` proposes for this work; list them in the final report.

A test asked for in a ticket, a launch or delegation brief, or a Done when list counts only when it quotes or links that user decision. Written by an agent without one, such as "tests that reproduce the failing case" or "follow `task-with-tests`", it is a proposal: verify with existing checks and a manual repro, and name the test in the final report for the user to accept.

A blanket no ("no tests until the MVP") refuses every test for this work and every child brief until the user lifts it. Stop offering tests.

Only `/verification` writes an accepted test. Build slices and every other skill leave test files alone.

## Check

Can you point to the user message that accepted this exact test, not an agent's brief that asks for it?

# No unrequested tests

**Open this when:** you are about to create or extend a test file, or you feel the change "should have a test".
**Skip it and you will:** pad the diff with tests nobody asked for, which the user then has to review and delete.

## Rule

No tests unless the user accepted that test. Changing code is not a reason to add a test.

Leave test files unchanged for a small tweak, copy change, rename, comment, type-only edit, wiring change, formatter, UI chrome, generated code, or a one-line fix. Skip a test that chases coverage, restates the implementation (`expect(add(1, 2)).toBe(3)`), or exists because the suite should cover this.

Running tests that already exist is fine. Fix an existing assertion only when this change made that assertion lie, and add no new case beside it.

## Accepted means

Write a test only when the user has accepted that lock:

- they explicitly asked for it, or
- they answered yes on a `/task` [behavior-lock brief](../task/reference.md#behavior-lock-suggestion) after the grill's Locked in message (each brief cites a grilled rule; every brief has a no; silence and a parent taking `recommended` are not acceptance), or
- they answered yes on a `/task-with-tests` [tests prompt](../task-with-tests/reference.md#tests-prompt) after the grill's Locked in message (same rules as a `/task` brief), or
- they said yes after `/review` recommended one for a complex public surface (authorization, ownership, safe-to-retry, a domain rule that can silently drift).

Only an accepted lock writes tests. A `/task` suggestion or a `/review` recommendation becomes acceptance when the user answers. `/task` build slices and other build steps leave test files alone. This binds every skill.

How to write an accepted test: [testing.md](testing.md).

## Check

Can you point to the user message that accepted this exact test?

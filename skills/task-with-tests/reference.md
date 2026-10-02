# Task with tests reference

Load at the tests prompt, when writing the accepted tests, and during the build. Everything not here follows [`/task`](../task/reference.md).

## Tests prompt

Use it for unsettled tests after the current lock, before any product plan. The [ready-ticket preflight](../rules/execution.md#ready-ticket-preflight) carries existing decisions without another prompt. It replaces the `/task` [behavior-lock suggestion](../task/reference.md#behavior-lock-suggestion).

Carry forward explicit acceptances and refusals with their decision source. Offer only unsettled tests; if none remain, proceed without a prompt. For a whole-stack run, batch unsettled choices across children once, then write each child's accepted tests before its product code.

1. Walk each rule that must stay true. Offer one test per rule that has an observable outcome. Skip tautologies (`expect(add(1, 2)).toBe(3)`), UI chrome, formatters, generated code, and types-only code. This bar is looser than the [testing.md](../rules/testing.md#when-a-test-is-worth-writing) default on purpose: the tests are the agent's pass or fail signal.
2. Tie every test to one rule and to the public entry the grill named. A rule with no public entry gets no test.
3. Send one Questions-only message and wait. Every item has a no.

```markdown
## Questions
Reply like: 1a 2a

1. Rule 2 on `makeUserPay`: a retry must not charge twice.
   - Locks: the same retry key creates one charge.
   - Checks: call `makeUserPay` twice with one key and assert one charge.
   - Why: a double submit could charge the user twice.
   - a) yes, write this test first ← recommended
   - b) no, do not add this test
```

**Locks** is the test's What, **Checks** is its How, and **Why** is its Why in the [required test comment](../rules/testing.md#required-test-comment).

- **Correction** ("that is not the behavior"): update the rule, drop its tests, and send the prompt again from the corrected rule.
- **No:** no test. The rule still stands. Record the refusal.

## Red baseline

After writing the accepted tests, run only those tests and record the result in the execution context.

- Each test should fail because the entry is missing or the behavior is not built yet.
- If a test fails from a broken setup (bad import path, missing fixture), fix the setup now, before the plan.
- If a test already passes, it guards existing behavior and proves nothing new. Tell the user and keep it.
- Once the only failures are the expected ones, stage the test files (`git add <test files>`, no commit). The staged copy is the baseline the [fixed-test check](#fixed-test-check) compares against.

## Test rules

- Create test files only in the test slice. Product slices leave them alone.
- Fix test setup only: imports, fixtures, paths, and the runner config the test needs.
- If a change touches an assertion, an expected value, a test's scenario, or deletes or skips a test, it reopens that rule. Stop and ask the user.
- If a test seems wrong while building, name the rule it contradicts and wait for the user. Bend neither the code nor the test to get green.

## Fixed-test check

Part of the acceptance evidence:

- The focused run of every accepted test passes.
- `git diff -- <test files>` (unstaged changes since the staged red baseline) shows setup fixes only.

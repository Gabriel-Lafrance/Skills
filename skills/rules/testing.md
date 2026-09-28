# Testing

How tests are written in this pack. No skill writes new tests: when a test is accepted, the agent follows this file. [`/test-audit`](../test-audit/SKILL.md) prunes and repairs existing tests against the same bar.

Parts of the authoring gate, junk patterns, and retention bar are adapted from [openclaw test-audit](https://github.com/openclaw/openclaw/tree/main/.agents/skills/test-audit) (MIT).

## No drive-by tests

When a test may be written at all lives in [no-unrequested-tests.md](no-unrequested-tests.md). Open it first. This file covers how to write a test the user already accepted.

## When a test is written

Only after the user accepted it, as defined in [no-unrequested-tests.md](no-unrequested-tests.md#accepted-means).

## When a test is worth writing

Lock a complex hook, domain rule, facade, stateful class, or a real regression whose public behavior could silently drift. Prefer it when review named authorization, ownership, or safe-to-retry writes with no durable lock. Skip thin wrappers, formatters, UI chrome, generated code, types-only files, coverage targets, and tautological checks (`expect(add(1, 2)).toBe(3)`). If the target is trivial, say so and stop.

`/task-with-tests` uses a looser bar: one test per grilled rule with an observable outcome, still skipping tautologies, UI chrome, formatters, generated code, and types-only code ([tests prompt](../task-with-tests/reference.md#tests-prompt)).

## Authoring gate

An accepted test still passes this gate before it lands. Answer four questions. A missing answer means do not write it yet:

1. What observable behavior, invariant, or independent contract does it protect?
2. What credible regression makes it fail?
3. Why does existing coverage not already catch that failure? Each contract has one primary test owner at the strongest boundary. Another layer needs its own risk the owner cannot reach, such as a transport or lifecycle failure. Extend a table-driven case or shared fixture instead of adding a near-duplicate test, and fold duplicated setup in the same change.
4. Does it need a production seam (export, flag, wrapper, injection hook) that no production caller needs? If yes, test at the real boundary instead.

Then check it against every [junk pattern](#junk-patterns). A match fails the gate unless the [retention bar](#retention-bar) names the contract it independently guards. A test that breaks under a behavior-preserving refactor asserts implementation, not behavior. Rewrite it at the owning boundary before it lands.

A bug regression test must fail on the pre-fix code for the intended reason and pass after the fix at the owner. A regression test that never failed proves the mock, not the fix. One regression at the owner covers the bug. Do not replay the same scenario at every layer it crosses.

## Junk patterns

The authoring gate rejects a new test that matches one. [`/test-audit`](../test-audit/SKILL.md) hunts for existing tests that do.

- Assertion-free coverage probes
- Self-comparisons and identity copies
- Copied fixtures, inventories, manifests, or export lists
- Exact source, import, or string greps
- Private predicate or call-shape tests that duplicate a real boundary test
- Duplicate invocations of the same contract
- Local replays of a shared helper's own tests
- Tests whose only job is to keep a test-only export, global, or wrapper alive
- Dead production code whose only callers are tests
- Expected values produced by the helper or renderer under test
- Mocks that implement the asserted behavior, or one mock standing in for different APIs
- Fixtures that supply the ordering, receipt, or callback the owner should produce, or persistence asserted against a store the path never writes
- Capability tests that restate a declared flag instead of exercising what the flag promises
- Negative controls that pass for an unrelated reason, such as a denial from a different guard or a rejection the production path never reaches
- Names or fixtures that promise more than the input exercises, such as a "clears the draft" test that asserts the draft was not cleared

## Retention bar

Keep a test when it independently enforces a public API, SDK, protocol, config, migration, storage, security, platform, default, generated cross-language, package, release, or architecture contract. Also keep:

- Call ordering when the order is observable behavior
- A regression with a credible failure mode
- Source inspection when it is the cheapest independent guard: it fails when the contract changes (the user-facing key, byte, or path) and survives an identifier-only rename
- A test that fails on the current code: treat it as a possible product bug, reproduce it, and fix the owner instead of deleting the test

Static or slow is not a reason to delete. A test that looks like implementation may still be the only proof of a contract. Prove otherwise before removing it.

## What a good test looks like

| Rule | Meaning |
| --- | --- |
| Lock observable behavior | Invariants and public contracts, not internals |
| Public entry | Exercise the public entry point. Mock only true external boundaries (network, clock, storage, authentication) |
| Name the invariant | Every test title states it |
| Approve first | Before writing, the user approves concise **Why**, **What**, and **How** statements for each main claim. A `/task` brief or `/task-with-tests` prompt item is already approved when the user answered yes on that line |
| Cite the grilled rule | A lock that came from `/task` names the rule that must stay true it locks (Rule N). No rule, no test |
| Small set | Core outcome, critical guard, meaningful edge, and the known regression when the brief named one. A few scenarios over combinatorial or snapshot theater |
| Reuse the repo | Runner, layout, fixtures, helpers. Do not add a framework |
| Focused run | Only the focused test file or filter unless that is inconclusive or the user asks otherwise |
| Code quality and structure | Helpers throw on setup failure (`quality:throw-at-boundaries`); comments summarize the approved lock (`quality:comments`); exercise the service or deep-module public API, not internals (`structure:deep-public-surface`) |

## Lock brief

Batch every known main claim in one message ([Asking the user](writing-style.md#asking-the-user)) and wait. Every brief has a no. Do not write tests until each brief is approved.

```markdown
## Lock brief: <symbol>
- Why: <risk if behavior changes>
- What: <observable contract or invariant>
- How: <public entry, setup, and assertion>

## Questions
Reply like: 1a

1. Approve this lock brief?
   - a) yes ← recommended
   - b) no, say what to change
```

## Required test comment

Put the approved three lines on each main test, in the repository's comment style:

```ts
/**
 * Why: <approved why>
 * What: <approved what>
 * How: <approved how>
 */
it("states the locked behavior", () => {
  // Assert an observable result.
});
```

## Process

1. Name the behavior to lock and what outside change it should catch. Find the public export and nearby tests. Run the [authoring gate](#authoring-gate). If the runner or layout is unclear, ask once.
2. Draft every needed Why / What / How brief, batch them for approval, and wait. When `/task` or `/task-with-tests` already collected that approval, do not ask again. Require the grilled rule id on each of those briefs. If the user corrected the rule after approval, stop and return the brief to the skill that collected it.
3. Write the tests from the approved Why / What / How through the named public entry. Keep the set small and put the approved comment on each main test. Run the focused test, not the whole suite. Check the result against the approved claim.
4. If the focused test fails on existing behavior, stop and report it; do not change production code to make it green without a user request. Under `/task-with-tests` the tests come before the code, so a failure is the expected [red baseline](../task-with-tests/reference.md#red-baseline): record it, and the build turns it green.
5. Report with the handoff below.

### Handoff

```markdown
## Behavior locks
- **Claim:** <approved Why / What / How>
- **Files:** <changed test files>
- **Verification:** `<command>`: pass | fail
- **Break signal:** <outside edit that makes this test fail>
```

## Do not

- Modify production code just to make a test convenient unless the user explicitly asks
- Expand into refactoring, or write tests before approval
- Write a test from a `/task` brief or `/task-with-tests` prompt item the user did not accept, or one that does not cite a grilled rule
- Write tautological tests (recompute the same arithmetic as the code, assert UI chrome exists) or chase coverage
- Add a test because the code changed, including a small tweak, copy change, rename, or one-line fix

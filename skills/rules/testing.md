# Testing

How tests are written in this pack. No skill writes new tests: when a test is accepted, the agent follows this file. [`/test-audit`](../test-audit/SKILL.md) prunes and repairs existing tests against the same bar.

Parts of the authoring gate, junk patterns, and retention bar are adapted from [openclaw test-audit](https://github.com/openclaw/openclaw/tree/main/.agents/skills/test-audit) (MIT).

## No drive-by tests

When a test may be written at all lives in [no-unrequested-tests.md](no-unrequested-tests.md). Open it first. This file covers how to write a test the user already accepted.

## When a test is written

Only after the user accepted it, as defined in [no-unrequested-tests.md](no-unrequested-tests.md#accepted-means).

## When a test is worth writing

Lock a complex hook, domain rule, facade, stateful class, or a real regression whose public behavior could silently drift. Prefer it when review named authorization, ownership, or safe-to-retry writes with no durable lock. Skip thin wrappers, formatters, UI chrome, generated code, types-only files, coverage targets, and [tautological tests](#no-tautological-tests). If the target is trivial, say so and stop.

`/task-with-tests` uses a looser bar: one test per grilled rule with an observable outcome, still skipping tautologies, UI chrome, formatters, generated code, and types-only code ([tests prompt](../task-with-tests/reference.md#tests-prompt)).

## No tautological tests

**Never write or extend a tautological test.** Test consent, a green run, or a coverage target does not relax this prohibition. Assert observable behavior at its real owning boundary against an expectation independently grounded in the accepted requirement or a public, external, or separately specified contract.

Do not derive the expected result from the implementation under test, copy its current constants or logic as the specification, compare a value with itself, or assert behavior supplied entirely by the test's own mock setup. Do not grep private names, call shapes, or source structure as a substitute for executing the claimed behavior. Such checks can pass while that behavior is absent or wrong.

Before writing, name a plausible incorrect behavior that the assertion would detect and explain why it would fail. Trace the actual production entry, setup and assertion: a mock must not suppress the failure mode the test claims to catch. Unit tests and faithful substitutes at true external boundaries remain useful; no rule bans mocks or literal expected values merely because of their form. An implementation-only refactor that preserves the contract should not break the test.

An independently mandated static or source contract is not a tautology. For example, an external loader may require an exact public manifest key or a protocol may fix an emitted byte value. Cite that independent obligation, inspect the actual consumed artifact, and identify the consumer-breaking change the check catches. This enforces a real contract; calling private code shape an architecture contract does not make a self-derived expectation independent. Apply the [retention bar](#retention-bar), without using it to waive this prohibition.

| Bad: the test supplies its own answer | Good: independent claim and observable result |
| --- | --- |
| Compare `quote(order)` with another call to `quote(order)`, or a copy of its current formula | Use a separately specified pricing example through the public quote entry; name a wrong rounding or omitted discount it catches |
| Mock `reserveStock` to decrement a local counter, then assert that counter | Call the real reservation entry with competing requests for the last item and observe successes and stored stock; setup must allow the race being checked |
| Grep for a private `authorize()` call and declare access denied | Invoke the real public operation as the prohibited caller and observe denial with no protected effect |
| Copy a constant's current value into an assertion without another source of truth | Assert a real emitted protocol field equals the value required by the independently cited protocol; a wrong wire value fails even if private code is renamed |

Finding an existing tautology is not permission to delete tests or change accepted assertions. Report it to the owning workflow and preserve [test consent](no-unrequested-tests.md) and its remediation gates.

## Authoring gate

An accepted test still passes this gate before it lands. Answer four questions, and write the test only once all four have answers:

1. What observable behavior, invariant, or independent contract does it protect, and what is the independent source of its expected outcome?
2. What plausible incorrect behavior makes it fail, and do setup or mocks hide that failure mode? Apply [No tautological tests](#no-tautological-tests).
3. Why does existing coverage not already catch that failure? Each contract has one primary test owner at the strongest boundary. Another layer needs its own risk the owner cannot reach, such as a transport or lifecycle failure. Extend a table-driven case or shared fixture instead of adding a near-duplicate test, and fold duplicated setup in the same change.
4. Does it need production code that only the test uses (export, flag, wrapper, injection hook)? If yes, test at the real boundary instead.

Then check it against every [junk pattern](#junk-patterns). A tautological test always fails the gate. Use the [retention bar](#retention-bar) to distinguish independently grounded contract checks from superficially similar implementation mirrors, not to excuse a tautology. A test that breaks under a behavior-preserving refactor asserts implementation, not behavior. Rewrite it at the owning boundary before it lands.

A bug regression test must fail on the pre-fix code for the intended reason and pass after the fix at the owner. A setup failure is not that red baseline. If the pre-fix run is unavailable, report the missing evidence; do not claim the test reproduced the bug. One regression at the owner covers the bug, not a replay at every layer the scenario crosses.

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
| Reuse the repo | Use its runner, layout, fixtures, and helpers instead of a new framework |
| Focused run | Run the focused test file or filter. Widen only when that is inconclusive or the user asks |
| Code quality and structure | Helpers throw on setup failure (`quality:throw-at-boundaries`); comments summarize the approved lock (`quality:comments`); exercise the service or deep-module public API, not internals (`structure:deep-public-surface`) |

## Lock brief

Batch every known main claim in one message ([Asking the user](writing-style.md#asking-the-user)) and wait. Every brief has a no. Write tests once each brief is approved.

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

1. Name the behavior to lock and the outside change it should catch.
2. Find the public export and nearby tests. If the runner or layout is unclear, ask once.
3. Run the [authoring gate](#authoring-gate).
4. Draft every needed Why / What / How brief, batch them for approval, and wait.
5. If `/task` or `/task-with-tests` already collected that approval, reuse it. Require the grilled rule id on each of those briefs. If the user corrected the rule after approval, stop and return the brief to the skill that collected it.
6. Write the tests from the approved Why / What / How through the named public entry. Keep the set small, put the approved comment on each main test, and leave refactoring out of the change.
7. Run the focused test, not the whole suite. Check the result against the approved claim.
8. If the focused test fails on existing behavior, stop and report it. Change production code only at a user request. Under `/task-with-tests` the tests come before the code, so a failure is the expected [red baseline](../task-with-tests/reference.md#red-baseline): record it, and the build turns it green.
9. Report with the handoff below.

### Handoff

```markdown
## Behavior locks
- **Claim:** <approved Why / What / How>
- **Files:** <changed test files>
- **Verification:** `<command>`: pass | fail
- **Break signal:** <outside edit that makes this test fail>
```

# Testing

How tests are written in this pack. A test is a verification step written as code, so it can run again on every change. [`/verification`](../verification/SKILL.md) owns writing them: it proposes the checks worth keeping and writes the ones the user names. [`/test-audit`](../test-audit/SKILL.md) prunes and repairs existing tests against the same bar.

Parts of the authoring gate, junk patterns, and retention bar are adapted from [openclaw test-audit](https://github.com/openclaw/openclaw/tree/main/.agents/skills/test-audit) (MIT).

## No drive-by tests

When a test may be written at all lives in [no-unrequested-tests.md](no-unrequested-tests.md). Open it first. This file covers how to write a test the user already accepted.

## When a test is written

Only after the user accepted it, as defined in [no-unrequested-tests.md](no-unrequested-tests.md#accepted-means).

## When a test is worth writing

A test earns its place when it repeats a verification that matters: a real user flow or a real boundary that could break without anyone noticing. Pick the highest layer that proves it:

1. **End to end:** the user's flow through the running app (browser, CLI, or API client) against local or disposable services.
2. **Integration:** one real boundary (an endpoint, mutation, job, webhook, migration, or query) against the real database or runtime, faking only the outside network.
3. **Unit:** only for logic that is hard to get right and must always return the right value, such as an obscure math function (tax rounding, a scheduling formula, a scoring curve). Changing it safely needs every case pinned. Say why no higher layer fits.

Skip thin wrappers, formatters, UI chrome, generated code, types-only files, coverage targets, and [tautological tests](#no-tautological-tests). If nothing qualifies, propose nothing.

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

Finding an existing tautology is not permission to delete tests or change accepted assertions. Report it to the owning workflow and preserve [test consent](no-unrequested-tests.md).

## Authoring gate

An accepted test still passes this gate before it lands. Answer four questions, and write the test only once all four have answers:

1. What observable behavior, invariant, or independent contract does it protect, and what is the independent source of its expected outcome?
2. What plausible incorrect behavior makes it fail, and do setup or mocks hide that failure mode? Apply [No tautological tests](#no-tautological-tests).
3. Why does existing coverage not already catch that failure? Each contract has one primary test owner at the strongest boundary. Another layer needs its own risk the owner cannot reach, such as a transport or lifecycle failure. Extend a table-driven case or shared fixture instead of adding a near-duplicate test, and fold duplicated setup in the same change.
4. Does it need production code that only the test uses (export, flag, wrapper, injection hook)? If yes, test at the real boundary instead.

Then check it against every [junk pattern](#junk-patterns). A tautological test always fails the gate. Use the [retention bar](#retention-bar) to distinguish independently grounded contract checks from superficially similar implementation mirrors, not to excuse a tautology. A test that breaks under a behavior-preserving refactor asserts implementation, not behavior. Rewrite it at the owning boundary before it lands.

A bug regression test must fail on the pre-fix code for the intended reason and pass after the fix at the owner. A setup failure does not count as that failure. If the pre-fix run is unavailable, report the missing evidence; do not claim the test reproduced the bug. One regression at the owner covers the bug, not a replay at every layer the scenario crosses.

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
| Named by the user | Written only after the user named it from a [proposal](#proposal) or asked for it |
| Cite the rule | When the work has a rule that must stay true (Rule N), the test names it |
| Small set | Core outcome, critical guard, meaningful edge, and the known regression when the proposal named one. A few scenarios over combinatorial or snapshot theater |
| Reuse the repo | Use its runner, layout, fixtures, and helpers instead of a new framework |
| Focused run | Run the focused test file or filter. Widen only when that is inconclusive or the user asks |
| Code quality and structure | Helpers throw on setup failure (`quality:throw-at-boundaries`); comments summarize the proposal (`quality:comments`); exercise the service or deep-module public API, not internals (`structure:deep-public-surface`) |

## Proposal

`/verification` lists the tests worth keeping in its report and keeps going; nothing waits for an answer. Number them, highest layer first:

```markdown
### Tests worth keeping
1. **E2E: a double submit charges once** (Rule 2). Why: a double click could charge twice. What: one charge per retry key. How: submit checkout twice in the browser and assert one charge in the Stripe test log.
2. **Integration: only the owner can refund** (Rule 3). Why: a caller could refund someone else's payment. What: a non-owner is rejected. How: call `refundPayment` as a non-owner and assert the rejection and no refund row.
```

The report's **Next** line says how to keep them: "Reply `tests 1 2` to write them."

## Required test comment

Put the proposal's three lines on each main test, in the repository's comment style:

```ts
/**
 * Why: <why>
 * What: <what>
 * How: <how>
 */
it("states the locked behavior", () => {
  // Assert an observable result.
});
```

## Process

1. Start from a verification that passed, or a reproduced bug, and the rule it proves.
2. Pick the [highest layer](#when-a-test-is-worth-writing) that proves it, and find the repository's runner, layout, and nearby tests. If the runner is unclear, look it up in CI configuration and manifests.
3. Run the [authoring gate](#authoring-gate).
4. If the user has not named or asked for this test, add it to the [proposal](#proposal) and stop there.
5. Write it through the real entry with the proposal's Why / What / How as its comment. Keep the set small and leave refactoring out of the change.
6. Run the focused test, not the whole suite. A failure on existing behavior is a bug report: report it, and change production code only at a user request.
7. Report with the handoff below.

### Handoff

```markdown
## Tests written
- **Claim:** <Why / What / How>
- **Files:** <changed test files>
- **Verification:** `<command>`: pass | fail
- **Break signal:** <outside edit that makes this test fail>
```

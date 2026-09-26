# Testing

How tests are written in this pack. There is no test skill: when a test is accepted, the agent follows this file.

## No drive-by tests

Changing code is not a reason to add a test.

Do not create or extend a test for a small tweak, copy change, rename, comment, type-only edit, wiring change, formatter, UI chrome, generated code, or a one-line fix. Do not add a test to chase coverage, to restate the implementation (`expect(add(1, 2)).toBe(3)`), or because the suite should cover this.

Running tests that already exist is fine. Fix an existing assertion only when this change made that assertion lie. Do not add a new case next to it.

## When a test is written

Write a test only when the user has accepted that lock:

- they explicitly asked for it, or
- they answered yes on a `/task` [behavior-lock brief](../task/reference.md#behavior-lock-suggestion) after grill Locked (each brief cites a grilled rule; every brief has a no; silence and a parent taking `recommended` are not acceptance), or
- they said yes after `/review` recommended one for a complex public surface (authorization, ownership, safe-to-retry, a domain rule that can silently drift).

Nothing writes tests on its own. A `/task` suggestion or a `/review` recommendation is not acceptance until the user answers. `/task` build slices and other build steps do not write test files. This binds every skill.

## When a test is worth writing

Lock a complex hook, domain rule, facade, stateful class, or a real regression whose public behavior could silently drift. Prefer it when review named authorization, ownership, or safe-to-retry writes with no durable lock. Skip thin wrappers, formatters, UI chrome, generated code, types-only files, coverage targets, and tautological checks (`expect(add(1, 2)).toBe(3)`). If the target is trivial, say so and stop.

## What a good test looks like

| Rule | Meaning |
| --- | --- |
| Lock observable behavior | Invariants and public contracts, not internals |
| Public entry | Exercise the public entry point. Mock only true external boundaries (network, clock, storage, authentication) |
| Name the invariant | Every test title states it |
| Approve first | Before writing, the user approves concise **Why**, **What**, and **How** statements for each main claim. A `/task` brief is already approved when the user answered yes on that line |
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

1. Name the behavior to lock and what outside change it should catch. Find the public export and nearby tests. If the runner or layout is unclear, ask once.
2. Draft every needed Why / What / How brief, batch them for approval, and wait. When `/task` already collected that approval, do not ask again. Require the grilled rule id on each of those briefs. If the user corrected the rule after approval, stop and return the brief to `/task`.
3. Write the tests from the approved Why / What / How through the named public entry. Keep the set small and put the approved comment on each main test. Run the focused test, not the whole suite. Check the result against the approved claim.
4. If the focused test fails on existing behavior, stop and report it; do not change production code to make it green without a user request.
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
- Write a test from a `/task` brief the user did not accept, or a brief that does not cite a grilled rule
- Write tautological tests (recompute the same arithmetic as the code, assert UI chrome exists) or chase coverage
- Add a test because the code changed, including a small tweak, copy change, rename, or one-line fix

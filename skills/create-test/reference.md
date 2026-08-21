# Lock brief and handoff

## Approval batch

```markdown
## Lock brief — <symbol>
- Why: <risk if behavior changes>
- What: <observable contract or invariant>
- How: <public entry, setup, and assertion>

## Questions
Reply like: 1a

1. Approve this lock brief?
   - a) yes ← recommended
   - b) no — say what to change
```

Batch all known main claims in the same first message. Do not write tests until
each brief is approved.

## Required test comment

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

Use the repository's comment style and keep the comment to those three
approved lines.

## Handoff

```markdown
## Behavior locks
- **Claim:** <approved Why / What / How>
- **Files:** <changed test files>
- **Verification:** `<command>` — pass | fail
- **Break signal:** <outside edit that makes this test fail>
```

If the runner or layout is unclear, ask once. If the focused test fails on
existing behavior, stop and report it; do not change production code to make it
green without a user request.

## Process

1. Read the public export, its callers, and existing nearby tests. State what
   behavior is being locked and what outside change it should catch.
2. Draft every needed Why / What / How brief, batch them for approval, and wait.
   Do not write tests until each brief is approved.
3. After approval, dispatch a `tester` Task per
   [../pack-shared/subagents.md](../pack-shared/subagents.md). The brief is the
   approved Why / What / How, public entry, and paths — **what**, not a recipe
   of assertions. The tester owns **how** (scenario set, tests, comments,
   focused run). Review the Completion against the approved claim.
4. Report the approved claim, files changed, command result, and one sentence
   about what would turn the test red.

Do not write tests on the main agent after approval. Never auto-start this
skill or dispatch `tester` without a user start.

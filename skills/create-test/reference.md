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

1. Name the behavior to lock and what outside change it should catch. If the
   public export or nearby tests need a noisy hunt, pick `explorer`. Do not
   grep the tree on the main agent.
2. Draft every needed Why / What / How brief, batch them for approval, and wait.
   Do not write tests until each brief is approved.
3. **Tester** always writes the tests. Dispatch `tester` per
   [../pack-shared/subagents.md](../pack-shared/subagents.md) with the approved
   Why / What / How, public entry, and paths — **what**, not a recipe of
   assertions. Tester owns **how**. Review the Completion against the approved
   claim. Never write tests on the main agent.
4. Report the approved claim, files changed, command result, and one sentence
   about what would turn the test red.

Never auto-start this skill. Never skip `tester` when tests are the job.

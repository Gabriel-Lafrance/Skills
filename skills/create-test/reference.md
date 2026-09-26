# Lock brief and handoff

## Approval batch

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
- **Verification:** `<command>`: pass | fail
- **Break signal:** <outside edit that makes this test fail>
```

If the runner or layout is unclear, ask once. If the focused test fails on
existing behavior, stop and report it; do not change production code to make it
green without a user request.

## Process

1. Name the behavior to lock and what outside change it should catch. Find the
   public export and nearby tests.
2. Draft every needed Why / What / How brief, batch them for approval, and wait.
   Do not write tests until each brief is approved. When `/task` already
   collected that approval, do not ask again. Require the grilled rule id on
   each of those briefs. If the user corrected the rule after approval, stop
   and return the brief to `/task`.
3. Write the tests from the approved Why / What / How through the named public
   entry. Keep the set small: core outcome, critical guard, meaningful edge,
   and the known regression when the brief named one. Put the approved
   three-line comment on each main test. Run the focused test, not the whole
   suite. Check the result against the approved claim.
4. Report the approved claim, files changed, command result, and one sentence
   about what would turn the test red.

Never auto-start this skill. A `/task` suggestion is not a start until the user accepts the brief.

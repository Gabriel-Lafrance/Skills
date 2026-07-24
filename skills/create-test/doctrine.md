# Behavior-lock doctrine

## Apply only when

Use this skill for a complex hook, domain rule, facade, stateful class, or a
real regression whose public behavior could silently drift. Skip thin wrappers,
formatters, UI chrome, generated code, types-only files, and coverage targets.

## Rules

1. Lock observable behavior, invariants, and public contracts—not internals.
2. Exercise the public entry point. Mock only true external boundaries such as
   network, clock, storage, or authentication.
3. Name the invariant in every test title.
4. Before writing, the user approves concise **Why**, **What**, and **How**
   statements for each main claim.
5. Prefer a few high-conviction scenarios over combinatorial or snapshot
   theater.
6. Reuse the repository's runner, layout, fixtures, and helpers. Do not add a
   framework.
7. Run only the focused test file or filter unless that is inconclusive or the
   user asks otherwise.
8. Match `/taste`: helpers throw on setup failure; comments summarize the
   approved lock and do not narrate the test.

## Process

1. Read the public export, its callers, and existing nearby tests. State what
   behavior is being locked and what outside change it should catch.
2. Draft every needed Why / What / How brief, batch them for approval, and wait.
3. Pick the smallest scenario set: core outcome, critical guard, meaningful
   edge, and a known regression when applicable.
4. Write tests through the public API. Keep fixture helpers local and DRY.
5. Add the approved three-line comment above each main test, using the
   repository's comment style.
6. Run the focused test. Confirm a behavior-breaking edit would fail and a
   harmless extraction would remain green.
7. Report the approved claim, files changed, command result, and one sentence
   about what would turn the test red.

## Boundaries

- Do not modify production code just to make a test convenient unless the user
  explicitly asks.
- Do not start `/goal`, expand into refactoring, or write tests before approval.
- `/goal`, `/implement`, `/repair`, and `/validate` never invoke this skill or
  write test files.

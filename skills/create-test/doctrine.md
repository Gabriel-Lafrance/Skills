# Create Test doctrine

## Job

Write durable behavior-lock tests for a complex public surface after review recommends a lock.

## Owns

The Why / What / How approval gate, writing the approved tests, and the lock report.

## Does not own

- Production code changes (unless the user explicitly asks)
- `/task` build slices and `/review`
- Numbered how-to: [`reference.md`](reference.md#process)

## Cite keys

none (uses `taste:*` and `architecture:*`)

## Bars

| Rule | Meaning |
| --- | --- |
| Lock observable behavior | Invariants and public contracts, not internals |
| Public entry | Exercise the public entry point. Mock only true external boundaries (network, clock, storage, authentication) |
| Name the invariant | Every test title states it |
| Approve first | Before writing, the user approves concise **Why**, **What**, and **How** statements for each main claim. A `/task` brief is already approved when the user answered yes on that line |
| Cite the grilled rule | A lock that came from `/task` names the rule that must stay true it locks (Rule N). No rule, no test |
| High-conviction set | A few scenarios over combinatorial or snapshot theater |
| Reuse the repo | Runner, layout, fixtures, helpers. Do not add a framework |
| Focused run | Only the focused test file or filter unless that is inconclusive or the user asks otherwise |
| Taste and architecture | Helpers throw on setup failure (`taste:throw-at-boundaries`); comments summarize the approved lock (`taste:comments`); exercise the service or deep-module public API, not internals (`architecture:deep-public-surface`) |

## Output

Approval brief, required test comment, and handoff live in [`reference.md`](reference.md).

## Apply

Use this skill for a complex hook, domain rule, facade, stateful class, or a real regression whose public behavior could silently drift. Prefer it when review named authorization, ownership, or safe-to-retry writes with no durable lock. Skip thin wrappers, formatters, UI chrome, generated code, types-only files, coverage targets, and tautological checks (`expect(add(1, 2)).toBe(3)`).

The user starts this skill. `/task` may continue it only for briefs the user accepted after grill Locked, and each of those briefs cites the grilled rule. `/review` may recommend a lock the task did not offer; the user starts this skill for that recommendation. Ordinary edits do not get tests.

## Anti-patterns

- Modifying production code just to make a test convenient unless the user explicitly asks
- Starting `/task`, expanding into refactoring, or writing tests before approval
- Starting this skill without a user start, or from a `/task` brief the user did not accept
- A `/task` brief that does not cite a grilled rule
- `/task` build slices, `/design`, and other build steps invoking this skill or writing test files
- Tautological tests (recompute the same arithmetic as the code, assert UI chrome exists) or coverage theater
- Adding a test because the code changed, including a small tweak, copy change, rename, or one-line fix
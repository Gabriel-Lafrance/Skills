# Create Test doctrine

## Job

Write durable behavior-lock tests for a complex public surface after review recommends a lock.

## Owns

The Why / What / How approval gate and the lock report. Tester always writes the tests.

## Does not own

- How to write the test after approval (`tester`)
- Production code changes (unless the user explicitly asks)
- `/task` / implement / review
- Numbered how-to: [`reference.md`](reference.md#process)

## Cite keys

none (uses `taste:*` and `architecture:*`)

## Bars

| Rule | Meaning |
| --- | --- |
| Lock observable behavior | Invariants and public contracts, not internals |
| Public entry | Exercise the public entry point. Mock only true external boundaries (network, clock, storage, authentication) |
| Name the invariant | Every test title states it |
| Approve first | Before writing, the user approves concise **Why**, **What**, and **How** statements for each main claim |
| High-conviction set | A few scenarios over combinatorial or snapshot theater |
| Reuse the repo | Runner, layout, fixtures, helpers. Do not add a framework |
| Focused run | Only the focused test file or filter unless that is inconclusive or the user asks otherwise |
| Taste and architecture | Helpers throw on setup failure (`taste:throw-at-boundaries`); comments summarize the approved lock (`taste:comments`); exercise the service or deep-module public API, not internals (`architecture:deep-public-surface`) |

## Output

Approval brief, required test comment, and handoff live in [`reference.md`](reference.md).

## Apply

Use this skill for a complex hook, domain rule, facade, stateful class, or a real regression whose public behavior could silently drift. Prefer it when review named authorization, ownership, or safe-to-retry writes with no durable lock. Skip thin wrappers, formatters, UI chrome, generated code, types-only files, and coverage targets.

This skill is a user start. Do not nest it under `/task` or start it automatically. Only `/code-review` and `/pr-review` may recommend a lock; only the user starts this skill. Review may recommend it; nothing auto-invokes it. **Tester** always writes the tests; the main agent never does.

## Anti-patterns

- Modifying production code just to make a test convenient unless the user explicitly asks
- Starting `/task`, expanding into refactoring, or writing tests before approval
- Writing tests on the main agent, or skipping `tester` when tests are the job
- Starting this skill without a user start
- `/task`, `/implement`, `/design`, and other build skills invoking this skill or writing test files

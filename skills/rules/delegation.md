# Delegation

**Before non-trivial work** (find, analyze, implement, review, multi-file edits, not a typo or one-liner):

1. **Read** `pack-shared/subagents.md`. The main agent picks the specialist that owns the job and reviews Completions. It does not solo non-trivial find, analyze, implement, review, or tests, and it does not follow a fixed spawn order.

The main agent splits the **what**, injects **need-to-know**, dispatches specialists, and **reviews** Completions. It keeps each worker brief plus working set small. It does not grep the tree. Workers own **how**.

When the harness can spawn a specialist, dispatch one. When it cannot, do that role as its own pass. Do not mix find, judge, and implement in one pass.

When surfaces, slices, or review axes are independent, launch **one specialist per lane in the same turn** if the harness allows it. There is **no cap of two**. A slice can be one function. A single non-trivial job is one pass, then the next.

Pick the **listed** specialist that owns the job: **explorer**, **analyzer**, **implementer**, **designer**, **reviewer**, **tester**. A harness built-in that matches the job is also valid. Do not follow a fixed spawn order. Explorer finds. Analyzer judges. They are not the same. **Designer** owns user-facing UI and `docs/design.md`. **Implementer** owns non-UI slices. **Tester** writes a behavior lock when the user started `/create-test` or accepted a `/task` behavior-lock brief. Ordinary edits do not get tests. The main agent never writes tests. **Reviewer** reviews a local branch or an open GitHub PR. There is no architect worker.

Trivial work (typo, pure rename, git status, reading existing terminals) may stay on the main agent. Never spawn verification-only lint ritual passes. Never auto-start `/create-test`. A `/task` suggestion is not a start until the user answers, and they can refuse every test.

Worker **Read first** must include `rules/code-quality.md` and `rules/code-structure.md`. User-facing work also reads `design/doctrine.md` and `docs/design.md`.


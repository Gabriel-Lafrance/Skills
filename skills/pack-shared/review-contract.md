# Review contract

## Job

Shared review evidence and worker output for `/code-review` and `/pr-review`. Each skill owns its own remediation or posting behavior. There is no Design-review skill and no Design axis.

## Owns

Fixed-point inputs, modes, evidence bar, finding record, one review output fence (including PR extras on `/pr-review`), one Correctness hunt, baseline defects, severity mapping, and when to recommend `/create-test`.

## Does not own

- Taste and architecture bars: cite `taste:*` and `architecture:*`
- UX bars and `docs/design.md`: [`../design/doctrine.md`](../design/doctrine.md)
- Blocker vs follow-up judgment table and naming alignment: [`../code-review/doctrine.md`](../code-review/doctrine.md)
- PR extras, Pass A/B, posting: [`../pr-review/doctrine.md`](../pr-review/doctrine.md)

## Inputs

Pin a fixed point and inspect the diff. Resolve specification from the current
user request, ticket, PR body, committed repository documentation, and relevant
execution context supplied by a parent. Do not depend on hidden review files.

## Modes

| Mode | Scope | Required work |
| --- | --- | --- |
| `initial` | Full shipped diff and available spec | Standards + Spec in parallel |
| `remediation` | Named findings, fix diff, touched paths, and direct callers | Verify named findings, regressions, and correctness in the changed surface |
| `full-rescan` | Full diff after meaningful change or user request | Run `initial` depth again and adjudicate prior PR threads when present |

### Follow-up partition (PR)

On a `/pr-review` follow-up, after historical Pass A:

1. Partition `previousReviewedHead..currentHead`.
2. Apply `remediation` to the addressed-findings surface inside that range.
3. Apply `initial` depth to **newly introduced** files/hunks in that range that
   are outside the remediation set.
4. Use `full-rescan` only on explicit user request or material scope expansion.

Do not run a broad architecture hunt during remediation of named findings. Do
not silently turn a follow-up into a full rescan of the entire PR. Do not let
new commits outside the remediation set skip review.

## Evidence bar

A blocker about a runtime failure, guard, concurrency, error path, retry, queue,
lock, or hardening need requires all of:

1. A reachable trigger.
2. Concrete evidence from the diff, a path walk, a violated rule, a signal, or
   a directly provable exploit.
3. Material correctness, security, data, availability, or acceptance impact.
4. The smallest authoritative fix.

These **are** reachable triggers. Do not dismiss them as theoretical:

- A public write in the diff that touches user data with no identity check
- A patch/delete/read of another row with no ownership or tenant check
- A UI-only guard (disabled button, hidden route, client `if`) while the public
  write still runs
- A webhook, payment, or insert that can duplicate on replay
- `Date.now()` / randomness inside a query
- An un-awaited write (`ctx.db.patch` / `insert` / `scheduler.runAfter` without
  `await`)
- Unbounded `collect()` or `.filter` scan on a growing table
- A `catch` that swallows or logs-and-continues at a boundary that should fail
- A secret, token, or private key in the shipped diff

Do not report imaginary futures or recommend extra coordination machinery
without evidence that a direct guard is insufficient.

## Finding record

Stable id grammar: `axis-rule-location` (example: `standards-never-nest-checkout-place-order`).

```markdown
- **<id>** · **standards|spec|cross** · **blocker|follow-up|nit**
  - **Where:** `path` (symbol or line)
  - **Rule:** `INV-*` | acceptance criterion | doctrine | none
  - **Trigger:** <required for runtime-risk findings>
  - **Evidence:** <hunk, path walk, or signal>
  - **Impact:** <why it matters>
  - **Fix:** <smallest authoritative direction>
```

Fold recurring sites with the same root cause and fix shape into one record.
Different root causes get different records. Drop duplicates by finding id. On a
PR, include the id in the final comment as `**Finding:** \`<id>\``. The
GitHub finding thread and that visible id are the durable record.

## Output

Standards workers **must** Read `/taste` and `/architecture` doctrines this
turn ([standards.md](standards.md)). They **must** run taste Cite keys (Named
principles) using **plain (Classic)** (`keep jobs apart (SoC)`) and cite those
keys in finding **Rule** fields when violated. Never acronym-only (`SoC
violation`) and never the paraphrase without the classic name. User-facing
notes must be ordinary sentences ([plain-language.md](plain-language.md)). On
`initial` / `full-rescan`, also run the code-review naming alignment pass, the
Architecture sweep, the Correctness hunt, and the Baseline defects scan. The
parent rejects Standards output that lacks the Principles, Architecture, or
Correctness tables, or that skipped a doctrine Read.

Spec workers fill the **Spec matrix** with every Done-when row, every rule that
must stay true, each user-visible state the diff touches (enabled, disabled,
loading, empty, error), and named unchanged behavior. Do not invent rows when
no specification exists; say so, and still let Standards run the Correctness
hunt (bugs are not "the ticket forgot to mention them").

UX bars live in `/design` while building. Do not dispatch a Design worker,
return a Design matrix, or run an Experience or Craft floor.

The parent provides the fixed-point diff, relevant spec, Active Rules, and
format below. It dispatches Standards and Spec as parallel Tasks (plus extra
Tasks when the diff has independent surfaces), reviews Completions, and
rejects and relaunches a narrative-only response once.

Workers report no finding explicitly when their axis is clean. Mark each sweep
row `clear`, `finding` (with finding id), or `none` when that check has no
surface in the diff (for example cheap-reads on a copy-only change). The parent
controls the dispatch and follows the [execution context](execution-context.md)
contract for models and completion reporting.

### Review output

```markdown
## Standards findings
- <finding record>

## Principles sweep
| Principle | Status | Note |
| --- | --- | --- |
| Keep it simple (KISS) | clear \| finding | … |
| Keep jobs apart (SoC) | clear \| finding | … |
| One altitude (SLAP) | clear \| finding | … |
| Read or write, not both (CQS) | clear \| finding | … |
| Fail fast (Fail Fast) | clear \| finding | … |
| Leave it cleaner (Boy Scout Rule) | clear \| finding | … |
| Related together (Cohesion / Law of Demeter) | clear \| finding | … |
| Safe to retry (Idempotency) | clear \| finding \| none | … |
| Say what happens (explicit over implicit) | clear \| finding | … |
| No surprises (PoLA) | clear \| finding | … |
| Honest names (intention-revealing names) | clear \| finding | … |
| Trust the server (never trust the client) | clear \| finding \| none | … |
| Types tell the truth (make illegal states unrepresentable) | clear \| finding \| none | … |
| Don’t repeat yourself (DRY) | clear \| finding \| none | … |

## Architecture sweep
| Check | Status | Note |
| --- | --- | --- |
| Services / public API | clear \| finding \| none | … |
| Simple public surface | clear \| finding \| none | … |
| One-job helpers (reuse, not copy) | clear \| finding \| none | … |
| Folders / placement | clear \| finding \| none | … |
| Cheap reads (store on write) | clear \| finding \| none | … |
| Indexes / no scan | clear \| finding \| none | … |
| Pagination / no unbounded collect | clear \| finding \| none | … |
| Deterministic queries | clear \| finding \| none | … |
| Authority on the write | clear \| finding \| none | … |
| Safe to retry writes | clear \| finding \| none | … |
| Prior mistakes not copied | clear \| finding \| none | … |

## Correctness hunt
| Class | Status | Note |
| --- | --- | --- |
| Identity on public writes | clear \| finding \| none | … |
| Ownership / tenant | clear \| finding \| none | … |
| Client-only guard | clear \| finding \| none | … |
| Replay / double-submit | clear \| finding \| none | … |
| Race / lost update | clear \| finding \| none | … |
| Un-awaited write | clear \| finding \| none | … |
| Swallowed error | clear \| finding \| none | … |
| Null / empty / off-by-one on the happy path | clear \| finding \| none | … |
| Cross-file stale caller | clear \| finding \| none | … |
| Secrets in the diff | clear \| finding \| none | … |

## Spec matrix
| Requirement | Status | Evidence |
| --- | --- | --- |
| <Done when / rule / state / unchanged> | met \| gap \| none | … |

## PR extras (`/pr-review` only)
| Extra | Status | Note |
| --- | --- | --- |
| Body vs diff | clear \| finding \| none | … |
| Historical thread | clear \| finding \| none | … |
| Migration / backfill | clear \| finding \| none | … |
| Breaking public API | clear \| finding \| none | … |
```

One review pass. Return Standards findings, Principles, Architecture,
Correctness hunt, and the Spec matrix. `/pr-review` also returns the four PR
extras rows in this same fence. Secrets stay in the Correctness hunt, not in
PR extras. There is no Design axis, no second adversarial wave, and no hunt
re-inspect.

### Baseline defects (Standards, after the tables)

If the shipped diff introduces any of these, it is a finding. Cite the matching
key (`taste:never-nest`, `taste:cyclomatic-cap`, `taste:dont-repeat-yourself`,
`taste:no-dead-code`, `taste:throw-at-boundaries`, `taste:one-export-per-file`,
`taste:static-imports`, `taste:oop-depth-cap`) or `taste:keep-it-simple`.
Findings still speak **plain (Classic)**. These are also `test:quality` (or `test:mutants`) hits when a runner exists; do not raise, skip, or delete a gate to go green:

- Nested control-flow pyramids
- A function with more than five independent paths (cyclomatic complexity (McCabe))
- Copy-paste twins of a concept already in-repo
- `{ success: false }` / Result bags for expected failure (fail fast (Fail Fast))
- `any` or Convex `v.any` on a public surface (types tell the truth (make illegal states unrepresentable))
- A public Convex write with no identity helper (trust the server (never trust the client))
- Clock or randomness inside a query (deterministic queries)
- Unused files, exports, or dependencies in the diff (no dead code (Knip))
- Dynamic `import()`
- New file with more than one main export
- Class or interface chain deeper than two
- Magic policy numbers at a call site that should be a named invariant
- Raising, skipping, or deleting `test:quality` (or lowering the `test:mutants` break threshold) to go green

## Severity mapping

| Canonical severity | `/code-review` | `/pr-review` |
| --- | --- | --- |
| `blocker` | Fix now | `Blocking` |
| `follow-up` | Follow-up | Chat-only by default; `Nit` only when a PR comment is useful |
| `nit` | Optional nit | `Nit` only when useful |

There is no unmapped `important` middle severity. `/pr-review` posts only
`Blocking` or `Nit`. Adapters do not re-explain this map.

## Behavior-lock recommendation

After an initial or full-rescan review, recommend `/create-test` only for a
complex architectural boundary with externally observable behavior and no
durable lock, especially authorization, ownership, and safe-to-retry writes.
Tell the user; do not invoke `/create-test` or write tests. After locks land,
`test:mutants` proves they bite: surviving mutants mean the lock is decoration.

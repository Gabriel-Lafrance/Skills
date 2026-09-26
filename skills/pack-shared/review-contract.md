# Review contract

## Job

Shared review evidence and output for `/review` (local branch diff or GitHub PR). `/review` owns remediation and posting. There is no Design-review skill and no Design axis.

## Owns

Inputs, modes, evidence bar, finding record, the review output fence (with PR extras), the Correctness hunt, baseline defects, severity mapping, and when to recommend `/create-test`.

## Does not own

- Taste and architecture bars: cite `taste:*` and `architecture:*`
- UX rules and `docs/design.md`: [`../rules/user-experience.md`](../rules/user-experience.md)
- Blocker vs follow-up judgment, naming alignment, PR extras: [`../review/doctrine.md`](../review/doctrine.md)
- Pass A/B and posting: [`../review/reference.md`](../review/reference.md)

## Inputs

Pin a fixed point and inspect the diff. Spec comes from the current user request, ticket, PR body, committed repository docs, and execution context a parent supplied. Do not depend on hidden review files.

## Modes

| Mode | Scope | Required work |
| --- | --- | --- |
| `initial` | Full shipped diff and available spec | Standards pass + Spec pass |
| `remediation` | Named findings, fix diff, touched paths, direct callers | Verify named findings, regressions, and correctness in the changed code |
| `full-rescan` | Full diff after meaningful change or user request | `initial` depth again; adjudicate prior PR threads when present |

### Follow-up partition (PR)

On a GitHub PR follow-up, after historical Pass A:

1. Partition `previousReviewedHead..currentHead`.
2. Apply `remediation` to the addressed-findings code in that range.
3. Apply `initial` depth to **newly introduced** files/hunks in that range outside the remediation set.
4. Use `full-rescan` only on explicit user request or material scope expansion.

No broad architecture hunt during remediation. No silent full rescan. New commits outside the remediation set still get reviewed.

## Evidence bar

A blocker about a runtime failure, guard, concurrency, error path, retry, queue, lock, or hardening need requires all of:

1. A reachable trigger.
2. Concrete evidence: the diff, a path walk, a violated rule, a signal, or a directly provable exploit.
3. Material correctness, security, data, availability, or acceptance impact.
4. The smallest authoritative fix.

These **are** reachable triggers, not theory:

- A public write touching user data with no identity check
- A patch/delete/read of another row with no ownership or tenant check
- A UI-only guard (disabled button, hidden route, client `if`) while the public write still runs
- A webhook, payment, or insert that can duplicate on replay
- `Date.now()` / randomness inside a query
- An un-awaited write (`ctx.db.patch` / `insert` / `scheduler.runAfter` without `await`)
- Unbounded `collect()` or `.filter` scan on a growing table
- A `catch` that swallows or logs-and-continues at a boundary that should fail
- A secret, token, or private key in the shipped diff

Do not report imaginary futures or recommend coordination machinery without evidence that a direct guard is insufficient.

## Finding record

Stable id grammar: `axis-rule-location` (example: `standards-never-nest-checkout-place-order`).

```markdown
- **<id>** · **standards|spec|cross** · **blocker|follow-up|nit**
  - **Where:** `path` (symbol or line)
  - **Rule:** Rule N | Done when item | doctrine | none
  - **Trigger:** <required for runtime-risk findings>
  - **Evidence:** <hunk, path walk, or signal>
  - **Impact:** <why it matters>
  - **Fix:** <smallest authoritative direction>
```

Fold sites with the same root cause and fix shape into one record; different root causes get separate records. Drop duplicates by id. On a PR, the final comment carries `**Finding:** \`<id>\``; the GitHub thread and that id are the durable record.

## Output

**Standards pass** (`initial` / `full-rescan`): apply [code-quality.md](../rules/code-quality.md) and [code-structure.md](../rules/code-structure.md) this turn ([standards.md](standards.md)). Standards also checks Knip and cyclomatic complexity: see [../review/static-checks.md](../review/static-checks.md). Run the Principles sweep, `review:naming-alignment`, the Architecture sweep, the Correctness hunt, and the Baseline defects scan. Missing tables or a skipped section means redo before reporting.

Cite principles as **plain (Classic)** (`keep jobs apart (SoC)`) in notes and in the finding **Rule** field; never acronym-only, never plain-only. User-facing notes are ordinary sentences ([plain-language.md](plain-language.md)).

**Spec pass**: one Spec matrix row per Done-when item, rule that must stay true, user-visible state the diff touches (enabled, disabled, loading, empty, error), and named unchanged behavior. With no spec, say so and add no rows; Standards still runs the Correctness hunt.

No Design pass, Design matrix, or Experience/Craft floor: UX rules in [user-experience.md](../rules/user-experience.md) apply while building.

Cover every independent part of the diff. Narrative-only output is incomplete. Mark each row `clear`, `finding` (with id), or `none` when the check has nothing to inspect (for example cheap reads on a copy-only change). One pass: no second adversarial pass, no hunt re-inspect. Secrets stay in the Correctness hunt, not PR extras.

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
| Don't repeat yourself (DRY) | clear \| finding \| none | … |

## Architecture sweep
| Check | Status | Note |
| --- | --- | --- |
| Services / public API | clear \| finding \| none | … |
| Simple public surface | clear \| finding \| none | … |
| One-job helpers (reuse, not copy) | clear \| finding \| none | … |
| Env var reuse (no synonym) | clear \| finding \| none | … |
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

## PR extras (GitHub PR only)
| Extra | Status | Note |
| --- | --- | --- |
| Body vs diff | clear \| finding \| none | … |
| Historical thread | clear \| finding \| none | … |
| Migration / backfill | clear \| finding \| none | … |
| Breaking public API | clear \| finding \| none | … |
```

### Baseline defects (Standards, after the tables)

Each of these in the shipped diff is a finding, cited by key and spoken **plain (Classic)**. Identity on public writes and clock/randomness in queries are covered by the Correctness hunt and Architecture sweep above.

| Defect | Key |
| --- | --- |
| Nested control-flow pyramids | `taste:never-nest` |
| New related files as mixed siblings with no owning folder | `architecture:folders` |
| A function with more than five independent paths (cyclomatic complexity (McCabe)) | `taste:cyclomatic-cap` |
| Copy-paste twin of a concept already in the repo | `taste:dont-repeat-yourself` |
| New env var whose job an existing var does (`FRONTEND_URL` while `SITE_URL` exists) | `taste:reuse-env` |
| `{ success: false }` / Result bags for expected failure (fail fast (Fail Fast)) | `taste:throw-at-boundaries` |
| `any` or Convex `v.any` on a public surface | types tell the truth (make illegal states unrepresentable) |
| Unused files, exports, or dependencies in the diff | `taste:no-dead-code` |
| Dynamic `import()` | `taste:static-imports` |
| New file with more than one main export | `taste:one-export-per-file` |
| Class or interface chain deeper than two | `taste:oop-depth-cap` |
| Magic policy number at a call site that should be a named invariant | `taste:keep-it-simple` |

## Severity mapping

| Canonical severity | Local branch | GitHub PR |
| --- | --- | --- |
| `blocker` | Fix now | `Blocking` |
| `follow-up` | Follow-up | Chat-only by default; `Nit` only when a PR comment is useful |
| `nit` | Optional nit | `Nit` only when useful |

No `important` middle severity. A GitHub PR review posts only `Blocking` or `Nit`. Adapters do not re-explain this map.

## Behavior-lock recommendation

After an `initial` or `full-rescan` review, recommend `/create-test` only for a complex architectural boundary with externally observable behavior and no durable lock (authorization, ownership, safe-to-retry writes). Tell the user; do not invoke `/create-test` or write tests. Skip a claim the user accepted or refused in the current `/task` lock batch, unless the shipped public contract differs from that brief.

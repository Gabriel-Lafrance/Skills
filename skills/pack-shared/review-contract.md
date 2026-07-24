# Review contract

This contract is shared by `/code-review` and `/pr-review`. It defines review
evidence and worker output; each skill owns its own remediation or posting
behavior.

## Inputs

Pin a fixed point and inspect the diff. Resolve specification from the current
user request, ticket, PR body, committed repository documentation, and relevant
execution context supplied by a parent. Do not depend on hidden review files.

## Modes

| Mode | Scope | Required work |
| --- | --- | --- |
| `initial` | Full shipped diff and available spec | Standards + Spec in parallel, then adversarial Wave 2 |
| `remediation` | Named findings, fix diff, touched paths, and direct callers | Verify named findings, regressions, and correctness in the changed surface |
| `full-rescan` | Full diff after meaningful change or user request | Run `initial` depth again and adjudicate prior PR threads when present |

Do not run a broad architecture hunt during remediation. Do not silently turn a
follow-up review into a full rescan.

## Evidence bar

A blocker about a runtime failure, guard, concurrency, error path, retry, queue,
lock, or hardening need requires all of:

1. A reachable trigger.
2. Concrete evidence from the diff, a path walk, a violated rule, a signal, or
   a directly provable exploit.
3. Material correctness, security, data, availability, or acceptance impact.
4. The smallest authoritative fix.

Do not report theoretical failures or recommend extra coordination machinery
without evidence that a direct guard is insufficient.

## Finding record

Use a stable finding id based on its axis, violated rule or root cause, and
strongest location, for example `standards-never-nest-checkout-place-order`.

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

## Worker artifacts

The parent provides the fixed-point diff, relevant spec, Active Rules, and
format below. It rejects and relaunches a narrative-only response once.

```markdown
## Standards findings
- <finding record>

## Spec matrix
| Requirement | Status | Evidence |
| --- | --- | --- |
| … | met | … |

## Adversarial findings
- <new finding record and why Wave 1 missed it>
```

Workers report no finding explicitly when their axis is clean. The parent
controls the dispatch and follows the [execution context](execution-context.md)
contract for models and completion reporting.

## Severity mapping

| Canonical severity | `/code-review` | `/pr-review` |
| --- | --- | --- |
| `blocker` | Fix now | `Blocking` |
| `follow-up` | Follow-up | Chat-only by default; `Nit` only when a PR comment is useful |
| `nit` | Optional nit | `Nit` only when useful |

There is no unmapped `important` middle severity. `/pr-review` posts only
`Blocking` or `Nit`.

## Behavior-lock recommendation

After an initial or full-rescan review, recommend `/create-test` only for a
complex architectural boundary with externally observable behavior and no
durable lock. Tell the user; do not invoke `/create-test` or write tests.

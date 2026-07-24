# Validate Flow Doctrine

**Gate out.** Use the shared [execution context](../pack-shared/execution-context.md):
the parent carries the contract in chat; validation judges whether the change
meets it.

## Required handoff

Before validation, the parent must provide in chat:

- Done when
- Active Rules, including enforcement and verification
- Every current slice: scope, acceptance criteria, lane, dependencies, and
  changed interface or handoff
- Relevant Ticket / PR and fixed Git point, if any

Use the named ticket / PR, Git diff/history, and repository code and rules as
evidence. They do not create user decisions or acceptance criteria. If Done
when, Active Rules, or applicable slice criteria are missing, stop and ask.

## Framing (pessimistic — required)

Do **not** assume the change works. It may be wrong, incomplete, unlinked, or
off-criteria. Every row needs evidence; silent “LGTM” is a process failure.

State whether every critical runtime path **works**, **won't work**, has a
**missing link**, or is **blocked**.

## Live evidence: terminals first

Match evidence to the criterion:

1. Read any relevant existing terminal first: frontend, backend, worker, test
   watcher, typecheck watcher, or `convex dev`.
2. Cite the useful signal from `terminals/<id>.txt` (or equivalent).
3. Use a narrow, fast command only for a remaining evidence gap: targeted
   typecheck or lint, one test, one smoke request, or an established repo
   health script.

Do not use ritual full suites, lint-everything, a second long-lived dev server,
or Convex MCP loops by default. Convex MCP is appropriate only when terminal
evidence cannot answer the question, shows an error needing diagnosis, or the
user asks for it.

For browser-reachable UI criteria, use [reference.md](reference.md) when
Browser capability is available. Browser evidence complements terminal signals;
it never follows from code alone. If tools, credentials, policy approval, safe
data, or the app are unavailable, mark the criterion **blocked** and say what
is needed.

## Process

### 1. Restate the bar

List every Done when, slice acceptance criterion, and Active Rule. For each
`INV-*`, check its named authoritative enforcement point and observable result.
Do not add scope.

### 2. Walk each runtime path

For each criterion or current slice, narrate the **runtime path**:

```markdown
### Path: <criterion or feature>
1. Entry: <route / UI / CLI / mutation caller>
2. → <module / function> (linked? yes/no — import, export, registration)
3. → <data / API / schema>
4. → <response / UI state>
**Verdict:** works | won't work | missing link (<what>) | blocked (<why>)
```

Hunt for unimported exports, unregistered routes/plugins/crons, schema fields
written but never read (or reverse), unread environment variables, and UI
actions without handlers (or handlers without UI). A missing link is a fail.

### 3. Walk cross-slice seams

When the inline context names two or more current slices, this is required
before a pass:

1. Read the Git diff and repo files each slice changed or hands off.
2. Walk imports, exports, route/API registration, schema↔callers,
   UI↔handlers, and environment reads across every stated dependency.
3. Find unused exports, orphaned registrations, one-sided schema changes,
   disconnected UI, and entry points that never import new code.
4. Record each seam below. A missing link is a fail; the parent creates a
   bounded fix slice and validation rechecks it.

With one slice, still perform its entry-point import check as part of the path
walk. No separate link-check replaces this step.

### 4. Check quality where relevant

| Check | When | Standard |
| --- | --- | --- |
| Taste | Code diff | `/taste`; failures fail validation |
| Scalability | Lists, metrics, aggregates, hot queries | `/architecture` write-path rules; state N/A only with a reason |
| Services | Domain capability | Features call an existing or extended service public API; do not fork it |
| Primitives | Inline Structure calls them out or the lane has one-job blocks | Reuse, do not fork; honor the stated primitive contract |
| Design | UI is in scope | `/design` doctrine and browser evidence |

Validation does not write tests to manufacture proof.

### 5. Report

```markdown
## Validation

**Context:** Ticket / PR <ref | none> · fixed point <ref | none>

| Criterion | Status | Evidence |
| --- | --- | --- |
| … | pass / fail / blocked | terminal / CLI / path walk |

### Code paths
| Path | Verdict | Missing link? |
| --- | --- | --- |
| … | works / won't / missing link / blocked | … |

### Active Rules
| ID | Rule | Enforcement verdict | Verification evidence |
| --- | --- | --- | --- |
| INV-1 | … | pass / fail / blocked | … |

### Cross-slice seams (two or more current slices)
| Seam | Verdict | Missing link? |
| --- | --- | --- |
| … | wired / missing link / blocked | … |

### Live signals
| Source | What it showed |
| --- | --- |
| terminals/<id>.txt | … |
| CLI: `<cmd>` | … |
| Browser: `<URL>` · `<viewport>` | `<flow/state>` → `<observed result>` |

### Quality checks
| Check | Status | Evidence |
| --- | --- | --- |
| Taste / primitives / scalability / design | pass / fail / N/A | … |

### Failures
- …

### Scope creep
- …
```

### 6. Next step

| Result | Parent action |
| --- | --- |
| All pass | Run `/code-review` when the parent flow requires it |
| Fail | Open the smallest in-chat fix slice, then revalidate |
| Blocked | Ask for the missing verification path or access |

## Anti-patterns

- Optimistic “it should be fine” or silent LGTM
- Reconstructing criteria from hidden files or a plan path
- Passing unlinked imports, routes, schemas, callers, or UI actions
- Skipping cross-slice seams when multiple inline slices exist
- Using generic Convex evidence for a types, lint, frontend, or API criterion
- Ritual MCP or broad commands when live terminal output already answers
- Claiming visual proof without Browser evidence
- Passing an unavailable visual/runtime environment
- Ignoring an Active Rule's named enforcement point
- Writing tests to “prove” validation

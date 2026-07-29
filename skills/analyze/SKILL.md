---
name: analyze
description: >-
  Stateless task analysis returned in chat. Supports explicit inline promotion
  to /goal and scoped remediation analysis for named code-review Fix-now
  blockers. Does not write tickets or automatic artifacts.
disable-model-invocation: true
---

# Analyze

**Execution context:** [../pack-shared/execution-context.md](../pack-shared/execution-context.md) · **Ask style:** [../pack-shared/asking.md](../pack-shared/asking.md) · **Variants:** [../pack-shared/variants.md](../pack-shared/variants.md) — standalone-only; use the no-flow message if flow is requested.

`/analyze` investigates a task, idea, ticket, PR, or review-fix backlog and returns an evidence-backed memo in chat. Its only in-goal use is review remediation of named Fix-now blockers. It never writes to Linear or GitHub.

## Contract

- Rediscover repository, ticket, PR, and diff facts from their live sources.
- Keep user decisions, rules, lanes, and promotion state visible in the execution context; never infer them from code.
- Return the analysis memo in chat. Do not create automatic runtime artifacts or hidden paths.
- Save a memo only when the user explicitly requests it and approves the destination.

## Process

1. Establish or refresh the relevant execution context and normalize the ask.
2. Investigate independent surfaces in parallel when useful, then synthesize the evidence.
3. Post the memo, including an inline `/goal` seed when the work is buildable.
4. For standard analysis, ask one batch for real unknowns, then offer the
   explicit hand-off choices in [doctrine.md](doctrine.md).
5. For review remediation, present every selected stable-finding analysis
   before the remediation-specific promotion choice.

**Read:** [doctrine.md](doctrine.md). **Always** apply `/taste` (KISS + named
principles). Apply `/architecture` when the ask touches structure, services,
folders, data shape, or duplicated domain logic — default to loading it unless
the ask is clearly a single-file pure-logic question with no placement decision.

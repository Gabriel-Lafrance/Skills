---
name: analyze
description: >-
  Stateless task analysis returned in chat. One-off research with
  promote-to-goal handoffs, or nested under a parent (write-ticket, just-do-it,
  review remediation). Does not write tickets or automatic artifacts.
disable-model-invocation: true
---

# Analyze

**Must read:** [../pack-shared/standards.md](../pack-shared/standards.md) — Read `/taste` and `/architecture` doctrines this turn before researching or posting the memo. Do not skip.

**Process:** [process.md](process.md)

**Execution context:** [../pack-shared/execution-context.md](../pack-shared/execution-context.md) · **Ask style:** [../pack-shared/asking.md](../pack-shared/asking.md)

`/analyze` investigates a task, idea, ticket, PR, or review-fix backlog and returns an evidence-backed memo in chat. It never writes to Linear or GitHub.

## Contract

- Rediscover repository, ticket, PR, and diff facts from their live sources.
- Keep user decisions, rules, lanes, and promotion state visible in the execution context; never infer them from code.
- Return the analysis memo in chat. Do not create automatic runtime artifacts or hidden paths.
- Save a memo only when the user explicitly requests it and approves the destination.

**Read:** [doctrine.md](doctrine.md). **Always** Read and apply `/taste` and
`/architecture` (see [standards.md](../pack-shared/standards.md)). Do not skip
architecture because the ask looks like a single file.

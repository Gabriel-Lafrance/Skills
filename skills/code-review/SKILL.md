---
name: code-review
description: >-
  Review a shipped diff for quality and whether it matches the request.
  Quality checks use /taste and /architecture (keep it simple, keep jobs
  apart, honest names, trust the server, types tell the truth, and related
  rules), a correctness hunt for reachable bugs, plus a pass for stale file and
  symbol names after renames. Two review waves, evidence-backed findings,
  and a bounded fix path. Use for branch, PR, or parent-flow review.
  User must invoke (not auto).
disable-model-invocation: true
---

# Code Review

**Must read:** [../pack-shared/standards.md](../pack-shared/standards.md). Read `/taste` and `/architecture` doctrines this turn before adjudicating Standards. Do not skip.

**Shared contracts:** [review](../pack-shared/review-contract.md) · [execution context](../pack-shared/execution-context.md) · [variants](../pack-shared/variants.md)

**Adapters:** [standalone](standalone.md) · [flow](flow.md) · [doctrine](doctrine.md) · [examples](examples.md)

Standards always load `/taste` and `/architecture`. Worker output uses the
review-contract **Wave 1** and **Wave 2** fences (Principles, Architecture,
Correctness hunt; Wave 2 hunt re-inspect). User-facing findings use ordinary
words ([plain-language.md](../pack-shared/plain-language.md)).

---
name: code-review
description: >-
  Review a shipped diff with separate Standards and Spec axes. Standards hard-
  require /taste KISS + named principles (SoC, SLAP, CQS, fail fast, Boy Scout,
  cohesion/coupling, idempotency, explicit, PoLA, honest names) and
  /architecture, plus a naming-alignment pass for stale files/symbols after
  renames. Adversarial Wave 2, evidence-backed findings, and remediation
  analysis before promoted fixes. Use for branch, PR, or parent-flow review.
  User must invoke (not auto).
disable-model-invocation: true
---

# Code Review

**Shared contracts:** [review](../pack-shared/review-contract.md) · [execution context](../pack-shared/execution-context.md) · [variants](../pack-shared/variants.md)

**Adapters:** [standalone](standalone.md) · [flow](flow.md) · [doctrine](doctrine.md) · [examples](examples.md)

Standards always load `/taste` (KISS + Named principles, including **Honest
names**) and `/architecture` when structure or writes are in play. Worker
output includes the **Principles sweep** table from the review contract.

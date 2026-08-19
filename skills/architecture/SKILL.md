---
name: architecture
description: >-
  Shape scalable code: one service per domain job, simple public APIs,
  one-job helpers inside those services, writes that check who may act,
  clear folders, cheap honest reads, and writes that are safe to retry.
  Use standalone to decide structure, or inside /goal before planning.
  Triggers: folders, services, split logic, data/reads, duplicating
  domain logic, auth on writes, Date.now in queries.
disable-model-invocation: true
---

# Architecture

**Must read:** [../pack-shared/standards.md](../pack-shared/standards.md). This skill *is* architecture; still Read `/taste` doctrine this turn before drafting a structure card. Do not skip.

**Ask style:** [../pack-shared/asking.md](../pack-shared/asking.md) · **Variants:** [../pack-shared/variants.md](../pack-shared/variants.md). Dual: [standalone.md](standalone.md) and [flow.md](flow.md).

Always load **flow** `/taste` (or Read its doctrine) before drafting a structure
card. Cite keys live in [doctrine.md](doctrine.md). Other skills load both
doctrines on every run via the standards contract.

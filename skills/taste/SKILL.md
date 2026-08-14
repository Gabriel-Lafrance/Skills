---
name: taste
description: >-
  Pack coding taste and named principles: KISS, SoC, SLAP, CQS, fail fast,
  Boy Scout, cohesion/coupling, idempotency, explicit over implicit, PoLA,
  honest names, complexity/entropy, never-nest, DRY, throw+try/catch, deep
  modules. Use standalone to audit or apply taste to a lane; parents load it
  before planning or writing code.
disable-model-invocation: true
---

# Taste

**Hard apply:** [../pack-shared/standards.md](../pack-shared/standards.md) — this skill *is* taste; still Read `/architecture` doctrine this turn. Other skills load both via that contract. Do not skip.

**Ask style:** [../pack-shared/asking.md](../pack-shared/asking.md) · **Variants:** [../pack-shared/variants.md](../pack-shared/variants.md) — dual. Choose exactly one of [standalone.md](standalone.md) or [flow.md](flow.md).

**Read:** [doctrine.md](doctrine.md) · [examples.md](examples.md)

Process and checks live in doctrine. Other skills Read this skill then doctrine
through [standards.md](../pack-shared/standards.md).
Parents (`/goal`, `/analyze`, `/grill-me`, `/implement`, `/architecture`) must
load flow `/taste` **and** flow `/architecture` before planning or writing code.

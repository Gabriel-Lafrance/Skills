---
name: architecture
description: >-
  Shape scalable code: domain services with public APIs, simple entry points,
  clear folders, write-path data design. Dual skill: agent picks standalone vs
  flow via variants.md. Use when adding features, splitting logic, designing
  data/reads, or about to dump files / duplicate domain logic. User must invoke.
disable-model-invocation: true
---

# Architecture

**Ask style:** [../asking.md](../asking.md) · **Variants:** [../variants.md](../variants.md)

## Variant

Choose **exactly one** per [variants.md](../variants.md) — never both:

- Standalone fits → Read [standalone.md](standalone.md) only
- Flow fits → Read [flow.md](flow.md) only
- Missing file → matching missing-variant message; do not invent process

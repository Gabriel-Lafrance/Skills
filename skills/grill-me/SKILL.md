---
name: grill-me
description: >-
  Relentless interview to sharpen intent until shared understanding. Batches
  questions (Reply like: 1a 2b — codes only); upserts .agents/temp/grills/
  theme files; under a goal, locks behavioral answers as Active Rules. Dual
  skill: agent picks standalone vs flow via variants.md. Use when sharpening
  fuzzy intent. User must invoke (not auto).
disable-model-invocation: true
---

# Grill Me

**Ask style:** [../pack-shared/asking.md](../pack-shared/asking.md) · **Variants:** [../pack-shared/variants.md](../pack-shared/variants.md)

## Variant

Choose **exactly one** per [variants.md](../pack-shared/variants.md) — never both:

- Standalone fits → Read [standalone.md](standalone.md) only
- Flow fits → Read [flow.md](flow.md) only
- Missing `standalone.md` or `flow.md` → matching missing-variant message; do not invent process
- If `variants.md` itself cannot be Read → still pick from the bullets above; do not stop

---
name: code-review
description: >-
  Initial review is five-axis (Standards + Spec + Routes + BigPicture + Risk)
  plus adversarial Wave 2; post-fix review is targeted to named blockers and
  regressions. Named remediation first goes through /analyze for proposed fixes,
  then explicit promotion. Failure claims require a reachable trigger and
  concrete evidence. A+ exam posture without scope drift. Dual skill:
  agent picks standalone vs flow via variants.md. Use for branch review or
  after validate in a goal. User must invoke (not auto).
disable-model-invocation: true
---

# Code Review

**Ask style:** [../asking.md](../asking.md) · **Variants:** [../variants.md](../variants.md)

## Variant

Choose **exactly one** per [variants.md](../variants.md) — never both:

- Standalone fits → Read [standalone.md](standalone.md) only
- Flow fits → Read [flow.md](flow.md) only
- Missing file → matching missing-variant message; do not invent process

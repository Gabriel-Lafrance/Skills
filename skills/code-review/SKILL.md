---
name: code-review
description: >-
  Initial review is two-axis (Standards + Spec) plus adversarial Wave 2;
  post-fix review is targeted to named blockers and regressions. Named
  remediation first goes through /analyze for proposed fixes, then explicit
  promotion. Failure claims require a reachable trigger and concrete evidence.
  A+ exam posture without scope drift. Dual skill: agent picks standalone vs
  flow via variants.md. Use for branch review or after validate in a goal.
  User must invoke (not auto).
disable-model-invocation: true
---

# Code Review

**Ask style:** [../pack-shared/asking.md](../pack-shared/asking.md) · **Variants:** [../pack-shared/variants.md](../pack-shared/variants.md)

## Variant

Choose **exactly one** per [variants.md](../pack-shared/variants.md) — never both:

- Standalone fits (one-off branch/PR review, no active goal wave) → Read [standalone.md](standalone.md) only
- Flow fits (inside `/goal` / orchestrator wave) → Read [flow.md](flow.md) only
- Missing `standalone.md` or `flow.md` → matching missing-variant message; do not invent process
- If `variants.md` itself cannot be Read → still pick from the bullets above; do not stop

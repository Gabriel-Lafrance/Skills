---
name: create-test
description: >-
  Write durable behavior-lock tests for complex hooks, domain logic, facades,
  and stateful classes. User-invoked standalone skill, used only after
  /code-review or /pr-review recommends a lock—not for coverage theater.
disable-model-invocation: true
---

# Create Test

**Standalone only.** Never invoke from a flow or automatically. Only
`/code-review` and `/pr-review` may recommend a lock; only the user starts this
skill.

**Variants:** [../pack-shared/variants.md](../pack-shared/variants.md) —
standalone-only; use the no-flow response when needed. **Ask style:**
[../pack-shared/asking.md](../pack-shared/asking.md).

**Read:** [doctrine.md](doctrine.md) · [reference.md](reference.md) when
drafting the approval brief, test comment, or handoff.

Lock observable behavior for a complex boundary. If the target is trivial, say
so and stop.

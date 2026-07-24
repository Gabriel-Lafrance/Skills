---
name: goal
description: >-
  Stateless Cursor goal loop: grill, plan, implement, validate, and review one
  verifiable outcome using in-chat execution context. Use when the user wants a
  feature or outcome built end to end.
disable-model-invocation: true
---

# Goal

**Variants:** [../pack-shared/variants.md](../pack-shared/variants.md) — standalone-only. If flow is requested, use the no-flow message.

**Execution context:** [../pack-shared/execution-context.md](../pack-shared/execution-context.md) · **Read:** [doctrine.md](doctrine.md) · [reference.md](reference.md) · **Ask style:** [../pack-shared/asking.md](../pack-shared/asking.md)

Orchestrator only. Use `/orchestrate` for Task workers.

## Lifecycle

1. Establish or refresh the required in-chat execution context.
2. Grill intent, record behavioral answers as Active Rules, and announce Locked closure before issuing plan or slice contracts.
3. Explore, split, create inline plan contracts, and implement frontier work.
4. Run `/validate`, then `/code-review`; analyze named blockers and explicitly promote selected fixes into bounded Fix mode or waive them.
5. Announce the completed outcome and offer ship questions only after all gates
   pass, unless a `/just-do-it` parent owns shipping.

`/goal` follows the stateless
[execution-context contract](../pack-shared/execution-context.md): plans are
inline unless the user explicitly requests a saved artifact and approves its
destination.

Recovery, progress, lookup, and safety rules live in the doctrine and reference.

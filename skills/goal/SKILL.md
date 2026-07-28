---
name: goal
description: >-
  Stateless Cursor goal loop: grill, plan, implement, gather acceptance
  evidence, and review one verifiable outcome using in-chat execution context.
  Use when the user wants a feature or outcome built end to end. Nested under
  /just-do-it as flow.
disable-model-invocation: true
---

# Goal

**Variants:** [../pack-shared/variants.md](../pack-shared/variants.md) — dual. Choose exactly one of [standalone.md](standalone.md) or [flow.md](flow.md).

**Execution context:** [../pack-shared/execution-context.md](../pack-shared/execution-context.md) · **Read:** [doctrine.md](doctrine.md) · [reference.md](reference.md) · **Ask style:** [../pack-shared/asking.md](../pack-shared/asking.md) · **Browser:** [../pack-shared/browser-evidence.md](../pack-shared/browser-evidence.md)

Orchestrator only. Use `/orchestrate` for Task workers. Always load flow
`/taste` during grill and before implement. Load flow `/architecture` unless
the work is trivial single-file with structure already settled.

## Lifecycle

1. Establish or refresh the required in-chat execution context.
2. Grill intent, record behavioral answers as Active Rules, and announce Locked closure before issuing plan or slice contracts.
3. Explore, split, create inline plan contracts, and implement frontier work.
4. Confirm Done when and Active Rules with path-walk / terminal / browser evidence, then run `/code-review`; analyze named blockers and explicitly promote selected fixes into bounded Fix mode or waive them.
5. Announce the completed outcome. Standalone may offer ship questions; flow returns completion evidence to the parent.

`/goal` follows the stateless
[execution-context contract](../pack-shared/execution-context.md): plans are
inline unless the user explicitly requests a saved artifact and approves its
destination.

Recovery, progress, lookup, and safety rules live in the doctrine and reference.

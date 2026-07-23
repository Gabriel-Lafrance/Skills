---
name: goal
description: >-
  Autonomous Cursor goal loop: grill, plan, implement, validate, and review one
  verifiable outcome in a scoped workspace. Resume through STATUS and archive on
  ACHIEVED. Use when the user wants a feature or outcome built end to end.
disable-model-invocation: true
---

# Goal

**Variants:** [../variants.md](../variants.md) — standalone-only. If flow is requested, use the no-flow message.

**Read:** [doctrine.md](doctrine.md) · [reference.md](reference.md) · [../workspace-roots.md](../workspace-roots.md) · **Ask style:** [../asking.md](../asking.md)

Orchestrator only. Use `/orchestrate` for Task workers and omit Task `model` unless the user asks for one.

## Lifecycle

1. Resolve the scoped goal root and create or resume the workspace.
2. Grill intent, record behavioral answers as Active Rules, and announce Locked closure before writing plans.
3. Explore, split, create plans, and implement frontier work.
4. Run `/validate`, then `/code-review`; analyze named blockers and explicitly promote selected fixes into bounded Fix mode or waive them.
5. Archive the goal and offer ship questions only after ACHIEVED.

Status, pause, clear, progress, lookup, and anti-pattern rules live in the doctrine and reference.

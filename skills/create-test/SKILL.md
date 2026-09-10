---
name: create-test
description: >-
  Write durable behavior-lock tests for complex hooks, domain logic, facades,
  and stateful classes. User-invoked skill, used only after
  /code-review or /pr-review recommends a lock—not for coverage theater.
disable-model-invocation: true
---

# Create Test

**Must read:** [../pack-shared/standards.md](../pack-shared/standards.md) — Read `/taste` and `/architecture` doctrines this turn so locks sit on the public surface, not internals. Do not skip.

This skill is a user start. Do not nest it under `/task` or start it
automatically. Only `/code-review` and `/pr-review` may recommend a lock; only
the user starts this skill. Review may recommend it; nothing auto-invokes it.

**Ask style:** [../pack-shared/asking.md](../pack-shared/asking.md).

**Read:** [doctrine.md](doctrine.md) · [reference.md](reference.md) when
drafting the approval brief, test comment, or handoff.

Lock observable behavior for a complex boundary. If the target is trivial, say
so and stop.

The parent owns the Why / What / How question. **Tester** is the go-to writer
of tests and must always be summoned for that labor per
[../pack-shared/subagents.md](../pack-shared/subagents.md). Feed **what** to
lock and need-to-know (approved brief, public entry, paths). Tester owns
**how**. Review the Completion. Never write tests on the main agent.

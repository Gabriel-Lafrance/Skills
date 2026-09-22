---
name: create-test
description: >-
  Write durable behavior-lock tests for complex hooks, domain logic, facades,
  and stateful classes. The user starts it, or /task continues it after the
  user accepts that task's lock briefs. Not for coverage theater.
disable-model-invocation: true
---

# Create Test

**Must read:** [../pack-shared/standards.md](../pack-shared/standards.md). Apply the **Taste** and **Architecture** sections of `AGENTS.md` this turn so locks sit on the public surface, not internals. Do not skip.

The user starts this skill. `/task` may continue it only after the user
accepts that task's [behavior-lock briefs](../task/reference.md#behavior-lock-suggestion).
That answer is the start for those briefs. Each task brief cites a grilled
rule. `/implement`, `/design`, and other build workers do not start this
skill. Silence, and a parent taking `recommended`, are not a start.

`/code-review` and `/pr-review` may still recommend a lock the task did not
offer. The user starts this skill for that recommendation. Nothing writes
tests on its own.

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

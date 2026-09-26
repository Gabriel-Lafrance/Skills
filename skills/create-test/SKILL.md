---
name: create-test
description: >-
  Write durable behavior-lock tests for complex hooks, domain logic, facades,
  and stateful classes. The user starts it, or /task continues it after the
  user accepts that task's lock briefs. Not for coverage theater.
disable-model-invocation: true
---

# Create Test

Lock observable behavior for a complex boundary. If the target is trivial, say
so and stop.

## Read when

- Every run, so locks sit on the public surface, not internals: [code-quality.md](../rules/code-quality.md) and [code-structure.md](../rules/code-structure.md) ([standards.md](../pack-shared/standards.md)), plus [doctrine.md](doctrine.md).
- Drafting the approval brief, test comment, or handoff: [reference.md](reference.md).
- Asking the Why / What / How question: [asking.md](../pack-shared/asking.md).
## Who starts it

The user starts this skill. `/task` may continue it only after the user
accepts that task's [behavior-lock briefs](../task/reference.md#behavior-lock-suggestion).
That answer is the start for those briefs. Each task brief cites a grilled
rule. `/task` build slices, `/design`, and other build steps do not start this
skill. Silence, and a parent taking `recommended`, are not a start.

`/review` may still recommend a lock the task did not offer. The user starts
this skill for that recommendation. Nothing writes tests on its own.

## Process

Ask the Why / What / How question first. Write tests only after each brief is
approved, through the public entry the brief names. Steps live in
[reference.md](reference.md#process).

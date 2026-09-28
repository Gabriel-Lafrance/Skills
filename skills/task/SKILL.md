---
name: task
description: Stateless end-to-end build loop for one verifiable outcome, with no tests-first phase. Use only when the user types /task or asks to build without tests. Any other build request goes to /task-with-tests.
category: Code
---

# Task

Orchestrate one verifiable outcome end to end. Plans stay inline in chat unless the user explicitly requests a saved artifact and approves its destination.

## Read when

- About to search the codebase, read a large file, or wade through long output? Open [smart-zone.md](../rules/smart-zone.md). Skip it and noise fills your context for the rest of the task.
- About to grill? Open [code-quality.md](../rules/code-quality.md), [code-structure.md](../rules/code-structure.md), [doctrine.md](doctrine.md), and the [execution context](../rules/planning.md#execution-context). Skip them and you recommend a shape the rules forbid.
- About to grill or plan a Feature? Open [strong-foundation.md](../rules/strong-foundation.md). Skip it and the first provider is hardcoded into every caller, so the next ticket is a rewrite.
- At a step that names a section? Open [reference.md](reference.md) (lifecycle, plan contract, behavior locks, ship Questions). Skip it and you improvise the lifecycle.
- About to ask the user anything? Open [Asking the user](../rules/writing-style.md#asking-the-user). Skip it and you send questions with no options and no recommendation.
- About to write a test? Open [no-unrequested-tests.md](../rules/no-unrequested-tests.md), then [testing.md](../rules/testing.md). Skip them and you write a test nobody accepted, or one that restates the code.
- About to commit, push, or open a PR from this chat? Open [shipping.md](../rules/shipping.md). Skip it and you push to `main`, open a PR nobody approved, or track `origin/main`.

## Process

1. Establish or refresh the in-chat execution context.
   If a parent already supplied ticket, lane, Done when, non-goals, rules
   that must stay true, fixed point, and slice bounds, accept that brief. Do
   not re-derive ticket or branch ownership the parent holds.
2. Run the [lifecycle](reference.md#lifecycle): grill (unless skip-grill
   applies) → plan → [behavior-lock suggestion](reference.md#behavior-lock-suggestion)
   → implement → `/verification` and `/review` in parallel → Fix mode as
   needed.
   - Write a test only for a lock the user accepted, following [testing.md](../rules/testing.md).
   - Apply code-quality.md and code-structure.md during grill and before
     every implement slice. Apply user-experience.md before every user-facing
     implement slice.
   - The behavior-lock suggestion waits for the user, who can refuse every test.
3. Announce completion.

Recovery, progress, lookup, and safety rules live in the doctrine and reference.

### If a parent already owns the ticket, branch, and PR

Do not ask ship Questions. Do not commit, push, or open a PR from this skill.
Return a completion summary plus evidence envelope to the parent.

### If this chat owns shipping

Offer ship Questions only after all gates pass
([reference.md](reference.md#ship-questions)). Do not commit or open a PR
unless the user answers yes. If they ask to open a PR, follow shipping.md. Do
not invent a parent.

## Anti-patterns

- Asking ship Questions when a parent owns shipping
- Pushing, committing for ship, or opening a PR when nested
- Suggesting a test before the grill is locked, or writing a test the user did not accept

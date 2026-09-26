---
name: task
description: >-
  Stateless end-to-end build loop: grill, plan, suggest behavior-lock tests
  the user can refuse, implement, gather acceptance evidence, and review one
  verifiable outcome using in-chat execution context. Use when the user wants
  a feature or outcome built end to end. When a parent owns shipping, return
  evidence to that parent.
disable-model-invocation: true
---

# Task

Orchestrate one verifiable outcome end to end. Plans stay inline in chat unless the user explicitly requests a saved artifact and approves its destination.

## Read when

- Throughout: stay in your smart zone (hard rule 9 in `AGENTS.md`).
- Before grilling: [code-quality.md](../rules/code-quality.md) and [code-structure.md](../rules/code-structure.md) ([standards.md](../pack-shared/standards.md)), plus [doctrine.md](doctrine.md) and the [execution-context contract](../pack-shared/execution-context.md).
- At the step that names a section: [reference.md](reference.md) (lifecycle, plan contract, behavior locks, ship Questions).
- Before asking the user anything: [asking.md](../pack-shared/asking.md).
- Only when this chat will open a PR: [pr-ship.md](../pack-shared/pr-ship.md).

## Process

1. Establish or refresh the in-chat execution context.
   If a parent already supplied ticket, lane, Done when, non-goals, rules
   that must stay true, fixed point, and slice bounds, accept that brief. Do
   not re-derive ticket or branch ownership the parent holds.
2. Run the [lifecycle](reference.md#lifecycle): grill (unless skip-grill
   applies) → plan → [behavior-lock suggestion](reference.md#behavior-lock-suggestion)
   → implement → acceptance evidence → `/review` → Fix mode as needed.
   - Write a test only for a lock the user accepted, following `/create-test`.
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
unless the user answers yes. If they ask to open a PR, follow pr-ship.md. Do
not invent a parent.

## Anti-patterns

- Asking ship Questions when a parent owns shipping
- Pushing, committing for ship, or opening a PR when nested
- Suggesting a test before the grill is locked, or writing a test the user did not accept

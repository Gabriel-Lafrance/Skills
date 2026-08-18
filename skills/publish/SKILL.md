---
name: publish
description: >-
  Publish completed work on a typed branch and optionally open a GitHub PR.
  Uses an approved draft with concrete QA steps, a high-level Mermaid Change
  diagram (Before/After for rework), Browser screenshots in Demo when visual,
  and a Cursor review canvas. Any agent that opens a PR follows the same ship
  contract, not only this skill. Use after work is complete when the user
  wants to ship a branch or PR. Never use inside /goal.
disable-model-invocation: true
---

# Publish

**Must read:** [../pack-shared/standards.md](../pack-shared/standards.md) — Read `/taste` and `/architecture` doctrines this turn so the Change diagram and QA match the shipped structure. Do not skip. Every PR this pack opens also follows [../pack-shared/pr-ship.md](../pack-shared/pr-ship.md) (screenshots, review canvas, create tool) — including `/just-do-it` and cloud agents, not only this skill.

**Variants:** [../pack-shared/variants.md](../pack-shared/variants.md) — standalone-only. If flow is requested, use the no-flow message.

**Read:** [doctrine.md](doctrine.md) · [reference.md](reference.md) · [../pack-shared/pr-ship.md](../pack-shared/pr-ship.md) · **Ask style:** [../pack-shared/asking.md](../pack-shared/asking.md)

Publish only. Never invoke from `/goal`, invent a `publish-flow`, write tracker issues, or implement product work.

## Process

1. Inspect git and stop on unsafe states.
2. Lock change type and ticket.
3. Create or reuse the typed branch, then push unless local-only.
4. Ask whether to draft and publish a PR.
5. Show the full title and body (including Mermaid Change diagram, Demo when
   visual, and canvas link).
6. Create the PR only after approval, using the create tool in
   [pr-ship.md](../pack-shared/pr-ship.md). Produce the review canvas for
   non-trivial PRs.

Templates, branch rules, question batches, and failure handling live in the reference and doctrine.

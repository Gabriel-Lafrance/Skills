---
name: publish
description: >-
  Publish completed work on a typed branch and optionally open a GitHub PR.
  Uses an approved draft with concrete QA steps. Use after work is complete when
  the user wants to ship a branch or PR. After standalone /goal completes, accept
  its hand-off. Never nest as a flow step inside /goal.
disable-model-invocation: true
---

# Publish

**Variants:** [../pack-shared/variants.md](../pack-shared/variants.md) — standalone-only. If flow is requested, use the no-flow message.

**Read:** [doctrine.md](doctrine.md) · [reference.md](reference.md) · **Ask style:** [../pack-shared/asking.md](../pack-shared/asking.md)

Publish only. Never nest as a flow step under `/goal`, invent a `publish-flow`,
write tracker issues, or implement product work. Accept a post-completion
hand-off from standalone `/goal`.

## Process

1. Inspect git and stop on unsafe states.
2. Lock change type and ticket.
3. Create or reuse the typed branch, then push unless local-only.
4. Ask whether to draft and publish a PR.
5. Show the full title and body.
6. Create the PR only after approval.

Templates, branch rules, question batches, and failure handling live in the reference and doctrine.

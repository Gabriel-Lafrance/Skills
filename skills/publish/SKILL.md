---
name: publish
description: >-
  Publish completed work on a typed branch and optionally open a GitHub PR.
  Uses an approved draft with concrete QA steps and a high-level Mermaid
  Change diagram (Before/After for rework). Any agent that opens a PR
  follows the same ship contract, not only this skill. Use after work is
  complete when the user wants to ship a branch or PR. Never use inside /task.
disable-model-invocation: true
---

# Publish

**Must read:** [../pack-shared/standards.md](../pack-shared/standards.md). Apply the **Taste** and **Architecture** sections of `AGENTS.md` this turn so the Change diagram and QA match the shipped structure. Do not skip. Every PR this pack opens also follows [../pack-shared/pr-ship.md](../pack-shared/pr-ship.md) (create tool), including `/just-do-it` and any agent that ships a branch, not only this skill.

**Read:** [doctrine.md](doctrine.md) · [reference.md](reference.md) · [../pack-shared/pr-ship.md](../pack-shared/pr-ship.md) · **Ask style:** [../pack-shared/asking.md](../pack-shared/asking.md)

This skill is a user start. Do not nest it under `/task`. Publish only. Never invent a `publish-flow` name, write tracker issues, or implement product work.

## Process

1. Inspect git and stop on unsafe states. Before a push that opens a PR, or
   a commit or push on a branch that already has an open PR, run the CI
   mirror in [pr-ship.md](../pack-shared/pr-ship.md) in this environment.
   Do not run it on a commit you are not pushing.
2. Lock change type and ticket.
3. Create or reuse the typed branch as a standalone ref (the steps in [reference.md](reference.md): detach, then `switch -c`, or `--no-track`). It must not track `dev`, `main`, or `master`. Then push that ref unless local-only.
4. Ask whether to draft and publish a PR.
5. Show the full title and body (including the Mermaid Change diagram).
6. Create the PR only after approval, using the create tool in
   [pr-ship.md](../pack-shared/pr-ship.md).

Templates, branch rules, question batches, and failure handling live in the reference and doctrine.

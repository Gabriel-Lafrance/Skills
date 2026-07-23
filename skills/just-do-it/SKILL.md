---
name: just-do-it
description: >-
  Autonomously turn a Linear ticket into a typed branch, reviewed implementation,
  and visible GitHub PR. Uses nested workspaces, scoped fix goals, and a human
  review handoff. Use when the user wants ticket-to-PR execution.
disable-model-invocation: true
---

# Just Do It

**Variants:** [../pack-shared/variants.md](../pack-shared/variants.md) — standalone-only. If flow is requested, use the no-flow message.

**Read:** [doctrine.md](doctrine.md) · [reference.md](reference.md) · [../pack-shared/workspace-roots.md](../pack-shared/workspace-roots.md) · [../publish/doctrine.md](../publish/doctrine.md) · [../publish/reference.md](../publish/reference.md) · **Ask style:** [../pack-shared/asking.md](../pack-shared/asking.md)

Standalone mega-orchestrator only. It owns a nested workspace, takes recommended soft decisions, auto-fixes only named Fix-now blockers, records optional review improvements as follow-ups, and leaves `/pr-review` to a human.

## Lifecycle

1. Resolve the Linear ticket and create the nested run workspace.
2. Create a typed branch after git hard stops pass.
3. Run `/analyze`, then promote into a root-scoped `/goal`.
4. Run flow `/code-review`, analyze CR1 Fix-now proposals, promote them into the build-goal Fix mode, and run targeted re-review loops.
5. Run standalone `/code-review` against the final branch; analyze CR2 proposals and promote selected rows into bounded fix goals.
6. Commit, preflight, record and print the full PR draft, then create the PR.

Status, hard stops, root propagation, review caps, shipping, resume, and anti-pattern rules live in the doctrine and reference.

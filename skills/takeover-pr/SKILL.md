---
name: takeover-pr
description: Use when the user explicitly asks to assess, revive, or take over an old PR. Check semantic relevance and current invariants before recommending continue, rework, or closure; implement and publish only within authorized scope.
category: Code
---

# Take over a PR

Every run applies [code quality](../rules/code-quality.md),
[code structure](../rules/code-structure.md), and
[Plain language](../rules/writing-style.md#plain-language).
Before a decision, use [Asking the user](../rules/writing-style.md#asking-the-user).
Carry the updated intent in the existing
[execution context](../rules/planning.md#execution-context).

1. Read [intent-aware takeover](../rules/pr-lifecycle.md#intent-aware-takeover),
   [execution preflight](../rules/execution.md#ready-ticket-preflight).
2. Inspect the source PR/history and current target under the shared takeover
   contract. Preserve authorship, unrelated work and settled user decisions.
3. Present the evidenced continue/rework/closure recommendation and authority
   boundary. Stop if the request was assessment only or a material decision
   blocks continuation; follow [asking rules](../rules/writing-style.md#asking-the-user).
4. For authorized work, hand the updated intent and pinned scope to the selected
   build skill via the Skills table in `AGENTS.md`. Reuse its readiness,
   checks, review and shipping contracts rather than copying their orchestration.
5. Report the resulting diff, source credit, checks and remaining blockers.
   Watch only if requested, with the existing parent as sole owner under
   [PR lifecycle](../rules/pr-lifecycle.md#authority-and-ownership).

A simple request to sync main follows
[Git sync only](../rules/execution.md#git-sync-only), without this assessment.

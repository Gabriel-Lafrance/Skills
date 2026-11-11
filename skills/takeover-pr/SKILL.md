---
name: takeover-pr
description: Use only when the user explicitly asks to assess, revive, or take over an old PR. Checks it against current code before recommending continue, rework, or closure.
category: Code
---

# Take over a PR

Carry the updated intent in the
[execution context](../rules/planning.md#execution-context).

1. Read [intent-aware takeover](../rules/pr-lifecycle.md#intent-aware-takeover)
   and [execution preflight](../rules/execution.md#ready-ticket-preflight).
2. Inspect the source PR/history and current target under the takeover
   contract. Preserve authorship, unrelated work and settled user decisions.
3. Present the evidenced continue/rework/closure recommendation and authority
   boundary. Stop if the request was assessment only or a material decision
   blocks continuation.
4. For authorized work, hand the updated intent and pinned scope to the build
   skill the `AGENTS.md` Skills table selects. Reuse its readiness, checks,
   review and shipping contracts; do not copy their orchestration.
5. Report the resulting diff, source credit, checks and remaining blockers.
   Watch only if requested, with the existing parent as sole owner under
   [PR lifecycle](../rules/pr-lifecycle.md#authority-and-ownership).

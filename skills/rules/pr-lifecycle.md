# PR lifecycle

Shared contracts for PR watching and old-PR assessment. Shipping stays in
[shipping.md](shipping.md); fixes and evidence stay in
[execution.md](execution.md#remediation). Apply
[code-quality.md](code-quality.md) and [code-structure.md](code-structure.md)
to any authorized changes.

## Authority and ownership

Watching or reporting grants no permission to edit, rebase, push, post comments,
resolve threads, close, or merge a PR. Reuse explicit authorization already in
the conversation; ask only for a missing action. Default completion leaves the
PR unmerged. A readiness report never grants merge permission.

One active parent/owner watches each repository and PR. Reviewers and fix
workers return evidence to that owner and never register competing watches.
On resume or handoff, reconcile the actual registration and owner before
creating another. Keep the PR identity, head, scope of authority, registration
identity/state, and last meaningful result in the existing chat context.

## Watch lifecycle

Inspect the current PR, all existing findings/discussion, and checks before
waiting. Address existing actionable work within authorized scope first. Without
fix authority, report the findings as a blocker; do not park a watch over work
already requiring a decision. Reuse [remediation](execution.md#remediation)
and [review modes](../review/contract.md#modes) rather than starting a new build
for every wake.

Discover the live permitted watch interface under
[harness-first discovery](tooling.md#harness-first-discovery). In T3, use its
native PR watch when available and permitted. Use only advertised identifiers,
fields, delivery and cleanup contracts. Follow returned next instructions;
do not add a second watcher or parallel polling loop. If no permitted watch
exists, report a bounded current snapshot and the missing capability. Use a
supported bounded fallback only when its tools and schedule are authorized.
Do not promise future monitoring from a finished turn.

A wake means new information. Read current state again, reconcile registration
status, and assess the latest remote head. Registrations can expire or end;
re-register only if this owner is still continuing the authorized watch. Do
not assume a watch survives settlement, interruption, handoff, or an error.
Repeated unchanged wakes or read failures need a bounded stop and an explicit
blocker, not an endless loop.

Before asking a question, reporting ready or blocked, handing off, or ending
the run, remove this run's watch through the supported cleanup operation and
verify the result. On interruption/resume reconcile leftover state first.
If removal fails or its outcome is uncertain, report the PR, registration,
attempted action, reason and known state; cleanup remains blocked/uncertain.
Never claim cleanup succeeded without evidence. A successor starts only after
ownership and any remaining registration are reconciled.

## Latest-head readiness

Pin and report the latest remote head and base. Inspect required checks and
statuses on that exact head, unresolved review findings/threads, review and
draft state, conflicts, branch-behind/update requirements, and applicable
acceptance/verification evidence. A conflict-free flag does not prove the
branch is current. Optional/advisory bots are evidence to judge, not authority
to override repository requirements or material findings.

Recheck head before the final readiness report. If it moved, invalidate affected
evidence under [handoffs and evidence](execution.md#handoffs-and-evidence), review
new surface, and reassess the new head. Unknown mergeability, pending/missing
required checks, missing permissions, unresolved material findings or stale
acceptance are pending/blocked, never ready. Report known current conditions,
remaining blockers, watch cleanup and that the PR remains unmerged. This
read-only report does not mark a draft ready for review or merge it.

## Intent-aware takeover

Use only when the user asks to take over, revive, or assess an old PR. Ordinary
branch synchronization stays [Git sync only](execution.md#git-sync-only).

Pin the original PR's base/head and current target revision; protect dirty and
unrelated work. Read the original problem, discussion, commits, prior findings
and acceptance evidence. Inspect current implementations and affected consumers,
including intervening architectural and security/data invariants. File overlap
and a clean rebase do not establish semantic relevance. Determine whether the
problem still exists, was solved elsewhere, became obsolete, or needs a
different implementation under current contracts.

Recommend **continue**, **rework**, or **closure** with concrete evidence,
remaining uncertainty, source PR/authors, intended destination branch/base,
and required authority. If only an assessment was requested, stop there. A
closure recommendation does not close anything. Takeover grants no automatic
force push, base change, merge, source-PR closure, scope expansion, or comment.

For authorized continuation, preserve original authorship and provenance when
carrying commits forward; put new fixes in separate commits and link/credit
the original PR in any authorized replacement PR. Verify identities before
adding human coauthor trailers; do not guess or rewrite attribution. Prefer a
clean branch/worktree when unrelated work or shared history needs protection,
using the live harness's supported isolation contract for delegated work.
Use the selected build skill's [ready-ticket preflight](execution.md#ready-ticket-preflight)
with the updated intent and existing test decisions, then scoped checks and
[shipping](shipping.md) only within existing authorization. Compare the carried
changes with the original (for example, range-diff when applicable), inspect
the final diff against the actual target base, and renew affected evidence.

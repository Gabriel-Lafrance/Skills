# Just Do It doctrine

Standalone parent orchestrator: **Linear ticket → typed branch → analyze →
bounded build → CR1 → CR2 → PR**. Human review owns `/pr-review`. Never run
this under `/goal` or invent a flow twin.

Use the shared [execution context](../pack-shared/execution-context.md), the
[asking contract](../pack-shared/asking.md), and [reference.md](reference.md).
No automatic run tree, registry, phase record, review snapshot, findings
ledger, ship record, archive, or nested root is allowed. Save only a
user-requested artifact at a user-approved location.

## Parent context

Before dispatching work and at every phase boundary, the parent keeps this
visible in chat:

- ticket, type, branch, base, outcome, Done when, lane, non-goals, and rules;
- phase and next action;
- CR1/CR2 loop counts, named Fix-now items, follow-ups, waived items, and
  their disposition;
- child completion evidence and handoffs;
- preflight evidence and the complete PR draft before creation.

Pass the applicable context to every child; never pass a path for it to
reconstruct.

## Autonomy and hard stops

Take `← recommended` on child soft Questions without waiting. Announce Locked
(correct if wrong) conclusions. Auto-remediate only a named **Fix now** item
that cites an invariant/spec, correctness, security, or regression defect.
Keep architecture, readability, relocation, cleanup, and nits as Follow-up;
do not promote or loop on them unless the user asks.

| Hard stop | Action |
| --- | --- |
| Missing or invalid Linear ticket | Stop; require `IN-1234` or URL |
| Linear MCP or `gh` unavailable when needed | State the blocker in context |
| Dirty tree before early branch | Ask commit, stash, or abort |
| Detached HEAD or no remote | Fix or stop |
| Merge conflict or rejected push | Stop; never force-push |
| Open blockers after a loop cap | Stop; do not ship |
| Type genuinely unknowable | One Questions batch for type only |

## Ticket and branch

- A ticket is required; never invent one.
- Lock type from Linear metadata where possible: Feature → `feature/`, Tweak →
  `tweak/`, Bug → `bug/`, Refactor → `refactor/`. Otherwise infer from the
  ticket and announce it Locked.
- After hard stops pass, create `{type}/{ticket}-{slug}` from the default base
  (`main`, else `master`); no colons and no push until shipping.
- Never push the default branch or force-push.

## Lifecycle and gates

1. **Resolve.** Fetch the ticket through read-only `/trackers` and open the
   parent context.
2. **Branch.** Apply the branch contract above.
3. **Analyze and build.** Run `/analyze` with an explicit parent instruction
   to choose its `promote + start` handoff, then run the bounded build `/goal`.
   Give child skills the ticket, lane, Done when, non-goals, rules, and current
   slice. The parent owns integration and shipping.
4. **CR1.** Run flow `/code-review` against the ticket and active build
   context. Add each result to the parent Fix backlog. For named Fix-now
   blockers, run scoped remediation analysis, show its complete memo, then
   promote the recommended bounded fix into the active build work and run
   `remediation` review. Follow-ups and nits never trigger a loop.
5. **CR2.** Run a fresh standalone `/code-review` against the final branch and
   default base; do not rubber-stamp CR1. Named Fix-now blockers may become a
   tightly bounded `fix-cr2-N` slice on the original ticket, then receive
   `remediation` review.
6. **Loop cap.** Each of CR1 and CR2 has at most three remediation loops. Stop
   sooner when Fix-now is empty. At the cap with an open blocker, mark the
   context blocked and do not ship.
7. **Ship.** Commit on the typed branch (never `--no-verify` unless explicitly
   requested), then run publish preflight: clean tree after commit, real
   branch, remote/default base, commits ahead, and authenticated `gh`. Build
   the full title and body from [publish reference](../publish/reference.md),
   print both in chat, then push with `git push -u origin HEAD` and create the
   PR. Record the URL in the parent context and hand review to a human.

## Fix boundaries

Every review repair stays on the original ticket and may touch only the ticket
lane or paths named by the finding. Preserve relevant Active Rules; add one
only when the finding exposes locked behavior. A fix must name the finding,
its risk/spec/invariant, and binary Done when. No new feature, unrelated
cleanup, product redesign, or “while we’re here” refactor is permitted.

## New-chat recovery

Rediscover ticket, PR, branch, diff, commits, and repository facts in the
shared execution-context authority order. Rebuild and show the compact parent
context before acting. Do not infer a prior user waiver, promotion, acceptance,
or loop disposition from Git alone; re-announce what is known and ask only for
the missing user-owned decision.

## Boundaries

- Never run `/pr-review`.
- Never write/edit tests or invoke `/create-test`; it may be recommended after
  review.
- Never create a PR without showing the complete draft in chat.

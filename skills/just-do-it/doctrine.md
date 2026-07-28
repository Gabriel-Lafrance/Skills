# Just Do It doctrine

Standalone parent orchestrator: **Linear ticket → typed branch → analyze →
bounded build → checkpoint → CR1 → CR2 → opened PR**. Human review owns
`/pr-review`. Never run this under `/goal` or invent a flow twin of itself.

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
- **Fixed point:** default base name, `baseSha`, `headSha` (after each
  checkpoint);
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
| Dirty tree at CR1/CR2 start | Checkpoint commit or stop — never review uncommitted work |
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
- Record **base SHA** at branch creation (`git rev-parse <base>`).
- Never push the default branch or force-push.

## Checkpoint and fixed point

Reviews must see a real committed diff. Before every CR1 or CR2 pass (and
before each remediation re-review):

1. If the working tree has staged, unstaged, or untracked changes in scope,
   create a checkpoint commit on the typed branch, e.g.
   `wip: just-do-it checkpoint before CR1` (or `before CR1-remediation-N` /
   `before CR2`).
2. Refuse to start review while dirty relative to `HEAD`.
3. Pin **Fixed point** as `<base>...<HEAD>` with recorded `baseSha` and
   `headSha` (`git rev-parse`). Pass both SHAs into every review brief — do
   not use a bare `main...HEAD` label while work is uncommitted.
4. After remediation edits, checkpoint again before the next review loop.

Final ship may add a descriptive commit (or commits). Amend or squash only if
the user explicitly asked; default is additional commit(s), then push + PR.

## Lifecycle and gates

1. **Resolve.** Fetch the ticket through read-only `/trackers` and open the
   parent context.
2. **Branch.** Apply the branch contract above; record `baseSha`.
3. **Analyze and build.** Run **flow** `/analyze` with an explicit parent
   instruction to choose its `promote + start` handoff, then run **flow**
   `/goal` for the bounded build. Give child skills the ticket, lane, Done
   when, non-goals, rules, and current slice. The parent owns integration and
   shipping; flow `/goal` returns completion evidence and skips ship Questions.
4. **Checkpoint → CR1.** Checkpoint if dirty; pin `baseSha`/`headSha`. Run
   flow `/code-review` against that fixed point and the active build context.
   Add each result to the parent Fix backlog. For named Fix-now blockers, run
   **flow** `/analyze` remediation, show its complete memo, promote the
   recommended bounded fix into flow `/goal` Fix mode, checkpoint, then run
   `remediation` review. Follow-ups and nits never trigger a loop.
5. **Checkpoint → CR2.** Checkpoint if dirty; pin fresh `headSha`. Run a fresh
   standalone `/code-review` against `baseSha...headSha`; do not rubber-stamp
   CR1. Named Fix-now blockers may become a tightly bounded `fix-cr2-N`
   slice on the original ticket (flow `/goal` Fix mode), then checkpoint and
   `remediation` review.
6. **Loop cap.** Each of CR1 and CR2 has at most three remediation loops. Stop
   sooner when Fix-now is empty. At the cap with an open blocker, mark the
   context blocked and do not ship.
7. **Ship.** Ensure a clean tree after any final ship commit(s) (never
   `--no-verify` unless explicitly requested), then run publish preflight:
   clean tree, real branch, remote/default base, commits ahead, and
   authenticated `gh`. Build the full title and body from
   [publish reference](../publish/reference.md), print both in chat, then push
   with `git push -u origin HEAD` and create the PR (**opened**, not merged).
   Record the URL in the parent context and hand review to a human.

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
- Never start CR1/CR2 on an uncommitted or dirty fixed point.

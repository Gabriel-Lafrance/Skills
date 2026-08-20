# Just Do It doctrine

## Job

Parent orchestrator: **Linear ticket → typed branch → analyze → bounded build → checkpoint → CR1 → CR2 → opened PR**. Human review owns `/pr-review`. Never run this under `/task`.

## Owns

Autonomy policy, hard stops, ticket/branch contract, checkpoint/fixed point, loop caps, fix boundaries, and shipping after a printed PR draft.

## Does not own

- `/pr-review` (human)
- Test writing (`/create-test` may be recommended after review)
- Taste and architecture bars: cite `taste:*` and `architecture:*`
- User-facing UI and `docs/design.md`: `/design`
- Numbered lifecycle: [`reference.md`](reference.md#lifecycle) · [`SKILL.md`](SKILL.md)

## Cite keys

none (uses `taste:*` and `architecture:*`)

## Bars

Use the shared [execution context](../pack-shared/execution-context.md), the [asking contract](../pack-shared/asking.md), [subagents.md](../pack-shared/subagents.md), and [reference.md](reference.md). No automatic run tree, registry, phase record, review snapshot, findings ledger, ship record, archive, or nested root is allowed. Save only a user-requested artifact at a user-approved location.

### Parent context

Before dispatching work and at every phase boundary, the parent keeps this visible in chat:

- ticket, type, branch, base, outcome, Done when, lane, non-goals, and rules;
- phase and next action;
- **Fixed point:** default base name, `baseSha`, `headSha` (after each checkpoint);
- CR1/CR2 loop counts, named Fix-now items, follow-ups, waived items, and their disposition;
- child completion evidence and handoffs;
- preflight evidence and the complete PR draft before creation.

Pass the applicable context to every child; never pass a path for it to reconstruct.

### Autonomy and hard stops

Take `recommended` on child soft Questions without waiting. Announce Locked-in conclusions only in announce-only messages (never above a Questions batch). Auto-remediate only a named **Fix now** item that cites an invariant/spec, correctness, security, or regression defect. Keep architecture, readability, relocation, cleanup, and nits as Follow-up; do not promote or loop on them unless the user asks.

| Hard stop | Action |
| --- | --- |
| Missing or invalid Linear ticket | Stop; require `IN-1234` or URL |
| Linear MCP or `gh` unavailable when needed | State the blocker in context |
| Dirty tree before early branch | Ask commit, stash, or abort |
| Detached HEAD or no remote | Fix or stop |
| Dirty tree at CR1/CR2 start | Checkpoint commit or stop. Never review uncommitted work |
| Merge conflict or rejected push | Stop; never force-push |
| Open blockers after a loop cap | Stop; do not ship |
| Type genuinely unknowable | One Questions batch for type only |
| Design mismatch "is this normal?" | Wait. Do not auto-pick. **No** means fix the UI; **Yes** means `/design` updates `docs/design.md` |

### Ticket and branch

- A ticket is required; never invent one.
- Lock type from Linear metadata where possible: Feature → `feature/`, Tweak → `tweak/`, Bug → `bug/`, Refactor → `refactor/`, Chore → `chore/`, Hotfix → `hotfix/`. Otherwise infer from the ticket and announce it Locked.
- After hard stops pass, create `{type}/{ticket}-{slug}` from the default base (`main`, else `master`); no colons and no push until shipping.
- Record **base SHA** at branch creation (`git rev-parse <base>`).
- Never push the default branch or force-push.

### Checkpoint and fixed point

Reviews must see a real committed diff. Before every CR1 or CR2 pass (and before each remediation re-review):

1. If the working tree has staged, unstaged, or untracked changes in scope, create a checkpoint commit on the typed branch, e.g. `wip: just-do-it checkpoint before CR1` (or `before CR1-remediation-N` / `before CR2`).
2. Refuse to start review while dirty relative to `HEAD`.
3. Pin **Fixed point** as `<base>...<HEAD>` with recorded `baseSha` and `headSha` (`git rev-parse`). Pass both SHAs into every review brief. Do not use a bare `main...HEAD` label while work is uncommitted.
4. After remediation edits, checkpoint again before the next review loop.

Final ship may add a descriptive commit (or commits). Amend or squash only if the user explicitly asked; default is additional commit(s), then push + PR.

Each of CR1 and CR2 has at most three remediation loops. Stop sooner when Fix-now is empty. At the cap with an open blocker, mark the context blocked and do not ship.

### Fix boundaries

Every review repair stays on the original ticket and may touch only the ticket lane or paths named by the finding. Preserve relevant Active Rules; add one only when the finding exposes locked behavior. A fix must name the finding, its risk/spec/invariant, and binary Done when. No new feature, unrelated cleanup, product redesign, or “while we’re here” refactor is permitted.

## Output

Parent context template and review disposition: [reference.md](reference.md). Print the complete PR title and body in chat before create. Record the URL and canvas link in the parent context and hand review to a human.

## Apply

Run the [lifecycle](reference.md#lifecycle). Child skills must follow `/taste` and `/architecture` ([standards.md](../pack-shared/standards.md)). User-facing slices also follow `/design` and `docs/design.md`.

Rediscover ticket, PR, branch, diff, commits, and repository facts in the shared execution-context authority order. Rebuild and show the compact parent context before acting. Do not infer a prior user waiver, promotion, acceptance, or loop disposition from Git alone; re-announce what is known and ask only for the missing user-owned decision.

## Anti-patterns

- Running `/pr-review` from this skill
- Writing/editing tests or invoking `/create-test` (it may be recommended after review)
- Creating a PR without showing the complete draft in chat (including the Mermaid Change diagram required by publish) or without following [pr-ship.md](../pack-shared/pr-ship.md)
- Starting CR1/CR2 on an uncommitted or dirty fixed point
- Force-pushing or pushing the default branch
- Looping on Follow-ups or nits unless the user asks

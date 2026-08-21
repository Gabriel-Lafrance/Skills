# Just Do It reference

Load this with [doctrine.md](doctrine.md) when opening or updating the parent
[execution context](../pack-shared/execution-context.md). It is a chat
template, not a filesystem schema.

## Parent context template

```markdown
## Execution context — just-do-it
**Outcome:** <ticket outcome>
**Done when:** <binary delivery checks>
**Non-goals:** <explicit exclusions>
**Ticket:** IN-1234 · <URL>
**Type:** feature | tweak | bug | refactor | chore | hotfix
**Branch / base:** `bug/IN-1234-fix-checkout` / `main`
**Fixed point:** `main...HEAD` · baseSha=`abc1234` · headSha=`def5678`
**Lane:** <paths and symbols>
**Phase:** resolve | branch | analyze | build | checkpoint | cr1 | cr2 | ship | done | blocked
**Next:** <one action>
**CR1 loops:** 0/3
**CR2 loops:** 0/3

### Locked decisions
- <type, promotion, waiver, or user-owned decision>

### Active Rules
| ID | Rule | Enforcement | Verification |
| --- | --- | --- | --- |
| INV-1 | … | … | … |

### Fix backlog
- `CR1-1` — fix now — <path, finding, risk/spec> — pending
- `CR2-1` — follow-up — <why it does not block>

### Handoffs and evidence
- <child completion, review result, acceptance evidence, blocker, or manual step>

### PR draft
**Preflight:** <clean tree · branch · remote/base · commits ahead · gh auth>
**Title:** [IN-1234] …
**Body:**
<complete PR body — includes Mermaid Change diagram, Demo when visual, canvas link>
**URL:** pending | https://github.com/…/pull/N
**Canvas:** pending | <share URL or local canvas link>
**Human next:** review on GitHub or `/pr-review`
```

**Fixed point rule:** always record `baseSha` and `headSha` after each
checkpoint. Review briefs use those SHAs. Do not claim `main...HEAD` while the
working tree is dirty or uncommitted relative to `headSha`.

Use only fields relevant to the current phase. Keep the complete PR title and
body visible in chat before creating the PR; autonomy removes an approval wait,
not draft visibility. Create with the tool choice in
[pr-ship.md](../pack-shared/pr-ship.md), not `gh pr create` when Cursor’s
pull-request tool is available.

## Review disposition

For every CR1 or CR2 pass, add a concise context entry with the review scope,
`baseSha`/`headSha`, evidence, and one disposition:

- **fix now** — named invariant/spec/correctness/security/regression blocker;
- **follow-up** — useful but not required now; never auto-loop;
- **waived** — explicit user decision with reason;
- **clear** — no named blockers remain;
- **blocked at cap** — an open blocker remains after the third loop.

Each bounded review fix preserves the original ticket, lane, and Active Rules.
Name the finding, cited risk/spec, smallest behavior-preserving change, and
binary Done when in the current slice.

## Lifecycle

Numbered how-to. Bars stay in [doctrine.md](doctrine.md). Also summarized in [SKILL.md](SKILL.md).

1. **Resolve.** Fetch the ticket through read-only `/trackers` and open the parent context.
2. **Branch.** Apply the doctrine branch contract; record `baseSha`.
3. **Analyze and build.** Run `/analyze` with an explicit parent instruction to choose its `promote + start` handoff, then run `/task` for the bounded build. Child skills must follow `/taste` and `/architecture` ([standards.md](../pack-shared/standards.md)). Child skills pick Task specialists per [subagents.md](../pack-shared/subagents.md) — the catalog, not a fixed spawn order. The parent does not grep, does not write tests, dispatches and reviews Completions, and does not solo that labor or redo a worker's how. Give child skills the ticket, lane, Done when, non-goals, rules, and current slice. The parent owns integration and shipping; `/task` returns completion evidence and skips ship Questions.
4. **Checkpoint → CR1.** Checkpoint if dirty; pin `baseSha`/`headSha`. Run `/code-review` against that fixed point and the active build context. Add each result to the parent Fix backlog. For named Fix-now blockers, run `/analyze` remediation, show its complete memo, promote the recommended bounded fix into `/task` Fix mode, checkpoint, then run `remediation` review. Follow-ups and nits never trigger a loop.
5. **Checkpoint → CR2.** Checkpoint if dirty; pin fresh `headSha`. Run a fresh `/code-review` against `baseSha...headSha`; do not rubber-stamp CR1. Named Fix-now blockers may become a tightly bounded `fix-cr2-N` slice on the original ticket (`/task` Fix mode), then checkpoint and `remediation` review.
6. **Loop cap.** Each of CR1 and CR2 has at most three remediation loops. Stop sooner when Fix-now is empty. At the cap with an open blocker, mark the context blocked and do not ship.
7. **Ship.** Ensure a clean tree after any final ship commit(s) (never `--no-verify` unless explicitly requested), then run publish preflight: clean tree, real branch, remote/default base, commits ahead, and authenticated `gh` or Cursor’s pull-request tool. Build the full title and body from [publish reference](../publish/reference.md) (including the Mermaid **Change diagram**: one for new work, Before/After for rework). Follow [pr-ship.md](../pack-shared/pr-ship.md) for Demo screenshots, the Cursor review canvas, and which tool writes the PR. Print title and body in chat, then push with `git push -u origin HEAD` and create the PR (**opened**, not merged). Record the URL and canvas link in the parent context and hand review to a human.

## New-chat recovery

Use the authority order in the shared execution context to rediscover the
ticket, branch, diff, commits, PR, and repository rules. Then post a rebuilt
parent context and distinguish facts from unresolved user decisions. Re-ask
only a missing waiver, promotion, acceptance, or disposition; do not assume
one from code or Git history.

## Optional persistence

If the user asks to save a review audit, plan, or run summary, honor the
user-approved destination and write only that requested artifact. It is not
required for continuation and must not become hidden runtime state.

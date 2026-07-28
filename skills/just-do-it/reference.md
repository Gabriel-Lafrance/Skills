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
**Type:** feature | tweak | bug | refactor
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
<complete PR body>
**URL:** pending | https://github.com/…/pull/N
**Human next:** review on GitHub or `/pr-review`
```

**Fixed point rule:** always record `baseSha` and `headSha` after each
checkpoint. Review briefs use those SHAs. Do not claim `main...HEAD` while the
working tree is dirty or uncommitted relative to `headSha`.

Use only fields relevant to the current phase. Keep the complete PR title and
body visible in chat before `gh pr create`; autonomy removes an approval wait,
not draft visibility.

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

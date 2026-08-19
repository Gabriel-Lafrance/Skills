# Goal reference (in-chat templates)

Load when establishing or recovering a goal, issuing a plan or slice contract, posting progress, or summarizing completion. Rules stay in [doctrine.md](doctrine.md).

## Stateless default

The shared [execution context](../pack-shared/execution-context.md) is the only
automatic state. Persist only a user-requested artifact at an approved
destination.

Plans, slices, grill outcomes, progress, and review findings stay in chat. If the user asks to save an analysis, plan, or summary and supplies or approves a destination, write only that artifact. It does not become hidden state or a requirement for recovery.

## Required execution context

Use the shared template, keeping only fields that matter to current work:

```markdown
## Execution context
**Outcome:** …
**Done when:** …
**Non-goals:** …
**Ticket / PR:** <reference | none>
**Fixed point:** <base...HEAD | none>
**Lane:** <allowed paths and symbols>
**Phase:** grill | plan | implement | acceptance | review | fix | done
**Next:** …

### Locked decisions
- <user decision, waiver, or promotion>

### Rules that must stay true
| ID | Rule | How we enforce it | How we check it |
| --- | --- | --- | --- |
| Rule 1 | … | … | … |

### Current slices
- <scope, acceptance criteria, ownership, dependencies, and status>

### Fix backlog
- `finding-id` — fix now | follow-up | waived
```

Do not infer a user decision, waiver, invariant, or promotion from repository facts. Re-announce settled decisions when they matter to a later phase.

## Inline plan contract

`/goal` produces this in chat for one slice (after Locked grill closing). It is not a file path or an instruction to write one.

```markdown
# Plan: <title>
**Slice:** <ordered ID>
**Status:** proposed | ready | implementing | done
**Blocked by:** <none | slice IDs>

## Outcome
<one verifiable slice result>

## Scope and lane
<allowed paths/symbols; explicit exclusions>

## Approach
<concrete implementation shape; no unresolved Option A/B>

## Taste
- **KISS / principles:** held | name the violation to fix in this slice
- **Sibling cited:** <good path | greenfield | correcting debt>

## Architecture
- **Service / public API:** <owns or calls>
- **Primitives:** <reuse | new inside which module | none>
- **Folder map:** <paths this slice may add>
- **Scalability:** <stored-on-write | none for this slice>

## Rules that must stay true
| ID | Role | How we enforce it | How we check it |
| --- | --- | --- | --- |
| Rule 1 | implement | … | … |

## Coordination
- **Owner:** …
- **Dependencies:** …
- **Handoffs / seams:** …
- **Must not touch:** …

## Acceptance criteria
- [ ] …

## Out of scope
- …
```

Assign relevant rules that must stay true to each contract. Keep the frontier and dependencies under **Current slices** in the execution context.

## New-chat recovery

Do not search for a goal directory, status file, archive, or resume tree. Follow the [authority order](../pack-shared/execution-context.md#authority):

1. Read the current request and decisions settled in this chat.
2. Re-derive named ticket/PR facts and comments.
3. Re-derive Git branch, diff, commits, and repository facts.
4. Read repository rules and committed project documentation.
5. Use a user-requested artifact only when its path was supplied.

State the recovered outcome, lane, fixed point, known rules, and phase in chat. Ask only for missing user-owned decisions; do not re-grill a decision carried by the request, ticket/PR, approved artifact, or repository rules merely because the chat is new.

## Progress and pause

After a phase change or Task wave, post one concise chat line:

```markdown
**Progress:** grill ✓ · slices 1/3 · implementing `02` · next: acceptance
```

For a pause, state the current phase, completed slices, blocker, and next action in chat. A later chat re-derives repository facts and asks only for decisions it cannot recover.

## Completion summary

After acceptance evidence is recorded and `/code-review` has run, report the outcome without archiving anything:

```markdown
# ✅ Goal complete: <short title>

## What changed
- …

## Evidence
- Acceptance: <Done when / rules that must stay true / seams — path walk, terminal, browser>
- `/code-review`: …

## Decisions and rules
- Rule 1: … verified by …

## Fix backlog
- <none | waived finding and user decision>

## Manual next steps
- <none | user action>
```

If review selected a Fix-now item, completion waits for remediation analysis,
explicit promotion, bounded Fix mode, re-checked acceptance evidence, and
`remediation` review—or a named user waiver.

## Ship questions

After the completion summary, ask one batch only when this chat owns
shipping. Defaults remain no unless already requested:

```markdown
## Questions
Reply like: 1b 2b

1. Commit these changes now?
   - a) yes — create a commit
   - b) no — leave uncommitted ← recommended
2. Open a PR?
   - a) yes — push and create a PR using `/publish` body rules (typed title,
     What changed, Mermaid Change diagram, How to QA) and
     [pr-ship.md](../pack-shared/pr-ship.md) (Demo screenshots, review canvas,
     Cursor pull-request tool when available)
   - b) no ← recommended
```

Wait for the answer before committing or opening a PR. If opening a PR, draft
the body from [publish reference](../publish/reference.md) (including Mermaid
**Change diagram**: one for new work, Before/After for rework), follow
[pr-ship.md](../pack-shared/pr-ship.md) for Demo, canvas, and create tool,
show the draft in chat, then create. When `/goal` runs under a parent
(`/just-do-it` or similar), return the completion evidence to the parent
instead; it owns the branch, preflight, draft visibility, and PR creation.

## Lifecycle

Numbered process for `/goal`. Rules stay in [doctrine.md](doctrine.md). Nested vs one-off shipping lives in [SKILL.md](SKILL.md).

### Phase 0: establish context and grill

1. Re-derive the ticket/PR, Git fixed point, repository facts, and applicable project rules as needed; state them in the in-chat execution context.
2. State the outcome, Done when, non-goals, lane, phase, and next action. Carry forward only user decisions already settled in this chat or an explicitly supplied artifact.
3. Unless the skip rule applies, run `/grill-me` fully. It pulls in `/taste` and `/architecture` on every run ([standards.md](../pack-shared/standards.md)).
4. Record Locked decisions and Active Rules in chat. Every locked behavioral answer has an `INV-*` row with authoritative enforcement and verification.
5. Announce the non-goals, intended slice split, and shared-understanding summary. Ask only real open questions in the same batch.

On a Locked correction or unanswered real question, revise or wait. Never infer a user decision, waiver, invariant, or promotion from code alone.

### Phase 1: plan and build

**Explore and shape.** Dispatch exploration through Task workers per [subagents.md](../pack-shared/subagents.md): non-trivial research **must** use a Task; ≥2 independent lanes **must** run in parallel. Confirm `/taste` and `/architecture` decisions against the grill (both doctrines must already be loaded this turn), then carry the relevant facts into the in-chat plan contracts.

**Split and plan.** Prefer small, ordered slices. `/split-task` announces the inline split; the parent then issues an [inline plan contract](#inline-plan-contract) for each slice before `/implement`. If the split changes, re-announce the new Locked split before implementation. Do not write an INDEX, plan path, or other runtime file.

**Implement wave.** Dispatch ready frontier slices as Task workers with a Worker Brief from [subagents.md](../pack-shared/subagents.md). Each prompt includes the applicable outcome, Done when, non-goals, Active Rules, lane, current slice, dependencies, and prior decisions. Anti-pattern: the parent solos non-trivial implement work. After integration, update **Current slices** in chat; if ready slices remain, dispatch the next frontier. Only when every slice is integrated, blocked, or explicitly waived does the parent enter acceptance evidence. The parent owns integration and the acceptance/review gates.

**Acceptance evidence and review.** After all implementation workers finish:

1. Confirm **Done when**, Active Rules, and slice acceptance criteria, including cross-slice seams, with path walks, terminal output, and (for UI criteria) the [browser evidence protocol](../pack-shared/browser-evidence.md). Record pass / fail / blocked per criterion in chat. Do not call an unperformed check a pass.
2. Always run **`/code-review`** next.
3. Put each review finding in the in-chat **Fix backlog** as `fix now`, `follow-up`, or `waived`.
4. For selected `fix now` findings, run `/analyze` in review-remediation mode, present the proposed correction, and enter Fix mode only after explicit user promotion. A `/just-do-it` parent may take the recommended promotion only after the complete remediation analysis is shown.
5. If the user declines a fix, completion remains blocked until every Fix-now finding is fixed or waived by name.

### Fix mode (review remediation only)

Fix mode is one bounded slice of the current goal, not fresh product discovery:

1. Carry only explicitly promoted findings into the current slice. Each cites its review finding, violated Active Rule, acceptance criterion, correctness/security issue, or regression.
2. Grill only the enforcement, footprint, and observable behavior needed to clear those findings. Preserve existing Active Rules; add one only when the finding exposes an unrecorded behavioral rule.
3. Prefer the smallest authoritative correction. Do not add queues, retries, wrappers, or new services unless the named finding proves a guard is insufficient.
4. No new feature scope, optional cleanup, or architecture move unless the named finding requires it.
5. Re-check the named findings and Active Rules with acceptance evidence, then run `/code-review` in `remediation` mode over the backlog, touched paths, direct regressions, correctness, and security.

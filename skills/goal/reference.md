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

### Active Rules
| ID | Rule | Enforcement | Verification |
| --- | --- | --- | --- |
| INV-1 | … | … | … |

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

## Invariants
| ID | Role | Required enforcement | Verification |
| --- | --- | --- | --- |
| INV-1 | implement | … | … |

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

Assign relevant Active Rules to each contract. Keep the frontier and dependencies under **Current slices** in the execution context.

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
- Acceptance: <Done when / Active Rules / seams — path walk, terminal, browser>
- `/code-review`: …

## Decisions and rules
- `INV-1`: … verified by …

## Fix backlog
- <none | waived finding and user decision>

## Manual next steps
- <none | user action>
```

If review selected a Fix-now item, completion waits for remediation analysis,
explicit promotion, bounded Fix mode, re-checked acceptance evidence, and
`remediation` review—or a named user waiver.

## Ship questions

After the completion summary, ask one batch only when standalone `/goal` owns
shipping. Defaults remain no unless already requested:

```markdown
## Questions
Reply like: 1b 2b

1. Commit these changes now?
   - a) yes — create a commit
   - b) no — leave uncommitted ← recommended
2. Open a PR?
   - a) yes — push and create a PR using `/publish` body rules (typed title,
     What changed, Mermaid Change diagram, How to QA)
   - b) no ← recommended
```

Wait for the answer before committing or opening a PR. If opening a PR, draft
the body from [publish reference](../publish/reference.md) (including Mermaid
**Change diagram**: one for new work, Before/After for rework), show it in chat,
then create. Under flow `/goal`
(parent `/just-do-it` or similar), return the completion evidence to the parent
instead; it owns the branch, preflight, draft visibility, and PR creation.

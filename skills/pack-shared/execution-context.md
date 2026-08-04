# Execution context

Pack skills are stateless by default. Do not create `.agents/temp/`, run
registries, status files, plans, grill logs, analysis memos, or review snapshots
unless the user explicitly asks to save an artifact and approves its destination.

## Authority

Resolve context in this order:

1. The current user request and settled decisions in this chat
2. The named ticket, PR, and its comments
3. Git branch, diff, commits, and repository code
4. Repository rules and committed project documentation
5. A user-requested artifact at the path the user supplied

Repository facts are rediscovered when needed. Do not infer a user decision,
waiver, invariant, or promotion from code alone.

## Parent context

Before dispatching work or crossing a lifecycle phase, the parent keeps the
relevant context visible in chat:

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
| Slice | Status | Scope / acceptance | Dependencies |
| --- | --- | --- | --- |
| 01 | ready | … | … |

### Fix backlog
- `finding-id` — fix now | follow-up | waived
```

Include only fields that matter to the current work. A new chat derives what it
can from the authority order, then re-announces or asks only about missing
user-owned decisions.

## Worker handoff

For when to spawn Tasks, Worker Brief shape, and after-wave integration, Read
[subagents.md](subagents.md).

The parent is the context compiler. Every Task prompt includes the applicable
outcome, Done when, non-goals, Active Rules, lane, current slice, dependencies,
and prior decisions. Do not make a worker reconstruct intent from hidden files
or a plan path.

Omit Task `model` unless the user explicitly requested one. The parent owns
integration, acceptance evidence, and `/code-review`; implementation workers do
not run those gates.

Every worker ends with:

```markdown
## Completion
**Status:** done | blocked
**Scope:** …
**Evidence:** …
**Findings:** none | <finding IDs and summaries>
**Handoff:** <changed interface, decision, or blocker>
```

Skill-specific artifacts may follow this envelope when they add useful detail.

## Optional persistence

When the user asks to save an analysis, plan, glossary, ADR, review audit, or
run summary, ask for or honor a user-approved destination. Write only that
requested artifact. It becomes an input under the authority order above; it is
not a hidden runtime cache.

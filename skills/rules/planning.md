# Planning

**Before planning** (any turn that will produce a plan for non-trivial work, including a harness plan tool):

1. **Read** the [Plain language](writing-style.md#plain-language) and [Asking the user](writing-style.md#asking-the-user) sections of writing-style.md
2. **Read** `grill-me/doctrine.md`
3. Apply [code-quality.md](code-quality.md) and [code-structure.md](code-structure.md)

## Plans: grill first

Whenever a non-trivial plan is about to be written, whether or not the harness calls that a plan mode:

1. **Do not** emit the final plan until material decisions are settled. If the harness has a plan tool, do not call it yet.
2. **Grill first.** Look up repository facts, then send **one batched Questions-only** message using the [asking rules](writing-style.md#asking-the-user) (`Reply like: 1a 2b`, lettered options, mark `recommended`, wait for the reply). Do **not** include a Locked-in section in that message.
3. Sweep open topics before planning: outcome, out of scope, users/edges, plan split, file lane, code quality and code structure choices, and any product or policy forks that would change the plan. Prefer recommending behavior-preserving moves and deep modules over leaving debt.
4. After the user answers (or when nothing remains to ask), announce agent-owned conclusions in a **separate** **Locked in (tell me if this is wrong)** message. Never mix Locked and Questions.
5. After Locked closure, **then** produce the plan. Use the harness plan tool when it has one. Otherwise write the plan in chat. New unknowns later mean a **new** Questions-only batch.

Skip the grill only for trivial asks (typo, pure rename the user already specified, or the user explicitly said to skip grilling / plan immediately).

Every non-trivial plan **must** include a high-level Mermaid **Change diagram** with **both** `### Before` and `### After`. Prefer modules, actors, and request/data flow. Keep the same node ids across Before/After when possible. A plan without Before/After is incomplete. PR bodies and `/analyze` memos use the [PR change diagram](shipping-templates.md#change-diagram) rule instead (one diagram for new work, Before/After for rework).

## Execution context

Pack skills are stateless by default. Do not create `.agents/temp/`, run registries, status files, plans, grill logs, analysis memos, or review snapshots unless the user explicitly asks to save an artifact and approves its destination.

### Authority

Resolve context in this order:

1. The current user request and settled decisions in this chat
2. The named ticket, PR, and its comments
3. Git branch, diff, commits, and repository code
4. Repository rules and committed project documentation
5. A user-requested artifact at the path the user supplied

Repository facts are rediscovered when needed. Do not infer a user decision, waiver, invariant, or promotion from code alone.

### Context in chat

Before starting a slice or crossing a lifecycle phase, the agent keeps the relevant context visible in chat:

```markdown
## Execution context
**Outcome:** …
**Done when:** …
**Non-goals:** …
**Ticket / PR:** <reference | none>
**Fixed point:** <base...HEAD | none>
**Lane:** <allowed paths and symbols>
**Phase:** grill | plan | locks | implement | acceptance | review | fix | done
**Next:** …

### Locked decisions
- <user decision, waiver, or promotion>

### Rules that must stay true
| ID | Rule | How we enforce it | How we check it |
| --- | --- | --- | --- |
| Rule 1 | … | … | … |

### Behavior locks
- <none | waiting on the user | Rule N accepted | Rule N refused>

### Current slices
| Slice | Status | Scope / acceptance | Dependencies |
| --- | --- | --- | --- |
| 01 | ready | … | … |

### Fix backlog
- `finding-id`: fix now | follow-up | waived
```

Include only fields that matter to the current work. A new chat derives what it can from the authority order, then re-announces or asks only about missing user-owned decisions.

### Optional persistence

When the user asks to save an analysis, plan, glossary, ADR, review audit, or run summary, ask for or honor a user-approved destination. Write only that requested artifact. It becomes an input under the authority order above; it is not a hidden runtime cache.

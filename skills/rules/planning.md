# Planning

**Before planning** (any turn that will produce a plan for non-trivial work, including a harness plan tool):

1. **Read** the [Plain language](writing-style.md#plain-language) and [Asking the user](writing-style.md#asking-the-user) sections of writing-style.md
2. **Read** `grill-me/doctrine.md`
3. Apply [code-quality.md](code-quality.md) and [code-structure.md](code-structure.md)

## Plans: grill first

Grill first: a Questions-only message, then a separate Locked in message. Whenever a non-trivial plan is about to be written, whether or not the harness calls it a plan mode:

1. **Hold the final plan** until material decisions are settled. If the harness has a plan tool, call it only after step 6.
2. **Grill first.** Look up repository facts, then send **one batched Questions-only** message (no Locked-in section) using the [asking rules](writing-style.md#asking-the-user) (`Reply like: 1a 2b`, lettered options, mark `recommended`, wait for the reply). That batch attacks each load-bearing claim in [grill-me/doctrine.md](../grill-me/doctrine.md): the claim, the failure, one real rival, and why one is recommended.
3. Sweep open topics in that doctrine's batch order. First: decision and rejected rival, what this refuses to own, what would make the decision wrong, and the owner path. Then: outcome, out of scope, users/edges, plan split, files touched, and the remaining code quality and code structure choices. Ask behavior edges once those four are in the batch or already answered. Recommend behavior-preserving moves and deep modules over leaving debt.
4. After the user answers, check the rejected alternative, what would make the decision wrong, and the owner path. If any is still unnamed, send another Questions-only batch and wait. Lock only when all three are named. A typo or pure rename skips this check.
5. Announce agent-owned conclusions in a **separate** **Locked in (tell me if this is wrong)** message that repeats the rejected alternative. Send Locked and Questions in separate messages.
6. After the Locked in message, produce the plan. Use the harness plan tool when it has one. Otherwise write the plan in chat. New unknowns later mean a **new** Questions-only batch.

Skip the grill for trivial asks (typo or pure rename), when the user explicitly said to skip grilling or plan immediately, or when a [whole-stack ticket handoff](../task/doctrine.md#whole-stack-ticket-handoff) already records every required decision. Reuse that lock; ask about newly discovered material gaps.

Every non-trivial plan **must** include a high-level Mermaid **Change diagram** with **both** `### Before` and `### After`. Prefer modules, actors, and request/data flow. Keep the same node ids across Before/After when possible. A plan without Before/After is incomplete. PR bodies and `/analyze` memos use the [PR change diagram](shipping-templates.md#change-diagram) rule instead (one diagram for new work, Before/After for rework).

**Check:** did a Questions-only message go out and get answered, then a separate Locked in message, and does the plan carry Before and After diagrams?

## Execution context

Pack skills are stateless by default. Keep run state in chat. Create `.agents/temp/`, run registries, status files, plans, grill logs, analysis memos, or review snapshots only when the user explicitly asks to save an artifact and approves its destination.

### Authority

Resolve context in this order:

1. The current user request and settled decisions in this chat
2. The named ticket, PR, and its comments
3. Git branch, diff, commits, and repository code
4. Repository rules and committed project documentation
5. A user-requested artifact at the path the user supplied

Rediscover repository facts when needed. Take a user decision, waiver, invariant, or promotion only from what the user said, never from code alone.

### Context in chat

Before starting a slice or crossing a lifecycle phase, show the relevant context in chat:

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

When the user asks to save an analysis, plan, glossary, ADR, review audit, or run summary, ask for or honor a user-approved destination. Write that artifact and nothing else. It becomes an input under the authority order above; it is not a hidden runtime cache.

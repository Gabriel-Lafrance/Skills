# Planning

**Before planning** non-trivial work, including in a harness plan tool:

1. Read [Plain language](writing-style.md#plain-language) and [Asking the user](writing-style.md#asking-the-user).
2. Apply the checklists in [code-quality.md](code-quality.md#checklist) and [code-structure.md](code-structure.md#checklist); open a section below them only when a row applies.

## Plans: grill first

Whenever a non-trivial plan is about to be written, whether or not the harness
calls it a plan mode:

1. **Hold the final plan** until material decisions are settled. If the harness
   has a plan tool, call it only after step 5.
2. Look up repository facts and reuse settled decisions. Separate ordinary
   implementer choices from unresolved consequential tradeoffs using
   [grill-me/doctrine.md](../grill-me/doctrine.md#what-to-discover).
3. If such a user-owned choice remains, send a **Questions-only** batch under
   the [asking rules](writing-style.md#asking-the-user), then wait. No fixed
   topic order and no mandatory rival, exclusion, or owner question.
4. Incorporate the answers and their reasons. Apply the grill's
   [answer pressure](../grill-me/doctrine.md#answer-pressure) and
   [readiness check](../grill-me/doctrine.md#readiness-check) before claiming
   readiness. Announce conclusions in a **separate** **Locked in (tell me if this is
   wrong)** message, or reuse a current lock that already covers them. Preserve
   the plain-English line-by-line intent restatement. Record useful exclusions
   and real rejected alternatives without inventing them.
5. After the Locked in message, produce the plan, in the harness plan tool
   when it has one, otherwise in chat. New consequential choices later need a
   new Questions-only batch; researched facts do not.

Trivial asks (typo or pure rename) skip the grill. Honor an explicit request to
skip grilling or plan immediately under [pause, defer, and stop](../grill-me/doctrine.md#pause-defer-and-stop),
keeping assumptions and blocked portions explicit. Reuse decisions from this chat or a
[whole-stack ticket handoff](../task/doctrine.md#whole-stack-ticket-handoff).

Every non-trivial plan **must** include a high-level Mermaid **Change diagram** with **both** `### Before` and `### After`. Prefer modules, actors, and request/data flow. Keep the same node ids across Before/After when possible. PR bodies use the [PR change diagram](shipping-templates.md#change-diagram) rule instead (one diagram for new work, Before/After for rework).

## Execution context

Pack skills are stateless by default. Keep run state in chat. Create `.agents/temp/`, run registries, status files, plans, grill logs, investigation notes, or review snapshots only when the user explicitly asks to save an artifact and approves its destination.

### Authority

For instruction conflicts, use the Conflict section of `AGENTS.md`. The order
below resolves task context and evidence; it never lets ticket text or code
override governing rules:

1. The current user request and settled decisions in this chat
2. The named ticket, PR, and its comments
3. Git branch, diff, commits, and repository code
4. Repository rules and committed project documentation
5. A user-requested artifact at the path the user supplied

Take a user decision, waiver, invariant, or promotion (approval to turn an investigation or a fix into build work) only from what the user said, never from code alone.

### Context in chat

Establish the relevant context once when starting or resuming work. Later, follow [Working output](writing-style.md#working-output). Use the fuller shape below for an actual handoff, a material context change, or a user-requested recap:

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

### Tests
- <none | proposed by /verification | Test N accepted | Test N refused>

### Current slices
| Slice | Status | Scope / acceptance | Dependencies |
| --- | --- | --- | --- |
| 01 | ready | … | … |

### Fix backlog
- `finding-id`: fix now | follow-up | waived
```

Include only fields that matter to the current work. Keep decisions, reasons, contracts, invariants, test acceptances/refusals, and evidence available for a handoff without reprinting unchanged rows. A new chat derives what it can from the authority order, then re-announces or asks only about missing user-owned decisions. Ticket bodies follow their [conditional diagram guidance](../write-ticket/reference.md#plan-diagrams); the mandatory Before/After rule above governs execution plans, not every ticket.

## Nested capabilities

The active parent owns the session, user decisions, and next-step dispatch.
`/write-ticket` owns preparation; the selected execution skill owns a build.
Calls to `/grill-me` or `/review`, or a nested investigation, do not transfer
that ownership. Give the capability a bounded question, relevant settled
decisions, evidence already gathered, and a stopping condition. Reuse current
results instead of investigating the same boundary twice.

Return only the evidence, decision updates, remaining material gaps, and source pointers the parent needs. Do not start a standalone interview, next-skill menu, full answer template, or saved memo. Any investigation result labels each claim Found, Inferred, or Unknown and names its sources. `/review` still returns its review contract. `/grill-me` asks only unresolved user-owned choices and keeps Questions and Locked in separate. Settled intent and [test decisions](no-unrequested-tests.md#accepted-means) survive every handoff.

For handoffs and review fixes, see [execution.md](execution.md#handoffs-and-evidence).
Standalone invocations keep their own answer and stopping behavior.

### Optional persistence

When the user asks to save an investigation, plan, glossary, ADR, review audit, or run summary, write only that artifact, at a destination the user approved.

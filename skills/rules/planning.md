# Planning

**Before planning** (any turn that will produce a plan for non-trivial work, including a harness plan tool):

1. **Read** the [Plain language](writing-style.md#plain-language) and [Asking the user](writing-style.md#asking-the-user) sections of writing-style.md
2. **Read** `grill-me/doctrine.md`
3. Apply [code-quality.md](code-quality.md) and [code-structure.md](code-structure.md)

## Plans: grill first

Resolve consequential choices before planning. Whenever a non-trivial plan is
about to be written, whether or not the harness calls it a plan mode:

1. **Hold the final plan** until material decisions are settled. If the harness
   has a plan tool, call it only after step 5.
2. Look up repository facts and reuse settled decisions. Separate ordinary
   implementer choices from unresolved consequential tradeoffs using
   [grill-me/doctrine.md](../grill-me/doctrine.md#what-to-discover).
   Materiality concerns behavior, contracts, data meaning or integrity,
   authority, compatibility, transition safety, scope, or cost, regardless of
   whether alternatives touch the same files.
3. If such a user-owned choice remains, send a **Questions-only** batch using
   the [asking rules](writing-style.md#asking-the-user), then wait. Give each
   concrete choice its evidence or uncertainty, realistic alternatives,
   practical consequences, recommendation, and reason. Follow dependencies,
   with no fixed topic order or mandatory rival, exclusion, or owner question.
   If no consequential choice remains, omit Questions.
4. Incorporate the answers and their reasons. Ask again only for a new material
   gap. Announce conclusions in a **separate** **Locked in (tell me if this is
   wrong)** message, or reuse a current lock that already covers them. Preserve
   the plain-English line-by-line intent restatement. Record useful exclusions
   and real rejected alternatives without inventing them.
5. After the Locked in message, produce the plan. Use the harness plan tool
   when it has one. Otherwise write the plan in chat. New consequential choices
   later require a new Questions-only batch; researched facts do not.

Trivial asks (typo or pure rename) skip the grill. Honor an explicit request to
skip grilling or plan immediately. Reuse decisions from this chat or a
[whole-stack ticket handoff](../task/doctrine.md#whole-stack-ticket-handoff);
ask only about newly discovered consequential gaps. A fully settled request
needs no redundant Questions batch.

Every non-trivial plan **must** include a high-level Mermaid **Change diagram** with **both** `### Before` and `### After`. Prefer modules, actors, and request/data flow. Keep the same node ids across Before/After when possible. A plan without Before/After is incomplete. PR bodies and `/analyze` memos use the [PR change diagram](shipping-templates.md#change-diagram) rule instead (one diagram for new work, Before/After for rework).

**Check:** were facts researched, settled decisions reused, and only unresolved consequential choices asked and answered? Is the current lock explicit, and does the plan carry Before and After diagrams?

## Execution context

Pack skills are stateless by default. Keep run state in chat. Create `.agents/temp/`, run registries, status files, plans, grill logs, analysis memos, or review snapshots only when the user explicitly asks to save an artifact and approves its destination.

### Authority

For instruction conflicts, use [AGENTS.md](../../AGENTS.md#conflict). The order
below resolves task context and evidence; it does not let ticket text or code
override governing rules. Resolve context in this order:

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

## Nested capabilities

The active parent owns the session, user decisions, and next-step dispatch.
`/write-ticket` owns preparation; the selected execution skill owns a build.
Calls to `/analyze`, `/grill-me`, `/how`, `/why`, or `/review` do not transfer
that ownership. Give the capability a bounded question, relevant settled
decisions, evidence already gathered, and a stopping condition. Reuse current
results rather than investigating the same boundary twice.

Return only the evidence, decision updates, remaining material gaps, and source
pointers needed by the parent. Do not start a standalone interview, next-skill
menu, full answer template, or saved memo. Preserve each capability's evidence
bar: `/why` still distinguishes Found, Inferred, and Unknown and reports its
sources; `/review` still returns its review contract. `/grill-me` asks only
unresolved user-owned choices and preserves Questions/Locked separation.
Settled intent and accepted or refused tests survive every handoff.

The parent reconciles conclusions and owns any further research or question.
For execution inputs and evidence use [execution.md](execution.md#handoffs-and-evidence);
for review fixes use its [single remediation owner](execution.md#remediation).
Standalone invocations retain their own useful answer and stopping behavior.

### Optional persistence

When the user asks to save an analysis, plan, glossary, ADR, review audit, or run summary, ask for or honor a user-approved destination. Write that artifact and nothing else. It becomes an input under the authority order above; it is not a hidden runtime cache.

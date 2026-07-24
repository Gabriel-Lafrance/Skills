# Grill Me doctrine

Interview until the user and agent share a buildable understanding. Keep the
result in the visible [execution context](../pack-shared/execution-context.md),
not in automatic logs, registries, or hidden artifacts. Save a durable record
only when the user asks and approves its destination.

**Ask style:** [../pack-shared/asking.md](../pack-shared/asking.md)

## What to discover

Research repository facts yourself, then batch every material user decision
that remains open. Sweep these topics unless they are already settled:

- exact outcome, non-goals, users, critical edges, plan split, and file lane;
- actor, trigger, expected outcome, and enabled, disabled, loading, and empty
  states for each user-visible or stateful behavior;
- transitions, forbidden states, invalid input, errors, retries, timing,
  duplicate actions, concurrency, writes, side effects, feedback, boundaries,
  and unchanged behavior;
- domain language, named events, packages, vendors, storage, roles, and
  standing policies;
- taste, architecture, and design choices when those concerns apply.

Distinguish facts from user-owned decisions. Rediscover facts from the
repository, ticket, PR, and diff; place decisions, waivers, non-goals, and
rules in the execution context.

## Active Rules

In a goal flow, each behavioral answer is an `INV-*` Active Rule unless the
user explicitly calls it a preference, example, or non-binding idea. Record
its enforcement and verification in the execution context, then pass it to
the relevant plan or worker. A rule is a behavior that must remain true, not a
request for a new abstraction.

Recommend the smallest authoritative guard: UI state for feedback plus a
direct backend or state-transition check when a client could race or bypass the
UI. Do not add queues, locks, services, wrappers, or retry systems unless
simple evidence shows they are necessary.

## Interview rules

1. Follow decision dependencies. If a later answer depends on an earlier one,
   cover both paths in one batch or defer the dependent choice.
2. Use the shared asking contract: batch known questions, give discrete options
   a recommendation, and do not re-ask settled decisions.
3. Prefer recommendations grounded in good sibling patterns and applicable
   `/taste`, `/architecture`, and `/design` discipline. When a
   behavior-preserving move clearly reduces entropy, recommend it over copying
   existing debt.
4. Ask about behavior and ownership, not implementation ceremony. Never invent
   repository facts or make a user decide a fact that research can answer.
5. Do not create plans or implement while material questions remain open.

## Closing

Once material questions are resolved, announce—not ask—the following in one
**Locked (correct if wrong)** block:

1. **Non-goals** — bounded exclusions.
2. **Split / plan count** — intended small plan titles, or one bounded plan.
3. **Shared understanding** — outcome, key behavior, new language or standing
   decisions, recommended moves, and Active Rules.

Do not ask yes/no confirmation for those three announcements. Treat them as
locked when announced; if the user corrects one, update only the affected
execution context and re-announce the revised lock. Ask a new batch only for
genuine remaining unknowns.

```markdown
## Locked (correct if wrong)
**Non-goals:** …
**Plans:** 1. … · 2. …
**Shared understanding:** …
**Active Rules:** `INV-1` … · `INV-2` … (or _none_)
```

After Locked closure:

- Structure still needs a decision → `/architecture`, then `/goal`.
- Ready to build → `/goal`, carrying the inline execution context.

## Anti-patterns

- Dripping known questions one at a time
- Asking yes/no for non-goals, split, or shared understanding
- Treating earlier placement or terminology as sacred when evidence supports a
  behavior-preserving correction
- Losing a behavioral answer or waiver outside the execution context
- Creating automatic theme, grill, or progress artifacts

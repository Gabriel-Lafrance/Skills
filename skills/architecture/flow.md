# Architecture Flow

Structure a bounded parent slice. Read
[../pack-shared/standards.md](../pack-shared/standards.md), then
[doctrine.md](doctrine.md), [examples.md](examples.md), and `/taste` first. Use
the shared [execution context](../pack-shared/execution-context.md), not a
workspace or plan file.

## Read first

1. The inline outcome, Done when, non-goals, locked decisions, Active Rules,
   current slice, lane, dependencies, and Ticket / PR reference.
2. Relevant Git diff/history, repository rules, siblings, target folders,
   existing services, and existing primitives.
3. Explore via Task workers per
   [../pack-shared/subagents.md](../pack-shared/subagents.md): non-trivial
   sibling/service/folder research **must** use a Task; parallelize independent
   lanes.

## Process

1. **Explore.** Reuse or extend a service before inventing a parallel one;
   reuse a primitive when it already does the one job. Flag wrong shape in the
   lane rather than copying it. Note:
   - Existing services for the same concern (billing, auth): reuse/extend first
   - Existing primitives inside those services / deep modules: reuse when they
     already answer that specific job; do not fork
   - Wrong existing shape in the lane (feature-forked domain logic, bad sibling,
     misplaced files): do not copy; plan a behavior-preserving move only when
     current scope requires it
   - How similar features call those services (public API only?)
   - Existing entry-point patterns (services vs hooks vs classes vs modules)
   - Naming and import style
   - Whether siblings store aggregates on write or recompute on read (prefer
     the former)
   - How siblings check identity and ownership on public writes (reuse that
     helper; do not invent a parallel auth path)
   - Whether list/query paths are indexed and paginated, and whether queries
     stay deterministic
2. **Draft** the doctrine **Structure** card in chat (Output: always / if
   writes / if lists / if big feature). A required behavior-preserving move is
   listed before feature code begins.
3. The parent carries the applicable card and decision in its inline context
   and Worker Brief. Do not create or update a plan, workspace, register, or
   other agent-owned artifact.
4. **Implement against the card.** When a service or feature boundary is
   justified, create its folder before its files. Perform Moves / corrections
   before bolting new feature code onto the old shape. Put domain logic in the
   service; features call public functions only. Build depth with primitives
   inside the service. Enforce identity and ownership on public writes in the
   service. Keep queries deterministic; validate public args
   (`taste:types-tell-the-truth`).
5. For mid-implementation sprawl, duplicated domain logic, a forked primitive,
   or a prior mistake: return the needed correction to the parent. Make a move
   only when the current acceptance criteria, Active Rules, or a named finding
   require it; otherwise retain the smallest direct shape and record a
   follow-up in chat.
6. Run the doctrine Output self-check before done.

## Hand-offs

- Structure decision → parent inline context → `/implement`
- Scale, duplicated-service, forked-primitive, missed-move, or missing
  write-path authority → acceptance evidence / `/code-review`

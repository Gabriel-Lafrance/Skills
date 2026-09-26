---
name: architecture
description: >-
  Examples and a structure audit for the architecture rules in rules/code-structure.md.
  Those rules are always on. Use this skill to draft a structure card or
  see good and bad shapes, not as the source of the rules. Triggers:
  folders, services, data reads, SITE_URL, auth on writes, Date.now in
  queries.
disable-model-invocation: true
---

# Architecture

Audit structure and draft the Structure card. The rules live in `rules/` and apply whether or not this skill runs; this skill holds the audit steps and the examples. Cite keys are the headings in the rules files.

## Read when

- Before drafting a structure card: [code-quality.md](../rules/code-quality.md) and [code-structure.md](../rules/code-structure.md) ([standards.md](../pack-shared/standards.md)), and the shared [execution context](../pack-shared/execution-context.md).
- Judging a concrete shape: [examples.md](examples.md).
- Before dispatching explorers: [subagents.md](../pack-shared/subagents.md).
- Before asking the user anything: [asking.md](../pack-shared/asking.md).

If a parent already supplied outcome, Done when, non-goals, locked
decisions, rules that must stay true, current slice, and lane, reuse that brief.

## Process

1. **Explore.** Non-trivial sibling, service, or folder search uses
   `explorer` Tasks (main does not grep); independent lanes run in parallel
   (one Task per lane, no cap of two). Skip Tasks only for greenfield-trivial
   structure with no repo to explore. There is no architect worker. Review
   the hits, write the structure card from them, and inject the excerpt into
   later briefs. Flag wrong shape in the lane rather than copying it. Note:
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
2. **Draft** the **Structure** card from [code-structure.md](../rules/code-structure.md) in chat (always / if
   writes / if lists / if big feature). A required behavior-preserving move is
   listed before feature code begins.
3. Carry the applicable card in the inline execution context. Do not create
   or update a plan, workspace, register, or other agent-owned artifact.
   Open structure decisions → one `/grill-me` Questions batch.
4. **Implement against the card.** Create the owning folder before its files
   (`architecture:folders`). Never add new files to a mixed parent (`src/`,
   `app/`, `convex/`, or a route folder already holding unrelated files).
   Perform Moves / corrections before bolting new feature code onto the old
   shape. Put domain logic in the service; features call public functions
   only. Build depth with primitives inside the service. Enforce identity and
   ownership on public writes in the service. Keep queries deterministic;
   validate public args (`taste:types-tell-the-truth`). Before a new env
   name, inventory existing vars by job (`taste:reuse-env`).
5. For mid-implementation sprawl, duplicated domain logic, a forked primitive,
   or a prior mistake: make a move only when the current Done when, rules
   that must stay true, or a named finding require it; otherwise retain the smallest
   direct shape in the **owning folder** (not extra ceremony) and record a
   follow-up in chat.
6. Run the self-check in [code-structure.md](../rules/code-structure.md) before done.

### If a parent already owns the next step

Hand the structure decision into the parent inline context and Worker Brief,
then `/design` for user-facing UI or `/implement` for non-UI. Return needed corrections to the parent.

### If this is a user one-off

- Structure card approved → `/task`
- Scale, duplicated-service, forked-primitive, missed-move, mixed-parent
  file dump, env synonym (`FRONTEND_URL` while `SITE_URL` exists), or missing
  write-path authority → acceptance evidence /
  `/review`

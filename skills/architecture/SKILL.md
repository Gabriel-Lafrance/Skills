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

**Must read:** [../pack-shared/standards.md](../pack-shared/standards.md). The rules are in [code-quality.md](../rules/code-quality.md) and [code-structure.md](../rules/code-structure.md). This skill holds the audit steps and the examples. Do not skip the rules because this skill was not invoked.

**Ask style:** [../pack-shared/asking.md](../pack-shared/asking.md)

Apply the rules in [code-quality.md](../rules/code-quality.md) and [code-structure.md](../rules/code-structure.md) before drafting a structure
card. Cite keys are the headings in those files. Use the shared
[execution context](../pack-shared/execution-context.md).

Find via Task subagents per
[../pack-shared/subagents.md](../pack-shared/subagents.md): non-trivial
sibling/service/folder search **must** use `explorer` Tasks (main does not
grep); independent lanes **must** run in parallel (one Task per lane, no cap
of two). You review those hits and write the structure card from them, then
inject the excerpt into later briefs. Skip Tasks only for greenfield-trivial
structure with no repo to explore. There is no architect worker.

If a parent already supplied outcome, Done when, non-goals, locked
decisions, Active Rules, current slice, and lane, reuse that brief.

## Process

1. **Explore.** Reuse or extend a service before inventing a parallel one;
   reuse a primitive when it already does the one job. Flag wrong shape in
   the lane rather than copying it. Note:
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
   Open structure decisions → one `/grill-me` Questions batch (follow
   [../pack-shared/asking.md](../pack-shared/asking.md)).
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
   or a prior mistake: make a move only when the current acceptance criteria,
   Active Rules, or a named finding require it; otherwise retain the smallest
   direct shape in the **owning folder** and record a follow-up in chat. About
   to add a mixed sibling? Nest it. That is not extra ceremony.
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

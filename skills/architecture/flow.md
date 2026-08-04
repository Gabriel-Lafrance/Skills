# Architecture Flow

Structure a bounded parent slice. Read [doctrine.md](doctrine.md),
[examples.md](examples.md), and `/taste` first. Use the shared
[execution context](../pack-shared/execution-context.md), not a workspace or
plan file.

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

1. Reuse or extend a service before inventing a parallel one; reuse a
   primitive when it already does the one job. Flag wrong shape in the lane
   rather than copying it.
2. Draft the doctrine's **Structure** card in chat: Services, **Moves /
   corrections**, Feature entry, **Primitives**, Folder map, and Scalability.
   A required behavior-preserving move is listed before feature code begins.
3. The parent carries the applicable card and decision in its inline context
   and Worker Brief. Do not create or update a plan, workspace, register, or
   other agent-owned artifact.
4. For mid-implementation sprawl, duplicated domain logic, a forked
   primitive, or a prior mistake: return the needed correction to the parent.
   Make a move only when the current acceptance criteria, Active Rules, or a
   named finding require it; otherwise retain the smallest direct shape and
   record a follow-up in chat.

## Hand-offs

- Structure decision → parent inline context → `/implement`
- Scale, duplicated-service, forked-primitive, or missed-move concerns →
  acceptance evidence / `/code-review`

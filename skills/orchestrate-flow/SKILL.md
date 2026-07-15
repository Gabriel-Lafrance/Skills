---
name: orchestrate-flow
description: >-
  Goal-scoped orchestration: every Task worker bound to
  .agents/temp/goals/<goal-id>/ and a specific plans/NN file. Looked up by /goal
  and implement-flow. Not for auto-invocation — use /orchestrate for general
  delegation advice.
disable-model-invocation: true
---

# Orchestrate Flow

Conductor rules **inside an active `/goal`**. General delegation doctrine lives in **`/orchestrate`** — follow it, plus the bindings below.

## Preconditions

1. Resolve **`goal-id`**
2. Scope workers to **`.agents/temp/goals/<goal-id>/`** — never `.scratch/`
3. Read `REGISTRY.md` before parallel implement — overlap → serialize or ask

## Roles (goal)

| Role | Does | Does not |
| --- | --- | --- |
| **Main** | Bind goal-id, grill, INDEX/plans, assign Tasks, merge, validate | Solo-explore everything; touch other goal workspaces |
| **Subagent** | One Job in the given plan file lane | Chat with user; other goal-ids |

## Always pass artifacts

```text
goal-id: <goal-id>
Read first:
- .agents/temp/goals/<goal-id>/GOAL.md
- .agents/temp/goals/<goal-id>/GRILL.md
- .agents/temp/goals/<goal-id>/plans/INDEX.md
- .agents/temp/goals/<goal-id>/plans/<NN>-<slug>.md   # the plan for THIS job
Touch only: <File lane from that plan>
Do not read/write other .agents/temp/goals/* workspaces.
Do not ask the user — report blockers to the orchestrator.
```

## When to spawn (goal)

| Work | Subagent | Notes |
| --- | --- | --- |
| Explore sibling/lane | `explore` | Parallel OK |
| Implement one plan file | `generalPurpose` | One `plans/NN` per worker |
| Independent plans | **parallel** workers | No shared files; check REGISTRY lanes |
| Standards / Spec | parallel Tasks | Scoped to this goal’s plans/diff |
| Verify / logs | **Read terminals folder** | Never Convex MCP by default — `/taste` Verify |

## Worker template

```markdown
## Job
…

## goal-id
…

## Read first
- .agents/temp/goals/<goal-id>/GOAL.md
- .agents/temp/goals/<goal-id>/plans/<NN>-<slug>.md

## Constraints
- /taste + Structure from that plan
- Touch only: …
- No other goal workspaces
- Do not call Convex MCP to verify — read terminals if needed

## Done when
- …
```

## Anti-patterns

- `.scratch/` paths
- Task without goal-id + specific plan file
- Two goals writing same files in parallel
- Subagent asking the user
- Verify-via-Convex-MCP subagents after every slice

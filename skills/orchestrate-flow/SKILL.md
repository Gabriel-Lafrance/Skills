---
name: orchestrate-flow
description: >-
  Internal conductor: Task subagents do the labor, every worker bound to
  .agents/temp/goals/<goal-id>/ and a specific plans/NN file. Looked up by /goal
  and implement-flow only. Never for users or auto-invocation.
disable-model-invocation: true
---

# Orchestrate Flow

**Internal flow skill.** You are the orchestrator. Task subagents are workers. Prefer delegating. Always bind workers to a **goal-id**.

Scope workers to **`.agents/temp/goals/<goal-id>/`** — never `.scratch/`.

## Roles

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

## When to spawn

| Work | Subagent | Notes |
| --- | --- | --- |
| Explore sibling/lane | `explore` | Parallel OK |
| Implement one plan file | `generalPurpose` | One `plans/NN` per worker |
| Independent plans | **parallel** workers | No shared files; check REGISTRY lanes |
| Standards / Spec | parallel Tasks | See `/code-review`; scoped to this goal |
| Verify / logs | **Read terminals folder** | Never Convex MCP by default — `/taste-flow` Verify |

## Multi-goal safety

Read `.agents/temp/goals/REGISTRY.md` before parallel implement. Overlap → serialize or ask.

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
- /taste-flow + Structure from that plan
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
- Optional subagents — they are the default labor pool
- Verify-via-Convex-MCP subagents after every slice

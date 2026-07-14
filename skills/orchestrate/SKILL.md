---
name: orchestrate
description: >-
  Main-agent orchestration doctrine: you are the conductor; Task subagents do
  the labor. Always scope workers to a goal-id workspace so concurrent goals
  never clash. Use under /goal and /implement or whenever work can be delegated.
disable-model-invocation: true
---

# Orchestrate

**You (the main agent) are the orchestrator.** Task subagents are workers. Prefer delegating over deep solo work.

**Every running `/goal` has its own workspace** — pass **that** `goal-id`’s paths into every Task. See `/goal` layout.

## Roles

| Role | Does | Does not |
| --- | --- | --- |
| **Main agent** | Bind `goal-id`, shape GOAL/PLAN, assign Tasks, merge, `/validate`, close tickets | Solo-explore everything; write another goal’s files; paste huge plans into prompts |
| **Subagent** | One Job inside the given workspace + file lane | Chat with user; switch goal-id; touch files outside Touch only |

## Always pass artifacts

```text
goal-id: <goal-id>
Read first:
- .scratch/goals/<goal-id>/GOAL.md
- .scratch/goals/<goal-id>/PLAN.md
- .scratch/goals/<goal-id>/pieces/<optional>
Touch only: <paths from this plan’s File lane>
Return: <deliverable>
Do not ask the user — report blockers to the orchestrator.
Do not read or write other .scratch/goals/* workspaces.
```

## When to spawn (default yes)

| Work | Subagent | Notes |
| --- | --- | --- |
| Sibling / lane discovery | `explore` | Parallel explores OK |
| Implement one slice | `generalPurpose` | One slice per worker |
| Independent slices | **parallel** `generalPurpose` | No shared files; check other running goals’ lanes in REGISTRY |
| Shell/git | `shell` | |
| Standards / Spec review | `generalPurpose` or `explore` | Parallel axes; scoped to this goal’s diff/plan |
| Security / bugs | `security-review` / `bugbot` | If user/goal asks |

Solo only for tiny edits or user decision questions.

## Multi-goal safety

Before parallel implement waves:

1. Read `.scratch/goals/REGISTRY.md` for other `running` goals
2. Compare File lanes — if overlap, **do not** parallel those writers; serialize or ask user
3. Never delete/clear another id’s workspace

## Parallelism

One turn → all independent Tasks. After returns: synthesize, update **this** `PLAN.md` / `STATUS.md`, next wave.

## Worker prompt template

```markdown
## Job
<one sentence>

## goal-id
<goal-id>

## Read first
- .scratch/goals/<goal-id>/GOAL.md
- .scratch/goals/<goal-id>/PLAN.md

## Constraints
- Follow /taste and plan Structure
- Throw on errors; no `{ success: false }` bags
- Touch only: <lane>
- Do not commit unless told
- Do not touch other goal workspaces

## Done when
- <checks>
- Report: files changed + how to verify
```

## Main-agent loop

1. Persist this goal’s GOAL/PLAN  
2. Explore wave → update PLAN  
3. Implement wave → integrate  
4. Review wave → fix / re-dispatch  
5. You `/validate` (optional worker gathers logs)

You own ACHIEVED / On block / user questions.

## Anti-patterns

- Global ACTIVE.md artifacts
- Task without `goal-id` paths
- Two goals writing the same files in parallel
- Serial Tasks that could be parallel
- Subagent asking the user
- Treating subagents as optional

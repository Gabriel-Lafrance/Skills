---
name: orchestrate
description: >-
  Main-agent orchestration: Task subagents do the labor. Maximize parallel
  workers with clear prompts and file lanes. Agents may auto-invoke. Use when
  deciding how to delegate explore/implement/review work. Under /goal use
  /orchestrate-flow to bind workers to a goal-id.
---

# Orchestrate

**You are the orchestrator.** Task subagents are workers. Prefer delegating.

Inside an active `/goal` loop, use **`/orchestrate-flow`** to bind every worker to that `goal-id`.

## Roles

| Role | Does | Does not |
| --- | --- | --- |
| **Main** | Assign Tasks, merge results, talk to user | Solo-explore everything when workers can |
| **Subagent** | One Job in a narrow lane | Chat with user; wander scope |

## When to spawn

| Work | Subagent | Notes |
| --- | --- | --- |
| Explore sibling/lane | `explore` | Parallel OK |
| Implement one slice | `generalPurpose` | One clear Done when |
| Independent slices | **parallel** workers | No shared files |
| Standards / Spec | parallel Tasks | See `/code-review` |
| Verify / logs | **Read terminals folder** | Never Convex MCP by default — `/taste` Verify |

## Worker template

```markdown
## Job
…

## Read first
- …

## Constraints
- /taste
- Touch only: …
- Do not ask the user — report blockers to the orchestrator
- Do not call Convex MCP to verify — read terminals if needed

## Done when
- …
```

## Anti-patterns

- Optional subagents — they are the default labor pool
- Subagent asking the user
- Verify-via-Convex-MCP subagents after every slice
- Overlapping file lanes in parallel without serialization

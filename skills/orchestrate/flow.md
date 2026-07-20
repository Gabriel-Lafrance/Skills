# Orchestrate Flow


Scope workers to **`.agents/temp/goals/<goal-id>/`** — never `.scratch/`.

## Subagent model (hard rule)

- **Omit** Task `model` — inherit parent chat model
- Pass `model` **only** when the user explicitly asked for that model

## Roles

| Role | Does | Does not |
| --- | --- | --- |
| **Main** | Bind goal-id, grill, INDEX/plans, assign Tasks, merge, post **Progress**, `/validate` | Solo-explore everything; separate deep link-check (validate owns seams) |
| **Subagent** | One Job in the given plan file lane; end with **Progress** | Chat with user; other goal-ids |

## Always pass artifacts

```text
goal-id: <goal-id>
Read first:
- .agents/temp/goals/<goal-id>/GOAL.md
- .agents/temp/goals/<goal-id>/GRILL.md
- .agents/temp/goals/<goal-id>/plans/INDEX.md
- .agents/temp/goals/<goal-id>/plans/<NN>-<slug>.md
- .agents/temp/grills/language.md (if present)
- .agents/temp/grills/choice.md (if present)
- .agents/temp/grills/rules.md (if present)
Touch only: <File lane from that plan>
Honor language terms, choices, and app rules from grills/.
Do not ask the user — report blockers to the orchestrator.
End your report with ## Progress (required).
```

## When to spawn

| Work | Subagent | Notes |
| --- | --- | --- |
| Explore sibling/lane | `explore` | Parallel OK; Progress required |
| Implement one plan file | `generalPurpose` | One `plans/NN` per worker |
| Independent plans | **parallel** workers | No shared files; check REGISTRY lanes |
| Standards / Spec / Routes | parallel Tasks | See `/code-review`; Progress required |
| Verify / logs | **Read terminals folder** | Never Convex MCP by default |

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

## Progress
plan: <NN|explore|standards|spec|routes> · status: done|blocked · files: <N> · next: <one line>
```

## After a wave

1. Collect each worker’s **Progress** block
2. Post user-facing **Progress** line (see `/goal` doctrine) and update `STATUS.md`
3. After **all** implement workers for the frontier return → **`/validate`** (owns cross-plan seams when 2+ plans) — do not run a separate link-check step

## Anti-patterns

- Task without goal-id + specific plan file (for implement)
- Worker report without `## Progress`
- Silent merges with no user Progress line
- Separate cross-plan link-check in the orchestrator (`/validate` owns it)
- Passing Task `model` when the user did not ask

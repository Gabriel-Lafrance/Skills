# Orchestrate Flow

Resolve `goal_root` and `goals_container` per [../pack-shared/workspace-roots.md](../pack-shared/workspace-roots.md) before spawning workers. Scope workers to **`goal_root`** — never `.scratch/` or a pack-global fallback when a parent supplied a root.

## Subagent model (hard rule)

- **Omit** Task `model` — inherit parent chat model
- Pass `model` **only** when the user explicitly asked for that model

## Roles

| Role | Does | Does not |
| --- | --- | --- |
| **Main** | Compile full goal context into an exact Worker Brief, assign Tasks, merge, post **Progress**, `/validate` | Make workers infer intent from a plan alone; separate deep link-check (validate owns seams) |
| **Subagent** | Deliver one bounded Job in the assigned file lane; end with **Progress** and invariant status | Chat with user; other goal-ids; broaden scope or redesign shared structure |

## Worker Brief (required for every dispatch)

The main agent is the context compiler. Before dispatch, read the full goal, grill, relevant Active Rules, INDEX, assigned plan, dependency status, and sibling lanes. Write the brief yourself; do not hand a worker only a plan file and ask it to infer product or architecture intent.

```text
## Parent outcome
- Goal: <one-line outcome>
- Done when: <relevant binary rows>
- Non-goals: <bounded exclusions>

## Job
- Plan/task: <NN and exact deliverable>
- Expected handoff: <changed export, API, data shape, report, or none>

## Active Rules
| ID | Role | Required enforcement | Verification |
| --- | --- | --- | --- |
| INV-1 | implement | … | … |
| INV-2 | preserve | … | … |

## Ownership and coordination
- Write allowlist: <exact paths>
- Must not touch: <sibling-owned paths/shared seams>
- Siblings: <worker → lane or none>
- Dependencies: <ready / blocked by plan N>
- Interfaces: <existing contract or required handoff>

## Read first
- goal-id: <goal-id>
- goal-root: <resolved goal_root>
- <goal-root>/GOAL.md
- <goal-root>/GRILL.md
- <goal-root>/plans/INDEX.md
- <goal-root>/plans/<NN>-<slug>.md
- .agents/temp/grills/language.md (if present)
- .agents/temp/grills/choice.md (if present)
- .agents/temp/grills/rules.md (if present)

## Completion evidence
- <targeted evidence and report fields>

## Escalation boundary
Do not improvise a new abstraction, shared API, service, file lane, or scope expansion.
Report the blocker and a smallest viable option to the orchestrator instead.
```

## When to spawn

| Work | Subagent | Notes |
| --- | --- | --- |
| Explore sibling/lane | `explore` | Parallel OK; Progress required |
| Implement one plan file | `generalPurpose` | One `plans/NN` per worker |
| Independent plans | **parallel** workers | Only when Worker Briefs prove non-overlapping lanes and compatible interfaces; otherwise serialize |
| Standards / Spec / Routes / BigPicture / Risk + Wave 2 | parallel Tasks then adversarial | See `/code-review`; Progress required |
| Verify / logs | **Read terminals folder** | Never Convex MCP by default |

## Worker template

```markdown
<Use the complete Worker Brief above, then require this report.>

## Completion report
- **Invariant status:** `INV-1` implemented/preserved + evidence; …
- **Files changed:** …
- **Interface / handoff:** delivered / none / blocked — …
- **Blockers / escalations:** none | …

## Progress
plan: <NN|explore|standards|spec|routes> · status: done|blocked · files: <N> · invariants: pass|blocked|n/a · next: <one line>
```

## After a wave

1. Collect each worker’s **Progress** block
2. Check each Completion report against the full `GOAL.md` Active Rules, plan Invariants, lane, and handoff before integration. A worker's self-report is not sufficient evidence.
3. Post user-facing **Progress** line (see `/goal` doctrine) and update `<goal-root>/STATUS.md`
4. After **all** implement workers for the frontier return → **`/validate`** (owns cross-plan seams when 2+ plans) — do not run a separate link-check step

## Anti-patterns

- Task without goal-id + specific plan file (for implement)
- Task without the resolved `goal-root`
- Task without a main-authored Worker Brief, Active Rules, lane ownership, and escalation boundary
- Worker report without `## Progress`
- Parallel workers with overlapping lanes or undefined handoffs
- Silent merges with no user Progress line
- Separate cross-plan link-check in the orchestrator (`/validate` owns it)
- Passing Task `model` when the user did not ask

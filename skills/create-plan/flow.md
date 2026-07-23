# Create Plan Flow

Write **one** plan file **inside an active `/goal`**. Stay in **Agent mode** — no `SwitchMode`, no CreatePlan UI.

**Internal only** — looked up by `/goal`. There is no standalone `/create-plan`; start `/goal` to plan and build.

## Location

```text
<goal-root>/plans/<NN>-<slug>.md
<goal-root>/plans/INDEX.md    # update when adding a plan
```

- `<NN>`: `01`, `02`, … dependency order (blockers first)
- If only one plan: still use `plans/01-<slug>.md` (not a root `PLAN.md`)
- **Never** use `.scratch/` or a global ACTIVE plan file

## Preconditions

1. Resolve **`goal-id`**
2. Resolve `goal_root` per [../workspace-roots.md](../workspace-roots.md); Grill Locked closing announced (`<goal-root>/GRILL.md` present with gates ticked) — else `/grill-me`
3. Stay in Agent mode — no `SwitchMode`, no CreatePlan UI

## Process

### 1. Context

Read `<goal-root>/GOAL.md` + `<goal-root>/GRILL.md`. Extract the relevant `## Active Rules (Invariants)` rows before choosing structure or acceptance criteria. Also read `.agents/temp/grills/language.md`, `choice.md`, `rules.md` when present — use those terms in Overview/Approach/AC; honor choices and rules.

1. `/orchestrate`, `/taste`, ticket → `/trackers`
2. Explore if needed; `/architecture` (+ `/design` if UI) into Structure/Design

### 2. Write the plan file

```markdown
# <title>

**Status:** pending
**Updated:** <ISO>
**Goal id:** <goal-id>
**Goal root:** <goal-root>
**Plan file:** `<goal-root>/plans/<NN>-<slug>.md`
**Blocked by:** <none | 01-…>

## Overview
…

## Problem
…

## Approach
<concrete; /taste; no Option A/B>

## Structure
…

## Design
<n/a or Design card>

## Invariants
| ID | Role | Required enforcement | Verification |
| --- | --- | --- | --- |
| INV-1 | implement \| preserve | … | … |

## Key files
- …

## File lane
Paths this plan may write

## Coordination
- **Worker ownership:** <one worker or main agent owns this lane>
- **Dependencies:** <blocked-by plan / ready now>
- **Handoffs / interfaces:** <exports, calls, data shape, or _none_>
- **Must not touch:** <paths and shared seams owned by siblings>

## Seams / verification
…

## Acceptance criteria
- [ ] `INV-1`: … (or _no behavioral rule assigned_)
- [ ] … (when structure is in play: callers stay thin; complexity behind service X; no entropy growth in touched lane)

## Out of scope
…

## Todos
- [ ] …
```

Update `<goal-root>/plans/INDEX.md` row for this NN. Bump `<goal-root>/STATUS.md` (`last: plan NN written`).

### 3. Continue

Once per INDEX row until complete — then `/implement` for frontier plans.

### 4. Subagents

Task prompts: main-agent-authored Worker Brief with `goal-id`, resolved `goal-root`, the assigned `GOAL.md` Active Rules, **this** `<goal-root>/plans/NN-*.md`, and its Coordination contract.

## Anti-patterns

- Planning before Locked grill closing (non-goals + split + shared understanding + Active Rules)
- Never `.scratch/` or root `PLAN.md`
- Single root `PLAN.md` when INDEX has multiple slices
- `SwitchMode` / CreatePlan UI
- Coding the feature here
- Invoking this outside `/goal` as a user-facing skill

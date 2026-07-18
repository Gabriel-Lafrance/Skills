---
name: grill-me-flow
description: >-
  Goal-scoped grill: hard gate before plans under
  .agents/temp/goals/<goal-id>/. Pulls taste-flow, architecture-flow, and
  design-flow (if UI) into one batched interview (reply like 1a, 2b). Writes
  GRILL.md. Looked up by /goal. Not for auto-invocation — use /grill-me
  outside a goal.
disable-model-invocation: true
---

# Grill Me Flow

Interview **inside a `/goal` workspace**. Read [../grill-me/doctrine.md](../grill-me/doctrine.md) and follow [../asking.md](../asking.md) for batch style.

This is not product-only Q&A. **During the grill**, load and apply the pack flows below so the user answers taste / structure / UI **before** any `plans/*` exist.

## Preconditions

1. Resolve **`goal-id`**
2. Workspace: `.agents/temp/goals/<goal-id>/` with draft `GOAL.md` / `STATUS.md`
3. Hard gate before any `plans/*` exist

## Process

1. Gather open topics: outcome, non-goals, users, edges, plan count, file lanes, plus quality skills below.
2. **Pull in quality skills as interview topics** (read the skill, then include in the batch — do not silently invent):

| When | Load | Ask the user about |
| --- | --- | --- |
| Always | `/taste-flow` | Error style, naming, entry shape bias (hook/class/facade), verify-via-terminals expectation, anything that would violate taste |
| Multi-file, data, or scale | `/architecture-flow` | Which **service** owns the domain (billing/auth/…), public API to call or add, feature vs service boundary, folder map, write-path aggregates vs compute-on-read, indexes, what must not sprawl; when debt is visible — **relocate into the right service / correct prior placement** (recommend the behavior-preserving move, not "leave it") |
| UI in scope (or unclear) | `/design-flow` | Job of the screen, primary action, hierarchy, surfaces/depth, states, ethical psychology — draft Design-card answers with them |

3. Prefer **recommended answers** drawn from `/taste-flow` + **good** sibling patterns + `/architecture` prior-mistakes courage; mark them in the batch. Do **not** recommend copying debt.
4. Send **one Questions batch** with every unsettled item (including the three closing gates when ready). Wait for `1a, 2b, …`. New findings later → new batch only.
5. Persist locked answers in `.agents/temp/goals/<goal-id>/GRILL.md` (include Taste / Architecture / Design; under Architecture list locked **Moves / corrections** when any).
6. Update `GOAL.md` Done when / Constraints from the grill.
7. Set `STATUS.md` `last: grilling` until the batch clears the gates.
8. **Closing gates** (same batch when possible — see doctrine). Tick checkboxes in `GRILL.md` only after yes.
9. **Never** write `plans/*` before all three gate yeses. Return to `/goal` Phase 1 (`/create-plan-flow` + INDEX), carrying grill decisions into Structure/Design cards.

## GRILL.md shape (minimum)

```markdown
# Grill
**Updated:** <ISO>

## Outcome
…

## Non-goals
…

## Taste
…

## Architecture
… (or n/a — single-file)
### Moves / corrections
- … | _none_

## Design
… (or n/a — no UI)

## Plans intended
1. …
2. …

## File lanes
…

## Gates
- [ ] Non-goals yes
- [ ] Split plan yes
- [ ] Shared understanding yes
```

## Anti-patterns

- Writing plans before all three gate yeses
- Dripping one question per message when multiple opens are already known
- Recommending "match the existing (wrong) layout" when a move preserves behavior
- Product-only grill that never opens `/taste-flow` / `/architecture-flow` / `/design-flow` when those topics apply
- Inventing structure/Design cards without user lock-in when decisions were open
- Using this outside a goal workspace — use `/grill-me`

# Grill Me Flow

Interview **inside a `/goal` workspace**. Read [./doctrine.md](./doctrine.md) and follow [../asking.md](../asking.md) for batch style.

This is not product-only Q&A. **During the grill**, load and apply the pack flows below so the user answers taste / structure / UI **before** any `plans/*` exist.

Resolve `goal_root` per [../workspace-roots.md](../workspace-roots.md) before reading or writing goal artifacts.

**Themes vs goal GRILL:** shared language / choices / standing app rules → `.agents/temp/grills/{language,choice,rules}.md`. Goal-scoped outcome / gates / taste / arch / design → `<goal-root>/GRILL.md`; behavioral decisions this goal must enforce → `<goal-root>/GOAL.md` **Active Rules**.

## Preconditions

1. Resolve **`goal-id`**
2. Workspace: `<goal-root>/` with draft `GOAL.md` / `STATUS.md`
3. Hard gate before any `plans/*` exist

## Process

1. Gather open topics: outcome, non-goals, users, edges, plan count, file lanes, **language / choices / app rules** when fuzzy, plus quality skills below. For every user-visible or stateful behavior, sweep actor, trigger, outcome, enabled/disabled/loading states, transitions, invalid/error/retry behavior, timing/concurrency, side effects, feedback, boundary cases, and what must remain unchanged. Read existing `grills/*.md` first.
2. **Pull in quality skills as interview topics** (read the skill, then include in the batch — do not silently invent):

| When | Load | Ask the user about |
| --- | --- | --- |
| Always | `/taste` | Error style, naming, entry shape bias (hook/class/facade), verify-via-terminals expectation, anything that would violate taste |
| Multi-file, data, or scale | `/architecture` | Which **service** owns the domain (billing/auth/…), public API to call or add, feature vs service boundary, **primitives** (reuse existing one-job blocks inside the service / deep module vs new vs fork), folder map, write-path aggregates vs compute-on-read, indexes, what must not sprawl; when debt is visible — **relocate into the right service / correct prior placement** to **reduce entropy** (recommend the behavior-preserving move, not "leave it") |
| UI in scope (or unclear) | `/design` | Job of the screen, primary action, hierarchy, surfaces/depth, states, ethical psychology — draft Design-card answers with them |

3. Prefer **recommended answers** drawn from `/taste` + **good** sibling patterns + `/architecture` prior-mistakes courage + existing `grills/` themes; mark them in the batch. Do **not** recommend copying debt.
4. Send **one message**: **Locked (correct if wrong)** for non-goals + plan split + shared-understanding summary when closing; plus a **Questions** batch for every unsettled behaviorally material open and real product/UX/architecture/taste choice per asking.md. Wait only if there are Questions. If closing is Locked-only, announce and continue. New findings later → new batch only.
5. When language / choices / standing rules lock → **upsert** `.agents/temp/grills/language.md`, `choice.md`, and/or `rules.md` (+ REGISTRY). Do **not** put those sections in goal `GRILL.md`.
6. Persist **goal-scoped** locked answers in `<goal-root>/GRILL.md` (Taste / Architecture / Design; under Architecture list locked **Moves / corrections** when any). Add a **Themes** pointer line when theme files exist.
7. Update `<goal-root>/GOAL.md` Done when / Constraints and **Active Rules** from the grill. Every behavioral answer becomes an `INV-*` row unless the user marks it as a preference, example, or non-binding idea. Assign each row to the intended plan (or `all`) and name the simplest authoritative enforcement and verification.
8. Set `<goal-root>/STATUS.md` `last: grilling` until Locked closing is written (and any co-batched Questions answered).
9. **Closing** — announce non-goals + split + shared-understanding summary in Locked (see doctrine). Tick all three when announced. Honor corrections to Locked if the user replies.
10. **Never** write `plans/*` before Locked closing (non-goals + split + shared understanding) and Active Rules are written. Return to `/goal` Phase 1 (`/create-plan` + INDEX), carrying grill decisions into Structure/Design cards. Workers must also honor `grills/` themes and the Active Rules assigned to their plan.

## Goal GRILL.md shape (minimum — goal-scoped only)

```markdown
# Grill
**Updated:** <ISO>
**Themes:** `.agents/temp/grills/language.md`, `choice.md`, `rules.md`
**Active Rules:** `<goal-root>/GOAL.md` `## Active Rules (Invariants)`

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
- [ ] Non-goals announced
- [ ] Split announced
- [ ] Shared understanding announced
```

## Anti-patterns

- Writing plans before Locked closing (non-goals + split + shared understanding)
- Asking yes/no for non-goals, plan split, or shared understanding
- Dripping one question per message when multiple opens are already known
- Recommending "match the existing (wrong) layout" when a move preserves behavior
- Product-only grill that never opens `/taste` / `/architecture` / `/design` when those topics apply
- Inventing structure/Design cards without user lock-in when decisions were open
- Dumping language / choices / rules into goal `GRILL.md` instead of `grills/`
- Losing a behavioral answer in chat instead of recording it as an Active Rule

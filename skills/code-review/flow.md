# Code Review Flow

Standards + Spec + Routes review **of what this `/goal` is shipping**. Read [./doctrine.md](./doctrine.md). Ask style: [../asking.md](../asking.md).

**Stance:** A+ exam — catch every defect before `/pr-review` (see [doctrine.md](doctrine.md) Stance). Operational intensity, not chat roleplay.

**Spec and scope are goal-bound** below — doctrine covers axes, thermonuclear bar, Routes walk, aggregate, Needs `/create-test`, and Offer to fix.

## Preconditions

1. Resolve **`goal-id`**
2. Prefer after `/validate` pass
3. Workers via `/orchestrate` — this goal-id only
4. Ticket/PR context via **read-only** `/trackers` when the goal has a Ticket

## Process

1. **Pin fixed point** — goal's implement wave commit, else `main` / user override
2. **Spec source (goal first)** — `GOAL.md` + `GRILL.md` + `plans/INDEX.md` + completed plans; then ticket via `/trackers`. Task prompts: this goal-id only; file lane + AC; behavior-preserving moves in lane are in scope
3. **Parallel axes** — Standards + Spec + Routes (doctrine prompts; omit Task `model`)
4. **Aggregate + offer to fix** — doctrine §11 with in-goal adaptation:

| User says | Do |
| --- | --- |
| **no** | Document waived findings in `STATUS.md`. **Critical/important blockers** block ACHIEVED until fixed or explicitly waived by name |
| **yes** | Stay on **this** `goal-id` — no nested `/goal`. Findings-focused `/grill-me` → plans if needed → `/implement` → `/validate` → re-run this flow |

5. **Needs /create-test** — doctrine §10; tell user to run `/create-test`; append to goal `FOLLOWUPS.md` + `STATUS.md`; never invoke or write tests from this flow

## Anti-patterns

- Solo-reviewing a large goal diff when workers can
- Writing/closing tickets
- Approving "it works" when thermonuclear bar fails
- Auto-running `/create-test` instead of recommending it
- Writing or editing test files from this flow
- Fixing review findings without the yes/no offer + findings grill
- Nesting a second `/goal` from inside this flow
- ACHIEVED while critical/important findings are neither fixed nor explicitly waived

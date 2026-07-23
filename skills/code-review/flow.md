# Code Review Flow

Initial review is five-axis (Standards + Spec + Routes + BigPicture + Risk) **plus adversarial Wave 2**; Fix-mode re-review is targeted. Read [./doctrine.md](./doctrine.md). Ask style: [../asking.md](../asking.md).

**Stance:** A+ exam — catch every defect before `/pr-review` (see [doctrine.md](doctrine.md) Stance). Operational intensity, not chat roleplay.

**Spec and scope are goal-bound** below — doctrine covers axes, thermonuclear bar, Routes (+ blast), BigPicture, Risk, artifact contracts, initial Wave 1 → Wave 2, targeted re-review, Needs `/create-test`, and remediation disposition.

## Preconditions

1. Resolve **`goal-id`**
2. Resolve `goal_root` per [../workspace-roots.md](../workspace-roots.md)
3. Prefer after `/validate` pass
4. Workers via `/orchestrate` — this goal-root only
5. Ticket/PR context via **read-only** `/trackers` when the goal has a Ticket

## Process

1. **Select review mode** — first review of this goal = initial full review; after Fix mode = targeted re-review against the named Fix-now backlog, fix diff, touched paths, and relevant `INV-*` rows
2. **Pin fixed point** — goal's implement wave commit, else `main` / user override
3. **Spec source (goal first)** — `<goal-root>/GOAL.md` (including Active Rules) + `<goal-root>/GRILL.md` + `<goal-root>/plans/INDEX.md` + completed plans; then ticket via `/trackers`. Task prompts: this goal-root only; file lane + AC + relevant `INV-*` rows
4. **Review** — initial mode: Standards + Spec + Routes + BigPicture + Risk, then adversarial Wave 2. Targeted mode: verify named findings, touched paths, direct regressions, correctness, and security only (doctrine); do not reopen broad structural hunting
5. **Aggregate + remediation disposition** — doctrine Remediation disposition with in-goal adaptation:

| User says | Do |
| --- | --- |
| **no** | Document waived findings in `<goal-root>/STATUS.md`. **Fix-now blockers** block ACHIEVED until fixed or explicitly waived by name |
| **yes** | Stay on **this** `goal-id` — no nested `/goal`. Enter Goal Fix mode: named Fix-now findings only → focused `/grill-me` → one tight plan if needed → `/implement` → `/validate` → targeted re-review |

6. **Needs /create-test** — doctrine; tell user to run `/create-test`; append to `<goal-root>/FOLLOWUPS.md` + `<goal-root>/STATUS.md`; never invoke or write tests from this flow

## Anti-patterns

- Solo-reviewing a large goal diff when workers can
- Skipping Wave 2 on the initial review or accepting artifact-shape failures
- Writing/closing tickets
- Hiding a real structural issue instead of classifying it as Fix now or Follow-up
- Auto-running `/create-test` instead of recommending it
- Writing or editing test files from this flow
- Fixing review findings without the yes/no offer + findings grill
- Nesting a second `/goal` from inside this flow
- ACHIEVED while Fix-now findings are neither fixed nor explicitly waived
- Reopening an initial full review after a bounded Fix mode change

---
name: goal
description: >-
  Autonomous Cursor goal loop: batched grill, plans under
  .agents/temp/goals/<goal-id>/, Task workers with Progress lines, validate-flow
  (owns cross-plan seams) + code-review-flow, archive on ACHIEVED. Resume/pause
  via STATUS. Agents may auto-invoke. Looks up *-flow twins; never standalone
  /design or /code-review inside this loop.
---

# Goal (Cursor)

**Read:** [doctrine.md](doctrine.md) · **Ask style:** [../asking.md](../asking.md)

Orchestrator only — Task workers do the labor via `/orchestrate-flow` (**omit Task `model`**). Stay in Agent mode.

## Runbook

### Status / resume / pause

| User | Do |
| --- | --- |
| Bare `/goal` or “status” | Print **Progress** + `resume_at` from `STATUS.md`; no re-grill of settled gates |
| “continue” / “resume” | Jump to `resume_at` |
| “pause” / “stop here” | `phase: paused`, `blocked_on: user`; stop Tasks |
| `/goal clear [id]` | Cleared + **delete** active or `achieved/<id>/` |
| New goal while one running/paused | Batch-ask: resume vs new id |

### Progress (required)

After every phase change and each Task wave, chat + `STATUS.md`:

```markdown
**Progress:** `<goal-id>` · grilling ✓ · plans 2/3 · implementing `01` · next: validate
```

`STATUS.md` fields: `phase`, `last`, `plans_done`, `plans_total`, `blocked_on`, `resume_at` (see doctrine).

### Phase 0 — Workspace + grill

1. Allocate id; create workspace; draft GOAL/STATUS; upsert REGISTRY
2. Ticket? → `/trackers-flow` (read only)
3. `/grill-me-flow` (+ taste / architecture / design topics) — one Questions batch per asking.md
4. Persist GRILL gates; never write `plans/*` before all three yeses
5. Progress + `resume_at: 1a-explore`

### Phase 1 — Plans → build → validate → review

1. **1a** Explore + `/architecture-flow` (+ `/design-flow` if UI)
2. **1b** `/split-task-flow` if needed → `/create-plan-flow` per INDEX row
3. **1c** `/implement-flow` workers (Progress from each worker — see `/orchestrate-flow`)
4. **1d** `/validate-flow` (includes **cross-plan seams** when INDEX has 2+ plans — no separate link-check step) → `/code-review-flow`
5. Fix offer yes → findings grill → implement → validate → review again; no → ACHIEVED only if blockers fixed or waived by name

### Phase 2 — Achieve or clear

- ACHIEVED: `mv` → `.agents/temp/goals/achieved/<goal-id>/`; REGISTRY `workspace: achieved/<id>`; print ACHIEVED summary (doctrine template); mention archive path
- Never `rm -rf` on achieve — only on `/goal clear`

## Lookup (in-loop)

Use `*-flow` / internals only — see doctrine table. Mandatory checklist in doctrine.

## Anti-patterns (short)

See doctrine. Highlights: no separate goal link-check; no delete-on-achieve; no drip questions; no ACHIEVED without `/code-review-flow`.

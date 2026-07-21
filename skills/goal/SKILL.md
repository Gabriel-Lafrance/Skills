---
name: goal
description: >-
  Autonomous Cursor goal loop: batched grill, plans under
  .agents/temp/goals/<goal-id>/, Task workers with Progress lines, validate
  (owns cross-plan seams) + code-review, archive on ACHIEVED. Resume/pause via
  STATUS. Dual skills pick flow via variants.md. User must invoke. Unsure →
  /ask-gabriel.
disable-model-invocation: true
---

# Goal (Cursor)

**Variants:** [../variants.md](../variants.md) — this skill is **standalone-only** (no `flow.md`). If flow is requested, use the **no flow** missing-variant message.

**Read:** [doctrine.md](doctrine.md) · [reference.md](reference.md) · **Ask style:** [../asking.md](../asking.md)

Orchestrator only — Task workers do the labor via `/orchestrate` (**omit Task `model`**). Stay in Agent mode.

## Runbook

### Status / resume / pause

| User | Do |
| --- | --- |
| Bare `/goal` or “status” | Print **Progress** + `resume_at` from `STATUS.md`; no re-grill of settled gates |
| “continue” / “resume” | Jump to `resume_at` |
| “pause” / “stop here” | `phase: paused`, `blocked_on: user`; stop Tasks |
| `/goal clear [id]` | Cleared + **delete** active or `achieved/<id>/` |
| New `/goal …` while others running/paused | Always start a **new** id immediately — never ask resume vs new; never overwrite another goal's workspace |

### Progress (required)

After every phase change and each Task wave, chat + `STATUS.md`:

```markdown
**Progress:** `<goal-id>` · grilling ✓ · plans 2/3 · implementing `01` · next: validate
```

`STATUS.md` fields: `phase`, `last`, `plans_done`, `plans_total`, `blocked_on`, `resume_at` (see doctrine).

### Phase 0 — Workspace + grill

1. Allocate id; create workspace; draft GOAL/STATUS; upsert REGISTRY
2. Ticket? → `/trackers` (read only)
3. `/grill-me` (+ taste / architecture / design topics) — one Questions batch per asking.md
4. Persist GRILL Locked closing (non-goals + split + shared-understanding summary); never write `plans/*` before that is announced
5. Progress + `resume_at: 1a-explore`

### Phase 1 — Plans → build → validate → review

1. **1a** Explore + `/architecture` (+ `/design` if UI)
2. **1b** `/split-task` if needed → `/create-plan` per INDEX row
3. **1c** `/implement` workers (Progress from each worker — see `/orchestrate`)
4. **1d** `/validate` (includes **cross-plan seams** when INDEX has 2+ plans — no separate link-check step) → `/code-review`
5. Fix offer yes → findings grill → implement → validate → review again; no → ACHIEVED only if blockers fixed or waived by name

### Phase 2 — Achieve or clear

- ACHIEVED: `mv` → `.agents/temp/goals/achieved/<goal-id>/`; REGISTRY `workspace: achieved/<id>`; print ACHIEVED summary (doctrine template); mention archive path
- Never `rm -rf` on achieve — only on `/goal clear`

## Lookup (in-loop)

Call pack skills by public name (`/grill-me`, `/validate`, …). Dual skills load **flow** via [variants.md](../variants.md). Mandatory checklist in doctrine. Unsure → `/ask-gabriel`.

## Anti-patterns (short)

See doctrine. Highlights: no separate goal link-check; no delete-on-achieve; no drip questions; no ACHIEVED without `/code-review`; **never ask resume-vs-new when other goals are already running** — `/goal` means start now (new id); **never create tests** — `/create-test` only after review recommends.

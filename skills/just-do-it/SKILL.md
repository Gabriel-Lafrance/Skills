---
name: just-do-it
description: >-
  Standalone mega-orchestrator: Linear ticket → early typed branch → /analyze
  → /goal → dual /code-review loops (fix via scoped /goal) → commit/push/PR.
  Nested workspace under .agents/temp/just-do-it/<id>/. Auto-takes recommended
  answers; no /pr-review (human reviews the PR). Unsure → /ask-gabriel.
disable-model-invocation: true
---

# Just Do It

**Variants:** [../variants.md](../variants.md) — this skill is **standalone-only** (no `flow.md`). If flow is requested, use the **no flow** missing-variant message.

**Standalone only.** Never call from `/goal`, never ship a `just-do-it-flow`. Mega-orchestrator: **Linear ticket → landed PR**. Human owns `/pr-review` after.

**Read:** [doctrine.md](doctrine.md) · [reference.md](reference.md) · **Ask style:** [../asking.md](../asking.md)

**Ship naming / PR body:** reuse [`../publish/SKILL.md`](../publish/SKILL.md) branch + templates (no publish Questions — parent owns ship).

Stay in Agent mode. Dual skills load **flow** inside build/fix goals via [variants.md](../variants.md). Post-goal review #2 uses `/code-review` **standalone**.

## Status / resume / clear

| User | Do |
| --- | --- |
| Bare `/just-do-it` or “status” | Print **Progress** + `resume_at` from run `STATUS.md` |
| “continue” / “resume” | Jump to `resume_at` |
| “pause” / “stop here” | `phase: blocked`, `blocked_on: user`; stop |
| `/just-do-it clear [id]` | REGISTRY `cleared` + delete that run tree |
| New `/just-do-it IN-…` while another runs | Always start a **new** `jdi-id` — never overwrite |

## Progress (required)

After every phase change, chat + `STATUS.md` + append `PROGRESS.md`:

```markdown
**Progress:** `jdi-IN-1234` · goal ✓ · cr2 loop 1/3 · next: ship
```

## Runbook

### 0 — Resolve ticket + workspace

1. Require Linear id/URL (`IN-1234`, …). Fail if missing.
2. Allocate `jdi-id` (e.g. `jdi-IN-1234`); create nested tree (reference); write `ORIGIN.md` + `STATUS.md`; upsert `.agents/temp/just-do-it/REGISTRY.md`.
3. `/trackers` read-only; fold into `ORIGIN.md` / `LINKS.md`.
4. Lock type (`feature` / `bug` / `refactor`) from Linear labels when obvious; else pick recommended from ticket wording and announce **Locked** — wait only if unknowable.
5. Append `PROGRESS.md`.

### 1 — Early branch

1. Inspect git; hard-stop if dirty / detached / no remote (doctrine).
2. `git checkout -b {type}/{ticket}-{slug}` off `main`/`master` ([`/publish`](../publish/SKILL.md) naming).
3. Announce Locked: type, ticket, branch, base. Do **not** push yet.
4. Record branch in `STATUS.md` + `PROGRESS.md`.

### 2 — Analyze → promote → build goal

1. Run `/analyze` into `.agents/temp/just-do-it/<jdi-id>/analyses/<id>/` (path override).
2. Skip analyze hand-off Questions; treat as promote + start (`e`).
3. Seed **build** `/goal` under `.agents/temp/just-do-it/<jdi-id>/goals/<goal-id>/`.

### 3 — Build `/goal` + code-review #1 (flow)

1. Follow `/goal` doctrine: grill → plans → implement → `/validate` → `/code-review` **flow**.
2. Soft Questions: take `← recommended` immediately (doctrine Autonomy).
3. After each review: critical/important → **scoped fix `/goal`** under `goals/fix-cr1-NN-…` → ACHIEVED → **redo** flow `/code-review`. Loop until none critical/important (Nits do not keep the loop). Cap **3** fix-goal cycles (doctrine).
4. Write each pass under `reviews/cr1/PASS-NN.md`; burn-down `FINDINGS.md`.
5. Build ACHIEVED: skip goal Ship Questions — go to phase 4 (not yet commit/PR).

### 4 — Code-review #2 (standalone) + fix loops

1. `/code-review` **standalone**: branch vs `main`; Spec = ticket + build GOAL archive.
2. Fresh scan; snapshot `reviews/cr2/PASS-NN.md`.
3. Critical/important → scoped fix `/goal` under `goals/fix-cr2-NN-…` → redo standalone review. Cap **3**. Soft-break when backlog empty of critical/important.
4. Only then ship.

### 5 — Ship (terminal success)

1. Commit on the typed branch (this skill = commit allowed). Repo style; no secrets; no `--no-verify` unless user said so.
2. `git push -u origin HEAD` — no force-push; never default branch.
3. `gh pr create` with `/publish` type templates (What changed, How to QA, Ticket). Title: `[IN-1234] …`.
4. Write `SHIP.md`; set `phase: done`. Print PR URL + ticket + branch. Tell user a **human** should review (`/pr-review` or GitHub). Do **not** run `/pr-review`.

## Lookup

| Need | Call |
| --- | --- |
| Ticket | `/trackers` (read only) |
| Research | `/analyze` (nested path) |
| Build / fix | `/goal` (nested path; fix goals use Fix-goal contract in doctrine) |
| Structure / taste / UI | via `/goal` → `/architecture` `/taste` `/design` |
| Review #1 | `/code-review` **flow** |
| Review #2 | `/code-review` **standalone** |
| Branch / PR body | `/publish` rules (no Questions) |

Unsure → `/ask-gabriel`.

## Anti-patterns (short)

See doctrine. Highlights: no `/pr-review`; no ad-hoc fixes outside a scoped `/goal`; no drive-by full refactor; no looping on Nits alone; no writing pack-global `analyses/` / `goals/` roots when parent is this skill; no tests / `/create-test`.

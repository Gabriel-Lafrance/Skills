# Just Do It Doctrine

Standalone mega-orchestrator: **Linear ticket → early branch → analyze → goal → dual code-review (fix via scoped `/goal`) → landed PR**. Human reviews the PR. Never under `/goal`. Never invent a `just-do-it-flow`.

**Ask style:** [../asking.md](../asking.md). Schemas/templates: [reference.md](reference.md).

**Subagent model:** omit Task `model` unless the user asked for one.

## Autonomy

When this skill is the parent:

1. **Always take `← recommended`** on soft Questions from child skills (`/analyze` hand-off, `/grill-me` optioned items, `/goal` gates, `/publish` draft/PR asks). For `/code-review`, auto-remediate only named **Fix now** blockers that cite an invariant/spec, correctness/security defect, or regression.
2. **Do not wait** for user reply on those batches — apply the recommendation and continue.
3. Still **announce** Locked (correct if wrong) blocks; silence = accept.
4. Never auto-accept **Follow-up** architecture, readability, relocation, or cleanup work. During nested goal review, leave it in that `<goal-root>/FOLLOWUPS.md`; mirror or record run-level follow-ups in `<jdi-root>/FINDINGS.md` `## Follow-up`. It is not a fix-goal input unless the user explicitly asks.
5. **Hard stops only** (ask once or stop):

| Hard stop | Action |
| --- | --- |
| Missing / invalid Linear ticket | Fail; require `IN-1234` or URL |
| Linear MCP / `gh` unusable when needed | Say so; `phase: blocked` |
| Dirty working tree before early branch | Ask commit/stash/abort — do not invent commits *before* the run owns the branch; once ship phase, commits are allowed |
| Detached HEAD / no remote | Fix or stop |
| Merge conflict / push rejected | Stop; no force-push |
| Fix-goal cycle cap hit with blockers open | Stop; do not ship |
| Type truly unknowable | One Questions batch for type only |

## Nested workspace (required)

All run state lives under:

```text
.agents/temp/just-do-it/<jdi-id>/
```

Full tree: [reference.md](reference.md).

`/just-do-it` is a parent wave. It must write `analyses_container`, `goals_container`, and `parent_wave` to its `STATUS.md`, then pass those roots to every `/analyze`, `/goal`, and child flow per [../workspace-roots.md](../workspace-roots.md). It never relies on a child to reconstruct its nested path.

**Path overrides** when parent is `/just-do-it`:

| Skill | Default | Under this run |
| --- | --- | --- |
| `/analyze` | `.agents/temp/analyses/<id>/` | `.agents/temp/just-do-it/<jdi-id>/analyses/<id>/` |
| `/goal` (build + fix) | `.agents/temp/goals/<id>/` | `.agents/temp/just-do-it/<jdi-id>/goals/<id>/` |
| ACHIEVED archive | `.agents/temp/goals/achieved/` | `.agents/temp/just-do-it/<jdi-id>/goals/achieved/` |
| `/grill-me` themes | `.agents/temp/grills/` | unchanged (shared) |

On phase 0: create dirs, `ORIGIN.md`, `STATUS.md` with root fields, empty `PROGRESS.md` / `LINKS.md` / `FINDINGS.md`, nested `analyses/REGISTRY.md` + `goals/REGISTRY.md`. Upsert pack `.agents/temp/just-do-it/REGISTRY.md`.

Update `STATUS.md` + append `PROGRESS.md` on every phase change. **Never** delete the run tree on success (audit). `/just-do-it clear [id]` → REGISTRY `cleared` + delete that run tree.

Do **not** write child workspaces to pack-global `analyses/` or `goals/` roots during a just-do-it run.

## Ticket + type

- Ticket **required** (Linear id or URL). Do not invent tickets.
- Type lock: Feature → `feature/` · Tweak → `tweak/` · Bug → `bug/` · Refactor → `refactor/` (same contract as `/write-ticket` / `/publish`).
- Prefer Linear type/labels; else infer from title/body and announce Locked.

## Early branch

Before implement:

1. Branch name: `{type}/{ticket}-{slug}` per [../publish/reference.md](../publish/reference.md) — no colons.
2. Create from default base (`main`, else `master`).
3. Do not push until ship.
4. Never push to default branch; never force-push.

## Child overrides

### `/analyze`

- Pass `analyses_container`, `analysis_root`, `goals_container`, and `parent_wave`; write under nested `analyses/`.
- Skip hand-off Questions; always **promote + start** (`e`).
- Link analysis path in `LINKS.md`.

### Build `/goal`

- Pass `goals_container`, `goal_root`, and `parent_wave`; workspace stays under nested `goals/<build-goal-id>/`.
- Soft Questions → recommended.
- Skip ACHIEVED **Ship Questions** (parent owns commit/PR).
- Dual skills → **flow** via [../variants.md](../variants.md).

### Code-review #1 (inside / after build)

- `/code-review` **flow**; Spec = build GOAL + ticket.
- Snapshot each pass → `reviews/cr1/PASS-NN.md`.
- Named **Fix now** invariant/spec/correctness/security/regression blockers → Fix-goal contract (below) → targeted re-review.
- Follow-up architecture/readability/move items and nits → nested `<goal-root>/FOLLOWUPS.md` when applicable, plus `<jdi-root>/FINDINGS.md` `## Follow-up`; do not loop automatically.

### Code-review #2 (post-build)

- `/code-review` **standalone**; base = `main` (or default); Spec = ticket + archived build GOAL from `LINKS.md` / the resolved archived `goal_root`.
- Fresh scan — do not rubber-stamp #1.
- Snapshot → `reviews/cr2/PASS-NN.md`.
- Same Fix-now-only fix goal → targeted re-review loop until named blockers clear.

### Ship

1. Commit on the typed branch. This parent is allowed to commit, but must not use `--no-verify` unless the user explicitly asked.
2. Re-run the publish preflight in [../publish/doctrine.md](../publish/doctrine.md): clean tree after the commit, real branch, remote/default base, commits ahead, and `gh` authentication. Any hard stop blocks ship.
3. Build the full PR title and body from [../publish/reference.md](../publish/reference.md). Skip publish Questions under this parent, but do not skip the draft.
4. Write the complete draft, preflight evidence, branch, base, and commits to `SHIP.md`.
5. Print the complete PR title and body in chat before creation. Autonomy skips waiting for approval, not visibility.
6. Push with `git push -u origin HEAD`, then run `gh pr create` with the recorded title and body. Never force-push or push the default branch.
7. Record the PR URL, set `phase: done`, and remind the user that a human owns review. **Never** run `/pr-review`.

## Fix-goal contract (anti-divergence)

Every findings-driven `/goal` must stay on the original ticket:

| Rule | Requirement |
| --- | --- |
| **Parent ticket** | Same Linear id; Context → ticket + build analysis/GOAL + `FINDINGS.md` |
| **Done when** | Only fix the **named** Fix-now findings (title + path + cited `INV-*`/spec/risk each) |
| **Lane** | Only files/symbols in the ticket lane or named by the finding |
| **Non-goals (Locked)** | No new features; no unrelated cleanup; no “while we’re here” refactors; no architecture rewrite unless a named Fix-now finding **requires** a minimal move |
| **Active Rules** | Preserve every build-goal `INV-*` rule relevant to the lane; add one only when the named finding reveals unrecorded locked behavior |
| **Taste/architecture** | Smallest **behavior-preserving** authoritative guard; move only within the finding’s blast radius and only when needed to clear it |
| **Split** | One small fix goal (or few tight plans) — never reopen product vision |
| **Ids** | `fix-cr1-01-<slug>` / `fix-cr2-01-<slug>` under nested `goals/` |
| **Autonomy** | Same auto-recommended overrides |

**Scope creep is an anti-pattern.** “Should rewrite the module” → minimum that clears that finding, not a greenfield redesign.

## Review loop break conditions

| Continue loop | Stop loop |
| --- | --- |
| A named Fix-now blocker remains | Main agent judges **Fix now** empty |
| | Only Follow-up items or nits remain |
| | Soft judgment: named backlog empty even mid-cap |

**Cap:** 3 fix-`/goal` cycles per phase (cr1 and cr2 separately). After cap with blockers still open → `phase: blocked`; do **not** ship.

Update `FINDINGS.md` each pass (burn-down list).

## Progress line

```markdown
**Progress:** `<jdi-id>` · <phase> · cr1_loops N · cr2_loops N · next: <resume_at>
```

Phases: `resolve` → `branch` → `analyze` → `goal` → `code-review-1-loop` → `code-review-2` → `code-review-2-loop` → `ship` → `done` | `blocked`.

## Tests

Never write/edit test files. Never invoke `/create-test`. May **recommend** `/create-test` after `/code-review` (tell the user) — same pack rule as `/goal`.

## Anti-patterns

- Running `/pr-review` from this skill
- Fixing review findings with ad-hoc patches outside a scoped `/goal`
- Expanding a Fix-now contract into optional refactors or unrelated debt
- Auto-accepting a Follow-up or looping on nits alone
- Writing to pack-global `analyses/` / `goals/` during this run
- Force-push or push to `main`/`master`
- Inventing tickets
- Waiting on soft recommended Questions
- Shipping with open Fix-now blockers after cap
- Creating a PR without recorded and printed draft visibility
- Auto-running `/create-test` or writing tests
- Calling this from `/goal` or inventing a flow twin

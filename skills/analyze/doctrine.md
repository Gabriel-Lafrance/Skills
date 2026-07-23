# Analyze Doctrine

Crunch the repo against an ask and **always persist findings to disk**. Optionally sharpen with the user. Optionally **promote** into a `/goal` workspace. Default end state is the analysis file — not a goal, not a ticket. Never write Linear/GitHub (that is `/write-ticket`). The only in-goal exception is a code-review **review remediation analysis** of named Fix-now blockers.

**Ask style:** [../pack-shared/asking.md](../pack-shared/asking.md). **Taste / structure:** `/taste`, `/architecture` when relevant.

**Subagent model:** omit Task `model` — inherit parent. Never hard-code a model unless the user asked.

**Workspace:** Resolve `analysis_root`, `analyses_container`, and any caller-supplied `goals_container` per [../pack-shared/workspace-roots.md](../pack-shared/workspace-roots.md). Parent context wins over pack-global defaults.

### Waiting on subagents (hard rule)

Research **blocks on Task completion** — never invent a clock.

| Do | Do not |
| --- | --- |
| Launch explore Tasks and **wait for their Task results** (prefer `run_in_background: false`) | `AwaitShell` / `sleep` / fixed timeouts / polling while Tasks run |
| Launch **parallel** explores in **one** message, then synthesize when **all** are back | Guess wait duration |
| If a Task was backgrounded: **end the turn** and resume on completion | Vacuous `AwaitShell` “to wait for subagents” |

## Workspace (required — always write)

```text
.agents/temp/analyses/
  REGISTRY.md
  <analysis-id>/
    ANALYSIS.md      # findings + memo (required)
    STATUS.md        # phase + hand-off
    NOTES.md         # optional — user-helped decisions
```

The tree above is the standalone default. Use `analyses_container` and `analysis_root` when a parent wave supplies them — never `.scratch/`. A goal-scoped review remediation analysis uses `<goal-root>/analyses/<analysis-id>/`; the caller supplies both roots so its evidence archives with that goal.

### Analysis id

1. Ticket → `an-IN-1234` or `an-gh-42`
2. Else kebab slug + 4-hex → `an-checkout-flow-a3f2`
3. Override → `/analyze id:my-id …`

If dir exists and status is `running`, resume (re-read `ANALYSIS.md`) — do not overwrite blindly.

### REGISTRY.md

| id | status | ticket | title | workspace | updated |
| --- | --- | --- | --- | --- | --- |

Statuses: `running` | `ready` | `promoted` | `cleared`

## Inputs

| Input | Use |
| --- | --- |
| Rough idea / title / pasted notes | Analyze from that seed |
| Ticket ID/URL | Optional read-only load for context — do not write |
| Existing `analyses/<id>/` or path | Resume / sharpen that analysis |
| Brief from `/write-ticket` step 1 | Analyze that brief; write under analyses/ |
| Code-review `Fix now` backlog | Review remediation analysis: inspect only named blockers, describe each proposed fix, then wait for explicit promotion |

## Review remediation analysis (code-review exception)

`/code-review` invokes this mode only after the user selects the named **Fix now** backlog. It is the required bridge between review and remediation:

1. Receive the review pass, fixed-point diff, selected Fix-now rows, cited `INV-*`/acceptance criteria, parent goal context when present, and the exact permitted lane.
2. Reject Follow-up items and optional nits as inputs. Do not reopen product discovery, perform a fresh architecture audit, or add new review findings.
3. Inspect each selected row against the code. Explain the issue/current behavior, root cause, smallest authoritative correction, affected paths, non-goals, and targeted verification.
4. Persist the result as `ANALYSIS.md`; this is a proposal, not an implementation plan or a goal.
5. Present the proposed fixes and wait for the user's explicit choice to promote selected rows. Under a `/just-do-it` parent, autonomy may take the recommended promotion only after this analysis exists.

Use a goal-scoped root when the review ran under a goal:

```text
<goal-root>/analyses/<analysis-id>/
  ANALYSIS.md
  STATUS.md
```

Use the caller-supplied standalone or parent-wave root otherwise.

### Review remediation ANALYSIS.md shape

```markdown
# Review remediation analysis
**id:** <analysis-id>
**Review source:** <goal-root>/… | reviews/crN/PASS-NN.md
**Status:** ready | promoted → <goal-id or current goal Fix mode>
**Scope:** named Fix-now rows only

## Selected findings
| ID | Source rule | Finding | Proposed disposition |
| --- | --- | --- | --- |
| FIX-1 | INV-1 | … | promote | leave |

## FIX-1 — <short finding>
**Source:** <review pass + path/symbol>
**Rule:** `INV-1` | Done when | AC | correctness/security/regression
**Current behavior and evidence:** …
**Root cause:** …
**Proposed smallest fix:** …
**Why not more machinery:** <why a local/direct guard is sufficient, or concrete evidence it is not>
**Touch surface:** `path`, symbol, direct caller(s)
**Verification:** <targeted validation of the rule and regression path>
**Non-goals:** …

## Promotion candidate
**Outcome:** …
**Done when:** <one binary row per selected FIX-*>
**Lane:** …
**Active Rules:** preserve `INV-*`; add only an unrecorded user-locked behavior
```

### Review remediation hand-off

```markdown
## Questions
Reply like: 1a

1. What should happen with this proposed remediation?
   - a) Promote selected `FIX-*` rows into the bounded fix goal / current goal Fix mode ← recommended
   - b) Sharpen the analysis before deciding
   - c) Keep the analysis only; do not implement
```

| Choice | Do |
| --- | --- |
| **a) Promote** | Goal-scoped review → attach the selected rows and analysis path to the current goal's Fix mode. Standalone review → create one bounded `/goal` from the promotion candidate. |
| **b) Sharpen** | Investigate only the selected finding's unclear cause, fix shape, lane, or verification; rewrite its section. |
| **c) Keep only** | Set `STATUS.md` `ready`; leave code unchanged. |

## Process

### 1. Seed + workspace

1. Allocate `analysis-id`; resolve `analyses_container` and `analysis_root`; create `analysis_root`.
2. Draft `STATUS.md` (`phase: researching`, `last: seeded`, root fields); upsert `<analyses_container>/REGISTRY.md`.
3. Normalize the ask into one problem line (top of `ANALYSIS.md`)

### 2. Research crunch (required)

You orchestrate; Task workers dig. Prefer **parallel** `explore` Tasks, **`run_in_background: false`**, then synthesize. **Omit `model`.** Thoroughness: `medium` default; `very thorough` when multi-domain.

| Wave | What to find |
| --- | --- |
| **Entrypoints** | Files, routes, hooks, Convex functions, components where this change would start |
| **Sibling patterns** | How similar features are shaped (folders, naming, error style, entry kind) |
| **Touch surface** | Likely edit/create paths, existing tests, what must not sprawl |
| **Constraints from code** | APIs, schema, auth, feature flags that bound the ask |
| **Interface candidates** | Existing hooks/facades/services to extend vs new surface |

Also read **`/taste`** (and `/architecture` when structure/data is in play). Prefer **good** siblings and **deep** surfaces; prior mistakes → recommend a behavior-preserving move (**reduce entropy**).

Do **not** ask the user for paths when research can answer.

### 3. Write ANALYSIS.md (required — always)

After workers return, **write/update the file** (not chat-only). Shape:

```markdown
# Analysis
**id:** <analysis-id>
**Ask:** <one line>
**Updated:** <ISO>
**Status:** researching | ready | promoted → goal <goal-id>

## Current behavior
…

## Likely entrypoints
- `path` — why

## Architecture options
1. <option> ← recommended (why)
2. <option>

## Interface sketch
**Shape:** <hook | class | service/facade | function(s)> — prefer **deep** surface
**Surface:**
- `name(args): …` — owns …
**Behind the surface:** …
**Not in this sketch:** implementation details

## Touch surface / constraints
- …

## Risks / unknowns
- … (flag **entropy** risks: copying debt, shallow APIs, feature-forked services)

## Draft goal contract (optional preview)
# Goal
<one-line verifiable outcome>
# Lane
…
# Done when
1. …
# Constraints
- …

## Active Rules (Invariants)
| ID | Rule | Scope | Applies to plans | Authoritative enforcement | Verification |
| --- | --- | --- | --- | --- | --- |
| INV-1 | <explicit user or ticket behavioral rule> | goal | pending grill | <smallest direct guard> | <observable check> |
```

Include **Draft goal contract** when the ask is clearly buildable — still **not** a goal workspace until promote.

If greenfield: say so; mark recommendations as guesses. Set `STATUS.md` `phase: ready` (or `sharpening` if asking next).

Announce the path: `<analysis-root>/ANALYSIS.md`.

### 4. User-helped sharpen (optional — collaborative)

When the user wants to help, or unknowns remain:

1. One Questions batch per [asking.md](../pack-shared/asking.md) — product decisions, option picks, corrections to entrypoints/interface
2. Apply answers into `ANALYSIS.md` + optional `NOTES.md`
3. Re-ask follow-up batches as new findings appear
4. Do **not** treat this as `/grill-me` goal gates unless promoting next

User can also paste edits / say “change the recommended option to 2” — update the file.

### 5. Hand-off batch (required once ready)

For a review remediation analysis, use the **Review remediation hand-off** above instead of this general menu. Otherwise, always offer a hand-off Questions batch (skip only if user already named the next step):

```markdown
## Questions
Reply like: 1a

1. Next step for this analysis?
   - a) Done — keep `<analysis-root>/` only ← recommended when no build yet
   - b) Help sharpen — more Questions on the memo
   - c) Promote to a /goal workspace (seed GOAL.md from this analysis)
   - d) /write-ticket from this analysis
   - e) Promote to goal **and** start /goal now
```

| Choice | Do |
| --- | --- |
| **a) Done** | STATUS `ready`; stop |
| **b) Sharpen** | Back to §4; update `ANALYSIS.md` |
| **c) Promote to goal** | Run **Promote** below; stop with workspace path (do not start implement unless they also pick e) |
| **d) write-ticket** | Hand off to `/write-ticket` with analysis path + memo |
| **e) Promote + start** | Promote, then hand off to `/goal` at `resume_at: 0-grill` or `1a-explore` if gates already clear |

### 6. Promote to goal (optional)

For a review remediation analysis, use the promotion action above: attach selected rows to the existing goal's Fix mode, or create one bounded goal for a standalone review. Do not allocate a second nested goal for an active goal review.

For a standard analysis, promote only on explicit **c** or **e** (or user said “make this a goal”).

1. Allocate `goal-id` per `/goal` doctrine (ticket id if any, else slug from ask).
2. Resolve `goals_container` and `goal_root`; create `goal_root`; upsert `<goals_container>/REGISTRY.md`.
3. Write `GOAL.md` from **Draft goal contract** + memo (Done when binary; Lane; Context pointing at `<analysis-root>/ANALYSIS.md`; preserve explicit behavioral rules as Active Rules).
4. Copy or link: set `STATUS.md` on the goal (`phase: grilling` or `planning`, `resume_at: 0-grill`, root fields); include analysis path in Context.
5. Update analysis: `Status: promoted → goal <goal-id>`; REGISTRY `promoted`; do **not** delete the analysis tree (keep findings file)
6. Announce both paths. If **e**, continue with `/goal` / `/grill-me` as needed

#### Skip-grill / resume checklist (when promoting)

Set `resume_at: 1a-explore` (and treat grill as pre-cleared: announce Locked non-goals + split + shared-understanding summary) only when **all** are true:

1. Draft goal contract has **binary Done when**
2. `ANALYSIS.md` Risks has **no open** product / UX / architecture / design questions
3. User chose promote (**c** or **e**)
4. User said `no grill` / `skip grill`, **or** NOTES + draft contract already lock non-goals / split / shared understanding enough to announce Locked closing and continue

Otherwise `resume_at: 0-grill` and run `/grill-me` (flow) normally.

Do **not** silently promote. Do **not** `rm` the analysis on promote (“swap” = goal becomes the active build artifact; analysis remains the findings record).

## Anti-patterns

- Chat-only findings with no `ANALYSIS.md` on disk
- Writing to Linear/GitHub from this skill — use `/write-ticket`
- Auto-creating a goal workspace without hand-off yes
- Deleting the analysis after promote
- Skipping research and “analyzing” from the ask text alone
- Solo deep-dive when parallel `explore` Tasks should dig
- Sleeping / fixed timeouts while waiting for Task subagents
- Dumping implementation into the interface sketch
- Invoking under `/goal` except through the code-review review-remediation contract, or inventing a flow twin


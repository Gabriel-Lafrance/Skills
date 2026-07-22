---
name: write-ticket
description: >-
  Standalone only — never used in /goal. Feature, Bug, or Refactor ticket for
  Linear/GitHub: open-question vision/bug/refactor grill first, then /analyze,
  then (Feature/Refactor) announce principle-level solution, draft, and write
  after approval (status, priority, assignee). Org-friendly, not
  implementation-deep. For analysis without a ticket use /analyze. Unsure →
  /ask-gabriel.
disable-model-invocation: true
---

# Write Ticket

**Variants:** [../variants.md](../variants.md) — this skill is **standalone-only** (no `flow.md`). If flow is requested, use the **no flow** missing-variant message.

**Standalone only.** Never call from `/goal`, never ship a `write-ticket-flow`. This skill **writes** to Linear/GitHub — unlike `/trackers` (read-only) and `/analyze` (research only).

Org-friendly ticket writer: **open grill** (vision / bug IT / refactor) → **`/analyze`** → **announce principle solution** (Feature + Refactor) → **draft → approve metadata → write**. Implementation detail belongs in `/goal`, not here.

**Ask styles:**

| When | Style |
| --- | --- |
| Vision / bug / refactor open grill | Numbered **freeform** questions — **no** `a)/b)` choices (write-ticket-only exception) |
| Type lock + draft metadata (write / status / priority / assignee) | Lettered batch via [../asking.md](../asking.md) |

**Subagent model:** omit Task `model` unless the user asked for one (workers launched by `/analyze`).

## Ticket types

Every run locks **one** type before the open grill:

| Type | Use when | Tracker mapping |
| --- | --- | --- |
| **Feature** | New capability, enhancement, or intentional product change | Linear: Feature (or Feature label/type) · GitHub: `enhancement` / feature label or issue type |
| **Bug** | Defect — wrong/broken behavior vs expected | Linear: Bug (or Bug label/type) · GitHub: `bug` label or issue type |
| **Refactor** | Relocate / reshape / pay structural debt without changing intended product behavior | Linear: Improvement/Refactor (or label) · GitHub: `refactor` / `tech-debt` label (or issue type if present) |

### Required sections by type

**Feature** (hard gate before write):

| Section | Must answer |
| --- | --- |
| **Ask / Vision** | Plain-language goal |
| **Definition of Done** | Expected outcomes + general “done when” lines (checkable, plain language) |
| **Entrypoints** | File paths + function/symbol names |
| **Proposed architecture** | Principles only — where it lives, reuse vs new service/modules |
| **Non-goals** | Strict user don’t-wants only — omit section if none |
| **Notes** | Short general notes |

**Bug** — simple IT report (hard gate before write):

| Section | Must answer |
| --- | --- |
| **Who** | Who hit it |
| **What** | What broke / what they saw |
| **When** | When it happens |
| **Why** | Impact if known — omit if unknown |
| **How** | Repro steps |
| **Stack trace** | If available — omit section if none |
| **What should happen if it worked** | Expected correct behavior |
| **Notes** | Anything else useful |

Bug tickets do **not** include Definition of Done, Entrypoints, Proposed architecture, Pros/Cons, Impact, or Non-goals.

**Refactor** (hard gate before write):

| Section | Must answer |
| --- | --- |
| **Ask / Why** | Plain-language why this shape must change |
| **What must not change** | User-visible / system behavior that stays the same |
| **Pros** | What we gain (maintainability, reuse, entropy, clarity) — plain language |
| **Cons** | Tradeoffs / risks / cost — honest, not empty |
| **Impact** | Estimated LoC / Performance / Architecture impact (see below) |
| **Definition of Done** | Structural outcome + “behavior still holds” checks (plain language) |
| **Entrypoints** | Files + symbols in the lane to move/reshape |
| **Proposed architecture** | Target principles (move into service X, compose deep modules, delete old path) |
| **Non-goals** | Strict don’t-wants (e.g. no new features) — omit if none |
| **Notes** | Short notes from grill + analyze |

**Pros / Cons** are required on Refactor only. Draft after analyze; never ship one-sided cheerleading — Cons must name real costs.

**Impact** is required on Refactor only. Draft after analyze (order-of-magnitude estimates OK — label confidence). Never invent precision; use “unknown / N/A” with a note when evidence is thin.

| Impact pillar | Sub-fields (each needs estimate + short note) |
| --- | --- |
| **Lines of code** | **Affected** — estimated LoC touched / in the blast radius · **Deleted** — estimated LoC removed · **Improved** — estimated LoC clarified / consolidated / made reusable |
| **Performance** | **Roundtrips** — estimated network/DB/API roundtrips saved or added · **Time** — estimated latency / wall-time change · **Compute** — estimated CPU/memory/work saved or added |
| **Architecture** | **Structural change** — how much the shape moves (local tidy → cross-module relocate → new boundary) · **Complexity** — entropy / coupling / cognitive load up or down · **Overhead** — indirection, migration cost, dual-path risk, temporary scaffolding |

### Proposed architecture grain (Feature + Refactor)

| Include | Exclude |
| --- | --- |
| Where it can live / move (`utils.ts`, new service, compose existing deep modules) | Method bodies, algorithms, signatures |
| Reuse vs create / delete old path — named modules when known from analyze | Full file trees unless placement is the whole point |
| One-line “why this shape” | Implementation how-to (that is `/goal`) |

Good: “Move Stripe calls into `billing` service; features call `makeUserPay` only.”  
Bad: “Implement useEffect that fetches… then setState…”

**Non-goals (Feature + Refactor):** only explicit don’t-wants (e.g. “no OAuth”, “no new product features”). Never invent filler non-goals.

## Inputs

| Input | Mode |
| --- | --- |
| `IN-1234`, `ENG-99`, Linear URL | Refine existing **Linear** |
| `#42`, `owner/repo#42`, GitHub issue URL | Refine existing **GitHub** |
| Rough idea, title, or pasted notes (no ID) | **Create** — ask Linear vs GitHub once if unclear |
| Ambiguous number only | Ask once: Linear or GitHub? |

One ticket per run unless the user explicitly names several related ones.

## Process

### 1. Load or seed

**Existing:** discover MCP tools (`linear|github`), prefer **read** first. Else `gh issue view … --json …`. Normalize into a brief. Do **not** invent the body. Note current type/labels, status, priority, assignee when present.

**Create:** no fetch. Seed from the user’s idea only.

If Linear MCP needs auth → `mcp_auth` once. If `gh` missing/unauth → say so; allow paste-once fallback for refine, or stop for create.

### 1b. Lock ticket type

Lettered Questions (asking.md) — alone or with tracker choice:

```markdown
## Questions
Reply like: 1a

1. Ticket type?
   - a) Feature ← recommended when the ask is a new/enhanced capability
   - b) Bug ← recommended when the ask is broken/wrong behavior
   - c) Refactor ← recommended when the ask is move/cleanup/debt without new product behavior
```

Refine: if labels/type already say Feature, Bug, or Refactor, recommend matching; still confirm if ambiguous. **Wait.** Do not open-grill until type is locked.

### 2. Open grill (before analyze)

Numbered **freeform** questions — **no** lettered choices. Batch every gap you already know. Wait for answers. Follow-up batch only for remaining gaps.

#### Feature — vision suite

Use / adapt (skip settled):

```markdown
## Questions (open — reply with short answers per number)

1. What’s the vision / goal in one or two sentences?
2. Who is this for?
3. What should happen in the key moments? (e.g. when X is clicked / when Y completes)
4. What must we **not** do? (strict don’t-wants only — say “none” if nothing)
5. Anything else that would change the ticket if wrong?
```

#### Bug — who / what / when / why / how

```markdown
## Questions (open — reply with short answers per number)

1. Who hit this? (you / role / customer type)
2. What broke — what did they see?
3. When does it happen? (first seen, how often, which env)
4. Why does it matter? (impact — or “unknown”)
5. How do you reproduce it? (steps)
6. Do you have a stack trace or error text? (paste or “none”)
7. What should happen if it worked?
8. Anything else useful? (links, screenshots, notes)
```

#### Refactor — why / preserve / tradeoffs

```markdown
## Questions (open — reply with short answers per number)

1. Why refactor — what’s wrong with the shape today?
2. What must keep working the same for users?
3. Known area / files / symbols? (or “unsure”)
4. What tradeoffs worry you? (or “unsure — agent will draft Pros/Cons”)
5. What must we **not** do? (strict don’t-wants — say “none” if nothing)
6. Anything else?
```

Do **not** ask implementation or step-by-step code here. Do **not** use `Reply like: 1a 2b`.

### 3. Analyze (required)

Run **`/analyze`** on the grilled brief (read [../analyze/SKILL.md](../analyze/SKILL.md) and follow it). Carry forward `.agents/temp/analyses/<id>/ANALYSIS.md`. Skip analyze’s goal-promote hand-off (ticket write is the path).

Waiting-on-subagents rules live in `/analyze` — do not sleep/poll for Tasks from this skill.

### 4. Propose solution

**Feature:** announce in **Locked (correct if wrong)** (asking.md announce pattern) — principle-level only:

```markdown
## Locked (correct if wrong)
**Vision:** …
**Definition of Done (outline):** …
**Entrypoints:** `path` — `symbol` · …
**Proposed architecture:** … (where it lives / reuse vs new service / deep modules)
**Non-goals:** … | _none_
```

**Refactor:** Locked announce including Pros, Cons, and Impact:

```markdown
## Locked (correct if wrong)
**Why:** …
**What must not change:** …
**Pros:** …
**Cons:** … (real costs — not empty)
**Impact:**
- **LoC** — affected: … · deleted: … · improved: … (notes)
- **Performance** — roundtrips: … · time: … · compute: … (notes)
- **Architecture** — structural: … · complexity: … · overhead: … (notes)
**Definition of Done (outline):** …
**Entrypoints:** `path` — `symbol` · …
**Proposed architecture:** … (target shape / move / delete old path)
**Non-goals:** … | _none_
```

No implementation Q&A. User corrects if needed; silence = accept. Then draft.

**Bug:** do **not** put architecture / DoD / entrypoints / Pros/Cons / Impact on the ticket. Optionally note in chat where analyze suggests looking; fold useful bits into **Notes** only.

### 5. Draft + metadata (required before any write)

Show the full proposed ticket body (template for the locked type). Then lettered Questions for write + tracker metadata:

```markdown
## Questions
Reply like: 1a 2a 3c 4a

1. Draft ready for `<ID or NEW>`. Write this to Linear/GitHub?
   - a) yes ← recommended
   - b) no — say what to edit
2. Status?
   - a) <tracker’s backlog / todo / triage state> ← recommended for create
   - b) <in progress / started>
   - c) Keep current ← recommended when refining and status is fine
   - d) Other — say which state
3. Priority?
   - a) No priority / unset
   - b) Low
   - c) Medium ← recommended unless urgency is clear
   - d) High
   - e) Urgent
   - f) Keep current ← when refining
4. Assignee?
   - a) Unassigned ← recommended unless someone owns it
   - b) <me / current user if known>
   - c) <teammate from tracker roster>
   - d) Keep current ← when refining
   - e) Other — say who
```

**Discover real options** from the tracker before asking:

| Field | Linear | GitHub |
| --- | --- | --- |
| Status | Team workflow states via MCP | Usually leave **open** on create; project/status only if the repo uses them |
| Priority | Native priority enum | Labels (`P0`/`P1`/…) or unset if none |
| Assignee | Team members via MCP | `gh` collaborators / org members; never invent emails |

Letter options must use **real** tracker values. **Wait.** No silent writes.

### 6. Write

On write = yes only. Apply **body + type + status + priority + assignee**:

| Tracker | Action |
| --- | --- |
| **Linear** (refine) | MCP update — description/body, type/label, state, priority, assignee |
| **Linear** (create) | MCP create — title + body + type + state + priority + assignee; return ID/URL |
| **GitHub** (refine) | `gh issue edit` body + labels (feature/bug/refactor) + assignees; priority label if used |
| **GitHub** (create) | `gh issue create` with title, body, label(s), assignee(s) |

Prefer a temp body file. Confirm with the issue URL and echo type / status / priority / assignee.

## Ticket body templates

### Feature

```markdown
## Type
Feature

## Ask / Vision
<plain-language goal>

## Definition of Done
- Expected: …
- [ ] …
- [ ] … (general lines — still checkable)

## Entrypoints
- `path/to/file` — `functionOrSymbol` — why this is the start
- `path/or/route` — `symbol` — …

## Proposed architecture
- … (e.g. place in `utils.ts` / create a service / compose these deep modules)
- Why: …

## Non-goals
- … (strict don’t-wants only — omit this heading if none)

## Notes
- …
```

### Bug

```markdown
## Type
Bug

## Who
…

## What
…

## When
…

## Why
… (omit this heading if unknown)

## How
1. …
2. …

## Stack trace
```
…paste…
```
(omit this heading if none)

## What should happen if it worked
…

## Notes
- …
```

### Refactor

```markdown
## Type
Refactor

## Ask / Why
<plain-language why the shape must change>

## What must not change
- …

## Pros
- …

## Cons
- … (real costs / risks — required)

## Impact

### Lines of code
- **Affected:** … — note: …
- **Deleted:** … — note: …
- **Improved:** … — note: …

### Performance
- **Roundtrips:** … — note: …
- **Time:** … — note: …
- **Compute:** … — note: …

### Architecture
- **Structural change:** … — note: …
- **Complexity:** … — note: …
- **Overhead:** … — note: …

## Definition of Done
- Structural: …
- Behavior still holds: …
- [ ] …
- [ ] …

## Entrypoints
- `path/to/file` — `functionOrSymbol` — why this is in the lane
- …

## Proposed architecture
- … (target shape / move into service / compose modules / delete old path)
- Why: …

## Non-goals
- … (strict don’t-wants only — omit this heading if none)

## Notes
- …
```

Preserve useful existing ticket content when refining. Keep required section headings exact so `/goal` / `/trackers` can find them.

## Failures

| Problem | Action |
| --- | --- |
| No Linear MCP | Point to `https://mcp.linear.app/mcp`; do not fake the ticket |
| No `gh` / not logged in | Ask install/auth, or paste body once (refine only) |
| Ticket not found | Stop; confirm ID / team / repo |
| User declines write | Leave draft in chat; do not write |
| Missing required section after grill | Keep open-grilling — never write incomplete |
| Analyze skipped | Do not draft from ticket text alone — run `/analyze` first |
| Cannot list states / members | Ask freeform under that number; still do not invent IDs |

## Anti-patterns

- Invoking this under `/goal` or as a flow twin
- Running `/analyze` before the open vision/bug/refactor grill
- Lettered `a)/b)` choices on the vision/bug/refactor open grill
- Grilling implementation detail (signatures, algorithms, step-by-step code) — that is `/goal`
- Shipping a **Constraints** section
- Feature DoD that is jargon-only with no expected outcomes
- Inventing filler Non-goals when the user said none
- Putting DoD / Entrypoints / Proposed architecture / Pros/Cons / Impact on a **Bug** ticket
- Omitting **Cons** or **Impact** on a Refactor, inventing fake Pros, or shipping Impact without notes / confidence
- Turning a Refactor into a Feature dump or a Bug who/what/when report
- Drafting without locking Feature vs Bug vs Refactor
- Using the wrong template for the locked type
- Writing before draft + metadata approval
- Skipping status / priority / assignee questions
- Inventing workflow states, priorities, or assignees not present in the tracker
- Using `/trackers` to write (read-only)
- Implementing the feature/fix/refactor in this skill

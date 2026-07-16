---
name: write-ticket
description: >-
  Standalone only — never used in /goal or any *-flow. Reads a Linear/GitHub
  ticket (or creates from a rough idea), crunches repo research via Task
  subagents, grills until Expected behavior, Definition of Done, Entrypoints,
  and Proposed architecture/interface are solid, then writes back after draft
  approval. Use when refining or writing a tracker ticket before work starts.
  Not for /goal, /grill-me-flow, or /trackers-flow.
---

# Write Ticket

**Standalone only.** Never call from `/goal`, never ship a `write-ticket-flow`. This skill **writes** to Linear/GitHub — unlike `/trackers-flow` (read-only).

Refine an existing ticket **or** create one from a rough idea. **Crunch research first** (parallel Task `explore` + analysis), then grill until the ticket is implementable, then **draft → user yes → write**.

This skill front-loads discovery so `/goal` / implementers inherit a sharp brief — not a vague wish. Do the analysis here; do **not** leave research for later.

**Subagent model:** when launching Task workers, **omit `model`** so workers inherit this chat’s parent model. Never hard-code a model unless the user asked for one.

### Waiting on subagents (hard rule)

Research **blocks on Task completion** — never invent a clock.

| Do | Do not |
| --- | --- |
| Launch explore Tasks and **wait for their Task results** (prefer `run_in_background: false` so this turn blocks until they return) | `AwaitShell` / `sleep` / “timeout 2 minutes” / polling loops while Tasks run |
| Launch **parallel** explores in **one** message, then synthesize when **all** results are back | Guess a wait duration (“subagents usually take 2 min”) |
| If a Task was backgrounded: **end the turn** and resume on the completion notification — or do other non-blocking work (read `/taste-flow`) | Vacuous `AwaitShell` with `block_until_ms: 120000` (or any fixed sleep) “to wait for subagents” |

Fixed sleeps leave the user hanging after workers already finished. **Forbidden.**

## Required ticket sections

Every finished ticket **must** include all four (hard gate before write):

| Section | Must answer |
| --- | --- |
| **Expected behavior** | What happens when done — user-visible or system-visible outcomes |
| **Definition of Done** | Binary, checkable items (pass/fail). No vibes |
| **Entrypoints** | Concrete files / modules / routes where the feature or edit starts (paths the implementer opens first) |
| **Proposed architecture / interface** | Non-concrete shape: entry kind, key signatures / hook surface, responsibilities — **not** the implementation |

Optional but preferred: Ask (problem), Non-goals, Constraints, Out of scope, Research notes (short).

### What “Proposed architecture / interface” means

Sketch the **contract**, not the body:

| Include | Exclude |
| --- | --- |
| Entry shape bias (hook / class / facade / narrow function) grounded in repo siblings + `/taste-flow` / `/architecture` | Full algorithm or step-by-step impl |
| Proposed names + signatures the caller will use (e.g. `useCheckout(): …`, `chargeInvoice(id): Promise<…>`) | Method bodies, pseudo-code dumps |
| What the surface **owns** vs what stays behind it | New file trees unless folder placement is a locked decision |
| Testability note (e.g. “hook returns X so UI can assert without mounting the whole page”) | Test file contents |

Example grain (good): “Reusable `useInvoiceStatus(invoiceId)` — loads status, exposes `{ status, error, retry }`; pure `formatInvoiceStatus(status)` for display.”  
Example grain (bad): “Implement useEffect that fetches… then setState…”

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

**Existing:** discover MCP tools (`linear|github`), prefer **read** first (`get_issue`, …). Else `gh issue view … --json …`. Normalize into a brief (title, ask, what’s already there). Do **not** invent the body.

**Create:** no fetch. Seed from the user’s idea only — research is step 2.

If Linear MCP needs auth → `mcp_auth` once, rediscover. If `gh` missing/unauth → say so; allow paste-once fallback for refine, or stop for create.

### 2. Research crunch (required — do most analysis here)

Before gap check or grill, **exhaust discovery**. You orchestrate; Task workers dig. Prefer **parallel** `explore` Tasks in one message, **`run_in_background: false`**, then synthesize as soon as results return. **Omit `model`.** Thoroughness: `medium` default; `very thorough` when multi-domain.

**Do not** sleep, timeout, or `AwaitShell`-wait for Task subagents — see **Waiting on subagents** above.

| Wave | What to find |
| --- | --- |
| **Entrypoints** | Files, routes, hooks, Convex functions, components where this change would start |
| **Sibling patterns** | How similar features are shaped (folders, naming, error style, entry kind) |
| **Touch surface** | Likely edit/create paths, existing tests, what must not sprawl |
| **Constraints from code** | APIs, schema, auth, feature flags that bound the ask |
| **Interface candidates** | Existing hooks/facades/functions to extend vs new surface; copy their grain |

Also read **`/taste-flow`** (and `/architecture` when structure/data is in play) so recommendations match pack doctrine — do not invent style.

**Synthesize** (you, after workers return) into a short research memo used for grill recommendations:

1. Current behavior (what code does today)
2. Likely entrypoints (paths + why)
3. 1–2 architecture options (e.g. reusable testable hook vs narrow pure functions vs facade) with a **recommended** default
4. Draft interface sketch (names + signatures + responsibilities only)
5. Risks / unknowns that still need the user

If explore returns nothing useful (greenfield), say so once; mark recommendations as guesses.

Do **not** ask the user for paths, sibling patterns, or “where does X live” when research can answer. Front-load that into the memo and into recommended grill answers.

### 3. Gap check

Against the **four** required sections, using the ticket brief **plus** the research memo. Mark each: present / weak / missing.

### 4. Grill (same style as `/grill-me`)

1. One question at a time. Wait.
2. Recommended answer first (one-word accept) — grounded in the research memo.
3. Walk gaps in order: **Expected behavior** → **Definition of Done** → **Entrypoints** → **Proposed architecture / interface** → then non-goals / constraints if still fuzzy.
4. On architecture / interface, ask explicitly when still open — e.g. reusable testable hook vs known function signature vs class/facade — with your recommended option first. Lock the **surface** (name, inputs/outputs, responsibilities), not the impl.
5. Decisions are the user’s.
6. Do **not** implement code, write `plans/*`, or start `/goal`.

Stop grilling when all four required sections are solid, Done items are binary, and the interface sketch has no implementation leakage.

### 5. Draft (required before any write)

Show the full proposed ticket body using the template below. Explicit ask:

> Draft ready for `<ID or NEW>`. Write this to Linear/GitHub?

**Wait for yes.** No silent writes. Edits → revise draft → ask again.

### 6. Write

On yes only:

| Tracker | Action |
| --- | --- |
| **Linear** (refine) | MCP update tool from live schema (`save_issue` / `update_issue` / equiv.) — set description/body to the draft |
| **Linear** (create) | MCP create tool — title + body from draft; return ID/URL |
| **GitHub** (refine) | `gh issue edit <N> --body-file …` (or MCP update if present) |
| **GitHub** (create) | `gh issue create --title … --body-file …` (or MCP create) |

Prefer writing via a temp body file so markdown survives. Confirm with the issue URL when done.

Do **not** change status, assign, close, or spam comments unless the user asked.

## Ticket body template

```markdown
## Ask
<what / why, user perspective>

## Expected behavior
- …
- …

## Definition of Done
- [ ] …
- [ ] …

## Entrypoints
- `path/to/file` — why this is the start
- `path/or/route` — …

## Proposed architecture / interface
**Shape:** <hook | class | facade | function(s)> — why (sibling / taste)
**Surface:**
- `useThing(args): { … }` — owns …
- `helperName(input): Output` — pure / boundary; owns …
**Behind the surface:** <what stays private — one line>
**Not in scope of this sketch:** implementation details

## Non-goals
- …

## Constraints
- …

## Research notes
- <optional: 2–5 bullets from the crunch — siblings cited, risks>
```

Preserve useful existing ticket content; merge rather than wipe when refining. Keep required sections under those exact headings so later `/goal` / `/trackers-flow` can find them.

## Failures

| Problem | Action |
| --- | --- |
| No Linear MCP | Point to `https://mcp.linear.app/mcp`; do not fake the ticket |
| No `gh` / not logged in | Ask install/auth, or paste body once (refine only) |
| Ticket not found | Stop; confirm ID / team / repo |
| User declines write | Leave draft in chat; do not write |
| Missing required section after grill | Keep grilling — never write incomplete |

## Anti-patterns

- Invoking this under `/goal` or as a flow twin
- Skipping research and grilling from the ticket text alone
- Solo deep-diving the whole repo when parallel `explore` Tasks should do the labor
- Sleeping / fixed timeouts / `AwaitShell` polling while waiting for Task subagents
- Leaving architecture / interface vague (“clean up the module”) with no surface
- Writing implementation into the ticket (bodies, algorithms, “then call setState…”)
- Writing before draft approval
- Shipping without Expected behavior, Definition of Done, Entrypoints, or Proposed architecture / interface
- Vague Done (“works well”, “feels right”)
- Entrypoints as “the backend” with no paths
- Using `/trackers-flow` to write (it is read-only)
- Implementing the feature in this skill

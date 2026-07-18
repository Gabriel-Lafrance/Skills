---
name: write-ticket
description: >-
  Standalone only — never used in /goal or any *-flow. Loads or seeds a
  Linear/GitHub ticket, runs /analyze for research, grills until Expected
  behavior, Definition of Done, Entrypoints, and Proposed architecture/interface
  are solid, then writes after draft approval. Use when refining or writing a
  tracker ticket. For analysis without a ticket use /analyze.
---

# Write Ticket

**Standalone only.** Never call from `/goal`, never ship a `write-ticket-flow`. This skill **writes** to Linear/GitHub — unlike `/trackers-flow` (read-only) and `/analyze` (research only).

Refine an existing ticket **or** create one from a rough idea. **Research via `/analyze`**, then grill until the ticket is implementable, then **draft → user yes → write**.

**Ask style:** [../asking.md](../asking.md). **Subagent model:** omit Task `model` unless the user asked for one (workers launched by `/analyze`).

## Required ticket sections

Every finished ticket **must** include all four (hard gate before write):

| Section | Must answer |
| --- | --- |
| **Expected behavior** | What happens when done — user-visible or system-visible outcomes |
| **Definition of Done** | Binary, checkable items (pass/fail). No vibes |
| **Entrypoints** | Concrete files / modules / routes where the feature or edit starts |
| **Proposed architecture / interface** | Contract: entry kind, signatures, responsibilities — **not** the implementation |

Optional but preferred: Ask, Non-goals, Constraints, Out of scope, Research notes (from `/analyze` memo).

### Proposed architecture / interface grain

| Include | Exclude |
| --- | --- |
| Entry shape + names/signatures callers use | Method bodies, algorithms |
| What the surface owns vs keeps behind it | Full file trees unless placement is locked |
| Testability note when useful | Test file contents |

Good: “Reusable `useInvoiceStatus(invoiceId)` → `{ status, error, retry }`.”  
Bad: “Implement useEffect that fetches… then setState…”

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

**Existing:** discover MCP tools (`linear|github`), prefer **read** first. Else `gh issue view … --json …`. Normalize into a brief. Do **not** invent the body.

**Create:** no fetch. Seed from the user’s idea only.

If Linear MCP needs auth → `mcp_auth` once. If `gh` missing/unauth → say so; allow paste-once fallback for refine, or stop for create.

### 2. Analyze (required)

Run **`/analyze`** on the seeded brief (read [../analyze/SKILL.md](../analyze/SKILL.md) and follow it). Carry forward the on-disk memo at `.agents/temp/analyses/<id>/ANALYSIS.md` — do not re-explore from scratch here. Skip analyze’s goal-promote hand-off when already inside write-ticket (ticket write is the path); sharpen/Questions from analyze are fine.

Waiting-on-subagents rules live in `/analyze` — do not sleep/poll for Tasks from this skill.

### 3. Gap check

Against the **four** required sections, using the ticket brief **plus** the analyze memo. Mark each: present / weak / missing.

### 4. Grill

1. **Batch** all known gap questions ([../asking.md](../asking.md)).
2. Recommended options grounded in the analyze memo (and asking.md defaults).
3. Cover gaps: **Expected behavior** → **Definition of Done** → **Entrypoints** → **Proposed architecture / interface** → non-goals / constraints if still fuzzy.
4. Lock the **surface**, not the impl.
5. Do **not** implement code, write `plans/*`, or start `/goal`.

Stop when all four sections are solid and Done items are binary.

### 5. Draft (required before any write)

Show the full proposed ticket body (template below). Approve via asking.md batch:

```markdown
## Questions
Reply like: `1a`

1. Draft ready for `<ID or NEW>`. Write this to Linear/GitHub?
   - a) yes ← recommended
   - b) no — say what to edit
```

**Wait for the batch.** No silent writes.

### 6. Write

On yes only:

| Tracker | Action |
| --- | --- |
| **Linear** (refine) | MCP update — description/body = draft |
| **Linear** (create) | MCP create — title + body; return ID/URL |
| **GitHub** (refine) | `gh issue edit <N> --body-file …` |
| **GitHub** (create) | `gh issue create --title … --body-file …` |

Prefer a temp body file. Confirm with the issue URL. Do **not** change status, assign, or close unless asked.

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
**Shape:** <hook | class | facade | service | function(s)> — why (sibling / taste)
**Surface:**
- `useThing(args): { … }` — owns …
- `helperName(input): Output` — owns …
**Behind the surface:** <one line>
**Not in scope of this sketch:** implementation details

## Non-goals
- …

## Constraints
- …

## Research notes
- <2–5 bullets from /analyze memo — siblings cited, risks>
```

Preserve useful existing ticket content when refining. Keep required section headings exact so `/goal` / `/trackers-flow` can find them.

## Failures

| Problem | Action |
| --- | --- |
| No Linear MCP | Point to `https://mcp.linear.app/mcp`; do not fake the ticket |
| No `gh` / not logged in | Ask install/auth, or paste body once (refine only) |
| Ticket not found | Stop; confirm ID / team / repo |
| User declines write | Leave draft in chat; do not write |
| Missing required section after grill | Keep grilling — never write incomplete |
| Analyze skipped | Do not draft from ticket text alone — run `/analyze` first |

## Anti-patterns

- Invoking this under `/goal` or as a flow twin
- Skipping `/analyze` and grilling from the ticket text alone
- Re-doing a full explore when `/analyze` just returned a memo
- Leaving architecture / interface vague (“clean up the module”)
- Writing implementation into the ticket
- Writing before draft approval
- Shipping without the four required sections
- Using `/trackers-flow` to write (read-only)
- Implementing the feature in this skill

---
name: write-ticket
description: >-
  Standalone only — never used in /goal or any *-flow. Reads a Linear/GitHub
  ticket (or creates from a rough idea), explores the repo via Task subagents
  for implementation knowledge, grills until Definition of Done, entrypoints,
  and expected behavior are solid, then writes back after draft approval. Use
  when refining or writing a tracker ticket before work starts. Not for /goal,
  /grill-me-flow, or /trackers-flow.
---

# Write Ticket

**Standalone only.** Never call from `/goal`, never ship a `write-ticket-flow`. This skill **writes** to Linear/GitHub — unlike `/trackers-flow` (read-only).

Refine an existing ticket **or** create one from a rough idea. **Explore first** (Task `explore` subagents), then grill until the ticket body is implementable, then **draft → user yes → write**.

**Subagent model:** when launching Task workers, **omit `model`** so workers inherit this chat’s parent model. Never hard-code a model unless the user asked for one.

## Required ticket sections

Every finished ticket **must** include all three (hard gate before write):

| Section | Must answer |
| --- | --- |
| **Expected behavior** | What happens when done — user-visible or system-visible outcomes |
| **Definition of Done** | Binary, checkable items (pass/fail). No vibes |
| **Entrypoints** | Concrete files / modules / routes where the feature or edit starts (paths the implementer opens first) |

Optional but preferred: Ask (problem), Non-goals, Constraints, Out of scope.

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

**Create:** no fetch. Seed from the user’s idea only — do **not** solo-walk the repo here; that is step 2.

If Linear MCP needs auth → `mcp_auth` once, rediscover. If `gh` missing/unauth → say so; allow paste-once fallback for refine, or stop for create.

### 2. Explore first (required)

Before gap check or grill, launch **Cursor Task** subagents (`subagent_type: "explore"`) to gather implementation knowledge. You orchestrate; they dig. Prefer **parallel** Tasks in one message when lanes are independent.

**Omit `model`.** Thoroughness: `medium` default; `very thorough` when the ticket spans multiple domains.

| Wave | What to find |
| --- | --- |
| **Entrypoints** | Concrete files, routes, hooks, Convex functions, components where this change would start |
| **Sibling patterns** | How similar features are shaped in this repo (folders, naming, error style) |
| **Touch surface** | Likely edit/create paths, tests, and what must not sprawl |
| **Constraints from code** | Existing APIs, schema, auth, feature flags that bound the ask |

Prompt each explore worker with the ticket brief / idea + a sharp question. Ask them to return: paths (with why), short notes on current behavior, and open risks — not a full plan.

If explore returns nothing useful (greenfield / empty repo), say so once and continue with grill recommendations marked as guesses.

Do **not** ask the user for paths or “where does X live” when explore can answer. Fold explore findings into recommended answers in the grill.

### 3. Gap check

Against the three required sections, using the ticket brief **plus** explore reports. Mark each: present / weak / missing.

### 4. Grill (same style as `/grill-me`)

1. One question at a time. Wait.
2. Recommended answer first (one-word accept) — prefer answers grounded in explore findings.
3. Walk gaps in order: **Expected behavior** → **Definition of Done** → **Entrypoints** → then non-goals / constraints if still fuzzy.
4. Decisions are the user’s.
5. Do **not** implement code, write `plans/*`, or start `/goal`.

Stop grilling when all three required sections are solid and binary Done items are checkable.

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

## Non-goals
- …

## Constraints
- …
```

Preserve useful existing ticket content; merge rather than wipe when refining. Keep Required sections under those exact headings so later `/goal` / `/trackers-flow` can find them.

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
- Skipping explore and grilling from the ticket text alone
- Solo deep-diving the whole repo when parallel `explore` Tasks should do the labor
- Writing before draft approval
- Shipping a ticket without Definition of Done, Entrypoints, or Expected behavior
- Vague Done (“works well”, “feels right”)
- Entrypoints as “the backend” with no paths
- Using `/trackers-flow` to write (it is read-only)
- Implementing the feature in this skill

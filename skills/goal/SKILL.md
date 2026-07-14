---
name: goal
description: >-
  Keep working toward one verifiable completion condition in Cursor. Shapes the
  goal from chat or a Linear/GitHub ticket (e.g. /goal IN-1234, /goal #42), then
  drives grill-me → architecture → create-plan → implement → validate (and
  split-task / review as needed) until evidence proves done and the ticket can
  close. Use when the user says /goal, passes a ticket ID, set a goal, keep
  going until, or wants autonomous progress toward a measurable end state.
disable-model-invocation: true
---

# Goal (Cursor)

Claude Code's `/goal` sets a completion condition and keeps turning until a small evaluator says yes. Cursor has no native goal loop — this skill **is** that loop, wired through this pack so output stays planned, validated, and reviewable.

One goal per session. Replace an active goal by stating a new one. Clear with `/goal clear` (aliases: stop, off, cancel).

## Ticket-driven goals

If the user passes a tracker ID or URL — `/goal IN-1234`, `/goal #42`, `/goal owner/repo#42`, or a Linear/GitHub issue link — **resolve that ticket** is the goal.

1. Run **`/trackers`** fetch immediately (Linear MCP or `gh`). Do not shape the contract from the ID alone.
2. Build the goal contract from the ticket brief (title → Goal, acceptance → Done when).
3. Keep **Ticket:** `ID` + URL in the contract Context.
4. On ACHIEVED, run **`/trackers`** close-out (comment + Done / `gh issue close`) after validate evidence exists.

If fetch fails, stop and fix auth/tools — do not proceed on a guessed spec.

## Suitability gate

**Hard reject** (ask to rephrase; do not start):

- Vague wishes with no observable evidence ("make it better")
- Open-ended research with no done state
- Multiple unrelated objectives in one goal (multiple ticket IDs only if the user says they are one unit of work)

**Warn then proceed** if the user insists:

- Subjective quality ("clean code") — force binary checks into Done when

Tickets with empty acceptance criteria: derive Done when from the Ask, show them, get a quick yes before Phase 1.

## Phase 0 — Shape the goal

If ticket-driven, start from the `/trackers` brief. If the user already gave a tight condition, normalize it. Otherwise ask **one** clarifying question at a time only for decisions you cannot look up.

Write and keep this contract visible (update if the user revises):

```markdown
# Goal
<one-line verifiable outcome>

# Ticket
<none | IN-1234 (Linear) | #42 (GitHub) — URL>

# Lane
<files, packages, apps, or area>

# Context
- First reads: <paths, plan, ticket brief, CONTEXT.md if present>
- Facts the agent cannot invent: <IDs, constraints>

# Constraints
- Hard rules
- Out of scope

# Done when
1. <binary check — prefer a command + exit code or transcript-visible artifact>
2. <binary check>
3. …
4. <if Ticket set: tracker close-out completed — comment + Done/closed>

# On block
After 3 failed attempts on the same check: stop, report root cause, ask for a decision.
Stop after <N> checkpoints if still incomplete (default 12) unless the user set another bound.
```

Rules for Done when:

- Judgeable from what this session surfaces (running server/Convex output, files, plan todos)
- Prefer observable checks: “Convex push succeeded / no error in convex dev”, “UI shows X on localhost” — not ritual `npm run lint`
- Point long specs at the ticket URL / a file instead of pasting them into the goal
- Ticket acceptance checklist rows become Done when rows when present
- Do **not** require lint/typecheck Done when rows unless the user asked — CI owns those

Show the contract. If anything critical is `TODO`, ask once. Do not invent paths.

## Phase 1 — Drive with this pack

Execute toward Done when. Do not wait for a new user prompt between checkpoints unless On block fires or the plan needs confirmation.

### Checkpoint loop

At each checkpoint:

1. **Ambiguous intent?** → run `/grill-me` (one question at a time) until shared understanding, then continue.
2. **Multi-file / extraction / UI state?** → read `/taste`, run `/architecture`, lock the structure card. If the change is user-facing UI, also run **`/design`** Mode B (Design card).
3. **Non-trivial and no approved plan?** → run `/create-plan` (Plan mode + CreatePlan), including Structure + taste-fit + Design card when UI; Spec source = ticket brief when Ticket is set. **Stop and wait** for user confirmation before any Agent edits.
4. **Too big for one window?** → `/split-task`, then work the frontier with `/implement` (fresh chat per piece when the user starts one; in-session, finish the current frontier piece only). Keep the same Ticket ID on every child piece.
5. **Approved plan or ready piece?** → `/implement` in Agent mode (`/taste` + `/design` when UI + folders before files; complexity behind the entry point).
6. **After implementation slices** → `/validate` against Done when (plan / ticket AC + taste self-check).
7. **Validate passes** → `/code-review` (Standards from `/taste` + Spec + structure; Spec = ticket when set). Fix must-fix findings, then `/validate` again.
8. **Re-evaluate Done when** from transcript evidence only. If unmet, start the next checkpoint with the latest failure reason as the directive.

### Cursor-specific rules

- CreatePlan confirmation is the **gate in**; `/validate` is the **gate out**
- Never claim the goal achieved without a `/validate` evidence table for every Done when row
- Prefer Task `explore` for unfamiliar code; use `bugbot` / `security-review` only if the user asked or the goal names security
- Surface evidence in the transcript after every checkpoint (server/Convex logs + results — not lint spam)
- Do not start a parallel second goal

### Status

When the user runs `/goal` with no new condition (or asks for status), report:

- Active condition (Goal + Ticket + Done when)
- Checkpoints completed / bound
- Latest validate summary
- Whether waiting on plan confirmation or On block

## Phase 2 — Achieve or clear

**Achieved:** all Done when rows pass with evidence → if Ticket is set, `/trackers` close-out → state ACHIEVED, one-line summary + ticket URL, stop autonomous looping.

**Cleared by user:** acknowledge, stop looping, leave the tree and ticket as-is unless they ask to revert or reopen.

## Anti-patterns

- Freeform coding past the plan gate
- "Looks done" without command/file evidence
- Merging multiple goals into one session
- Skipping `/validate` because “the build looked fine”
- Ritual lint/typecheck instead of reading running localhost + Convex output
- Re-asking facts that are already in the repo or ticket
- Closing Linear/GitHub before validate evidence exists
- Shaping a ticket goal without a successful `/trackers` fetch

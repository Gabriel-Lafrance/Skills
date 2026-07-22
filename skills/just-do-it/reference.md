# Just Do It reference (schemas & templates)

Load when writing workspace artifacts, STATUS, Progress, ORIGIN, SHIP, or review snapshots. Rules stay in [doctrine.md](doctrine.md).

## Workspace layout

```text
.agents/temp/just-do-it/
  REGISTRY.md
  <jdi-id>/                              # e.g. jdi-IN-1234
    STATUS.md
    ORIGIN.md
    PROGRESS.md
    LINKS.md

    analyses/
      REGISTRY.md
      <analysis-id>/
        ANALYSIS.md
        STATUS.md
        NOTES.md                         # optional

    goals/
      REGISTRY.md
      <build-goal-id>/
        GOAL.md
        STATUS.md
        GRILL.md
        plans/
          INDEX.md
          01-<slug>.md
        pieces/                          # optional
      fix-cr1-01-<slug>/
      fix-cr2-01-<slug>/
      achieved/
        <goal-id>/

    reviews/
      cr1/
        PASS-01.md
        PASS-02.md
      cr2/
        PASS-01.md

    FINDINGS.md
    SHIP.md
```

Base path **`.agents/temp/just-do-it/`** — never `.scratch/`. Shared grill themes remain under `.agents/temp/grills/`.

### jdi-id

1. Ticket → `jdi-IN-1234` or `jdi-ENG-99`
2. Override → `/just-do-it id:my-id IN-1234`
3. If dir exists and status is `running`/`blocked`, allocate a **new** id (suffix) — never overwrite another run

### Pack REGISTRY.md

`.agents/temp/just-do-it/REGISTRY.md`:

| id | status | ticket | type | branch | pr | title | workspace | updated |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

Statuses: `running` | `blocked` | `done` | `cleared`

### Nested analyses REGISTRY.md

| id | status | ticket | title | workspace | updated |
| --- | --- | --- | --- | --- | --- |

### Nested goals REGISTRY.md

| id | kind | status | ticket | title | workspace | updated |
| --- | --- | --- | --- | --- | --- | --- |

`kind`: `build` | `fix-cr1` | `fix-cr2`

On goal ACHIEVED: `mv` active goal dir → `goals/achieved/<goal-id>/`; set nested registry `workspace: achieved/<goal-id>`, `status: achieved`.

## STATUS.md

```markdown
# Status
**id:** jdi-IN-1234
**phase:** resolve | branch | analyze | goal | code-review-1-loop | code-review-2 | code-review-2-loop | ship | done | blocked
**last:** <one line>
**ticket:** IN-1234
**type:** feature | bug | refactor
**branch:** bug/IN-1234-fix-checkout
**base:** main
**pr_url:**
**cr1_loops:** 0
**cr2_loops:** 0
**blocked_on:** none | user | auth | git | review-cap | …
**resume_at:** <phase or step>
**updated:** <ISO>
```

## ORIGIN.md

```markdown
# Origin
**jdi-id:** jdi-IN-1234
**started_at:** <ISO>
**ticket:** IN-1234
**ticket_url:** https://linear.app/…
**type:** bug
**title:** <ticket title>
**repo:** <origin remote>
**base:** main
**initial_ask:** <one line from ticket / user>
```

## PROGRESS.md

Append-only:

```markdown
# Progress

- <ISO> · resolve · workspace created
- <ISO> · branch · `bug/IN-1234-fix-checkout`
- <ISO> · analyze · `analyses/an-IN-1234` ready → promote
- <ISO> · goal · build `IN-1234` ACHIEVED
- <ISO> · code-review-1-loop · pass 1 → fix-cr1-01-auth-check
- <ISO> · code-review-2 · clear
- <ISO> · ship · PR https://github.com/…/pull/N
```

## LINKS.md

```markdown
# Links
**ticket:** …
**analysis:** `.agents/temp/just-do-it/jdi-IN-1234/analyses/an-IN-1234/`
**build_goal:** `.agents/temp/just-do-it/jdi-IN-1234/goals/achieved/IN-1234/`
**fix_goals:**
- `goals/achieved/fix-cr1-01-…`
**branch:** `bug/IN-1234-…`
**pr:**
```

## FINDINGS.md

Current critical/important burn-down:

```markdown
# Findings backlog
**phase:** code-review-2
**pass:** 1

## Critical
- [ ] `path` — title — from PASS-01

## Important
- [x] `path` — title — fixed via `fix-cr2-01-…`

## Nits (do not block loop)
- …
```

## Review PASS template

`reviews/cr1/PASS-01.md` or `reviews/cr2/PASS-01.md`:

```markdown
# Review pass
**axis:** cr1 | cr2
**pass:** 01
**variant:** flow | standalone
**base:** main
**updated:** <ISO>

## Critical
- …

## Important
- …

## Nits
- …

## Disposition
- fix via goal: `fix-cr1-01-slug` | clear | blocked-at-cap
```

## Fix-goal seed (GOAL.md outline)

```markdown
# Goal
Fix critical/important review findings for IN-1234 (no scope expansion).

# Lane
Only paths/symbols named in FINDINGS.md / this Done when list.

# Done when
1. Finding: `<title>` at `path` — fixed
2. …

# Constraints
- Same ticket IN-1234
- Smallest behavior-preserving fix
- No new features; no unrelated cleanup; no full refactor

# Context
- Parent: `.agents/temp/just-do-it/jdi-IN-1234/`
- Build goal: …
- Review pass: `reviews/crN/PASS-NN.md`
- Ticket: …
```

## SHIP.md

```markdown
# Ship
**jdi-id:** jdi-IN-1234
**ticket:** IN-1234
**type:** bug
**branch:** bug/IN-1234-…
**base:** main
**commits:**
- abc1234 — …
**pr_url:** https://github.com/…/pull/N
**pr_title:** [IN-1234] …
**human_next:** Run `/pr-review` or review on GitHub — agent does not own PR review.
```

## Progress (chat)

```markdown
**Progress:** `jdi-IN-1234` · code-review-2-loop · cr1_loops 1 · cr2_loops 1 · next: ship
```

## ACHIEVED hand-off from build goal

After build `/goal` ACHIEVED summary: **do not** ask Ship Questions. Set just-do-it `resume_at: code-review-2` and continue.

## Clear

`/just-do-it clear [id]`:

1. Pack REGISTRY → `cleared`
2. Delete `.agents/temp/just-do-it/<id>/` (active run only)

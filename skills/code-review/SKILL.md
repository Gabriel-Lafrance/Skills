---
name: code-review
description: >-
  Three-axis review (Standards + Spec + Routes) of a git diff since a fixed
  point the user names (default main/master). After findings, offers a batched Questions ask to fix; on yes starts /goal
  (grill → plans → implement) to clear the backlog.
  Standards = taste-flow + architecture examples + thermonuclear
  maintainability. Routes = out-loud top-down codepath walk. Agents may
  auto-invoke. Use for branch/PR review outside /goal. Under /goal use
  /code-review-flow.
---

# Code Review

**Standalone** review of whatever the user asked to review — typically `main...HEAD` (or another fixed point they name). Not the goal-loop reviewer; that is **`/code-review-flow`**.

**Read:** [doctrine.md](doctrine.md)

## Process

1. **Pin fixed point** — `git diff <fixed-point>...HEAD` (doctrine)
2. **Resolve spec source** — user paste, PR/issue, commits, or ask
3. **Launch parallel Tasks** — Standards + Spec + Routes (doctrine prompts)
4. **Aggregate** — separate `## Standards`, `## Spec`, `## Routes`
5. **Needs /create-test** — recommend to user; do not run (doctrine §10)
6. **Offer to fix** — Fix backlog + Questions batch via [../asking.md](../asking.md); on yes → `/goal` (doctrine §11)

Under `/goal` → **`/code-review-flow`**.

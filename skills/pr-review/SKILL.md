---
name: pr-review
description: >-
  Standalone only — evaluate an open GitHub Pull Request with strict
  taste/architecture/design (plus Spec and Routes), show full draft comments,
  then ask what to publish/modify/skip before posting on the PR. No em dashes.
  Never under /goal (use /code-review-flow). For local branch fix loops use
  /code-review.
---

# PR Review

**Standalone only.** Never call from `/goal`, never ship a `pr-review-flow`. Posts review comments on the **Pull Request**. Linked Linear issues are **read-only** Spec context.

**Read:** [doctrine.md](doctrine.md) · **Ask style:** [../asking.md](../asking.md) · **Axes:** [../code-review/doctrine.md](../code-review/doctrine.md)

**Subagent model:** omit Task `model` unless the user asked for one.

## Process

1. **Resolve PR** — URL, number, or `gh pr view` for current branch. Fail if none / `gh` missing.
2. **Load context (read-only)** — PR body, commits, threads. Linked Linear/GitHub issue → read for Spec only (do not write Linear).
3. **Pin base** — PR base branch; `gh pr diff` or `git diff <base>...HEAD`.
4. **Strict review** — parallel Tasks: Standards + Spec + Routes. Standards **must** load `/taste-flow`, `/architecture`, and `/design` when UI is in the diff. Pack violations are presumptive **blocking** (doctrine).
5. **Aggregate** — `## Standards`, `## Spec`, `## Routes`; name taste / architecture / design failures.
6. **Show all draft comments** — full Where / Issue / Why / Fix bodies for every candidate (doctrine). Nothing published yet. **No em dashes.**
7. **Then ask** — Questions batch: publish as blocking / non-blocking, skip, or modify (paste revised text); plus Request changes vs Comment vs Approve. Wait for `1a, 2b, …`. Apply modifications before any post.
8. **Post** — only approved comments on the **PR** via `gh` (inline when possible). Never post without that yes. Never comment on Linear.
9. **Stop** — summarize what posted. Fix loop → `/code-review` then `/goal` (do not auto-start).

## Anti-patterns

- Asking publish/skip before showing full draft bodies
- Posting before triage or with em dashes
- Softening pack doctrine failures into nits
- Writing Linear issue comments instead of PR comments
- Starting `/goal` from this skill
- Using this inside `/goal` (use `/code-review-flow`)

---
name: pr-review
description: >-
  Standalone only — evaluate an open GitHub Pull Request with strict
  taste/architecture/design (plus Spec and Routes). If prior review comments
  exist, check whether they were answered, then rescan for new issues. Show
  full draft comments, then ask what to publish/modify/skip before posting on
  the PR. No em dashes. Never under /goal (use /code-review-flow). For local
  branch fix loops use /code-review.
---

# PR Review

**Standalone only.** Never call from `/goal`, never ship a `pr-review-flow`. Posts review comments on the **Pull Request**. Linked Linear issues are **read-only** Spec context.

**Read:** [doctrine.md](doctrine.md) · **Ask style:** [../asking.md](../asking.md) · **Axes:** [../code-review/doctrine.md](../code-review/doctrine.md)

**Subagent model:** omit Task `model` unless the user asked for one.

## Process

1. **Resolve PR** — URL, number, or `gh pr view` for current branch. Fail if none / `gh` missing.
2. **Load context (read-only)** — PR body, commits, **all review threads/comments**. Linked Linear/GitHub issue → Spec only (do not write Linear).
3. **Pin base** — PR base branch; `gh pr diff` or `git diff <base>...HEAD`.
4. **Prior comments** (if any threads) — ledger: Addressed / Partial / Unanswered / Outdated / Disputed against the current diff (doctrine). Draft follow-ups for anything not fully Addressed.
5. **Fresh rescan** — parallel Tasks: Standards + Spec + Routes (always, even on follow-up). Standards **must** load `/taste-flow`, `/architecture`, and `/design` when UI is in the diff. Do not re-file issues already covered by an open prior thread.
6. **Aggregate** — Prior ledger + `## Standards`, `## Spec`, `## Routes`.
7. **Show all draft comments** — follow-ups first, then new; full Where / Issue / Why / Fix. Nothing published yet. **No em dashes.**
8. **Then ask** — publish / skip / modify per draft; optional resolve/ack for Addressed threads; Request changes vs Comment vs Approve. Wait for `1a, 2b, …`.
9. **Post** — only approved items on the **PR** (thread replies for follow-ups; inline for new). Never post without that yes. Never comment on Linear.
10. **Stop** — summarize what posted. Fix loop → `/code-review` then `/goal` (do not auto-start).

## Anti-patterns

- Skipping prior-comment check when threads already exist
- Asking publish/skip before showing full draft bodies
- Approving while prior blockers are unanswered
- Posting before triage or with em dashes
- Softening pack doctrine failures into nits
- Writing Linear issue comments instead of PR comments
- Starting `/goal` from this skill
- Using this inside `/goal` (use `/code-review-flow`)

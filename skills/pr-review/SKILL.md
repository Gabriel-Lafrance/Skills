---
name: pr-review
description: >-
  Standalone only — evaluate an open GitHub PR with strict taste/architecture/design.
  On Nth pass, triage ALL prior finding comments (not just last pass), then rescan.
  One finding per PR comment; never summary/announcement comments; never repo helper
  scripts (use gh only). Show drafts in chat before publish. No em dashes. Never under
  /goal. For local fix loops use /code-review.
---

# PR Review

**Standalone only.** Never call from `/goal`, never ship a `pr-review-flow`. Posts on the **Pull Request**. Linked Linear is **read-only** Spec.

**Read:** [doctrine.md](doctrine.md) · **Ask style:** [../asking.md](../asking.md) · **Axes:** [../code-review/doctrine.md](../code-review/doctrine.md)

**Hard:**

- **One finding = one PR comment** (never bundle)
- **No summary / announcement comments** on the PR (chat-only status)
- **No helper scripts** in the repo (`build-review.cjs`, etc.) — **`gh` / `gh api` only**
- **Nth pass:** Pass A covers **all** prior finding comments across every pass, not only the last one

**Subagent model:** omit Task `model` unless the user asked for one.

## Process

1. **Resolve PR** — URL, number, or `gh pr view`. Fail if none / `gh` missing.
2. **Load context** — body, commits, **all** inline review comments + threads (every review, every page, resolved included). Linear/GitHub issue → Spec only.
3. **Pin base** — `gh pr diff` or `git diff <base>...HEAD`.

### Pass A (if any prior finding comments exist)

4. For **each** prior finding (full history): short **"here's what's done"** + read (Addressed / Partial / Unanswered / …).
5. **Questions** — per prior: mark resolved / leave open / reply / other. Wait for `1a, 2b, …`.
6. Apply approved actions only (**one reply or resolve per thread**). **Do not** post a Pass A summary on the PR.

### Pass B (always: first review or after Pass A)

7. **Fresh rescan** — Standards + Spec + Routes. Skip issues already on an open prior finding thread.
8. **Show new drafts in chat** — **one full draft per new finding**. Nothing on the PR yet. **No em dashes.**
9. **Questions** — publish / skip / modify **per draft**; review event (Request changes / Comment / Approve). Wait.
10. **Post via `gh` only** — each approved draft as its **own** inline/API comment. Empty/minimal review body. **Never** a summary PR comment. **Never** write `build-review.cjs` (or any review helper) into the repo.
11. **Stop** — tell the user what posted **in chat**. Fix loop → `/code-review` then `/goal` (do not auto-start).

## Anti-patterns

- Summary / "posted N comments" / index comment on the PR
- `build-review.cjs` or other repo files to submit reviews
- One comment or review body containing multiple findings
- Pass A only on the latest pass
- Skipping per-prior triage; asking Pass B before Pass A is answered
- Posting before showing full drafts in chat
- Approving while prior blockers remain open
- Writing Linear comments; starting `/goal`; using inside `/goal`

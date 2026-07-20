---
name: pr-review
description: >-
  Standalone only — evaluate an open GitHub PR with strict taste/architecture/design.
  Follow-up passes: per prior comment, summarize what's done and ask resolve/reply/leave
  open; then rescan and draft new issues as one comment each. Show drafts before publish.
  No em dashes. Never under /goal. For local fix loops use /code-review.
---

# PR Review

**Standalone only.** Never call from `/goal`, never ship a `pr-review-flow`. Posts on the **Pull Request**. Linked Linear is **read-only** Spec.

**Read:** [doctrine.md](doctrine.md) · **Ask style:** [../asking.md](../asking.md) · **Axes:** [../code-review/doctrine.md](../code-review/doctrine.md)

**Hard:** **one finding = one comment**. Never bundle multiple edits into one PR comment.

**Subagent model:** omit Task `model` unless the user asked for one.

## Process

1. **Resolve PR** — URL, number, or `gh pr view`. Fail if none / `gh` missing.
2. **Load context** — body, commits, **all review threads**. Linear/GitHub issue → Spec only.
3. **Pin base** — `gh pr diff` or `git diff <base>...HEAD`.

### Pass A (if prior comments exist)

4. For **each** prior thread: short **"here's what's done"** summary + your read (Addressed / Partial / Unanswered / …).
5. **Questions batch** — per prior issue: mark resolved / leave open / reply on thread / other. Wait for `1a, 2b, …`.
6. Apply only approved Pass A actions (**one reply or resolve per thread**).

### Pass B (always: first review or after Pass A)

7. **Fresh rescan** — Standards + Spec + Routes. Skip issues already on an open prior thread.
8. **Show new drafts** — **one full draft per new finding** (Where / Issue / Why / Fix). Nothing posted yet. **No em dashes.**
9. **Questions** — publish / skip / modify **per draft**; plus Request changes vs Comment vs Approve. Wait.
10. **Post** — each approved draft as its **own** PR review comment (separate inlines). Never one mega-comment.
11. **Stop** — summarize per comment. Fix loop → `/code-review` then `/goal` (do not auto-start).

## Anti-patterns

- One comment containing multiple unrelated findings
- Skipping per-prior resolve/reply triage on follow-up passes
- Asking about new drafts before Pass A is answered
- Bundling 2nd-pass feedback into a single PR comment
- Posting before showing full drafts (Pass B)
- Approving while prior blockers remain open
- Writing Linear comments; starting `/goal`; using inside `/goal`

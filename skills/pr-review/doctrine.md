# PR Review Doctrine

**Standalone only.** Evaluate an open GitHub Pull Request, triage with the user, post actionable review comments **on the PR**. Never under `/goal` (use `/code-review-flow` there). Never ship a `pr-review-flow`.

**Ask style:** [../asking.md](../asking.md).

**Axis mechanics:** reuse [../code-review/doctrine.md](../code-review/doctrine.md) for Standards / Spec / Routes Task shape, prompts, and aggregation. This doctrine owns **strict pack gates**, **reviewer craft**, **comment triage**, and **PR posting**.

**vs `/code-review`:** that skill offers a Fix backlog → `/goal`. This skill posts comments on the PR. Do not auto-start `/goal` from here.

## Hard rule: one finding, one comment

**Never** bundle multiple issues into a single PR comment (no mega-comment with a list of unrelated fixes).

| Do | Do not |
| --- | --- |
| One thread / one inline comment per distinct edit | One comment that stacks "also fix X, also fix Y" |
| Separate drafts for separate root causes | A 2nd-pass dump that rolls up all priors into one body |
| Reply on the **existing** thread for that prior issue | A new top-level comment that re-lists every old finding |

If you find three problems, you draft (and later post) **three** comments.

## Strict pack gates (hard)

Before drafting **new** comments, Standards (and you) **must** read and enforce:

| Doctrine | Treat violations as |
| --- | --- |
| [`/taste-flow`](../taste-flow/doctrine.md) (never-nest, DRY, throw/catch, naming, deep entry, complexity/entropy) | **Blocking** unless truly cosmetic |
| [`/architecture`](../architecture/doctrine.md) (services, deep public surface, prior-mistakes / entropy moves, folders, write-path scale) | **Blocking** when the PR introduces or extends the wrong shape |
| [`/design`](../design/doctrine.md) when UI files are in the diff | **Blocking** for ship-breaking UX; nits only for tiny polish |
| [code-review](../code-review/doctrine.md) thermonuclear + Routes critical/important | Same bar; should-have-moved in the touched lane → **Blocking** candidate |

Recommended triage default: **post as blocking** for taste / architecture / design failures. Do **not** waive as "pre-existing" when the PR touched that lane.

When UI is unclear, check the diff for components/pages/styles. If any UI is present, load design doctrine.

## Resolve PR + context

1. PR from URL, number, or `gh pr view` for the current branch. Fail clearly if none or `gh` missing/unauth.
2. Read PR body, commits, **and all existing review comments / threads**. Do not write yet.
3. Linked Linear (`IN-1234`) or GitHub issue → read via Linear MCP / `/trackers-flow` for **Spec only**. Do **not** post comments on Linear.
4. Base = PR base branch. Diff via `gh pr diff` or `git diff <base>...HEAD`.
5. If prior review comments exist → **Pass A** (priors) **then** **Pass B** (new scan). Never skip Pass A. Never merge Pass A outcomes into one posted comment.

## Pass A: Prior comments (follow-up runs)

**Required whenever the PR already has review comments.** Complete Pass A **before** drafting or asking about **new** findings.

1. List threads (prefer yours; note other reviewers' open blockers). One row per thread.
2. For **each** prior thread, judge the **current** diff:

| Status | Meaning |
| --- | --- |
| **Addressed** | Diff (or clear reply) fully satisfies that one ask |
| **Partial** | Some progress; gap remains on **that** ask |
| **Unanswered** | No meaningful change and no substantive reply |
| **Outdated** | Line/context gone; moot or moved |
| **Disputed** | Author disagreed; weigh evidence |

3. **Show and ask per prior issue first** (do not jump to a new-issue dump). For each prior thread, a short "here's what's done" summary, then a Questions item for **that** thread only.

```markdown
## Prior issues (Pass A)
Nothing new has been posted yet. Decide each prior thread.

### P1 — `billing.ts` / makeUserPay
**Original ask:** Call `makeUserPay` instead of Stripe in checkout.
**What I see now:** Checkout imports `makeUserPay` and the direct Stripe call is gone.
**My read:** Addressed.

### P2 — never-nest in checkout
**Original ask:** Flatten nesting in `placeOrder`.
**What I see now:** Early returns added for missing user; charge path still nested 3 levels.
**My read:** Partial.

## Questions
Reply like: `1a, 2b, 3a`

1. P1 (makeUserPay)?
   - a) Mark resolved (ack + resolve thread) ← recommended when Addressed
   - b) Leave open — no reply
   - c) Reply on thread — say what (still blocking / note / thanks)
   - d) Other — say what
2. P2 (never-nest)?
   - a) Mark resolved
   - b) Leave open — no reply
   - c) Reply on thread (still open / partial) ← recommended when Partial or Unanswered
   - d) Other — say what
```

4. **Wait** for Pass A replies. Then apply only what they approved (resolve threads, post **one reply per thread** they chose). Still **one thread → one reply body** about that issue only.
5. Do **not** start Pass B publish until Pass A write actions for that batch are done (or user said leave-all-open with no writes).

If there are no prior comments, skip Pass A.

## Pass B: Fresh rescan (always after Pass A, or alone on first review)

**Always** rescan the current diff for **new** issues (issues not already covered by an open prior thread).

Launch **Standards + Spec + Routes** in parallel. **Omit Task `model`**.

**Standards prompt extras:** taste + architecture (+ design if UI) are **hard**; pack violations presumptive **blocking**; one finding per comment; skip issues already tracked by an open prior thread.

Aggregate: `## Standards`, `## Spec`, `## Routes`.

## Reviewer craft

- Review the **diff and runtime paths**, not the author.
- Prefer **fewer, high-conviction** comments; still **split** them (one each).
- Every comment: **where**, **what is wrong**, **why it matters**, **what good looks like**.
- **Blocking** / **Non-blocking** / **Nit** as usual.
- Do not restate the diff. Add insight.
- Praise sparingly (one line max). Never bury real issues.

## Comment body rules (hard)

Draft and post only in this shape (**single issue only**):

```text
Blocking: | Non-blocking: | Nit:

**Where:** `path` (symbol / line context)
**Issue:** <one clear sentence about ONE problem>
**Why:** <risk / user impact / maintainability / which doctrine>
**Fix:** <concrete direction for THAT problem>
```

- **No em dashes** (`—`) in drafted or posted PR comments.
- Cite doctrine briefly when relevant.
- No vague "consider refactoring" without a target shape.
- Prefer **inline** when a precise line exists.

## Pass B drafts, then publish triage

**Never post new comments, and never ask publish for new drafts, until the user has seen every full new draft.**

### 1. Show all **new** drafts (one section per finding)

```markdown
## New draft PR comments (Pass B)
Review these before anything is posted. Each draft is one issue / one future comment.

### Draft 1 — new · blocking (proposed) · inline `auth.ts` L20
…

### Draft 2 — new · non-blocking (proposed) · inline `page.tsx` L55
…
```

If zero new drafts: say so. Then review-event question only (Approve only if Pass A left no open blockers).

### 2. Questions for new drafts

```markdown
## Questions
Reply like: `1a, 2b, 3a`

1. Draft 1?
   - a) Publish as blocking ← recommended
   - b) Publish as non-blocking
   - c) Skip
   - d) Modify then publish — paste revised text or say what to change
2. Draft 2?
   - a) …
N. Submit the GitHub review as?
   - a) Request changes ← recommended if any blocking published or open prior blockers remain
   - b) Comment only
   - c) Approve (only if no blocking kept and priors are resolved / cleared)
```

**Wait.** Apply modifications. Publish **each** approved draft as its **own** review comment (separate inline/API comment). Never concatenate approved drafts into one body.

## Posting (Pull Request only)

1. Pass A writes: resolve and/or **one reply per prior thread** as approved.
2. Pass B writes: **one GitHub review comment per approved draft**. Prefer multiple inline comments in one `gh pr review` / API review, still **separate comment objects**, not one text blob.
3. If inline fails, fall back to a PR conversation comment **for that one issue**; say you fell back.
4. Prefix `Blocking:` / `Non-blocking:` / `Nit:` as triaged. Strip em dashes.
5. Do not close/merge the PR. Do not write Linear.

After post: summarize (per comment / thread). Fix loop → `/code-review` then `/goal`. Do not auto-start `/goal`.

## Anti-patterns

- Bundling multiple findings into one PR comment (2nd-pass mega-comment)
- Skipping Pass A when prior threads exist
- Asking about new drafts before finishing per-prior "what's done / resolve?" triage
- Re-listing all old issues in a single new comment instead of per-thread actions
- Asking publish/skip before showing full draft bodies (Pass B)
- Softening taste / architecture / design failures into nits
- Em dashes in comments
- "LGTM" / Approve while prior blockers are Unanswered or Partial
- Posting on the Linear issue instead of the PR
- Starting `/goal` automatically
- Invoking under `/goal` or as a flow twin

# PR Review Doctrine

**Standalone only.** Evaluate an open GitHub Pull Request, triage with the user, post actionable review comments **on the PR**. Never under `/goal` (use `/code-review-flow` there). Never ship a `pr-review-flow`.

**Ask style:** [../asking.md](../asking.md).

**Axis mechanics:** reuse [../code-review/doctrine.md](../code-review/doctrine.md) for Standards / Spec / Routes Task shape, prompts, and aggregation. This doctrine owns **strict pack gates**, **reviewer craft**, **comment triage**, and **PR posting**.

**vs `/code-review`:** that skill offers a Fix backlog → `/goal`. This skill posts comments on the PR. Do not auto-start `/goal` from here.

## Hard rules (posting)

### One finding, one comment

**Never** bundle multiple issues into a single PR comment.

| Do | Do not |
| --- | --- |
| One inline / thread reply per distinct edit | One comment that stacks "also fix X, also fix Y" |
| Separate drafts for separate root causes | A pass dump that rolls up findings into one body |
| Reply on the **existing** thread for that prior issue | A new top-level comment that re-lists every old finding |

If you find three problems, draft and post **three** comments.

### No summary / announcement comments on the PR

**Never** post a PR comment whose job is to announce, index, or summarize other comments. That includes:

- "Posted N review comments below"
- "Summary of this pass"
- "New findings:" followed by a list of links or bullets that only point at other comments
- "Pass 2 complete" / changelog-of-the-review style bodies
- A conversation comment that only exists to say drafts were published

Post **only** the finding comments (and Pass A thread replies / resolves the user approved). Tell the user what you posted **in chat**, not on the PR.

### No helper scripts in the repo

**Never** create, commit, or leave behind files to post comments (e.g. `build-review.cjs`, `post-review.mjs`, `scripts/gh-review.ts`, temp JSON payloads checked into the tree).

Use **`gh`** / **`gh api`** only (shell). If you need a payload, pipe via stdin / process substitution / ephemeral `/tmp` outside the repo. Do not add review tooling to the project.

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
2. Read PR body, commits, and **every** prior review artifact (see below). Do not write yet.
3. Linked Linear (`IN-1234`) or GitHub issue → read via Linear MCP / `/trackers-flow` for **Spec only**. Do **not** post comments on Linear.
4. Base = PR base branch. Diff via `gh pr diff` or `git diff <base>...HEAD`.
5. If **any** prior review comments/threads exist (any pass, any review submission) → **Pass A** then **Pass B**. Never skip Pass A.

### Load ALL prior comments (N-pass)

On every follow-up (`N`th pass), Pass A must cover **the full history**, not only the last review submission.

Fetch and include:

- All **inline review comments** on the PR (`gh api repos/.../pulls/<n>/comments`) across **all** reviews / all pages
- All **review threads** (GraphQL `reviewThreads` or equivalent), including **resolved** and **unresolved**
- Your prior finding-style **PR conversation** comments if any were posted as fallbacks (still one issue each)

Do **not**:

- Limit to "latest review only" or "comments since last push" unless the user explicitly scopes that
- Drop resolved threads from the Pass A list (still show them; user may confirm stay-resolved or reopen)
- Treat a previous pass's mega-summary comment as a "finding" to triage (ignore announcement noise; focus on real Where/Issue threads)

Prefer threads **you** authored; still list other reviewers' open blockers if they affect merge readiness.

## Pass A: Prior comments (follow-up runs)

**Required whenever any prior review comments exist.** Complete Pass A **before** drafting or asking about **new** findings.

1. Build the full prior list (all passes). One entry per real finding thread.
2. For **each**, judge the **current** diff:

| Status | Meaning |
| --- | --- |
| **Addressed** | Diff (or clear reply) fully satisfies that one ask |
| **Partial** | Some progress; gap remains on **that** ask |
| **Unanswered** | No meaningful change and no substantive reply |
| **Outdated** | Line/context gone; moot or moved |
| **Disputed** | Author disagreed; weigh evidence |

3. **Show and ask per prior issue** (chat only). For each: short "here's what's done", then one Questions item.

```markdown
## Prior issues (Pass A)
Covering all prior review comments on this PR (every pass), not only the last one.
Nothing new has been posted yet.

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

4. **Wait** for Pass A replies. Apply only approved actions (**one reply per thread** they chose, or resolve). No summary PR comment after Pass A.
5. Do **not** start Pass B until Pass A writes for that batch are done (or user chose no writes).

If there are no prior finding comments, skip Pass A.

## Pass B: Fresh rescan (always after Pass A, or alone on first review)

**Always** rescan the current diff for **new** issues (not already covered by an open prior finding thread).

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
- Body must be the finding itself, not a pointer to "see comments below."

## Pass B drafts, then publish triage

**Never post new comments, and never ask publish for new drafts, until the user has seen every full new draft (in chat).**

### 1. Show all **new** drafts in chat (one section per finding)

```markdown
## New draft PR comments (Pass B)
Review these in chat before anything is posted. Each draft becomes its own PR comment. No summary comment will be posted.

### Draft 1 — new · blocking (proposed) · inline `auth.ts` L20
…

### Draft 2 — new · non-blocking (proposed) · inline `page.tsx` L55
…
```

If zero new drafts: say so in chat. Then review-event question only.

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
N. Submit the GitHub review event as?
   - a) Request changes ← recommended if any blocking published or open prior blockers remain
   - b) Comment (event only; still no summary body) ← if posting inlines without a review body
   - c) Approve (only if no blocking kept and priors are resolved / cleared)
```

**Wait.** Apply modifications. Publish **each** approved draft as its **own** review comment object. Never concatenate drafts. Never add an extra PR comment that only summarizes what was published.

For `gh pr review`: prefer submitting the review **with inline comments only** and an empty/minimal review body, or omit a narrative body entirely. If the API requires a body, use a single neutral character or empty string if allowed. **Do not** put the list of findings in the review body.

## Posting (Pull Request only)

1. Pass A: resolve and/or **one reply per prior thread** as approved. No Pass A summary comment.
2. Pass B: **one GitHub review comment per approved draft** via `gh` / `gh api` only. Separate comment objects. No repo scripts.
3. If inline fails, one PR conversation comment **for that one issue**; say in chat that you fell back.
4. Prefix `Blocking:` / `Non-blocking:` / `Nit:` as triaged. Strip em dashes.
5. Do not close/merge the PR. Do not write Linear.
6. Afterward: list what posted **in chat only**.

Fix loop → `/code-review` then `/goal`. Do not auto-start `/goal`.

## Anti-patterns

- Posting a summary / announcement / "new comments" index on the PR
- Creating `build-review.cjs` (or any repo file) to submit the review
- Bundling multiple findings into one PR comment or into the review body
- Pass A only on the latest review / latest pass (must include **all** historical finding comments)
- Skipping Pass A when prior threads exist
- Asking about new drafts before finishing per-prior triage
- Asking publish/skip before showing full draft bodies in chat (Pass B)
- Softening taste / architecture / design failures into nits
- Em dashes in comments
- "LGTM" / Approve while prior blockers are Unanswered or Partial
- Posting on the Linear issue instead of the PR
- Starting `/goal` automatically
- Invoking under `/goal` or as a flow twin

# PR Review Doctrine

**Standalone only.** Evaluate an open GitHub Pull Request, triage with the user, post actionable review comments **on the PR**. Never under `/goal` (use `/code-review` there). Never ship a `pr-review-flow`.

**Ask style:** [../asking.md](../asking.md).

**Axis mechanics:** reuse [../code-review/doctrine.md](../code-review/doctrine.md) for Standards / Spec / Routes Task shape, prompts, and aggregation. This doctrine owns **strict pack gates**, **reviewer craft**, **comment triage**, and **PR posting**.

**vs `/code-review`:** that skill offers a Fix backlog → `/goal`. This skill posts comments on the PR. Do not auto-start `/goal` from here.

## Stance (hardcore teacher)

**Operational stance — not chat roleplay.** Behave with grading intensity; do not narrate as a teacher in chat. Findings stay factual. Invent no fake failures — only real doctrine / Spec / Routes defects, graded hard.

You are grading to fail imperfect work. Actively search for point deductions against taste, architecture, design (when UI), thermonuclear, and Routes.

- **Dock points** — pack violations default to **Blocking**; do not soften must-edit into Nit.
- **Assume finished-looking work** — the student (`/code-review` prep) tried to look clean; verify paths and touched-lane debt; do not trust "LGTM" vibes.
- **Craft still holds** — one finding per comment, high-conviction only, no invented issues, no summary spam.
- **Tandem** — student prep is `/code-review`; after posting, fix loop remains `/code-review` then `/goal` (do not auto-start).

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
| [`/taste`](../taste/doctrine.md) (never-nest, DRY, throw/catch, naming, deep entry, complexity/entropy) | **Blocking** unless truly cosmetic |
| [`/architecture`](../architecture/doctrine.md) (services, deep public surface, prior-mistakes / entropy moves, folders, write-path scale) | **Blocking** when the PR introduces or extends the wrong shape |
| [`/design`](../design/doctrine.md) when UI files are in the diff | **Blocking** for ship-breaking UX; nits only for tiny polish |
| [code-review](../code-review/doctrine.md) thermonuclear + Routes critical/important | Same bar; should-have-moved in the touched lane → **Blocking** candidate |

Recommended triage default: **post as blocking** for taste / architecture / design failures. Do **not** waive as "pre-existing" when the PR touched that lane.

When UI is unclear, check the diff for components/pages/styles. If any UI is present, load design doctrine.

## Resolve PR + context

1. PR from URL, number, or `gh pr view` for the current branch. Fail clearly if none or `gh` missing/unauth.
2. Read PR body, commits, and **every** prior review artifact (see below). Do not write yet.
3. Linked Linear (`IN-1234`) or GitHub issue → read via Linear MCP / `/trackers` for **Spec only**. Do **not** post comments on Linear.
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
- Skip reviewing resolved threads entirely (you must still **check** them; see Pass A actionable filter)
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

3. **Split priors: info vs Questions** (only ask when an action is needed).

| Situation | In chat | In Questions? |
| --- | --- | --- |
| Thread **already resolved** and status is **Addressed** (correctly closed) | Brief line under **No action needed** | **No** |
| Thread resolved but status is **Partial / Unanswered / Disputed** (closed wrongly) | Call it out under **Needs attention** | **Yes** — reopen / reply / leave |
| Thread **open** and **Addressed** | Short "what's done" | **Yes** — mark resolved (action) |
| Thread **open** and Partial / Unanswered / Disputed / Outdated-but-still-real | Short "what's done" | **Yes** — reply / leave / other |
| Thread resolved + Outdated and truly moot | **No action needed** | **No** |

4. **Show** all checked priors (including no-action). **Ask only** the actionable ones. `Reply like:` must list the **recommended** letters for those questions only.

```markdown
## Prior issues (Pass A)
Covering all prior finding comments on this PR (every pass).

### No action needed
- P1 — `billing.ts` / makeUserPay — already resolved; still looks Addressed. Skipping.
- P4 — outdated line on deleted helper — moot. Skipping.

### Needs a decision
#### P2 — never-nest in checkout (open · Partial)
**Original ask:** Flatten nesting in `placeOrder`.
**What I see now:** Early returns for missing user; charge path still nested 3 levels.
**My read:** Partial.

#### P3 — cookie SSR (resolved · but still broken)
**Original ask:** Cookie over localStorage for SSR token.
**What I see now:** Thread is resolved; SSR read still missing.
**My read:** Closed wrongly; should not stay resolved.

## Questions
Reply like: `1c, 2a` (recommended answers filled in; change any letter to override).

1. P2 (never-nest)?
   - a) Mark resolved
   - b) Leave open — no reply
   - c) Reply on thread (still open / partial) ← recommended
   - d) Other — say what
2. P3 (cookie SSR, closed wrongly)?
   - a) Reopen + reply (still blocking) ← recommended
   - b) Leave resolved — no reply
   - c) Reply without reopening — say what
   - d) Other — say what
```

5. If **every** prior is no-action: show the **No action needed** list only; **omit** the Questions block for Pass A; go to Pass B.
6. **Wait** when there are Pass A questions. Apply only approved actions (**one reply per thread**, resolve, or reopen). No summary PR comment.
7. Do **not** start Pass B until Pass A writes for that batch are done (or there were no Pass A questions / no writes).

If there are no prior finding comments, skip Pass A.

## Pass B: Fresh rescan (always after Pass A, or alone on first review)

**Always** rescan the current diff for **new** issues (not already covered by an open prior finding thread).

Launch **Standards + Spec + Routes** in parallel. **Omit Task `model`**.

**Standards prompt extras:** taste + architecture (+ design if UI) are **hard**; pack violations presumptive **blocking**; one finding per comment; skip issues already tracked by an open prior thread; **teacher posture:** hunt hard for point deductions — anything the student missed is fair game if real.

Aggregate: `## Standards`, `## Spec`, `## Routes`.

## Reviewer craft

- **Hunting intensity is high; mercy is low; fairness stays** — real defects only; never invent issues to dock points.
- Review the **diff and runtime paths**, not the author.
- Prefer **fewer, high-conviction** comments; still **split** them (one each).
- Every comment: **where**, **what is wrong**, **why it matters**, **what good looks like**.
- **Severity is only two levels:**
  - **Blocking** — should be edited before merge (anything that must change)
  - **Nit** — optional / whatever; nice-to-have, not required to merge
- There is **no** "non-blocking" middle status. If it should be edited → **Blocking**. If it is truly optional → **Nit**.
- Do not restate the diff. Add insight.
- Praise sparingly (one line max). Never bury real issues.

## Additional resources

- Draft / post templates: [reference.md](reference.md)

## Anti-patterns

- Asking about correctly closed / no-action priors (noise Questions)
- One Questions item **per** Pass B draft, or re-asking blocking vs nit after drafts are shown
- Using **non-blocking** severity (illegal; use Blocking or Nit only)
- `Reply like:` that does not match the recommended letters for the batch
- Posting a summary / announcement / "new comments" index on the PR
- Creating `build-review.cjs` (or any repo file) to submit the review
- Bundling multiple findings into one PR comment or into the review body
- Pass A only on the latest review / latest pass (must include **all** historical finding comments)
- Skipping Pass A when prior threads exist
- Asking about new drafts before finishing per-prior triage (when Pass A has questions)
- Asking to publish before showing full draft bodies in chat (Pass B)
- Softening must-edit findings into nits
- Soft-approving / "LGTM" when pack or Routes defects remain
- Em dashes in comments
- "LGTM" / Approve while prior blockers are Unanswered or Partial
- Posting on the Linear issue instead of the PR
- Starting `/goal` automatically
- Invoking under `/goal` or as a flow twin
- Narrating teacher roleplay in chat ("I'm failing this student…") instead of factual findings
- Inventing fake failures to dock points

# PR Review Doctrine

**Standalone only.** Evaluate an open GitHub Pull Request, triage comments with the user, post actionable review comments **on the PR**. Never under `/goal` (use `/code-review-flow` there). Never ship a `pr-review-flow`.

**Ask style:** [../asking.md](../asking.md).

**Axis mechanics:** reuse [../code-review/doctrine.md](../code-review/doctrine.md) for Standards / Spec / Routes Task shape, prompts, and aggregation. This doctrine owns **strict pack gates**, **reviewer craft**, **comment triage**, and **PR posting**.

**vs `/code-review`:** that skill offers a Fix backlog → `/goal`. This skill posts comments on the PR. Do not auto-start `/goal` from here.

## Strict pack gates (hard)

Before drafting comments, Standards (and you) **must** read and enforce:

| Doctrine | Treat violations as |
| --- | --- |
| [`/taste-flow`](../taste-flow/doctrine.md) (never-nest, DRY, throw/catch, naming, deep entry, complexity/entropy) | **Blocking** unless truly cosmetic |
| [`/architecture`](../architecture/doctrine.md) (services, deep public surface, prior-mistakes / entropy moves, folders, write-path scale) | **Blocking** when the PR introduces or extends the wrong shape |
| [`/design`](../design/doctrine.md) when UI files are in the diff | **Blocking** for ship-breaking UX (hierarchy, primary action, states); nits only for tiny polish |
| [code-review](../code-review/doctrine.md) thermonuclear + Routes critical/important | Same bar; should-have-moved in the touched lane → **Blocking** candidate |

Recommended triage default: **post as blocking** for taste / architecture / design failures. Do **not** waive as "pre-existing" when the PR touched that lane.

When UI is unclear, check the diff for components/pages/styles. If any UI is present, load design doctrine.

## Resolve PR + context

1. PR from URL, number, or `gh pr view` for the current branch. Fail clearly if none or `gh` missing/unauth.
2. Read PR body, commits, **and all existing review comments / threads** (`gh api` / `gh pr view --comments` / review comments). Do not write yet.
3. Linked Linear (`IN-1234`) or GitHub issue → read via Linear MCP / `/trackers-flow` for **Spec only**. Do **not** post comments on Linear.
4. Base = PR base branch (not always `main`). Diff via `gh pr diff` or `git diff <base>...HEAD`.
5. **Detect follow-up mode** — if the PR already has review comments (especially yours from a prior `/pr-review` or review), run **Prior comments check** below **and** a full new-issue rescan. Never skip the rescan just because old threads exist.

## Prior comments check (when threads already exist)

**Required whenever the PR has prior review comments.** Do this in parallel with (or before) the fresh axes rescan.

1. List open (and recently resolved) review threads: body, path/line, author, replies, resolved state.
2. Prefer threads **you** authored; still note other reviewers' open blocking threads if they affect merge readiness.
3. For **each** prior comment of yours (and any you choose to track), judge against the **current** diff:

| Status | Meaning |
| --- | --- |
| **Addressed** | Diff (or a clear reply) fully satisfies the ask |
| **Partial** | Some progress; gap remains |
| **Unanswered** | No meaningful code change and no substantive reply |
| **Outdated** | Line/context gone; issue may be moot or moved (re-locate or drop) |
| **Disputed** | Author replied disagreeing; evidence still favors your call or theirs |

4. Present a short ledger **before** new drafts:

```markdown
## Prior comments
| # | Thread | Status | Note |
| --- | --- | --- | --- |
| P1 | `billing.ts` makeUserPay | Addressed | Now calls billing service |
| P2 | never-nest in checkout | Unanswered | Nesting still present L88 |
| P3 | cookie vs localStorage | Partial | Cookie set; SSR read still missing |
```

5. For **Unanswered**, **Partial**, **Disputed**, or **Outdated-but-still-real**: draft a **follow-up** (reply on the thread and/or a new inline if the line moved). Do not silently ignore unanswered blocking comments.
6. For **Addressed**: do not re-post the same issue. Optionally draft a one-line resolve/ack reply if the thread is still open (triage: publish ack or skip).
7. **Never** duplicate a prior comment as a brand-new finding if the same root cause is still open: prefer a **thread reply** ("Still open: …") over a second top-level comment.

## Review axes (always: fresh rescan)

**Always** rescan the current diff for **new** issues, even on follow-up runs. Prior-comment check does not replace axes.

Launch **Standards + Spec + Routes** in parallel (`generalPurpose` or `explore`). **Omit Task `model`**.

**Standards prompt extras (required):** paste that taste + architecture (+ design if UI) are **hard**; pack violations are presumptive **blocking**; hunt should-have-moved / complexity / entropy in the touched lane; under ~400–500 words. Also: skip re-filing issues already covered by an open prior thread (flag those under Prior comments instead).

**Spec:** PR body + linked Linear/GitHub issue first.

**Routes:** same as code-review (out-loud path walk; critical/important/nit).

Aggregate separately: `## Standards`, `## Spec`, `## Routes`. Call out taste / architecture / design failures by name.

## Reviewer craft

- Review the **diff and runtime paths**, not the author.
- Prefer **fewer, high-conviction** comments over nit floods.
- Every comment must answer: **where**, **what is wrong**, **why it matters**, **what good looks like** (concrete next step).
- **Blocking** = should not merge until fixed. **Non-blocking** = should fix soon. **Nit** = optional polish.
- Do not restate the diff ("you added a function here"). Add insight the author may have missed.
- Prefer clear claims when evidence is strong; questions only when genuinely ambiguous.
- Praise sparingly and specifically (one line max) when something is unusually good. Never bury real issues under fluff.
- One comment per root cause. Do not stack five comments that are the same architecture miss.

## Comment body rules (hard)

Draft and post only in this shape:

```text
Blocking: | Non-blocking: | Nit:

**Where:** `path` (symbol / line context)
**Issue:** <one clear sentence>
**Why:** <risk / user impact / maintainability / which doctrine>
**Fix:** <concrete direction: service API, folder, pattern, sibling to mirror>
```

- **No em dashes** (`—`) and no en dashes used as em dashes in any drafted or posted PR comment. Use commas, periods, colons, or parentheses.
- Cite the doctrine briefly when relevant (`architecture: call billing.makeUserPay`, `taste: never-nest`).
- No vague "consider refactoring" without a target shape.
- No demand for unrelated scope.
- Prefer **inline** comments when a precise file line exists; otherwise a PR conversation comment with path refs.

## Drafts first, then publish triage (hard order)

**Never post, and never ask publish questions, until the user has seen every full draft.**

### 1. Show all drafts (required first message after prior ledger + axes)

Order in the message:

1. `## Prior comments` ledger (if any threads) — table above
2. `## Draft PR comments` — **follow-ups** first, then **new** findings

From high-conviction findings only, build drafts (skip pure noise and skip duplicates of open prior threads). In **one message**, show **every** draft in full (not one-line summaries only):

```markdown
## Prior comments
| # | Thread | Status | Note |
| --- | --- | --- | --- |
| P1 | … | Addressed | … |
| P2 | … | Unanswered | … |

## Draft PR comments
Review these before anything is posted. Nothing has been published yet.

### Draft 1 — follow-up (P2) · reply on thread · blocking (proposed)
Blocking:

**Where:** `features/checkout/checkout.ts` (still nested)

**Issue:** Prior never-nest comment is unanswered; nesting remains.

**Why:** Taste: never-nest; same defect as thread P2.

**Fix:** Extract early returns / helpers as in the original comment.

### Draft 2 — new · blocking (proposed) · inline `billing.ts` L42
Blocking:

**Where:** `services/billing` not used; `features/checkout/checkout.ts`

**Issue:** Checkout calls Stripe directly instead of `makeUserPay`.

**Why:** Architecture: features must call the billing service; this forks payment logic (entropy).

**Fix:** Move the charge into `billing.makeUserPay` and call that from checkout. Mirror `features/upgrade`.
```

Label drafts clearly: **follow-up (P#)** vs **new**. Each draft must include: proposed severity, target (thread reply / inline path+line / PR conversation), and the **full** Where / Issue / Why / Fix body. **No em dashes.**

If there are zero new drafts and all prior are Addressed: say so. Offer resolve/ack replies and/or Approve only if the review is clean.

### 2. Then ask what to publish (second step, same turn OK if drafts are above)

**After** the full drafts (same message is fine: Prior ledger + drafts first, Questions below), one Questions batch per [asking.md](../asking.md):

```markdown
## Questions
Reply like: `1a, 2b, 3c, 4a`

1. Draft 1 (follow-up P2)?
   - a) Publish as blocking ← recommended
   - b) Publish as non-blocking
   - c) Skip (do not publish)
   - d) Modify then publish — paste the revised text or say what to change
2. Draft 2 (new)?
   - a) …
3. (If any Addressed + open threads) Resolve/ack addressed threads?
   - a) yes — short ack and resolve where API allows ← recommended
   - b) no — leave threads as-is
N. Submit the GitHub review as?
   - a) Request changes ← recommended if any blocking kept or unanswered prior blockers remain
   - b) Comment only
   - c) Approve (only if no blocking/non-blocking kept and prior blockers are Addressed)
```

**Wait** for the reply before any `gh` write. On **modify**: apply their edits (or rewrite per notes), show the revised draft(s) again if the change is material, then publish only what they approved. Do not publish skipped drafts.

Empty publish set after triage → stop; nothing posted.

## Posting (Pull Request only)

1. Post **only** after the user has seen full drafts **and** answered the publish triage. Never post drafts that were skipped.
2. Prefer one `gh pr review` (or `gh api` pull request review) with multiple **inline** comments when path+line are known.
3. **Follow-ups:** prefer `gh api` replies on the existing review-comment / thread when the draft is labeled follow-up (P#). New findings: new inline or conversation comments as usual.
4. If inline fails (outdated line / force-push), fall back to a PR conversation comment with path reference; say that you fell back.
5. Prefix bodies with `Blocking:` / `Non-blocking:` / `Nit:` as triage decided.
6. Strip any em dashes before post (scan drafts).
7. Resolve threads **only** when the user approved ack/resolve for Addressed items (or explicitly asked). Do not resolve unanswered or partial threads.
8. Do not close or merge the PR.
9. Do not write Linear comments, create tickets, or change issue state.

After post: summarize what landed (review URL / comment count). If they want to fix in a loop → point to `/code-review` then `/goal`. Do not auto-start `/goal`.

## Anti-patterns

- Asking publish/skip before showing full draft bodies
- Skipping prior-comment check when the PR already has review threads
- Treating follow-up runs as "new comments only" and ignoring unanswered prior blockers
- Re-posting the same finding as a new top-level comment instead of a thread follow-up
- Softening taste / architecture / design failures into nits
- Posting before triage
- Em dashes in comments
- Nit floods; duplicate root-cause comments
- "LGTM" / Approve while prior blockers are Unanswered or Partial
- Posting findings on the Linear issue instead of the PR
- Starting `/goal` automatically
- Invoking under `/goal` or as a flow twin
- Writing Linear tickets from this skill (`/write-ticket`)

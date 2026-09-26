# Review reference: GitHub PR

PR mode only. Use this after review triage; on follow-ups, complete Pass A
first. Shared review requirements are in
[review-contract.md](../pack-shared/review-contract.md); PR decisions are in
[doctrine.md](doctrine.md).

GitHub reads and writes use the harness pull-request / GitHub tool when the
harness has one; otherwise `gh` or `gh api`.

## Follow-up passes

### Pass A (historical finding adjudication)

On any follow-up, Pass A precedes new review work:

1. Read every historical finding thread and inline finding across all reviews
   and pages, including resolved threads and issue-specific conversation
   fallbacks. Ignore old summary noise.
2. Associate each with its stable internal finding ID and its GitHub thread.
   The GitHub thread, not a local registry or artifact, is the durable record.
3. Assess its current state as addressed, partial, unanswered, outdated, or
   disputed.
4. List correctly resolved or genuinely moot findings as no-action in chat. Ask
   only about thread actions that need the user's decision. Wait for that
   decision before issuing a new review batch, and apply only the approved
   reply, resolve, or reopen action.

Pass A covers the entire history even when the user asks about a recent push.

### Pass B (remediation + new surface)

After Pass A completes on a follow-up:

1. Pin `previousReviewedHead` (last reviewed head for this PR) and
   `currentHead` (live PR head). Partition `previousReviewedHead..currentHead`.
2. Run shared-contract `remediation` over addressed findings, their
   changed/touched surface, and direct callers.
3. Separately run `initial`-depth review (Standards + Spec) over **newly
   introduced** files and hunks in that partition that are outside the
   remediation set, with the same principles checklist, Architecture sweep, and
   Correctness hunt. Non-trivial Pass A adjudication and new-surface review
   **must** dispatch via Task workers per
   [subagents.md](../pack-shared/subagents.md) (one Task per independent
   surface, no cap of two). New unrelated commits must not escape review.
4. Promote the whole follow-up to `full-rescan` only when the user explicitly
   requests it or materially expands the review scope.

Do not treat "new commits alone" as a reason to skip either the remediation
pass or the new-surface pass.

## Final comment shape

Each draft and posted comment covers one topic. Fold its equivalent sites under
**Where**; never combine unrelated findings.

```text
Blocking: | Nit:

**Finding:** `standards-rule-path-symbol`
**Where:** `path` (symbol or precise line); list every folded site
**Issue:** <one clear statement of the topic>
**Trigger:** <reachable path, for runtime-risk findings only>
**Evidence:** <specific diff, path walk, rule, signal, or proof>
**Why:** <material impact or relevant rule>
**Fix:** <smallest concrete direction>
**Why not lighter:** <only for a coordination-heavy fix>
```

Use only `Blocking:` or `Nit:`. The **Finding** id must match the shared
finding record and stays stable across follow-ups. Cite a rule briefly when it
makes the issue clear, prefer the strongest inline location, and avoid em
dashes. The body is the finding, not a pointer to other comments.

## Draft display

Show every full new comment in chat before any publication:

```markdown
## New draft PR comments
Each draft becomes its own PR comment. No summary comment will be posted.

### Draft 1: Blocking, inline `path/to/file` L42
<full final comment body>
```

Severity is already decided. If there are no new public drafts and no unresolved
Blocking prior remains, ask once whether to approve the PR:

```markdown
## Questions
Reply like: 1a

1. Approve this PR as clean?
   - a) yes: submit an approval with no review-body summary ← recommended
   - b) no: leave no review event
```

If a Blocking prior remains, do not offer approval. Otherwise, when drafts
exist, ask exactly once:

```markdown
## Questions
Reply like: 1a

1. Publish all drafts above as shown?
   - a) yes: post each as its own PR comment ← recommended
   - b) no: say what to change, drop, or rewrite
```

On a revision request, show the revised full drafts before asking that same
single publish question again.

## Posting

After explicit approval:

0. **Stale-head guard:** immediately before posting comments or submitting
   approve/request-changes, re-fetch the PR head SHA. If it differs from the
   pinned `currentHead` / `headSha`, abort publish: do not post. Re-pin,
   re-partition as needed, redraft, and re-ask the single publish question.
1. Publish one comment object per draft/topic. Prefer inline placement; if it
   cannot be posted inline, use one PR conversation comment for that finding
   and report the fallback in chat.
2. Submit **Request changes** if any published comment is Blocking; otherwise
   submit a **Comment** review. For a clean approval, submit **Approve** with
   no finding comments. Keep the review body empty or minimal, never a list or
   summary of findings.
3. Do not add a summary, announcement, or pass-status PR comment. Report what
   posted in chat only. Record the published head as `previousReviewedHead`
   for the next follow-up.

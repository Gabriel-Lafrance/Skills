# PR Review Reference: drafts and posting

Use this after review triage; on follow-ups, complete Pass A first. Shared review requirements are in
[review-contract.md](../pack-shared/review-contract.md); PR-specific decisions
are in [doctrine.md](doctrine.md).

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

After explicit approval, use `gh` or `gh api` only:

1. Publish one comment object per draft/topic. Prefer inline placement; if it
   cannot be posted inline, use one PR conversation comment for that finding
   and report the fallback in chat.
2. Submit **Request changes** if any published comment is Blocking; otherwise
   submit a **Comment** review. For a clean approval, submit **Approve** with
   no finding comments. Keep the review body empty or minimal, never a list or
   summary of findings.
3. Do not add a summary, announcement, or pass-status PR comment. Report what
   posted in chat only.

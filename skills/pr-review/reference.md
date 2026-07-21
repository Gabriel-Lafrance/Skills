# PR Review reference (drafts & posting)

Load when drafting or posting. Gates stay in [doctrine.md](doctrine.md).

**Stance reminder:** teacher grades hard — pack / thermonuclear / Routes must-edits stay **Blocking** by default; do not soften into Nit. Real defects only.

## Comment body rules (hard)

Draft and post only in this shape (**single issue only**):

```text
Blocking: | Nit:

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
- Prefix is **Blocking:** or **Nit:** only. Never `Non-blocking:`.

## Pass B drafts, then one publish question

**Never post, and never ask to publish, until the user has seen every full new draft in chat** (with severity already chosen on each draft).

### 1. Show all **new** drafts in chat (one section per finding)

Severity is **already set** on each draft (Blocking or Nit). Do not ask per-draft severity.

```markdown
## New draft PR comments (Pass B)
Review these in chat before anything is posted. Each draft becomes its own PR comment. No summary comment will be posted.

### Draft 1 — Blocking · inline `auth.ts` L20
Blocking:

**Where:** …
**Issue:** …
**Why:** …
**Fix:** …

### Draft 2 — Nit · inline `page.tsx` L55
Nit:

**Where:** …
**Issue:** …
**Why:** …
**Fix:** …
```

If zero new drafts: say so in chat. No Pass B Questions (unless you only need a review event with no new comments; usually stop or Approve only when clean and priors clear).

### 2. Exactly **one** Questions item for Pass B

Do **not** ask one question per draft. Do **not** ask blocking vs nit again (already visible on the drafts). Do **not** add a separate "review event" question; derive it on publish:

- Any **Blocking** draft published → GitHub review event **Request changes**
- Only **Nit** drafts published → review event **Comment** (minimal/empty body)
- No drafts / user declined publish, priors clear → may **Approve** only if nothing open remains

```markdown
## Questions
Reply like: 1a

1. Publish all drafts above as shown?
   - a) yes — post each as its own PR comment ← recommended
   - b) no — say what to change, drop, or rewrite
```

**Wait.** On **yes**: post every shown draft as its own comment (severity unchanged). On **no**: apply their instructions, show revised drafts again if needed, then the same single question once more.

Never concatenate drafts. Never add an extra PR comment that only summarizes what was published.

For `gh pr review`: inline comments only + empty/minimal review body. **Do not** put the list of findings in the review body.

## Posting (Pull Request only)

1. Pass A: resolve and/or **one reply per prior thread** as approved. No Pass A summary comment.
2. Pass B: **one GitHub review comment per draft** via `gh` / `gh api` only (after the single yes). Separate comment objects. No repo scripts.
3. If inline fails, one PR conversation comment **for that one issue**; say in chat that you fell back.
4. Prefix `Blocking:` or `Nit:` only. Strip em dashes.
5. Do not close/merge the PR. Do not write Linear.
6. Afterward: list what posted **in chat only**.

Fix loop → `/code-review` then `/goal`. Do not auto-start `/goal`.

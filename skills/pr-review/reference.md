# PR Review reference (drafts & posting)

Load when drafting or posting. Gates stay in [doctrine.md](doctrine.md).

**Stance reminder:** grade hard with evidence — pack / thermonuclear / Spec must-edits are **Blocking** only when their contract or failure trigger is concrete. Real, evidenced defects only; no findings cap.

## Comment body rules (hard)

Draft and post only in this shape (**one topic only** — fold recurring sites of that topic):

```text
Blocking: | Nit:

**Where:** `path` (symbol / line context); if folded, list every site
**Issue:** <one clear sentence about ONE topic>
**Trigger:** <reachable caller, state, input, response, or load path — runtime-risk only>
**Evidence:** <hunk, path walk, violated rule, signal, or exploit proof; cover each folded site>
**Why:** <risk / user impact / maintainability / which doctrine>
**Fix:** <concrete direction for THAT topic at every listed site>
**Why not lighter:** <why a direct authoritative guard is insufficient — only when Fix proposes a queue, lock, retry, catch wrapper, or error system>
```

- **No em dashes** (`—`) in drafted or posted PR comments.
- Cite doctrine briefly when relevant.
- Runtime-risk comments include **Trigger:** with a reachable caller, state, input, response, or load path.
- If a runtime-risk **Fix** proposes a queue, lock, retry, catch wrapper, or error system, it also includes **Why not lighter:** with evidence that a direct authoritative guard is insufficient.
- No vague "consider refactoring" without a target shape.
- Prefer **inline** on the strongest / first site when a precise line exists; list every other occurrence under **Where**.
- Body must be the finding itself, not a pointer to "see comments below."
- Prefix is **Blocking:** or **Nit:** only. Never `Non-blocking:`.
- **Fold recurring topics:** same doctrine rule + same fix shape across sites → one draft. Unrelated topics stay separate drafts.

## Pass B drafts, then one publish question

**Never post, and never ask to publish, until the user has seen every full new draft in chat** (with severity already chosen on each draft).

### 1. Show all **new** drafts in chat (one section per topic)

Severity is **already set** on each draft (Blocking or Nit). Do not ask per-draft severity. Fold recurring sites of the same topic into one draft before showing.

```markdown
## New draft PR comments (Pass B)
Review these in chat before anything is posted. Each draft becomes its own PR comment (one topic each; recurring sites folded). No summary comment will be posted.

### Draft 1 — Blocking · inline `auth.ts` L20 (also `checkout.ts`, `orders.ts`)
Blocking:

**Where:**
- `auth.ts` L20 (`requireUser`)
- `checkout.ts` L88 (`placeOrder`)
- `orders.ts` L41 (`cancelOrder`)
**Issue:** Nesting pyramids on the same auth/guard pattern; flatten with early returns.
**Trigger:** … (runtime-risk only)
**Evidence:** …
**Why:** …
**Fix:** …
**Why not lighter:** … (coordination-heavy fix only)

### Draft 2 — Nit · inline `page.tsx` L55
Nit:

**Where:** `page.tsx` L55
**Issue:** …
**Trigger:** … (runtime-risk only)
**Evidence:** …
**Why:** …
**Fix:** …
**Why not lighter:** … (coordination-heavy fix only)
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

Never concatenate **unrelated** topics into one draft. Never add an extra PR comment that only summarizes what was published. Do fold recurring sites of the same topic before asking to publish.

For `gh pr review`: inline comments only + empty/minimal review body. **Do not** put the list of findings in the review body.

## Posting (Pull Request only)

1. Pass A: resolve and/or **one reply per prior thread** as approved. No Pass A summary comment.
2. Pass B: **one GitHub review comment per draft/topic** via `gh` / `gh api` only (after the single yes). Separate comment objects. Folded topics stay one comment with every site listed. No repo scripts.
3. If inline fails, one PR conversation comment **for that one issue**; say in chat that you fell back.
4. Prefix `Blocking:` or `Nit:` only. Strip em dashes.
5. Do not close/merge the PR. Do not write Linear.
6. Afterward: list what posted **in chat only**.

Fix loop → `/code-review` then `/goal`. Do not auto-start `/goal`.

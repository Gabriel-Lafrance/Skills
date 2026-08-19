# Opening a pull request

Every agent that **creates or updates a GitHub PR** while this pack is
installed follows this contract — **not only `/publish`**.

Parents include `/publish`, `/just-do-it` ship, `/goal` when this chat
owns shipping and the user asked to open a PR, and any cloud or freeform agent that ships a branch
as a PR.

Body templates, change type, branch names, and Mermaid rules stay in
[`../publish/reference.md`](../publish/reference.md). This file owns demo
screenshots, the Cursor review canvas, and which create/update tool to use.

Do **not** load [browser-evidence.md](browser-evidence.md) to ship a PR.
That protocol is for `/goal` acceptance proof. A screenshot on the PR is
not a test pass.

## Required Reads

1. [`../publish/reference.md`](../publish/reference.md) — title, type template,
   Change diagram, How to QA.
2. This file — screenshots, canvas, create tool.
3. When producing the review canvas: the installed Cursor **canvas** skill
   (`canvas/SKILL.md`), and **PR review canvas** if that skill is installed.

## Who this applies to

| Actor | Follows this? |
| --- | --- |
| `/publish` | Yes |
| `/just-do-it` ship | Yes |
| Standalone `/goal` after “open a PR?” = yes | Yes |
| Cloud / background agent opening a PR without naming `/publish` | Yes |
| `/pr-review` (comments only) | No — does not create the PR |
| Flow `/goal` | No — the parent ships |

Do not skip the canvas or screenshots because the work was done by
`/just-do-it`, `/goal`, or a cloud agent. The create path does not change
the bar.

## Demo screenshots

When the change is **user-visible**, put a picture in the PR body so a
reviewer can see the screen without checking out the branch. Use Cursor’s
Browser **only** to open the page and take the screenshot.

1. Reuse an already-running local app or preview. Do not start a second
   server just for a picture.
2. Open the changed screen (existing tab if one is there).
3. Take **one or a few** screenshots of the state a reviewer should see.
   Honest alt text. Stop.
4. Embed them in `## Demo` after How to QA (see Create tool). Never put
   artifact paths only in a PR comment — rewriting happens on the body.

**This is not a test pass.** Do not walk empty / loading / error / success
just to be thorough. Do not check the console or network. Do not mark
criteria pass or fail. Do not record a video. Do not build a Playwright
harness. If a recording already exists from this session, you may attach it;
do not go capture one.

If Browser is unavailable, the app is not running, or the change is **not
visual** (docs, schema, CI, skill markdown), omit Demo — or one Notes line
on why. **Do not block the PR.**

**Do not** commit screenshots or videos into the git repo just to attach them.

## Cursor review canvas

For a **non-trivial** PR, also produce a Cursor canvas that walks a reviewer
through the change — the same job as a PR review canvas, done at ship time.

Skip only when the diff is typo-only or otherwise hostile to a walkthrough
(same bar as omitting a Change diagram); say why in Notes.

The canvas is **part of shipping the PR**, not a substitute for the GitHub
body. The generic canvas skill may say not to canvas “make this PR” — this
pack overrides that for ship: the PR is the deliverable, and the canvas is
how reviewers see it quickly.

### What to put on it

Reorganize by reviewer value, not file-tree order:

1. **Demo** — screenshots when you have them (see Media on the canvas).
   Lead with this when the change is visual.
2. **Core** — new behavior, algorithms, state, API surface. Full diffs and
   short notes on *why*.
3. **Wiring** — routes, registration, config that connect the core. Condensed.
4. **Mechanical** — renames, generated code, formatting. File list and stats;
   no inline diffs unless something is surprising.

Use callouts only for genuinely tricky hunks. Prefer the canvas SDK’s diff,
cards, and stats over hand-rolled chrome. Follow the canvas skill’s design
rules (no gradients, emoji decoration, or box shadows).

### Where it lives

Follow the installed canvas skill’s delivery path:

- **Cloud:** write the `.canvas.tsx` where that skill says, then publish with
  the cloud share tool when it exists. Put the **share URL** in chat and in
  the PR body’s Demo or Notes section. Do not link a VM file path.
- **Local:** write the `.canvas.tsx` beside chat and link the file in chat and
  in the PR body.

One canvas per PR; update it when you update the PR in a meaningful way.

### Media on the canvas

If the canvas host can render them, include `<img>` with the same absolute
artifact paths used in the PR body. If it cannot, still describe the demo in
one or two sentences and link the GitHub Demo section. Do not drop the
GitHub embeds because the canvas exists.

## Create tool

Show the complete title and body in chat before creating (approval rules stay
with `/publish`; `/just-do-it` still prints the draft, then creates).

Then pick **one** write path:

| Session | How to create or update the PR |
| --- | --- |
| Cursor pull-request tool is available (typical cloud agent) | Use that tool. Put screenshots in the **body** with HTML tags and absolute paths, for example `<img alt="Checkout success" src="/opt/cursor/artifacts/screenshots/checkout-success.png" />`. Attach `<video>` only when a recording already exists. Do **not** use `gh pr create` or `gh pr edit` for that write — those skip artifact rewriting, so images stay broken on GitHub. |
| No Cursor pull-request tool (typical local `gh`) | Use the heredoc in [publish reference](../publish/reference.md). Embed images only when you already have a URL GitHub can fetch. Do not invent URLs. Point reviewers at the canvas or chat attachments when files cannot be inlined. |

Push the branch before create, unless the user asked for local-only. Never
force-push or push the default branch.

If a PR is already open on the branch, update its body with the same tool
choice; do not open a second PR.

## Anti-patterns

- Only `/publish` attaching screenshots or producing a review canvas
- Creating the PR with `gh` in a session that has Cursor’s pull-request tool
- Putting `/opt/cursor/artifacts/…` paths in a comment instead of the body
- Committing binaries into the repo to “attach” a demo
- Running [browser-evidence.md](browser-evidence.md) (or any full UI test
  loop) just to fill Demo
- Recording a walkthrough or checking every UI state at ship time
- Blocking the PR because Browser was unavailable
- Building a canvas that is a file list in tree order
- Skipping the canvas because a cloud Walkthrough tab exists

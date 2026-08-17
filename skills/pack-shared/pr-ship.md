# Opening a pull request

Every agent that **creates or updates a GitHub PR** while this pack is
installed follows this contract — **not only `/publish`**.

Parents include `/publish`, `/just-do-it` ship, standalone `/goal` when the
user asked to open a PR, and any cloud or freeform agent that ships a branch
as a PR.

Body templates, change type, branch names, and Mermaid rules stay in
[`../publish/reference.md`](../publish/reference.md). This file owns demo
media, the Cursor review canvas, and which create/update tool to use.

## Required Reads

1. [`../publish/reference.md`](../publish/reference.md) — title, type template,
   Change diagram, How to QA.
2. This file — demo media, canvas, create tool.
3. For user-visible or browser-reachable changes:
   [`browser-evidence.md`](browser-evidence.md).
4. When producing the review canvas: the installed Cursor **canvas** skill
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

Do not skip the canvas or demo because the work was done by `/just-do-it`,
`/goal`, or a cloud agent. The create path does not change the bar.

## Demo media

When the change is **user-visible or browser-reachable**, put proof in the PR
body so a reviewer can see the path without checking out the branch.

1. Reuse screenshots already captured for acceptance evidence. If none exist,
   capture them now with [browser-evidence.md](browser-evidence.md).
2. When this session can record the screen, record a short happy-path
   walkthrough (and any state that How to QA calls out). Save it with a
   descriptive name.
3. Embed those files in the **PR description** (see Create tool). Never put
   artifact paths only in a PR comment — rewriting happens on the body.
4. Add a `## Demo` section after How to QA (templates in publish reference).

When the change is **not visual** (docs-only, schema, CI, skill markdown with
no UI), omit Demo. If a reviewer might expect a recording, say why in Notes.

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

1. **Demo** — screenshots and video when you have them (see Media on the
   canvas). Lead with this when the change is visual.
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

If the canvas host can render them, include `<img>` / `<video>` with the same
absolute artifact paths used in the PR body. If it cannot, still describe the
demo in one or two sentences and link the GitHub Demo section. Do not drop
the GitHub embeds because the canvas exists.

## Create tool

Show the complete title and body in chat before creating (approval rules stay
with `/publish`; `/just-do-it` still prints the draft, then creates).

Then pick **one** write path:

| Session | How to create or update the PR |
| --- | --- |
| Cursor pull-request tool is available (typical cloud agent) | Use that tool. Put demo files in the **body** with HTML tags and absolute paths, for example `<img alt="Checkout success" src="/opt/cursor/artifacts/screenshots/checkout-success.png" />` and `<video src="/opt/cursor/artifacts/checkout-happy-path.mp4"></video>`. Do **not** use `gh pr create` or `gh pr edit` for that write — those skip artifact rewriting, so images and video stay broken on GitHub. |
| No Cursor pull-request tool (typical local `gh`) | Use the heredoc in [publish reference](../publish/reference.md). Embed images only when you already have a URL GitHub can fetch. Do not invent URLs. Point reviewers at the canvas or chat attachments when files cannot be inlined. |

Push the branch before create, unless the user asked for local-only. Never
force-push or push the default branch.

If a PR is already open on the branch, update its body with the same tool
choice; do not open a second PR.

## Anti-patterns

- Only `/publish` attaching demo media or producing a review canvas
- Creating the PR with `gh` in a session that has Cursor’s pull-request tool
- Putting `/opt/cursor/artifacts/…` paths in a comment instead of the body
- Committing binaries into the repo to “attach” a demo
- Calling visual proof done from terminal output alone
- Skipping the canvas because a cloud Walkthrough tab exists — still embed
  media on GitHub and still ship the review canvas
- Building a canvas that is a file list in tree order

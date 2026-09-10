# Opening a pull request

Every agent that **creates or updates a GitHub PR** while this pack is
installed follows this contract — **not only `/publish`**.

Parents include `/publish`, `/just-do-it` ship, `/task` when this chat
owns shipping and the user asked to open a PR, and any cloud or freeform agent that ships a branch
as a PR.

Body templates, change type, branch names, and Mermaid rules stay in
[`../publish/reference.md`](../publish/reference.md). This file owns
which create/update tool to use.

No Demo screenshots, no review canvas, no videos. The PR body is text:
type, ticket, what changed, Change diagram, How to QA, Notes. Do not
open a browser, capture screenshots, or produce a canvas to ship a PR.

## Required Reads

1. [`../publish/reference.md`](../publish/reference.md) — title, type template,
   Change diagram, How to QA.
2. This file — create tool.

## Who this applies to

| Actor | Follows this? |
| --- | --- |
| `/publish` | Yes |
| `/just-do-it` ship | Yes |
| Standalone `/task` after “open a PR?” = yes | Yes |
| Cloud / background agent opening a PR without naming `/publish` | Yes |
| `/pr-review` (comments only) | No — does not create the PR |
| Flow `/task` | No — the parent ships |

## Create tool

Show the complete title and body in chat before creating (approval rules stay
with `/publish`; `/just-do-it` still prints the draft, then creates).

Then pick **one** write path:

| Session | How to create or update the PR |
| --- | --- |
| Cursor pull-request tool is available (typical cloud agent) | Use that tool. Do **not** use `gh pr create` or `gh pr edit` for that write. |
| No Cursor pull-request tool (typical local `gh`) | Use the heredoc in [publish reference](../publish/reference.md). |

Push the branch before create, unless the user asked for local-only. Never
force-push or push the default branch.

## Before you commit

Run this repo’s existing `lint` and `test` scripts (`test:quality` when that
is the test script). Fix failures before `git commit`. That catches the same
failures CI will report on the PR. Skip `test:mutants` here. If those scripts
are missing, skip. Never `git commit --no-verify` unless the user asked.

If a PR is already open on the branch, update its body with the same tool
choice; do not open a second PR.

## Anti-patterns

- Creating the PR with `gh` in a session that has Cursor’s pull-request tool
- Opening a browser, capturing screenshots, or producing a review canvas to ship a PR
- Committing binaries into the repo to “attach” a demo
- Recording a walkthrough or checking every UI state at ship time

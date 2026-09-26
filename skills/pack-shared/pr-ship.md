# Opening a pull request

Every agent that **creates or updates a GitHub PR** while this pack is
installed follows this contract. The name pattern and hard rules are in [shipping.md](../rules/shipping.md).

This applies to `/task` when this chat owns shipping and the user asked to open a PR, and to any cloud or freeform agent that ships a branch as a PR.

Body templates and Mermaid rules stay in
[`ship.md`](ship.md). This file owns
which create/update tool to use and the CI mirror before a push that opens or updates a PR.

No Demo screenshots, no review canvas, no videos. The PR body is text:
type, ticket, what changed, Change diagram, How to QA, Notes. Do not
open a browser, capture screenshots, or produce a canvas to ship a PR.

## Required Reads

1. [`ship.md`](ship.md): for the title and body template (type template, Change diagram, How to QA).
2. This file: create tool and the CI mirror.

## Who this applies to

| Actor | Follows this? |
| --- | --- |
| Standalone `/task` after "Ship this work?" = yes | Yes |
| Any agent opening a PR | Yes |
| `/review` on a GitHub PR (comments only) | No. Does not create the PR |
| Nested `/task` when a parent owns shipping | No. The parent ships |

## Create tool

Show the complete title and body in chat before creating. Wait for approval. [shipping.md](../rules/shipping.md) is the rule.

Then pick **one** write path:

| Session | How to create or update the PR |
| --- | --- |
| This harness has a pull-request tool | Use that tool. Do **not** use `gh pr create` or `gh pr edit` for that write. |
| No pull-request tool | Use the heredoc in [ship.md](ship.md). |

Before create, cut and push the branch with the branch-and-push step of the Process in [ship.md](ship.md), unless the user asked for local-only.

If a PR is already open on the branch, update its body with the same tool
choice; do not open a second PR.

## Green before a CI push

Remote CI confirms a tree that is already green here. A red push spends
Actions minutes and a build for nothing.

Run the check in the environment you are in: the local machine, or this
cloud agent VM. Do not start GitHub Actions (`gh workflow run`, a push, or
a rerun) to learn if the tree is green.

**When**

- You are about to push a branch that will open a PR
- You are about to commit or push on a branch that already has an open PR

**When not**

A local commit you are not pushing, while no PR is open on that branch.
Do not run the suite then.

**Once**

If this exact tree already passed and nothing has changed, do not run it
again before the push.

**What to run**

1. Read `.github/workflows` for jobs that run on `pull_request`, and on
   `push` when that is what updates the open PR. Run those jobs' check
   commands here.
2. Skip deploy, publish, and jobs that need secrets you do not have. Say
   which jobs you skipped.
3. If a workflow path filter would skip the job for this diff, skip it here
   too. A docs-only change does not get a full build the workflow would not
   run.
4. If there is no such workflow, run `lint` and `test` when those scripts
   exist.
5. Do not wipe and reinstall dependencies when the lockfile is unchanged and
   the install is already present.
6. If a command fails, fix it and rerun that command. Then push once.
7. If there is no workflow and no `lint` or `test` script, say so and
   continue. Do not invent a suite.
8. Never `git commit --no-verify` or `git push --no-verify` unless the user
   asked.

**Do not**

- Push red and wait for CI
- Run the suite after every slice while coding
- Run a full build the workflow would skip

## Anti-patterns

- Pushing a new branch onto `dev`, `main`, or `master`, or leaving its upstream on those refs
- Pushing red so GitHub Actions is the first time the suite runs
- Running the CI mirror on a commit that will not be pushed
- Creating the PR with `gh` when this harness has a pull-request tool
- Opening a browser, capturing screenshots, or producing a review canvas to ship a PR
- Committing binaries into the repo to “attach” a demo
- Recording a walkthrough or checking every UI state at ship time

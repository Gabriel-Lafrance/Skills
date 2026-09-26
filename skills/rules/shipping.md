# Shipping

Any agent that cuts a branch or creates or updates a GitHub pull request follows this file. There is no `/publish` skill. Question shapes, the Change diagram rule, and the PR body template live in [shipping-templates.md](shipping-templates.md).

| Actor | Follows this? |
| --- | --- |
| Standalone `/task` after "Ship this work?" = yes | Yes |
| Any agent opening a PR, including a cloud or freeform agent | Yes |
| `/review` on a GitHub PR (comments only) | No. Does not create the PR |
| Nested `/task` when a parent owns shipping | No. The parent ships |

## Branch names

```text
{type}/{ticket}-{slug}
```

| Type | Use when |
| --- | --- |
| `feature` | New capability or intentional enhancement |
| `tweak` | Small bounded intentional adjustment, not a defect or standalone capability |
| `bug` | A defect, including an urgent production defect |
| `refactor` | Structural change with behavior preserved (no intended product behavior change) |
| `chore` | Non-product maintenance: deps, CI, tooling, docs-only, repo hygiene |

- The type matches the ticket kind.
- `ticket` is the Linear id (`IN-1234`) or the GitHub issue number (`42`).
- `no-ticket` only when the user explicitly says there is no ticket.
- `slug` is a lowercase verb phrase in kebab case. No spaces or colons. Keep the name under about 60 characters.
- Examples: `bug/IN-1234-fix-checkout-total`, `tweak/IN-1234-adjust-empty-state-copy`, `feature/ENG-99-add-invite-flow`, `refactor/42-extract-billing-service`, `chore/IN-55-bump-eslint`.

## Hard rules

- Do not auto-commit, force-push, or push `dev`, `main`, `master`, or the default branch.
- A new branch is a standalone ref. Cut it with `git switch --detach <base-sha>`, then `git switch -c <new-branch>` (or `git switch --no-track -c`). It must not track `origin/dev`, `origin/main`, or `origin/master`. Push only `HEAD:refs/heads/<new-branch>`. If `@{upstream}` is `origin/dev`, `origin/main`, or `origin/master`, stop. Steps: [Branch and push](#3-branch-and-push).
- Show the complete pull request title and body, and wait for approval before creating it.
- Body: type, ticket, what changed, Mermaid Change diagram (Before/After for rework), How to QA, Notes. The body is text: no screenshots, no canvas, no videos, no browser.
- Do not invent a ticket. Use `/write-ticket` when the work belongs on a tracker.
- Before a push that opens a PR, or a commit or push on a branch that already has an open PR, run the [CI mirror](#ci-mirror). Push once it is green. Never `--no-verify` unless the user asked.
- Use the harness pull-request tool when it has one. Otherwise use `gh` ([Create or update the PR](#create-or-update-the-pr)). Do not use `gh` in a session that already has a pull-request tool.

## Create or update the PR

Before create, cut and push the branch with [Branch and push](#3-branch-and-push), unless the user asked for local-only. Then pick **one** write path, only after the user approved the title and body:

| Session | How to create or update the PR |
| --- | --- |
| This harness has a pull-request tool | Use that tool. Do **not** use `gh pr create` or `gh pr edit` for that write |
| No pull-request tool | Use the `gh` command below |

```bash
gh pr create --title "<title>" --base <base> --body "$(cat <<'EOF'
<approved body>
EOF
)"
```

If a PR is already open on the branch, update its body with the same tool choice; do not open a second PR.

## CI mirror

Remote CI confirms a tree that is already green here. A red push spends Actions minutes and a build for nothing. Run the check in the environment you are in: the local machine, or this cloud agent VM. Do not start GitHub Actions (`gh workflow run`, a push, or a rerun) to learn if the tree is green.

**When:** you are about to push a branch that will open a PR, or to commit or push on a branch that already has an open PR.

**When not:** a local commit you are not pushing, while no PR is open on that branch.

**Once:** if this exact tree already passed and nothing has changed, do not run it again before the push.

**What to run**

1. Read `.github/workflows` for jobs that run on `pull_request`, and on `push` when that is what updates the open PR. Run those jobs' check commands here.
2. Skip deploy, publish, and jobs that need secrets you do not have. Say which jobs you skipped.
3. If a workflow path filter would skip the job for this diff, skip it here too. A docs-only change does not get a full build the workflow would not run.
4. If there is no such workflow, run `lint` and `test` when those scripts exist.
5. Do not wipe and reinstall dependencies when the lockfile is unchanged and the install is already present.
6. If a command fails, fix it and rerun that command. Then push once.
7. If there is no workflow and no `lint` or `test` script, say so and continue. Do not invent a suite.
8. Never `git commit --no-verify` or `git push --no-verify` unless the user asked.

## Process

### 1. Inspect git

In parallel, inspect `git status`, current branch, remotes/default base, commits ahead of base, and diff summary.

| State | Action |
| --- | --- |
| No pull-request tool, and no `gh` or not authenticated | Cut and push the branch as usual. Stop before the publish step and say why |
| Dirty tree | Ask commit first, stash, or abort; never auto-commit. If that commit will be pushed, or a PR is already open on the branch, run the [CI mirror](#ci-mirror) first and push only when it is green |
| No commits ahead of base | Stop; there is nothing to publish |
| Detached HEAD | Create the standalone branch from that commit (step 3), then continue on it |

### 2. Lock type and ticket

Use the [type and ticket questions](shipping-templates.md#questions-and-announcements) unless both are already clear. If no ticket exists, ask once whether to stop and create one with `/write-ticket` (recommended) or use `no-ticket` because the user said there is none.

### 3. Branch and push

A new branch is a standalone ref. GitHub applies `dev`'s protection only when a push updates `dev`. Three common ways to do that by accident:

- `git switch -c <name> origin/dev` or `git checkout -b <name> origin/dev` sets upstream to `origin/dev` under the default `branch.autoSetupMerge` (`true`). `inherit` and `always` also copy it from a local `dev` that tracks `origin/dev`.
- A plain `git push` then fails and suggests `git push origin HEAD:dev`. That updates protected `dev`.
- With `push.default=upstream`, a plain `git push` updates `dev` and never creates the new remote ref.

The same trap exists for `main` and `master`.

1. Build `{type}/{ticket}-{slug}` from the locked values. The name is not `dev`, `main`, or `master`.
2. Announce the branch with the [branch announcement](shipping-templates.md#questions-and-announcements) Locked block.
3. Record the base SHA (`git rev-parse <base>`) and create the branch from that commit:

   ```bash
   git switch --detach <base-sha>
   git switch -c <new-branch>
   ```

   Same result in one command: `git switch --no-track -c <new-branch> <base-sha>`.

   Do not use `git switch -c` or `git checkout -b` from a remote ref without `--no-track`. Do not `git branch --set-upstream-to` `origin/dev`, `origin/main`, `origin/master`, or the default branch. End on the new branch: `git branch --show-current` prints `<new-branch>`.

   Reuse a local branch only when it already holds the intended commits and its upstream is unset or `origin/<new-branch>`. If `@{upstream}` is `origin/dev`, `origin/main`, or `origin/master`, run `git branch --unset-upstream` before any push. If the current branch is `dev`, `main`, or `master`, create the standalone branch before any commit. Rename only a disposable local branch that holds the intended commits, and only when upstream stays unset or `origin/<new-branch>`.
4. Unless the user asked for local-only work, check that `git rev-parse --abbrev-ref --symbolic-full-name @{upstream}` is unset or `origin/<new-branch>`. If it is `origin/dev`, `origin/main`, or `origin/master`, stop. Then push the new name only:

   ```bash
   git push -u origin HEAD:refs/heads/<new-branch>
   ```

5. Never force-push. Never `git push` with no refspec while upstream is `origin/dev`, `origin/main`, or `origin/master`. If git suggests `git push origin HEAD:dev`, `HEAD:main`, or `HEAD:master`, do not run it.

### 4. Ask whether to draft and publish

After a successful push, ask the [draft and publish question](shipping-templates.md#questions-and-announcements) and wait:

- Declined: return the branch and remote URL.
- Draft only: show it in chat and stop.
- Approved: continue to the full draft.

### 5. Draft the PR

Build the title and body from the commits, diff, ticket, and locked type with the [body template](shipping-templates.md#body-template) and [title shape](shipping-templates.md#pr-title-and-body). Keep **How to QA** concrete: paths, roles, clicks, commands, and checkable outcomes. Never ship empty QA steps.

Show the complete title and body, then ask the publish question. Never create a PR silently.

### 6. Publish

On approval only, create or update the PR with the [write path](#create-or-update-the-pr). Return the PR URL. Do not write Linear comments or change ticket status.

## Do not

- Invent a ticket, or use a branch type that does not match the ticket kind
- Implement new product work in the same turn as shipping
- Push a new branch onto `dev`, `main`, or `master`, or leave its upstream on those refs
- Push red so GitHub Actions is the first time the suite runs, or push red and wait for CI
- Run the CI mirror on a commit that will not be pushed, after every slice while coding, or as a full build the workflow would skip
- Create the PR with `gh` when this harness has a pull-request tool
- Open a browser, capture screenshots, or produce a review canvas to ship a PR
- Commit binaries into the repo to "attach" a demo
- Record a walkthrough or check every UI state at ship time

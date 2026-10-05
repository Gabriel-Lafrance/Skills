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
- `slug` is a lowercase verb phrase in kebab case (hyphens only, no spaces or colons). Keep the name under about 60 characters.
- Examples: `bug/IN-1234-fix-checkout-total`, `tweak/IN-1234-adjust-empty-state-copy`, `feature/ENG-99-add-invite-flow`, `refactor/42-extract-billing-service`, `chore/IN-55-bump-eslint`.

## Shipping rules

- Never commit to, push to, or force-push `main`, `master`, `dev`, or the default branch. Work on a new branch.
- Show the complete pull request title and body, and wait for approval before creating it unless the user already authorized publishing the [whole stack](#stacked-pull-requests).
- A new branch is a standalone ref. Cut it with `git switch --detach <base-sha>`, then `git switch -c <new-branch>` (or `git switch --no-track -c`). It must not track `origin/dev`, `origin/main`, or `origin/master`. Push only `HEAD:refs/heads/<new-branch>`. If `@{upstream}` is `origin/dev`, `origin/main`, or `origin/master`, stop. Steps: [Branch and push](#3-branch-and-push).
- Body: type, ticket, what changed, Mermaid Change diagram (Before/After for rework), How to QA, Notes. The body is text. When [`/verification`](../verification/SKILL.md) ran, summarize its handoff under Notes.
- End every new or updated PR body with the [blast radius and merge danger assessment](shipping-templates.md#blast-radius-and-merge-danger), including each stacked PR. Apply it through every publication tool; keep stack and verification details above it. Refresh it against the current PR base, diff, and actual evidence before publication. It is reporting, never permission to merge.
- Use only a real ticket. Use `/write-ticket` when the work belongs on a tracker.
- Before a push that opens or updates a PR, apply the [CI mirror](#ci-mirror) policy: scoped verification and repository-required local checks, valid evidence reuse, and honest remote CI status. A local commit or clean Git sync does not itself trigger a full mirror because a PR exists. Never bypass required checks or hooks.
- Use the harness pull-request tool when it has one. Otherwise use `gh` ([Create or update the PR](#create-or-update-the-pr)).

## Create or update the PR

Before create, cut and push the branch with [Branch and push](#3-branch-and-push), unless the user asked for local-only. Then pick **one** write path after title/body approval or explicit whole-stack publishing authorization:

| Session | How to create or update the PR |
| --- | --- |
| This harness has a pull-request tool | Use that tool for the whole write, in place of `gh pr create` and `gh pr edit` |
| No pull-request tool | Use the `gh` command below |

```bash
gh pr create --title "<title>" --base <base> --body "$(cat <<'EOF'
<approved body>
EOF
)"
```

If a PR is already open on the branch, update its body with the same tool choice instead of opening a second PR.

## Stacked pull requests

A user request such as "implement all children and open stacked PRs" authorizes branches, scoped commits, pushes, and PR creation for that set. Show each finished title and body before publishing, then proceed without repeating the ship or publish questions. Default to draft PRs unless the user requested ready-for-review PRs. A ticket containing an example execution request is not itself publishing authorization. This authorization does not include merging PRs, force-pushing, unrelated work, or tracker status changes.

- Use the child's ticket ID and kind for its branch and PR. The first PR targets the recorded integration branch; each dependent PR targets its predecessor's branch. Independent children can target the integration branch. Confirm that the selected base contains all of the child's prerequisites.
- Cut a standalone branch from the selected base SHA using the existing branch safety rules. Git upstream tracking stays unset or points to that branch's own remote, never to the predecessor or integration branch.
- Review and describe only the child's delta against its actual PR base. Run its CI mirror on the resulting tree. Link its child ticket, parent ticket, prerequisite PRs, and position in the stack in Notes. Each PR must pass its checks before later children are included.
- Reuse existing child PRs on resume. If a predecessor changes, refresh affected descendants and recheck their diffs and gates before reporting completion. After an ancestor merges, confirm the descendant base and diff before retargeting; follow the existing prohibition on force-pushes.
- Return a table of child tickets, PR URLs, branches, and bases. Leave PRs open for review. A blocked child blocks its dependents; report completed PRs and remaining work without calling the whole stack complete.

## CI mirror

This anchor owns applicable pre-push checks, not an unconditional local replica
of every CI job. A local merge/commit alone follows [Git sync only](execution.md#git-sync-only)
or its actual changed scope, even when the branch has an open PR.

Before shipping, inspect repository instructions, hooks, CI jobs/path filters,
and known required checks. Run mandatory local commands and the checks selected
by [verification scope](execution.md#verification-scope). A full local CI mirror
is warranted when required by the repository, explicitly requested, or justified
by cross-cutting impact/uncertainty. A bounded fix need not repeat unrelated
full suites locally merely because remote CI includes them. Preserve the actual
remote CI requirements and security controls; do not edit workflows or protection
to avoid checks.

Reuse applicable passing evidence when relevant code/context remain unchanged;
recheck invalidated claims. Use supported scoped commands and existing dependencies.
If a selected local check fails, fix/recheck it before shipping or report the
blocker. If required access/setup is unavailable, disclose the missing check;
do not call it passed. Deployment/publishing jobs remain outside verification.

An authorized push may trigger configured remote CI after applicable local
checks. Report remote checks as pending, passed, failed, or unavailable on the
actual head; do not call shipping ready or mergeable while required CI is
pending/failed. If the repository requires a gate before push, honor that gate.
Do not start redundant workflow runs, bypass hooks, or change branch protection.
The shipping handoff briefly states actual checks/results, retained evidence,
and residual unverified scope. No workflow or test commands means no invented suite.

## Process

### 1. Inspect git

In parallel, inspect `git status`, current branch, remotes/default base, commits ahead of base, and diff summary.

| State | Action |
| --- | --- |
| No pull-request tool, and no `gh` or not authenticated | Cut and push the branch as usual. Stop before the publish step and say why |
| Dirty tree | Commit only authorized scoped changes; otherwise resolve the index boundary with the user. Preserve unrelated work. Apply [CI mirror](#ci-mirror) before a requested push, not merely because a local commit updates an open-PR branch |
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

1. Build `{type}/{ticket}-{slug}` from the locked values. Pick a name other than `dev`, `main`, or `master`.
2. Announce the branch in a Locked in message using the [branch announcement](shipping-templates.md#questions-and-announcements) shape.
3. Record the base SHA (`git rev-parse <base>`) and create the branch from that commit:

   ```bash
   git switch --detach <base-sha>
   git switch -c <new-branch>
   ```

   Same result in one command: `git switch --no-track -c <new-branch> <base-sha>`.

   From a remote ref, add `--no-track` to `git switch -c` or `git checkout -b`. Never `git branch --set-upstream-to` `origin/dev`, `origin/main`, `origin/master`, or the default branch. End on the new branch: `git branch --show-current` prints `<new-branch>`.

   Reuse a local branch only when it already holds the intended commits and its upstream is unset or `origin/<new-branch>`. If `@{upstream}` is `origin/dev`, `origin/main`, or `origin/master`, run `git branch --unset-upstream` before any push. If the current branch is `dev`, `main`, or `master`, create the standalone branch before any commit. Rename only a disposable local branch that holds the intended commits, and only when upstream stays unset or `origin/<new-branch>`.
4. Unless the user asked for local-only work, check that `git rev-parse --abbrev-ref --symbolic-full-name @{upstream}` is unset or `origin/<new-branch>`. If it is `origin/dev`, `origin/main`, or `origin/master`, stop. Then push the new name only:

   ```bash
   git push -u origin HEAD:refs/heads/<new-branch>
   ```

5. Never force-push. Never `git push` with no refspec while upstream is `origin/dev`, `origin/main`, or `origin/master`. If git suggests `git push origin HEAD:dev`, `HEAD:main`, or `HEAD:master`, do not run it.

### 4. Ask whether to draft and publish

After a successful push, continue to the full draft when whole-stack publishing is already authorized. Otherwise ask the [draft and publish question](shipping-templates.md#questions-and-announcements) and wait:

- Declined: return the branch and remote URL.
- Draft only: show it in chat and stop.
- Approved: continue to the full draft.

### 5. Draft the PR

Build the title and body from the commits, diff, ticket, and locked type with the [body template](shipping-templates.md#body-template) and [title shape](shipping-templates.md#pr-title-and-body). Keep **How to QA** concrete: paths, roles, clicks, commands, and checkable outcomes in every step.

Show the complete title and body, then ask the publish question unless whole-stack publishing is already authorized.

### 6. Publish

On approval or explicit whole-stack publishing authorization, create or update the PR with the [write path](#create-or-update-the-pr). Return the PR URL. Leave Linear comments and ticket status alone.

## Out of scope for shipping

- Implementing product work inside this shipping procedure. A whole-stack build may alternate its build lifecycle and shipping for successive children
- Browser checks, screenshots, walkthrough recordings, review canvases, and per-state UI checks (that is `/verification`, before shipping)
- Committing binaries into the repo to "attach" a demo

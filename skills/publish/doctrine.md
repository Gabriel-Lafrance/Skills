# Publish Doctrine

Publish local work only. This skill is standalone-only, never runs under `/goal`, and never writes tracker issues. Use `/write-ticket` to create or refine an issue.

**Ask style:** [../pack-shared/asking.md](../pack-shared/asking.md). Templates and question batches: [reference.md](reference.md).

## Core rules

- Lock exactly one type: `feature`, `tweak`, `bug`, or `refactor`.
- Use the branch naming contract in [reference.md](reference.md).
- Do not auto-commit, force-push, or push to the default branch.
- Show the complete PR title and body before `gh pr create`; wait for explicit approval.
- A linked ticket is required when known or detectable. Do not invent one.

## Inputs

| Input | Handling |
| --- | --- |
| Linear ID or URL | Use that ticket; load its title when useful |
| GitHub issue ID or URL | Use that issue; load its title when useful |
| Type named by user | Pre-lock it, then confirm if ambiguous |
| Correct branch already exists | Reuse it |
| “Don't push” or “local only” | Create or rename the branch only |

## Process

### 1. Inspect git

In parallel, inspect `git status`, current branch, remotes/default base, commits ahead of base, and diff summary.

| State | Action |
| --- | --- |
| No `gh` or not authenticated | Stop before PR; branch and push may still proceed if remotes work |
| Dirty tree | Ask commit first, stash, or abort; never auto-commit |
| No commits ahead of base | Stop; there is nothing to publish |
| Detached HEAD | Create a real branch before continuing |

### 2. Lock type and ticket

Use the Question batch in [reference.md](reference.md) unless both are already clear. If no ticket exists, ask once whether to use a descriptive `no-ticket` branch or stop and create a ticket first. Recommend `/write-ticket` when the work belongs on a tracker.

### 3. Branch and push

1. Build `{type}/{ticket}-{slug}` from the locked values.
2. Announce the branch in a Locked block from [reference.md](reference.md).
3. Create, rename, or reuse the branch. Only rename a disposable local branch that already holds the intended commits.
4. Unless the user asked for local-only work, push with `git push -u origin HEAD`.
5. Never force-push or push to `main`/`master`.

### 4. Ask whether to draft and publish

After a successful push, use the draft/publish Question batch in [reference.md](reference.md). Wait:

- Declined: return the branch and remote URL.
- Draft only: show it in chat and stop.
- Approved: continue to the full draft.

### 5. Draft the PR

Build the title and body from the commits, diff, ticket, and locked type. Use the type template in [reference.md](reference.md). Keep **How to QA** concrete: paths, roles, clicks, commands, and checkable outcomes.

Show the complete title and body, then use the publish-approval Question batch. Never create a PR silently.

### 6. Publish

On approval only, use the heredoc command in [reference.md](reference.md). Return the PR URL. Do not write Linear comments or change ticket status.

## Failures

| Problem | Action |
| --- | --- |
| Dirty tree | Ask commit, stash, or abort; never auto-commit |
| Push rejected | Show the remote error; do not force-push |
| `gh` missing or unauthenticated | Stop before PR with install/auth guidance |
| PR already open | Return its URL; ask whether to update the body or stop |
| Unknown type | Lock it before branching |

## Anti-patterns

- Invoking under `/goal` or inventing a flow twin.
- Creating a PR before draft and approval.
- Empty QA instructions.
- Labeling a defect, standalone capability, or structural cleanup as a Tweak.
- Turning a Tweak or Refactor into the wrong PR template.
- Implementing new product work instead of shipping existing work.

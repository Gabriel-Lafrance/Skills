# Publish doctrine

## Job

Publish local work only. This skill is a user start, never runs under `/task`, and never writes tracker issues. Use `/write-ticket` to create or refine an issue.

## Owns

Type lock, branch naming contract, no auto-commit / no force-push, draft-before-create, Change diagram, and failure handling.

## Does not own

- Numbered how-to: [`reference.md`](reference.md#process) · [`SKILL.md`](SKILL.md)
- Screenshots, canvas, create-tool choice: [pr-ship.md](../pack-shared/pr-ship.md)
- Taste and architecture bars: cite `taste:*` and `architecture:*`

## Cite keys

none (uses `taste:*` and `architecture:*`)

## Bars

**Ask style:** [../pack-shared/asking.md](../pack-shared/asking.md). Templates and question batches: [reference.md](reference.md).

**Must read:** [../pack-shared/standards.md](../pack-shared/standards.md), then `/taste` and `/architecture` doctrines this turn so the Change diagram and QA describe the real structure. Read [../pack-shared/pr-ship.md](../pack-shared/pr-ship.md) before creating or updating a PR. That contract applies to **every** agent that opens a PR, not only this skill.

- Lock exactly one type: `feature`, `tweak`, `bug`, `refactor`, `chore`, or `hotfix`.
- Use the branch naming contract in [reference.md](reference.md).
- Do not auto-commit, force-push, or push to the default branch.
- Show the complete PR title and body before creating the PR; wait for explicit approval.
- Every PR body includes a high-level Mermaid **Change diagram** (one for new work; Before/After for rework) per [reference.md](reference.md).
- Follow [pr-ship.md](../pack-shared/pr-ship.md): Browser screenshots in the body when the change is visual (not a UI test pass), a Cursor review canvas for non-trivial PRs, and Cursor’s pull-request tool when it exists (do not fall back to `gh pr create` in that session).
- A linked ticket is required when known or detectable. Do not invent one.

When `/just-do-it` reads this doctrine for its preflight and templates, its explicit autonomous parent instruction replaces the approval wait only after it has printed the complete draft in chat. It still follows [pr-ship.md](../pack-shared/pr-ship.md). This approval exception does not apply to `/publish` when the user invoked it directly.

### Inputs

| Input | Handling |
| --- | --- |
| Linear ID or URL | Use that ticket; load its title when useful |
| GitHub issue ID or URL | Use that issue; load its title when useful |
| Type named by user | Pre-lock it, then confirm if ambiguous |
| Correct branch already exists | Reuse it |
| “Don't push” or “local only” | Create or rename the branch only |

## Output

| Problem | Action |
| --- | --- |
| Dirty tree | Ask commit, stash, or abort; never auto-commit |
| Push rejected | Show the remote error; do not force-push |
| `gh` missing or unauthenticated | Stop before PR with install/auth guidance unless Cursor’s pull-request tool can create it |
| PR already open | Return its URL; ask whether to update the body or stop |
| Unknown type | Lock it before branching |

## Apply

Run the [process](reference.md#process). Keep **How to QA** concrete: paths, roles, clicks, commands, and checkable outcomes.

## Anti-patterns

- Invoking under `/task`
- Creating a PR before draft and approval
- Empty QA instructions
- Shipping a PR without a Mermaid Change diagram (unless Notes explain a typo-only exception)
- Shipping a visual change without a screenshot when Browser was available, or a non-trivial PR without a review canvas, or using `gh pr create` when Cursor’s pull-request tool is available
- Running a full UI test loop just to fill Demo
- Labeling a defect, standalone capability, or structural cleanup as a Tweak
- Labeling urgent production breakage as Bug when Hotfix fits, or routine defects as Hotfix
- Labeling product tweaks, refactors, or defects as Chore
- Turning a Tweak, Refactor, Chore, or Hotfix into the wrong PR template
- Implementing new product work instead of shipping existing work

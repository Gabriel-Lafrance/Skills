# Shipping

Any agent that cuts a branch or opens a pull request follows this section. There is no `/publish` skill.

**Branch name:** `{type}/{ticket}-{slug}`

| Type | Use when |
| --- | --- |
| `feature` | New capability or intentional enhancement |
| `tweak` | Small bounded intentional adjustment |
| `bug` | A defect, including an urgent production defect |
| `refactor` | Structural change with behavior preserved |
| `chore` | Deps, CI, tooling, docs-only, repo hygiene |

- The type matches the ticket kind.
- `ticket` is the Linear id (`IN-1234`) or the GitHub issue number (`42`).
- `no-ticket` only when the user explicitly says there is no ticket.
- `slug` is a lowercase verb phrase. No spaces or colons. Keep the name under about 60 characters.
- Examples: `bug/IN-1234-fix-checkout-total`, `feature/ENG-99-add-invite-flow`.

**Hard rules**

- Do not auto-commit, force-push, or push `dev`, `main`, `master`, or the default branch.
- A new branch is a standalone ref. Cut it with `git switch --detach <base-sha>`, then `git switch -c <new-branch>` (or `git switch --no-track -c`). It must not track `origin/dev`, `origin/main`, or `origin/master`. Push only `HEAD:refs/heads/<new-branch>`. If `@{upstream}` is `origin/dev`, `origin/main`, or `origin/master`, stop.
- Show the complete pull request title and body, and wait for approval before creating it.
- Body: type, ticket, what changed, Mermaid Change diagram (Before/After for rework), How to QA, Notes. No screenshots, no canvas, no browser.
- Do not invent a ticket. Use `/write-ticket` when the work belongs on a tracker.
- Before a push that opens a PR, or a commit or push on a branch that already has an open PR, run the CI mirror in `pack-shared/pr-ship.md`. Push once it is green. A local commit you are not pushing, while no PR is open, does not run that suite. Do not invent a suite when the repo has no workflow and no lint or test script. Never `--no-verify` unless the user asked.
- Use the harness pull-request tool when it has one. Otherwise use `gh` as `pr-ship.md` describes. Do not use `gh` in a session that already has a pull-request tool.

Templates, questions, and the branch-cut steps: `pack-shared/ship.md`. Create tool and CI mirror: `pack-shared/pr-ship.md`.


# Tooling

Follow the repo's ESLint and Prettier configs when they exist. This pack installs no ESLint, Prettier, or editor files, and pastes no style guide into chat.

- If the repo's ESLint config already bans the em dash, en dash, and horizontal bar, keep that rule on. If it caps cyclomatic complexity at 5, keep the cap and split the function.
- Put editor workspace files in `.vscode/extensions.json` and `.vscode/settings.json` only.
- CI and the user's running terminals own the per-slice check loop ([Verify terminals first](#verify-terminals-first)), so skip `eslint`, `tsc`, and full suites after each slice.
- **Before a push that opens or updates a PR:** run the [CI mirror](shipping.md#ci-mirror) in this environment, then push once. A local commit with no open PR and no push does not run that suite. If there is no workflow and no lint or test script, say so. Never `git commit --no-verify` unless the user asked.
- Run lint or format when the user asked, when a named review finding requires it, or when you just added the config and need one smoke check.
- Format only files you already had to touch, unless the user asked for a repo-wide format.
- Never overwrite an existing `eslint.config.*`, Prettier config, or `.vscode/settings.json` without asking.

## Verify terminals first

`quality:verify-terminals-first`. The frontend dev server and `npx convex dev` are usually already running. While coding, read those terminals. The suite runs once before a push that opens or updates a PR ([CI mirror](shipping.md#ci-mirror)).

In order:

1. Read existing terminal output (the IDE terminals folder, running `convex dev` and frontend logs) for push success, compile errors, HMR, and runtime stacks.
2. Check the diff and structure of the change.
3. If terminals are silent or missing, say so, then ask or start the **minimal** command once.

Read terminals instead of running these by default:

- Convex MCP (`status`, `data`, `tables`, `logs`, `run`, `runOneoffQuery`, `insights`, `functionSpec`, env tools) just to verify.
- `npx convex`, deploy, or codegen after every slice while `convex dev` is watching.
- `eslint`, `tsc --noEmit`, `npm run lint`, or full suites while coding a slice. Run the CI mirror once, right before a push that opens a PR or updates an open one.
- A second frontend or Convex process when one is already up, or a pass whose only job is MCP verification.

Use Convex MCP or deeper checks only when:

- terminals show an error you cannot diagnose from the log,
- the user asked for a one-off data read or explicit MCP, dashboard, or CLI verification,
- a [`/verification`](../verification/SKILL.md) run needs them, or
- no Convex terminal exists and you said so first.

Cite evidence as `terminals/3.txt: convex push ok` (terminal file, then what it showed), not a fresh MCP round-trip.

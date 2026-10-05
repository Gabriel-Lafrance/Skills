# Tooling

Follow the repo's ESLint and Prettier configs when they exist. This pack installs no ESLint, Prettier, or editor files, and pastes no style guide into chat.

- If the repo's ESLint config already bans the em dash, en dash, and horizontal bar, keep that rule on. If it caps cyclomatic complexity at 5, keep the cap and split the function.
- Put editor workspace files in `.vscode/extensions.json` and `.vscode/settings.json` only.
- Reuse current terminal evidence ([Verify terminals first](#verify-terminals-first)) and run focused existing tests/lint/type checks when they establish the changed behavior. Select scope under [verification scope](execution.md#verification-scope); broaden for shared/high-risk impact or an explicit full request.
- **Before a push that opens or updates a PR:** apply [CI mirror](shipping.md#ci-mirror) for applicable scoped and mandatory local checks, then track required remote CI. Local commits and clean Git sync do not trigger full suites merely because a PR exists. Preserve hooks and required checks; report missing commands/evidence.
- Run lint or format when the user asked, when a named review finding requires it, or when you just added the config and need one smoke check.
- Format only files you already had to touch, unless the user asked for a repo-wide format.
- Never overwrite an existing `eslint.config.*`, Prettier config, or `.vscode/settings.json` without asking.

## Verify terminals first

`quality:verify-terminals-first`. The frontend dev server and `npx convex dev` may already be running. Read relevant terminals before starting duplicate processes or checks. Shipping uses [CI mirror](shipping.md#ci-mirror); pure Git sync uses [Git sync only](execution.md#git-sync-only).

In order:

1. Read existing terminal output (the IDE terminals folder, running `convex dev` and frontend logs) for push success, compile errors, HMR, and runtime stacks.
2. Check the diff and structure of the change.
3. If terminals are silent or missing, say so, then ask or start the **minimal** command once.

Read terminals instead of running these by default:

- Convex MCP (`status`, `data`, `tables`, `logs`, `run`, `runOneoffQuery`, `insights`, `functionSpec`, env tools) just to verify.
- `npx convex`, deploy, or codegen after every slice while `convex dev` is watching.
- Unrelated full lint/type/test runs after every slice. Relevant focused checks remain allowed; use a full command when impact, requested scope, or required repository gates justify it.
- A second frontend or Convex process when one is already up, or a pass whose only job is MCP verification.

Use Convex MCP or deeper checks only when:

- terminals show an error you cannot diagnose from the log,
- the user asked for a one-off data read or explicit MCP, dashboard, or CLI verification,
- a [`/verification`](../verification/SKILL.md) run needs them, or
- no Convex terminal exists and you said so first.

Cite evidence as `terminals/3.txt: convex push ok` (terminal file, then what it showed), not a fresh MCP round-trip.

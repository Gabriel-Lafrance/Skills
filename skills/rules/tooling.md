# Tooling

Do **not** paste a style guide into chat. If this repo already has ESLint or Prettier, **follow those configs**.

- Add or change lint/format tooling with `/setup-toolkit` after the user says yes to that phase. Do not invent a parallel config.
- The toolkit ESLint baseline includes `no-emdash/no-emdash` (em dash, en dash, horizontal bar) and the `complexity` cap of 5. Keep both on. Do not disable the dash rule to "make the prose look fancy," and do not raise the cap: split the function.
- Editor workspace files live in `.vscode/extensions.json` and `.vscode/settings.json`. Do not add a parallel `.cursor/extensions.json`.
- Do **not** ritual-run `eslint`, `tsc`, or full suites after every slice. CI and the user's running terminals own that loop ([Verify terminals first](#verify-terminals-first)).
- **Before a push that opens or updates a PR:** run the [CI mirror](shipping.md#ci-mirror) in this environment, then push once. A local commit with no open PR and no push does not run that suite. If there is no workflow and no lint or test script, say so. Never `git commit --no-verify` unless the user asked.
- Run lint or format when the user asked, when a named review finding requires it, or when you just added the config and need one smoke check.
- Do not reformat the whole tree as a drive-by. Format only files you already had to touch, unless the user asked for a repo-wide format.
- Never overwrite an existing `eslint.config.*`, Prettier config, or `.vscode/settings.json` without asking.

## Verify terminals first

`quality:verify-terminals-first`. The frontend dev server and `npx convex dev` are usually already running. While coding, read those terminals. The suite runs once before a push that opens or updates a PR ([CI mirror](shipping.md#ci-mirror)).

In order:

1. Read existing terminal output (the IDE terminals folder, running `convex dev` and frontend logs) for push success, compile errors, HMR, and runtime stacks.
2. Check the diff and structure of the change.
3. Only if terminals are silent or missing: say so, then ask, or start the **minimal** command once.

Do not, by default:

- Call Convex MCP (`status`, `data`, `tables`, `logs`, `run`, `runOneoffQuery`, `insights`, `functionSpec`, env tools) just to verify.
- Re-run `npx convex`, deploy, or codegen after every slice while `convex dev` is watching.
- Run `eslint`, `tsc --noEmit`, `npm run lint`, or full suites while coding a slice. Run the CI mirror once, right before a push that opens a PR or updates an open one.
- Start a second frontend or Convex process when one is already up, or run a pass whose only job is MCP verification.

Use Convex MCP or deeper checks only when terminals show an error you cannot diagnose from the log, the user asked for a one-off data read or explicit MCP, dashboard, or CLI verification, or no Convex terminal exists and you said so first.

Cite evidence as `terminals/3.txt: convex push ok` (terminal file, then what it showed), not a fresh MCP round-trip.

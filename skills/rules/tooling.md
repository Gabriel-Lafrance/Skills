# Tooling

Follow the repo's ESLint and Prettier configs when they exist. This pack installs no ESLint, Prettier, or editor files, and pastes no style guide into chat.

## Harness-first discovery

A hand-built route (a Playwright script, `curl` against an API, `open`, a
screenshot script, a scraped CLI, a new package) is the fallback, never the
first move. Before any route that reaches outside the code:

1. **Search the harness for the job** (browser, preview, screenshot, PR, CI,
   logs, deploy, database, ticket, docs, other agent, thread, secret): the
   tools listed this turn, deferred tool names in system reminders (load
   matches through the supported loader, in Claude Code `ToolSearch` with a
   keyword such as `preview`), the MCP servers listed this session including
   ones still connecting, and the skills listing.
2. **Use the most direct match** over a script that does the same thing.
3. **Fall back only with a named gap:** no matching tool, unsupported
   operation, tool error, or permission boundary. Say the gap in one line, then
   use the simplest permitted fallback or report the blocker.

Do this once per job per session and reuse the result; search again after a
tool error or capability mismatch. Never invent tool names or fields, or guess
a tool from an upstream example.

**Browser.** When the user asks to open, view, click through, record or screenshot a page, use the harness's preview or browser tool, within its own limits on when preview is allowed. Public source research uses permitted fetch or search, not a browser. In T3 Code, open [t3-code.md](t3-code.md#browser-and-preview).

Availability is not permission. Honor explicit user tool choices and access
restrictions, and never bypass a denial through another interface. Do not
globally ban Playwright: keep repository-owned Playwright E2E, required CI, and
explicit user tool choices. A browser inspection cannot replace those suites.

For web startup or preview debugging, follow
[accessible development-server logs](dev-server-logs.md).

## Repository tooling

- If the repo's ESLint config already bans the em dash, en dash, and horizontal bar, keep that rule on. If it caps cyclomatic complexity at 6 or lower, keep the cap and split the function.
- Put editor workspace files in `.vscode/extensions.json` and `.vscode/settings.json` only.
- Run lint or format only when the user asked, a named review finding requires it, or you just added the config and need one smoke check, and only on files you had to touch unless the user asked for a repo-wide format.
- Never overwrite an existing `eslint.config.*`, Prettier config, or `.vscode/settings.json` without asking.

## Verify terminals first

`quality:verify-terminals-first`. Read relevant terminals before starting duplicate processes or checks. Shipping uses [CI mirror](shipping.md#ci-mirror); pure Git sync uses [Git sync only](execution.md#git-sync-only). A Convex repo (a `convex/` folder exists) also applies [convex.md](convex.md#terminals).

In order:

1. Read existing terminal output (the IDE terminals folder, running backend and frontend logs) for push success, compile errors, HMR, and runtime stacks.
2. If terminals are silent or missing, say so, then ask or start the **minimal** command once.

Read terminals instead of running these by default:

- Backend MCP or CLI calls just to verify.
- Deploy or codegen after every slice while a watcher is running.
- Unrelated full lint/type/test runs after every slice ([verification scope](execution.md#verification-scope)).
- A second frontend or backend process when one is already up, or a pass whose only job is MCP verification.

Use MCP or deeper checks only when:

- terminals show an error you cannot diagnose from the log,
- the user asked for a one-off data read or explicit MCP, dashboard, or CLI verification,
- a [`/verification`](../verification/SKILL.md) run needs them, or
- no backend terminal exists and you said so first.

Cite evidence as the terminal file, then what it showed, not a fresh MCP round-trip.

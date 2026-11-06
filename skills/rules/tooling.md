# Tooling

Follow the repo's ESLint and Prettier configs when they exist. This pack installs no ESLint, Prettier, or editor files, and pastes no style guide into chat.

## Harness-first discovery

The ADE (T3 Code, Claude Code, Codex, Cursor) and its MCP servers usually
already have a tool for the job. A hand-built route (a Playwright script, `curl`
against an API, `open`, a screenshot script, a scraped CLI, a new package) is
the fallback, never the first move.

Before any route that reaches outside the code:

1. **Name the job** in one or two words: browser, preview, screenshot, PR,
   CI, logs, deploy, database, ticket, docs, other agent, thread, secret.
2. **Search the harness for it.** Scan the tools listed this turn, then the
   deferred tool names in system reminders, and load matches through the
   supported loader (in Claude Code, `ToolSearch` with the keyword, such as
   `preview` or `pull request`). Check the MCP servers listed this session,
   including ones still connecting, and the skills listing.
3. **Use the most direct match.** One tool call beats a script that does the
   same thing. Follow the harness's own instructions for that tool.
4. **Fall back only with a named gap:** no matching tool, unsupported
   operation, tool error, or permission boundary. Say the gap in one line, then
   use the simplest permitted fallback or report the blocker.

Do this once per job per session and reuse the result; search again after a
tool error or capability mismatch. Never invent tool names or fields, and never
guess a tool from an upstream example.

**Browser in T3 Code.** When the user asks to open, view, click through, record
or screenshot a page, use T3's `preview_*` tools (load them first if deferred),
not Playwright, the system browser or a screenshot script. Follow T3's installed
instructions on when preview is allowed; where they forbid preview unasked, for
example to check your own edit, that limit stands. Public source research uses
permitted fetch or search, not a browser.

Availability is not permission. Honor explicit user tool choices and access
restrictions, and never bypass a denial through another interface. Do not
globally ban Playwright: keep repository-owned Playwright E2E, required CI, and
explicit user tool choices. A browser inspection cannot replace those suites.

For web startup or preview debugging, use
[accessible development-server logs](dev-server-logs.md): reuse services,
capture actual output, prefer native terminals, and offer an OS-aware log-only
viewer or remote fallback when needed. Opening logs never restarts the app.

## Repository tooling

- If the repo's ESLint config already bans the em dash, en dash, and horizontal bar, keep that rule on. If it caps cyclomatic complexity at 6 or lower, keep the cap and split the function.
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

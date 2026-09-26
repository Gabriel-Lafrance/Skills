# Setup toolkit doctrine

## Job

Put this pack and the `AGENTS.md` contract onto the machine. Phase one verifies what is already installed, then writes skills and the contract to **this repo** (the default) or **user level** (or both) after one question. ESLint and Prettier are a later, opt-in phase. The install stays harness-agnostic: one contract file, `AGENTS.md`, plus a one-line pointer for any harness that reads a different filename.

## Owns

Verifying current installs, installing or updating the rest of this pack with `npx skills`, installing `AGENTS.md` and the harness pointer lines, which lint templates to copy, what not to overwrite, Convex plugin detection, the smoke check, and whether to start `/design` Initialization when `docs/design.md` is missing after they opted into lint.

## Does not own

- Rewriting an existing lint stack
- Reformatting the repo as part of setup
- Writing `.cursor/rules` or any `.mdc` file (Cursor reads `AGENTS.md`)
- Creating a harness home the user does not have
- Behavior-lock tests (`/create-test`)
- The design file contents or code-derived route inventory: [`../design/doctrine.md`](../design/doctrine.md)
- Detect and choose details: [`reference.md`](reference.md)

## Cite keys

none (uses `taste:*` and `architecture:*`)

## Bars

1. **Verify, then ask, then install.** Look up skill roots, `AGENTS.md`, and harnesses in use first. Print those facts. Then one Questions batch: scope (this repo, this repo and user level, or user level only) and, when a `package.json` exists, whether to add ESLint and Prettier. Wait. Follow [asking.md](../pack-shared/asking.md).
2. **Pack first.** For each chosen scope, install the pack when `rules/code-quality.md` is missing, and update a stale copy (pack skills present, `rules/code-quality.md` missing) with the commands in [reference.md](reference.md#pack-skills). Skip when this workspace is the Skills pack.
3. **One contract, pointers elsewhere.** The repo gets `AGENTS.md`. A harness that reads another filename gets one pointer line ([reference.md](reference.md#harness-files)). User level points each installed harness at the installed template instead of copying it ([reference.md](reference.md#user-level)).
4. **Never overwrite someone else's instructions file.** A file is the pack's only when it contains `gabriel-skills-agents`. Every other `AGENTS.md`, `CLAUDE.md`, or `GEMINI.md` only gets a line or short section appended. Report it.
5. **Never create a harness home** (`~/.claude`, `~/.codex`, `~/.gemini`, and the rest) for a harness that is not installed.
6. **Fail fast on lint setup** if they said yes to lint and there is no `package.json` at the workspace root (or the app root the user named). Phase one still stands.
7. **Never overwrite** an existing ESLint or Prettier config, ignore file, `.vscode/settings.json`, or a script that already exists. Report what you skipped. `.vscode/extensions.json` may be merged (add missing recommendation IDs only).
8. **One stack.** Templates in [templates/](templates/) only: ESLint with the no-emdash plugin (plus Convex when detected), Prettier, and `.vscode/`. Detect which ESLint template fits; do not ask the user facts the repo already answers.
9. **No ritual lint or reformat.** One smoke command after install (`npx eslint --version`). Full `lint` or `format` only if the user asked.
10. Talk in ordinary words. Cite principles as **plain (Classic)**, for example `fail fast (Fail Fast)` (`taste:plain-language`).

## Output

For the scopes they chose:

- Pack skills in the user skill home, the project skill home, or both
- Workspace-root `AGENTS.md` (a foreign file keeps its text and gets a pointer section)
- A pointer line in `CLAUDE.md`, `GEMINI.md`, or the matching file for each harness in use
- User level: existing harness homes pointed at the installed template, or reported skipped. Cursor has no user-level file; the repo install covers it
- No new harness home folder
- A report of every file written, refreshed, appended, symlinked, copied, or skipped, with the reason

If they said yes to lint, the app has:

- `eslint.config.mjs` (flat config) **or** the existing ESLint config left untouched
- `eslint-plugin-no-emdash.mjs` next to that config (bans em dash, en dash, and horizontal bar)
- `prettier.config.mjs` and `.prettierignore` **or** the existing Prettier config left untouched
- `.vscode/extensions.json` recommending the ESLint and Prettier extensions (IDs merged if the file exists)
- `.vscode/settings.json` for format-on-save and ESLint **or** the existing settings left untouched
- `package.json` scripts `lint`, `lint:fix`, `format`, and `format:check` when those names are free
- Dev dependencies installed with the repo's package manager
- `/design` Initialization started when `docs/design.md` was missing (or reported skipped)

## Apply

Verify first ([reference.md](reference.md#verify)). Ask scope and lint ([reference.md](reference.md#questions)). Wait. Install the pack and `AGENTS.md` only for the chosen scopes. Write lint configs next to the app `package.json` only if they said yes. Do not invent `services/lint/` or a wrapper package unless this repo already publishes shareable configs that way.

If the repo already has a working lint and format setup, fill only missing pieces (no-emdash plugin file, `.vscode` recommendations, Prettier if missing). Do not edit their ESLint config. Print the import line if it does not already include `noEmdashConfig`.

## Anti-patterns

- Overwriting an `AGENTS.md`, `CLAUDE.md`, or `GEMINI.md` that lacks `gabriel-skills-agents`
- Creating `~/.claude`, `~/.cursor`, `~/.codex`, or `~/.gemini` when that harness is not installed
- Copying the contract into each harness home instead of pointing at the installed template
- Writing a Cursor `.mdc` rule or `.cursor/rules` copy of the contract
- Overwriting a working ESLint or Prettier config, or an existing `docs/design.md`
- Ritual-linting or reformatting the whole tree as setup
- Asking the user facts the repo already answers
- Writing tests as setup
- Copying only lint files and leaving the rest of this pack uninstalled
- Copying ESLint or Prettier before they said yes
- Writing to a scope they did not choose
- Telling the user to hunt the skills.sh leaderboard instead of `npx skills add gabriel-lafrance/skills@setup-toolkit`

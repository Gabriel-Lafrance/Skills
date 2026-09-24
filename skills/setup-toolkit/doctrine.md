# Setup toolkit doctrine

## Job

Put this pack and the `AGENTS.md` contract onto the machine. Phase one verifies what is already installed, then writes skills and the contract to the **repo** or to **user data** (or both) after one question. ESLint, Prettier, and quality gates are a later, opt-in phase. The pack repo stays harness-agnostic. This skill is the skills.sh installer. Cursor plugins cannot run ESLint or Prettier for a project that has no config.

## Owns

Which templates to copy, what not to overwrite, verifying current installs, installing the rest of this pack with `npx skills` into the chosen scope, installing the pack `AGENTS.md` into the chosen destinations, Convex plugin detection, the quality-gate tests (`test:quality`), the mutant check (`test:mutants`), the smoke check, and whether to start `/design` Initialization when `docs/design.md` is missing after they opted into lint.

## Does not own

- Rewriting an existing lint stack
- Reformatting the repo as part of setup
- Writing `.cursor/rules`, any `.mdc` file, or a Cursor `hooks.json` (Cursor reads `AGENTS.md`)
- Adding a project `CLAUDE.md` (Claude Code then skips `AGENTS.md`)
- Creating a harness home the user does not have
- Behavior-lock tests (`/create-test`)
- A keep-jobs-apart (SoC) import denylist
- The design file contents or code-derived route inventory: [`../design/doctrine.md`](../design/doctrine.md)
- Detect/choose details: [`reference.md`](reference.md)

## Cite keys

none (uses `taste:*` and `architecture:*`)

## Bars

1. **Verify, then ask, then install.** Look up skill roots, `AGENTS.md`, and harness homes first. Print those facts. Then one Questions batch: destination (repo, user data, or both) and, when a `package.json` exists, whether to add ESLint, Prettier, and quality gates. Wait. Do not copy lint files on `no`. Follow [asking.md](../pack-shared/asking.md).
2. **Pack first.** For each chosen destination, if that scope is missing `pack-shared`, install the rest of this pack with the command in [reference.md](reference.md#pack-skills). Skip when this workspace is the Skills pack. Then install `AGENTS.md` only for the chosen destinations. The repo copy is the full file. Claude is one `@` import of the installed template. Codex is a symlink to that template, and a byte copy only when the symlink cannot be created (say so in that case). Gemini CLI and Aider keep their rows. The contract step does not need `package.json`. Refresh the repo copy only when it is missing or already contains `gabriel-skills-agents`. Leave a different `AGENTS.md` in place and say so. Do not create a harness directory that is not installed. Do not write `~/.claude/gabriel-skills/AGENTS.md`. Do not write a Cursor `hooks.json`. Delete `gabriel-skills/follow-agents.mdc` when that old pointer is already on disk (user home when they chose user data, app `.cursor/rules` when they chose the repo). Leave every other Cursor rule and hook alone.
3. **Fail fast on lint setup** if they said yes to lint and there is no `package.json` at the workspace root (or the obvious app root the user named). ESLint and Prettier belong in JS/TS apps, not in this markdown pack itself. Phase one still stands.
4. **Never overwrite** an existing ESLint or Prettier config, ignore file, `.vscode/settings.json`, `complexity.test.mjs`, `cyclomatic-cap.mjs`, `principle-gate.test.mjs`, `principle-scan.mjs`, `knip.json`, `knip.test.mjs`, `stryker.conf.json`, or a script that already exists. Report what you skipped. `.vscode/extensions.json` may be merged (add missing recommendation IDs only).
5. **One stack.** Templates in [templates/](templates/) only. Do not add extra ESLint plugins beyond no-emdash and Convex when detected. The cyclomatic cap is ESLint’s built-in `complexity` rule plus the quality-gate test, not a third plugin. Quality tooling is ESLint, Prettier, Knip, and Stryker from templates. Do not swap in a different dead-code or mutation runner. Do not add a UI import denylist for keep jobs apart (SoC). Do not raise a cap, skip a gate, or delete a gate to go green (`taste:cyclomatic-cap`, `taste:fail-fast`, `taste:types-tell-the-truth`, `taste:trust-the-server`, `taste:no-dead-code`, `taste:kill-the-mutants`).
6. **Detect, then choose the matching template** (see [reference.md](reference.md)). Do not ask the user facts the repo already answers. Convex-only principle checks run only when `convex/` exists. The Knip gate runs only when its config exists. Stryker uses the TypeScript-checker template when `tsconfig.json` exists.
7. **Do not ritual-lint the whole tree** after install. One smoke command is enough (`npx eslint --print-config eslint.config.mjs` or `package-manager exec eslint --version`). Full `lint` only if the user asked. Do not run `test:quality` or `test:mutants` as setup smoke: on an existing messy codebase they are supposed to fail until functions are split, types/errors/auth are honest, dead code is removed, and locks bite.
8. **Do not reformat the repo** as part of setup. Leave `format` for the user.
9. Convex ESLint plugin **only** when `convex/` exists (or `@convex-dev/eslint-plugin` is already a dependency).
10. Talk in ordinary words. Gate failures and chat use **plain (Classic)** — `fail fast (Fail Fast)`. Do not dump pack nicknames (`taste:plain-language`).

## Output

The machine and the app have, for the destinations they chose:

- Pack skills in the user-level skill home, the project skill home, or both
- Workspace-root `AGENTS.md` when they chose the repo (a different file is left in place)
- When they chose user data: Claude `@` import of the installed template, Codex symlink to that template (template bytes copied and reported only if the symlink could not be created), Gemini setting, Aider `read`, or reported skipped. Cursor has no user-home row: the repo `AGENTS.md` is its contract
- No new harness home directory, and no new project `CLAUDE.md`
- No ESLint, Prettier, or quality-gate files unless they said yes to that phase

If they said yes to lint, the current workspace has:

- `eslint.config.mjs` (flat config) **or** the existing ESLint config left untouched
- `eslint-plugin-no-emdash.mjs` next to that config (bans em dash, en dash, and horizontal bar)
- `cyclomatic-cap.mjs` and `complexity.test.mjs` next to `package.json` (cyclomatic complexity (McCabe) cap 5) **or** those files left untouched
- `principle-gate.test.mjs` and `principle-scan.mjs` next to `package.json` **or** those files left untouched
- `knip.json` and `knip.test.mjs` next to `package.json` (no dead code (Knip)) **or** those files left untouched
- `stryker.conf.json` next to `package.json` (kill the mutants (Mutation testing)) **or** that file left untouched
- `prettier.config.mjs` and `.prettierignore` **or** the existing Prettier config left untouched
- `.vscode/extensions.json` recommending the ESLint and Prettier extensions (merge IDs if the file already exists)
- `.vscode/settings.json` for format-on-save and ESLint **or** the existing settings left untouched
- `package.json` scripts `lint`, `lint:fix`, `format`, `format:check`, `test:quality`, and `test:mutants` when those names are free; `test` set to the quality command only when `test` is missing
- Dev dependencies installed with the repo’s package manager
- `/design` Initialization started when `docs/design.md` was missing (or reported skipped because the file already exists)

## Apply

Verify first ([reference.md](reference.md#verify)). Ask destination and lint ([reference.md](reference.md#questions)). Wait. Install missing pack skills and `AGENTS.md` only for the chosen destinations. Write lint configs next to the app `package.json` only if they said yes. Do not invent `services/lint/` or a wrapper package unless this repo already publishes shareable configs that way.

If they said yes to lint and the repo already has a working lint/format story, **fill only missing pieces** (no-emdash plugin file, quality-gate files, `.vscode` recommendations, Prettier if missing). Do not overwrite their ESLint config. Print the import snippet if their config does not already include `noEmdashConfig` or the cyclomatic cap.

After that work, if they said yes to lint and `docs/design.md` is missing, run `/design` Initialization (`design:initialization`). Do not invent the file from this skill. If the file already exists, leave it.

## Anti-patterns

- Overwriting an app or user `AGENTS.md` that is not the pack copy
- Replacing `~/.claude/CLAUDE.md` or a project `CLAUDE.md` wholesale. On the user file, replace a stale `gabriel-skills/AGENTS.md` import with the template path, or add that one `@` line when the import is missing. Do not replace unrelated text
- Writing `~/.claude/gabriel-skills/AGENTS.md`
- Creating `~/.claude`, `~/.cursor`, `~/.codex`, or `~/.gemini` when that harness is not installed
- Writing a Cursor `.mdc` rule, `.cursor/rules` copy, or `hooks.json`
- Deleting Cursor rules or hooks other than `gabriel-skills/follow-agents.mdc`
- Adding a `CLAUDE.md` in the pack or the app
- Overwriting a working ESLint or Prettier config
- Overwriting an existing `docs/design.md`
- Ritual-linting or reformatting the whole tree as setup
- Inventing a lint service folder (`architecture:folders` still says keep the existing structure here)
- Asking the user facts the repo already answers
- Writing behavior-lock or UI tests as setup
- Raising the cyclomatic cap so an existing messy function passes
- Lowering the Stryker break threshold so surviving mutants pass
- Deleting `knip.json` so dead code passes
- Adding a keep-jobs-apart (SoC) SDK or UI import denylist
- Skipping Convex identity or clock checks by deleting `convex/` from the test instead of fixing the function
- Writing `docs/design.md` from memory instead of `/design` Initialization
- Copying only lint files and leaving the rest of this pack uninstalled when the chosen destination is missing `pack-shared`
- Copying ESLint, Prettier, or quality gates before they said yes
- Writing `AGENTS.md` to a destination they did not choose
- Telling the user to hunt the skills.sh leaderboard instead of `npx skills add gabriel-lafrance/skills@setup-toolkit`

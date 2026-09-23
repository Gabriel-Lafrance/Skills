# Setup toolkit doctrine

## Job

Put lint, format, and principle quality gates **in the app repo**, and install the pack `AGENTS.md` into that repo and into each harness home that already exists for this user. The pack repo stays harness-agnostic. This skill is the installer. Cursor plugins cannot run ESLint or Prettier for a project that has no config.

## Owns

Which templates to copy, what not to overwrite, installing the pack `AGENTS.md` into the repo and into existing harness homes, Convex plugin detection, the quality-gate tests (`test:quality`), the mutant check (`test:mutants`), and the smoke check.

## Does not own

- Rewriting an existing lint stack
- Reformatting the repo as part of setup
- Writing `.cursor/rules` or any `.mdc` file (Cursor reads `AGENTS.md`)
- Adding a project `CLAUDE.md` (Claude Code then skips `AGENTS.md`)
- Creating a harness home the user does not have
- Behavior-lock tests (`/create-test`)
- A keep-jobs-apart (SoC) import denylist
- `docs/design.md` contents or a code-derived route inventory: the App UX section of `AGENTS.md` and the designer
- Detect/choose details: [`reference.md`](reference.md)

## Cite keys

none (uses `taste:*` and `architecture:*`)

## Bars

1. **Contract first.** Install the pack `AGENTS.md` before lint setup. This step does not need `package.json`. Copy it into the repo. Then install each harness row in [reference.md](reference.md#install-agents-md) whose home already exists. Refresh a pack copy only when it is missing or already contains `gabriel-skills-agents`. Leave a different `AGENTS.md` in place and say so. Do not create a harness directory that is not installed.
2. **Fail fast on lint setup** if there is no `package.json` at the workspace root (or the obvious app root the user named). ESLint and Prettier belong in JS/TS apps, not in this markdown pack itself. The `AGENTS.md` copy still stands.
3. **Never overwrite** an existing ESLint or Prettier config, ignore file, `.vscode/settings.json`, `complexity.test.mjs`, `cyclomatic-cap.mjs`, `principle-gate.test.mjs`, `principle-scan.mjs`, `knip.json`, `knip.test.mjs`, `stryker.conf.json`, or a script that already exists. Report what you skipped. `.vscode/extensions.json` may be merged (add missing recommendation IDs only).
4. **One stack.** Templates in [templates/](templates/) only. Do not add extra ESLint plugins beyond no-emdash and Convex when detected. The cyclomatic cap is ESLint’s built-in `complexity` rule plus the quality-gate test, not a third plugin. Quality tooling is ESLint, Prettier, Knip, and Stryker from templates. Do not swap in a different dead-code or mutation runner. Do not add a UI import denylist for keep jobs apart (SoC). Do not raise a cap, skip a gate, or delete a gate to go green (`taste:cyclomatic-cap`, `taste:fail-fast`, `taste:types-tell-the-truth`, `taste:trust-the-server`, `taste:no-dead-code`, `taste:kill-the-mutants`).
5. **Detect, then choose the matching template** (see [reference.md](reference.md)). Do not ask the user facts the repo already answers. Convex-only principle checks run only when `convex/` exists. The Knip gate runs only when its config exists. Stryker uses the TypeScript-checker template when `tsconfig.json` exists.
6. **Ask** only when a real fork remains (for example two app roots, or the user asked to replace a config). Follow [asking.md](../pack-shared/asking.md).
7. **Do not ritual-lint the whole tree** after install. One smoke command is enough (`npx eslint --print-config eslint.config.mjs` or `package-manager exec eslint --version`). Full `lint` only if the user asked. Do not run `test:quality` or `test:mutants` as setup smoke: on an existing messy codebase they are supposed to fail until functions are split, types/errors/auth are honest, dead code is removed, and locks bite.
8. **Do not reformat the repo** as part of setup. Leave `format` for the user.
9. Convex ESLint plugin **only** when `convex/` exists (or `@convex-dev/eslint-plugin` is already a dependency).
10. Talk in ordinary words. Gate failures and chat use **plain (Classic)** — `fail fast (Fail Fast)`. Do not dump pack nicknames (`taste:plain-language`).

## Output

The machine and the app have:

- Workspace-root `AGENTS.md` copied from the pack when missing or already marked `gabriel-skills-agents` (a different file is left in place)
- Each existing harness home updated in that harness's own instruction file (Claude import, Codex `AGENTS.md`, Gemini setting, Aider `read`), or reported skipped. Cursor is covered by the repo `AGENTS.md`
- No new harness home directory, and no new project `CLAUDE.md`

The current workspace has:

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
- `docs/design.md` left untouched

## Apply

Copy the pack `AGENTS.md` first ([reference.md](reference.md#install-agents-md)). Then write configs next to the app `package.json`. That is the normal home for ESLint and Prettier. Do not invent `services/lint/` or a wrapper package unless this repo already publishes shareable configs that way.

If the repo already has a working lint/format story, **fill only missing pieces** (no-emdash plugin file, quality-gate files, `.vscode` recommendations, Prettier if missing). Do not overwrite their ESLint config. Print the import snippet if their config does not already include `noEmdashConfig` or the cyclomatic cap.

Do not write `docs/design.md` from this skill. If the file is missing, the designer writes a short Do / Don't list from the routes in code before UI work. If the file already exists, leave it.

## Anti-patterns

- Overwriting an app or user `AGENTS.md` that is not the pack copy
- Replacing `~/.claude/CLAUDE.md` or a project `CLAUDE.md` instead of appending one import line
- Creating `~/.claude`, `~/.cursor`, `~/.codex`, or `~/.gemini` when that harness is not installed
- Writing a Cursor `.mdc` rule or `.cursor/rules` copy of the contract
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
- Writing `docs/design.md` from this skill

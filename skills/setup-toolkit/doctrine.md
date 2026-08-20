# Setup toolkit doctrine

## Job

Put lint, format, and a cyclomatic quality-gate **in the app repo**. Cursor plugins cannot run ESLint or Prettier for a project that has no config. This skill copies this pack’s templates and installs the matching packages.

## Owns

Which templates to copy, what not to overwrite, Convex plugin detection, the cyclomatic quality-gate test, and the smoke check.

## Does not own

- Rewriting an existing lint stack
- Reformatting the repo as part of setup
- Plugin rules copy unless the user asks to pin them
- Behavior-lock tests (`/create-test`)
- Detect/choose details: [`reference.md`](reference.md)

## Cite keys

none (uses `taste:*` and `architecture:*`)

## Bars

1. **Fail fast** if there is no `package.json` at the workspace root (or the obvious app root the user named). ESLint and Prettier belong in JS/TS apps, not in this markdown pack itself.
2. **Never overwrite** an existing ESLint or Prettier config, ignore file, `.vscode/settings.json`, `complexity.test.mjs`, `cyclomatic-cap.mjs`, or a script that already exists. Report what you skipped. `.vscode/extensions.json` may be merged (add missing recommendation IDs only).
3. **One stack.** Templates in [templates/](templates/) only. Do not add extra ESLint plugins beyond no-emdash and Convex when detected. The cyclomatic cap is ESLint’s built-in `complexity` rule plus the quality-gate test, not a third plugin. Do not raise the cap, skip the test, or delete it to go green (`taste:cyclomatic-cap`).
4. **Detect, then choose the matching template** (see [reference.md](reference.md)). Do not ask the user facts the repo already answers.
5. **Ask** only when a real fork remains (for example two app roots, or the user asked to replace a config). Follow [asking.md](../pack-shared/asking.md).
6. **Do not ritual-lint the whole tree** after install. One smoke command is enough (`npx eslint --print-config eslint.config.mjs` or `package-manager exec eslint --version`). Full `lint` only if the user asked. Do not run the cyclomatic test as setup smoke: on an existing branchy codebase it is supposed to fail until functions are split.
7. **Do not reformat the repo** as part of setup. Leave `format` for the user.
8. Convex ESLint plugin **only** when `convex/` exists (or `@convex-dev/eslint-plugin` is already a dependency).
9. Talk in ordinary words. Do not dump pack nicknames (`taste:plain-language`).

## Output

The current workspace has:

- `eslint.config.mjs` (flat config) **or** the existing ESLint config left untouched
- `eslint-plugin-no-emdash.mjs` next to that config (bans em dash, en dash, and horizontal bar)
- `cyclomatic-cap.mjs` and `complexity.test.mjs` next to `package.json` (quality gate: max cyclomatic complexity 5) **or** those files left untouched
- `prettier.config.mjs` and `.prettierignore` **or** the existing Prettier config left untouched
- `.vscode/extensions.json` recommending the ESLint and Prettier extensions (merge IDs if the file already exists)
- `.vscode/settings.json` for format-on-save and ESLint **or** the existing settings left untouched
- `package.json` scripts `lint`, `lint:fix`, `format`, `format:check`, and `test:complexity` when those names are free; `test` set to the complexity gate only when `test` is missing
- Dev dependencies installed with the repo’s package manager

## Apply

Write configs next to the app `package.json`. That is the normal home for ESLint and Prettier. Do not invent `services/lint/` or a wrapper package unless this repo already publishes shareable configs that way.

If the repo already has a working lint/format story, **fill only missing pieces** (no-emdash plugin file, cyclomatic quality-gate files, `.vscode` recommendations, Prettier if missing). Do not overwrite their ESLint config. Print the import snippet if their config does not already include `noEmdashConfig` or the cyclomatic cap.

## Anti-patterns

- Overwriting a working ESLint or Prettier config
- Ritual-linting or reformatting the whole tree as setup
- Inventing a lint service folder (`architecture:folders` still says keep the existing structure here)
- Asking the user facts the repo already answers
- Writing behavior-lock or UI tests as setup
- Raising the cyclomatic cap so an existing messy function passes

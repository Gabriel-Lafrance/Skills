# Setup toolkit doctrine

## Job

Put lint, format, and principle quality gates **in the app repo**. Cursor plugins cannot run ESLint or Prettier for a project that has no config. This skill copies this pack’s templates and installs the matching packages.

## Owns

Which templates to copy, what not to overwrite, Convex plugin detection, the quality-gate tests (`test:quality`), the mutant check (`test:mutants`), the smoke check, and whether to start `/design` Initialization when `docs/design.md` is missing.

## Does not own

- Rewriting an existing lint stack
- Reformatting the repo as part of setup
- Plugin rules copy unless the user asks to pin them
- Behavior-lock tests (`/create-test`)
- A keep-jobs-apart (SoC) import denylist
- The design file contents or code-derived route inventory: [`../design/doctrine.md`](../design/doctrine.md)
- Detect/choose details: [`reference.md`](reference.md)

## Cite keys

none (uses `taste:*` and `architecture:*`)

## Bars

1. **Fail fast** if there is no `package.json` at the workspace root (or the obvious app root the user named). ESLint and Prettier belong in JS/TS apps, not in this markdown pack itself.
2. **Never overwrite** an existing ESLint or Prettier config, ignore file, `.vscode/settings.json`, `complexity.test.mjs`, `cyclomatic-cap.mjs`, `principle-gate.test.mjs`, `principle-scan.mjs`, `knip.json`, `knip.test.mjs`, `stryker.conf.json`, or a script that already exists. Report what you skipped. `.vscode/extensions.json` may be merged (add missing recommendation IDs only).
3. **One stack.** Templates in [templates/](templates/) only. Do not add extra ESLint plugins beyond no-emdash and Convex when detected. The cyclomatic cap is ESLint’s built-in `complexity` rule plus the quality-gate test, not a third plugin. Quality tooling is ESLint, Prettier, Knip, and Stryker from templates. Do not swap in a different dead-code or mutation runner. Do not add a UI import denylist for keep jobs apart (SoC). Do not raise a cap, skip a gate, or delete a gate to go green (`taste:cyclomatic-cap`, `taste:fail-fast`, `taste:types-tell-the-truth`, `taste:trust-the-server`, `taste:no-dead-code`, `taste:kill-the-mutants`).
4. **Detect, then choose the matching template** (see [reference.md](reference.md)). Do not ask the user facts the repo already answers. Convex-only principle checks run only when `convex/` exists. The Knip gate runs only when its config exists. Stryker uses the TypeScript-checker template when `tsconfig.json` exists.
5. **Ask** only when a real fork remains (for example two app roots, or the user asked to replace a config). Follow [asking.md](../pack-shared/asking.md).
6. **Do not ritual-lint the whole tree** after install. One smoke command is enough (`npx eslint --print-config eslint.config.mjs` or `package-manager exec eslint --version`). Full `lint` only if the user asked. Do not run `test:quality` or `test:mutants` as setup smoke: on an existing messy codebase they are supposed to fail until functions are split, types/errors/auth are honest, dead code is removed, and locks bite.
7. **Do not reformat the repo** as part of setup. Leave `format` for the user.
8. Convex ESLint plugin **only** when `convex/` exists (or `@convex-dev/eslint-plugin` is already a dependency).
9. Talk in ordinary words. Gate failures and chat use **plain (Classic)** — `fail fast (Fail Fast)`. Do not dump pack nicknames (`taste:plain-language`).

## Output

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
- `/design` Initialization started when `docs/design.md` was missing (or reported skipped because the file already exists)

## Apply

Write configs next to the app `package.json`. That is the normal home for ESLint and Prettier. Do not invent `services/lint/` or a wrapper package unless this repo already publishes shareable configs that way.

If the repo already has a working lint/format story, **fill only missing pieces** (no-emdash plugin file, quality-gate files, `.vscode` recommendations, Prettier if missing). Do not overwrite their ESLint config. Print the import snippet if their config does not already include `noEmdashConfig` or the cyclomatic cap.

After that work, if `docs/design.md` is missing, run `/design` Initialization (`design:initialization`). Do not invent the file from this skill. If the file already exists, leave it.

## Anti-patterns

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

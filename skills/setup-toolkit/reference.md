# Setup toolkit reference

Load with [SKILL.md](SKILL.md). Copy files from [templates/](templates/) — do not rewrite them from memory.

## Resolve the pack root

Templates are at `<pack-root>/skills/setup-toolkit/templates/`.

Find `<pack-root>` from the same skill-root order as the gold-standards rule:

1. Parent of `setup-toolkit` under `~/.agents/skills/`
2. Parent of `setup-toolkit` under `~/.cursor/skills/`
3. This repository when the workspace **is** the Skills pack (`skills/setup-toolkit/templates/`)

If templates are missing, stop. Tell the user to install the plugin or:

```bash
npx skills@latest add Gabriel-Lafrance/Skills -a cursor -s '*' -g -y
```

## Detect the app root

Prefer the workspace root `package.json`. If the only `package.json` lives in a subdirectory the user named (for example `apps/web`), use that. If several apps could be the target, ask once with lettered options.

## Detect the package manager

From lockfiles in the app root, first match wins:

| File | Command |
| --- | --- |
| `pnpm-lock.yaml` | `pnpm add -D` |
| `yarn.lock` | `yarn add -D` |
| `bun.lock` / `bun.lockb` | `bun add -d` |
| `package-lock.json` or none | `npm install -D` |

## Pick templates

| Condition | ESLint template | Dev packages |
| --- | --- | --- |
| `tsconfig.json` exists, or `typescript` is a dependency | `eslint.config.mjs` | `eslint`, `@eslint/js`, `typescript-eslint`, `eslint-config-prettier`, `prettier` |
| Same, and `convex/` exists or `@convex-dev/eslint-plugin` is already a dependency | `eslint.config.with-convex.mjs` (write as `eslint.config.mjs`) | plus `@convex-dev/eslint-plugin` |
| JavaScript only | `eslint.config.js-only.mjs` (write as `eslint.config.mjs`) | `eslint`, `@eslint/js`, `eslint-config-prettier`, `prettier` |

Prettier is always `prettier.config.mjs` + `prettierignore` (written as `.prettierignore`).

Treat any of these as “ESLint already present”: `eslint.config.js`, `eslint.config.mjs`, `eslint.config.cjs`, `eslint.config.ts`, `.eslintrc`, `.eslintrc.js`, `.eslintrc.cjs`, `.eslintrc.json`, or `package.json` `"eslintConfig"`.

Treat any of these as “Prettier already present”: `prettier.config.*`, `.prettierrc`, `.prettierrc.*`, or `package.json` `"prettier"`.

## Write `package.json` scripts

Add only keys that are missing:

```json
{
  "lint": "eslint .",
  "lint:fix": "eslint . --fix",
  "format": "prettier --write .",
  "format:check": "prettier --check ."
}
```

Do not change an existing script with the same name.

## Install

Run the package manager add command once with the chosen packages. Do not pin versions unless the repo already pins with exact versions everywhere.

## Smoke check

After install, run **one** of:

```bash
npx eslint --version
npx prettier --version
```

(or the same binaries via the detected package manager). Report versions. Do not run a full-repo lint or format unless the user asked.

## Pin plugin rules (only if asked)

If the user wants Cursor rules **in this app repo** (cloud agents, teammates without the plugin):

1. Create `.cursor/rules/gabriel-skills/`.
2. Copy every `*.mdc` from `<pack-root>/rules/` into that folder.
3. Do not copy them when the user did not ask. The marketplace plugin already loads `rules/` for installed users.

## Done when

- Missing configs were written from templates
- Existing configs were left in place and listed
- Packages installed (or skipped because already present)
- Scripts added or skipped with names listed
- One version smoke check ran

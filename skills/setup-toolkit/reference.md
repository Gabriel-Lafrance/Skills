# Setup toolkit reference

Load with [SKILL.md](SKILL.md). Copy files from [templates/](templates/). Do not rewrite them from memory.

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

Always copy `eslint-plugin-no-emdash.mjs` next to `eslint.config.mjs` when you write that config. Always copy these next to the app `package.json` when missing (never overwrite): `cyclomatic-cap.mjs`, `complexity.test.mjs`, `principle-gate.test.mjs`, `principle-scan.mjs`. If ESLint already exists, still copy the plugin file and the quality-gate files when missing, then print the import to add (do not edit their config):

```js
import { maxCyclomaticComplexity } from "./cyclomatic-cap.mjs";
import { noEmdashConfig } from "./eslint-plugin-no-emdash.mjs";
// include noEmdashConfig in the exported config array / tseslint.config(...)
// rules: { complexity: ["error", maxCyclomaticComplexity] }
```

Treat any of these as “ESLint already present”: `eslint.config.js`, `eslint.config.mjs`, `eslint.config.cjs`, `eslint.config.ts`, `.eslintrc`, `.eslintrc.js`, `.eslintrc.cjs`, `.eslintrc.json`, or `package.json` `"eslintConfig"`.

Treat any of these as “Prettier already present”: `prettier.config.*`, `.prettierrc`, `.prettierrc.*`, or `package.json` `"prettier"`.

## Write `package.json` scripts

Add only keys that are missing:

```json
{
  "lint": "eslint .",
  "lint:fix": "eslint . --fix",
  "format": "prettier --write .",
  "format:check": "prettier --check .",
  "test:quality": "node --test complexity.test.mjs principle-gate.test.mjs"
}
```

Do not change an existing script with the same name. If `test` is missing, also add:

```json
{
  "test": "node --test complexity.test.mjs principle-gate.test.mjs"
}
```

Do not append the quality gates onto an existing `test` script. Do not add a new `test:complexity` script; `test:quality` is the one agent command. If `test:complexity` already exists from an older setup, leave it and still add `test:quality` when that name is free.

## Quality gates

`test:quality` runs both Node tests. Failure lines are `file:line` plus **plain (Classic)** plus what to do. Convex-only checks skip when there is no `convex/` directory. JavaScript-only apps (no `tsconfig.json`) skip TypeScript `any`; they still scan Convex `v.any` when that call appears.

| Gate | Scanner |
| --- | --- |
| Cyclomatic complexity (McCabe) | `complexity.test.mjs` (cap 5) |
| Types tell the truth (make illegal states unrepresentable) | `any`, Convex `v.any` |
| Fail fast (Fail Fast) | empty `catch`, `{ success: true/false }` Result bags |
| Trust the server (never trust the client) | public Convex `mutation` / `action` with no identity helper (`requireUser`, `getUserIdentity`, `getAuthUserId`, `auth.getUserId`). Skips `internalMutation`, `internalAction`, queries, `http.ts`, `httpActions.ts`, `crons.ts` |
| Deterministic queries (no clock in queries) | `Date.now`, `new Date`, `Math.random`, `crypto.randomUUID` inside `query` / `internalQuery` |

Keep jobs apart (SoC), one altitude (SLAP), read or write, not both (CQS), leave it cleaner (Boy Scout Rule), and no surprises (PoLA) stay review. Do not invent a denylist to fake them.

## Cursor / VS Code workspace files

Copy from `templates/vscode/` into the app’s `.vscode/`:

| File | If missing | If present |
| --- | --- | --- |
| `extensions.json` | Write the template | Merge: keep existing `recommendations`, append `dbaeumer.vscode-eslint` and `esbenp.prettier-vscode` when absent |
| `settings.json` | Write the template | Leave it. Report that format-on-save / ESLint settings were skipped |

Do not invent a `.cursor/extensions.json`. Cursor reads `.vscode/extensions.json` and `.vscode/settings.json` the same way VS Code does.

## Install

Run the package manager add command once with the chosen packages. Do not pin versions unless the repo already pins with exact versions everywhere.

## Smoke check

After install, run **one** of:

```bash
npx eslint --version
npx prettier --version
```

(or the same binaries via the detected package manager). Report versions. Do not run a full-repo lint, format, or `test:quality` unless the user asked.

## Pin plugin rules (only if asked)

If the user wants Cursor rules **in this app repo** (cloud agents, teammates without the plugin):

1. Create `.cursor/rules/gabriel-skills/`.
2. Copy every `*.mdc` from `<pack-root>/rules/` into that folder.
3. Do not copy them when the user did not ask. The marketplace plugin already loads `rules/` for installed users.

## Done when

- Missing configs were written from templates
- `eslint-plugin-no-emdash.mjs` is present next to ESLint config (or reported skipped)
- `cyclomatic-cap.mjs`, `complexity.test.mjs`, `principle-gate.test.mjs`, and `principle-scan.mjs` are present next to `package.json` (or reported skipped)
- `.vscode/extensions.json` has the ESLint and Prettier extension IDs
- `.vscode/settings.json` was written or reported skipped
- Existing configs were left in place and listed
- Packages installed (or skipped because already present)
- Scripts added or skipped with names listed (`test:quality`, and `test` only when it was missing)
- One version smoke check ran
- `test:quality` was **not** run as setup smoke

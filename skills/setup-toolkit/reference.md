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

| Condition | ESLint template | Stryker template | Dev packages |
| --- | --- | --- | --- |
| `tsconfig.json` exists, or `typescript` is a dependency | `eslint.config.mjs` | `stryker.conf.with-ts.json` (write as `stryker.conf.json`) | `eslint`, `@eslint/js`, `typescript-eslint`, `eslint-config-prettier`, `prettier`, `knip`, `@stryker-mutator/core`, `@stryker-mutator/typescript-checker` |
| Same, and `convex/` exists or `@convex-dev/eslint-plugin` is already a dependency | `eslint.config.with-convex.mjs` (write as `eslint.config.mjs`) | `stryker.conf.with-ts.json` (write as `stryker.conf.json`) | plus `@convex-dev/eslint-plugin` |
| JavaScript only | `eslint.config.js-only.mjs` (write as `eslint.config.mjs`) | `stryker.conf.json` | `eslint`, `@eslint/js`, `eslint-config-prettier`, `prettier`, `knip`, `@stryker-mutator/core` |

Prettier is always `prettier.config.mjs` + `prettierignore` (written as `.prettierignore`).

Knip config is always `knip.json`.

Always copy `eslint-plugin-no-emdash.mjs` next to `eslint.config.mjs` when you write that config. Always copy these next to the app `package.json` when missing (never overwrite): `cyclomatic-cap.mjs`, `complexity.test.mjs`, `principle-gate.test.mjs`, `principle-scan.mjs`, `knip.json`, `knip.test.mjs`, `stryker.conf.json`. If ESLint already exists, still copy the plugin file and the quality-gate files when missing, then print the import to add (do not edit their config):

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
  "test:quality": "node --test complexity.test.mjs principle-gate.test.mjs knip.test.mjs",
  "test:mutants": "stryker run"
}
```

Do not change an existing script with the same name. If `test` is missing, also add:

```json
{
  "test": "node --test complexity.test.mjs principle-gate.test.mjs knip.test.mjs"
}
```

Do not append the quality gates onto an existing `test` script. Do not include `test:mutants` in `test` or `test:quality`: mutants are a deliberate hardening run, not an every-save gate. Do not add a new `test:complexity` script; `test:quality` is the one agent command. If `test:complexity` already exists from an older setup, leave it and still add `test:quality` when that name is free.

## Quality gates

`test:quality` runs three fast Node tests. `test:mutants` is the slow mutant check (Stryker) and runs separately. Failure lines are `file:line` plus **plain (Classic)** plus what to do. Convex-only checks skip when there is no `convex/` directory. JavaScript-only apps (no `tsconfig.json`) skip TypeScript `any`; they still scan Convex `v.any` when that call appears. The Knip gate skips when its config or binary is missing.

| Gate | Check |
| --- | --- |
| Cyclomatic complexity (McCabe) | `complexity.test.mjs` (cap 5) |
| Types tell the truth (make illegal states unrepresentable) | `any`, Convex `v.any` |
| Fail fast (Fail Fast) | empty `catch`, `{ success: true/false }` Result bags |
| Trust the server (never trust the client) | public Convex `mutation` / `action` with no identity helper (`requireUser`, `getUserIdentity`, `getAuthUserId`, `auth.getUserId`). Skips `internalMutation`, `internalAction`, queries, `http.ts`, `httpActions.ts`, `crons.ts` |
| Deterministic queries (no clock in queries) | `Date.now`, `new Date`, `Math.random`, `crypto.randomUUID` inside `query` / `internalQuery` |
| No dead code (Knip) | `knip.test.mjs`: unused files, exports, and dependencies |
| Kill the mutants (Mutation testing) | `test:mutants` (Stryker): flipped operators and negated booleans must fail the suite. Deliberate run, not part of `test:quality` |

Keep jobs apart (SoC), one altitude (SLAP), read or write, not both (CQS), no surprises (PoLA), and don’t repeat yourself (DRY) stay review, as does the rest of leave it cleaner (Boy Scout Rule) beyond dead code. Do not invent a denylist to fake them.

### No dead code (Knip)

Knip walks the import graph from package entries, framework plugins, and scripts. It reports unused files, unused exports, unused dependencies, and imports missing from `package.json`. The template `knip.json` is intentionally empty: Knip discovers entries itself. Narrow `entry` and `project` in that file only when Knip prints configuration hints for this repo.

- If `test:quality` could not be added because the name is taken, the gate files are unreferenced: append them to `ignore` in the copied `knip.json` so Knip does not flag its own runner files, and tell the user where the gates run instead.
- Never delete `knip.json` or add broad ignores to go green. Remove the dead code.

### Kill the mutants (Mutation testing)

Stryker flips operators (`>` to `>=`), negates booleans, and changes signs, one mutant at a time, then runs the behavior suite. A surviving mutant means the suite is decoration: green checkmarks that assert almost nothing. The break threshold fails the run when the score drops, so the rule lives in the build instead of in a prompt.

- **Deliberate, not every save.** Run `test:mutants` after `/create-test` locks land, before shipping a risky slice, or nightly in CI. Never add it to `test:quality` or `test`. Mutation runs are CPU-heavy and run unattended.
- **Configure after copying.** Set `packageManager` to the detected manager (`npm`, `pnpm`, or `yarn`; `bun` projects use `npm`). Keep `commandRunner.command` on `npm test` unless the behavior suite needs a different command. Never point Stryker at `test:quality`: static scanners cannot kill runtime mutants. When no behavior suite exists yet, tell the user mutants will fail until locks exist.
- **Thresholds.** `break` 60 fails the run below 60. Raise it toward 80 as locks land. Never lower `break` (or set it to `null`) to go green. Add locks until mutants die.
- **Faster runs.** The template omits `testRunner`: Stryker's default is the command runner, and naming it makes Knip demand a `@stryker-mutator/command-runner` package that does not exist. Apps on Vitest, Jest, or Mocha can set `testRunner` to that Stryker plugin with `coverageAnalysis: perTest` so each mutant runs only its covering tests. The command runner works everywhere but runs the whole suite per mutant. Keep `incremental` off: with the command runner Stryker reuses stale scores after test-only changes.
- **TypeScript 7.** Stryker 10 does not support TypeScript 7 yet (its sandbox crashes reading the config). On `typescript@7`, still install the config, and tell the user `test:mutants` waits on upstream Stryker support. TypeScript 5 and JavaScript work today.

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

(or the same binaries via the detected package manager). Report versions. Do not run a full-repo lint, format, `test:quality`, or `test:mutants` unless the user asked.

## Design file

After lint/format work, check workspace-root `docs/design.md` only (no other path).

| State | Action |
| --- | --- |
| File missing | Run `/design` Initialization. That skill inventories every route from code and writes a short Do / Don't list. |
| File present | Leave it. Do not overwrite. |

Skip Initialization only when this workspace is not an app (setup already stopped for a missing `package.json`).

## Pin plugin rules (only if asked)

If the user wants Cursor rules **in this app repo** (cloud agents, teammates without the plugin):

1. Create `.cursor/rules/gabriel-skills/`.
2. Copy every `*.mdc` from `<pack-root>/rules/` into that folder.
3. Do not copy them when the user did not ask. The marketplace plugin already loads `rules/` for installed users.

## Done when

- Missing configs were written from templates
- `eslint-plugin-no-emdash.mjs` is present next to ESLint config (or reported skipped)
- `cyclomatic-cap.mjs`, `complexity.test.mjs`, `principle-gate.test.mjs`, `principle-scan.mjs`, `knip.json`, `knip.test.mjs`, and `stryker.conf.json` are present next to `package.json` (or reported skipped)
- `.vscode/extensions.json` has the ESLint and Prettier extension IDs
- `.vscode/settings.json` was written or reported skipped
- Existing configs were left in place and listed
- Packages installed (or skipped because already present)
- Scripts added or skipped with names listed (`test:quality`, `test:mutants`, and `test` only when it was missing)
- One version smoke check ran
- `test:quality` and `test:mutants` were **not** run as setup smoke
- `docs/design.md` exists, or `/design` Initialization was started because it was missing

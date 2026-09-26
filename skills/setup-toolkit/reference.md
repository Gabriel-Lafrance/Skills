# Setup toolkit reference

Load with [SKILL.md](SKILL.md). Copy files from [templates/](templates/). Do not rewrite them from memory.

## Resolve the skill root

The skill root is the folder that holds `setup-toolkit/`. Use the same order as the "Find the pack" section of `AGENTS.md`: `~/.agents/skills/`, `~/.claude/skills/`, `~/.cursor/skills/`, then this repository's `skills/` when the workspace **is** the Skills pack. Templates are at `<skill-root>/setup-toolkit/templates/`.

This workspace is the Skills pack when a parent directory holds both an `AGENTS.md` with `gabriel-skills-agents` and `skills/setup-toolkit/`.

If templates are missing, stop and tell the user:

```bash
npx skills@latest add gabriel-lafrance/skills@setup-toolkit -g -y
```

## Verify

Read the disk and print a short list. Do not ask the user for these facts.

| Fact | How to see it |
| --- | --- |
| User skills | `rules/code-quality.md` under `~/.agents/skills/`, `~/.claude/skills/`, or `~/.cursor/skills/` |
| Repo skills | `rules/code-quality.md` under the workspace `.agents/skills/`, `.claude/skills/`, or `.cursor/skills/` (ignore when the workspace is the Skills pack) |
| Repo contract | workspace-root `AGENTS.md`: missing, pack copy (has `gabriel-skills-agents`), or someone else's file. For a pack copy, its [contract version](#contract-version) |
| Harnesses in use | each folder in [Harness files](#harness-files) that exists, plus any harness the user named |
| App | workspace `package.json`; ESLint or Prettier already present |

### Contract version

The marker is the first line: `<!-- gabriel-skills-agents v2.0.0 -->`. Detect a pack copy by the prefix `gabriel-skills-agents` alone, so a copy with an old version or no version still counts as the pack's.

Compare each installed pack copy (the repo `AGENTS.md`, and a copied Codex `AGENTS.md`) with the [source](#install-agentsmd) marker. When the installed version is older, or the marker has no version, the copy is out of date:

1. Refresh it with the source now. It is the pack's own file, so no question is needed.
2. Tell the user it was out of date (old version, new version) and where to see what changed: [merged pull requests](https://github.com/Gabriel-Lafrance/Skills/pulls?q=is%3Apr+is%3Amerged) and [commits on main](https://github.com/Gabriel-Lafrance/Skills/commits/main).

A symlink to the installed template is always current. A file without the prefix is someone else's: never refresh it.

## Questions

After Verify, one batch. Wait. Do not install until they reply. Shape: [asking.md](../pack-shared/asking.md).

```markdown
## Questions
Reply like: 1a 2a

1. Where should this pack and AGENTS.md go?
   - a) This repo recommended
   - b) This repo and user-level (every repo on this machine)
   - c) User-level only
2. Add ESLint and Prettier to this app?
   - a) no recommended
   - b) yes
```

Omit item 2 when there is no `package.json`. If they pick c, say that Cursor has no user-level file, so Cursor in this repo will not see the rules.

## Pack skills

`npx skills add gabriel-lafrance/skills@setup-toolkit` copies only this skill. This step lands the rest of the pack for each chosen scope. Skip it when the workspace is the Skills pack.

A scope is current when `rules/code-quality.md` exists in it. A scope with pack skills but no `rules/code-quality.md` is stale: update it, do not skip it.

```bash
# User-level (b or c)
npx skills@latest add gabriel-lafrance/skills --all -g

# This repo (a or b)
npx skills@latest add gabriel-lafrance/skills --all

# Stale copy
npx skills@latest update
```

`--all` installs every skill into every harness the CLI sees, with no prompt. If a command fails (no network, old Node), say so and continue with the contract from the source below. Do not build skill folders by hand.

## Install AGENTS.md

Do this even when there is no `package.json`. Touch only the scopes they chose.

**Source:** the pack root `AGENTS.md` when the workspace is the Skills pack, otherwise `<skill-root>/setup-toolkit/templates/AGENTS.md`. It must contain `gabriel-skills-agents`. If it does not, say so and skip this section.

**Never overwrite someone else's instructions file.** A file is the pack's only when it contains `gabriel-skills-agents`. Every other file only ever gets a line appended.

### Repo

1. Workspace-root `AGENTS.md` missing: copy the source there.
2. It has the marker: overwrite it with the source (refresh).
3. It exists without the marker: append this section, then say so.

```markdown

## Gabriel skills

Also follow the Gabriel skills contract: `<skill-root>/setup-toolkit/templates/AGENTS.md`.
```

Use the real path: workspace-relative when the pack is installed in this repo, absolute otherwise. Skip the append when the file already mentions `setup-toolkit/templates/AGENTS.md`.

Then apply [Harness files](#harness-files) at the repo level.

### Harness files

Most harnesses read a workspace `AGENTS.md` on their own (Cursor, Codex, GitHub Copilot, Windsurf, Zed, Amp, OpenCode, goose, and others). A harness that reads a different filename gets a one-line pointer to `AGENTS.md`.

The rule, for every row whose harness is in use (its project or home folder exists, or the user named it):

- The file is missing: create it with only the pointer line.
- The file exists without the pointer line: append the pointer line on its own line.
- The file already has the pointer line: leave it.

| Harness | In use when this exists | Repo file | Pointer line |
| --- | --- | --- | --- |
| Claude Code | `.claude/` or `~/.claude/` | `CLAUDE.md` | `@AGENTS.md` |
| Gemini CLI | `.gemini/` or `~/.gemini/` | `GEMINI.md` | `@AGENTS.md` |
| Aider | `.aider.conf.yml` | `.aider.conf.yml` (edit only, never create) | `read: AGENTS.md`, or append `AGENTS.md` to an existing `read` list |

A new harness needs one row. When a tool has no import syntax, the pointer line is the plain sentence `Follow AGENTS.md.`. Do not write `.cursor/rules` or an `.mdc` file: Cursor reads `AGENTS.md`.

### User level

Run only for b or c. Point each harness at the installed template. Do not copy its bytes, so `npx skills update` refreshes every harness at once. `<template>` is the absolute path of `<skill-root>/setup-toolkit/templates/AGENTS.md` in the **user** skill root.

Only touch a harness whose home already exists. Never create a home folder for a harness that is not installed.

| Harness | Home | What to do |
| --- | --- | --- |
| Claude Code | `~/.claude/` | Pointer line `@<template>` in `~/.claude/CLAUDE.md`, by the rule in [Harness files](#harness-files) |
| Gemini CLI | `~/.gemini/` | Pointer line `@<template>` in `~/.gemini/GEMINI.md`, same rule |
| Codex | `$CODEX_HOME` when set, else `~/.codex/` | `AGENTS.md` missing or a pack copy: symlink it to `<template>`. If the symlink fails, copy the file and say it will not refresh on update. Someone else's file: append `Follow <template>.` |
| Cursor | none | No user-level file. Say the repo install covers Cursor |

## Clean up old installs

Older versions of this pack left two files that nothing reads now. Delete only these, only in the scopes they chose:

- **Old Claude copy** (b or c): if `~/.claude/gabriel-skills/AGENTS.md` contains `gabriel-skills-agents`, delete it, and remove the `@~/.claude/gabriel-skills/AGENTS.md` line from `~/.claude/CLAUDE.md` when present. Remove `~/.claude/gabriel-skills/` only if it is then empty. A file there without the marker stays.
- **Old Cursor pointer:** delete `gabriel-skills/follow-agents.mdc` under `~/.cursor/rules` (b or c) or the app `.cursor/rules` (a or b) when it exists. Leave every other Cursor rule and hook.

Setup never writes `.cursor/rules`, an `.mdc` file, or `.cursor/hooks.json`.

## Report

End with one line per file: path, then **written**, **refreshed** (say "out of date" and the versions when [Contract version](#contract-version) triggered it), **appended**, **symlinked**, **copied**, **deleted**, or **skipped**, and the reason (for example "skipped: foreign AGENTS.md, pointer appended instead", "skipped: `~/.gemini` not installed", or "deleted: old pack copy"). List each [cleanup](#clean-up-old-installs) path that existed as deleted, or skipped with the reason (for example "skipped: no `gabriel-skills-agents` marker").

## Detect the app

**App root:** the workspace root `package.json`, else the folder the user named (for example `apps/web`). If several apps could be the target, ask once with lettered options.

**Package manager**, from lockfiles in the app root, first match wins: `pnpm-lock.yaml` is `pnpm add -D`; `yarn.lock` is `yarn add -D`; `bun.lock` or `bun.lockb` is `bun add -d`; otherwise `npm install -D`.

## Pick templates

| Condition | ESLint template (write as `eslint.config.mjs`) | Dev packages |
| --- | --- | --- |
| `tsconfig.json` exists, or `typescript` is a dependency | `eslint.config.mjs` | `eslint`, `@eslint/js`, `typescript-eslint`, `globals`, `eslint-config-prettier`, `prettier` |
| Same, and `convex/` exists or `@convex-dev/eslint-plugin` is a dependency | `eslint.config.with-convex.mjs` | the row above plus `@convex-dev/eslint-plugin` |
| JavaScript only | `eslint.config.js-only.mjs` | `eslint`, `@eslint/js`, `globals`, `eslint-config-prettier`, `prettier` |

Prettier is always `prettier.config.mjs` plus `prettierignore` (written as `.prettierignore`). Always copy `eslint-plugin-no-emdash.mjs` next to `eslint.config.mjs`.

ESLint is already present when any of these exist: `eslint.config.{js,mjs,cjs,ts}`, `.eslintrc`, `.eslintrc.{js,cjs,json}`, or `package.json` `"eslintConfig"`. Then leave their config, copy only the plugin file, and print the line to add:

```js
import { noEmdashConfig } from "./eslint-plugin-no-emdash.mjs";
// add noEmdashConfig to the exported config array
```

Prettier is already present when `prettier.config.*`, `.prettierrc`, `.prettierrc.*`, or `package.json` `"prettier"` exists. Then leave it.

**Scripts:** add only missing keys in `package.json`, never change an existing one: `"lint": "eslint ."`, `"lint:fix": "eslint . --fix"`, `"format": "prettier --write ."`, `"format:check": "prettier --check ."`.

## Editor files

Copy from `templates/vscode/` into the app's `.vscode/`. Cursor reads `.vscode/` the same way VS Code does; do not add `.cursor/extensions.json`.

| File | If missing | If present |
| --- | --- | --- |
| `extensions.json` | Write the template | Keep existing `recommendations`, append `dbaeumer.vscode-eslint` and `esbenp.prettier-vscode` when absent |
| `settings.json` | Write the template | Leave it and report it skipped |

## Install and smoke check

Run the package manager add command once with the chosen packages. Do not pin versions unless the repo already pins exact versions everywhere. Then run `npx eslint --version` (or through the detected manager) and report the version. Do not lint or format the whole repo unless the user asked.

## Done when

- Verify printed its facts, and scope and lint were asked once
- Pack skills and contract went only to the chosen scopes; stale copies were updated
- Only pack-marked files were overwritten; others only got a pointer; no harness home was created
- Only the two [old install](#clean-up-old-installs) files were deleted, and only when they matched
- Lint files, packages, and scripts exist only if they said yes to lint
- The report lists every file with its action and reason

---
name: setup-toolkit
description: >-
  Gabriel Lafrance Skills on-ramp (setup-toolkit) from skills.sh. Verifies
  what is installed, then installs this pack and AGENTS.md into the repo
  (default), user level, or both, with one-line pointers for harnesses
  that read another file (CLAUDE.md, GEMINI.md). ESLint and Prettier are
  opt-in. Use when the user wants npx skills, skills.sh, this pack,
  AGENTS.md, linting, formatting, or to set up the rules across Claude,
  Cursor, Codex, Gemini, and other harnesses. Not for rewriting an
  existing lint stack.
disable-model-invocation: true
---

# Setup toolkit

Install this pack and `AGENTS.md`, then optionally ESLint and Prettier. User start only; do not nest it under `/task`. Install this skill with
`npx skills@latest add gabriel-lafrance/skills@setup-toolkit -g -y`, then run it.

## Read when

- Every run: [code-quality.md](../rules/code-quality.md) and [code-structure.md](../rules/code-structure.md), plus [doctrine.md](doctrine.md).
- At the step that links a section: [reference.md](reference.md).
- Talking to or asking the user: [plain-language.md](../pack-shared/plain-language.md) and [asking.md](../pack-shared/asking.md).

Phase one verifies what is on disk, then installs the pack and `AGENTS.md` into
**this repo** (recommended), **user level**, or both. ESLint, Prettier, and
editor files are a second phase. Ask before that phase. Do not copy lint files
until the user says yes.

## Process

1. Verify. Look up skill roots, `AGENTS.md`, harnesses in use, and whether this
   app has a `package.json`. Print those facts. Do not ask the user for them
   ([reference.md](reference.md#verify)).
2. Ask once ([reference.md](reference.md#questions)). Wait. Scope is this repo,
   this repo and user level, or user level only. Lint is yes or no. Skip the
   lint item when there is no `package.json`.
3. Phase one: install or update pack skills and `AGENTS.md` for the chosen
   scopes, with pointer lines for harnesses that read another filename
   ([reference.md](reference.md#pack-skills),
   [reference.md](reference.md#install-agentsmd)).
4. Phase two, only if they said yes to lint: copy lint, format, and editor
   templates.
5. If they said yes to lint and `docs/design.md` is missing at the workspace
   root, run `/design` Initialization. Do not write a fake design file from
   this skill.
6. Report every file written, refreshed, appended, symlinked, copied, or
   skipped, with the reason ([reference.md](reference.md#report)).

## Anti-patterns

- Overwriting an instructions file that lacks `gabriel-skills-agents`
- Creating a home folder for a harness that is not installed
- Writing a `.cursor/rules` or `.mdc` copy

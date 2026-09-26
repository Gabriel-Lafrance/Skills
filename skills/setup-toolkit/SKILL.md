---
name: setup-toolkit
description: >-
  Verify, then install this pack and AGENTS.md in the repo, user level, or
  both, with pointer lines for other harnesses. Lint and format are opt-in.
  Use when the user wants npx skills, skills.sh, this pack, AGENTS.md, or
  linting set up. Not for rewriting an existing lint stack.
disable-model-invocation: true
---

# Setup toolkit

Install this pack and `AGENTS.md`, then optionally ESLint and Prettier. User start only; do not nest it under `/task`. Install this skill with
`npx skills@latest add gabriel-lafrance/skills@setup-toolkit -g -y`, then run it.

## Read when

- Every run: [code-quality.md](../rules/code-quality.md) and [code-structure.md](../rules/code-structure.md), plus [doctrine.md](doctrine.md).
- At the step that links a section: [reference.md](reference.md).
- Talking to or asking the user: the [Plain language](../rules/writing-style.md#plain-language) and [Asking the user](../rules/writing-style.md#asking-the-user) sections of writing-style.md.

Phase one verifies what is on disk, then installs the pack and `AGENTS.md` into
**this repo** (recommended), **user level**, or both. ESLint, Prettier, and
editor files are a second phase. Ask before that phase. Do not copy lint files
until the user says yes.

## Process

1. Verify. Look up skill roots, `AGENTS.md`, harnesses in use, and whether this
   app has a `package.json`. Print those facts. Do not ask the user for them
   ([reference.md](reference.md#verify)). Refresh a pack `AGENTS.md` whose
   marker version is older or missing, and tell the user it was out of date
   with links to what changed ([reference.md](reference.md#contract-version)).
2. Ask once ([reference.md](reference.md#questions)). Wait. Scope is this repo,
   this repo and user level, or user level only. Lint is yes or no. Skip the
   lint item when there is no `package.json`.
3. Phase one: install or update pack skills and `AGENTS.md` for the chosen
   scopes, with pointer lines for harnesses that read another filename
   ([reference.md](reference.md#pack-skills),
   [reference.md](reference.md#install-agentsmd)).
4. Phase two, only if they said yes to lint: copy lint, format, and editor
   templates.
5. Delete old pack leftovers and retired pack skill folders when they match, and nothing else
   ([reference.md](reference.md#clean-up-old-installs)).
6. Report every file written, refreshed, appended, symlinked, copied,
   deleted, or skipped, with the reason ([reference.md](reference.md#report)).

## Anti-patterns

- Overwriting an instructions file that lacks `gabriel-skills-agents`
- Creating a home folder for a harness that is not installed
- Writing a `.cursor/rules` or `.mdc` copy

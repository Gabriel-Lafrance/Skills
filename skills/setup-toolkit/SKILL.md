---
name: setup-toolkit
description: >-
  Gabriel Lafrance Skills on-ramp (setup-toolkit) from skills.sh. First
  verifies, then installs this pack and AGENTS.md into the repo or the
  user's harness data. ESLint, Prettier, and quality gates are opt-in.
  Use when the user wants npx skills, skills.sh, this pack, AGENTS.md,
  linting, formatting, Knip, Stryker, or to set up tools across Claude,
  Cursor, Codex, and other environments. Not for rewriting an existing
  lint stack.
disable-model-invocation: true
---

# Setup toolkit

Install this pack and `AGENTS.md`, then optionally lint and quality gates. User start only; do not nest it under `/task`. Install this skill with
`npx skills@latest add gabriel-lafrance/skills@setup-toolkit -g -y`, then run it.

## Read when

- Every run: [code-quality.md](../rules/code-quality.md) and [code-structure.md](../rules/code-structure.md) ([standards.md](../pack-shared/standards.md)), plus [doctrine.md](doctrine.md).
- At the step that links a section: [reference.md](reference.md).
- Talking to or asking the user: [plain-language.md](../pack-shared/plain-language.md) and [asking.md](../pack-shared/asking.md).

Phase one verifies what is already on disk, then installs the rest of this pack
and `AGENTS.md` into the **repo**, **user data**, or both. ESLint, Prettier, editor
files, and quality gates (`test:quality`, `test:mutants`) are a second phase.
Ask before that phase. Do not copy lint files until the user says yes.

## Process

1. Verify. Look up skill roots, `AGENTS.md`, harness homes, and whether this
   app has a `package.json`. Print those facts. Do not ask the user for them
   ([reference.md](reference.md#verify)).
2. Ask once ([reference.md](reference.md#questions)). Wait. Destination is
   repo, user data, or both. Lint is yes or no. Skip the lint item when there
   is no `package.json`.
3. Phase one: install pack skills and `AGENTS.md` only for the chosen
   destination ([reference.md](reference.md#pack-skills),
   [reference.md](reference.md#install-agentsmd)).
4. Phase two, only if they said yes to lint: copy lint, format, editor, and
   quality-gate templates.
5. If they said yes to lint and `docs/design.md` is missing at the workspace
   root, run `/design` Initialization. That skill owns the code-derived route
   inventory. Do not write a fake design file from this skill.

## Anti-patterns

- Writing a `.cursor/rules` or `.mdc` copy
- Creating a harness home that is not installed
- Adding a project `CLAUDE.md`

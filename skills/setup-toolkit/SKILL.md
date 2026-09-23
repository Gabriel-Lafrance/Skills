---
name: setup-toolkit
description: >-
  Gabriel Lafrance Skills on-ramp (setup-toolkit) from skills.sh. Install
  this pack into every harness already on the machine, copy AGENTS.md, then
  ESLint, Prettier, editor files, and quality gates (test:quality,
  test:mutants) into the current app. Use when the user wants npx skills,
  skills.sh, this pack, AGENTS.md, linting, formatting, Knip, Stryker, or
  to set up tools across Claude, Cursor, Codex, and other environments.
  Not for rewriting an existing lint stack.
disable-model-invocation: true
---

# Setup toolkit

**Must read:** [../pack-shared/standards.md](../pack-shared/standards.md). Apply the **Taste** and **Architecture** sections of `AGENTS.md` this turn. Do not skip.

This skill is a user start. Do not nest it under `/task`.

**Read:** [doctrine.md](doctrine.md) · [reference.md](reference.md) · **Ask style:** [../pack-shared/asking.md](../pack-shared/asking.md) · **Plain language:** [../pack-shared/plain-language.md](../pack-shared/plain-language.md)

This is the skills.sh skill for this pack. Install it with
`npx skills@latest add gabriel-lafrance/skills@setup-toolkit -g -y`, then run
this skill. It fills the rest of the pack, then the contract, then lint.

Add **ESLint**, **Prettier**, Cursor/VS Code workspace files, and **quality-gate tests** (`test:quality`: cyclomatic complexity (McCabe) plus principle and dead-code gates; `test:mutants`: Stryker mutant check) to the **current app repo**. Templates live in [templates/](templates/). Do not invent a different stack.

The ESLint templates include a no-emdash rule (em dash, en dash, horizontal bar) and a cyclomatic cap of 5. Knip reports unused files, exports, and dependencies. Stryker proves behavior locks bite. Workspace files recommend the ESLint and Prettier extensions. Gate failures use **plain (Classic)**: `keep this simple (KISS)`.

If `docs/design.md` is missing at the workspace root, run `/design` Initialization after the lint/format work. That skill owns the code-derived route inventory. Do not write a fake design file from this skill.

## Process

1. Install the rest of this pack into every harness already on the machine ([reference.md](reference.md#pack-skills)). Skip when `pack-shared` already sits next to this skill, or when this workspace is the Skills pack.
2. Copy `AGENTS.md` into the app and into each existing harness home ([reference.md](reference.md#install-agents-md)).
3. Copy lint, format, editor, and quality-gate templates when the app has a `package.json`.
4. If `docs/design.md` is missing, run `/design` Initialization.

Details: [reference.md](reference.md). Do not write a `.cursor/rules` or `.mdc` copy. Do not create a harness home that is not installed. Do not add a project `CLAUDE.md`.

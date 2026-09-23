---
name: setup-toolkit
description: >-
  Install ESLint, Prettier, Cursor/VS Code workspace files, and principle
  quality-gate tests into the current JavaScript or TypeScript repo from
  this pack's templates. Use when the user wants linting, formatting, ESLint, Prettier,
  a formatter, recommended extensions, a complexity test, test:quality, dead
  code, Knip, mutants, Stryker, test:mutants, AGENTS.md, or to
  add the engineering toolkit to an app. Installs the pack AGENTS.md into
  the repo and into each harness home that already exists. Bans em dashes.
  Not for rewriting an existing lint stack.
disable-model-invocation: true
---

# Setup toolkit

**Must read:** [../pack-shared/standards.md](../pack-shared/standards.md). Apply the **Taste** and **Architecture** sections of `AGENTS.md` this turn. Do not skip.

This skill is a user start. Do not nest it under `/task`.

**Read:** [doctrine.md](doctrine.md) · [reference.md](reference.md) · **Ask style:** [../pack-shared/asking.md](../pack-shared/asking.md) · **Plain language:** [../pack-shared/plain-language.md](../pack-shared/plain-language.md)

Add **ESLint**, **Prettier**, Cursor/VS Code workspace files, and **quality-gate tests** (`test:quality`: cyclomatic complexity (McCabe) plus principle and dead-code gates; `test:mutants`: Stryker mutant check) to the **current app repo**. Templates live in [templates/](templates/). Do not invent a different stack.

The ESLint templates include a no-emdash rule (em dash, en dash, horizontal bar) and a cyclomatic cap of 5. Knip reports unused files, exports, and dependencies. Stryker proves behavior locks bite. Workspace files recommend the ESLint and Prettier extensions. Gate failures use **plain (Classic)**: `keep this simple (KISS)`.

Do not write `docs/design.md` from this skill, and do not start a design pass. If that file is missing, the designer writes a short Do / Don't list from the routes in code before UI work. Never overwrite an existing file with a blank template.

Install the pack `AGENTS.md` into this repo, then into each harness home that already exists for this user (Claude Code, Codex, Gemini CLI, Aider). Cursor reads the repo file. Do not write a `.cursor/rules` or `.mdc` copy. Details are in [reference.md](reference.md). Do not create a harness home that is not installed. Do not add a project `CLAUDE.md`.

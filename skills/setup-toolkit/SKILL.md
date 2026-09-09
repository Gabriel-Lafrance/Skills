---
name: setup-toolkit
description: >-
  Install ESLint, Prettier, Cursor/VS Code workspace files, and principle
  quality-gate tests into the current JavaScript or TypeScript repo from
  this pack's templates. Use when the user wants linting, formatting,
  ESLint, Prettier, a formatter, recommended extensions, a complexity
  test, test:quality, dead code, Knip, mutants, Stryker, test:mutants,
  or to add the engineering toolkit to an app. Bans
  em dashes. Not for rewriting an existing lint stack.
disable-model-invocation: true
---

# Setup toolkit

**Must read:** [../pack-shared/standards.md](../pack-shared/standards.md). Read `/taste` and `/architecture` doctrines this turn. Do not skip.

This skill is a user start. Do not nest it under `/task`.

**Read:** [doctrine.md](doctrine.md) · [reference.md](reference.md) · **Ask style:** [../pack-shared/asking.md](../pack-shared/asking.md) · **Plain language:** [../pack-shared/plain-language.md](../pack-shared/plain-language.md)

Add **ESLint**, **Prettier**, Cursor/VS Code workspace files, and **quality-gate tests** (`test:quality`: cyclomatic complexity (McCabe) plus principle and dead-code gates; `test:mutants`: Stryker mutant check) to the **current app repo**. Templates live in [templates/](templates/). Do not invent a different stack.

The ESLint templates include a no-emdash rule (em dash, en dash, horizontal bar) and a cyclomatic cap of 5. Knip reports unused files, exports, and dependencies. Stryker proves behavior locks bite. Workspace files recommend the ESLint and Prettier extensions. Gate failures use **plain (Classic)**: `keep this simple (KISS)`.

This pack’s Cursor **plugin rules** already apply when the plugin is installed. This skill does not copy those rules into `.cursor/rules` unless the user asks to pin them in the app repo.

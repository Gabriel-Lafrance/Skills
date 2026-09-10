---
name: setup-toolkit
description: >-
  Install ESLint, Prettier, and Cursor/VS Code workspace files (recommended
  ESLint and Prettier extensions) into the current JavaScript or TypeScript
  repo from this pack's templates. Also starts docs/design.md capture when
  that file is missing. Use when the user wants linting, formatting, ESLint,
  Prettier, a formatter, recommended extensions, design.md, or to add the
  engineering toolkit to an app. Bans em dashes. Not for rewriting an
  existing lint stack.
disable-model-invocation: true
---

# Setup toolkit

**Must read:** [../pack-shared/standards.md](../pack-shared/standards.md). Read `/taste` and `/architecture` doctrines this turn. Do not skip.

This skill is a user start. Do not nest it under `/task`.

**Read:** [doctrine.md](doctrine.md) · [reference.md](reference.md) · **Ask style:** [../pack-shared/asking.md](../pack-shared/asking.md) · **Plain language:** [../pack-shared/plain-language.md](../pack-shared/plain-language.md)

Add **ESLint**, **Prettier**, and Cursor/VS Code workspace files to the **current app repo**. Templates live in [templates/](templates/). Do not invent a different stack.

The ESLint templates include a no-emdash rule (em dash, en dash, horizontal bar). Workspace files recommend the ESLint and Prettier extensions.

If `docs/design.md` is missing at the workspace root, run `/design` Initialization after the lint/format work. That skill owns the code-derived route inventory. Do not write a fake design file from this skill.

This pack’s Cursor **plugin rules** already apply when the plugin is installed. This skill does not copy those rules into `.cursor/rules` unless the user asks to pin them in the app repo.

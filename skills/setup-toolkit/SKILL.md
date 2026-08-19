---
name: setup-toolkit
description: >-
  Install ESLint and Prettier into the current JavaScript or TypeScript
  repo from this pack's templates. Use when the user wants linting,
  formatting, ESLint, Prettier, a formatter, or to add the engineering
  toolkit to an app. Not for rewriting an existing lint stack.
disable-model-invocation: true
---

# Setup toolkit

**Must read:** [../pack-shared/standards.md](../pack-shared/standards.md) — Read `/taste` and `/architecture` doctrines this turn. Do not skip.

**Standalone only.** [../pack-shared/variants.md](../pack-shared/variants.md) — use the no-flow message if a parent asks for flow.

**Read:** [doctrine.md](doctrine.md) · [reference.md](reference.md) · **Ask style:** [../pack-shared/asking.md](../pack-shared/asking.md) · **Plain language:** [../pack-shared/plain-language.md](../pack-shared/plain-language.md)

Add **ESLint** and **Prettier** to the **current app repo**. Templates live in [templates/](templates/). Do not invent a different stack.

This pack’s Cursor **plugin rules** already apply when the plugin is installed. This skill does not copy those rules into `.cursor/rules` unless the user asks to pin them in the app repo.

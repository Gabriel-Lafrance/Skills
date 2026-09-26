---
name: setup-toolkit
description: >-
  Install the pack AGENTS.md into the repo or the user's harness
  data (the skill asks), then optionally add ESLint, Prettier, editor
  workspace files, and principle quality-gate tests from this pack's
  templates. Use when the user wants the engineering toolkit, AGENTS.md,
  lint, format, eslint, prettier, extensions, a complexity test,
  test:quality, dead code, knip, mutants, or test:mutants in an app.
---

# Setup toolkit

Follow the `/setup-toolkit` skill in this pack (`skills/setup-toolkit/SKILL.md`).

Apply `rules/code-quality.md` and `rules/code-structure.md` this turn, then execute that skill. The skill installs the contract. This command does not grow a second copy of those steps. Do not invent a different ESLint or Prettier stack. Do not add a project `CLAUDE.md`.

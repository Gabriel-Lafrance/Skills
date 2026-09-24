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

**Must read:** [../pack-shared/standards.md](../pack-shared/standards.md). Apply the **Taste** and **Architecture** sections of `AGENTS.md` this turn. Do not skip.

This skill is a user start. Do not nest it under `/task`.

**Read:** [doctrine.md](doctrine.md) · [reference.md](reference.md) · **Ask style:** [../pack-shared/asking.md](../pack-shared/asking.md) · **Plain language:** [../pack-shared/plain-language.md](../pack-shared/plain-language.md)

This is the skills.sh skill for this pack. Install it with
`npx skills@latest add gabriel-lafrance/skills@setup-toolkit -g -y`, then run
this skill.

Phase one verifies what is already on disk, then installs the rest of this pack
and `AGENTS.md` into the **repo**, **user data**, or both. ESLint, Prettier, editor
files, and quality gates (`test:quality`, `test:mutants`) are a second phase.
Ask before that phase. Do not copy lint files until the user says yes.

If they said yes to lint, and `docs/design.md` is missing at the workspace root,
run `/design` Initialization after. That skill owns the code-derived route
inventory. Do not write a fake design file from this skill.

## Process

1. Verify. Look up skill roots, `AGENTS.md`, harness homes, and whether this
   app has a `package.json`. Print those facts. Do not ask the user for them
   ([reference.md](reference.md#verify)).
2. Ask once ([reference.md](reference.md#questions)). Wait. Destination is
   repo, user data, or both. Lint is yes or no. Skip the lint item when there
   is no `package.json`.
3. Phase one: install pack skills and `AGENTS.md` only for the chosen
   destination ([reference.md](reference.md#pack-skills),
   [reference.md](reference.md#install-agents-md)).
4. Phase two, only if they said yes to lint: copy lint, format, editor, and
   quality-gate templates.
5. If they said yes to lint and `docs/design.md` is missing, run `/design`
   Initialization.

Details: [reference.md](reference.md). The repo gets the full `AGENTS.md` when they chose it. When they chose user data, Claude Code is one `@` import of the installed template and Codex is a symlink to that template. Gemini CLI and Aider keep their rows. Do not write `~/.claude/gabriel-skills/AGENTS.md`. Do not write a `.cursor/rules` file, a `.mdc` file, or a Cursor `hooks.json`. Delete `gabriel-skills/follow-agents.mdc` when that old pointer is already on disk. Do not create a harness home that is not installed. Do not add a project `CLAUDE.md`. Cursor reads the repo file.

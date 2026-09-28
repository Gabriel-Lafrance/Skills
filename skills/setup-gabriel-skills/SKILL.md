---
name: setup-gabriel-skills
description: Install this pack's skills and place AGENTS.md for the harness in use. Use when setting up Gabriel skills. If that install cannot be done, offer a manual copy.
category: General
disable-model-invocation: true
---

# Setup Gabriel skills

Install this pack's skills, including `rules/`, and place `AGENTS.md` where the harness already reads it. User start only; do not nest it under `/task`. Install this skill with
`npx skills@latest add gabriel-lafrance/skills@setup-gabriel-skills -g -y`, then run it.

This skill does not install ESLint, Prettier, or editor files.

## Read when

- Every run: open [code-quality.md](../rules/code-quality.md), [code-structure.md](../rules/code-structure.md), and [doctrine.md](doctrine.md). Skip them and you write files this skill must not touch.
- At a step that links a section? Open [reference.md](reference.md). Skip it and you overwrite someone else's `AGENTS.md` or create a harness home.
- About to talk to or ask the user? Open the [Plain language](../rules/writing-style.md#plain-language) and [Asking the user](../rules/writing-style.md#asking-the-user) sections of writing-style.md. Skip them and the scope question has no recommendation.

## Process

1. Verify. Look up skill roots and which harness homes exist. Print those facts. Do not ask the user for them
   ([reference.md](reference.md#verify)).
2. Ask once where the skills and `AGENTS.md` should go ([reference.md](reference.md#questions)). Wait.
3. Install or update pack skills for the chosen scopes
   ([reference.md](reference.md#pack-skills)).
4. Place `AGENTS.md` for the chosen scopes and the harnesses in use. Never overwrite a file that is not this pack's
   ([reference.md](reference.md#place-agentsmd)).
5. If the skills or `AGENTS.md` could not be installed, ask once about a manual install
   ([reference.md](reference.md#manual-install)). Yes: link the repo and say what to put where for the harnesses in use. No: setup failed. Stop.
6. Delete old pack leftovers and retired pack skill folders when they match, and nothing else
   ([reference.md](reference.md#clean-up-old-installs)).
7. Report every install, update, delete, skip, or failure, with the reason
   ([reference.md](reference.md#report)).

## Anti-patterns

- Offering a manual install before the install has failed
- Treating a declined manual install as success
- Overwriting an instructions file that lacks `gabriel-skills-agents`
- Creating a home folder for a harness that is not installed
- Writing a `.cursor/rules` or `.mdc` copy
- Writing ESLint, Prettier, or `.vscode` files

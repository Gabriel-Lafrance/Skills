---
name: setup-gabriel-skills
description: Use when the user runs /setup-gabriel-skills or asks to install, set up, or update Gabriel skills.
category: General
disable-model-invocation: true
---

# Setup Gabriel skills

User start only, never nested under `/task`. Install this skill with
`npx skills@latest add gabriel-lafrance/skills@setup-gabriel-skills -g -y`, then run it.

## Read when

- Every run: [doctrine.md](doctrine.md).
- Before asking the user: the [scope question](reference.md#questions) as written. Once `rules/` is installed, later messages follow [Plain language](../rules/writing-style.md#plain-language).

## Process

1. Verify. Look up skill roots and which harness homes exist, and print those facts instead of asking the user
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

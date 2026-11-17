# Setup Gabriel skills doctrine

## Job

Put this pack's skills, including `rules/`, onto the machine, and place `AGENTS.md` where the harness already reads it. Install into **this repo** (the default), at **user level**, or both.

## Owns

Every step of the Process in [SKILL.md](SKILL.md).

## Does not own

- ESLint, Prettier, editor files, package scripts, `.cursor/rules`, any `.mdc` file, or `.cursor/hooks.json`
- Creating a harness home the user does not have
- Rewriting `AGENTS.md` from memory
- `docs/design.md`

## Bars

1. **Place the contract from its source**, never from memory ([reference.md](reference.md#place-agentsmd)).
2. Talk in ordinary words. Cite principles as **plain (Classic)** (`quality:plain-language`).

## Output

For the scopes they chose, when install succeeds:

- Pack skills, including `rules/`, in the user skill home, the project skill home, or both
- `AGENTS.md` placed or refreshed only where that harness reads it, or a pointer line on someone else's file
- The old pack leftovers and retired pack skill folders deleted when they match, or reported skipped
- A report of every install, update, delete, skip, or failure, with the reason

## Apply

Follow the Process in [SKILL.md](SKILL.md).

## Anti-patterns

- Telling the user to hunt the skills.sh leaderboard instead of `npx skills add gabriel-lafrance/skills@setup-gabriel-skills`

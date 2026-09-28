# Setup Gabriel skills doctrine

## Job

Put this pack's skills, including `rules/`, onto the machine, and place `AGENTS.md` where the harness already reads it. Verify first, then install into **this repo** (the default), at **user level**, or both, after one question. If that install cannot be done, offer one manual copy. A no on that offer is a failed setup. The skill does not install ESLint, Prettier, or editor files.

## Owns

Verifying current installs, installing or updating the rest of this pack with `npx skills`, placing `AGENTS.md` without overwriting someone else's file, the manual-install offer after a real failure, and deleting old pack leftovers and retired pack skill folders ([reference.md](reference.md#clean-up-old-installs)).

## Does not own

- ESLint, Prettier, editor files, or package scripts
- Writing `.cursor/rules` or any `.mdc` file
- Creating a harness home the user does not have
- Rewriting `AGENTS.md` from memory
- Behavior-lock tests ([testing.md](../rules/testing.md))
- `docs/design.md` (the agent doing UI work writes it when missing)
- Detect and choose details: [`reference.md`](reference.md)

## Bars

1. **Verify, then ask, then install.** Look up skill roots and harness homes first. Print those facts. Then one Questions batch: where the skills and `AGENTS.md` go (this repo, this repo and user level, or user level only). Wait. Follow [Asking the user](../rules/writing-style.md#asking-the-user).
2. **Skills and rules together.** For each chosen scope, install the pack when `rules/code-quality.md` is missing, and update a stale copy with the commands in [reference.md](reference.md#pack-skills). Skip the skills command when this workspace is the Skills pack. `rules/` is one of those skill folders.
3. **Place the contract from its source.** Copy `AGENTS.md` from the pack root when this workspace is the Skills pack. Otherwise fetch `https://raw.githubusercontent.com/Gabriel-Lafrance/Skills/main/AGENTS.md`. It must contain `gabriel-skills-agents`. A file with that marker may be refreshed. Every other instructions file only gets a pointer line. Details: [reference.md](reference.md#place-agentsmd).
4. **Manual install is the way out, not the first path.** Offer it only after the skills command or the `AGENTS.md` place could not be done. One question. Yes: link [the repo](https://github.com/Gabriel-Lafrance/Skills) and list destinations for the harnesses in use. No: say setup failed and stop. Leave files that already landed in place.
5. **Use only harness homes that exist** (`~/.claude`, `~/.codex`, `~/.gemini`, and the rest). Skip a harness that is not installed.
6. Talk in ordinary words. Cite principles as **plain (Classic)**, for example `fail fast (Fail Fast)` (`quality:plain-language`).

## Output

For the scopes they chose, when install succeeds:

- Pack skills, including `rules/`, in the user skill home, the project skill home, or both
- `AGENTS.md` placed or refreshed only where that harness reads it, or a pointer line on someone else's file
- No new harness home folder
- No ESLint, Prettier, or editor file
- The old pack leftovers and retired pack skill folders deleted when they match, or reported skipped
- A report of every install, update, delete, skip, or failure, with the reason

When install cannot be done and they decline the manual copy: the report says setup failed. Name what already landed.

## Apply

Verify first ([reference.md](reference.md#verify)). Ask scope ([reference.md](reference.md#questions)). Wait. Install skills and place `AGENTS.md` only for the chosen scopes. Offer the manual copy only after a failed install.

## Anti-patterns

- Writing a Cursor `.mdc` rule, `.cursor/rules` copy, or `.cursor/hooks.json`
- Deleting any Cursor rule or hook other than `gabriel-skills/follow-agents.mdc`, or a file without `gabriel-skills-agents`
- Writing tests as setup
- Telling the user to hunt the skills.sh leaderboard instead of `npx skills add gabriel-lafrance/skills@setup-gabriel-skills`

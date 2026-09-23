# Contributing

Thanks for helping improve **Gabriel Lafrance Skills**, an engineering toolkit
for Claude, Cursor, and other harnesses.

By participating, you agree to follow the [Code of Conduct](CODE_OF_CONDUCT.md).

## What this repo is

Skills under [`skills/`](../skills/). The always-on contract is
[`AGENTS.md`](../AGENTS.md) for every harness, including Cursor. There is no
Cursor rules copy. An optional Cursor plugin ships the same skills, plus
[`agents/`](../agents/) and [`commands/`](../commands/).
Pack layout and authoring rules live in [`how-to.md`](../how-to.md). Standards
for how agents should work live in the Taste and Architecture sections of
[`AGENTS.md`](../AGENTS.md). [`skills/pack-shared/standards.md`](../skills/pack-shared/standards.md)
tells every skill to apply those sections. Chat
replies follow the Unslop section of `AGENTS.md`. Do not paste that file into a
User Rules box, and do not add a project `CLAUDE.md`. `/setup-toolkit` is what
installs the contract into an app and into harness homes that already exist.

## Before you start

1. Search [existing issues](https://github.com/Gabriel-Lafrance/Skills/issues)
   and PRs so we do not duplicate work.
2. For larger changes, open an issue first and describe the problem and
   proposed approach.
3. Keep changes focused — one concern per PR when practical.

## Local setup

```bash
git clone https://github.com/Gabriel-Lafrance/Skills.git
cd Skills
```

There is no build step. Edit skill markdown, then smoke-check:

```bash
npx skills@latest add . --list
```

`npx skills` can target Claude, Cursor, or both (`-a claude`, `-a cursor`). The
Cursor plugin is optional and does not add a separate ruleset. People install
this pack from skills.sh with
`npx skills@latest add gabriel-lafrance/skills@setup-toolkit -g -y`, then
`/setup-toolkit`. Installed skills must apply the Taste and Architecture
sections of `AGENTS.md`. ESLint and Prettier templates live in
[`skills/setup-toolkit/templates/`](../skills/setup-toolkit/templates/) and are
copied into **app** repos by `/setup-toolkit` — they are not run from this
markdown pack.

## How to change skills

- Prefer improving an existing skill over adding a new one.
- Numbered how-to lives in `SKILL.md`. Put durable rules in `doctrine.md` and
  detail in `reference.md` / `examples.md`. Taste and Architecture are the
  exception: those rules live in `AGENTS.md`, and their doctrine files only
  point there.
- Shared contracts (`asking`, execution context) live under
  `skills/pack-shared/` so `npx skills` installs them.
- Teach principles in prose — avoid steering agents with a catalog of concrete
  product examples when the skill should stay principle-first.

See [`how-to.md`](../how-to.md) for folder layout, frontmatter, and publish notes.

## Branch and PR

Use typed branches when possible (same contract as `/publish`):

```text
feature|tweak|bug|refactor|chore|hotfix/<ticket-or-no-ticket>-<slug>
```

Create that branch from the base commit with `git switch --detach <base-sha>`,
then `git switch -c <name>` (or `git switch --no-track -c`). Do not let it
track `dev`, `main`, or `master`. Push `HEAD:refs/heads/<name>`. A branch cut
from `dev` is its own ref: the push does not update `dev`, so it does not
take `dev`'s protection. Steps live in
[`skills/publish/reference.md`](../skills/publish/reference.md).

Before a push that opens a PR, or a commit or push on a branch that already
has an open PR, run that repo's CI in your environment and fix failures
first. A red push spends CI for nothing. This pack itself has no lint or
test CI; app repos that use `/setup-toolkit` do (`lint`, `test` or
`test:quality`), and the check is the mirror in
[`skills/pack-shared/pr-ship.md`](../skills/pack-shared/pr-ship.md). Do not
run that suite on a commit you are not pushing. Never skip hooks
(`--no-verify`) unless you were asked to.

Open a PR against `main` using the pull request template:

- **What changed**
- **Change diagram** (Mermaid; Before/After for rework)
- **How to QA**

Agents that open the PR — `/publish`, `/just-do-it`, `/task` ship, or a cloud
agent — follow [`skills/pack-shared/pr-ship.md`](../skills/pack-shared/pr-ship.md).

## Security

Do not open a public issue for vulnerabilities. See [SECURITY.md](SECURITY.md).

## License

Contributions are accepted under the [MIT License](../LICENSE).

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
for how agents should work live in skill doctrines (especially `/taste` and
`/architecture`) and the must-follow contract
[`skills/pack-shared/standards.md`](../skills/pack-shared/standards.md). Chat
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
Cursor plugin is optional and does not add a separate ruleset. Installed skills
must follow taste and architecture. ESLint and
Prettier templates live in
[`skills/setup-toolkit/templates/`](../skills/setup-toolkit/templates/) and are
copied into **app** repos by `/setup-toolkit` — they are not run from this
markdown pack.

## How to change skills

- Prefer improving an existing skill over adding a new one.
- Numbered how-to lives in `SKILL.md`. Put durable rules in `doctrine.md` and
  detail in `reference.md` / `examples.md`.
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

Before you commit, run this repo’s lint and tests when those scripts exist, and
fix failures first. A red local run is a red PR. This pack itself has no lint
or test CI; app repos that use `/setup-toolkit` do (`lint`, `test` or
`test:quality`). Never skip hooks (`--no-verify`) unless you were asked to.

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

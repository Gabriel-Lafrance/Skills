# Contributing

Thanks for helping improve **Gabriel Lafrance Skills** — an engineering toolkit
for Cursor.

By participating, you agree to follow the [Code of Conduct](CODE_OF_CONDUCT.md).

## What this repo is

A Cursor **plugin toolkit**: skills under [`skills/`](../skills/), plugin rules
under [`rules/`](../rules/), agents under [`agents/`](../agents/), and commands
under [`commands/`](../commands/). Pack layout and authoring rules live in
[`how-to.md`](../how-to.md). Standards for how agents should work live in skill
doctrines (especially `/taste` and `/architecture`), the must-follow contract
[`skills/pack-shared/standards.md`](../skills/pack-shared/standards.md), and the
plugin rules (especially
[`rules/gold-standards.mdc`](../rules/gold-standards.mdc)). Do not paste those
rules into User Rules when the plugin is installed.

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

The Cursor plugin loads [`rules/`](../rules/) automatically. Installed skills
must follow taste and architecture even if a rule is toggled off. ESLint and
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

Open a PR against `main` using the pull request template:

- **What changed**
- **Change diagram** (Mermaid; Before/After for rework)
- **How to QA**
- **Demo** (Browser screenshots of the changed screen, plus a review canvas
  when the change is visual). Pictures for reviewers — not a test pass.

Agents that open the PR — `/publish`, `/just-do-it`, `/goal` ship, or a cloud
agent — follow [`skills/pack-shared/pr-ship.md`](../skills/pack-shared/pr-ship.md).

## Security

Do not open a public issue for vulnerabilities. See [SECURITY.md](SECURITY.md).

## License

Contributions are accepted under the [MIT License](../LICENSE).

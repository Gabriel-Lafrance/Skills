# Contributing

Thanks for helping improve **Gabriel Lafrance Skills** — Cursor agent skills for
real engineering work.

By participating, you agree to follow the [Code of Conduct](CODE_OF_CONDUCT.md).

## What this repo is

Markdown skills under [`skills/`](../skills/). Pack layout and authoring rules
live in [`how-to.md`](../how-to.md). Standards for how agents should work live
in skill doctrines (especially `/taste` and `/architecture`) and
[`rules/ultimate-gold-standards.mdc`](../rules/ultimate-gold-standards.mdc).

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

Optional: paste the body of
[`rules/ultimate-gold-standards.mdc`](../rules/ultimate-gold-standards.mdc)
(without YAML frontmatter) into **Cursor Settings → Rules → User Rules**.

## How to change skills

- Prefer improving an existing skill over adding a new one.
- Keep `SKILL.md` thin; put durable rules in `doctrine.md` and detail in
  `reference.md` / `examples.md`.
- Dual skills: follow [`skills/pack-shared/variants.md`](../skills/pack-shared/variants.md)
  — do not invent a missing `standalone.md` / `flow.md` process.
- Shared contracts (`asking`, `variants`, execution context) live under
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

## Security

Do not open a public issue for vulnerabilities. See [SECURITY.md](SECURITY.md).

## License

Contributions are accepted under the [MIT License](../LICENSE).

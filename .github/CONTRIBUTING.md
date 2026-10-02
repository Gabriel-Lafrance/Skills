# Contributing

Thanks for helping improve **Gabriel Lafrance Skills**, an engineering toolkit
for Claude, Cursor, and other harnesses.

By participating, you agree to follow the [Code of Conduct](CODE_OF_CONDUCT.md).

## What this repo is

Skills under [`skills/`](../skills/). The always-on contract is
[`AGENTS.md`](../AGENTS.md) for every harness, including Cursor: a short index
that points at the rule files in [`skills/rules/`](../skills/rules/SKILL.md). There is no
Cursor rules copy. An optional Cursor plugin ships the same skills, plus
[`commands/`](../commands/).
Pack layout and authoring rules live in [`how-to.md`](../how-to.md). Standards
for how agents should work live in
[`skills/rules/code-quality.md`](../skills/rules/code-quality.md) and
[`skills/rules/code-structure.md`](../skills/rules/code-structure.md), with
examples beside them. Every skill links both files. Chat
replies follow [`skills/rules/writing-style.md`](../skills/rules/writing-style.md). Do not paste `AGENTS.md` into a
User Rules box, and do not add a project `CLAUDE.md`. `/setup-gabriel-skills`
installs the other skills and places `AGENTS.md` where the harness reads it. It does not write ESLint or Prettier.

## Before you start

1. Search [existing issues](https://github.com/Gabriel-Lafrance/Skills/issues)
   and PRs so we do not duplicate work.
2. For larger changes, open an issue first and describe the problem and
   proposed approach.
3. Keep changes focused: one concern per PR when practical.

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
`npx skills@latest add gabriel-lafrance/skills@setup-gabriel-skills -g -y`, then
`/setup-gabriel-skills`. That skill asks where the skills and `AGENTS.md` go. It does not write
`AGENTS.md` from memory, ESLint, or Prettier. Installed skills must apply
`rules/code-quality.md` and `rules/code-structure.md`.

## How to change skills

- Prefer improving an existing skill over adding a new one.
- Numbered how-to lives in `SKILL.md`. Put durable rules in `doctrine.md` and
  detail in `reference.md` / `examples.md` ([Skill file layout](#skill-file-layout)).
  Always-on rules live in `skills/rules/`, not in a skill doctrine.
- The pack holds rules (how things are done, in `skills/rules/`) and skills
  (procedures the user starts). Asking, plain language, execution context,
  testing, and shipping are rules in `skills/rules/` so `npx skills` installs
  them. A contract only one skill uses lives in that skill's folder.
- Teach principles in prose; avoid steering agents with a catalog of concrete
  product examples when the skill should stay principle-first.

See [`how-to.md`](../how-to.md) for folder layout, frontmatter, and publish notes.

### Skill file layout

Every `skills/*/doctrine.md` uses these H2s, in this order, with these names.
Rule files in `skills/rules/` and contracts such as `skills/review/contract.md`
are not doctrine; a contract that defines a return shape still keeps Job, Owns, and
Output.

| Order | H2 | What goes here |
| --- | --- | --- |
| 1 | **Job** | One sentence. What this file is for. |
| 2 | **Owns** | What this skill decides. |
| 3 | **Does not own** | What it leaves to others, plus a link to the file that owns it. |
| 4 | **Bars** | Canonical definitions only. Tables. No numbered how-to. |
| 5 | **Output** | Artifact to emit, or `none (see SKILL.md)`. |
| 6 | **Apply** | When this changes the work, and when to keep the existing shape. |
| 7 | **Anti-patterns** | Patterns to avoid, one line each. |

- Extra detail goes under **Bars** as `###` subheads, or in `examples.md` / `reference.md`.
- Numbered process steps belong in `SKILL.md`, not doctrine.
- Link another skill's Bars instead of restating them, and name the rule key inline where it helps (`quality:keep-jobs-apart`).
- When a section has nothing to say, write an explicit `none` line so a reader knows the file was not cut off.

### Change a rule

1. Edit the rule in its file under [`skills/rules/`](../skills/rules/SKILL.md).
   Keep cite keys and headings stable so `quality:*`, `structure:*`, and
   `ux:*` links still resolve.
2. If the **Read when** index or the Rules section changes, edit root
   [`AGENTS.md`](../AGENTS.md). There is no second copy.
3. Bump the version in
   [`.cursor-plugin/plugin.json`](../.cursor-plugin/plugin.json),
   [`.cursor-plugin/marketplace.json`](../.cursor-plugin/marketplace.json),
   [`.claude-plugin/plugin.json`](../.claude-plugin/plugin.json),
   [`.claude-plugin/marketplace.json`](../.claude-plugin/marketplace.json),
   [`.agents/plugins/marketplace.json`](../.agents/plugins/marketplace.json),
   and the first line of `AGENTS.md` (`<!-- gabriel-skills-agents v2.4.2 -->`)
   together.
4. There is no changelog file. The PR description is the changelog: say what
   changed and why, so a user sent to the merged PRs can follow it.

## Branch and PR

Use the branch name from [`skills/rules/shipping.md`](../skills/rules/shipping.md):

```text
feature|tweak|bug|refactor|chore/<ticket-or-no-ticket>-<slug>
```

Create that branch from the base commit with `git switch --detach <base-sha>`,
then `git switch -c <name>` (or `git switch --no-track -c`). Do not let it
track `dev`, `main`, or `master`. Push `HEAD:refs/heads/<name>`. A branch cut
from `dev` is its own ref: the push does not update `dev`, so it does not
take `dev`'s protection. Steps live in
[`skills/rules/shipping.md`](../skills/rules/shipping.md#process).

Before a push that opens a PR, or a commit or push on a branch that already
has an open PR, run that repo's CI in your environment and fix failures
first. A red push spends CI for nothing. This pack itself has no lint or
test CI; app repos that have their own lint and test scripts do, and the
check is the mirror in
[`skills/rules/shipping.md`](../skills/rules/shipping.md#ci-mirror). Do not
run that suite on a commit you are not pushing. Never skip hooks
(`--no-verify`) unless you were asked to.

Open a PR against `main` using the pull request template:

- **What changed**
- **Change diagram** (Mermaid; Before/After for rework)
- **How to QA**
- **Blast radius and merge danger**, last after any Notes or other details; follow the [shared assessment guidance](../skills/rules/shipping-templates.md#blast-radius-and-merge-danger).

Agents that open the PR follow [`skills/rules/shipping.md`](../skills/rules/shipping.md).

## Security

Do not open a public issue for vulnerabilities. See [SECURITY.md](SECURITY.md).

## License

Contributions are accepted under the [MIT License](../LICENSE).

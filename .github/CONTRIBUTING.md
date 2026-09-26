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
User Rules box, and do not add a project `CLAUDE.md`. `/setup-toolkit` is what
installs the contract into an app and into harness homes that already exist.

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
`npx skills@latest add gabriel-lafrance/skills@setup-toolkit -g -y`, then
`/setup-toolkit`. That skill asks where skills and `AGENTS.md` go. Installed
skills must apply `rules/code-quality.md` and `rules/code-structure.md`. ESLint
and Prettier templates live in
[`skills/setup-toolkit/templates/`](../skills/setup-toolkit/templates/) and are
copied into **app** repos only when the user says yes. They are not run from
this markdown pack.

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
| 3 | **Does not own** | What it must not decide, plus a link to the file that does. |
| 4 | **Cite keys** | `skill:slug` to heading. If none: `none (uses quality:* and structure:*)`. |
| 5 | **Bars** | Canonical definitions only. Tables. No numbered how-to. |
| 6 | **Output** | Artifact to emit, or `none (see SKILL.md)`. |
| 7 | **Apply** | When this changes the work, and when to keep the existing shape. |
| 8 | **Anti-patterns** | What this skill must not do. |

- Extra detail goes under **Bars** as `###` subheads, or in `examples.md` / `reference.md`.
- Numbered process steps belong in `SKILL.md`, not doctrine.
- Do not restate another skill's Bars. Cite the key (`quality:keep-jobs-apart`).
- Omit a section only with an explicit `none` line, so a reader does not think the file was cut off.

### Change a rule

1. Edit the rule in its file under [`skills/rules/`](../skills/rules/SKILL.md).
   Keep cite keys and headings stable so `quality:*`, `structure:*`, and
   `ux:*` links still resolve.
2. If the **Read when** index or the hard rules change, edit root
   [`AGENTS.md`](../AGENTS.md), then copy it to
   [`skills/setup-toolkit/templates/AGENTS.md`](../skills/setup-toolkit/templates/AGENTS.md)
   so the two files stay identical.
3. Bump the version in
   [`.cursor-plugin/plugin.json`](../.cursor-plugin/plugin.json),
   [`.cursor-plugin/marketplace.json`](../.cursor-plugin/marketplace.json), and
   the first line of `AGENTS.md` (`<!-- gabriel-skills-agents v2.0.0 -->`)
   together, then copy `AGENTS.md` to the template again. `/setup-toolkit`
   uses that marker to refresh out-of-date installs.
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
test CI; app repos that use `/setup-toolkit` do (`lint`, `test`), and the
check is the mirror in
[`skills/rules/shipping.md`](../skills/rules/shipping.md#ci-mirror). Do not
run that suite on a commit you are not pushing. Never skip hooks
(`--no-verify`) unless you were asked to.

Open a PR against `main` using the pull request template:

- **What changed**
- **Change diagram** (Mermaid; Before/After for rework)
- **How to QA**

Agents that open the PR follow [`skills/rules/shipping.md`](../skills/rules/shipping.md).

## Security

Do not open a public issue for vulnerabilities. See [SECURITY.md](SECURITY.md).

## License

Contributions are accepted under the [MIT License](../LICENSE).

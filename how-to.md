# How to maintain this pack

For **authors** of Gabriel Lafrance Skills, not for end users installing the pack.

## Layout

```text
AGENTS.md                # always-on index for every harness, including Cursor; points at skills/rules/
.cursor-plugin/
  plugin.json            # optional Cursor plugin manifest (skills, commands)
  marketplace.json       # Team marketplace import
commands/                # Slash commands (setup-toolkit)
skills/
  rules/                 # rule files AGENTS.md points to (NOT user-invoked)
    SKILL.md             # required so npx skills installs this folder
    code-quality.md      # code quality rules (quality:* cite keys), SOLID, futureproofing
    code-quality-examples.md   # good vs bad snippets for code-quality.md
    code-structure.md    # code structure rules (structure:* cite keys)
    code-structure-examples.md # good vs bad shapes for code-structure.md
    planning.md          # grill first, Before/After change diagram
    user-experience.md   # every UI and UX rule (ux:*), React and UI, docs/design.md contract
    writing-style.md     # no em dash, Unslop
    testing.md           # no drive-by tests
    shipping.md          # branch names and PR hard rules
    tooling.md           # lint, format, CI, verify terminals first
  pack-shared/           # installable shared contracts (NOT user-invoked)
    SKILL.md             # required so npx skills installs this folder
    asking.md            # how to ask the user (batch Questions)
    plain-language.md    # talk to humans in ordinary words
    execution-context.md # in-chat execution context
    review-contract.md   # shared review evidence and finding rules
    ship.md              # branch and PR templates and steps
    pr-ship.md           # every agent that opens a PR (create tool, standalone branch, green before push)
  review/                # /review: a local branch diff or an open GitHub PR
  setup-toolkit/
    templates/           # ESLint / Prettier files copied into app repos
  <skill-name>/
    SKILL.md             # required: frontmatter + how-to
    doctrine.md          # optional: durable rules (fixed H2 schema)
    examples.md          # optional: good vs bad
    reference.md         # optional: deep detail (progressive disclosure)
LICENSE
README.md                # install + user-facing catalog
how-to.md                # this file
```

Skill folder names: `lowercase-with-hyphens` (e.g. `grill-me`, `create-test`).

**Install rule:** `npx skills` only copies folders that contain `SKILL.md`. Pack-wide contracts must live under `pack-shared/` (or another skill folder). Bare `skills/*.md` files are **not** installed; other skills will fail looking for `../pack-shared/...`.

**Plugin vs `npx skills`:** the Cursor plugin is optional. It auto-discovers `commands/` and `skills/`. It does not ship a Cursor rules folder. `npx skills` still copies **only** skill folders, and can target Claude, Cursor, or both (`-a claude`, `-a cursor`). It does not install root `AGENTS.md`. [`skills/setup-toolkit/templates/AGENTS.md`](./skills/setup-toolkit/templates/AGENTS.md) is the same contract so the skill can install it. `/setup-toolkit` asks whether that file goes in the app, in existing harness homes, or both. Cursor reads the repo file. Do not add a `.cursor/rules` or `.mdc` copy. Put files a skill copies into an app **inside that skill folder**.

Do not add plugin **hooks** unless the pack explicitly wants scripts on agent/Tab events. Do not add **MCP** unless there is a real server to ship. ESLint and Prettier are app-repo configs, not plugin components.

## Skill folders

Each skill is `SKILL.md` plus optional `doctrine.md`, `examples.md`, and `reference.md`.

Numbered how-to lives in `SKILL.md`. Nested vs one-off (who ships, who asks the next question) is a short fork in that file. Do not paste pack-wide ask rules. Link [`asking.md`](./skills/pack-shared/asking.md). User starts that must not nest (`/review` on a GitHub PR, `/write-ticket`, `/setup-toolkit`) say that in `SKILL.md`. `/create-test` stays a user start. `/task` may continue it only after the user accepts that task's lock briefs.

## Frontmatter

```yaml
---
name: skill-name          # matches folder name
description: >-
  Third person. WHAT it does + WHEN to use it. Keep under 1024 chars.
  Include trigger terms users actually say.
disable-model-invocation: true   # required on every skill except ask-gabriel
---
```

**Only [`ask-gabriel`](./skills/ask-gabriel/SKILL.md)** may omit `disable-model-invocation`: it is the sole auto-invokable router.

## Shared contracts

- **Plain language:** every skill that talks to the user links [`pack-shared/plain-language.md`](./skills/pack-shared/plain-language.md). Chat uses ordinary words. Named principles use **plain (Classic)**, for example `keep this simple (KISS)`. Never acronym-only (`SoC violation`) and never the paraphrase without the classic name. Pack jargon (a bare Rule 1) stays banned.
- **Unslop:** chat replies follow the **Unslop** section of [`skills/rules/writing-style.md`](./skills/rules/writing-style.md#unslop). Not a user skill. Do not add `/unslop`. `/setup-toolkit` copies `AGENTS.md`.
- **Standards:** every pack skill except `/ask-gabriel` links and applies [`skills/rules/code-quality.md`](./skills/rules/code-quality.md) and [`skills/rules/code-structure.md`](./skills/rules/code-structure.md) on every run. `/ask-gabriel` stays thin and does not restate those rules.
- **Asking:** every skill that needs decisions links [`pack-shared/asking.md`](./skills/pack-shared/asking.md): batch Questions, mark `recommended`, one-row `Reply like: 1a 2b 3c` (codes only, no descriptions). Do not add skill-specific freeform grill exceptions.
- **Process:** numbered how-to lives in that skill’s `SKILL.md`. Nested vs one-off is a short fork in that file, not a second process file.
- **Execution context:** parent orchestrators link [`execution-context.md`](./skills/pack-shared/execution-context.md), keep outcome, decisions, rules that must stay true, scope, and handoff visible in chat. Do not create agent-owned runtime trees.
- **Review:** review skills link [`review-contract.md`](./skills/pack-shared/review-contract.md) for evidence, modes, finding records, the review output fence, correctness hunt, and severity mapping.
- **PR ship:** every agent that creates a GitHub PR follows [`skills/rules/shipping.md`](./skills/rules/shipping.md), [`ship.md`](./skills/pack-shared/ship.md), and [`pr-ship.md`](./skills/pack-shared/pr-ship.md): the harness pull-request tool when it has one, otherwise `gh`, a standalone branch that does not track `dev`, and the CI mirror in this environment before a push that opens or updates a PR.
- **Do not** put shared contracts at `skills/*.md`: they will not install.
- **Tests:** **no skill writes or edits test files** except [`/create-test`](./skills/create-test/SKILL.md) (the agent writes them only after the user started that skill, or after the user accepted a `/task` behavior-lock brief; ordinary edits do not get tests). `/task` suggests locks after grill Locked and waits; the user can refuse every test. [`/review`](./skills/review/SKILL.md) may still recommend a lock the task did not offer (tell the user, never auto-invoke). `/task` build slices, `/analyze`, and `/write-ticket` do not write tests or start `/create-test`. The always-on bar is [`skills/rules/testing.md`](./skills/rules/testing.md).

## No visual tooling

This pack does not use Cursor's Browser, review canvas, screenshots, or videos. Acceptance evidence is path walks and terminal output. PR bodies are text (type, ticket, what changed, Change diagram, How to QA, Notes). Do not add skills or contracts that open a browser, capture screens, or produce canvases.

## Add a skill

1. Create `skills/<skill-name>/SKILL.md` with frontmatter above. Put numbered how-to in that file. If nested vs one-off differs (who ships, who asks the next question), put that fork in `SKILL.md`. Inner steps say they are not a typical user start. User starts that must not nest under `/task` say so in `SKILL.md`. `/create-test` is the exception in the skill-folders section: `/task` continues it only after the user accepts the lock briefs.
2. Add `doctrine.md` / `examples.md` / `reference.md` only when progressive disclosure helps (bars vs examples vs deep detail). Every `doctrine.md` follows the [skill file layout](./.github/CONTRIBUTING.md#skill-file-layout): Job, Owns, Does not own, Cite keys, Bars, Output, Apply, Anti-patterns, in that order. Process steps go in `SKILL.md`, not doctrine. Code quality and code structure rules live in [`skills/rules/code-quality.md`](./skills/rules/code-quality.md) and [`skills/rules/code-structure.md`](./skills/rules/code-structure.md), not in a skill doctrine.
3. Link `asking.md` if the skill asks the user anything. Link `rules/code-quality.md` and `rules/code-structure.md` on every skill except `/ask-gabriel`. Link `plain-language.md` if the skill talks to the user.
4. Wire discovery:
   - User-facing → [`README.md`](./README.md) catalog + [`ask-gabriel`](./skills/ask-gabriel/SKILL.md) on-ramps.
   - Inner step → only the orchestrator `SKILL.md` / doctrine that should call it (do not put it on the README as a typical entry).
5. Smoke-check locally:

```bash
npx skills@latest add . --list
```

## Add a command

Do not add a root or `.cursor/rules` folder or a `.mdc` file. The always-on index is [`AGENTS.md`](./AGENTS.md) for every harness, including Cursor; the rule text lives in `skills/rules/`. Do not add a `CLAUDE.md` in the pack or an app.
- **Command:** `commands/<name>.md`. Do not create a command with the same name as an existing skill unless they share one job (today: `setup-toolkit` only).
- **Templates an agent must copy into an app**: live inside that skill’s folder so `npx skills` installs them. `/setup-toolkit` copies ESLint, Prettier, `eslint-plugin-no-emdash.mjs`, and `.vscode/` workspace files **only when the user said yes**. Missing `docs/design.md` is written from the routes in code before UI work ([`ux:initialization`](./skills/rules/user-experience.md#initialization)), not by copying a stub from this pack. `/setup-toolkit` does not write that file.

## Conventions

- One skill = one job. Prefer new skill over bloating an existing one.
- Doctrine files share one layout ([skill file layout](./.github/CONTRIBUTING.md#skill-file-layout)). Cite another skill's keys instead of restating its Bars.
- Harness tools: use the plan tool after the grill when the harness has one, otherwise write the plan in chat. Open a pull request with the harness tool when it has one, otherwise `gh` (`pack-shared/pr-ship.md`). Acceptance evidence stays path walks and terminal output.
- Teach in ordinary words, no explainer-video links in skill bodies. Do not make agents dump acronyms at the user (`pack-shared/plain-language.md`).
- No secrets in skills.
- New long-running orchestrators should reuse `pack-shared/asking.md`, `pack-shared/execution-context.md`, and `pack-shared/pr-ship.md` without editing those files for skill-specific names. Any orchestrator that opens a PR must follow `pr-ship.md`; do not fork a private ship recipe into that skill.
- Never create `.agents/temp`, status/registry files, or hidden process artifacts by default. Persist only an artifact the user explicitly requested at a user-approved destination.
- Do not list `/pack-shared` or `/rules` in the README catalog. They are install vehicles, not on-ramps.
- Do not add Cursor-only rules. The code quality and code structure rules live in `skills/rules/code-quality.md` and `skills/rules/code-structure.md`, with their examples beside them. Do not keep a second copy in a skill doctrine.
- Do not add ESLint or Prettier to **this** markdown repo; they belong in consumer apps via `/setup-toolkit`.
- When you change pack-root `AGENTS.md`, copy the same file to `skills/setup-toolkit/templates/AGENTS.md` in that change. Setup uses the root file when the pack is on disk, and the template when only the skill was installed.

## Publish / install

The contract is [`AGENTS.md`](./AGENTS.md) plus the rule files in `skills/rules/`. The Cursor plugin is optional. After you push a plugin change, refresh the marketplace (or Auto Refresh).

Skills from GitHub, for every harness the CLI already sees:

```bash
npx skills@latest add gabriel-lafrance/skills@setup-toolkit -g -y
```

Then run `/setup-toolkit` in an app. Phase one verifies, then installs the rest of this pack and `AGENTS.md` into the repo or user data (it asks). Lint is a later question.

To copy every skill without running setup:

```bash
npx skills@latest add gabriel-lafrance/skills --all -g
npx skills@latest update -g -y
```

Use `-a claude` or `-a cursor` alone when you only need one harness.

After you push, `npx skills` users refresh with `update`. The skills.sh on-ramp is [`setup-toolkit`](https://skills.sh/gabriel-lafrance/skills/setup-toolkit). While developing the pack itself, list from the repo root with `npx skills@latest add . --list`.

### Cursor plugin / marketplace

This repo is one Cursor plugin (`gabriel-skills`). Keep it **one plugin** until a second installable product is truly independent (do not split one plugin per skill; they share `pack-shared`).

Manifests live in [`.cursor-plugin/`](./.cursor-plugin/) (`plugin.json` + `marketplace.json`). After you push, refresh the marketplace (or turn on Auto Refresh). `npx skills` is unchanged and still skills-only.

Plugin components (folder discovery, or explicit paths in `plugin.json`):

| Component | This pack |
| --- | --- |
| Skills | `skills/` |
| Commands | `commands/`: do not alias every skill (avoids slash-command collisions with Cursor builtins and with skills) |
| Hooks / MCP | none until there is a concrete server or an explicit format-on-edit decision |

### Contract

[`AGENTS.md`](./AGENTS.md) is the always-on index for every harness, including Cursor and including chats that never invoke a skill. It tells agents which file in [`skills/rules/`](./skills/rules/SKILL.md) to open for which job. [`skills/rules/code-quality.md`](./skills/rules/code-quality.md) and [`skills/rules/code-structure.md`](./skills/rules/code-structure.md) are the code quality and code structure rules. Every skill except `/ask-gabriel` links them in its Read when list.

- Do **not** add a root `rules/` folder, a `.mdc` file, or a `.cursor/rules` copy. Rule text lives only in `skills/rules/`.
- Do **not** paste `AGENTS.md` into a User Rules box.
- Rule text lives in `skills/rules/`, one file per topic. `AGENTS.md` is only the index: a short intro, how to find the pack, the **Read when** table, the hard rules that hold with no file open, and the Conflict line. Change a rule in its `skills/rules/` file. Do not grow `AGENTS.md` back into the full rulebook, and keep it under 8,192 bytes.
- Do **not** copy the code quality or code structure rules into a skill doctrine. The Unslop catalog lives in `skills/rules/writing-style.md` because it is not a user skill.
- When the index or the hard rules change, edit root `AGENTS.md` and copy it to `skills/setup-toolkit/templates/AGENTS.md` in the same change so the two stay identical.
- Do **not** add a `CLAUDE.md` in the pack or the app.
- `npx skills` does not install root `AGENTS.md`. The setup skill ships `templates/AGENTS.md` (keep it identical to the pack-root file). `/setup-toolkit` copies that contract into the destinations the user chose: the app, existing harness homes, or both. Refresh only when the app file is missing or already the pack copy (marker prefix `gabriel-skills-agents`); an older or unversioned pack copy is refreshed and reported as out of date. A different app `AGENTS.md` stays put. Cursor is the repo file. It does not create a harness directory the user does not have, and it does not add a project `CLAUDE.md`. ESLint and Prettier wait for a yes.

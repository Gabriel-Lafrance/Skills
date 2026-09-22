# How to maintain this pack

For **authors** of Gabriel Lafrance Skills — not for end users installing the pack.

## Layout

```text
AGENTS.md                # always-on contract for every harness, including Cursor
.cursor-plugin/
  plugin.json            # optional Cursor plugin manifest (skills, agents, commands)
  marketplace.json       # Team marketplace import
agents/                  # Specialist configs (same roles in every harness)
commands/                # Slash commands (setup-toolkit)
skills/
  pack-shared/           # installable shared contracts (NOT user-invoked)
    SKILL.md             # required so npx skills installs this folder
    asking.md            # how to ask the user (batch Questions)
    standards.md         # must follow taste + architecture on every skill run
    plain-language.md    # talk to humans in ordinary words
    execution-context.md # in-chat parent / worker context
    subagents.md         # what vs how; explorer finds; analyzer judges; Worker Brief
    review-contract.md   # shared review evidence and finding rules
    doctrine-schema.md   # H2 order every skills/*/doctrine.md must use
    pr-ship.md           # every agent that opens a PR (create-tool choice)
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

Skill folder names: `lowercase-with-hyphens` (e.g. `grill-me`, `code-review`).

**Install rule:** `npx skills` only copies folders that contain `SKILL.md`. Pack-wide contracts must live under `pack-shared/` (or another skill folder). Bare `skills/*.md` files are **not** installed — other skills will fail looking for `../pack-shared/...`.

**Plugin vs `npx skills`:** the Cursor plugin is optional. It auto-discovers `agents/`, `commands/`, and `skills/`. It does not ship a rules folder. `npx skills` still copies **only** skill folders, and can target Claude, Cursor, or both (`-a claude`, `-a cursor`). It does not install root `AGENTS.md`. [`skills/setup-toolkit/templates/AGENTS.md`](./skills/setup-toolkit/templates/AGENTS.md) is the same contract so the skill can install it. `/setup-toolkit` copies that file into the app and into each harness home that already exists. Cursor reads the repo file. Do not add a `.cursor/rules` or `.mdc` copy. Put files a skill copies into an app **inside that skill folder**.

Do not add plugin **hooks** unless the pack explicitly wants scripts on agent/Tab events. Do not add **MCP** unless there is a real server to ship. ESLint and Prettier are app-repo configs, not plugin components.

## Skill folders

Each skill is `SKILL.md` plus optional `doctrine.md`, `examples.md`, and `reference.md`.

Numbered how-to lives in `SKILL.md`. Nested vs one-off (who ships, who asks the next question) is a short fork in that file. Do not paste pack-wide ask rules — link [`asking.md`](./skills/pack-shared/asking.md). Worker steps (`/implement`, `/design`, `/trackers`, `/split-task`) say in `SKILL.md` they are not a typical user start (`/design` is also a user start for capturing `docs/design.md`). User starts that must not nest (`/pr-review`, `/publish`, `/just-do-it`, `/write-ticket`, `/create-test`, `/setup-toolkit`) say that in `SKILL.md`.

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

**Only [`ask-gabriel`](./skills/ask-gabriel/SKILL.md)** may omit `disable-model-invocation` — it is the sole auto-invokable router.

## Shared contracts

- **Plain language:** every skill that talks to the user links [`pack-shared/plain-language.md`](./skills/pack-shared/plain-language.md). Chat uses ordinary words. Named principles use **plain (Classic)** — `keep this simple (KISS)`. Never acronym-only (`SoC violation`) and never the paraphrase without the classic name. Pack jargon (INV-1, Worker Brief) stays banned.
- **Unslop:** chat replies follow the **Unslop** section of [`AGENTS.md`](./AGENTS.md). Not a skill. Do not add `/unslop`. `/setup-toolkit` copies `AGENTS.md`.
- **Standards:** every pack skill except `/ask-gabriel` links [`pack-shared/standards.md`](./skills/pack-shared/standards.md) and applies the **Taste** and **Architecture** sections of [`AGENTS.md`](./AGENTS.md) on every run. `/ask-gabriel` stays thin and does not restate those sections.
- **Asking:** every skill that needs decisions links [`pack-shared/asking.md`](./skills/pack-shared/asking.md) — batch Questions, mark `recommended`, one-row `Reply like: 1a 2b 3c` (codes only, no descriptions). Do not add skill-specific freeform grill exceptions.
- **Process:** numbered how-to lives in that skill’s `SKILL.md`. Nested vs one-off is a short fork in that file, not a second process file.
- **Execution context:** parent orchestrators link [`execution-context.md`](./skills/pack-shared/execution-context.md), keep outcome, decisions, Active Rules, scope, and handoff visible in chat, and compile that context into each worker brief. Do not create agent-owned runtime trees.
- **Subagents:** parents link [`subagents.md`](./skills/pack-shared/subagents.md) for what vs how, the specialist catalog, injected Worker Brief, parallel lanes, and after-wave integration (there is no `/orchestrate` skill, no architect worker, and no fixed spawn order).
- **Review:** review skills link [`review-contract.md`](./skills/pack-shared/review-contract.md) for evidence, modes, finding records, the review output fence, correctness hunt, and severity mapping.
- **PR ship:** every agent that creates a GitHub PR (not only `/publish`)
  follows [`pr-ship.md`](./skills/pack-shared/pr-ship.md): the harness
  pull-request tool when it has one, otherwise `gh`.
- **Do not** put shared contracts at `skills/*.md` — they will not install.
- **Tests:** **no skill writes or edits test files** except [`/create-test`](./skills/create-test/SKILL.md) (that labor is **always** `tester`, the main agent never writes tests) and [`/setup-toolkit`](./skills/setup-toolkit/SKILL.md) copying quality-gate templates (`complexity.test.mjs`, `cyclomatic-cap.mjs`, `principle-gate.test.mjs`, `principle-scan.mjs`, `knip.json`, `knip.test.mjs`, `stryker.conf.json`). Only [`/code-review`](./skills/code-review/SKILL.md) and [`/pr-review`](./skills/pr-review/SKILL.md) may **recommend** `/create-test` (tell the user, never auto-invoke). `/task`, `/implement`, `/design`, `/analyze`, `/write-ticket`, `/publish`, `/just-do-it`, etc. must not create tests or call `/create-test`.

## No visual tooling

This pack does not use Cursor's Browser, review canvas, screenshots, or videos. Acceptance evidence is path walks and terminal output. PR bodies are text (type, ticket, what changed, Change diagram, How to QA, Notes). Do not add skills or contracts that open a browser, capture screens, or produce canvases.

## Add a skill

1. Create `skills/<skill-name>/SKILL.md` with frontmatter above. Put numbered how-to in that file. If nested vs one-off differs (who ships, who asks the next question), put that fork in `SKILL.md`. Worker steps say they are not a typical user start. User starts that must not nest under `/task` say so in `SKILL.md`.
2. Add `doctrine.md` / `examples.md` / `reference.md` only when progressive disclosure helps (bars vs examples vs deep detail). Every `doctrine.md` except taste and architecture follows [`pack-shared/doctrine-schema.md`](./skills/pack-shared/doctrine-schema.md): Job, Owns, Does not own, Cite keys, Bars, Output, Apply, Anti-patterns, in that order. Process steps go in `SKILL.md`, not doctrine. Taste and Architecture rules live in [`AGENTS.md`](./AGENTS.md). Their `doctrine.md` files only point there. Convex verify, landing UI, SOLID, and futureproofing detail live in [`skills/taste/reference.md`](./skills/taste/reference.md).
3. Link `asking.md` if the skill asks the user anything. Link `standards.md` on every skill except `/ask-gabriel`. Link `plain-language.md` if the skill talks to the user.
4. Wire discovery:
   - User-facing → [`README.md`](./README.md) catalog + [`ask-gabriel`](./skills/ask-gabriel/SKILL.md) on-ramps.
   - Internal worker step → only the orchestrator `SKILL.md` / doctrine that should call it (do not put it on the README as a typical entry).
5. Smoke-check locally:

```bash
npx skills@latest add . --list
```

## Add an agent or command

Do not add a `rules/` folder or a `.mdc` file. The always-on contract is [`AGENTS.md`](./AGENTS.md) for every harness, including Cursor. Do not add a `CLAUDE.md` in the pack or an app.

- **Agent:** `agents/<name>.md` with `name` + `description` frontmatter. One job. Tell it to apply the Taste and Architecture sections of `AGENTS.md`. The same role must stay in `pack-shared/subagents.md`, because other harnesses do not load `agents/`.
- **Command** — `commands/<name>.md`. Do not create a command with the same name as an existing skill unless they share one job (today: `setup-toolkit` only).
- **Templates an agent must copy into an app**: live inside that skill’s folder so `npx skills` installs them. `/setup-toolkit` copies ESLint, Prettier, `eslint-plugin-no-emdash.mjs`, `cyclomatic-cap.mjs`, `complexity.test.mjs`, `principle-gate.test.mjs`, `principle-scan.mjs`, `knip.json`, `knip.test.mjs`, `stryker.conf.json`, and `.vscode/` workspace files. Missing `docs/design.md` is initialized by `/design`, not by copying a stub from this pack.

## Conventions

- One skill = one job. Prefer new skill over bloating an existing one.
- Doctrine files share one schema ([`pack-shared/doctrine-schema.md`](./skills/pack-shared/doctrine-schema.md)), except `skills/taste/doctrine.md` and `skills/architecture/doctrine.md`, which point at the rules in `AGENTS.md`. Cite another skill's keys instead of restating its Bars.
- Harness tools: use the plan tool after the grill when the harness has one, otherwise write the plan in chat. Dispatch a specialist when the harness can spawn one, otherwise that role is its own pass (`pack-shared/subagents.md`). Open a pull request with the harness tool when it has one, otherwise `gh` (`pack-shared/pr-ship.md`). Acceptance evidence stays path walks and terminal output.
- Teach in ordinary words — no explainer-video links in skill bodies. Do not make agents dump acronyms at the user (`pack-shared/plain-language.md`).
- No secrets in skills.
- New long-running orchestrators should reuse `pack-shared/standards.md`, `pack-shared/asking.md`, `pack-shared/execution-context.md`, `pack-shared/subagents.md`, and `pack-shared/pr-ship.md` without editing those files for skill-specific names. Any orchestrator that opens a PR must follow `pr-ship.md`; do not fork a private ship recipe into that skill.
- Never create `.agents/temp`, status/registry files, or hidden process artifacts by default. Persist only an artifact the user explicitly requested at a user-approved destination.
- Do not list `/pack-shared` in the README catalog — it is an install vehicle, not an on-ramp.
- Do not add Cursor-only rules. The Taste and Architecture rules live in `AGENTS.md`. Do not keep a second copy in the skill doctrines. `/taste` and `/architecture` stay as the examples and the audit.
- Do not add ESLint or Prettier to **this** markdown repo; they belong in consumer apps via `/setup-toolkit`.
- When you change pack-root `AGENTS.md`, copy the same file to `skills/setup-toolkit/templates/AGENTS.md` in that change. Setup uses the root file when the pack is on disk, and the template when only the skill was installed.

## Publish / install

The contract is [`AGENTS.md`](./AGENTS.md). The Cursor plugin is optional. After you push a plugin change, refresh the marketplace (or Auto Refresh).

Skills from GitHub, for Claude, Cursor, or both:

```bash
npx skills@latest add Gabriel-Lafrance/Skills -a claude -a cursor -s '*' -g -y
npx skills@latest update -g -y
```

Use `-a claude` or `-a cursor` alone when you only need one harness.

After you push, `npx skills` users refresh with `update`. While developing the pack itself, list from the repo root with `npx skills@latest add . --list`.

### Cursor plugin / marketplace

This repo is one Cursor plugin (`gabriel-skills`). Keep it **one plugin** until a second installable product is truly independent (do not split one plugin per skill — they share `pack-shared`).

Manifests live in [`.cursor-plugin/`](./.cursor-plugin/) (`plugin.json` + `marketplace.json`). After you push, refresh the marketplace (or turn on Auto Refresh). `npx skills` is unchanged and still skills-only.

Plugin components (folder discovery, or explicit paths in `plugin.json`):

| Component | This pack |
| --- | --- |
| Skills | `skills/` |
| Agents | `agents/` (explorer, analyzer, implementer, designer, reviewer, pr-reviewer, tester). Same roles as `pack-shared/subagents.md` |
| Commands | `commands/` — do not alias every skill (avoids slash-command collisions with Cursor builtins and with skills) |
| Hooks / MCP | none until there is a concrete server or an explicit format-on-edit decision |

### Contract

[`AGENTS.md`](./AGENTS.md) is the always-on contract for every harness, including Cursor and including chats that never invoke a skill. The **Taste** and **Architecture** sections are the rules. Skills apply them via [`pack-shared/standards.md`](./skills/pack-shared/standards.md). `/taste` and `/architecture` are the examples and the audit.

- Do **not** add a `rules/` folder, a `.mdc` file, or a `.cursor/rules` copy.
- Do **not** paste `AGENTS.md` into a User Rules box.
- Do **not** copy the Taste or Architecture rules back into `skills/taste/doctrine.md` or `skills/architecture/doctrine.md`. Those files point at `AGENTS.md`. The Unslop catalog also lives in `AGENTS.md` because it is not a skill.
- Do **not** add a `CLAUDE.md` in the pack or the app.
- `npx skills` does not install root `AGENTS.md`. The setup skill ships `templates/AGENTS.md` (keep it identical to the pack-root file). `/setup-toolkit` copies that contract into the app when the app file is missing or already the pack copy (marker `gabriel-skills-agents`). A different app `AGENTS.md` stays put. It then writes only the harness homes that already exist (Claude import, Codex `AGENTS.md`, and the other rows in the setup reference). Cursor is the repo file. It does not create a harness directory the user does not have, and it does not add a project `CLAUDE.md`.

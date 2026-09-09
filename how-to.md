# How to maintain this pack

For **authors** of Gabriel Lafrance Skills — not for end users installing the pack.

## Layout

```text
.cursor-plugin/
  plugin.json            # Cursor plugin manifest
  marketplace.json       # Team marketplace import
rules/                   # Cursor plugin rules (.mdc only — no extra README)
  gold-standards.mdc     # alwaysApply — doctrine Reads, grill, diagrams
  no-emdash.mdc          # alwaysApply — dash characters
  unslop.mdc             # alwaysApply — chat-reply voice
  ship-work.mdc          # PRs / branches
  subagents.mdc          # Task bias
  project-tooling.mdc    # ESLint / Prettier in the app repo
agents/                  # Custom agent configs (explorer, architect, implementer, reviewer, pr-reviewer)
commands/                # Slash commands (setup-toolkit)
skills/
  pack-shared/           # installable shared contracts (NOT user-invoked)
    SKILL.md             # required so npx skills installs this folder
    asking.md            # how to ask the user (batch Questions)
    standards.md         # must follow taste + architecture on every skill run
    plain-language.md    # talk to humans in ordinary words
    execution-context.md # in-chat parent / worker context
    subagents.md         # Task bias, Worker Brief, spawn rules
    review-contract.md   # shared review evidence and finding rules
    doctrine-schema.md   # H2 order every skills/*/doctrine.md must use
    browser-evidence.md  # browser proof for UI acceptance
    pr-ship.md           # every agent that opens a PR (canvas + screenshots)
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

**Plugin vs `npx skills`:** the Cursor plugin auto-discovers `rules/`, `agents/`, `commands/`, and `skills/`. `npx skills` still copies **only** skill folders. Put any file a skill must copy into a consumer repo (ESLint/Prettier templates) **inside that skill folder**, not only at the plugin root.

**Rules folder:** only `.mdc` rule files. A `README.md` in `rules/` would be loaded as a rule. Document rules in [README.md](./README.md) and this file.

Do not add plugin **hooks** unless the pack explicitly wants scripts on agent/Tab events. Do not add **MCP** unless there is a real server to ship. ESLint and Prettier are app-repo configs, not plugin components.

## Skill folders

Each skill is `SKILL.md` plus optional `doctrine.md`, `examples.md`, and `reference.md`.

Numbered how-to lives in `SKILL.md`. Nested vs one-off (who ships, who asks the next question) is a short fork in that file. Do not paste pack-wide ask rules — link [`asking.md`](./skills/pack-shared/asking.md). Worker steps (`/implement`, `/trackers`, `/split-task`) say in `SKILL.md` they are not a typical user start. User starts that must not nest (`/pr-review`, `/publish`, `/just-do-it`, `/write-ticket`, `/create-test`, `/setup-toolkit`) say that in `SKILL.md`.

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
- **Unslop:** chat replies follow the plugin rule [`unslop.mdc`](./rules/unslop.mdc) (`alwaysApply`). Not a skill. Do not add `/unslop`. Toggle it in Customize. `npx skills` does not install it; pin `rules/*.mdc` with `/setup-toolkit` when needed without the plugin.
- **Standards:** every pack skill except `/ask-gabriel` links [`pack-shared/standards.md`](./skills/pack-shared/standards.md) and **Reads** `/taste` plus `/architecture` doctrines on every run. `/ask-gabriel` stays thin and does not load the bodies.
- **Asking:** every skill that needs decisions links [`pack-shared/asking.md`](./skills/pack-shared/asking.md) — batch Questions, mark `recommended`, one-row `Reply like: 1a 2b 3c` (codes only, no descriptions). Do not add skill-specific freeform grill exceptions.
- **Process:** numbered how-to lives in that skill’s `SKILL.md`. Nested vs one-off is a short fork in that file, not a second process file.
- **Execution context:** parent orchestrators link [`execution-context.md`](./skills/pack-shared/execution-context.md), keep outcome, decisions, Active Rules, scope, and handoff visible in chat, and compile that context into each worker brief. Do not create agent-owned runtime trees.
- **Subagents:** parents link [`subagents.md`](./skills/pack-shared/subagents.md) for Task bias, Worker Brief, parallel lanes, and after-wave integration (there is no `/orchestrate` skill).
- **Review:** review skills link [`review-contract.md`](./skills/pack-shared/review-contract.md) for evidence, modes, finding records, Wave 1 / Wave 2 fences, correctness hunt, and severity mapping.
- **Browser evidence:** UI acceptance proof links [`browser-evidence.md`](./skills/pack-shared/browser-evidence.md). Do not use it to fill a PR Demo section.
- **PR ship:** every agent that creates a GitHub PR (not only `/publish`)
  follows [`pr-ship.md`](./skills/pack-shared/pr-ship.md) — Cursor review
  canvas, Browser screenshots in the body (not a UI test pass), Cursor PR
  tool when available.
- **Do not** put shared contracts at `skills/*.md` — they will not install.
- **Tests:** **no skill writes or edits test files** except [`/create-test`](./skills/create-test/SKILL.md) and [`/setup-toolkit`](./skills/setup-toolkit/SKILL.md) copying quality-gate templates (`complexity.test.mjs`, `cyclomatic-cap.mjs`, `principle-gate.test.mjs`, `principle-scan.mjs`, `knip.json`, `knip.test.mjs`, `stryker.conf.json`). Only [`/code-review`](./skills/code-review/SKILL.md) and [`/pr-review`](./skills/pr-review/SKILL.md) may **recommend** `/create-test` (tell the user, never auto-invoke). `/task`, `/implement`, `/analyze`, `/write-ticket`, `/publish`, `/just-do-it`, etc. must not create tests or call `/create-test`.

## Browser-assisted validation

Cursor's native Browser is a runtime capability, not a `SKILL.md` frontmatter option. It needs no custom `mcp.json` or external package, but a skill cannot enable it or bypass approval, Browser Protection, policy, or origin allowlists.

For post-build UI **acceptance** (`/task`, `/code-review`):

1. Use an Agent-mode session where Browser tools are exposed.
2. Reuse a running local app or approved preview with safe test data.
3. Use [`skills/pack-shared/browser-evidence.md`](./skills/pack-shared/browser-evidence.md) as the single browser evidence protocol; link to it instead of copying its steps into other skills.
4. Write capability-based guidance: use Browser when it is available; otherwise report visual validation as `blocked`, never passed.

For PR **Demo screenshots** (any agent that opens a PR): follow
[`pr-ship.md`](./skills/pack-shared/pr-ship.md). Open the changed screen, take
one or a few pictures, embed them. Do not run the acceptance protocol to fill
Demo. If Browser is unavailable, omit Demo — do not block the PR.

Browser state can persist per workspace. Reset safe test state when needed, or report the state used as evidence.

## Add a skill

1. Create `skills/<skill-name>/SKILL.md` with frontmatter above. Put numbered how-to in that file. If nested vs one-off differs (who ships, who asks the next question), put that fork in `SKILL.md`. Worker steps say they are not a typical user start. User starts that must not nest under `/task` say so in `SKILL.md`.
2. Add `doctrine.md` / `examples.md` / `reference.md` only when progressive disclosure helps (bars vs examples vs deep detail). Every `doctrine.md` follows [`pack-shared/doctrine-schema.md`](./skills/pack-shared/doctrine-schema.md): Job, Owns, Does not own, Cite keys, Bars, Output, Apply, Anti-patterns, in that order. Process steps go in `SKILL.md`, not doctrine. Taste’s Convex verify, landing UI, SOLID, and futureproofing detail live in [`skills/taste/reference.md`](./skills/taste/reference.md), not in the taste doctrine body.
3. Link `asking.md` if the skill asks the user anything. Link `standards.md` on every skill except `/ask-gabriel`. Link `plain-language.md` if the skill talks to the user.
4. Wire discovery:
   - User-facing → [`README.md`](./README.md) catalog + [`ask-gabriel`](./skills/ask-gabriel/SKILL.md) on-ramps.
   - Internal worker step → only the orchestrator `SKILL.md` / doctrine that should call it (do not put it on the README as a typical entry).
5. Smoke-check locally:

```bash
npx skills@latest add . --list
```

## Add a plugin rule, agent, or command

- **Rule** — `rules/<name>.mdc` with YAML frontmatter (`description`, `alwaysApply`, optional `globs`). Keep it a pointer to skill doctrines, except self-contained writing bars (`no-emdash.mdc`, `unslop.mdc`). `alwaysApply: true` only when every chat needs it (today: `gold-standards.mdc`, `no-emdash.mdc`, and `unslop.mdc`). Never put a `README.md` in `rules/`.
- **Agent** — `agents/<name>.md` with `name` + `description` frontmatter. One job. Tell it which doctrines to Read.
- **Command** — `commands/<name>.md`. Do not create a command with the same name as an existing skill unless they share one job (today: `setup-toolkit` only).
- **Templates an agent must copy into an app**: live inside that skill’s folder so `npx skills` installs them. `/setup-toolkit` copies ESLint, Prettier, `eslint-plugin-no-emdash.mjs`, `cyclomatic-cap.mjs`, `complexity.test.mjs`, `principle-gate.test.mjs`, `principle-scan.mjs`, `knip.json`, `knip.test.mjs`, `stryker.conf.json`, and `.vscode/` workspace files.

## Conventions

- One skill = one job. Prefer new skill over bloating an existing one.
- Doctrine files share one schema ([`pack-shared/doctrine-schema.md`](./skills/pack-shared/doctrine-schema.md)). Cite another skill’s keys instead of restating its Bars.
- Cursor-native: Plan mode, CreatePlan, Task subagents (`pack-shared/subagents.md`), acceptance evidence gates.
- Teach in ordinary words — no explainer-video links in skill bodies. PR Demo
  screenshots are a different job ([`pr-ship.md`](./skills/pack-shared/pr-ship.md)). Agents cite principles as plain (Classic) (`pack-shared/plain-language.md`).
- No secrets in skills.
- New long-running orchestrators should reuse `pack-shared/standards.md`, `pack-shared/asking.md`, `pack-shared/execution-context.md`, `pack-shared/subagents.md`, and `pack-shared/pr-ship.md` without editing those files for skill-specific names. Any orchestrator that opens a PR must follow `pr-ship.md`; do not fork a private canvas/demo recipe into that skill.
- Never create `.agents/temp`, status/registry files, or hidden process artifacts by default. Persist only an artifact the user explicitly requested at a user-approved destination.
- Do not list `/pack-shared` in the README catalog — it is an install vehicle, not an on-ramp.
- Plugin rules stay short pointers to skill doctrines, except `no-emdash.mdc` and `unslop.mdc` (self-contained writing bars). Do not copy `/taste` or `/architecture` bodies into `.mdc` files.
- Do not add ESLint or Prettier to **this** markdown repo; they belong in consumer apps via `/setup-toolkit`.

## Publish / install

Preferred: Cursor plugin via Marketplace / team marketplace import of this repo. After you push, refresh the marketplace (or Auto Refresh).

Skills-only from GitHub:

```bash
npx skills@latest add Gabriel-Lafrance/Skills -a cursor -s '*' -g -y
npx skills@latest update -g -y
```

After you push, `npx skills` users refresh with `update`. While developing the pack itself, list from the repo root with `npx skills@latest add . --list`.

### Cursor plugin / marketplace

This repo is one Cursor plugin (`gabriel-skills`). Keep it **one plugin** until a second installable product is truly independent (do not split one plugin per skill — they share `pack-shared`).

Manifests live in [`.cursor-plugin/`](./.cursor-plugin/) (`plugin.json` + `marketplace.json`). After you push, refresh the marketplace (or turn on Auto Refresh). `npx skills` is unchanged and still skills-only.

Plugin components (folder discovery, or explicit paths in `plugin.json`):

| Component | This pack |
| --- | --- |
| Skills | `skills/` |
| Rules | `rules/*.mdc` — gold-standards is a pointer; no-emdash and unslop are self-contained writing bars |
| Agents | `agents/` (explorer, architect, implementer, reviewer, pr-reviewer) |
| Commands | `commands/` — do not alias every skill (avoids slash-command collisions with Cursor builtins and with skills) |
| Hooks / MCP | none until there is a concrete server or an explicit format-on-edit decision |

### Plugin rules (not User Rules)

Cursor loads plugin `rules/` automatically on install. That is the apply path for Plan mode and freeform chats that never invoke a skill. Skills still follow `/taste` and `/architecture` via [`pack-shared/standards.md`](./skills/pack-shared/standards.md) even if a user disables a plugin rule.

- Split rules so **Customize** can toggle them. Keep `alwaysApply` only on [`gold-standards.mdc`](./rules/gold-standards.mdc), [`no-emdash.mdc`](./rules/no-emdash.mdc), and [`unslop.mdc`](./rules/unslop.mdc).
- Do **not** paste rule bodies into **User Rules** when the plugin is installed (duplicates).
- Do **not** duplicate `/taste` or `/architecture` doctrine into `.mdc` files. Pointers only. `unslop.mdc` owns the chat-voice catalog because it is not a skill.
- `npx skills` does not install `rules/`. Users who want rules without the plugin can copy `rules/*.mdc` into an app’s `.cursor/rules/gabriel-skills/` (or ask `/setup-toolkit` to pin them).

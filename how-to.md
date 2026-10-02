# How to maintain this pack

For **authors** of Gabriel Lafrance Skills, not for end users installing the pack.

## Layout

```text
AGENTS.md                # always-on index for every harness, including Cursor; points at skills/rules/
.cursor-plugin/
  plugin.json            # Cursor plugin manifest (skills, commands)
  marketplace.json       # Cursor marketplace import; category and tags match Claude
.claude-plugin/
  plugin.json            # Claude plugin manifest (same skills and commands)
  marketplace.json       # Claude marketplace; category and tags live on the plugin entry. Copilot reads this too
.agents/
  plugins/
    marketplace.json     # Codex marketplace. Different shape: display name, install policy, auth policy
commands/                # Slash command (setup-gabriel-skills)
skills/
  rules/                 # rule files AGENTS.md points to (NOT user-invoked)
    SKILL.md             # required so npx skills installs this folder
    keep-it-simple.md, strong-foundation.md, no-unrequested-tests.md, main-context.md
                         # one file per rule in the AGENTS.md Rules section
    principles.md          # steering vocabulary; detail stays in the file that owns it
    journeys/            # one piece of work followed through skills and rules; /ask-gabriel is the map
    code-quality.md      # code quality rules (quality:* cite keys), named principles, mechanical rules
    code-quality-examples.md   # good vs bad snippets for code-quality.md
    code-structure.md    # code structure rules (structure:* cite keys)
    code-structure-examples.md # good vs bad shapes for code-structure.md
    planning.md          # grill first, Before/After change diagram, in-chat execution context
    user-experience.md   # every UI and UX rule (ux:*), React and UI, docs/design.md contract
    writing-style.md     # plain language, asking the user, Unslop
    testing.md           # how an accepted test is written
    shipping.md          # branch names, shipping rules, create tool, CI mirror, process
    shipping-templates.md # ship questions, PR Change diagram, PR body template
    tooling.md           # lint, format, CI, verify terminals first
  review/                # /review: a local branch diff or an open GitHub PR
    contract.md          # review evidence, modes, finding record, output fence, severity
  retro/                 # scoped workflow retrospective; recommendations by default
  setup-gabriel-skills/   # installs skills, including rules/, and places AGENTS.md
  <skill-name>/
    SKILL.md             # required: frontmatter + how-to
    doctrine.md          # optional: durable rules (fixed H2 schema)
    examples.md          # optional: good vs bad
    reference.md         # optional: deep detail (progressive disclosure)
LICENSE
README.md                # install + user-facing catalog
how-to.md                # this file
```

Skill folder names: `lowercase-with-hyphens` (e.g. `grill-me`, `write-ticket`).

**The pack holds two kinds of things.** **Rules** are how the user likes things done; they live in `skills/rules/` and apply whenever the topic comes up. **Skills** are procedures the user starts. A contract only one skill uses lives in that skill's folder (for example `review/contract.md`).

**Install rule:** `npx skills` only copies folders that contain `SKILL.md`. Pack-wide rules must live under `rules/` (or another skill folder). Bare `skills/*.md` files are **not** installed; other skills will fail looking for `../rules/...`.

**Plugin vs `npx skills`:** the Cursor plugin is optional. It auto-discovers `commands/` and `skills/`. It does not ship a Cursor rules folder. `npx skills` still copies **only** skill folders, and can target Claude, Cursor, or both (`-a claude`, `-a cursor`). It does not install root `AGENTS.md`. `/setup-gabriel-skills` installs the other skills and places that file from the pack root or from GitHub. Cursor reads the repo file. Do not add a `.cursor/rules` or `.mdc` copy.

Do not add plugin **hooks** unless the pack explicitly wants scripts on agent/Tab events. Do not add **MCP** unless there is a real server to ship. Do not add ESLint or Prettier as plugin components.

## Skill folders

Each skill is `SKILL.md` plus optional `doctrine.md`, `examples.md`, and `reference.md`.

Numbered how-to lives in `SKILL.md`. Nested vs one-off (who ships, who asks the next question) is a short fork in that file. Do not paste pack-wide ask rules. Link [Asking the user](./skills/rules/writing-style.md#asking-the-user). User starts that must not nest (`/review` on a GitHub PR, `/write-ticket`, `/setup-gabriel-skills`) say that in `SKILL.md`.

## Frontmatter

```yaml
---
name: skill-name          # matches folder name
description: Third person. WHAT it does and WHEN to use it. One line, 60 words or fewer.
category: Code            # one of Code, Data, Design, Documents, General, Web
disable-model-invocation: true   # only on setup-gabriel-skills and rules
---
```

Keep `description` on one line. Ono's Add a skill card prints the rest of that line. A folded block (`description: >-`) shows up as `>-`.

`category` is the one chip on that card. Use the chip names as written: Code, Data, Design, Documents, General, Web.

Every workflow skill triggers from what the user asks, so its `description` must name those requests ("Use when the user asks to write, file, or draft a ticket"). The Skills table in `AGENTS.md` maps the same requests for harnesses that ignore descriptions; keep the two in step. Only [`setup-gabriel-skills`](./skills/setup-gabriel-skills/SKILL.md) and [`rules`](./skills/rules/SKILL.md) keep `disable-model-invocation: true`. A build request goes to `/task-with-tests`; plain `/task` runs only when the user types it or asks to skip tests.

## Shared rules

- **Plain language:** every skill that talks to the user links the [Plain language](./skills/rules/writing-style.md#plain-language) section of `writing-style.md`. Chat uses ordinary words. Named principles use **plain (Classic)**, for example `keep this simple (KISS)`. Never acronym-only (`SoC violation`) and never the paraphrase without the classic name. Pack jargon (a bare Rule 1) stays banned.
- **Unslop:** chat replies follow the **Unslop** section of [`skills/rules/writing-style.md`](./skills/rules/writing-style.md#unslop). Not a user skill. Do not add `/unslop`. `/setup-gabriel-skills` places `AGENTS.md`. It does not rewrite it from memory.
- **Standards:** every pack skill except `/ask-gabriel` links and applies [`skills/rules/code-quality.md`](./skills/rules/code-quality.md) and [`skills/rules/code-structure.md`](./skills/rules/code-structure.md) on every run. `/ask-gabriel` stays thin and does not restate those rules.
- **Asking:** every skill that needs decisions links the [Asking the user](./skills/rules/writing-style.md#asking-the-user) section of `writing-style.md`: batch Questions, mark `recommended`, one-row `Reply like: 1a 2b 3c` (codes only, no descriptions). Do not add skill-specific freeform grill exceptions.
- **Process:** numbered how-to lives in that skill’s `SKILL.md`. Nested vs one-off is a short fork in that file, not a second process file.
- **Execution context:** parent orchestrators link the [Execution context](./skills/rules/planning.md#execution-context) section of `planning.md`, keep outcome, decisions, rules that must stay true, scope, and handoff visible in chat. Do not create agent-owned runtime trees.
- **Execution handoffs:** reuse [execution.md](./skills/rules/execution.md) for ready-ticket preflight, evidence, remediation, recovery, and completion. The chosen build skill owns its execution sequence; the active orchestrator owns dispatch and acceptance. Nested capabilities follow [planning.md](./skills/rules/planning.md#nested-capabilities), returning bounded updates to their parent.
- **Review:** `/review` keeps its [contract](./skills/review/contract.md) for evidence, modes, finding records, the review output fence, correctness hunt, and severity mapping.
- **Retrospectives:** [`/retro`](./skills/retro/SKILL.md) owns scoped evidence-backed workflow recommendations, including instruction removal. It does not create another standards owner or an automatic post-build loop.
- **PR ship:** every agent that creates a GitHub PR follows [`skills/rules/shipping.md`](./skills/rules/shipping.md): the harness pull-request tool when it has one, otherwise `gh`, a standalone branch that does not track `dev`, and the CI mirror in this environment before a push that opens or updates a PR.
- **Ticket stacks:** `/write-ticket` defaults larger work to a parent and PR-sized child tickets with dependencies and explicit PR bases. Use its [stack handoff](./skills/write-ticket/reference.md#stack-handoff) for a single request to implement all children; builds follow the [whole-stack handoff](./skills/task/doctrine.md#whole-stack-ticket-handoff) and [stack shipping rules](./skills/rules/shipping.md#stacked-pull-requests).
- **Do not** put shared rules at `skills/*.md`: they will not install.
- **Tests:** tests require the user's acceptance under [`no-unrequested-tests.md`](./skills/rules/no-unrequested-tests.md). [`/test-audit`](./skills/test-audit/SKILL.md) only prunes and repairs existing tests after the user approves the evidence. Reuse accepted and refused decisions with their sources from the [ready-ticket preflight](./skills/rules/execution.md#ready-ticket-preflight); changing execution entry point does not reset consent. For newly proposed tests, the owning build skill asks and waits. [`/review`](./skills/review/SKILL.md) may recommend a lock, never write it unasked. `/task` build slices, `/analyze`, and `/write-ticket` do not write tests.

## Runtime and visual checks

Only [`/verification`](./skills/verification/SKILL.md) manually drives the browser, migrations, endpoints, and jobs, and captures screenshots or traces. It runs all configured repository test suites on every verification, while live checks cover only the layers that changed ([scope](./skills/verification/doctrine.md#scope-to-the-change)). `/task` and `/task-with-tests` launch it alongside `/review`; `/gabriel-mode` accepts worker self-reviews and the combined review before verification. Verification may delegate independent expensive checks to isolated runners, while its parent owns check coverage and verdict. Follow [evidence validity](./skills/rules/execution.md#handoffs-and-evidence) after fixes; a passed check for an older change is not current proof. Every other skill stays on the diff, path walks, and terminal output except when running accepted automated tests. Evidence files live outside the repo and are never committed. PR bodies stay text and may summarize the verification handoff.

## Add a skill

1. Create `skills/<skill-name>/SKILL.md` with frontmatter above. Put numbered how-to in that file. If nested vs one-off differs (who ships, who asks the next question), put that fork in `SKILL.md`. Inner steps say they are not a typical user start. User starts that must not nest under `/task` say so in `SKILL.md`. If the steps are really a preference that applies whenever a topic comes up (how tests look, how PRs are shipped), write a rule in `skills/rules/` instead of a skill.
2. Add `doctrine.md` / `examples.md` / `reference.md` only when progressive disclosure helps (bars vs examples vs deep detail). Every `doctrine.md` follows the [skill file layout](./.github/CONTRIBUTING.md#skill-file-layout): Job, Owns, Does not own, Bars, Output, Apply, Anti-patterns, in that order. Process steps go in `SKILL.md`, not doctrine. Code quality and code structure rules live in [`skills/rules/code-quality.md`](./skills/rules/code-quality.md) and [`skills/rules/code-structure.md`](./skills/rules/code-structure.md), not in a skill doctrine.
3. Link the Asking the user section of `rules/writing-style.md` if the skill asks the user anything. Link `rules/code-quality.md` and `rules/code-structure.md` in the Read when list of any skill that writes or judges code. Link the Plain language section of `rules/writing-style.md` if the skill talks to the user.
4. Wire discovery:
   - User-facing → [`README.md`](./README.md) catalog + [`ask-gabriel`](./skills/ask-gabriel/SKILL.md) on-ramps.
   - Inner step → only the orchestrator `SKILL.md` / doctrine that should call it (do not put it on the README as a typical entry).
5. Smoke-check locally:

```bash
npx skills@latest add . --list
```

## Add a command

Do not add a root or `.cursor/rules` folder or a `.mdc` file. The always-on index is [`AGENTS.md`](./AGENTS.md) for every harness, including Cursor; the rule text lives in `skills/rules/`. Do not add a `CLAUDE.md` in the pack or an app.
- **Command:** `commands/<name>.md`. Do not create a command with the same name as an existing skill unless they share one job (today: `setup-gabriel-skills` only).
- This pack does not copy ESLint, Prettier, or editor files into an app. Missing `docs/design.md` is written from the routes in code before UI work ([`ux:initialization`](./skills/rules/user-experience.md#initialization)), not by copying a stub from this pack. `/setup-gabriel-skills` does not write that file.

## Conventions

- One skill = one job. Prefer new skill over bloating an existing one.
- Doctrine files share one layout ([skill file layout](./.github/CONTRIBUTING.md#skill-file-layout)). Cite another skill's keys instead of restating its Bars.
- Harness tools: use the plan tool after the grill when the harness has one, otherwise write the plan in chat. Open a pull request with the harness tool when it has one, otherwise `gh` (`rules/shipping.md`). Acceptance evidence is the `/verification` handoff.
- Teach in ordinary words, no explainer-video links in skill bodies. Do not make agents dump acronyms at the user (`rules/writing-style.md`, Plain language).
- No secrets in skills.
- New long-running orchestrators should reuse `rules/writing-style.md` (asking), `rules/planning.md` (execution context), and `rules/shipping.md` without editing those files for skill-specific names. Any orchestrator that opens a PR must follow `shipping.md`; do not fork a private ship recipe into that skill.
- Never create `.agents/temp`, status/registry files, or hidden process artifacts by default. Persist only an artifact the user explicitly requested at a user-approved destination.
- Do not list `/rules` in the README catalog. It is an install vehicle, not an on-ramp.
- Do not add Cursor-only rules. The code quality and code structure rules live in `skills/rules/code-quality.md` and `skills/rules/code-structure.md`, with their examples beside them. Do not keep a second copy in a skill doctrine.
- Do not add ESLint or Prettier to **this** markdown repo. This pack does not ship them.
- There is one `AGENTS.md`, at the pack root. Do not keep a second copy inside a skill.

## Publish / install

The contract is [`AGENTS.md`](./AGENTS.md) plus the rule files in `skills/rules/`. The Cursor plugin is optional. After you push a plugin change, refresh the marketplace (or Auto Refresh).

Skills from GitHub, for every harness the CLI already sees:

```bash
npx skills@latest add gabriel-lafrance/skills@setup-gabriel-skills -g -y
```

Then run `/setup-gabriel-skills` in an app. It verifies, then installs the rest of this pack and places `AGENTS.md` (it asks where). If that install cannot be done, it offers a manual copy.

To copy every skill without running setup:

```bash
npx skills@latest add gabriel-lafrance/skills --all -g
npx skills@latest update -g -y
```

Use `-a claude` or `-a cursor` alone when you only need one harness.

After you push, `npx skills` users refresh with `update`. The skills.sh on-ramp is [`setup-gabriel-skills`](https://skills.sh/gabriel-lafrance/skills/setup-gabriel-skills). While developing the pack itself, list from the repo root with `npx skills@latest add . --list`.

### Cursor plugin / marketplace

This repo is one Cursor plugin (`gabriel-skills`). Keep it **one plugin** until a second installable product is truly independent (do not split one plugin per skill; they share `rules/`).

Cursor manifests live in [`.cursor-plugin/`](./.cursor-plugin/). Claude manifests live in [`.claude-plugin/`](./.claude-plugin/). Keep those two `plugin.json` files and those two `marketplace.json` files on the same version, description, category, and tags. Category and tags belong on the Claude and Cursor marketplace plugin entry, not in `plugin.json`. Codex uses [`.agents/plugins/marketplace.json`](./.agents/plugins/marketplace.json) instead: display name, `policy.installation`, `policy.authentication`, and category `Productivity`. Do not copy the Claude JSON into that file. After you push, refresh the marketplace (or turn on Auto Refresh). `npx skills` is unchanged and still skills-only.

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
- Rule text lives in `skills/rules/`: one file per rule in the `AGENTS.md` Rules section, and one file per topic in the Read when table. `AGENTS.md` is only the index: a short intro, how to find the pack, the Rules section (each line states the rule in bold, then the moment, the file, and the mistake), the **Read when** table, and the Conflict line. Change a rule in its `skills/rules/` file. Do not grow `AGENTS.md` back into the full rulebook, and keep it under 8,192 bytes.
- Every pointer, in `AGENTS.md` and in a skill's Read when list, names the action the agent is about to take, the file, and the mistake it makes without that file.
- Do **not** copy the code quality or code structure rules into a skill doctrine. The Unslop catalog lives in `skills/rules/writing-style.md` because it is not a user skill.
- When the index or the Rules section changes, edit root `AGENTS.md`. There is no second copy.
- Do **not** add a `CLAUDE.md` in the pack or the app.
- `npx skills` does not install root `AGENTS.md` by itself. `/setup-gabriel-skills` places that file from the pack root or from GitHub. Cursor reads the repo file. Do not add a project `CLAUDE.md`.

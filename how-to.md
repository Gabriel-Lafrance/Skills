# How to maintain this pack

For **authors** of Gabriel Lafrance Skills — not for end users installing the pack.

## Layout

```text
skills/
  pack-shared/           # installable shared contracts (NOT user-invoked)
    SKILL.md             # required so npx skills installs this folder
    asking.md            # how to ask the user (batch Questions)
    variants.md          # standalone vs flow selection
    execution-context.md # in-chat parent / worker context
    subagents.md         # Task bias, Worker Brief, spawn rules
    review-contract.md   # shared review evidence and finding rules
    browser-evidence.md  # browser proof for UI acceptance
  <skill-name>/
    SKILL.md             # required — frontmatter + thin entry
    standalone.md        # optional — one-off use
    flow.md              # optional — step inside a long-running wave
    doctrine.md          # optional — durable rules
    examples.md          # optional — good vs bad
    reference.md         # optional — deep detail (progressive disclosure)
LICENSE
README.md                # install + user-facing catalog
how-to.md                # this file
```

Skill folder names: `lowercase-with-hyphens` (e.g. `grill-me`, `code-review`).

**Install rule:** `npx skills` only copies folders that contain `SKILL.md`. Pack-wide contracts must live under `pack-shared/` (or another skill folder). Bare `skills/*.md` files are **not** installed — dual skills will fail looking for `../variants.md`.

## Skill kinds

| Kind | Files | When |
| --- | --- | --- |
| **Dual** | `SKILL.md` + `standalone.md` + `flow.md` | Same skill as a one-off *or* inside a wave |
| **Flow-only** | `SKILL.md` + `flow.md` (no `standalone.md`) | Looked up by an orchestrator (`/goal`, `/just-do-it`, …) |
| **Standalone-only** | `SKILL.md` (+ doctrine/reference); no `flow.md` | User-invoked entry (`/ask-gabriel`, `/just-do-it`, `/write-ticket`, …) |

`SKILL.md` stays thin. Point at doctrine / examples / the chosen variant. Do not paste pack-wide ask or variant rules — link [`asking.md`](./skills/pack-shared/asking.md) and [`variants.md`](./skills/pack-shared/variants.md).

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

- **Asking:** every skill that needs decisions links [`pack-shared/asking.md`](./skills/pack-shared/asking.md) — batch Questions, mark `← recommended`, one-row `Reply like: 1a 2b 3c` (codes only, no descriptions).
- **Variants:** dual / flow-only / standalone-only skills link [`pack-shared/variants.md`](./skills/pack-shared/variants.md). Agent loads **exactly one** of `standalone.md` or `flow.md` per turn. Keep those files wave-agnostic (any long-running orchestrator, not only `/goal`).
- **Execution context:** parent flows link [`execution-context.md`](./skills/pack-shared/execution-context.md), keep outcome, decisions, Active Rules, scope, and handoff visible in chat, and compile that context into each worker brief. Do not create agent-owned runtime trees.
- **Subagents:** parents link [`subagents.md`](./skills/pack-shared/subagents.md) for Task bias, Worker Brief, parallel lanes, and after-wave integration (there is no `/orchestrate` skill).
- **Review:** review skills link [`review-contract.md`](./skills/pack-shared/review-contract.md) for evidence, modes, finding records, and severity mapping.
- **Browser evidence:** UI acceptance proof links [`browser-evidence.md`](./skills/pack-shared/browser-evidence.md).
- **Do not** put shared contracts at `skills/*.md` — they will not install.
- **Tests:** **no skill writes or edits test files** except [`/create-test`](./skills/create-test/SKILL.md). Only [`/code-review`](./skills/code-review/SKILL.md) and [`/pr-review`](./skills/pr-review/SKILL.md) may **recommend** `/create-test` (tell the user — never auto-invoke). `/goal`, `/implement`, `/analyze`, `/write-ticket`, `/publish`, `/just-do-it`, etc. must not create tests or call `/create-test`.

## Browser-assisted validation

Cursor's native Browser is a runtime capability, not a `SKILL.md` frontmatter option. It needs no custom `mcp.json` or external package, but a skill cannot enable it or bypass approval, Browser Protection, policy, or origin allowlists.

For post-build UI validation:

1. Use an Agent-mode session where Browser tools are exposed.
2. Reuse a running local app or approved preview with safe test data.
3. Use [`skills/pack-shared/browser-evidence.md`](./skills/pack-shared/browser-evidence.md) as the single browser evidence protocol; link to it instead of copying its steps into other skills.
4. Write capability-based guidance: use Browser when it is available; otherwise report visual validation as `blocked`, never passed.

Browser state can persist per workspace. Reset safe test state when needed, or report the state used as evidence.

## Add a skill

1. Create `skills/<skill-name>/SKILL.md` with frontmatter above.
2. Pick a kind:
   - Dual → add `standalone.md` and `flow.md`; in `SKILL.md` say choose exactly one via `variants.md`.
   - Flow-only → add `flow.md`; note “no standalone” and link `variants.md`.
   - Standalone-only → no `flow.md`; if flow is requested, use the missing-variant message from `variants.md`.
3. Add `doctrine.md` / `examples.md` / `reference.md` only when progressive disclosure helps (keep `SKILL.md` short).
4. Link `asking.md` if the skill asks the user anything.
5. Wire discovery:
   - User-facing → [`README.md`](./README.md) catalog + [`ask-gabriel`](./skills/ask-gabriel/SKILL.md) on-ramps.
   - Internal flow step → only the orchestrator doctrine/flow that should call it (do not put it on the README as a typical entry).
6. Smoke-check locally:

```bash
npx skills@latest add . --list
```

## Conventions

- One skill = one job. Prefer new skill over bloating an existing one.
- Cursor-native: Plan mode, CreatePlan, Task subagents (`pack-shared/subagents.md`), acceptance evidence gates.
- Teach principles in prose — no video links in skill bodies.
- No secrets in skills.
- Do not invent a missing `standalone.md` / `flow.md` process.
- New long-running orchestrators should reuse `pack-shared/asking.md`, `pack-shared/variants.md`, `pack-shared/execution-context.md`, and `pack-shared/subagents.md` without editing those files for skill-specific names.
- Never create `.agents/temp`, status/registry files, or hidden process artifacts by default. Persist only an artifact the user explicitly requested at a user-approved destination.
- Do not list `/pack-shared` in the README catalog — it is an install vehicle, not an on-ramp.

## Publish / install

Users install from GitHub:

```bash
npx skills@latest add Gabriel-Lafrance/Skills -a cursor -s '*' -g -y
npx skills@latest update -g -y
```

After you push, they refresh with `update`. While developing the pack itself, list from the repo root with `npx skills@latest add . --list`.

### Personal Cursor User Rules (not via `npx skills`)

Always-on teaching for Plan mode / freeform lives in [`cursor-rules/`](./cursor-rules/). The skills CLI only copies `SKILL.md` folders.

**Important:** Cursor **User Rules** (Settings → Rules → User Rules) are account/settings-backed. Copying `.mdc` into `~/.cursor/rules` does **not** show up there and is not a reliable global apply path.

- Source: [`cursor-rules/ultimate-gold-standards.mdc`](./cursor-rules/ultimate-gold-standards.mdc) — pointer that forces doctrine Reads (`taste`, `architecture`, `publish`), Plan-mode grill-before-plan, and Before/After Mermaid on every non-trivial plan.
- Install: copy the body **without** YAML frontmatter, then paste into **Settings → Rules → User Rules** under the title **Ultimate gold standards**. Or ask an Agent to install that file into User Rules.
- After changing the `.mdc`, re-paste (or re-ask the Agent). Skill doctrine edits do not require that if skills were refreshed with `npx skills update`.

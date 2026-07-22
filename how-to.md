# How to maintain this pack

For **authors** of Gabriel Lafrance Skills — not for end users installing the pack.

## Layout

```text
skills/
  asking.md              # pack-wide: how to ask the user (batch Questions)
  variants.md            # pack-wide: standalone vs flow selection
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

## Skill kinds

| Kind | Files | When |
| --- | --- | --- |
| **Dual** | `SKILL.md` + `standalone.md` + `flow.md` | Same skill as a one-off *or* inside a wave |
| **Flow-only** | `SKILL.md` + `flow.md` (no `standalone.md`) | Looked up by an orchestrator (`/goal`, `/repair`, …) |
| **Standalone-only** | `SKILL.md` (+ doctrine/reference); no `flow.md` | User-invoked entry (`/goal`, `/analyze`, `/ask-gabriel`, …) |

`SKILL.md` stays thin. Point at doctrine / examples / the chosen variant. Do not paste pack-wide ask or variant rules — link [`asking.md`](./skills/asking.md) and [`variants.md`](./skills/variants.md).

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

- **Asking:** every skill that needs decisions links `asking.md` — batch Questions, mark `← recommended`, one-row `Reply like: 1a 2b 3c` (codes only, no descriptions).
- **Variants:** dual / flow-only / standalone-only skills link `variants.md`. Agent loads **exactly one** of `standalone.md` or `flow.md` per turn. Keep those files wave-agnostic (any long-running orchestrator, not only `/goal`).
- **Tests:** **no skill writes or edits test files** except [`/create-test`](./skills/create-test/SKILL.md). Only [`/code-review`](./skills/code-review/SKILL.md) and [`/pr-review`](./skills/pr-review/SKILL.md) may **recommend** `/create-test` (tell the user — never auto-invoke). `/goal`, `/implement`, `/repair`, `/validate`, `/analyze`, `/write-ticket`, `/publish`, `/just-do-it`, etc. must not create tests or call `/create-test`.

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
- Cursor-native: Plan mode, CreatePlan, Task subagents, validate gates.
- Teach principles in prose — no video links in skill bodies.
- No secrets in skills.
- Do not invent a missing `standalone.md` / `flow.md` process.
- New long-running orchestrators should reuse `asking.md` + `variants.md` without editing those files for skill-specific names.

## Publish / install

Users install from GitHub:

```bash
npx skills@latest add Gabriel-Lafrance/Skills -a cursor -s '*' -g -y
npx skills@latest update -g -y
```

After you push, they refresh with `update`. While developing the pack itself, list from the repo root with `npx skills@latest add . --list`.

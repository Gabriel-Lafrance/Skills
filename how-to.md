# How to maintain this pack

For **authors** of Gabriel Lafrance Skills — not for end users installing the pack.

## Layout

```text
skills/
  pack-shared/           # installable shared contracts (NOT user-invoked)
    SKILL.md             # required so npx skills installs this folder
    asking.md            # how to ask the user (batch Questions)
    variants.md          # standalone vs flow selection
    workspace-roots.md   # goal/analysis root resolution
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
| **Flow-only** | `SKILL.md` + `flow.md` (no `standalone.md`) | Looked up by an orchestrator (`/goal`, `/repair`, …) |
| **Standalone-only** | `SKILL.md` (+ doctrine/reference); no `flow.md` | User-invoked entry (`/goal`, `/analyze`, `/ask-gabriel`, …) |

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
- **Workspace roots:** every goal or analysis flow resolves caller-provided workspace roots before falling back to pack-global defaults. See [`workspace-roots.md`](./skills/pack-shared/workspace-roots.md); never rebuild a nested parent path from an id alone.
- **Do not** put shared contracts at `skills/*.md` — they will not install.
- **Tests:** **no skill writes or edits test files** except [`/create-test`](./skills/create-test/SKILL.md). Only [`/code-review`](./skills/code-review/SKILL.md) and [`/pr-review`](./skills/pr-review/SKILL.md) may **recommend** `/create-test` (tell the user — never auto-invoke). `/goal`, `/implement`, `/repair`, `/validate`, `/analyze`, `/write-ticket`, `/publish`, `/just-do-it`, etc. must not create tests or call `/create-test`.

## Browser-assisted validation

Cursor's native Browser is a runtime capability, not a `SKILL.md` frontmatter option. It needs no custom `mcp.json` or external package, but a skill cannot enable it or bypass approval, Browser Protection, policy, or origin allowlists.

For post-build UI validation:

1. Use an Agent-mode session where Browser tools are exposed.
2. Reuse a running local app or approved preview with safe test data.
3. Use [`skills/validate/reference.md`](./skills/validate/reference.md) as the single browser evidence protocol; link to it instead of copying its steps into other skills.
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
- Cursor-native: Plan mode, CreatePlan, Task subagents, validate gates.
- Teach principles in prose — no video links in skill bodies.
- No secrets in skills.
- Do not invent a missing `standalone.md` / `flow.md` process.
- New long-running orchestrators should reuse `pack-shared/asking.md` + `pack-shared/variants.md` without editing those files for skill-specific names.
- Do not list `/pack-shared` in the README catalog — it is an install vehicle, not an on-ramp.

## Publish / install

Users install from GitHub:

```bash
npx skills@latest add Gabriel-Lafrance/Skills -a cursor -s '*' -g -y
npx skills@latest update -g -y
```

After you push, they refresh with `update`. While developing the pack itself, list from the repo root with `npx skills@latest add . --list`.

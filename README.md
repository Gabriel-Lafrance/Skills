# Gabriel Lafrance Skills

Cursor-first agent skills for real engineering — not vibe coding.

Autonomous `/goal` as **orchestrator**: Task subagents explore/implement/review; on-disk plans keep them aligned. Dual skills ship as **standalone + `*-flow`** so each can be tweaked for who calls it. Inspired by [Matt Pocock's skills](https://github.com/mattpocock/skills), rewritten for Cursor.

## Install

```bash
npx skills@latest add Gabriel-Lafrance/Skills -a cursor -s '*' -y
```

Global:

```bash
npx skills@latest add Gabriel-Lafrance/Skills -a cursor -s '*' -g -y
```

```bash
npx skills@latest update -g -y
```

Then in Cursor:

1. Run `/goal` for long verifiable work (agents may auto-start it).
2. Outside a goal: `/grill-me`, `/architecture`, `/design`, `/create-plan`, `/code-review`.
3. Ticket: `/goal IN-1234` or `/goal #42` — `/goal` loads read-only `/trackers-flow` internally.

## Invocation model

| Kind | Skills | Auto-invoke | Who uses it |
| --- | --- | --- | --- |
| **Flow skill** | `goal` | Yes | Users + agents; no twin |
| **Standalone (public)** | `grill-me`, `architecture`, `design`, `create-plan`, `code-review` | Yes | Users + agents outside `/goal` |
| **Flow twin** | `grill-me-flow`, `architecture-flow`, `design-flow`, `create-plan-flow`, `code-review-flow` | No | Only `/goal` (and explicit `/name-flow`) |
| **Internal only** | `orchestrate-flow`, `trackers-flow`, `taste-flow`, `split-task-flow`, `implement-flow`, `validate-flow` | No | Pack callees only — no standalone twin |

Example: `/code-review` = diff vs `main` (or what the user asked). `/code-review-flow` = review what this goal’s plans shipped.

## Main flow

```text
/goal
   → .agents/temp/goals/<goal-id>/
   → /trackers-flow (read only) if ticket
   → /grill-me-flow
   → /architecture-flow (+ /design-flow if UI)
   → /create-plan-flow → plans/INDEX + plans/NN-*.md
   → /implement-flow
   → /validate-flow → /code-review-flow
   → ACHIEVED: delete workspace (ticket close manual)
```

### Verify

Prefer **existing terminals** (frontend + `npx convex dev`). No ritual Convex MCP / lint / tsc.

## Public skills

| Skill | When to use |
| --- | --- |
| [goal](./skills/goal/SKILL.md) | Autonomous goal loop |
| [grill-me](./skills/grill-me/SKILL.md) / [grill-me-flow](./skills/grill-me-flow/SKILL.md) | Sharpen intent (solo vs goal gate) |
| [architecture](./skills/architecture/SKILL.md) / [architecture-flow](./skills/architecture-flow/SKILL.md) | Structure card (solo vs into plans) |
| [design](./skills/design/SKILL.md) / [design-flow](./skills/design-flow/SKILL.md) | UI polish vs goal Design card |
| [create-plan](./skills/create-plan/SKILL.md) / [create-plan-flow](./skills/create-plan-flow/SKILL.md) | Plan file (solo vs after grill) |
| [code-review](./skills/code-review/SKILL.md) / [code-review-flow](./skills/code-review-flow/SKILL.md) | Diff vs main/user ask vs goal Spec |

## Internal flow skills

| Skill | Role |
| --- | --- |
| [orchestrate-flow](./skills/orchestrate-flow/SKILL.md) | Bind Task workers to goal-id |
| [trackers-flow](./skills/trackers-flow/SKILL.md) | Read-only Linear/GitHub |
| [taste-flow](./skills/taste-flow/SKILL.md) | Author taste (+ [examples](./skills/taste-flow/examples.md)) |
| [split-task-flow](./skills/split-task-flow/SKILL.md) | INDEX / agent-sized plans |
| [implement-flow](./skills/implement-flow/SKILL.md) | Slice workers |
| [validate-flow](./skills/validate-flow/SKILL.md) | Done when gate |

## Repo layout

```text
skills/
  <name>/SKILL.md
  <name>-flow/SKILL.md   # when dual
LICENSE
README.md
scripts/validate-skills.sh
```

Artifacts: **`.agents/temp/goals/<goal-id>/`** — never `.scratch/`.

## Attribution

Inspired by [mattpocock/skills](https://github.com/mattpocock/skills) (MIT). `/goal` from [Claude Code](https://code.claude.com/docs/en/goal), Cursor reimplementation. Standards thermonuclear bar from Cursor’s [thermo-nuclear-code-quality-review](https://github.com/cursor/plugins/blob/main/cursor-team-kit/skills/thermo-nuclear-code-quality-review/SKILL.md).

## License

MIT — see [LICENSE](./LICENSE).

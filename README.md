# Gabriel Lafrance Skills

Cursor-first agent skills for real engineering — not vibe coding.

**`/goal`** is the autonomous orchestrator: Task subagents explore, implement, and review against on-disk plans. Most craft skills ship as a **standalone** (you / agents outside a goal) plus a **`*-flow`** twin (only `/goal` looks those up). A few skills are **standalone-only** — no flow twin, never inside `/goal`.

Inspired by [Matt Pocock's skills](https://github.com/mattpocock/skills), rewritten for Cursor.

## Install

```bash
npx skills@latest add Gabriel-Lafrance/Skills -a cursor -s '*' -y
```

Global:

```bash
npx skills@latest add Gabriel-Lafrance/Skills -a cursor -s '*' -g -y
npx skills@latest update -g -y
```

## Quick start

| You want… | Run |
| --- | --- |
| Long, verifiable feature work | `/goal` (or `/goal IN-1234` / `/goal #42`) |
| Sharpen fuzzy intent | `/grill-me` |
| Structure / data shape | `/architecture` |
| UI polish or new UI craft | `/design` |
| One plan file | `/create-plan` |
| Review a branch vs `main` (or a ref you name) | `/code-review` |
| Fix a bug (smallest footprint) | `/repair` |
| Refine or create a Linear/GitHub ticket | `/write-ticket` |
| Lock complex behavior with durable tests | `/create-test` (manual only — you must ask) |

**Ticket tip:** refine with `/write-ticket` first (Done, entrypoints, expected behavior), then `/goal IN-1234`. Inside `/goal`, ticket fetch is read-only via `/trackers-flow`.

**Bug tip:** `/repair` for local defects; escalate massive multi-layer bugs to `/goal`.

## Invocation model

| Kind | Skills | Auto-invoke | Who uses it |
| --- | --- | --- | --- |
| **Orchestrator** | `goal` | Yes | Users + agents; no twin |
| **Standalone + flow twin** | `grill-me`, `architecture`, `design`, `create-plan`, `code-review`, `repair` | Standalone: yes · Flow: no | Standalone outside `/goal`; `*-flow` only under `/goal` (or explicit `/name-flow`) |
| **Standalone only** | `write-ticket` | Yes | Never under `/goal` / any `*-flow`; may **write** trackers after draft approval |
| **Standalone only (manual)** | `create-test` | No | Never in a flow, never autonomous — user runs `/create-test`; `/code-review` may recommend it |
| **Internal only** | `orchestrate-flow`, `trackers-flow`, `taste-flow`, `split-task-flow`, `implement-flow`, `validate-flow` | No | Pack callees only — no user-facing twin |

Rule of thumb: outside `/goal` use the bare name (`/code-review`). Inside `/goal` the orchestrator uses the `*-flow` twin (`/code-review-flow`).

## `/goal` loop

```text
/goal
   → .agents/temp/goals/<goal-id>/
   → /trackers-flow (read only) if ticket
   → /grill-me-flow  (+ taste / architecture / design topics with the user)
   → /architecture-flow (+ /design-flow if UI)
   → /split-task-flow (when multi-slice) → /create-plan-flow
   → /implement-flow (via /orchestrate-flow)
   → mid-build bugs → /repair-flow → /validate-flow
   → /validate-flow → /code-review-flow  (both required)
   → ACHIEVED summary → delete workspace
```

### Verify

Prefer **existing terminals** (frontend, backend, types, lint, Convex, …) plus narrow CLI when needed. No ritual Convex MCP.

Artifacts live under **`.agents/temp/goals/<goal-id>/`** and **`.agents/temp/repairs/<repair-id>/`** — never `.scratch/`.

---

## Skill catalog

### Orchestrator

| Skill | Role |
| --- | --- |
| [goal](./skills/goal/SKILL.md) | Autonomous loop: grill → plans → Task workers → validate + code-review → ACHIEVED |

### Public standalones (and their flow twins)

| Standalone | Flow twin | When to use |
| --- | --- | --- |
| [grill-me](./skills/grill-me/SKILL.md) | [grill-me-flow](./skills/grill-me-flow/SKILL.md) | Sharpen intent until shared understanding (solo vs hard gate before plans) |
| [architecture](./skills/architecture/SKILL.md) | [architecture-flow](./skills/architecture-flow/SKILL.md) | Entry points, folders, write-path data design (solo vs Structure card into plans) |
| [design](./skills/design/SKILL.md) | [design-flow](./skills/design-flow/SKILL.md) | UI craft / polish (solo vs Design card into plans) |
| [create-plan](./skills/create-plan/SKILL.md) | [create-plan-flow](./skills/create-plan-flow/SKILL.md) | One `plans/NN-slug.md` (solo vs after grill in a goal) |
| [code-review](./skills/code-review/SKILL.md) | [code-review-flow](./skills/code-review-flow/SKILL.md) | Standards + Spec + Routes on a diff (vs `main`/ref you name vs this goal’s plans) |
| [repair](./skills/repair/SKILL.md) | [repair-flow](./skills/repair-flow/SKILL.md) | Pessimistic bug hunt → grill → acceptance → smallest fix → `/validate-flow` |

### Standalone only (no `*-flow` twin)

| Skill | Role |
| --- | --- |
| [write-ticket](./skills/write-ticket/SKILL.md) | Explore via Task subagents → grill → ticket must have **Expected behavior**, **Definition of Done**, **Entrypoints** → draft → write to Linear/GitHub |
| [create-test](./skills/create-test/SKILL.md) | Manual behavior-lock tests for complex hooks / domain logic / facades so outside edits cannot silently break them |

### Internal flow skills (pack callees)

| Skill | Role |
| --- | --- |
| [orchestrate-flow](./skills/orchestrate-flow/SKILL.md) | Bind Task workers to `goal-id` + plan file; **omit Task `model`** (inherit parent chat model) |
| [trackers-flow](./skills/trackers-flow/SKILL.md) | Read-only Linear/GitHub brief — never write/close/comment |
| [taste-flow](./skills/taste-flow/SKILL.md) | Author coding taste contract (+ [examples](./skills/taste-flow/examples.md)) |
| [split-task-flow](./skills/split-task-flow/SKILL.md) | Shape `plans/INDEX` into agent-sized slices |
| [implement-flow](./skills/implement-flow/SKILL.md) | Frontier workers that build from one plan file |
| [validate-flow](./skills/validate-flow/SKILL.md) | Gate out: out-loud path walk + live terminals/CLI vs acceptance |

---

## Repo layout

```text
skills/
  <name>/SKILL.md            # standalone or orchestrator
  <name>-flow/SKILL.md       # goal/internal twin when dual
  <name>/examples.md         # optional (architecture, design, taste-flow, …)
LICENSE
README.md
scripts/validate-skills.sh
```

## Attribution

Inspired by [mattpocock/skills](https://github.com/mattpocock/skills) (MIT). `/goal` from [Claude Code](https://code.claude.com/docs/en/goal), Cursor reimplementation. Standards thermonuclear bar from Cursor’s [thermo-nuclear-code-quality-review](https://github.com/cursor/plugins/blob/main/cursor-team-kit/skills/thermo-nuclear-code-quality-review/SKILL.md).

## License

MIT — see [LICENSE](./LICENSE).

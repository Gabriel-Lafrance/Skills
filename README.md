# Gabriel Lafrance Skills

Cursor-first agent skills for real engineering — not vibe coding.

Autonomous `/goal` as **orchestrator**: Task subagents do explore/implement/review; on-disk plans keep them aligned. Plus tasteful UI, simple entry points, and validate-before-ship. Inspired by [Matt Pocock's skills](https://github.com/mattpocock/skills), rewritten for Cursor.

## Install

Install the full pack into Cursor (no per-skill checkboxes):

```bash
npx skills@latest add Gabriel-Lafrance/Skills -a cursor -s '*' -y
```

Global (all projects):

```bash
npx skills@latest add Gabriel-Lafrance/Skills -a cursor -s '*' -g -y
```

`-s '*'` selects every skill; `-y` skips prompts. Omit `-s '*'` only if you want the interactive picker.

Update all installed skills (global):

```bash
npx skills@latest update -g -y
```

Or reinstall this pack fresh:

```bash
npx skills@latest add Gabriel-Lafrance/Skills -a cursor -s '*' -g -y
```

Then in Cursor:

1. When unsure, agents may auto-load `/ask-gabriel` — or run it yourself.
2. For long verifiable work, run `/goal` (agents may auto-invoke it too).
3. For a tracker ticket: `/goal IN-1234` (Linear) or `/goal #42` (GitHub).

## Invocation model

| Kind | Examples | Auto-invoke | Who uses it |
| --- | --- | --- | --- |
| **Flow skill** | `goal`, `ask-gabriel` | Yes | Agents + user; no `*-flow` twin |
| **Standalone** | `design`, `grill-me`, `architecture`, … | Yes | One-shot work outside `/goal` |
| **Flow variant** | `design-flow`, `grill-me-flow`, … | No (`disable-model-invocation`) | Only `/goal` (and explicit `/name-flow`) |

## Main flow

```text
/goal  (main agent = orchestrator; agents may auto-start)
   → .agents/temp/goals/<goal-id>/
   → /grill-me-flow until shared understanding (hard gate)
   → explore → /architecture-flow (+ /design-flow if UI)
   → plans/INDEX.md + plans/01.md, 02.md, … (via /create-plan-flow)
   → /implement-flow via parallel workers (per plan file)
   → /validate-flow → /code-review-flow
   → on ACHIEVED: /trackers-flow close-out → delete that goal workspace
```

See **`/orchestrate-flow`** for conductor/worker rules and multi-goal file-lane safety.


| Skill | When to use |
| --- | --- |
| [ask-gabriel](./skills/ask-gabriel/SKILL.md) | Router — which skill/flow fits (auto) |
| [goal](./skills/goal/SKILL.md) | Autonomous goal loop (auto; looks up `*-flow`) |
| [orchestrate](./skills/orchestrate/SKILL.md) / [orchestrate-flow](./skills/orchestrate-flow/SKILL.md) | Main vs Task subagents |
| [trackers](./skills/trackers/SKILL.md) / [trackers-flow](./skills/trackers-flow/SKILL.md) | Linear + GitHub fetch / close-out |
| [taste](./skills/taste/SKILL.md) / [taste-flow](./skills/taste-flow/SKILL.md) | Author coding taste |
| [design](./skills/design/SKILL.md) / [design-flow](./skills/design-flow/SKILL.md) | UI craft — polish vs goal Design card |
| [grill-me](./skills/grill-me/SKILL.md) / [grill-me-flow](./skills/grill-me-flow/SKILL.md) | Sharpen intent |
| [architecture](./skills/architecture/SKILL.md) / [architecture-flow](./skills/architecture-flow/SKILL.md) | Entry points + folders + scale |
| [create-plan](./skills/create-plan/SKILL.md) / [create-plan-flow](./skills/create-plan-flow/SKILL.md) | Write `plans/NN-*.md` |
| [split-task](./skills/split-task/SKILL.md) / [split-task-flow](./skills/split-task-flow/SKILL.md) | Agent-sized pieces / INDEX |
| [implement](./skills/implement/SKILL.md) / [implement-flow](./skills/implement-flow/SKILL.md) | Dispatch slice workers |
| [validate](./skills/validate/SKILL.md) / [validate-flow](./skills/validate-flow/SKILL.md) | Done when / taste / design / scale |
| [code-review](./skills/code-review/SKILL.md) / [code-review-flow](./skills/code-review-flow/SKILL.md) | Standards + Spec |


## Repo layout

```text
skills/
  <skill-name>/
    SKILL.md          # required — name + description frontmatter
    examples.md       # optional progressive disclosure
LICENSE
README.md
```

## Why Cursor-only


| Agent-agnostic packs              | This pack                                         |
| --------------------------------- | ------------------------------------------------- |
| Freeform plans in chat     | `.agents/temp/goals/<id>/plans/NN-*.md` (after grill) |
| One agent does everything  | Main orchestrates; Task subagents labor (`/orchestrate-flow`) |
| Single global ACTIVE files | Isolated workspaces + REGISTRY — concurrent `/goal`s OK |
| Skip straight to coding    | Mandatory `/grill-me-flow` before any plan files             |
| Ad-hoc “done?”             | `/validate-flow` against Done when                       |
| Flat file dumps            | `/architecture-flow` requires entry point + folder map   |
| Native Claude `/goal` hook | `/goal` drives an autonomous subagent loop          |




## Attribution

Workflow ideas inspired by [mattpocock/skills](https://github.com/mattpocock/skills) (MIT). `/goal` pattern inspired by [Claude Code's](https://code.claude.com/docs/en/goal) `/goal`, reimplemented for Cursor.

## License

MIT — see [LICENSE](./LICENSE).

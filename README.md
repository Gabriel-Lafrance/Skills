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

Then in Cursor:

1. When unsure, run `/ask-gabriel`.
2. For long verifiable work, run `/goal`.
3. For a tracker ticket: `/goal IN-1234` (Linear) or `/goal #42` (GitHub).

## Main flow

```text
/goal  (main agent = orchestrator)
   → .scratch/goals/<goal-id>/   (isolated; many goals at once)
   → REGISTRY.md updated
   → parallel explore subagents → /architecture (+ /design if UI)
   → /create-plan → PLAN.md in that workspace
   → /split-task → pieces/ if needed
   → /implement via parallel workers (scoped to goal-id + file lane)
   → /validate → /code-review
```

See **`/orchestrate`** for conductor/worker rules and multi-goal file-lane safety.


| Skill                                          | When to use                                                |
| ---------------------------------------------- | ---------------------------------------------------------- |
| [ask-gabriel](./skills/ask-gabriel/SKILL.md)   | Router — which skill/flow fits                             |
| [orchestrate](./skills/orchestrate/SKILL.md)   | Main agent vs Task subagents — maximize workers            |
| [goal](./skills/goal/SKILL.md)                 | Autonomous goal loop (orchestrator)                        |
| [trackers](./skills/trackers/SKILL.md)         | Fetch / update / close Linear + GitHub issues              |
| [taste](./skills/taste/SKILL.md)               | Author coding taste — shared by plan/implement/review      |
| [design](./skills/design/SKILL.md)             | UI craft — fix current UI, or Design card when creating UI |
| [grill-me](./skills/grill-me/SKILL.md)         | Relentless interview to sharpen intent                     |
| [architecture](./skills/architecture/SKILL.md) | Simple entry points + folders + scalable data              |
| [create-plan](./skills/create-plan/SKILL.md)   | Write `PLAN.md` into a goal workspace                      |
| [split-task](./skills/split-task/SKILL.md)     | Split work into agent-sized pieces                         |
| [implement](./skills/implement/SKILL.md)       | Dispatch slice workers; integrate                          |
| [validate](./skills/validate/SKILL.md)         | Check Done when / plan / taste / design                    |
| [code-review](./skills/code-review/SKILL.md)   | Standards + Spec via parallel subagents                    |


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
| Freeform plans in chat     | Per-goal `.scratch/goals/<id>/PLAN.md` (no mode switch) |
| One agent does everything  | Main orchestrates; Task subagents labor (`/orchestrate`) |
| Single global ACTIVE files | Isolated workspaces + REGISTRY — concurrent `/goal`s OK |
| Ad-hoc “done?”             | `/validate` against Done when                       |
| Flat file dumps            | `/architecture` requires entry point + folder map   |
| Native Claude `/goal` hook | `/goal` drives an autonomous subagent loop          |




## Attribution

Workflow ideas inspired by [mattpocock/skills](https://github.com/mattpocock/skills) (MIT). `/goal` pattern inspired by [Claude Code's](https://code.claude.com/docs/en/goal) `/goal`, reimplemented for Cursor.

## License

MIT — see [LICENSE](./LICENSE).
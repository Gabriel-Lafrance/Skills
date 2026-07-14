# Gabriel Lafrance Skills

Cursor-first agent skills for real engineering — not vibe coding.

Plan mode, CreatePlan, simple entry points, folder structure, tasteful UI, and a validate-before-ship loop. Inspired by [Matt Pocock's skills](https://github.com/mattpocock/skills), rewritten for Cursor.

## Install

From any project (or globally with `-g`):

```bash
npx skills@latest add Gabriel-Lafrance/GabrielLafrance-Skills -a cursor
```

Then in Cursor:

1. Pick the skills you want (or install all).
2. When unsure, run `/ask-gabriel`.
3. For long verifiable work, run `/goal`.
4. For a tracker ticket: `/goal IN-1234` (Linear) or `/goal #42` (GitHub).

## Main flow

```text
/goal  (or /grill-me → /architecture → /create-plan)
                         ↓
                (user confirms plan)
                         ↓
                /split-task (keep agents in the smart zone)
                         ↓
                    /implement
                         ↓
                /validate → /code-review
```


| Skill                                          | When to use                                                |
| ---------------------------------------------- | ---------------------------------------------------------- |
| [ask-gabriel](./skills/ask-gabriel/SKILL.md)   | Router — which skill/flow fits                             |
| [goal](./skills/goal/SKILL.md)                 | Keep working until a verifiable condition holds            |
| [trackers](./skills/trackers/SKILL.md)         | Fetch / update / close Linear + GitHub issues              |
| [taste](./skills/taste/SKILL.md)               | Author coding taste — shared by plan/implement/review      |
| [design](./skills/design/SKILL.md)             | UI craft — fix current UI, or Design card when creating UI |
| [grill-me](./skills/grill-me/SKILL.md)         | Relentless interview to sharpen intent                     |
| [architecture](./skills/architecture/SKILL.md) | Simple entry points + folders + scalable data              |
| [create-plan](./skills/create-plan/SKILL.md)   | Plan mode + CreatePlan (validation gate)                   |
| [split-task](./skills/split-task/SKILL.md)     | Split work into agent-sized pieces                         |
| [implement](./skills/implement/SKILL.md)       | Build approved work                                        |
| [validate](./skills/validate/SKILL.md)         | Check Done when / plan / taste / design                    |
| [code-review](./skills/code-review/SKILL.md)   | Standards + Spec via Cursor subagents                      |


## Repo layout

```text
skills/
  <skill-name>/
    SKILL.md          # required — name + description frontmatter
    examples.md       # optional progressive disclosure
LICENSE
README.md
CONTRIBUTING.md
```

## Why Cursor-only


| Agent-agnostic packs              | This pack                                         |
| --------------------------------- | ------------------------------------------------- |
| Freeform plans in chat            | Plan mode + CreatePlan + user confirm             |
| Start coding after chat agreement | No Agent edits until the plan is approved         |
| Ad-hoc “done?”                    | `/validate` against Done when                     |
| Flat file dumps                   | `/architecture` requires entry point + folder map |
| Native Claude `/goal` hook        | `/goal` skill drives this pack’s loop             |




## Attribution

Workflow ideas inspired by [mattpocock/skills](https://github.com/mattpocock/skills) (MIT). `/goal` pattern inspired by [Claude Code's](https://code.claude.com/docs/en/goal) `/goal`, reimplemented for Cursor.

## License

MIT — see [LICENSE](./LICENSE).
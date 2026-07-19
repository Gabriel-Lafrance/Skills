# Gabriel Lafrance Skills

Cursor agent skills for real engineering — not vibe coding.

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

## Skills to call

These are the skills **you** run. Everything else is internal and only used by `/goal`.

| Skill | When to use |
| --- | --- |
| [`/goal`](./skills/goal/SKILL.md) | Build a feature end-to-end (grill → plans → implement → validate → review). Pass a ticket if you have one: `/goal IN-1234` or `/goal #42`. |
| [`/analyze`](./skills/analyze/SKILL.md) | Research a task or idea. Writes findings to disk. Optionally sharpen with you, promote into a goal, or hand off to a ticket. |
| [`/write-ticket`](./skills/write-ticket/SKILL.md) | Refine or create a Linear/GitHub ticket (runs `/analyze`, then drafts and writes after you approve). |
| [`/grill-me`](./skills/grill-me/SKILL.md) | Sharpen fuzzy intent until you share the same understanding. |
| [`/architecture`](./skills/architecture/SKILL.md) | Decide structure, entry points, and data shape. |
| [`/design`](./skills/design/SKILL.md) | Craft or polish UI. |
| [`/create-plan`](./skills/create-plan/SKILL.md) | Write one plan file without starting a full `/goal`. |
| [`/code-review`](./skills/code-review/SKILL.md) | Review a branch vs `main` (or another ref you name). |
| [`/pr-review`](./skills/pr-review/SKILL.md) | Evaluate an open PR with strict taste/architecture/design; show full draft comments; ask what to publish/modify; post on the Pull Request. |
| [`/repair`](./skills/repair/SKILL.md) | Fix a bug with the smallest safe change. Escalate big multi-layer bugs to `/goal`. |
| [`/create-test`](./skills/create-test/SKILL.md) | Lock complex behavior with durable tests. Manual only — you must ask for it. |

### Typical paths

- **Just thinking** → `/analyze` → done, or promote to `/goal`, or `/write-ticket`
- **Ticket then build** → `/write-ticket` → `/goal IN-1234`
- **Build now** → `/goal` (or `/goal` + a short brief)
- **Stuck on intent** → `/grill-me`
- **Review a PR** → `/pr-review`
- **Bug** → `/repair` (or `/goal` if it's huge)

## License

MIT — see [LICENSE](./LICENSE).

Inspired by [mattpocock/skills](https://github.com/mattpocock/skills). `/goal` adapted from [Claude Code](https://code.claude.com/docs/en/goal).

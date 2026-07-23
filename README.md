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

**[`/ask-gabriel`](./skills/ask-gabriel/SKILL.md)** is the front door — sole auto-invokable skill. Agents should use it often when unsure what to run. Dual skills (`/grill-me`, `/repair`, …) pick standalone vs flow themselves ([variants.md](./skills/variants.md)).

| Skill | When to use |
| --- | --- |
| [`/ask-gabriel`](./skills/ask-gabriel/SKILL.md) | Unsure which skill; what next; before non-trivial work |
| [`/goal`](./skills/goal/SKILL.md) | Build a feature end-to-end with user-locked Active Rules (grill → plans → implement → validate → review). Pass a ticket: `/goal IN-1234` or `/goal #42`. |
| [`/analyze`](./skills/analyze/SKILL.md) | Research a task or idea. Writes findings to disk. Optionally promote to `/goal` or `/write-ticket`. |
| [`/write-ticket`](./skills/write-ticket/SKILL.md) | Refine or create a Linear/GitHub Feature, Tweak, Bug, or Refactor ticket (open grill → `/analyze` → draft → write after you approve). |
| [`/publish`](./skills/publish/SKILL.md) | Put work on a typed branch (`feature|tweak|bug|refactor/<ticket>-<slug>`), push, then draft/publish a PR (What changed, How to QA, ticket link). |
| [`/just-do-it`](./skills/just-do-it/SKILL.md) | Linear ticket → early branch → analyze → goal → dual code-review (Fix-now blockers only) → landed PR. Human reviews after. |
| [`/grill-me`](./skills/grill-me/SKILL.md) | Sharpen fuzzy intent until you share the same understanding. |
| [`/architecture`](./skills/architecture/SKILL.md) | Decide structure, entry points, and data shape. |
| [`/design`](./skills/design/SKILL.md) | Craft or polish UI. |
| [`/code-review`](./skills/code-review/SKILL.md) | Initial deep review of a branch vs `main`; post-fix re-review stays targeted to named blockers. |
| [`/pr-review`](./skills/pr-review/SKILL.md) | Evaluate a PR: triage priors, rescan; one finding per comment; post via gh only. |
| [`/repair`](./skills/repair/SKILL.md) | Fix a bug with the smallest safe change. Escalate huge bugs to `/goal`. |
| [`/create-test`](./skills/create-test/SKILL.md) | Lock complex behavior with durable tests. Only after `/code-review` or `/pr-review` recommends — you must run it. |

Internals (`/validate`, `/implement`, `/taste`, `/orchestrate`, …) are looked up by `/goal` or `/repair` — not typical user entries. Coding taste is loaded via `/taste` when other skills need it.

### Typical paths

- **Unsure** → `/ask-gabriel`
- **Just thinking** → `/analyze` → done, or promote to `/goal`, or `/write-ticket`
- **Ticket then build** → `/write-ticket` → `/goal IN-1234`
- **Build now** → `/goal` (or `/goal` + a short brief)
- **Ship a branch/PR** → `/publish`
- **Ticket → PR (autonomous)** → `/just-do-it IN-1234` (human reviews the PR after)
- **Stuck on intent** → `/grill-me`
- **Review a PR** → `/pr-review`
- **Bug** → `/repair` (or `/goal` if it's huge)

## License

MIT — see [LICENSE](./LICENSE).

Maintaining the pack (structure, adding skills): [how-to.md](./how-to.md).

Inspired by [mattpocock/skills](https://github.com/mattpocock/skills). `/goal` adapted from [Claude Code](https://code.claude.com/docs/en/goal).

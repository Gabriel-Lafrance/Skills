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

**[`/ask-gabriel`](./skills/ask-gabriel/SKILL.md)** is the front door — sole auto-invokable skill. Agents should use it often when unsure what to run. Dual skills (`/grill-me`, `/taste`, `/architecture`, `/analyze`, `/goal`, …) pick standalone vs flow themselves ([variants.md](./skills/pack-shared/variants.md)).

| Skill | When to use |
| --- | --- |
| [`/ask-gabriel`](./skills/ask-gabriel/SKILL.md) | Unsure which skill; what next; before non-trivial work |
| [`/goal`](./skills/goal/SKILL.md) | Build a feature end-to-end with user-locked Active Rules (grill → plans → implement → acceptance evidence → review). Always loads `/taste`; loads `/architecture` unless trivial. Pass a ticket: `/goal IN-1234` or `/goal #42`. |
| [`/analyze`](./skills/analyze/SKILL.md) | Research a task or idea in chat. Always applies `/taste`; loads `/architecture` when structure is in play. Optionally save a user-requested memo, promote to `/goal`, or hand off to `/write-ticket`. |
| [`/taste`](./skills/taste/SKILL.md) | Coding style and named principles (KISS, SoC, SLAP, CQS, fail fast, Boy Scout, cohesion/coupling, idempotency, explicit, PoLA). Standalone audit/fix, or loaded by parents before code. |
| [`/architecture`](./skills/architecture/SKILL.md) | Decide structure, services, entry points, and data shape (SoC, cohesion/coupling, idempotent writes). |
| [`/write-ticket`](./skills/write-ticket/SKILL.md) | Refine or create a Linear/GitHub Feature, Tweak, Bug, or Refactor ticket (open grill → `/analyze` → draft → write after you approve). |
| [`/publish`](./skills/publish/SKILL.md) | Put work on a typed branch (`feature|tweak|bug|refactor/<ticket>-<slug>`), push, then draft/publish a PR (What changed, How to QA, ticket link). |
| [`/just-do-it`](./skills/just-do-it/SKILL.md) | Linear ticket → early branch → analyze → goal → dual code-review (Fix-now blockers only) → opened PR. Human reviews after. |
| [`/grill-me`](./skills/grill-me/SKILL.md) | Sharpen fuzzy intent until you share the same understanding. |
| [`/design`](./skills/design/SKILL.md) | Craft or polish UI. |
| [`/code-review`](./skills/code-review/SKILL.md) | Initial deep review of a branch vs `main`; named blockers are analyzed with proposed fixes before optional promotion, then re-review stays targeted. |
| [`/pr-review`](./skills/pr-review/SKILL.md) | Evaluate a PR: triage all prior threads, then review the changed surface; one finding per comment; post via gh only. |
| [`/create-test`](./skills/create-test/SKILL.md) | Lock complex behavior with durable tests. Only after `/code-review` or `/pr-review` recommends — you must run it. |

Internals (`/implement`, `/orchestrate`, …) are looked up by `/goal` or `/just-do-it` — not typical user entries. `/taste` and `/architecture` are user-facing as well as parent-loaded.

### Typical paths

- **Unsure** → `/ask-gabriel`
- **Just thinking** → `/analyze` → done, or promote to `/goal`, or `/write-ticket`
- **Style / principles** → `/taste`
- **Structure first** → `/architecture` → `/goal`
- **Ticket then build** → `/write-ticket` → `/goal IN-1234`
- **Build now** → `/goal` (or `/goal` + a short brief)
- **Ship a branch/PR** → `/publish` (standalone `/goal` hands off here after completion)
- **Ticket → PR (autonomous)** → `/just-do-it IN-1234` (human reviews the PR after)
- **Stuck on intent** → `/grill-me`
- **Review a PR** → `/pr-review`
- **Bug** → `/analyze` → `/goal`

## License

MIT — see [LICENSE](./LICENSE).

Maintaining the pack (structure, adding skills): [how-to.md](./how-to.md).

Inspired by [mattpocock/skills](https://github.com/mattpocock/skills). `/goal` adapted from [Claude Code](https://code.claude.com/docs/en/goal).

# Gabriel Lafrance Skills

Cursor agent skills for real engineering work.

## Install

```bash
# Global (recommended)
npx skills@latest add Gabriel-Lafrance/Skills -a cursor -s '*' -g -y
npx skills@latest update -g -y

# Or project-only
npx skills@latest add Gabriel-Lafrance/Skills -a cursor -s '*' -y
```

Optional: paste [`cursor-rules/ultimate-gold-standards.mdc`](./cursor-rules/ultimate-gold-standards.mdc) (body only, no YAML frontmatter) into **Cursor Settings → Rules → User Rules** so Plan mode and freeform chats load taste, architecture, and publish doctrines without invoking a skill.

## What this pack is

Five kinds of skills. **Guide** informs; everything else moves work forward.

| Job               | Skills                                                   | Purpose               |
| ----------------- | -------------------------------------------------------- | --------------------- |
| **Guide**         | `/ask-gabriel`, `/taste`, `/architecture`                | Route and standards   |
| **Clarify**       | `/grill-me`, `/analyze`                                  | Intent and research   |
| **Specify**       | `/write-ticket`                                          | Tracker tickets       |
| **Build**         | `/goal`, `/just-do-it`                                   | Implement end-to-end  |
| **Review & ship** | `/code-review`, `/publish`, `/pr-review`, `/create-test` | Quality gates and PRs |

```mermaid
flowchart LR
  clarify[Clarify] --> build[Build]
  specify[Specify] --> build
  guide[Guide] -.-> build
  build --> ship[Review and ship]
```

**Unsure which to run?** Start with [`/ask-gabriel`](./skills/ask-gabriel/SKILL.md).

## Common paths

- Think / research → `/analyze`
- Fuzzy intent → `/grill-me`
- Ticket → build → `/write-ticket` then `/goal`
- Build now → `/goal` or `/just-do-it`
- Ship a PR → `/publish`
- Review a PR → `/pr-review`

Skill details live under [`skills/`](./skills/). Pack maintenance: [how-to.md](./how-to.md).

## License

MIT — see [LICENSE](./LICENSE).

## Community

- [Contributing](.github/CONTRIBUTING.md)
- [Code of Conduct](.github/CODE_OF_CONDUCT.md)
- [Security policy](.github/SECURITY.md)

Inspired by [Matt Pocock](https://github.com/mattpocock/skills).

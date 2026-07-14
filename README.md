# Gabriel Lafrance Skills (Cursor)

[![skills.sh](https://skills.sh/b/gabriellafrance/GabrielLafrance-Skills)](https://skills.sh/gabriellafrance/GabrielLafrance-Skills)

Cursor-first agent skills for real engineering — not vibe coding.

Plan mode, CreatePlan, simple entry points, folder structure, tasteful UI, and a validate-before-ship loop. Inspired by [Matt Pocock's skills](https://github.com/mattpocock/skills), rewritten for Cursor.

## Install

From any project (or globally with `-g`):

```bash
npx skills@latest add gabriellafrance/GabrielLafrance-Skills -a cursor
```

Then in Cursor:

1. Pick the skills you want (or install all).
2. When unsure, run `/ask-gabriel`.
3. For long verifiable work, run `/goal`.
4. For a tracker ticket: `/goal IN-1234` (Linear) or `/goal #42` (GitHub).

### Useful variants

```bash
# Browse what’s in the repo (no install)
npx skills@latest add gabriellafrance/GabrielLafrance-Skills --list

# One skill only
npx skills@latest add gabriellafrance/GabrielLafrance-Skills --skill architecture -a cursor

# All skills, Cursor only, non-interactive
npx skills@latest add gabriellafrance/GabrielLafrance-Skills --skill '*' -a cursor -y

# Global (all your projects)
npx skills@latest add gabriellafrance/GabrielLafrance-Skills -g -a cursor

# Update later
npx skills@latest update
```

Project installs land under `.cursor/skills/`. Global installs land under `~/.cursor/skills/`.

### Try before the repo is public

```bash
npx skills@latest add /absolute/path/to/GabrielLafrance-Skills -a cursor --list
npx skills@latest add /absolute/path/to/GabrielLafrance-Skills -a cursor -y
```

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

| Skill | When to use |
| --- | --- |
| [ask-gabriel](./skills/ask-gabriel/SKILL.md) | Router — which skill/flow fits |
| [goal](./skills/goal/SKILL.md) | Keep working until a verifiable condition holds |
| [trackers](./skills/trackers/SKILL.md) | Fetch / update / close Linear + GitHub issues |
| [taste](./skills/taste/SKILL.md) | Author coding taste — shared by plan/implement/review |
| [design](./skills/design/SKILL.md) | UI craft — fix current UI, or Design card when creating UI |
| [grill-me](./skills/grill-me/SKILL.md) | Relentless interview to sharpen intent |
| [architecture](./skills/architecture/SKILL.md) | Simple entry points + folders + scalable data |
| [create-plan](./skills/create-plan/SKILL.md) | Plan mode + CreatePlan (validation gate) |
| [split-task](./skills/split-task/SKILL.md) | Split work into agent-sized pieces |
| [implement](./skills/implement/SKILL.md) | Build approved work |
| [validate](./skills/validate/SKILL.md) | Check Done when / plan / taste / design |
| [code-review](./skills/code-review/SKILL.md) | Standards + Spec via Cursor subagents |

## Publish (maintainers)

This pack is just a **public GitHub repo** with `skills/*/SKILL.md`. `npx skills` installs from GitHub — no npm publish step.

### 1. First-time push

```bash
cd /path/to/GabrielLafrance-Skills

git add .
git commit -m "$(cat <<'EOF'
Initial Cursor skills pack.

EOF
)"

# Create the public repo (GitHub CLI), then push
gh repo create gabriellafrance/GabrielLafrance-Skills --public --source=. --remote=origin --push
```

Without `gh`: create an empty public repo on GitHub named `GabrielLafrance-Skills`, then:

```bash
git remote add origin git@github.com:gabriellafrance/GabrielLafrance-Skills.git
git push -u origin main
```

If your GitHub username is not `gabriellafrance`, change the owner in the install commands and the skills.sh badge URL.

### 2. Verify discovery

```bash
npx skills@latest add gabriellafrance/GabrielLafrance-Skills --list
```

You should see every skill under `skills/`.

### 3. Optional — skills.sh listing

After the repo is public, the badge above resolves at [skills.sh/gabriellafrance/GabrielLafrance-Skills](https://skills.sh/gabriellafrance/GabrielLafrance-Skills). If it does not appear yet, skills.sh may need an index request (community often files an issue on [vercel-labs/skills](https://github.com/vercel-labs/skills)). Install via `npx skills add owner/repo` works as soon as GitHub is public — you do not need skills.sh for that.

### 4. Suggested GitHub topics

`cursor` · `agent-skills` · `skills` · `ai` · `claude-code` (optional) · `productivity`

### 5. Ship updates

```bash
git add skills README.md
git commit -m "Describe the skill change"
git push
# Consumers:
npx skills@latest update
```

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

Valid for the skills CLI: flat `skills/<name>/SKILL.md` (what this repo uses).

## Why Cursor-only

| Agent-agnostic packs | This pack |
| --- | --- |
| Freeform plans in chat | Plan mode + CreatePlan + user confirm |
| Start coding after chat agreement | No Agent edits until the plan is approved |
| Ad-hoc “done?” | `/validate` against Done when |
| Flat file dumps | `/architecture` requires entry point + folder map |
| Native Claude `/goal` hook | `/goal` skill drives this pack’s loop |

## Attribution

Workflow ideas inspired by [mattpocock/skills](https://github.com/mattpocock/skills) (MIT). `/goal` pattern inspired by [Claude Code's `/goal`](https://code.claude.com/docs/en/goal), reimplemented for Cursor.

## License

MIT — see [LICENSE](./LICENSE).

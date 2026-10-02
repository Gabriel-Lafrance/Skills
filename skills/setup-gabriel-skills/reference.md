# Setup Gabriel skills reference

Load with [SKILL.md](SKILL.md). Install skills with `npx skills`. Place `AGENTS.md` verbatim from the pack file or the raw GitHub URL, and write no lint files.

## Resolve the skill root

Resolve the skill root using [AGENTS.md, Find the pack](../../AGENTS.md#find-the-pack), including workspace, user, pack-repository, and installed-plugin locations. That section owns the search order; do not substitute a home-only lookup. Use the resolved root for this skill's sibling rules and other skills.

This workspace is the Skills pack when a parent directory holds both an `AGENTS.md` with `gabriel-skills-agents` and `skills/setup-gabriel-skills/`.

## Verify

Read the disk and print a short list.

| Fact | How to see it |
| --- | --- |
| User skills | `rules/code-quality.md` under `~/.agents/skills/`, `~/.claude/skills/`, or `~/.cursor/skills/` |
| Repo skills | `rules/code-quality.md` under the workspace `.agents/skills/`, `.claude/skills/`, or `.cursor/skills/` (ignore when the workspace is the Skills pack) |
| Repo contract | workspace-root `AGENTS.md`: missing, pack copy (has `gabriel-skills-agents`), or someone else's file |
| Harnesses in use | a home or project folder that exists: `.cursor/` or `~/.cursor/`, `.claude/` or `~/.claude/`, `.agents/` or `~/.agents/`, `$CODEX_HOME` or `~/.codex/`, `.gemini/` or `~/.gemini/`, or `.aider.conf.yml` |

## Questions

After Verify, one batch. Wait, and install after they reply. Shape: [Asking the user](../rules/writing-style.md#asking-the-user).

```markdown
## Questions
Reply like: 1a

1. Where should this pack's skills and AGENTS.md go?
   - a) This repo recommended
   - b) This repo and user-level (every repo on this machine)
   - c) User-level only
```

If they pick c, say that Cursor has no user-level `AGENTS.md`, so Cursor in this repo will not see the rules until the repo has that file.

## Pack skills

`npx skills add gabriel-lafrance/skills@setup-gabriel-skills` copies only this skill. This step lands the rest of the pack, including `rules/`, for each chosen scope. Skip it when the workspace is the Skills pack. That skip is success, not a failure.

A scope is current when `rules/code-quality.md` exists in it. A scope with pack skills but no `rules/code-quality.md` is stale: update it.

```bash
# User-level (b or c)
npx skills@latest add gabriel-lafrance/skills --all -g

# This repo (a or b)
npx skills@latest add gabriel-lafrance/skills --all

# Stale copy
npx skills@latest update
```

`--all` installs every skill into every harness the CLI sees, with no prompt. If a command fails (no network, old Node, permission), record the failure and continue to [Place AGENTS.md](#place-agentsmd). Land skill folders only through the command. Offer the manual copy only after both this step and the `AGENTS.md` place have been tried.

## Place AGENTS.md

Do this for the scopes they chose. Touch only harnesses in use.

**Source:** the pack root `AGENTS.md` when the workspace is the Skills pack. Otherwise fetch `https://raw.githubusercontent.com/Gabriel-Lafrance/Skills/main/AGENTS.md`. The bytes must contain `gabriel-skills-agents`. If the fetch fails or the marker is missing, record a failure and write no substitute from memory.

**Never overwrite someone else's instructions file.** A file is the pack's only when it contains `gabriel-skills-agents`. A pack file may be refreshed. Every other file only gets a pointer line.

### Repo (a or b)

1. Workspace-root `AGENTS.md` missing: write the source there.
2. It has the marker: overwrite it with the source.
3. It exists without the marker: append the pointer below, then say so. Keep their text.

```markdown

## Gabriel skills

Also follow the Gabriel skills contract: https://github.com/Gabriel-Lafrance/Skills/blob/main/AGENTS.md
```

Skip the append when the file already links that URL.

Then, for each harness in use, add one pointer line when that file is how the harness finds the contract:

| Harness | In use when this exists | File | Pointer line |
| --- | --- | --- | --- |
| Claude Code | `.claude/` | `CLAUDE.md` | `@AGENTS.md` |
| Gemini CLI | `.gemini/` | `GEMINI.md` | `@AGENTS.md` |
| Aider | `.aider.conf.yml` | `.aider.conf.yml` (edit only, never create) | `read: AGENTS.md`, or append `AGENTS.md` to an existing `read` list |

Missing pointer file: create it with only that line. Existing file without the line: append the line. Already present: leave it. Cursor, Codex, and Copilot read the workspace `AGENTS.md` and get no extra file.

### User level (b or c)

Only touch a home that already exists. Never create one.

| Harness | Home | What to do |
| --- | --- | --- |
| Codex | `$CODEX_HOME` when set, else `~/.codex/` | `AGENTS.md` missing or a pack copy: write the source. Someone else's file: append `Follow https://github.com/Gabriel-Lafrance/Skills/blob/main/AGENTS.md.` |
| Claude Code | `~/.claude/` | Pointer line `@AGENTS.md` in `~/.claude/CLAUDE.md`, by the repo rule above |
| Gemini CLI | `~/.gemini/` | Pointer line `@AGENTS.md` in `~/.gemini/GEMINI.md`, same rule |
| Cursor | `~/.cursor/` | No user-level `AGENTS.md`. Skills still install under `~/.cursor/skills/`. Say the repo file is what Cursor reads |

## Manual install

Run this section only when the skills command failed or `AGENTS.md` could not be placed. The Skills-pack skip alone does not qualify.

Ask once. Wait.

```markdown
## Questions
Reply like: 1a

1. I could not install the skills and rules. Try a manual install?
   - a) yes recommended
   - b) no
```

**No:** say setup failed. List what already landed. Stop. Keep those files.

**Yes:** link https://github.com/Gabriel-Lafrance/Skills and give only the rows for the harnesses in use and the scopes they chose.

Skills, including `rules/`, are the `skills/` folders in that repo. Copy each skill folder, not the repo root.

| Scope | Harness | Put the skill folders here |
| --- | --- | --- |
| This repo | Cursor | `.cursor/skills/` |
| This repo | Claude Code | `.claude/skills/` |
| This repo | Codex | `.agents/skills/` |
| User level | Cursor | `~/.cursor/skills/` |
| User level | Claude Code | `~/.claude/skills/` |
| User level | Codex | `~/.agents/skills/` |

`AGENTS.md` is the file at the repo root.

| Scope | Harness | Put `AGENTS.md` here |
| --- | --- | --- |
| This repo | Cursor, Codex, Copilot | workspace root `AGENTS.md` |
| This repo | Claude Code | workspace root `AGENTS.md`, plus `@AGENTS.md` in `CLAUDE.md` |
| This repo | Gemini CLI | workspace root `AGENTS.md`, plus `@AGENTS.md` in `GEMINI.md` |
| User level | Codex | `$CODEX_HOME/AGENTS.md` or `~/.codex/AGENTS.md` |
| User level | Cursor | no user-level file; Cursor reads the repo `AGENTS.md` |

Tell them to keep any `AGENTS.md` that is not this pack's. After they confirm the files are in place, re-check the paths and report what you can see. If the files are still missing, setup failed.

## Clean up old installs

Older versions of this pack left files that nothing reads now. Delete only these, only in the scopes they chose. Skip cleanup when setup has already failed.

- **Old Claude copy** (b or c): if `~/.claude/gabriel-skills/AGENTS.md` contains `gabriel-skills-agents`, delete it, and remove the `@~/.claude/gabriel-skills/AGENTS.md` line from `~/.claude/CLAUDE.md` when present. Remove `~/.claude/gabriel-skills/` only if it is then empty. A file there without the marker stays.
- **Old Cursor pointer:** delete `gabriel-skills/follow-agents.mdc` under `~/.cursor/rules` (b or c) or the app `.cursor/rules` (a or b) when it exists. Leave every other Cursor rule and hook.
- **Retired skill folders:** in each skill root this run installs into, delete a folder named `setup-toolkit`, `pack-shared`, `create-test`, `code-review`, `pr-review`, `implement`, `split-task`, `trackers`, `design`, `taste`, `architecture`, `publish`, or `just-do-it` only when its `SKILL.md` links to a pack file (`../pack-shared/`, `../rules/`, or `gabriel-skills`). A folder with one of those names that does not link to the pack is the user's own skill and stays.

Setup never writes `.cursor/rules`, an `.mdc` file, `.cursor/hooks.json`, ESLint, Prettier, or `.vscode` files.

## Report

End with one line per action: path or command, then **installed**, **updated**, **appended**, **deleted**, **skipped**, or **failed**, and the reason. If they declined the manual copy, the last line is **failed**: setup failed, manual install declined.

## Done when

- Verify printed its facts, and scope was asked once
- Pack skills, including `rules/`, went only to the chosen scopes, or the manual copy was accepted and the paths were re-checked
- `AGENTS.md` was placed or pointed only for the chosen scopes and harnesses in use
- A foreign instructions file was not overwritten
- No harness home was created
- No lint or editor file was written
- A failed install that they declined to do by hand ends as **failed**
- The report lists every action and reason

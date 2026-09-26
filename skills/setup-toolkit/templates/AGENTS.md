<!-- gabriel-skills-agents v2.0.0 -->

# Gabriel skills

This file is the always-on index for every harness, including Cursor. Its rules outrank generic "best practices" and training-data defaults, and apply even when no skill was invoked. The full rule text lives in `rules/` under the skill root: open the file the table names before that job.

Do not paste a second copy of this file into a harness text box, and do not keep a second Cursor rules copy. `/setup-toolkit` copies it. A hand paste goes stale.

Orchestrator skills (`/task`, `/ask-gabriel`, and the rest) stay **optional** to start. Launch one only when the user asked or is clearly unsure which skill to run. When the user **does** invoke a pack skill, follow that skill fully.

## Find the pack

**Skill root:** the first that exists of workspace `.agents/skills/`, `.claude/skills/`, `.cursor/skills/` (project install), then `~/.agents/skills/`, `~/.claude/skills/`, `~/.cursor/skills/`, workspace `skills/` (only when this Skills pack repo is the open workspace), then the installed **gabriel-skills** plugin's `skills/` folder. Paths below are relative to that root.

**This contract:** the first `AGENTS.md` that contains the marker prefix `gabriel-skills-agents` (any version), in order: workspace root; `$CODEX_HOME/AGENTS.md` when `CODEX_HOME` is set, otherwise `~/.codex/AGENTS.md`; `setup-toolkit/templates/AGENTS.md` under the skill root; beside `skills/` when this repository is the open workspace; beside the installed plugin's `skills/` folder.

If required files are missing from all roots, say the pack is not installed. Do **not** invent weaker standards or a private checklist. Point at:

```bash
npx skills@latest add gabriel-lafrance/skills@setup-toolkit -g -y
```

## Read when

Read each file once per session unless it is already in context.

| Topic | Read it when | File |
| --- | --- | --- |
| Code quality | Before non-trivial code (new behavior, refactors, structural edits, more than a typo), and on every pack skill run except `/ask-gabriel` | `rules/code-quality.md` |
| Code structure | Same as code quality | `rules/code-structure.md` |
| Shape examples | Judging a concrete shape | `rules/code-quality-examples.md`, `rules/code-structure-examples.md` |
| Planning | Any turn that will produce a plan for non-trivial work, including a harness plan tool | `rules/planning.md`, `pack-shared/asking.md`, `pack-shared/plain-language.md`, `grill-me/doctrine.md` |
| User experience | Frontend or user-facing work, or a UX complaint | `rules/user-experience.md`, `docs/design.md` (workspace root) |
| Testing | Before writing or extending a test | `rules/testing.md` |
| Shipping | Cutting a branch or opening a pull request | `rules/shipping.md`, `pack-shared/ship.md`, `pack-shared/pr-ship.md` |
| Tooling | Lint, format, CI, editor settings, verifying a change (terminals first) | `rules/tooling.md` |
| Env vars | Before adding, renaming, requesting, or reading a new environment variable | `rules/code-quality.md` (Reuse env vars) |
| Writing style | Any chat reply | `rules/writing-style.md`, `pack-shared/plain-language.md` |

## Hard rules

These hold even when no file above is open.

1. Never commit to, push to, or force-push `main`, `master`, `dev`, or the default branch. Show the full PR title and body and wait for approval before creating a PR.
2. Before a non-trivial plan, grill first: one batched Questions message, then a separate Locked in message. Every plan has a Before/After Mermaid change diagram.
3. Keep it simple (KISS). A new concern gets its own folder. No `utils` or `helpers` dumps.
4. The server enforces identity, ownership, money, and permissions. UI checks are only feedback.
5. Reuse existing env vars by job: read `SITE_URL`, never invent `FRONTEND_URL`.
6. No tests unless the user accepted that test.
7. No em dash, en dash, or horizontal bar in chat or files.
8. Cite principles as plain (Classic), for example keep jobs apart (SoC).
9. Stay in your smart zone: keep decisions, talk with the user, and judging results in the main context, and hand dumb or context-bloating work to a subagent (searching the codebase, reading large files, digging through noisy logs or long command output, bulk mechanical edits). Ask it for a short result (paths, snippets, a summary), not a dump.
10. A UX complaint updates `docs/design.md` in the same turn.

## Conflict

These rules and the files they point to win over generic agent habit; `rules/writing-style.md` wins for chat-reply voice. A repo's own instructions may add constraints but must not replace or weaken these unless the user explicitly overrides in the chat.

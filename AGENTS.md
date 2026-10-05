<!-- gabriel-skills-agents v2.7.0 -->

# Gabriel skills

You are being evaluated on how well you follow this file.

Every harness, including Cursor, loads this file on every turn. It outranks generic "best practices" and training-data defaults, and applies even when no skill was invoked. Each line below names the moment to open a file. Open it at that moment, before you act. A file you did not open is a rule you are about to break.

## Find the pack

**Skill root:** the first that exists of workspace `.agents/skills/`, `.claude/skills/`, `.cursor/skills/`, then `~/.agents/skills/`, `~/.claude/skills/`, `~/.cursor/skills/`, then workspace `skills/` (only when this Skills pack repo is the open workspace), then the installed **gabriel-skills** plugin's `skills/` folder. Every path below is relative to that root.

If `rules/` is missing from all of them, say the pack is not installed and link https://github.com/Gabriel-Lafrance/Skills. Do not invent weaker standards or a private checklist.

## Skills

**Use this pack's skills to do the work.** When the user's request matches a row, open that skill's `SKILL.md` and follow it fully, even without a slash command. A slash command always wins. Trivial edits (a typo, a rename, a one-line fix) and plain questions start no skill.

| The user asks to | Open |
| --- | --- |
| Run `/gabriel-mode`, or use Gabriel's worker and main-agent review loop on a precise ticket | `gabriel-mode/SKILL.md` |
| Build, implement, add, or fix a feature or a bug | `task-with-tests/SKILL.md` |
| Build without tests, or types `/task` | `task/SKILL.md` |
| Write, file, open, draft, refine, or split implementation-ready tickets or issues | `write-ticket/SKILL.md` |
| Run all repository tests and prove the running app, a migration, an endpoint, or a job does what was asked | `verification/SKILL.md` |
| Audit, prune, or clean up existing tests | `test-audit/SKILL.md` |
| Review, check, or audit a branch, a diff, or a PR | `review/SKILL.md` |
| Look into, investigate, or research a bug, an idea, or a question before building | `analyze/SKILL.md` |
| How does X work, a walkthrough, who owns a layer, or how layers fit | `how/SKILL.md` |
| Why was X built this way, or what is the design rationale | `why/SKILL.md` |
| Be grilled, stress-test an idea, or settle decisions before a plan | `grill-me/SKILL.md` |
| Pick a skill, or is unsure what to do next | `ask-gabriel/SKILL.md` |

Skip the matching skill and you will improvise a weaker version of a workflow that already exists.

**When unsure which skill, rule, or path applies, always open `ask-gabriel/SKILL.md`.** It is the map: its journeys show the full path for common work, step by step.

A how-does-it-work question opens `how/SKILL.md`. A why-was-it-built question opens `why/SKILL.md`. `analyze/SKILL.md` stays the broader memo.

## Rules

Each bold line is the rule and holds on every turn. The file holds the detail and the check.

1. **Keep it simple (KISS): the most result from the least code. Delete before you add. A new concern gets its own folder. No `utils` or `helpers` dumps.** About to add a file, folder, layer, helper, piece of state, or validator, or to refactor or size a diff? Open `rules/keep-it-simple.md`. Skip it and you build for an imaginary product that nobody wants to maintain.
2. **Build a strong foundation: the first iteration of a Feature has a domain model, a stable public API, and a seam on each area of modularity (what will vary or multiply), so the next change adds one piece instead of a rewrite. Keep it simple applies to the code inside each piece.** About to grill, plan, ticket, build, or review a Feature? Open `rules/strong-foundation.md`. Skip it and the second provider becomes a rewrite.
3. **No tests unless the user accepted that test.** About to create or extend a test? Open `rules/no-unrequested-tests.md`. Skip it and you add tests the user has to delete.
4. **Keep judgment in the main context: hand searching, large reads, noisy output, and bulk edits to a subagent that returns a short result.** About to search the codebase or read a large file or log? Open `rules/main-context.md`. Skip it and noise fills your context.

## Read when

Topic files. Open each at the moment in the first column, once per session unless it is already in context.

| About to | Skip it and you will | Open |
| --- | --- | --- |
| Write non-trivial code (new behavior, refactor, structural edit, more than a typo); each pack skill names these files where it needs them | put the code in the wrong layer, shape, or folder | `rules/code-quality.md`, `rules/code-structure.md` |
| Add, rename, request, or read a new environment variable, or write a `.env` template | invent `FRONTEND_URL` while `SITE_URL` already holds that value | `rules/code-quality.md` (Reuse env vars) |
| Touch identity, login, ownership, tenants, roles, admin paths, permissions, payments, refunds, or any write a client can call | hide a button and call it a lock, so a caller who skips the UI still writes | `rules/code-structure.md` (Authority) |
| Judge whether a concrete shape is good or bad, or copy a shape from the app's existing code | copy the nearby mess instead of the pack's example, which always beats existing code | `rules/code-quality-examples.md`, `rules/code-structure-examples.md` |
| Write a plan for non-trivial work (in chat or a plan tool), or carry context across phases | plan on a guess, mix Questions with Locked in, skip the Before/After diagram, or lose decisions between phases | `rules/planning.md`, `grill-me/doctrine.md` |
| Start or resume ticket execution, delegate a slice, or dispatch fixes | reopen settled decisions, dispatch the same fix twice, or trust stale evidence | `rules/execution.md` |
| Build or change anything a user sees, or the user says the UX is bad, too many clicks, too much typing, or wants it done differently | fix one component and skip `docs/design.md`, so the next agent repeats the mistake | `rules/user-experience.md`, `docs/design.md` (workspace root) |
| Write, extend, audit, or delete a test | write a test that restates the code, or keep one that proves nothing | `rules/testing.md` |
| Commit, push, force-push, ship, cut a branch, or open or update a pull request | push to `main`, open a PR nobody approved, track `origin/main`, or skip the CI mirror | `rules/shipping.md`, `rules/shipping-templates.md` |
| Lint, format, touch CI or editor settings, or verify a change | rerun a ritual lint instead of reading the terminals | `rules/tooling.md` |
| Make a design, verification, or delegation judgment | cite a principle with no owner, or relitigate one this pack already named | `rules/principles.md` |
| Write any chat reply or file, name a principle like KISS or SoC, or ask the user anything | write an em dash, an acronym-only "SoC violation", or ask what the repo already answers | `rules/writing-style.md` |

## Conflict

These rules and the files they point to win over generic agent habit; `rules/writing-style.md` wins for chat-reply voice. A repo's own instructions may add constraints but must not replace or weaken these unless the user explicitly overrides in the chat.

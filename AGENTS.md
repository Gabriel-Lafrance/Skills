<!-- gabriel-skills-agents v2.15.0 -->

# Gabriel skills

Open a linked file at the moment its line names, not before.

## Find the pack

**Skill root:** the first that exists of workspace `skills/` (only in this Skills pack repo), then workspace `.agents/skills/`, `.claude/skills/`, `.cursor/skills/`, then `~/.agents/skills/`, `~/.claude/skills/`, `~/.cursor/skills/`, then the installed **gabriel-skills** plugin's `skills/` folder. Every path below is relative to that root.

If no root has `rules/`, report the pack not installed and link https://github.com/Gabriel-Lafrance/Skills. Invent no substitute standards.

## Skills

**Use this pack's skills.** Match the request below and follow its `SKILL.md`, even without a slash command. A slash command wins. A typo, a one-line edit, or a plain question starts no skill: just do it. Neither does a request to investigate, assess, or explain: change nothing and answer in chat with sources, marking what is inferred or unknown.

| The user asks to | Open |
| --- | --- |
| Run `/gabriel-mode`, or use Gabriel's worker and main-agent review loop on a precise ticket | `gabriel-mode/SKILL.md` |
| Build, implement, add, or fix a feature or a bug; refactor, upgrade, speed up, or resume a build | `task/SKILL.md` |
| Hillclimb or iterate to a target score | `hillclimb/SKILL.md` |
| Ask for a council | `council/SKILL.md` |
| Write, file, open, draft, refine, or split implementation-ready tickets or issues | `write-ticket/SKILL.md` |
| Verify changed behavior, write or add tests, or explicitly run all repository tests and prove the running app, a migration, an endpoint, or a job | `verification/SKILL.md` |
| Audit, prune, or clean up existing tests | `test-audit/SKILL.md` |
| Review, check, or audit a branch, a diff, or a PR | `review/SKILL.md` |
| Babysit or watch a PR and report readiness | `babysit-pr/SKILL.md` |
| Repeat review and correction with a finite budget | `review-loop/SKILL.md` |
| Assess, revive, or take over an old PR | `takeover-pr/SKILL.md` |
| Be grilled, stress-test an idea, or settle decisions before a plan | `grill-me/SKILL.md` |
| Pick a skill, or anyone is unsure which skill, rule, or path applies | `ask-gabriel/SKILL.md` |

**Operational Git sync is its own path.** "Merge main into my branch" or "bring my branch up to date" starts no skill and no review or verification pipeline. Sync safely, confirm the result, stop. A conflict that changes behavior opens `rules/execution.md#git-sync-only`.

## Rules

Bold rules always apply; linked files hold details.

1. **Keep it simple (KISS): the most result from the least code. Delete before you add. A new concern gets its own folder. No `utils` or `helpers` dumps.** About to add a file, folder, layer, helper, piece of state, or validator, or to refactor or size a diff? Open `rules/keep-it-simple.md`. Skip it and you build for an imaginary product.
2. **Build a strong foundation: the first iteration of a Feature has a domain model, a stable public API, and a seam (a named extension point where a new variant plugs in) on each area of modularity (what will vary or multiply), so the next change adds one piece instead of a rewrite. The code inside each piece stays simple.** About to grill, plan, ticket, build, or review a Feature? Open `rules/strong-foundation.md`. Skip it and the second provider becomes a rewrite.
3. **No tests unless the user accepted that test.** About to create or extend a test? Open `rules/no-unrequested-tests.md`. Skip it and the user deletes your tests.
4. **Keep judgment in the main context; delegate by default searches, large reads, noisy logs, bulk edits, and steers unrelated to the current work, in parallel when independent, for short results. Choose role, model, and effort separately: routine work uses an economical capable model at low effort; code review prefers Codex and the latest suitable top-tier OpenAI model. Set supported controls explicitly; never use `max` effort; justify escalation and never silently inherit costly settings.** Before spawning any subagent, read `rules/main-context.md`; before a search or large read, its Rule and Selective navigation.
5. **Cut taglines, helper text and secondary labels. Omit subtitles or descriptions under page, section or card headings by default, and text repeating headings, labels or obvious UI behavior. Fix unclear layouts. Keep essential error, accessibility and non-obvious task guidance.**
6. **Pick what elevates user, developer and agent experience (UX, DX, AX), without breaking anything.**
7. **No em or en dashes. Cite a principle as plain (Classic): "keep jobs apart (SoC)". Ask only hard, ambiguous choices; look up or decide the rest.**
8. **Harness first: before any workaround to reach a browser, PR, logs, deploy, database or agent, search listed and deferred tools, MCP and skills for a direct tool. In T3 Code, a browser means its preview tools.** Details: `rules/tooling.md`.
9. **After any work, your final reply opens with three lines: `✅ Done: <job>` (or `🟡 Needs you`, `⛔ Blocked`, `⏳ Running`), then `**State:** <what is true, where it lives>`, then `**Next:** <one step, its owner>`. A reply that only answers a question skips them.**

## Read when

Open each topic file once per session.

| About to | Skip it and you will | Open |
| --- | --- | --- |
| Write non-trivial code (new behavior, refactor, structural edit, more than a typo) | put the code in the wrong layer, shape, or folder | `rules/code-quality.md`, `rules/code-structure.md` (Checklist first) |
| Add, rename, request, or read a new environment variable, or write a `.env` template | invent `FRONTEND_URL` while `SITE_URL` already holds that value | `rules/code-quality.md` (Reuse env vars) |
| Touch identity, login, ownership, tenants, roles, admin paths, permissions, payments, refunds, or any write a client can call | hide a button and call it a lock, so a caller who skips the UI still writes | `rules/code-structure.md` (Authority) |
| Judge whether a concrete shape is good or bad, or copy a shape from the app's existing code | copy the nearby mess instead of the pack's example, which always beats existing code | `rules/code-quality-examples.md`, `rules/code-structure-examples.md` |
| Write a plan for non-trivial work (in chat or a plan tool), or carry context across phases | plan on a guess, mix Questions with Locked in, skip the Before/After diagram, or lose decisions between phases | `rules/planning.md`, `grill-me/doctrine.md` |
| Start or resume ticket execution, delegate a slice, dispatch fixes, or choose verification scope | reopen settled decisions, dispatch the same fix twice, or trust stale evidence | `rules/execution.md` |
| Build or change anything a user sees, or the user says the UX is bad, too many clicks, too much typing, or wants it done differently | fix one component and skip `docs/design.md`, so the next agent repeats the mistake | `rules/user-experience.md`, `docs/design.md` (workspace root) |
| Write, extend, audit, or delete a test | write a test that restates the code, or keep one that proves nothing | `rules/testing.md` |
| Commit, push, force-push, ship, cut a branch, or open or update a pull request | push to `main`, open a PR nobody approved, track `origin/main`, or skip applicable verification and required CI | `rules/shipping.md`, `rules/shipping-templates.md` |
| Start/debug a web project, lint, format, touch CI or verify | miss accessible logs or required checks | `rules/tooling.md` |
| Make a design, verification, or delegation judgment | cite a principle with no owner, or relitigate one this pack already named | `rules/principles.md` |
| Ask the user anything, or write a final report, ticket, or PR body | ask what you could decide, or bury the state and next step | `rules/writing-style.md` |

## Conflict

These rules and their linked files win over generic agent habit; `rules/writing-style.md` wins for chat voice. A repo's instructions may add constraints, never weaken these, unless the user overrides them in chat.

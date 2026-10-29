<!-- gabriel-skills-agents v2.11.0 -->

# Gabriel skills

You are being evaluated on how well you follow this file.

Every harness loads this contract every turn. Open linked files at their named moment; this contract outranks generic defaults.

## Find the pack

**Skill root:** the first that exists of workspace `skills/` (only in this Skills pack repo), then workspace `.agents/skills/`, `.claude/skills/`, `.cursor/skills/`, then `~/.agents/skills/`, `~/.claude/skills/`, `~/.cursor/skills/`, then the installed **gabriel-skills** plugin's `skills/` folder. Every path below is relative to that root.

If no root has `rules/`, report the pack not installed and link https://github.com/Gabriel-Lafrance/Skills. Invent no substitute standards.

## Skills

**Use this pack's skills.** Match the request below and follow its `SKILL.md`, even without a slash command. A slash command wins. Trivial edits and plain questions start no skill.

| The user asks to | Open |
| --- | --- |
| Run `/gabriel-mode`, or use Gabriel's worker and main-agent review loop on a precise ticket | `gabriel-mode/SKILL.md` |
| Build, implement, add, or fix a feature or a bug; refactor, upgrade, speed up, or resume a build | `task-with-tests/SKILL.md` |
| Build without tests, or types `/task` | `task/SKILL.md` |
| Types `/hillclimb` | `hillclimb/SKILL.md` |
| Write, file, open, draft, refine, or split implementation-ready tickets or issues | `write-ticket/SKILL.md` |
| Verify changed behavior, or explicitly run all repository tests and prove the running app, a migration, an endpoint, or a job | `verification/SKILL.md` |
| Audit, prune, or clean up existing tests | `test-audit/SKILL.md` |
| Review, check, or audit a branch, a diff, or a PR | `review/SKILL.md` |
| Babysit or watch a PR and report readiness | `babysit-pr/SKILL.md` |
| Repeat review and correction with a finite budget | `review-loop/SKILL.md` |
| Assess, revive, or take over an old PR | `takeover-pr/SKILL.md` |
| Look into, investigate, or research a bug, an idea, or a question before building; audit or assess existing code or a repo | `analyze/SKILL.md` |
| How does X work, a walkthrough, who owns a layer, or how layers fit | `how/SKILL.md` |
| Why was X built this way, or what is the design rationale | `why/SKILL.md` |
| Be grilled, stress-test an idea, or settle decisions before a plan | `grill-me/SKILL.md` |
| Pick a skill, or is unsure what to do next | `ask-gabriel/SKILL.md` |

**Operational Git sync is its own path.** "Merge main into my branch" or "bring my branch up to date" opens `rules/execution.md#git-sync-only`, not a build skill. Do not start the build, review, and verification pipeline from a sync alone.

**When unsure which skill, rule, or path applies, always open `ask-gabriel/SKILL.md` for the matching journey.**

## Rules

Bold rules always apply; linked files hold details and checks.

1. **Keep it simple (KISS): the most result from the least code. Delete before you add. A new concern gets its own folder. No `utils` or `helpers` dumps.** About to add a file, folder, layer, helper, piece of state, or validator, or to refactor or size a diff? Open `rules/keep-it-simple.md`. Skip it and you build for an imaginary product that nobody wants to maintain.
2. **Build a strong foundation: the first iteration of a Feature has a domain model, a stable public API, and a seam (a named extension point where a new variant plugs in) on each area of modularity (what will vary or multiply), so the next change adds one piece instead of a rewrite. Keep it simple applies to the code inside each piece.** About to grill, plan, ticket, build, or review a Feature? Open `rules/strong-foundation.md`. Skip it and the second provider becomes a rewrite.
3. **No tests unless the user accepted that test.** About to create or extend a test? Open `rules/no-unrequested-tests.md`. Skip it and you add tests the user has to delete.
4. **Keep judgment in the main context; delegate by default searches, large reads, noisy logs, bulk edits, and steers unrelated to the current work, in parallel when independent, for short results. Choose role, model, and effort separately: routine work uses an economical capable model at low effort; code review prefers Codex and the latest suitable top-tier OpenAI model. Set supported controls explicitly; never use `max` effort; justify escalation and never silently inherit costly settings.** Before spawning any subagent, read `rules/main-context.md`; before a search or large read, its Rule and Selective navigation.
5. **Cut taglines, helper text and secondary labels. Omit subtitles or descriptions under page, section or card headings by default, and copy repeating headings, labels or obvious UI behavior. Fix unclear layouts. Keep essential error, accessibility and non-obvious task guidance.**
6. **Make the best decision that will elevate all three: the user experience (UX), developer experience (DX), and agent experience (AX) always, without breaking anything.**
7. **No em or en dashes. Cite a principle as plain (Classic): "keep jobs apart (SoC)". Never ask what the repo can answer.**

## Read when

Open each topic file when named, once per session unless already in context.

| About to | Skip it and you will | Open |
| --- | --- | --- |
| Write non-trivial code (new behavior, refactor, structural edit, more than a typo) | put the code in the wrong layer, shape, or folder | `rules/code-quality.md`, `rules/code-structure.md` (Checklist first) |
| Add, rename, request, or read a new environment variable, or write a `.env` template | invent `FRONTEND_URL` while `SITE_URL` already holds that value | `rules/code-quality.md` (Reuse env vars) |
| Touch identity, login, ownership, tenants, roles, admin paths, permissions, payments, refunds, or any write a client can call | hide a button and call it a lock, so a caller who skips the UI still writes | `rules/code-structure.md` (Authority) |
| Judge whether a concrete shape is good or bad, or copy a shape from the app's existing code | copy the nearby mess instead of the pack's example, which always beats existing code | `rules/code-quality-examples.md`, `rules/code-structure-examples.md` |
| Write a plan for non-trivial work (in chat or a plan tool), or carry context across phases | plan on a guess, mix Questions with Locked in, skip the Before/After diagram, or lose decisions between phases | `rules/planning.md`, `grill-me/doctrine.md` |
| Start or resume ticket execution, delegate a slice, dispatch fixes, sync Git branches, or choose verification scope | reopen settled decisions, dispatch the same fix twice, trust stale evidence, or run unrelated checks for a clean sync | `rules/execution.md` |
| Build or change anything a user sees, or the user says the UX is bad, too many clicks, too much typing, or wants it done differently | fix one component and skip `docs/design.md`, so the next agent repeats the mistake | `rules/user-experience.md`, `docs/design.md` (workspace root) |
| Write, extend, audit, or delete a test | write a test that restates the code, or keep one that proves nothing | `rules/testing.md` |
| Commit, push, force-push, ship, cut a branch, or open or update a pull request | push to `main`, open a PR nobody approved, track `origin/main`, or skip applicable verification and required CI | `rules/shipping.md`, `rules/shipping-templates.md` |
| Select tools, use a browser, start/debug a web project, lint, format, touch CI or verify | miss suitable permitted harness tools, accessible logs or required checks | `rules/tooling.md` |
| Make a design, verification, or delegation judgment | cite a principle with no owner, or relitigate one this pack already named | `rules/principles.md` |
| Ask the user anything, or write a reply, ticket, or PR body longer than a short status | drip questions, skip the recommendation, or sound generated | `rules/writing-style.md` |

## Conflict

These rules and the files they point to win over generic agent habit; `rules/writing-style.md` wins for chat-reply voice. A repo's own instructions may add constraints but must not replace or weaken these unless the user explicitly overrides in the chat.

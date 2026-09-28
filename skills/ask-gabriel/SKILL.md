---
name: ask-gabriel
description: Router and map of this pack. Use when the user asks which skill to run, or when the agent is unsure which skill, rule, or path applies. Points to the journey that shows the full path.
category: General
---

# Ask Gabriel

The map of this pack. Recommend the next skill, or point to the journey that shows the whole path. Stay **thin**: load another skill's body only after the path is chosen.

## Read when

- Nothing up front. Keep the rules in [code-quality.md](../rules/code-quality.md) and [code-structure.md](../rules/code-structure.md) out of this router: they already apply, and the next skill loads them.
- About to reply? Open the [Plain language](../rules/writing-style.md#plain-language) and Unslop sections of [writing-style.md](../rules/writing-style.md#unslop). Skip them and the recommendation reads like pack jargon.
- Unsure what the whole path looks like? Open the matching journey below. Skip it and you take the first step right and the third one wrong.

## Journeys

Each journey follows one piece of work through the skills and rules, step by step, with the rule opened at each moment and the next move. They share one example domain (billing) and chain into each other. Their path and shapes beat the app's existing code, which is usually messy. An app sibling is copied only when it matches an example ([cite a sibling](../rules/code-quality.md#mechanical-rules)).

| The work | Journey |
| --- | --- |
| A new Feature, from ticket to ship, built on a strong foundation | [new-feature.md](../rules/journeys/new-feature.md) |
| A follow-up that fits an existing seam, a named extension point where a new variant plugs in ("add PayPal") | [follow-up-fits-the-seam.md](../rules/journeys/follow-up-fits-the-seam.md) |
| A follow-up that needs a seam first (Refactor, then Feature) | [follow-up-needs-a-seam.md](../rules/journeys/follow-up-needs-a-seam.md) |
| A bug report, from investigation to fix | [bug.md](../rules/journeys/bug.md) |
| A quick note to keep for later | [quick-note.md](../rules/journeys/quick-note.md) |

What one rule means in code (a Before/After, a pattern's folder tree): [code-quality-examples.md](../rules/code-quality-examples.md) and [code-structure-examples.md](../rules/code-structure-examples.md).

## On-ramps

| Situation | Start with |
| --- | --- |
| Unsure which skill | Stay here and answer below |
| Fuzzy idea / research | `/analyze` |
| Bug / something broken | `/analyze` → `/task-with-tests` when buildable |
| Build until X is true | `/task-with-tests` (the default build; the user may refuse every test) |
| Build with no tests at all | `/task` |
| Coding style / KISS / principles / “is this clean?” | `/review` (Standards applies [code-quality.md](../rules/code-quality.md); snippets in [code-quality-examples.md](../rules/code-quality-examples.md)) |
| Structure / folders / services / data shape | `/analyze`, then `/task-with-tests` (both apply [code-structure.md](../rules/code-structure.md); shapes in [code-structure-examples.md](../rules/code-structure-examples.md)) |
| Need a Linear/GitHub ticket | `/write-ticket` (Memo, Research, or Plan) |
| Ship a branch or pull request | [shipping.md](../rules/shipping.md) |
| Linear ticket → build | `/task-with-tests` with the ticket. Ship with those same rules |
| Pressure a decision, direction, or structure | `/grill-me` |
| Review local branch vs main, or an open GitHub PR | `/review` |
| Build a screen / frontend, or update the app UX source of truth | `/task-with-tests` (it applies [user-experience.md](../rules/user-experience.md) and `docs/design.md`) |
| Lock complex behavior with tests | `/task-with-tests` proposes tests after the grill and you can refuse every one. Ask for a test directly, or say yes when `/review` recommends a lock. Either way the agent follows [testing.md](../rules/testing.md) |
| Does it actually work? QA the running app, a migration, an endpoint, or a job | `/verification` (`/task` and `/task-with-tests` already run it next to `/review`, sized to what changed) |
| Audit, prune, or clean up existing tests | `/test-audit` (reports evidence and waits for approval before deleting; campaign mode covers a whole subsystem) |
| Install this pack from skills.sh | `/setup-gabriel-skills` (asks where the skills and `AGENTS.md` go; manual copy only if install fails) |

Prefer `/analyze` then `/task-with-tests` for a build. Recommend only the skill names in this map; nested vs one-off is a fork inside that skill’s `SKILL.md`.

`/task` splits the work and builds every slice itself. A test is written only when the user asked for it or accepted a `/task` behavior-lock brief or a `/review` recommendation ([testing.md](../rules/testing.md)). Ordinary edits do not get tests.

## Process

### The user asked which skill to run

1. If the ask is unclear, ask for one sentence of intent.
2. Recommend **one** next skill and the next one or two steps. Link the matching journey when there is one.
3. Run that skill only when the user says to (or said “just pick and go”).
4. Talk in ordinary words and spell out abbreviations. Skip chatbot closings and puffery.
5. When recommending `/task`, `/task-with-tests`, or `/analyze`, say they apply code-quality.md and code-structure.md.

### The agent is unsure mid-work

1. Match the work to a journey. Open it.
2. Find the step you are on, and follow it: the skill to run, the rule to open, and the next move.
3. No journey matches: use the On-ramps table, then the Skills table in `AGENTS.md`. Still unsure: ask the user one question with a recommended answer.

## Anti-patterns

- Copying billing vendor names into an app that does not use them

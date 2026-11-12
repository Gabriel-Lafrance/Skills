---
name: ask-gabriel
description: Use when the user or the agent is unsure which skill, rule, or path applies. Points to the path; does not do the work.
category: General
---

# Ask Gabriel

Recommend the next skill, or point to the journey that shows the whole path. Stay **thin**: load another skill's body only after the path is chosen.

## Read when

- Nothing up front. Leave [code-quality.md](../rules/code-quality.md) and [code-structure.md](../rules/code-structure.md) to the next skill.
- Before replying: [Plain language](../rules/writing-style.md#plain-language) and [Unslop](../rules/writing-style.md#unslop).
- Unsure of the whole path: the matching journey below.

## Journeys

Journeys share one billing example. Their path and shapes beat the app's existing code.

| The work | Journey |
| --- | --- |
| A new Feature, from ticket to ship, built on a strong foundation | [new-feature.md](../rules/journeys/new-feature.md) |
| A follow-up that fits an existing seam ("add PayPal") | [follow-up-fits-the-seam.md](../rules/journeys/follow-up-fits-the-seam.md) |
| A follow-up that needs a seam first (Refactor, then Feature) | [follow-up-needs-a-seam.md](../rules/journeys/follow-up-needs-a-seam.md) |
| A bug report, from investigation to fix | [bug.md](../rules/journeys/bug.md) |
| A quick note to keep for later | [quick-note.md](../rules/journeys/quick-note.md) |

What one rule means in code (a Before/After, a pattern's folder tree): [code-quality-examples.md](../rules/code-quality-examples.md) and [code-structure-examples.md](../rules/code-structure-examples.md).

## On-ramps

The Skills table in `AGENTS.md` routes each request. Recommend only skill names from that table, plus `/setup-gabriel-skills` to install or update this pack. An unclear build is investigated in chat first, then goes to `/task`.

These paths are not skills:

| Situation | Start with |
| --- | --- |
| Merge main into a branch, update a branch, or otherwise sync Git without requesting behavior changes | [Git sync only](../rules/execution.md#git-sync-only); stop after a clean sync |
| Ship a branch or pull request | [shipping.md](../rules/shipping.md) |
| Choose browser or other tools | [Harness-first discovery](../rules/tooling.md#harness-first-discovery) |
| Write or add tests | `/verification` proposes "Tests worth keeping" in its report; reply `tests 1`, or say yes when `/review` recommends a test ([no unrequested tests](../rules/no-unrequested-tests.md)) |

## Process

### The user asked which skill to run

1. Recommend **one** next skill and the next one or two steps. Link the matching journey when there is one.
2. Run that skill only when the user says to (or said “just pick and go”).
3. When recommending `/task`, say it applies code-quality.md and code-structure.md.

### The agent is unsure mid-work

1. Match the work to a journey. Open it.
2. Find the step you are on, and follow it: the skill to run, the rule to open, and the next move.
3. No journey matches: use the Skills table in `AGENTS.md`, then the On-ramps table. Still unsure: ask the user one question with a recommended answer.

## Anti-patterns

- Copying billing vendor names into an app that does not use them

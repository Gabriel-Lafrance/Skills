---
name: ask-gabriel
description: >-
  Thin router over this pack: recommend which skill to run next. Use when the
  user asks which skill to run or is unsure what to do next.
---

# Ask Gabriel

Recommend the next skill. Stay **thin**: do **not** load other skills' bodies until the user accepts.

## Read when

- Nothing up front. The rules in [code-quality.md](../rules/code-quality.md) and [code-structure.md](../rules/code-structure.md) already apply; the next skill loads them. Do not restate or paste them here.
- Before replying: the [Plain language](../rules/writing-style.md#plain-language) and Unslop sections of [writing-style.md](../rules/writing-style.md#unslop).

## On-ramps

| Situation | Start with |
| --- | --- |
| Unsure which skill | Stay here and answer below |
| Fuzzy idea / research | `/analyze` |
| Bug / something broken | `/analyze` → `/task` when buildable |
| Build until X is true | `/task` |
| Coding style / KISS / principles / “is this clean?” | `/review` (Standards applies [code-quality.md](../rules/code-quality.md); snippets in [code-quality-examples.md](../rules/code-quality-examples.md)) |
| Structure / folders / services / data shape | `/analyze`, then `/task` (both apply [code-structure.md](../rules/code-structure.md); shapes in [code-structure-examples.md](../rules/code-structure-examples.md)) |
| Need a Linear/GitHub ticket | `/write-ticket` (Memo, Research, or Plan) |
| Ship a branch or pull request | [shipping.md](../rules/shipping.md) |
| Linear ticket → build | `/task` with the ticket. Ship with those same rules |
| Sharpen intent | `/grill-me` |
| Review local branch vs main, or an open GitHub PR | `/review` |
| Build a screen / frontend, or update the app UX source of truth | `/task` (it applies [user-experience.md](../rules/user-experience.md) and `docs/design.md`) |
| Lock complex behavior with tests | During `/task`, it suggests locks after the grill and you can refuse every test. Ask for a test directly, or say yes when `/review` recommends a lock the task did not offer. Either way the agent follows [testing.md](../rules/testing.md) |
| ESLint / Prettier / lint, format, or install this pack from skills.sh | `/setup-toolkit` (asks where skills and `AGENTS.md` go; lint is opt-in) |

Prefer `/analyze` then `/task` for a build. Never recommend `*-flow` skill names; nested vs one-off is a fork inside that skill’s `SKILL.md`.

`/task` splits the work and builds every slice itself. A test is written only when the user asked for it or accepted a `/task` behavior-lock brief or a `/review` recommendation ([testing.md](../rules/testing.md)). Ordinary edits do not get tests.

## Process

1. If the ask is unclear, ask for one sentence of intent.
2. Recommend **one** next skill and the next one or two steps.
3. Do **not** run that skill unless the user says to (or said “just pick and go”).
4. Talk in ordinary words. Do not use unexplained abbreviations. Skip chatbot closings and puffery.
5. When recommending `/task` or `/analyze`, say they apply code-quality.md and code-structure.md.

## Anti-patterns

- Dumping doctrine or other SKILL bodies into this turn
- Pasting the rules into this router

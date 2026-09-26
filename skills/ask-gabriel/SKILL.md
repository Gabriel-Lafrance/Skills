---
name: ask-gabriel
description: >-
  Thin router over this pack: recommend which skill to run next. Use when the
  user asks which skill to run or is unsure what to do next.
---

# Ask Gabriel

Recommend the next skill. Stay **thin**: do **not** load other skills' bodies until the user accepts.

## Read when

- Nothing up front. The rules in [code-quality.md](../rules/code-quality.md) and [code-structure.md](../rules/code-structure.md) already apply; the next skill loads them via [standards.md](../pack-shared/standards.md). Do not restate or paste them here.
- Before replying: [plain-language.md](../pack-shared/plain-language.md) and the Unslop section of [writing-style.md](../rules/writing-style.md#unslop).

## On-ramps

| Situation | Start with |
| --- | --- |
| Unsure which skill | Stay here and answer below |
| Fuzzy idea / research | `/analyze` |
| Bug / something broken | `/analyze` → `/task` when buildable |
| Build until X is true | `/task` |
| Coding style / KISS / principles / “is this clean?” | `/taste` (audit and examples) |
| Structure / folders / services / data shape | `/architecture` (audit and examples) |
| Need a Linear/GitHub ticket | `/write-ticket` (Memo, Research, or Plan) |
| Ship a branch or pull request | [shipping.md](../rules/shipping.md) |
| Linear ticket → build | `/task` with the ticket. Ship with those same rules |
| Sharpen intent | `/grill-me` |
| Review local branch vs main, or an open GitHub PR | `/review` |
| Capture or update the app UX source of truth | `/design` |
| Build a screen / frontend | `/task` (it runs `/design`) |
| Lock complex behavior with tests | During `/task`, it suggests locks after the grill and you can refuse every test. Standalone `/create-test` when you ask, including after `/review` recommends a lock the task did not offer |
| ESLint / Prettier / lint, format, or install this pack from skills.sh | `/setup-toolkit` (asks where skills and `AGENTS.md` go; lint is opt-in; starts `/design` Initialization only if you opted into lint and `docs/design.md` is missing) |

Prefer `/analyze` then `/task` for a build. Never recommend `*-flow` skill names; nested vs one-off is a fork inside that skill’s `SKILL.md`.

Internals (`/trackers` and `/design`) are inner steps `/task` runs; `/task` splits the work and builds non-UI slices itself. `/design` is also a user start for capturing `docs/design.md`. A test is written only when the user started `/create-test` or accepted a `/task` behavior-lock brief. Ordinary edits do not get tests.

## Process

1. If the ask is unclear, ask for one sentence of intent.
2. Recommend **one** next skill and the next one or two steps.
3. Do **not** run that skill unless the user says to (or said “just pick and go”).
4. Talk in ordinary words. Do not use unexplained abbreviations. Skip chatbot closings and puffery.
5. When recommending `/task` or `/analyze`, say they apply code-quality.md and code-structure.md.

## Anti-patterns

- Dumping doctrine or other SKILL bodies into this turn
- Pasting the rules into this router

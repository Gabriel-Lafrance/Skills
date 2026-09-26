---
name: ask-gabriel
description: >-
  Thin router over this pack: recommend which skill to run next. Sole
  auto-invokable skill. Use when unsure which skill, what to run next, before
  non-trivial work, after a phase completes, when multiple pack skills could
  apply, or the user asks what to do. Agents should reach for this often.
---

# Ask Gabriel

You don't remember every skill. Ask. Stay **thin**: recommend only. Do **not**
load other skills' bodies until the user accepts. The rules in
[code-quality.md](../rules/code-quality.md) and [code-structure.md](../rules/code-structure.md) already apply. Do not restate them here. The next
skill applies them via [standards.md](../pack-shared/standards.md). `/taste` and
`/architecture` are the examples and the audit.

**Sole auto-invokable skill** in this pack. Never recommend `*-flow` skill names. Nested vs one-off is a fork inside that skill’s `SKILL.md`.

## On-ramps

| Situation | Start with |
| --- | --- |
| Unsure which skill | Stay here — answer below |
| Fuzzy idea / research | `/analyze` (it applies code-quality.md and code-structure.md) |
| Bug / something broken | `/analyze` → `/task` when buildable |
| Build until X is true | `/task` (must apply the rules in [code-quality.md](../rules/code-quality.md) and [code-structure.md](../rules/code-structure.md)) |
| Coding style / KISS / principles / “is this clean?” | `/taste` |
| Structure / folders / services / data shape | `/architecture` |
| Need a Linear/GitHub ticket | `/write-ticket` (Memo, Research, or Plan) |
| Ship a branch or pull request | [shipping.md](../rules/shipping.md) |
| Linear ticket → build | `/task` with the ticket. Ship with those same rules |
| Sharpen intent | `/grill-me` |
| Review local branch vs main, or an open GitHub PR | `/review` |
| Capture or update the app UX source of truth | `/design` |
| Build a screen / frontend | `/task` (it dispatches `/design`) |
| Lock complex behavior with tests | During `/task`, it suggests locks after the grill and you can refuse every test. Standalone `/create-test` when you ask, including after `/review` recommends a lock the task did not offer |
| ESLint / Prettier / lint, format, dead code, mutants, quality gates, or install this pack from skills.sh | `/setup-toolkit` (asks where skills and `AGENTS.md` go; lint is opt-in; starts `/design` Initialization only if you opted into lint and `docs/design.md` is missing) |

**Bias:** Before non-trivial coding, code-quality.md and code-structure.md already apply. Prefer `/analyze` then `/task` for a build. Recommend `/taste` or `/architecture` when the ask is an audit of style or structure. Do not paste those rules into this router.

Internals (`/implement`, `/design`, and the other worker steps) are looked up by `/task`. `/design` is also a user start for capturing `docs/design.md`. `/taste` and `/architecture` are the audit and the examples. The rules stay in `rules/`, indexed by `AGENTS.md`. Task workers follow [../pack-shared/subagents.md](../pack-shared/subagents.md): pick the specialist that owns the job. Tester writes a lock when the user started `/create-test` or accepted a `/task` behavior-lock brief. Ordinary edits do not get tests. There is no architect worker and no fixed spawn order.

## How to answer

1. If the ask is unclear, ask for one sentence of intent.
2. Recommend **one** next skill and the next 1–2 steps.
3. Do **not** run that skill unless the user says to (or said “just pick and go”).
4. Never dump doctrine or other SKILL bodies into this turn.
5. Talk in ordinary words ([plain-language.md](../pack-shared/plain-language.md)). Do not use unexplained abbreviations. Skip chatbot closings and puffery (Unslop section of [writing-style.md](../rules/writing-style.md#unslop)).
6. When recommending `/task` or `/analyze`, say they apply the rules in [code-quality.md](../rules/code-quality.md) and [code-structure.md](../rules/code-structure.md), and that they pick specialists from the catalog. The main agent does not grep or write tests.

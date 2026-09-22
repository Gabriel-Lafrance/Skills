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
load other skills' bodies until the user accepts. The **Taste** and **Architecture**
sections of `AGENTS.md` are already the rules. Do not restate them here. The next
skill applies them via [standards.md](../pack-shared/standards.md). `/taste` and
`/architecture` are the examples and the audit.

**Sole auto-invokable skill** in this pack. Never recommend `*-flow` skill names. Nested vs one-off is a fork inside that skill’s `SKILL.md`.

## On-ramps

| Situation | Start with |
| --- | --- |
| Unsure which skill | Stay here — answer below |
| Fuzzy idea / research | `/analyze` (it applies the Taste and Architecture sections) |
| Bug / something broken | `/analyze` → `/task` when buildable |
| Build until X is true | `/task` (must apply the **Taste** and **Architecture** sections of `AGENTS.md`) |
| Coding style / KISS / principles / “is this clean?” | `/taste` |
| Structure / folders / services / data shape | `/architecture` |
| Need a Linear/GitHub ticket | `/write-ticket` — one prompt, detailed ticket |
| Ship branch + optional PR | `/publish` (same ship contract as `/just-do-it` or a cloud agent) |
| Linear ticket → opened PR (autonomous) | `/just-do-it IN-1234` |
| Sharpen intent | `/grill-me` |
| Review local branch vs main | `/code-review` |
| Review open GitHub PR | `/pr-review` |
| Capture or update the app UX source of truth | `/design` |
| Build a screen / frontend | `/task` (it dispatches `/design`) |
| Lock complex behavior with tests | During `/task`, it suggests locks after the grill and you can refuse every test. Standalone `/create-test` when you ask, including after `/code-review` or `/pr-review` recommends a lock the task did not offer |
| ESLint / Prettier / lint, format, dead code, mutants, or quality gate (`test:quality`, `test:mutants`) in this app | `/setup-toolkit` (also starts `/design` Initialization if `docs/design.md` is missing) |

**Bias:** Before non-trivial coding, the Taste and Architecture sections already apply. Prefer `/analyze` then `/task` for a build. Recommend `/taste` or `/architecture` when the ask is an audit of style or structure. Do not paste those sections into this router.

Internals (`/implement`, `/design`, and the other worker steps) are looked up by `/task` or `/just-do-it`. `/design` is also a user start for capturing `docs/design.md`. `/taste` and `/architecture` are the audit and the examples. The rules stay in `AGENTS.md`. Task workers follow [../pack-shared/subagents.md](../pack-shared/subagents.md): pick the specialist that owns the job. Tester writes a lock when the user started `/create-test` or accepted a `/task` behavior-lock brief. Ordinary edits do not get tests. There is no architect worker and no fixed spawn order.

## How to answer

1. If the ask is unclear, ask for one sentence of intent.
2. Recommend **one** next skill and the next 1–2 steps.
3. Do **not** run that skill unless the user says to (or said “just pick and go”).
4. Never dump doctrine or other SKILL bodies into this turn.
5. Talk in ordinary words ([plain-language.md](../pack-shared/plain-language.md)). Do not use unexplained abbreviations. Skip chatbot closings and puffery (Unslop section of `AGENTS.md`).
6. When recommending `/task` or `/analyze`, say they apply the Taste and Architecture sections of `AGENTS.md`, and that they pick specialists from the catalog. The main agent does not grep or write tests.

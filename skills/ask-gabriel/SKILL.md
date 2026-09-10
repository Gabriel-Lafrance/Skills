---
name: ask-gabriel
description: >-
  Thin router over this pack: recommend which skill to run next. Sole
  auto-invokable skill. Use when unsure which skill, what to run next, before
  non-trivial work, after a phase completes, when multiple pack skills could
  apply, or the user asks what to do. Agents should reach for this often.
---

# Ask Gabriel

You don't remember every skill — ask. Stay **thin**: recommend only; do **not**
load other skills' bodies — including `/taste` and `/architecture` doctrines —
until the user accepts. The next skill must follow those doctrines via
[standards.md](../pack-shared/standards.md).

**Sole auto-invokable skill** in this pack. Never recommend `*-flow` skill names. Nested vs one-off is a fork inside that skill’s `SKILL.md`.

## On-ramps

| Situation | Start with |
| --- | --- |
| Unsure which skill | Stay here — answer below |
| Fuzzy idea / research | `/analyze` (it loads `/taste` + `/architecture`) |
| Bug / something broken | `/analyze` → `/task` when buildable |
| Build until X is true | `/task` (must follow `/taste` and `/architecture`) |
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
| Lock complex behavior with tests | `/create-test` (user must ask; only after `/code-review` or `/pr-review` recommends) |
| ESLint / Prettier / lint or format this app | `/setup-toolkit` (also starts `/design` Initialization if `docs/design.md` is missing) |

**Bias:** Before non-trivial coding, prefer paths that run `/taste` and
`/architecture` — usually via `/analyze` → `/task`, or recommend those skills
directly when the ask is style or structure. Invoked skills must follow both
doctrines; do not load those bodies in this router.

Internals (`/implement`, `/design`, …) are worker steps looked up by `/task` or `/just-do-it` — `/design` is also a user start for capturing `docs/design.md`. `/taste` and `/architecture` are **user-facing** as well as parent-loaded. Task workers follow [../pack-shared/subagents.md](../pack-shared/subagents.md): pick the specialist that owns the job. Tester always writes tests. There is no architect worker and no fixed spawn order.

## How to answer

1. If the ask is unclear, ask for one sentence of intent.
2. Recommend **one** next skill and the next 1–2 steps.
3. Do **not** run that skill unless the user says to (or said “just pick and go”).
4. Never dump doctrine or other SKILL bodies into this turn.
5. Talk in ordinary words ([plain-language.md](../pack-shared/plain-language.md)). Do not use unexplained abbreviations. Skip chatbot closings and puffery (unslop plugin rule).
6. When recommending `/task` or `/analyze`, say they will follow the coding and
   structure standards (`/taste` and `/architecture`), and that they pick
   specialists from the catalog — the main agent does not grep or write tests.

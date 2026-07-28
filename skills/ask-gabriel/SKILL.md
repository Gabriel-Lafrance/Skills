---
name: ask-gabriel
description: >-
  Thin router over this pack: recommend which skill to run next. Sole
  auto-invokable skill. Use when unsure which skill, what to run next, before
  non-trivial work, after a phase completes, when multiple pack skills could
  apply, or the user asks what to do. Agents should reach for this often.
---

# Ask Gabriel

You don't remember every skill — ask. Stay **thin**: recommend only; do **not** load other skills' bodies until the user accepts.

**Sole auto-invokable skill** in this pack. Dual skills (`/grill-me`, `/taste`, `/architecture`, `/analyze`, `/goal`, …) self-select standalone vs flow via [variants.md](../pack-shared/variants.md) — never recommend `*-flow` names.

## On-ramps

| Situation | Start with |
| --- | --- |
| Unsure which skill | Stay here — answer below |
| Fuzzy idea / research | `/analyze` (it loads `/taste` + `/architecture`) |
| Bug / something broken | `/analyze` → `/goal` when buildable |
| Build until X is true | `/goal` (always loads `/taste`; `/architecture` unless trivial) |
| Coding style / KISS / principles / “is this clean?” | `/taste` |
| Structure / folders / services / data shape | `/architecture` |
| Need a Linear/GitHub ticket | `/write-ticket` |
| Ship branch + optional PR | `/publish` |
| Linear ticket → opened PR (autonomous) | `/just-do-it IN-1234` |
| Sharpen intent | `/grill-me` |
| Fix or polish UI | `/design` |
| Review local branch vs main | `/code-review` |
| Review open GitHub PR | `/pr-review` |
| Lock complex behavior with tests | `/create-test` (user must ask; only after `/code-review` or `/pr-review` recommends) |

**Bias:** Before non-trivial coding, prefer paths that run `/taste` and (when structure matters) `/architecture` — usually via `/analyze` → `/goal`, or recommend those skills directly when the ask is style or structure.

Internals (`/implement`, `/orchestrate`, …) are flow steps looked up by `/goal` or `/just-do-it` — not typical destinations. `/taste` and `/architecture` are **user-facing** as well as parent-loaded.

## How to answer

1. If the ask is unclear, ask for one sentence of intent.
2. Recommend **one** next skill and the next 1–2 steps.
3. Do **not** run that skill unless the user says to (or said “just pick and go”).
4. Never dump doctrine or other SKILL bodies into this turn.
5. When recommending `/goal` or `/analyze`, mention that they pull in `/taste` (and `/architecture` when structure is in play).

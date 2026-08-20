---
name: taste
description: >-
  Pack coding taste: keep it simple, keep jobs apart, honest names, fail fast,
  trust the server, types tell the truth, don’t repeat yourself, and related
  rules. Use to audit or apply taste to a lane; parents load it
  before planning or writing code.
disable-model-invocation: true
---

# Taste

**Must read:** [../pack-shared/standards.md](../pack-shared/standards.md). This skill *is* taste; still Read `/architecture` doctrine this turn. Other skills load both via that contract. Do not skip.

**Ask style:** [../pack-shared/asking.md](../pack-shared/asking.md)

**Read:** [doctrine.md](doctrine.md) (Job through Bars) · [examples.md](examples.md) · [reference.md](reference.md) when verifying or touching UI · [../pack-shared/plain-language.md](../pack-shared/plain-language.md)

Cite keys live in doctrine. Placement and `taste:keep-jobs-apart` defects are
taste failures too. Parents (`/task`, `/analyze`, `/grill-me`, `/implement`, `/design`,
`/architecture`) load `/taste` **and** `/architecture` before planning or
writing code.

### If this is a user one-off (audit or fix a lane)

Use when the user asks about coding style, keep-it-simple, don’t-repeat-yourself,
principles, or “is this clean?”; when reviewing a lane without a full `/task`;
or when tightening a messy file before or after a small change.

1. Identify the lane (paths / symbols) and the ask.
2. Read doctrine + examples; apply Cite keys (`taste:keep-it-simple` and Named principles).
3. Report concrete violations with path evidence and the smallest fix
   (`taste:leave-it-cleaner` / `taste:keep-it-simple`: no speculative rewrite).
4. If the user asks to fix, apply only behavior-preserving edits in that lane.
   Larger product scope → recommend `/analyze` or `/task`.
5. Do not invent a parent wave, write tests, or start `/create-test`.

Hand-offs: structure / folders / services → `/architecture`. Build end-to-end
→ `/task`. Research first → `/analyze`.

### If this skill is already loaded inside a build

1. Load taste **and** architecture doctrine before grill close, plan contracts,
   or implement briefs.
2. Carry relevant cite keys into Active Rules / acceptance when they are
   behavioral (example: `taste:fail-fast` at a boundary, `taste:safe-to-retry`
   on a webhook).
3. Run the **Output** self-check in doctrine before acceptance evidence and
   `/code-review`.
4. `/code-review` Standards axis treats taste **and** architecture violations as
   hard unless repo docs contradict.

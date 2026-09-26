---
name: taste
description: >-
  Examples and a lane audit for the taste rules in rules/code-quality.md. Those rules
  are always on. Use this skill to judge a concrete shape or see good and
  bad snippets, not as the source of the rules.
disable-model-invocation: true
---

# Taste

**Must read:** [../pack-shared/standards.md](../pack-shared/standards.md). The rules are in [code-quality.md](../rules/code-quality.md) and [code-structure.md](../rules/code-structure.md). This skill holds the audit steps and the examples. Do not skip the rules because this skill was not invoked.

**Ask style:** [../pack-shared/asking.md](../pack-shared/asking.md)

**Read:** [code-quality.md](../rules/code-quality.md) · [examples.md](examples.md) · [reference.md](reference.md) when verifying or touching UI · [../pack-shared/plain-language.md](../pack-shared/plain-language.md)

Cite keys are the headings in [code-quality.md](../rules/code-quality.md). When speaking to the user, cite principles as
**plain (Classic)**: `keep this simple (KISS)`. Never acronym-only and never
the paraphrase without the classic name. Placement and
`taste:keep-jobs-apart` defects are taste failures too. Parents (`/task`,
`/analyze`, `/grill-me`, `/implement`, `/design`) apply code-quality.md and code-structure.md
before planning or writing code.

### If this is a user one-off (audit or fix a lane)

Use when the user asks about coding style, keep-it-simple, don’t-repeat-yourself,
principles, or “is this clean?”; when reviewing a lane without a full `/task`;
or when tightening a messy file before or after a small change.

1. Identify the lane (paths / symbols) and the ask.
2. Apply [code-quality.md](../rules/code-quality.md) plus [examples.md](examples.md). Use cite keys (`taste:keep-it-simple` and Named principles).
3. Report concrete violations with path evidence and the smallest fix
   (`taste:leave-it-cleaner` / `taste:keep-it-simple`: no speculative rewrite).
4. If the user asks to fix, apply only behavior-preserving edits in that lane.
   Larger product scope → recommend `/analyze` or `/task`.
5. Do not invent a parent wave, write tests, or start `/create-test`.

Hand-offs: structure / folders / services → `/architecture`. Build end-to-end
→ `/task`. Research first → `/analyze`.

### If this skill is already loaded inside a build

1. Apply code-quality.md and code-structure.md before grill close, plan contracts,
   or implement briefs.
2. Carry relevant cite keys into Active Rules / acceptance when they are
   behavioral (example: `taste:fail-fast` at a boundary, `taste:safe-to-retry`
   on a webhook).
3. Run the checklist in [code-quality.md](../rules/code-quality.md) before acceptance evidence and
   `/review`.
4. `/review` Standards axis treats taste **and** architecture violations as
   hard unless repo docs contradict.

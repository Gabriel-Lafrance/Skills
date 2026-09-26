---
name: taste
description: >-
  Examples and a lane audit for the taste rules in rules/code-quality.md. Those rules
  are always on. Use this skill to judge a concrete shape or see good and
  bad snippets, not as the source of the rules.
disable-model-invocation: true
---

# Taste

Audit a lane against the taste rules. The rules live in `rules/` and apply whether or not this skill runs; this skill holds the audit steps and the examples. Cite keys are the headings in [code-quality.md](../rules/code-quality.md).

## Read when

- Every run: [code-quality.md](../rules/code-quality.md) and [code-structure.md](../rules/code-structure.md) ([standards.md](../pack-shared/standards.md)).
- Judging a concrete shape: [examples.md](examples.md).
- Verifying or touching UI: [reference.md](reference.md).
- Talking to the user: [plain-language.md](../pack-shared/plain-language.md). Cite principles as **plain (Classic)**: `keep this simple (KISS)`, never acronym-only and never the paraphrase without the classic name.
- Before asking the user anything: [asking.md](../pack-shared/asking.md).

Placement and `taste:keep-jobs-apart` defects are taste failures too.

### If this is a user one-off (audit or fix a lane)

Use when the user asks about coding style, keep-it-simple, don’t-repeat-yourself,
principles, or “is this clean?”; when reviewing a lane without a full `/task`;
or when tightening a messy file before or after a small change.

1. Identify the lane (paths / symbols) and the ask.
2. Judge the lane against code-quality.md and examples.md, using cite keys
   (`taste:keep-it-simple` and Named principles).
3. Report concrete violations with path evidence and the smallest fix
   (`taste:leave-it-cleaner` / `taste:keep-it-simple`: no speculative rewrite).
4. If the user asks to fix, apply only behavior-preserving edits in that lane.
   Larger product scope → recommend `/analyze` or `/task`.
5. Do not invent a parent lifecycle, write tests, or start `/create-test`.

Hand-offs: structure / folders / services → `/architecture`. Build end-to-end
→ `/task`. Research first → `/analyze`.

### If this skill is already loaded inside a build

Parents (`/task`, `/analyze`, `/grill-me`) apply
code-quality.md and code-structure.md before planning or writing code.

1. Apply both files before grill close, plan contracts, or implement briefs.
2. Carry relevant cite keys into rules that must stay true or Done when, if they are
   behavioral (example: `taste:fail-fast` at a boundary, `taste:safe-to-retry`
   on a webhook).
3. Run the checklist in code-quality.md before acceptance evidence and
   `/review`.
4. `/review` Standards axis treats taste **and** architecture violations as
   hard unless repo docs contradict.

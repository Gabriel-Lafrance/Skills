# Taste process

Read [../pack-shared/standards.md](../pack-shared/standards.md), then
[doctrine.md](doctrine.md) and [examples.md](examples.md). Read
[reference.md](reference.md) when verifying or touching UI. Also Read
`/architecture` doctrine this turn. Placement and `taste:keep-jobs-apart`
defects are taste failures too.

Other pack skills must read this and `/architecture` before planning or
writing code (see [../pack-shared/standards.md](../pack-shared/standards.md)).

### If this is a user one-off (audit or fix a lane)

Use when the user asks about coding style, keep-it-simple, don’t-repeat-yourself,
principles, or “is this clean?”; when reviewing a lane without a full `/goal`;
or when tightening a messy file before or after a small change.

1. Identify the lane (paths / symbols) and the ask.
2. Read doctrine + examples; apply Cite keys (`taste:keep-it-simple` and Named principles).
3. Report concrete violations with path evidence and the smallest fix
   (`taste:leave-it-cleaner` / `taste:keep-it-simple`: no speculative rewrite).
4. If the user asks to fix, apply only behavior-preserving edits in that lane.
   Larger product scope → recommend `/analyze` or `/goal`.
5. Do not invent a parent wave, write tests, or start `/create-test`.

Hand-offs: structure / folders / services → `/architecture`. Build end-to-end
→ `/goal`. Research first → `/analyze`.

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

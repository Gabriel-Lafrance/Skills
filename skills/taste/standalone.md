# Taste (standalone)

Apply or audit pack coding taste outside a build wave. Read
[../pack-shared/standards.md](../pack-shared/standards.md), then
[doctrine.md](doctrine.md) and [examples.md](examples.md). Read
[reference.md](reference.md) when verifying or touching UI. Also Read
`/architecture` doctrine this turn. Placement and `taste:keep-jobs-apart`
defects are taste failures too.

## When to use

- User asks about coding style, keep-it-simple, don’t-repeat-yourself, principles, or “is this clean?”
- Review a lane for taste/principle violations without a full `/goal`
- Tighten a messy file before or after a small change

## Process

1. Identify the lane (paths / symbols) and the ask.
2. Read doctrine + examples; apply Cite keys (`taste:keep-it-simple` and Named principles).
3. Report concrete violations with path evidence and the smallest fix
   (`taste:leave-it-cleaner` / `taste:keep-it-simple`: no speculative rewrite).
4. If the user asks to fix, apply only behavior-preserving edits in that lane.
   Larger product scope → recommend `/analyze` or `/goal`.
5. Do not invent a parent wave, write tests, or start `/create-test`.

## Hand-offs

- Structure / folders / services → `/architecture`
- Build end-to-end → `/goal`
- Research first → `/analyze`

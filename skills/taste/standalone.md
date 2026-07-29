# Taste (standalone)

Apply or audit pack coding taste outside a build wave. Read [doctrine.md](doctrine.md)
and [examples.md](examples.md).

## When to use

- User asks about coding style, KISS, DRY, principles, or “is this clean?”
- Review a lane for taste/principle violations without a full `/goal`
- Tighten a messy file before or after a small change

## Process

1. Identify the lane (paths / symbols) and the ask.
2. Read doctrine + examples; apply KISS and **Named principles**.
3. Report concrete violations with path evidence and the smallest fix
   (Boy Scout / KISS — no speculative rewrite).
4. If the user asks to fix, apply only behavior-preserving edits in that lane.
   Larger product scope → recommend `/analyze` or `/goal`.
5. Do not invent a parent wave, write tests, or start `/create-test`.

## Hand-offs

- Structure / folders / services → `/architecture`
- Build end-to-end → `/goal`
- Research first → `/analyze`
- UI craft → `/design`

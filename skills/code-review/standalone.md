# Code Review

**Stance:** A+ exam — catch every evidenced defect before `/pr-review` (see [doctrine.md](doctrine.md) Stance). Every failure claim needs a reachable trigger and concrete evidence; operational intensity is not speculation.

**Read:** [doctrine.md](doctrine.md) · [examples.md](examples.md)

## Process

1. **Pin fixed point** — `git diff <fixed-point>...HEAD` (doctrine)
2. **Resolve spec source** — user paste, PR/issue, commits, or ask
3. **Wave 1** — launch Standards + Spec + Routes + BigPicture + Risk in parallel (doctrine prompts; skip Spec only if no spec; fill-or-fail artifacts)
4. **Aggregate Wave 1** — separate `## Standards`, `## Spec`, `## Routes`, `## BigPicture`, `## Risk`
5. **Wave 2** — always launch adversarial Task(s); merge unique hits (doctrine)
6. **Needs /create-test** — recommend to user; do not run; do not write tests (doctrine)
7. **Remediation disposition** — Fix-now / Follow-up / optional-nit backlog + Questions batch via [../asking.md](../asking.md); on yes → `/analyze` proposed fixes → explicit bounded `/goal` promotion (doctrine)

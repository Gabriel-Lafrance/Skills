---
name: pack-shared
description: >-
  Internal pack contracts for Gabriel Lafrance Skills: asking,
  stateless execution context, review behavior,
  and how every agent opens a PR. Not
  user-invoked. Other skills link here so shared docs install with npx skills
  (skill folders only).
disable-model-invocation: true
---

# Pack shared contracts

Not a user skill. Do not recommend `/pack-shared`. This folder exists so `npx skills` installs the contracts next to every other skill (`../pack-shared/...`). Root-level `skills/*.md` files are **not** installed.

## Read when

Other skills link the file they need at the step that needs it:

- [plain-language.md](plain-language.md): talking to humans in ordinary words
- [asking.md](asking.md): asking the user anything
- [execution-context.md](execution-context.md): keeping in-chat context across phases
- [review-contract.md](review-contract.md): reviewing (evidence, modes, finding records)
- [ship.md](ship.md) and [pr-ship.md](pr-ship.md): only when this chat will cut a branch or open a PR (templates, create tool, standalone branch push, CI mirror)

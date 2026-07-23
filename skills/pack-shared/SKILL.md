---
name: pack-shared
description: >-
  Internal pack contracts for Gabriel Lafrance Skills: asking, variants, and
  workspace-roots. Not user-invoked. Other skills link here so shared docs
  install with npx skills (skill folders only).
disable-model-invocation: true
---

# Pack shared contracts

Not a user skill. Do not recommend `/pack-shared`.

Other skills Read these files by relative path:

- [asking.md](asking.md) — how to ask the user
- [variants.md](variants.md) — standalone vs flow selection
- [workspace-roots.md](workspace-roots.md) — goal/analysis root resolution

This folder exists so `npx skills` installs the contracts next to every other skill (`../pack-shared/...`). Root-level `skills/*.md` files are **not** installed.

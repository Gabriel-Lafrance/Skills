---
name: rules
description: >-
  Rule files for Gabriel Lafrance Skills that the always-on AGENTS.md index
  points to: code quality, code structure, planning, user experience,
  writing style, testing, shipping, and tooling. Not
  user-invoked. Other skills and AGENTS.md link here so the rules install
  with npx skills (skill folders only).
disable-model-invocation: true
---

# Pack rules

Not a user skill. Do not recommend `/rules`. This folder exists so `npx skills` installs the rules next to every other skill (`../rules/...`). Root-level `skills/*.md` files are **not** installed.

## Read when

The Read when table in `AGENTS.md` is the source for when to open each file:

- [code-quality.md](code-quality.md): taste rules (`taste:*` cite keys), keep it simple, named principles, mechanical rules, reuse env vars, naming
- [code-structure.md](code-structure.md): architecture rules (`architecture:*` cite keys), services, primitives, folders, cheap reads, authority, the Structure card
- [planning.md](planning.md): reads before planning, grill first, the Before/After change diagram
- [user-experience.md](user-experience.md): every UI and UX rule (`design:*` cite keys), `docs/design.md` as the app UX source of truth, copy, locale, quality floor
- [writing-style.md](writing-style.md): no em dash, and the Unslop rules for chat replies
- [testing.md](testing.md): no drive-by tests; write a test only after the user accepts that lock
- [shipping.md](shipping.md): branch names and hard rules for branches and pull requests
- [tooling.md](tooling.md): lint, format, and the CI mirror before a push

---
name: rules
description: Rule files the always-on AGENTS.md index points to. Not user-invoked. Other skills link here so the rules install with npx skills.
category: Documents
disable-model-invocation: true
---

# Pack rules

Not a user skill. Do not recommend `/rules`. This folder exists so `npx skills` installs the rules next to every other skill (`../rules/...`). Root-level `skills/*.md` files are **not** installed.

## Read when

The Rules section and the Read when table in `AGENTS.md` are the source for when to open each file.

One file per rule, named in the `AGENTS.md` Rules section:

- [keep-it-simple.md](keep-it-simple.md): least code for the result, subtract first, light to read, a folder per concern, no `utils` dumps
- [strong-foundation.md](strong-foundation.md): a strong first iteration with a seam on each area of modularity, scaled to the work and the context
- [no-unrequested-tests.md](no-unrequested-tests.md): no test unless the user accepted it
- [smart-zone.md](smart-zone.md): keep judgment in the main context, hand noisy work to a subagent

Journeys, listed in [`/ask-gabriel`](../ask-gabriel/SKILL.md#journeys): [journeys/](journeys/new-feature.md) holds one file per journey, each following one piece of billing work through the skills and rules.

Topic files, named in the Read when table:

- [code-quality.md](code-quality.md): code quality rules (`quality:*` cite keys), named principles, mechanical rules, reuse env vars, naming
- [code-quality-examples.md](code-quality-examples.md): good and bad snippets for code-quality.md
- [code-structure.md](code-structure.md): code structure rules (`structure:*` cite keys), services, primitives, folders, cheap reads, authority (the server enforces), the Structure card
- [code-structure-examples.md](code-structure-examples.md): good and bad shapes for code-structure.md
- [planning.md](planning.md): reads before planning, grill first, the Before/After change diagram, and the in-chat execution context (authority order, context template, optional persistence)
- [user-experience.md](user-experience.md): every UI and UX rule (`ux:*` cite keys), React and UI, `docs/design.md` as the app UX source of truth, copy, locale, quality floor
- [writing-style.md](writing-style.md): no em dash, plain language and plain (Classic) principle names, asking the user (Questions and Locked-in templates), and the Unslop rules for chat replies
- [testing.md](testing.md): when an accepted test is worth writing, what a good test looks like, the lock brief, the test comment, and the handoff
- [shipping.md](shipping.md): branch names, shipping rules, the create tool, the CI mirror, and the branch-and-push process
- [shipping-templates.md](shipping-templates.md): ship questions and announcements, the PR Change diagram rule, and the PR title and body template
- [tooling.md](tooling.md): lint, format, verify terminals first, and when to run the CI mirror

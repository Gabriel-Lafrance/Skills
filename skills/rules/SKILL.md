---
name: rules
description: Rule files the always-on AGENTS.md index points to. Not user-invoked. Other skills link here so the rules install with npx skills.
category: Documents
disable-model-invocation: true
---

# Pack rules

Not a user skill: never recommend `/rules`. This folder exists so `npx skills` installs the rules next to every other skill (`../rules/...`). Root-level `skills/*.md` files are **not** installed.

## Read when

The Rules section and the Read when table in `AGENTS.md` are the source for when to open each file.

One file per rule, named in the `AGENTS.md` Rules section:

- [keep-it-simple.md](keep-it-simple.md): least code for the result, subtract first, light to read, a folder per concern instead of `utils` dumps
- [strong-foundation.md](strong-foundation.md): a strong first iteration with a seam (a named extension point where a new variant plugs in) on each area of modularity, scaled to the work and the context
- [no-unrequested-tests.md](no-unrequested-tests.md): no test unless the user accepted it
- [main-context.md](main-context.md): keep judgment in the main context, hand noisy work to a subagent

Journeys, listed in [`/ask-gabriel`](../ask-gabriel/SKILL.md#journeys): [journeys/](journeys/new-feature.md) holds one file per journey, each following one piece of billing work through the skills and rules.

Topic files, named in the Read when table:

- [code-quality.md](code-quality.md): code quality rules (`quality:*` cite keys), named principles, mechanical rules, reuse env vars, naming
- [code-quality-examples.md](code-quality-examples.md): good and bad snippets for code-quality.md
- [code-structure.md](code-structure.md): code structure rules (`structure:*` cite keys), services, primitives (one-job helpers), folders, cheap reads, authority (the server enforces), the Structure card
- [code-structure-examples.md](code-structure-examples.md): good and bad shapes for code-structure.md
- [planning.md](planning.md): reads before planning, grill first, the Before/After change diagram, and the in-chat execution context (authority order, context template, optional persistence)
- [user-experience.md](user-experience.md): every UI and UX rule (`ux:*` cite keys), React and UI, `docs/design.md` as the app UX source of truth, copy, locale, quality floor
- [writing-style.md](writing-style.md): no em dash, plain language and plain (Classic) principle names, asking the user (Questions and Locked-in templates), and the Unslop rules for chat replies
- [testing.md](testing.md): when an accepted test is worth writing, the authoring gate, junk patterns, the retention bar, what a good test looks like, the lock brief, the test comment, and the handoff
- [shipping.md](shipping.md): branch safety, scoped pre-push/required checks, remote CI reporting, the create tool, and the branch-and-push process
- [shipping-templates.md](shipping-templates.md): ship questions and announcements, the PR Change diagram rule, and the PR title and body template
- [tooling.md](tooling.md): focused lint/type/test checks, terminal evidence, and applicable shipping checks
- [principles.md](principles.md): steering vocabulary for a design, verification, or delegation judgment. One-line rule, when to open it, and a pointer to the file that owns the detail

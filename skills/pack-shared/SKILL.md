---
name: pack-shared
description: >-
  Internal pack contracts for Gabriel Lafrance Skills: asking,
  stateless execution context, subagent dispatch, review behavior, browser
  evidence, and how every agent opens a PR (canvas, screenshots). Not
  user-invoked. Other skills link here so shared docs install with npx skills
  (skill folders only).
disable-model-invocation: true
---

# Pack shared contracts

Not a user skill. Do not recommend `/pack-shared`.

Other skills Read these files by relative path:

- [standards.md](standards.md) — must follow `/taste` and `/architecture` on every skill run
- [doctrine-schema.md](doctrine-schema.md) — H2 order every `skills/*/doctrine.md` must use
- [plain-language.md](plain-language.md) — talk to humans in ordinary words
- [asking.md](asking.md) — how to ask the user
- [execution-context.md](execution-context.md) — in-chat context and worker handoff
- [subagents.md](subagents.md) — what vs how; pick the specialist; tester always writes tests; Worker Brief
- [review-contract.md](review-contract.md) — evidence, modes, and finding records
- [browser-evidence.md](browser-evidence.md) — browser proof for UI acceptance
  (`/task`); not for PR Demo screenshots
- [pr-ship.md](pr-ship.md) — every agent that opens a PR: Browser screenshots
  for Demo (not a test pass), Cursor review canvas, create-tool choice (not
  only `/publish`)

This folder exists so `npx skills` installs the contracts next to every other skill (`../pack-shared/...`). Root-level `skills/*.md` files are **not** installed.

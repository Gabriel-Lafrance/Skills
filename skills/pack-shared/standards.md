# Hard-apply taste and architecture

Pack skills do **not** depend on Cursor User Rules. The file in [`rules/`](../../rules/ultimate-gold-standards.mdc) is **opt-in** for Plan mode and freeform chats that never invoke a skill. When a pack skill runs, **this contract is the enforcement**.

Do not substitute a private checklist or this file’s summary. **Source of truth is the doctrines.**

## Required Reads (every skill run)

Before grilling, planning, specifying, splitting, implementing, reviewing, or shipping:

1. **Read** [`../taste/doctrine.md`](../taste/doctrine.md) — KISS, named principles, non-negotiables. Read [`../taste/examples.md`](../taste/examples.md) when judging a shape.
2. **Read** [`../architecture/doctrine.md`](../architecture/doctrine.md) — services, deep public surface, primitives, folders, write-path scale. Read [`../architecture/examples.md`](../architecture/examples.md) when judging structure.

Do this **every time** the skill is used this turn, including flow steps. Do not skip because you “already know” the pack. If you have not Read both doctrines this turn, **stop and Read them** before continuing.

## Who loads this

| Actor | Load |
| --- | --- |
| Every pack skill except `/ask-gabriel` | **Yes** — this file, then both doctrines |
| `/ask-gabriel` | **No** — stay thin; the recommended next skill loads this |
| Task workers that write, review, or research product code | **Yes** — Worker Brief **Read first** includes both doctrines |

## How to apply (hard, not flavor)

- **Taste is hard.** KISS, named principles, never-nest, DRY, throw + purposeful try/catch, honest names, and the rest of the taste non-negotiables fail the skill’s quality bar when violated. `/code-review` Standards treats them as **hard** unless repository docs contradict.
- **Architecture is hard.** Always load it. Apply services, public APIs, primitives, folders, SoC / cohesion / coupling, idempotent writes, and write-path scale whenever the work could add files, move ownership, or touch data. For a typo or a user-specified pure rename, still load; the application is “keep the existing structure.”
- **Smallest structure still wins.** Loading architecture does not authorize ceremony. Taste KISS and the architecture abstraction budget still require the smallest shape that meets the outcome.
- **Fail closed.** Do not invent a weaker standard. Do not treat “structure not in play” as permission to skip the architecture Read.

## Parents and workers

Parents put both doctrine paths in every Worker Brief **Read first** (see [subagents.md](subagents.md)). Workers apply them inside the write allowlist. Do not improvise a new service, primitive, or folder layout that violates the loaded doctrines — report the blocker to the parent.

## Conflict

Repository `AGENTS.md` / `.cursor/rules` may add constraints. They must not weaken taste or architecture unless the user explicitly overrides in chat.

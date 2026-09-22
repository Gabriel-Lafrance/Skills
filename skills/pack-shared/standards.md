# Must follow taste and architecture

The always-on contract is the pack [`AGENTS.md`](../../AGENTS.md). **Taste** and **Architecture** in that file are rules, not optional skills. Pack skills do **not** depend on a User Rules paste or a Cursor rules file. When a pack skill runs, apply those sections. They are not a substitute you may skip.

Do not substitute a private checklist or this file's summary. **Source of truth is the Taste and Architecture sections of `AGENTS.md`.**

## Required Reads (every skill run)

Before grilling, planning, specifying, splitting, implementing, reviewing, or shipping:

1. Apply the **Taste** and **Architecture** sections of [`AGENTS.md`](../../AGENTS.md). If that file is not already in context, Read it. Read [`../taste/examples.md`](../taste/examples.md) and [`../architecture/examples.md`](../architecture/examples.md) when judging a shape. Read [`../taste/reference.md`](../taste/reference.md) when verifying or touching UI. Also Read [`plain-language.md`](plain-language.md) before any user-facing message.

Do this **every time** the skill is used this turn, including worker steps. Do not skip because you "already know" the pack. If those sections are not already in context, **stop and Read `AGENTS.md`** before continuing.

## Who loads this

| Actor | Load |
| --- | --- |
| Every pack skill except `/ask-gabriel` | **Yes.** This file, then apply the Taste and Architecture sections |
| `/ask-gabriel` | **No.** Stay thin. The recommended next skill loads this |
| Task workers that write, review, or research product code | **Yes.** Worker Brief **Read first** includes the Taste and Architecture sections of `AGENTS.md` |

## How to apply (hard, not flavor)

- **Taste is required.** Apply the cite keys in the Taste section. Violations fail the skill's quality bar. `/code-review` treats them as required unless repository docs contradict.
- **Architecture is required.** Always apply it. Use its cite keys whenever the work could add files, move ownership, or touch data. New files go in an owning folder (`architecture:folders`). Do not dump them in a mixed parent. For a typo or a user-specified pure rename, still apply it. The application is "keep the existing structure."
- **Smallest structure still wins.** Applying architecture does not authorize extra layers. Taste still requires the smallest shape that meets the outcome (`taste:keep-it-simple`). The owning folder is not an extra layer.
- **Fail closed.** Do not invent a weaker standard. Do not treat "structure not in play" as permission to skip the Architecture section.

## Parents and workers

Parents name the Taste and Architecture sections of `AGENTS.md` in every Worker Brief **Read first** (see [subagents.md](subagents.md)). Workers apply them inside the write allowlist. Do not improvise a new service, primitive, or folder layout that violates those sections. Report the blocker to the parent.

## Conflict

A repository's own instructions may add constraints. They must not weaken taste or architecture unless the user explicitly overrides in chat.

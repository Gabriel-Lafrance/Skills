# Must follow taste and architecture

The always-on index is the pack `AGENTS.md`. The rules it points to live in [`../rules/code-quality.md`](../rules/code-quality.md) (taste) and [`../rules/code-structure.md`](../rules/code-structure.md) (architecture). They are rules, not optional skills. Pack skills do **not** depend on a User Rules paste or a Cursor rules file. When a pack skill runs, apply those files. They are not a substitute you may skip.

Do not substitute a private checklist or this file's summary. **Source of truth is [`code-quality.md`](../rules/code-quality.md) and [`code-structure.md`](../rules/code-structure.md).**

## Required Reads (every skill run)

Before grilling, planning, specifying, splitting, implementing, reviewing, or shipping:

1. Apply [`../rules/code-quality.md`](../rules/code-quality.md) and [`../rules/code-structure.md`](../rules/code-structure.md). If they are not already in context, Read them. Read [`../taste/examples.md`](../taste/examples.md) and [`../architecture/examples.md`](../architecture/examples.md) when judging a shape. Read [`../taste/reference.md`](../taste/reference.md) when verifying or touching UI. Also Read [`plain-language.md`](plain-language.md) before any user-facing message.

Do this once per session unless the file is already in context. Do not skip because you "already know" the pack. If those files are not already in context, **stop and Read them** before continuing.

## Who loads this

| Actor | Load |
| --- | --- |
| Every pack skill except `/ask-gabriel` | **Yes.** This file, then apply `code-quality.md` and `code-structure.md` |
| `/ask-gabriel` | **No.** Stay thin. The recommended next skill loads this |
| Task workers that write, review, or research product code | **Yes.** Worker Brief **Read first** includes `rules/code-quality.md` and `rules/code-structure.md` |

## How to apply (hard, not flavor)

- **Taste is required.** Apply the cite keys in [`code-quality.md`](../rules/code-quality.md). Violations fail the skill's quality bar. `/review` treats them as required unless repository docs contradict.
- **Architecture is required.** Always apply it. Use its cite keys whenever the work could add files, move ownership, or touch data. New files go in an owning folder (`architecture:folders`). Do not dump them in a mixed parent. For a typo or a user-specified pure rename, still apply it. The application is "keep the existing structure."
- **Smallest structure still wins.** Applying architecture does not authorize extra layers. Taste still requires the smallest shape that meets the outcome (`taste:keep-it-simple`). The owning folder is not an extra layer.
- **Fail closed.** Do not invent a weaker standard. Do not treat "structure not in play" as permission to skip [`code-structure.md`](../rules/code-structure.md).

## Parents and workers

Parents name `rules/code-quality.md` and `rules/code-structure.md` in every Worker Brief **Read first** (see [subagents.md](subagents.md)). Workers apply them inside the write allowlist. Do not improvise a new service, primitive, or folder layout that violates those files. Report the blocker to the parent.

## Conflict

A repository's own instructions may add constraints. They must not weaken taste or architecture unless the user explicitly overrides in chat.

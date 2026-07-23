# Skill variants (pack-wide)

Dual skills ship `standalone.md` and/or `flow.md`. The agent **chooses** which to load. Do **not** restate this contract inline — link here: [`variants.md`](variants.md).

Same contract for every dual skill — today and for future long-running orchestrators. Prefer wording that stays true without naming a specific wave skill.

## Hard rules

1. Read **exactly one** of `standalone.md` or `flow.md` this turn — never both.
2. If the user (or calling prompt) says `standalone` / `flow`, honor that **only if that file exists**; if missing, use the matching message below (do not invent the other process).
3. Otherwise pick using the hints; match **how the work is being run**, not a keyword hunt for a workspace id alone.
4. After picking an existing file, follow that file’s Read-first links only.
5. Never silently fall back to the other variant.
6. Goal-scoped flows resolve `goal_root` from [workspace-roots.md](workspace-roots.md); a parent wave's supplied root wins over a pack-global default.
7. **Missing `variants.md` is not a stop.** If this file cannot be Read, still choose using the skill’s local `standalone.md` / `flow.md` and the hints above. “Missing file” in dual-skill SKILL.md means missing `standalone.md` or `flow.md`, not this contract.

## Hints

| Prefer **flow** when | Prefer **standalone** when |
| --- | --- |
| Continuing a long-running pack wave (orchestrator skill, implement step, nested repair under that workspace) | User asked for a one-off outside any wave |
| Another pack skill told you to run this as a step in that wave | No active wave/workspace is in play and the ask is self-contained |
| Writing under that wave’s temp workspace (e.g. `.agents/temp/<wave>/<id>/`) as part of the loop | Sharpening / reviewing / fixing in isolation |

## Missing-variant messages

**No `standalone.md`** (wanted standalone):

```text
Standalone variant isn’t available.
This skill isn’t meant to be used that way — it runs as a flow step.
Next: /ask-gabriel — or start the long-running skill that owns this wave and use this skill inside that loop.
```

**No `flow.md`** (wanted flow):

```text
Flow variant isn’t available.
This skill isn’t meant to be used that way — it is standalone-only.
Next: /ask-gabriel — or run this skill as a one-off (standalone), not inside a long-running wave.
```

## Anti-patterns

- Loading both variants “to be safe”
- Inventing a missing variant’s process
- Silent fallback to the other file
- Treating a workspace id as a hard switch when the user clearly wants a one-off
- Hard-coding this file to one orchestrator skill (keep hints and messages wave-agnostic)

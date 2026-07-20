# Asking the user (pack-wide)

Every pack skill that needs decisions follows this contract — including one-offs **and** any long-running / multi-wave skill. Do **not** restate these rules inline — link here: [`asking.md`](asking.md).

When a new long-running skill appears later, it still uses this file as-is. Prefer wording that stays true without naming a specific orchestrator.

## Rules

1. **Batch every question you already know** into **one** message — never drip one-at-a-time when multiple opens are known.
2. Number them `1`, `2`, `3`… Each item: short prompt + lettered options when discrete.
3. **Every optioned item must mark a recommended option** (`← recommended`).
4. Tell the user to reply like the **recommended** answers filled in, e.g. `Reply like: 1a, 2b, 3a` where those letters **are** your recommendations for this batch (so accepting defaults is copy-paste). They may override any letter. Optional: `1a — short note` per number.
5. **Wait** for that batch reply before acting on those decisions.
6. After explore/implement/review and **new** unknowns appear, send a **new** batch — that is fine. Do not re-ask settled items.
7. Look up facts in the repo/tools — do not put those in the batch.
8. Decisions are the user’s — honor overrides of recommended options.
9. **Only ask when an action is needed.** Do not put items in Questions if there is nothing to decide (e.g. already correctly done). Still may list them briefly as info outside the Questions block.

## Recommended defaults (bias)

When drafting options, prefer these as **recommended** unless the user already locked otherwise:

| Topic | Prefer (recommended) |
| --- | --- |
| Taste / entry shape | Match `/taste` doctrine + a **good** sibling |
| Unsure which skill | Recommend `/ask-gabriel` |
| Architecture | Services over feature-forked domain logic; folders before files |
| Prior mistakes / debt | **Behavior-preserving move** into the right service/folder — not “leave it where it is” |
| Complexity / entropy | **Deep module** + behavior-preserving cleanup over “leave debt / add another shallow helper” |
| Package / vendor / storage | Lock a one-phrase pick into the active skill’s choice log (e.g. under `.agents/temp/…/choice.md`) |
| Actor / business policy | Lock a one-phrase rule into the active skill’s rules log (e.g. under `.agents/temp/…/rules.md`) |
| Repair | **Smallest patch** that fixes the defect |
| Design polish | Smallest depth/color/hierarchy fix over structural rewrite |
| Confirm gates / recap | `a) yes` when the recap already matches answers locked earlier in this session or wave |

## Batch template

```markdown
## Questions
Reply like: `1a, 2c, 3a` (recommended answers already filled in; change any letter to override; add a short note after a letter if needed).

1. <topic>?
   - a) <recommended> ← recommended
   - b) <alternative>
   - c) Other — say what you want
2. <topic>?
   - a) …
   - b) …
   - c) <recommended> ← recommended
3. <topic>?
   - a) yes ← recommended
   - b) no — say what to change
```

The `Reply like: …` line **must** use the recommended letter for each numbered item (here `1a, 2c, 3a`), not placeholder examples that disagree with `← recommended`.

Yes/no gates use the same shape (`a) yes` / `b) no`). Freeform-only items still get a number; omit letters and ask for a short reply under that number.

Works the same whether the caller is a short skill turn or a long-running wave that will ask again later when new opens appear.

## Anti-patterns

- One question per message when you already have a list of opens
- Optioned questions with no recommended mark
- `Reply like:` using fake letters that are not the recommended set for this batch
- Asking about items with no decision/action (noise Questions)
- Recommending “keep the wrong layout” when a clear move preserves behavior
- Hard-coding this file to one orchestrator skill (keep examples and defaults skill-agnostic)

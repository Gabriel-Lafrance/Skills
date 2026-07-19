# Asking the user (pack-wide)

Every pack skill that needs decisions follows this contract. Do **not** restate these rules inline — link here: [`asking.md`](asking.md).

## Rules

1. **Batch every question you already know** into **one** message — never drip one-at-a-time when multiple opens are known.
2. Number them `1`, `2`, `3`… Each item: short prompt + lettered options when discrete.
3. **Every optioned item must mark a recommended option** (`← recommended`).
4. Tell the user to reply like: `1a, 2b, 3a` (or `1a — short note` per number).
5. **Wait** for that batch reply before acting on those decisions.
6. After explore/implement/review and **new** unknowns appear, send a **new** batch — that is fine. Do not re-ask settled items.
7. Look up facts in the repo/tools — do not put those in the batch.
8. Decisions are the user’s — honor overrides of recommended options.

## Recommended defaults (bias)

When drafting options, prefer these as **recommended** unless the user already locked otherwise:

| Topic | Prefer (recommended) |
| --- | --- |
| Taste / entry shape | Match `/taste-flow` + a **good** sibling |
| Architecture | Services over feature-forked domain logic; folders before files |
| Prior mistakes / debt | **Behavior-preserving move** into the right service/folder — not “leave it where it is” |
| Complexity / entropy | **Deep module** + behavior-preserving cleanup over “leave debt / add another shallow helper” |
| Package / vendor / storage | Lock a one-phrase pick into `.agents/temp/grills/choice.md` |
| Actor / business policy | Lock a one-phrase rule into `.agents/temp/grills/rules.md` |
| Repair | **Smallest patch** that fixes the defect |
| Design polish (Mode B) | Smallest depth/color/hierarchy fix over structural rewrite |
| Closing gates (non-goals / split / shared understanding) | `a) yes` when the recap already matches locked GRILL answers |

## Batch template

```markdown
## Questions
Reply like: `1a, 2b, 3a` (add a short note after a letter if needed).

1. <topic>?
   - a) <recommended> ← recommended
   - b) <alternative>
   - c) Other — say what you want
2. <topic>?
   - a) …
   - b) …
3. <topic>?
   - a) yes ← recommended
   - b) no — say what to change
```

Yes/no gates use the same shape (`a) yes` / `b) no`). Freeform-only items still get a number; omit letters and ask for a short reply under that number.

## Anti-patterns

- One question per message when you already have a list of opens
- Optioned questions with no recommended mark
- Recommending “keep the wrong layout” when a clear move preserves behavior

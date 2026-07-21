# Asking the user (pack-wide)

Every pack skill that needs decisions follows this contract — including one-offs **and** any long-running / multi-wave skill. Do **not** restate these rules inline — link here: [`asking.md`](asking.md).

When a new long-running skill appears later, it still uses this file as-is. Prefer wording that stays true without naming a specific orchestrator.

## Rules

1. **Batch every question you already know** into **one** message — never drip one-at-a-time when multiple opens are known.
2. Number them `1`, `2`, `3`… Each item: short prompt + lettered options when discrete.
3. **Every optioned item must mark a recommended option** (`← recommended`).
4. **`Reply like:` is codes only, one row** — e.g. `Reply like: 1a 2b 3c 4a 5b`. Space-separated; no commas; **no option text / descriptions**. Soft-wrap OK if long. Those letters **are** the recommendations (match each `← recommended` below). User overrides any letter; optional short note only when they need freeform.
5. **Wait** for that batch reply before acting on those decisions.
6. After explore/implement/review and **new** unknowns appear, send a **new** batch — that is fine. Do not re-ask settled items.
7. Look up facts in the repo/tools — do not put those in the batch.
8. Decisions are the user’s — honor overrides of recommended options.
9. **Only ask when an action is needed.** Do not put items in Questions if there is nothing to decide (e.g. already correctly done). Still may list them briefly as info outside the Questions block.
10. **Announce vs ask.** When the agent should own the call (user almost always accepts the recommendation), **do not** put a yes/no in Questions — **state it** in a short **Locked (correct if wrong)** block above Questions. The user corrects only if needed; silence = accept. Pack defaults for this pattern: **non-goals**, **plan split**, and **shared understanding** (a short summary of what the agent believes — not a yes/no). Real product/UX/architecture/taste *choices that are still open* stay in Questions.

## Recommended defaults (bias)

When drafting options, prefer these as **recommended** unless the user already locked otherwise:

| Topic | Prefer (recommended) |
| --- | --- |
| Taste / entry shape | Match `/taste` doctrine + a **good** sibling |
| Unsure which skill | Recommend `/ask-gabriel` |
| Architecture | Services over feature-forked domain logic; folders before files; compose **primitives** inside deep modules over ad-hoc reimplementation |
| Prior mistakes / debt | **Behavior-preserving move** into the right service/folder — not “leave it where it is” |
| Complexity / entropy | **Deep module** + **primitives** (reuse, do not fork) + behavior-preserving cleanup over “leave debt / add another shallow helper” |
| Package / vendor / storage | Lock a one-phrase pick into the active skill’s choice log (e.g. under `.agents/temp/…/choice.md`) |
| Actor / business policy | Lock a one-phrase rule into the active skill’s rules log (e.g. under `.agents/temp/…/rules.md`) |
| Repair | **Smallest patch** that fixes the defect |
| Design polish | Smallest depth/color/hierarchy fix over structural rewrite |
| Confirm gates / recap | **Announce** non-goals + plan split + shared-understanding summary in Locked. Ask only real open product/UX/architecture/taste choices |
| Ticket type (`/write-ticket`) | Feature when capability/enhancement; Bug when broken/wrong behavior |
| Ticket metadata (`/write-ticket`) | Status: backlog/todo for create; Priority: Medium unless urgency clear; Assignee: Unassigned unless an owner is obvious |

## Batch template

```markdown
## Locked (correct if wrong)
**Non-goals:** …
**Plans:** 1. … · 2. …  (or: one plan — …)
**Shared understanding:** …
- …
- … (include Moves / corrections + new language / choices / rules when relevant)

## Questions
Reply like: 1a 2c 3a

1. <open product/UX/architecture/taste choice>?
   - a) <recommended> ← recommended
   - b) <alternative>
   - c) Other — say what you want
```

Omit the **Locked** block when there is nothing to announce. Omit **Questions** when every open item is announce-only — state Locked and **continue** (user can interrupt with a correction). Do **not** turn non-goals, plan split, or shared understanding into yes/no Questions.

The `Reply like:` line **must** use the recommended letter for each numbered item (here `1a 2c 3a`) — codes only, one row, spaces not commas. Do **not** append option text. Long batches stay the same shape (`1a 2b 3c 4a 5b 6d 7b 8a`).

Yes/no Questions use the same shape (`a) yes` / `b) no`). Freeform-only items still get a number; omit letters and ask for a short reply under that number.

Works the same whether the caller is a short skill turn or a long-running wave that will ask again later when new opens appear.

## Anti-patterns

- One question per message when you already have a list of opens
- Optioned questions with no recommended mark
- `Reply like:` using fake letters that are not the recommended set for this batch
- Putting descriptions / option text in `Reply like:` (codes only)
- Stacking `Reply like:` as one answer per line
- Asking about items with no decision/action (noise Questions)
- Asking yes/no to confirm **non-goals**, **plan split**, or **shared understanding** — announce those; user corrects if needed
- Recommending “keep the wrong layout” when a clear move preserves behavior
- Hard-coding this file to one orchestrator skill (keep examples and defaults skill-agnostic)

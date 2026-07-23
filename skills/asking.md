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

## Skill exception

`/write-ticket` uses a two-stage ask:

1. Its vision, bug, or refactor **open grill** is numbered freeform questions only. Do not add lettered options, recommendations, or `Reply like:`.
2. Its type lock and write metadata use this normal lettered contract.

See [`write-ticket/doctrine.md`](write-ticket/doctrine.md).

## Recommended defaults (bias)

When drafting options, prefer these as **recommended** unless the user already locked otherwise:

| Topic | Prefer (recommended) |
| --- | --- |
| Taste / entry shape | Match `/taste` doctrine + a **good** sibling |
| Unsure which skill | Recommend `/ask-gabriel` |
| Architecture | Reuse a real service boundary; create one only for an independent capability, real duplication, a locked rule, or explicit growth — not speculative ceremony |
| Prior mistakes / debt | Behavior-preserving move when the current goal or named finding requires it; otherwise record a follow-up |
| Complexity / entropy | Keep a local guard inline unless extraction owns independent behavior, removes real duplication, or enforces an Active Rule; reuse an existing primitive rather than fork |
| Package / vendor / storage | Lock a one-phrase pick into the active skill’s choice log (e.g. under `.agents/temp/…/choice.md`) |
| Actor / business policy | Lock a one-phrase rule into the active skill’s rules log (e.g. under `.agents/temp/…/rules.md`) |
| Behavioral answer in a goal grill | Record it as a `GOAL.md` Active Rule (`INV-*`) by default; user may say it is only a preference, example, or non-binding idea |
| Code-review Fix now backlog | Run `/analyze` in review remediation mode first; show issue/current behavior, root cause, smallest proposed fix, touch surface, non-goals, and verification, then require explicit promotion before implementation |
| Review failure claim | Require a reachable trigger, concrete evidence, material impact, and smallest authoritative fix; omit remote hypothetical hardening |
| Repair | **Smallest patch** that fixes the defect |
| Design polish | Smallest depth/color/hierarchy fix over structural rewrite |
| Confirm gates / recap | **Announce** non-goals + plan split + shared-understanding summary in Locked. Ask only real open product/UX/architecture/taste choices |
| Ticket type (`/write-ticket`) | Feature when capability/enhancement; Tweak when a small intentional adjustment is neither a defect nor a standalone capability; Bug when broken/wrong behavior; Refactor when move/cleanup/debt without new product behavior |
| Ticket metadata (`/write-ticket`) | Status: backlog/todo for create; Priority: Medium unless urgency clear; Assignee: Unassigned unless an owner is obvious |
| Publish (`/publish`) | Branch + push unless user said local-only; then ask PR draft+publish (recommend yes); use Feature, Tweak, Bug, or Refactor to match the work; ticket id when known |
| Publish branch name | `{type}/{ticket}-{slug}` (e.g. `bug/IN-1234-fix-checkout-total`) — no colons |
| Just-do-it (`/just-do-it`) | Auto-take recommended child choices except optional review Follow-ups; early typed branch; dual code-review; fix via scoped `/goal` only; no `/pr-review`; nested workspace under `.agents/temp/just-do-it/<id>/` |
| Just-do-it fix goals | Same ticket lane; named Fix-now invariant/spec/correctness/security/regression blockers only; no drive-by full refactor |

## Batch template

```markdown
## Locked (correct if wrong)
**Non-goals:** …
**Plans:** 1. … · 2. …  (or: one plan — …)
**Shared understanding:** …
- …
- … (include Moves / corrections + new language / choices / rules when relevant)
**Active Rules:** `INV-1` … · `INV-2` … (or _none_)

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

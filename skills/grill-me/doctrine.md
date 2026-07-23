# Grill Me Doctrine

Interview until you and the user share understanding. **Standalone** — for goal workspaces use **`/grill-me`**.

**Pack-wide ask style:** follow [../asking.md](../asking.md) — batch, not drip.

## Shared themes (ubiquitous language + choices + app rules)

Durable domain facts live under **`.agents/temp/grills/`** as **theme files** — not in goal `GRILL.md`. Goal `GRILL.md` stays **goal-scoped** (outcome, gates, taste/arch/design for this goal).

```text
.agents/temp/grills/
  REGISTRY.md      # themes + last updated
  language.md      # ubiquitous language
  choice.md        # locked decisions
  rules.md         # app rules (actors + policies)
```

| File | Owns | One-phrase shape |
| --- | --- | --- |
| `language.md` | Domain vocabulary: nouns/verbs, forbidden synonyms, named events/facts, stable context names as words | `Invoice — a bill owed by a customer for a completed order` · `Charge — not PaymentIntent` |
| `choice.md` | A-over-B / package / storage / vendor picks (+ hard limits framed as picks) | `Stripe over Polar — need custom metered billing` · `Cookie over localStorage — SSR needs auth token` |
| `rules.md` | **App rules:** who can do what + standing business policies | `Owner — can invite members and change billing` · `Refund — allowed within 30 days of Charge` |

Both **standalone** and **flow** variants of `/grill-me` **upsert** the matching theme file(s) when terms, choices, or rules lock. Append/update lines — do not wipe unrelated prior entries. Prefer exact term match over synonyms. Align code/service names with `language.md` (DDD).

After each batch that locks any of these, **write the theme file(s)** — not chat-only. Upsert `REGISTRY.md` (`theme` | `updated`).

Theme file shapes:

```markdown
# Language
**Updated:** <ISO>

- Invoice — a bill owed by a customer for a completed order
```

```markdown
# Choices
**Updated:** <ISO>

- Stripe over Polar — need custom metered billing + existing Stripe webhooks
```

```markdown
# Rules
**Updated:** <ISO>

- Owner — can invite members and change billing
- Refund — allowed within 30 days of Charge
```

## Active Rules (goal behavior)

When grilling inside a goal, every **behavioral** answer defaults to an Active Rule in `<goal-root>/GOAL.md` unless the user explicitly calls it an example, preference, or non-binding idea. An Active Rule is a condition that must remain true while the feature runs, not a request for a new abstraction.

Use one `INV-*` row per rule in `GOAL.md` with its scope, intended plan, authoritative enforcement point, and verification. A standing rule may remain in `grills/rules.md`, but copy it into the goal ledger whenever this goal must honor it.

Sweep every behaviorally material unknown in batched questions before closing:

- Actor and permission
- Triggered action and expected outcome
- Enabled, disabled, loading, and empty states
- State transitions and what is forbidden during each state
- Invalid input, errors, retries, and recovery
- Timing, duplicate actions, and concurrent requests
- Data writes, side effects, and what must remain unchanged
- User feedback, boundary cases, and explicit non-goals

Ask for behavior, not implementation ceremony. Inspect repo facts yourself. When a rule needs enforcement, recommend the smallest authoritative guard first: UI state for feedback plus a direct backend/state-transition check when clients could race or bypass the UI. Do not propose locks, queues, new services, wrappers, or retry systems unless a simple guard cannot satisfy the rule.

## Rules

1. Walk each branch of the decision tree. Resolve dependencies — if Q2 depends on Q1's answer, either give options that cover both paths in one batch, or ask Q1's batch first then a follow-up batch.
2. For every optioned question, give your **recommended** answer (marked). When architecture debt is visible and a **behavior-preserving move** is clear (`/architecture` §4), **recommend the move** to **reduce entropy** (`/taste` complexity & entropy) — not "keep where it is."
3. **Batch** per [../asking.md](../asking.md) — do not ask one at a time when several are known.
4. Cover at least (skip only if already settled) — put all unsettled items in the **same** first batch when possible:
   - Exact outcome and non-goals
   - Who it is for / critical edge cases
   - **Language** — domain terms / aliases / named events → upsert `grills/language.md` when locked
   - **Choices** — packages, vendors, storage, auth transport → upsert `grills/choice.md` when locked
   - **App rules** — actors/roles + standing policies → upsert `grills/rules.md` when locked; copy any rule this goal relies on into `GOAL.md` Active Rules
   - **Behavioral rules** — state, timing, availability, error, or side-effect answers → `GOAL.md` Active Rules by default
   - **Taste** — when relevant, read `/taste` and ask about entry shape, errors, naming, verify style; prefer **deep** surfaces over shallow helpers
   - **Architecture** — when multi-file/data/scale, read `/architecture` (or under goal: `/architecture`): which **service** owns the domain, folders, write-path aggregates; when explore found debt, include **move vs leave** with **move** recommended if old behavior can be preserved (**reduce entropy**)
   - **Design** — when UI, read `/design` (or under goal: `/design`) and lock Design-card topics with the user
   - **How many separate plans** the work should become (prefer more small plans)
   - File lanes / what must not be touched
5. Do **not** write `plans/*`, implement feature code, or skip to plans until the closing gates in the batch all pass (goal flow via `/create-plan`). Standalone may stop after themes + shared understanding without a goal workspace.

## Closing

When closing, use [../asking.md](../asking.md) **announce vs ask** — all three closing items are **announce-only**:

1. **Non-goals** — bullet list in **Locked (correct if wrong)**. Do **not** ask yes/no.
2. **Split / plan count** — intended plan titles (or “one plan — …”) in the same Locked block. Prefer more small plans that keep each slice in the AI smart zone. Do **not** ask yes/no.
3. **Shared understanding** — short **summary** of the outcome the agent believes (include planned **Moves / corrections** when locked; briefly restate **new** language / choices / rules and each new Active Rule) in the same Locked block. Do **not** ask yes/no — this is a recap, not a confirm question.

Tick all three when announced. Persist to `GRILL.md` and the goal's Active Rules ledger. On a user correction: revise only those topics, re-announce Locked (plus Questions for any *real* remaining opens). After Locked closing stands (and any co-batched Questions are answered), hand off:

- Structure needed → `/architecture`, then `/goal`
- Ready to build → `/goal`

## Anti-patterns

- Dripping one question per message when multiple opens are known
- Asking yes/no for non-goals, plan split, or shared understanding (announce those)
- Recommending "match the existing (wrong) layout" to avoid disruption when a move preserves behavior
- Treating prior placement as sacred
- Leaving locked language / choices / rules only in chat
- Leaving a locked behavioral answer out of `GOAL.md` Active Rules
- Dumping shared themes into goal `GRILL.md` (themes belong in `grills/`)
- Inventing synonyms in plans/code that contradict `language.md`
- Skipping choices or rules that were decided in the grill

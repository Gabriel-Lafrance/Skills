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

**Both** `/grill-me` and `/grill-me` **upsert** the matching theme file(s) when terms, choices, or rules lock. Append/update lines — do not wipe unrelated prior entries. Prefer exact term match over synonyms. Align code/service names with `language.md` (DDD).

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

## Rules

1. Walk each branch of the decision tree. Resolve dependencies — if Q2 depends on Q1's answer, either give options that cover both paths in one batch, or ask Q1's batch first then a follow-up batch.
2. For every optioned question, give your **recommended** answer (marked). When architecture debt is visible and a **behavior-preserving move** is clear (`/architecture` §4), **recommend the move** to **reduce entropy** (`/taste` complexity & entropy) — not "keep where it is."
3. **Batch** per [../asking.md](../asking.md) — do not ask one at a time when several are known.
4. Cover at least (skip only if already settled) — put all unsettled items in the **same** first batch when possible:
   - Exact outcome and non-goals
   - Who it is for / critical edge cases
   - **Language** — domain terms / aliases / named events → upsert `grills/language.md` when locked
   - **Choices** — packages, vendors, storage, auth transport → upsert `grills/choice.md` when locked
   - **App rules** — actors/roles + policies → upsert `grills/rules.md` when locked
   - **Taste** — when relevant, read `/taste` and ask about entry shape, errors, naming, verify style; prefer **deep** surfaces over shallow helpers
   - **Architecture** — when multi-file/data/scale, read `/architecture` (or under goal: `/architecture`): which **service** owns the domain, folders, write-path aggregates; when explore found debt, include **move vs leave** with **move** recommended if old behavior can be preserved (**reduce entropy**)
   - **Design** — when UI, read `/design` (or under goal: `/design`) and lock Design-card topics with the user
   - **How many separate plans** the work should become (prefer more small plans)
   - File lanes / what must not be touched
5. Do **not** write `plans/*`, implement feature code, or skip to plans until the closing gates in the batch all pass (goal flow via `/create-plan`). Standalone may stop after themes + shared understanding without a goal workspace.

## Closing

Include these **in the same batch** as other open grill questions when you already know them (do not send three separate messages):

1. **Non-goals** — recap → `a) yes` / `b) no — say what to change`
2. **Split / plan count** — titles → `a) yes` / `b) no — …` (if one plan: `One plan is enough?`)
3. **Shared understanding** — short outcome bullets (include planned **Moves / corrections** when locked; briefly restate **new** language / choices / rules so the user confirms) → `a) yes — proceed` / `b) no — …`

On any `b`/`no`: revise only those topics, then send a **follow-up batch** for the unresolved gates (plus any new opens). After all closing gates pass, hand off:

- Structure needed → `/architecture`, then `/goal`
- Ready to build → `/goal`

## Anti-patterns

- Dripping one question per message when multiple opens are known
- Recommending "match the existing (wrong) layout" to avoid disruption when a move preserves behavior
- Treating prior placement as sacred
- Leaving locked language / choices / rules only in chat
- Dumping shared themes into goal `GRILL.md` (themes belong in `grills/`)
- Inventing synonyms in plans/code that contradict `language.md`
- Skipping choices or rules that were decided in the grill

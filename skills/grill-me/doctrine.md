# Grill Me Doctrine

Interview until you and the user share understanding. **Standalone** — for goal workspaces use **`/grill-me-flow`**.

**Pack-wide ask style:** follow [../asking.md](../asking.md) — batch, not drip.

## Rules

1. Walk each branch of the decision tree. Resolve dependencies — if Q2 depends on Q1's answer, either give options that cover both paths in one batch, or ask Q1's batch first then a follow-up batch.
2. For every optioned question, give your **recommended** answer (marked). When architecture debt is visible and a **behavior-preserving move** is clear (`/architecture` §3), **recommend the move** — not "keep where it is."
3. **Batch** per [../asking.md](../asking.md) — do not ask one at a time when several are known.
4. Cover at least (skip only if already settled) — put all unsettled items in the **same** first batch when possible:
   - Exact outcome and non-goals
   - Who it is for / critical edge cases
   - **Taste** — when relevant, read `/taste-flow` and ask about entry shape, errors, naming, verify style
   - **Architecture** — when multi-file/data/scale, read `/architecture` (or under goal: `/architecture-flow`): which **service** owns the domain, folders, write-path aggregates; when explore found debt, include **move vs leave** with **move** recommended if old behavior can be preserved
   - **Design** — when UI, read `/design` (or under goal: `/design-flow`) and lock Design-card topics with the user
   - **How many separate plans** the work should become (prefer more small plans)
   - File lanes / what must not be touched
5. Do **not** write `plans/*`, implement feature code, or skip to `/create-plan` until the closing gates in the batch all pass.

## Closing

Include these **in the same batch** as other open grill questions when you already know them (do not send three separate messages):

1. **Non-goals** — recap → `a) yes` / `b) no — say what to change`
2. **Split / plan count** — titles → `a) yes` / `b) no — …` (if one plan: `One plan is enough?`)
3. **Shared understanding** — short outcome bullets (include planned **Moves / corrections** when locked) → `a) yes — proceed` / `b) no — …`

On any `b`/`no`: revise only those topics, then send a **follow-up batch** for the unresolved gates (plus any new opens). After all closing gates pass, hand off:

- Structure needed → `/architecture`, then `/create-plan` or `/goal`
- Ready to build a loop → `/goal`
- Ready for one plan file → `/create-plan`

## Anti-patterns

- Dripping one question per message when multiple opens are known
- Recommending "match the existing (wrong) layout" to avoid disruption when a move preserves behavior
- Treating prior placement as sacred

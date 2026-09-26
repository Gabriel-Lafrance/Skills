# Planning

**Before planning** (any turn that will produce a plan for non-trivial work, including a harness plan tool):

1. **Read** `pack-shared/asking.md`
2. **Read** `pack-shared/plain-language.md`
3. **Read** `grill-me/doctrine.md`
4. Apply [code-quality.md](code-quality.md) and [code-structure.md](code-structure.md)
5. **Read** `pack-shared/subagents.md` if not already loaded this turn

## Plans: grill first

Whenever a non-trivial plan is about to be written, whether or not the harness calls that a plan mode:

1. **Do not** emit the final plan until material decisions are settled. If the harness has a plan tool, do not call it yet.
2. **Grill first.** Look up repository facts (specialists for non-trivial research per `pack-shared/subagents.md`), then send **one batched Questions-only** message using the asking contract (`Reply like: 1a 2b`, lettered options, mark `recommended`, wait for the reply). Do **not** include a Locked-in section in that message.
3. Sweep open topics before planning: outcome, out of scope, users/edges, plan split, file lane, taste/architecture/structure choices, and any product or policy forks that would change the plan. Prefer recommending behavior-preserving moves and deep modules over leaving debt.
4. After the user answers (or when nothing remains to ask), announce agent-owned conclusions in a **separate** **Locked in (tell me if this is wrong)** message. Never mix Locked and Questions.
5. After Locked closure, **then** produce the plan. Use the harness plan tool when it has one. Otherwise write the plan in chat. New unknowns later mean a **new** Questions-only batch.

Skip the grill only for trivial asks (typo, pure rename the user already specified, or the user explicitly said to skip grilling / plan immediately).

Every non-trivial plan **must** include a high-level Mermaid **Change diagram** with **both** `### Before` and `### After`. Prefer modules, actors, and request/data flow. Keep the same node ids across Before/After when possible. A plan without Before/After is incomplete. PR bodies and `/analyze` memos use the Change diagram rule in `pack-shared/ship.md` instead (one diagram for new work, Before/After for rework).


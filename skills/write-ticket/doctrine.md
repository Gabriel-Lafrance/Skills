# Write Ticket doctrine

Write or refine one Linear or GitHub ticket from as little as one prompt.
This skill is standalone-only, never implements the ticket, and always runs
**flow** `/analyze` to full memo depth before drafting.

**Execution context:** [../pack-shared/execution-context.md](../pack-shared/execution-context.md) · **Ask style:** [../pack-shared/asking.md](../pack-shared/asking.md) · **Templates:** [reference.md](reference.md)

Infer first. Ask only what this file allows. A short “don’t forget this”
note is a valid seed: analyze the repo, write a detailed ticket, and leave
refinement for later.

## Allowed questions

Exactly two situations may produce a Questions batch. Nothing else.

| When | What to ask | Shape |
| --- | --- | --- |
| The seed is **too short** to analyze | One asking-contract batch: what to capture, plus type only if it is still unknowable, plus any missing metadata | Lettered; mark `recommended`; one `Reply like:` row. Include metadata in **this** batch when it is also missing so there is only one wait. |
| The seed is enough, but **priority, assignee, or tracker** was not in the prompt and cannot be inferred | One metadata batch | Same asking contract. Do not ask status (default backlog / todo). Do not ask “write this?”. |

Do **not** ask vision, who, DoD, entrypoints, non-goals, repro, architecture,
or type when those can be inferred from the prompt, an existing ticket, or
`/analyze`. Do not run the old type-specific open grill. Do not invoke full
`/grill-me` (that interview is too wide).

## Too short

The seed is too short when, after the prompt plus a quick repo look, you still
cannot name **an observable outcome, defect, or maintenance ask**.

| Enough | Too short |
| --- | --- |
| “Checkout total ignores tax on the success screen” | “checkout” / “fix auth” / “don’t forget the billing thing” |
| “Bump eslint and fix the CI workflow” | “chores” |
| An existing ticket with a usable body | An empty ticket and a one-word prompt |

A “don’t forget this” **sentence that names an outcome, defect, or maintenance
ask** is enough: skip grill, analyze, write a full ticket. A bare noun is not:
one batch, then analyze.

## Inputs

| Input | Mode |
| --- | --- |
| Linear ID or URL | Read and refine that Linear ticket |
| GitHub issue ID or URL | Read and refine that GitHub issue |
| Rough idea or “don’t forget this” note | Create; infer Linear versus GitHub from the repo and prompt |
| In-chat analysis memo | Reuse it; still run flow `/analyze` if it is shallow or stale |
| Ambiguous number | Prefer the tracker this repo already uses; ask only inside the allowed metadata / too-short batch |

An in-chat analysis memo is not a substitute for a full flow `/analyze` unless
it already has the complete memo shape (evidence, entrypoints, direction,
ownership, touch surface, risks, `/goal` seed when buildable). Rediscover
ticket, repository, PR, and tracker facts from live sources.

## Type and required content

Infer exactly one type from the seed. Announce it Locked. Ask type only inside
the too-short batch when it is still unknowable.

| Type | Use when | Tracker mapping |
| --- | --- | --- |
| Feature | New capability or intentional enhancement | Linear Feature or equivalent; GitHub enhancement/feature label |
| Tweak | Small bounded intentional adjustment | Linear Improvement or Tweak label/type when available; GitHub tweak/improvement label when available |
| Bug | Wrong or broken behavior at normal priority | Linear Bug or equivalent; GitHub bug label |
| Refactor | Structural debt with preserved behavior | Linear Improvement/Refactor or equivalent; GitHub refactor/tech-debt label |
| Chore | Non-product maintenance: deps, CI, tooling, docs-only, repo hygiene | Linear Chore/Improvement or equivalent; GitHub chore/maintenance label when available |
| Hotfix | Urgent production defect that needs expedited shipping | Linear Bug with urgent priority or Hotfix label when available; GitHub bug + urgent/hotfix labels |

| Type | Required on the ticket (fill from prompt + analysis; `unknown` / `_none` when weak) |
| --- | --- |
| Feature | Ask/Vision, Definition of Done, Entrypoints, principle-level Proposed architecture, named Non-goals, Notes |
| Tweak | Ask/Adjustment, Definition of Done, known Entrypoints, named Non-goals, Notes |
| Bug | Who, What, When, Why when known, How/repro, stack trace when available, expected behavior, Notes |
| Refactor | Ask/Why, preserved behavior, Pros, honest Cons, Impact, Definition of Done, Entrypoints, principle-level Proposed architecture, named Non-goals, Notes |
| Chore | Ask/Maintenance, Definition of Done, known Entrypoints, named Non-goals, Notes |
| Hotfix | Who, What, When, Why when known, How/repro, stack trace when available, expected behavior, urgency/blast radius, Notes |

Bug and Hotfix tickets never include Feature or Refactor architecture fields.
Keep Tweak and Chore tickets lean: no Proposed architecture, Pros/Cons, or
Impact unless the user needs that context. Refactor Cons and Impact are
mandatory; label weak evidence and use `unknown` or `N/A` instead of invented
precision. Prefer Hotfix over Bug only when production breakage is urgent.

Feature and Refactor architecture may name placement, reuse versus a new
boundary, moves, deletion of old paths, and one-line reasoning. Cite `/taste`
and `/architecture` in that sketch. Do not prescribe method bodies,
algorithms, signatures, or implementation steps.

## Process

1. **Load or seed.** Read an existing ticket before changing it. For a new
   ticket, start from the user's prompt. Infer type, tracker, priority, and
   assignee when the prompt or roster makes them obvious. Preserve useful
   existing headings.
2. **Thinness gate.** If too short, send the one allowed grill batch and wait.
   If enough, do not grill.
3. **Analyze — always, fully.** Run **flow** `/analyze` on the seed (plus any
   grill answers). Parent brief: complete standard-research memo, Task workers
   per [subagents.md](../pack-shared/subagents.md), no stub, no standalone
   hand-off Questions. Skip `/goal` promotion; ticket writing is the next
   step. Refresh a stale or shallow memo instead of reusing it.
4. **Draft.** Fill the type template from the memo. Entrypoints, DoD, non-goals,
   repro, and architecture sketches come from analysis, not from extra user
   questions. For a capture from a short note, say so in Notes and still write
   the full template.
5. **Metadata.** If priority, assignee, or tracker is still unknown, one
   metadata batch and wait. Default status to backlog / todo; do not ask it.
   Do not ask permission to write.
6. **Write.** Show the complete draft in chat, then create or update through
   the tracker capability or `gh`. Return the URL and applied metadata.

Announce inferred type and the draft as Locked (correct if wrong) only in
messages that have no Questions.

## Failures

| Problem | Action |
| --- | --- |
| No Linear capability | Explain the limitation; do not fake a ticket |
| GitHub tooling unavailable | Ask for install/auth inside the allowed metadata batch, or allow one pasted body for refine only |
| Ticket not found | Stop and confirm ID, team, or repository |
| User declines after write | Leave the URL; do not silently delete |
| Required section empty after analysis | Use `unknown` / `_none` and say so in Notes; do not start a second grill |
| Analysis absent or stubby | Run or refresh full flow `/analyze` before drafting |
| Tracker options unavailable | Ask freeform for that field inside the metadata batch; do not invent IDs |

## Anti-patterns

- Running inside `/goal` or inventing a flow variant
- Skipping flow `/analyze` or accepting a stub memo
- Asking the type-specific open grill, or invoking full `/grill-me`
- Asking vision / who / DoD / entrypoints when analysis can fill them
- Asking “write this?” or status when a default exists
- A second Questions batch after the too-short grill
- Labeling a defect, standalone capability, or structural cleanup as a Tweak
- Labeling urgent production breakage as Bug when Hotfix fits, or routine defects as Hotfix
- Labeling product tweaks, refactors, or defects as Chore
- Writing code-level implementation instructions
- Inventing tracker IDs or fake precision on Cons / Impact
- Writing a one-line stub instead of a detailed ticket

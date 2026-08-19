# Write Ticket doctrine

## Job

Write or refine one Linear or GitHub ticket from as little as one prompt. This skill is a user start, never implements the ticket, and always runs `/analyze` to full memo depth before drafting.

## Owns

Allowed questions, too-short vs enough, inputs, type mapping, required six sections, and failure handling.

## Does not own

- Implementation
- Full `/grill-me`
- Numbered how-to: [`SKILL.md`](SKILL.md)
- Section presets: [`reference.md`](reference.md)

## Cite keys

none (uses `taste:*` and `architecture:*`)

## Bars

**Execution context:** [../pack-shared/execution-context.md](../pack-shared/execution-context.md) · **Ask style:** [../pack-shared/asking.md](../pack-shared/asking.md) · **Templates:** [reference.md](reference.md)

Infer first. Ask only what this file allows. A short “don’t forget this” note is a valid seed: analyze the repo, write a detailed ticket, and leave refinement for later.

### Allowed questions

Exactly two situations may produce a Questions batch. Nothing else.

| When | What to ask | Shape |
| --- | --- | --- |
| The seed is **too short** to analyze | One asking-contract batch: what to capture, plus type only if it is still unknowable, plus any missing metadata | Lettered; mark `recommended`; one `Reply like:` row. Include metadata in **this** batch when it is also missing so there is only one wait. |
| The seed is enough, but **priority, assignee, or tracker** was not in the prompt and cannot be inferred | One metadata batch | Same asking contract. Do not ask status (default **Todo** unless the prompt already names one). Do not ask “write this?”. |

Do **not** ask vision, who, done-when, start-here, out of scope, repro, architecture, or type when those can be inferred from the prompt, an existing ticket, or `/analyze`. Do not run the old type-specific open grill. Do not invoke full `/grill-me` (that interview is too wide).

### Too short

The seed is too short when, after the prompt plus a quick repo look, you still cannot name **an observable outcome, defect, or maintenance ask**.

| Enough | Too short |
| --- | --- |
| “Checkout total ignores tax on the success screen” | “checkout” / “fix auth” / “don’t forget the billing thing” |
| “Bump eslint and fix the CI workflow” | “chores” |
| An existing ticket with a usable body | An empty ticket and a one-word prompt |

A “don’t forget this” **sentence that names an outcome, defect, or maintenance ask** is enough: skip grill, analyze, write a full ticket. A bare noun is not: one batch, then analyze.

### Inputs

| Input | Mode |
| --- | --- |
| Linear ID or URL | Read and refine that Linear ticket |
| GitHub issue ID or URL | Read and refine that GitHub issue |
| Rough idea or “don’t forget this” note | Create; infer Linear versus GitHub from the repo and prompt |
| In-chat analysis memo | Reuse it; still run `/analyze` if it is shallow or stale |
| Ambiguous number | Prefer the tracker this repo already uses; ask only inside the allowed metadata / too-short batch |

An in-chat analysis memo is not a substitute for a full `/analyze` unless it already has the complete memo shape (diagram, evidence, entrypoints, direction, ownership, touch surface, risks, `/goal` seed when buildable). Rediscover ticket, repository, PR, and tracker facts from live sources.

### Type and required content

Infer exactly one type from the seed. Announce it Locked. Ask type only inside the too-short batch when it is still unknowable.

| Type | Use when | Tracker mapping |
| --- | --- | --- |
| Feature | New capability or intentional enhancement | Linear Feature or equivalent; GitHub enhancement/feature label |
| Tweak | Small bounded intentional adjustment | Linear Improvement or Tweak label/type when available; GitHub tweak/improvement label when available |
| Bug | Wrong or broken behavior at normal priority | Linear Bug or equivalent; GitHub bug label |
| Refactor | Structural debt with preserved behavior | Linear Improvement/Refactor or equivalent; GitHub refactor/tech-debt label |
| Chore | Non-product maintenance: deps, CI, tooling, docs-only, repo hygiene | Linear Chore/Improvement or equivalent; GitHub chore/maintenance label when available |
| Hotfix | Urgent production defect that needs expedited shipping | Linear Bug with urgent priority or Hotfix label when available; GitHub bug + urgent/hotfix labels |

Every ticket uses the **same sections**, in this order. Type only changes what you write inside them (presets in [reference.md](reference.md)).

| Section | What it is |
| --- | --- |
| Type | Feature, Tweak, Bug, Refactor, Chore, or Hotfix |
| Diagram | Mermaid that explains the ticket: path, Before/After, or a race sequence |
| Ask | A few plain sentences: what we want, what’s broken, or what to land |
| Done when | Short checks. Bugs include how to see it. |
| Out of scope | What we are not doing. `_none` if there is nothing. |
| Start here | One or two `path` / `symbol` lines, or `_unknown` |

Do not add extra headings (no Who/What/When, stack trace, expected behavior, proposed architecture, pros/cons, or impact boxes). Fold those facts into Ask, Done when, and Diagram. Prefer Hotfix over Bug only when production breakage is urgent. Architecture belongs in the picture; add one sentence in Ask only if the picture is not enough. Do not write method bodies or implementation steps.

When refining an old ticket, map leftover headings into this body. Do not keep the old heading set.

Announce inferred type and the draft as Locked (correct if wrong) only in messages that have no Questions.

## Output

| Problem | Action |
| --- | --- |
| No Linear capability | Explain the limitation; do not fake a ticket |
| GitHub tooling unavailable | Ask for install/auth inside the allowed metadata batch, or allow one pasted body for refine only |
| Ticket not found | Stop and confirm ID, team, or repository |
| User declines after write | Leave the URL; do not silently delete |
| Required section empty after analysis | Use `unknown` / `_none` in that section; do not start a second grill |
| Analysis absent or stubby | Run or refresh full `/analyze` before drafting |
| Tracker options unavailable | Ask freeform for that field inside the metadata batch; do not invent IDs |

## Apply

Always run `/analyze` to full memo depth. Show the complete draft in chat, then create or update through the tracker capability or `gh`. Return the URL and applied metadata. Status is **Todo** unless the prompt already names another; when refining, keep the current status unless the prompt overrides it.

## Anti-patterns

- Running inside `/goal`
- Skipping `/analyze` or accepting a stub memo
- Asking the type-specific open grill, or invoking full `/grill-me`
- Asking vision / who / done-when / start-here when analysis can fill them
- Asking “write this?” or status when a default exists
- Defaulting a new ticket to Backlog instead of Todo
- A second Questions batch after the too-short grill
- Labeling a defect, standalone capability, or structural cleanup as a Tweak
- Labeling urgent production breakage as Bug when Hotfix fits, or routine defects as Hotfix
- Labeling product tweaks, refactors, or defects as Chore
- Writing code-level implementation instructions
- Adding extra headings, or inventing tracker IDs or fake impact numbers
- Writing a one-line stub instead of a detailed ticket
- Dropping the Mermaid diagram, leaving a copy-placeholder, or using a path chart when a race needs a sequence

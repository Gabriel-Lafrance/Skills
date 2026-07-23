# Write Ticket Doctrine

Write or refine one Linear or GitHub ticket. This skill is standalone-only, never runs under `/goal`, and does not implement the ticket. `/trackers` is read-only; `/analyze` researches; this skill owns the approved write.

**Ask style:** [../asking.md](../asking.md). The open ticket grill is the documented exception: numbered freeform questions with no letters or `Reply like:`. Type lock and metadata use the normal lettered contract. Templates: [reference.md](reference.md).

**Subagent model:** omit Task `model` unless the user explicitly asked for one.

## Type and required content

Lock exactly one type before the open grill:

| Type | Use when | Tracker mapping |
| --- | --- | --- |
| Feature | New capability or intentional enhancement | Linear Feature or equivalent; GitHub enhancement/feature label |
| Tweak | Small bounded intentional adjustment; not a defect, standalone capability, or structural cleanup | Linear Improvement or Tweak label/type when available; GitHub tweak/improvement label when available |
| Bug | Wrong or broken behavior | Linear Bug or equivalent; GitHub bug label |
| Refactor | Structural debt without intended behavior change | Linear Improvement/Refactor or equivalent; GitHub refactor/tech-debt label |

| Type | Required before write |
| --- | --- |
| Feature | Ask/Vision, Definition of Done, Entrypoints, principle-level Proposed architecture, explicit Non-goals only when named, Notes |
| Tweak | Ask/Adjustment, Definition of Done, Entrypoints when known, explicit Non-goals only when named, Notes |
| Bug | Who, What, When, Why when known, How/repro, Stack trace when available, expected behavior, Notes |
| Refactor | Ask/Why, preserved behavior, Pros, honest Cons, Impact, Definition of Done, Entrypoints, principle-level Proposed architecture, explicit Non-goals only when named, Notes |

Bug tickets never include Feature or Refactor architecture fields. Tweak tickets stay lean: no Proposed architecture, Pros/Cons, or Impact unless the user explicitly needs that context. Refactor Cons and Impact are mandatory. Estimate Impact honestly, label weak evidence, and use `unknown` or `N/A` rather than invented precision.

## Architecture grain

Feature and Refactor tickets may name placement, reuse versus new services/modules, moves, deletion of old paths, and one-line reasoning. They must not prescribe method bodies, algorithms, signatures, or implementation steps. Those belong in `/goal`.

## Inputs

| Input | Mode |
| --- | --- |
| Linear ID or URL | Refine that Linear ticket |
| GitHub issue ID or URL | Refine that GitHub issue |
| Rough idea or pasted notes | Create; ask Linear versus GitHub once if unclear |
| Ambiguous number | Ask once whether it is Linear or GitHub |

One ticket per run unless the user explicitly names related tickets.

## Process

### 1. Load or seed

- For an existing ticket, discover the relevant Linear or GitHub capability, read it first, and normalize its current body, type, status, priority, and assignee.
- For a new ticket, seed from the user's idea only.
- Authenticate once when needed. If GitHub tooling is unavailable, allow one pasted body for refine or stop for create.
- Never invent an existing ticket body or tracker metadata.
- Preserve useful existing content when refining, and keep required type headings exact so `/goal` and `/trackers` can find them.

### 2. Lock type

Use the type-lock question batch in [reference.md](reference.md) unless the existing ticket makes the type unambiguous. Wait before opening the grill.

### 3. Open grill

Use the type-specific freeform suite in [reference.md](reference.md), skip settled questions, batch known gaps, and wait for answers. Do not ask implementation or step-by-step coding questions.

### 4. Analyze

Run `/analyze` on the grilled brief before drafting. Carry forward its scoped `ANALYSIS.md`; skip its goal-promotion hand-off because ticket writing is the next step. Do not sleep or poll for its workers.

### 5. Propose the solution

- Feature and Refactor: announce a principle-level Locked summary using [reference.md](reference.md). The user may correct it; silence accepts it.
- Tweak: announce the bounded adjustment, expected outcome, known entrypoint, and non-goals; do not inflate it into an architecture proposal.
- Bug: do not put DoD, entrypoints, architecture, Pros/Cons, or Impact in the ticket. Keep useful investigation notes short.

### 6. Draft and lock metadata

Show the complete body from the type template. Discover actual workflow states, priorities, and assignees before offering the metadata question batch. Wait for approval; never silently write.

### 7. Write

On explicit approval only, create or update the ticket body, type/labels, state, priority, and assignee through the tracker capability or `gh`. Return the URL and echo applied metadata.

## Failures

| Problem | Action |
| --- | --- |
| No Linear capability | Explain the limitation; do not fake a ticket |
| GitHub tooling unavailable | Ask for install/auth, or allow one pasted body for refine only |
| Ticket not found | Stop and confirm ID, team, or repository |
| User declines | Leave the draft in chat; do not write |
| Required section missing | Continue the open grill; never write incomplete |
| Analysis skipped | Run `/analyze` before drafting |
| Tracker options unavailable | Ask freeform for that field; do not invent IDs |

## Anti-patterns

- Running inside `/goal` or inventing a flow variant.
- Skipping the open grill or `/analyze`.
- Lettering the freeform grill.
- Labeling a defect, standalone capability, or structural cleanup as a Tweak.
- Writing code-level implementation instructions.
- Inventing Non-goals, tracker values, Pros, Cons, or Impact precision.
- Using Feature/Refactor fields on a Bug.
- Writing before full draft and metadata approval.
- Using `/trackers` to write.

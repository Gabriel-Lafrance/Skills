# Write Ticket doctrine

Write or refine one Linear or GitHub ticket. This skill is standalone-only,
never implements the ticket, and owns a tracker write only after explicit user
approval. `/trackers` is read-only; flow `/analyze` supplies evidence.

**Execution context:** [../pack-shared/execution-context.md](../pack-shared/execution-context.md) · **Ask style:** [../pack-shared/asking.md](../pack-shared/asking.md) · **Templates:** [reference.md](reference.md)

The open ticket grill is the asking-contract exception: use numbered freeform
questions without letters or `Reply like:`. Type and metadata choices use the
normal lettered format.

## Inputs

| Input | Mode |
| --- | --- |
| Linear ID or URL | Read and refine that Linear ticket |
| GitHub issue ID or URL | Read and refine that GitHub issue |
| Rough idea or notes | Create; ask Linear versus GitHub once if unclear |
| In-chat analysis memo | Reuse it as analysis evidence; refresh only stale or missing facts |
| Ambiguous number | Ask once whether it is Linear or GitHub |

An in-chat analysis memo is sufficient. Do not require or create an
agent-owned analysis artifact. Rediscover ticket, repository, PR, and tracker
facts from their live sources; keep user decisions and approvals in the
execution context.

## Type and required content

Lock exactly one type before the open grill:

| Type | Use when | Tracker mapping |
| --- | --- | --- |
| Feature | New capability or intentional enhancement | Linear Feature or equivalent; GitHub enhancement/feature label |
| Tweak | Small bounded intentional adjustment | Linear Improvement or Tweak label/type when available; GitHub tweak/improvement label when available |
| Bug | Wrong or broken behavior at normal priority | Linear Bug or equivalent; GitHub bug label |
| Refactor | Structural debt with preserved behavior | Linear Improvement/Refactor or equivalent; GitHub refactor/tech-debt label |
| Chore | Non-product maintenance: deps, CI, tooling, docs-only, repo hygiene | Linear Chore/Improvement or equivalent; GitHub chore/maintenance label when available |
| Hotfix | Urgent production defect that needs expedited shipping | Linear Bug with urgent priority or Hotfix label when available; GitHub bug + urgent/hotfix labels |

| Type | Required before write |
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
boundary, moves, deletion of old paths, and one-line reasoning. Do not prescribe
method bodies, algorithms, signatures, or implementation steps.

## Process

1. **Load or seed.** Read an existing ticket before changing it; normalize its
   current body, type, status, priority, and assignee. For a new ticket, start
   from the user's idea. Preserve useful content and exact required headings.
2. **Lock type.** Use the type question in [reference.md](reference.md) unless
   the existing ticket makes it unambiguous. Wait for the answer.
3. **Open grill.** Use the type-specific freeform suite, skip settled items,
   batch known gaps, and do not ask step-by-step implementation questions.
4. **Analyze.** Before drafting, obtain an evidence-backed analysis memo in
   chat. Reuse a supplied or current memo; otherwise run **flow** `/analyze` on
   the grilled brief (Task workers per
   [subagents.md](../pack-shared/subagents.md)). If the memo is stale, refresh
   the needed evidence. Skip analysis promotion because ticket writing is the
   next step.
5. **Propose.** For Feature and Refactor, announce the principle-level Locked
   summary. For Tweak, announce the bounded adjustment, outcome, entrypoint,
   and non-goals. For Chore, announce the maintenance ask, outcome, entrypoint,
   and non-goals. For Bug or Hotfix, keep investigation notes short and omit
   unrelated ticket sections; Hotfix must include urgency/blast radius.
6. **Draft and lock metadata.** Show the complete template body. Discover live
   workflow states, priorities, and assignees before asking the metadata batch.
   Wait for explicit approval.
7. **Write.** On approval only, create or update the body, type/labels, state,
   priority, and assignee through the tracker capability or `gh`. Return the
   URL and applied metadata.

## Failures

| Problem | Action |
| --- | --- |
| No Linear capability | Explain the limitation; do not fake a ticket |
| GitHub tooling unavailable | Ask for install/auth, or allow one pasted body for refine only |
| Ticket not found | Stop and confirm ID, team, or repository |
| User declines | Leave the draft in chat; do not write |
| Required section missing | Continue the open grill; never write incomplete |
| Analysis absent or stale | Obtain or refresh the in-chat analysis memo before drafting |
| Tracker options unavailable | Ask freeform for that field; do not invent IDs |

## Anti-patterns

- Running inside `/goal` or inventing a flow variant
- Requiring a hidden analysis path instead of accepting the in-chat memo
- Skipping the open grill or evidence-backed analysis
- Lettering the freeform grill
- Labeling a defect, standalone capability, or structural cleanup as a Tweak
- Labeling urgent production breakage as Bug when Hotfix fits, or routine defects as Hotfix
- Labeling product tweaks, refactors, or defects as Chore
- Writing code-level implementation instructions
- Inventing Non-goals, tracker values, Pros, Cons, or Impact precision
- Writing before full draft and metadata approval

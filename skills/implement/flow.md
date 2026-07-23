# Implement Flow

Build from **one plan file** inside a goal workspace. Follow **`/orchestrate`**.

## Preconditions

1. Resolve **`goal-id`**, `goal_root` per [../pack-shared/workspace-roots.md](../pack-shared/workspace-roots.md), and the plan file (`<goal-root>/plans/NN-*.md` or frontier from `<goal-root>/plans/INDEX.md`)
2. Read `<goal-root>/GOAL.md` Active Rules, `<goal-root>/GRILL.md` (if any), that plan file, `<goal-root>/plans/INDEX.md`, and `.agents/temp/grills/{language,choice,rules}.md` when present
3. `/taste` (+ `/design` if UI); ticket brief via `/trackers` if needed
4. Scoped REGISTRY: serialize if another running goal in `goals_container` shares File lane

## Process

1. Structure/design gaps → update **this** plan via `/architecture` / `/design` only when needed to meet its Active Rules or acceptance criteria. Do not use a bounded plan as a reason to reopen unrelated cleanup.
2. Dispatch `generalPurpose` for this plan with the main-agent-authored Worker Brief from `/orchestrate` (parallel only when briefs prove non-overlapping lanes and compatible interfaces). **Omit Task `model`** — inherit parent. If the plan’s Structure lists a required move, do the behavior-preserving move first. Name types/functions with `language.md` terms; honor `choice.md`, `rules.md`, and the Active Rules. Uncertain about behavior → `/grill-me` batch-ask; report a new abstraction or shared-seam need to the orchestrator rather than improvising it.
3. Integrate only after checking the worker's invariant status, files changed, interface/handoff, and blockers against the full goal; then mark INDEX row status
4. Taste check; verify via **existing terminals** (`/taste` Verify) — **no** Convex MCP ritual; after a move, confirm old observable behavior still holds
5. Bugs mid-slice → **`/repair`** → **`/validate`**. Misplaced architecture → Structure move / plan update, not a patch that hardens the wrong place
6. When **all** frontier workers for this wave are done → **`/validate`** (includes cross-plan seams when INDEX has 2+ plans) → then `/code-review` — prefer terminals over MCP
7. No tracker close here; commit only if asked

## Notes

- Paths: `<goal-root>/…` only
- One plan file per Worker Brief; worker must end with invariant status plus `## Progress` (`/orchestrate`)
- Never write another goal-id’s tree
- Prior mistakes in-lane are not sacred — `/architecture` doctrine
- **Never write or edit test files** — only `/create-test` (after `/code-review` or `/pr-review` recommends); do not invent coverage while implementing

## Abstraction budget

Keep a local guard inline when it has one local call site and one clear purpose. Extract only when the extraction owns independent behavior, removes real duplication, or is required to enforce a locked Active Rule.

Before adding a new layer, file, service, abstraction, queue/lock/retry system, or shared API, show evidence that the existing local shape cannot meet the assigned invariant or acceptance criterion. A disabled UI state is feedback; when clients can bypass it, prefer a direct authoritative backend/state-transition guard before coordination machinery.

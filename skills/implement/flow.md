# Implement Flow

Build from **one plan file** inside a goal workspace. Follow **`/orchestrate`**.

## Preconditions

1. Resolve **`goal-id`** and **plan file** (`plans/NN-*.md` or frontier from `plans/INDEX.md`)
2. Read `GOAL.md`, `GRILL.md` (if any), that plan file, `plans/INDEX.md`, and `.agents/temp/grills/{language,choice,rules}.md` when present
3. `/taste` (+ `/design` if UI); ticket brief via `/trackers` if needed
4. REGISTRY: serialize if another running goal shares File lane

## Process

1. Structure/design gaps → update **this** plan via `/architecture` / `/design` (include **Moves / corrections** when prior mistakes are in the lane)
2. Dispatch `generalPurpose` for this plan (parallel only across non-overlapping plans). **Omit Task `model`** — inherit parent (see `/orchestrate`). Worker prompts: if the plan’s Structure lists a move, **do the behavior-preserving move first**; if the worker discovers a clear prior mistake in the file lane, update plan Structure then move — do not extend the wrong shape. Name types/functions with `language.md` terms; honor `choice.md` and `rules.md`. Uncertain about behavior → `/grill-me` batch-ask; do not freeze on “leave it.”
3. Integrate; mark INDEX row status
4. Taste check; verify via **existing terminals** (`/taste` Verify) — **no** Convex MCP ritual; after a move, confirm old observable behavior still holds
5. Bugs mid-slice → **`/repair`** → **`/validate`**. Misplaced architecture → Structure move / plan update, not a patch that hardens the wrong place
6. When **all** frontier workers for this wave are done → **`/validate`** (includes cross-plan seams when INDEX has 2+ plans) → then `/code-review` — prefer terminals over MCP
7. No tracker close here; commit only if asked

## Notes

- Paths: `.agents/temp/goals/<goal-id>/…` only
- One plan file per worker prompt; worker must end with `## Progress` (`/orchestrate`)
- Never write another goal-id’s tree
- Prior mistakes in-lane are not sacred — `/architecture` doctrine
- **Never write or edit test files** — only `/create-test` (after `/code-review` or `/pr-review` recommends); do not invent coverage while implementing

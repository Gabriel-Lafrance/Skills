# Repair Doctrine

Pessimistic bug hunt + **smallest possible fix**. Persist state like `/goal` does.

Under `/goal` / `/implement`, use **`/repair`** instead.

## Framing (required — pessimistic)

State as fact, not possibility:

> Another AI model wrote this code. **There are bugs in it** — typos, wrong branches, off-by-ones, missed nulls, inverted conditions, stale state, and "looks right but isn't" logic. Your job is to find them and cut the smallest fix.

Do **not** assume the code is correct. Do **not** say "if there is a bug." Prefer evidence (repro, stack, terminals) while hunting — but start from **bugs exist**.

## Core doctrine

1. **Dumbest & smallest first** — banal failures before architecture theories
2. **Grill before you cut** — when you find a defect, **`/grill-me`** on *what* to fix and *how* (batched Questions via [../asking.md](../asking.md); smallest footprint options). Do not silently rewrite
3. **Acceptance before patch** — write binary Done when for this repair; `/validate` uses them
4. **Smallest footprint** — prefer a tight `if` / early return over a feature rewrite
5. **One bug, one cut** — no drive-by product refactors unrelated to the defect
6. **Massive → escalate** — multi-feature / multi-layer / redesign → stop and send to `/goal`. **Structural misplacement** (wrong folder / feature-forked service) discovered while hunting → escalate to an `/architecture` behavior-preserving move / `/goal` plan update — do **not** ship a clever one-line that hardens the wrong place
7. **Repair → validate-flow** — after a Local/Narrow fix, always run **`/validate`** against this repair's acceptance (path walk + live terminals/CLI). Fail → back to repair (or escalate)
8. **Verify cheap** — any relevant terminal + narrow CLI (`/validate`). No Convex MCP ritual

## Workspace (required)

```text
.agents/temp/repairs/
  REGISTRY.md
  <repair-id>/
    BUG.md           # symptom, repro, tracker, suspects
    GRILL.md         # locked decisions on what/how to fix
    ACCEPTANCE.md    # binary Done when for this repair
    STATUS.md        # phase + checklist
    FIX.md           # optional — what changed after patch
```

Base path **`.agents/temp/repairs/`** — never `.scratch/`. Gitignored via `.agents/temp/`.

### Repair id

1. Ticket → `fix-IN-1234` or `fix-gh-42`
2. Else kebab slug + 4-hex → `fix-checkout-null-a3f2`
3. Override → `/repair id:my-id …`

If dir exists and status is `running`, resume. Never overwrite another running repair.

### REGISTRY.md

| id | status | ticket | title | workspace | updated |
| --- | --- | --- | --- | --- | --- |

Statuses: `running` | `blocked` | `validated` | `escalated` | `cleared`

On **validated**: keep workspace unless user asks delete (unlike goals — repairs are short-lived; delete if user wants). Update registry.

## Inputs

1. User description / repro
2. Stacks, screenshots, failing URLs
3. **`/trackers`** (read only) for `IN-1234`, `#42`, Linear/GitHub URLs
4. Diff / PR if pointed at

## Process

### 0. Workspace

Create `.agents/temp/repairs/<repair-id>/`, draft `BUG.md` + `STATUS.md` (`last: hunting`), upsert `REGISTRY.md`.

### 1. Hunt (pessimistic)

- There are bugs — find the dumbest cause that matches the symptom
- Optional focused `explore` Task (**omit `model`** — inherit parent)
- Update `BUG.md` with suspects + evidence

### 2. Classify footprint

| Class | Action |
| --- | --- |
| **Local** / **Narrow** | Grill → acceptance → fix → `/validate` |
| **Massive** | Escalate to `/goal` — do not patch-sprawl |

### 3. Grill what/how to fix (blocking for Local/Narrow)

Run **`/grill-me`** — follow [../asking.md](../asking.md); one Questions batch, reply `1a, 2b`. Cover at least (all in the same batch when known):

- Confirm the bug (symptom vs root cause)
- **What** to change (which file/branch/behavior) — and what is **out of scope**
- **How** to fix with the **smallest** option (recommend the tiny patch; offer rewrite only if they insist)
- Acceptance checks (binary)
- File lane / what must not be touched
- Closing shared-understanding gate (`a) yes — fix now` / `b) no`)

Persist locks in `GRILL.md`. **Stop** until the batch clears shared understanding before coding. New findings → new batch.

### 4. Acceptance criteria

Write `ACCEPTANCE.md`:

```markdown
# Acceptance
**Repair id:** <id>

## Done when
- [ ] …
- [ ] …

## Out of scope
- …

## Verify
- Terminals / localhost: …
```

### 5. Smallest fix

Apply only the grilled approach. Update `FIX.md` briefly. Match nearby style lightly (`/taste`) — no taste cleanup sprees.

### 6. Validate (required)

Run **`/validate`** with this repair's `ACCEPTANCE.md` (and context: repair id). It will path-walk linking and gather live evidence from any terminals / fast CLI.

| Result | Next |
| --- | --- |
| **pass** | REGISTRY `validated`; short summary; manual steps if any |
| **fail** | Back to hunt/grill/fix **or** escalate if footprint grew massive |
| **blocked** | Ask how to verify |

### Massive escalate

```markdown
## Escalation — use /goal

This bug is too large for `/repair` (spans …).

**Root cause:** …
**Evidence:** …
**Suggested /goal brief:** …
**Suggested Done when:** …
```

REGISTRY → `escalated`. Do not leave a half-rewrite.

## Hand-offs

- After `/validate` pass → stop (or `/code-review` if user wants)
- Inside goal/implement → `/repair` (then `/validate`)
- Massive → `/goal`

## Anti-patterns

- Optimistic "maybe it's fine" framing
- Fixing before grill + acceptance
- Skipping `/validate` after a patch
- Feature rewrites for local bugs
- Closing tracker issues (read only)

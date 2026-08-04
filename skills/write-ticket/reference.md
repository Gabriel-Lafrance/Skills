# Write Ticket Reference

Load when asking ticket questions, announcing a solution, drafting a body, or writing metadata.

## Type lock

```markdown
## Questions
Reply like: 1a

1. Ticket type?
   - a) Feature ← recommended when this is a new or enhanced capability
   - b) Tweak ← recommended when this is a small intentional adjustment, not a defect or standalone capability
   - c) Bug ← recommended when this is broken or wrong behavior at normal priority
   - d) Refactor ← recommended when this moves or cleans up debt without new behavior
   - e) Chore ← recommended when this is non-product maintenance (deps, CI, tooling, docs)
   - f) Hotfix ← recommended when this is an urgent production defect
```

## Open grill suites

These are numbered freeform questions. Do not add letters or `Reply like:`.

### Feature

```markdown
## Questions (open — reply with short answers per number)

1. What is the vision or goal in one or two sentences?
2. Who is this for?
3. What should happen in the key moments?
4. What must we not do? Say “none” if there is nothing.
5. What else would materially change this ticket if wrong?
```

### Tweak

```markdown
## Questions (open — reply with short answers per number)

1. What small adjustment should change?
2. Who uses it, or which screen, path, or setting does it affect?
3. What should be true after the adjustment?
4. What must stay unchanged or remain out of scope?
5. Which file, route, or surface is involved, if known?
6. Anything else that would make this no longer a small tweak?
```

### Bug

```markdown
## Questions (open — reply with short answers per number)

1. Who hit this?
2. What broke or what did they see?
3. When does it happen?
4. Why does it matter? Say “unknown” if needed.
5. How do you reproduce it?
6. Do you have a stack trace or error text?
7. What should happen if it worked?
8. Anything else useful?
```

### Refactor

```markdown
## Questions (open — reply with short answers per number)

1. Why refactor? What is wrong with the current shape?
2. What must keep working the same?
3. Which files or symbols are involved, if known?
4. Which tradeoffs worry you?
5. What must we not do? Say “none” if there is nothing.
6. Anything else?
```

### Chore

```markdown
## Questions (open — reply with short answers per number)

1. What maintenance should land?
2. Which tooling, CI, deps, docs, or repo surface does it affect?
3. What should be true after the chore?
4. What must stay unchanged or remain out of scope?
5. Which file, config, or workflow is involved, if known?
6. Anything else that would make this a product change instead of a chore?
```

### Hotfix

```markdown
## Questions (open — reply with short answers per number)

1. Who is hit in production?
2. What broke or what are they seeing?
3. When did it start, and how urgent is it?
4. Why does it matter / what is the blast radius? Say “unknown” if needed.
5. How do you reproduce it?
6. Do you have a stack trace or error text?
7. What should happen if it worked?
8. Anything else useful?
```

## Locked solution summaries

### Feature

```markdown
## Locked (correct if wrong)
**Vision:** …
**Definition of Done (outline):** …
**Entrypoints:** `path` — `symbol` · …
**Proposed architecture:** … (placement / reuse versus new service)
**Non-goals:** … | _none_
```

### Refactor

```markdown
## Locked (correct if wrong)
**Why:** …
**What must not change:** …
**Pros:** …
**Cons:** … (real costs)
**Impact:**
- **LoC** — affected: … · deleted: … · improved: …
- **Performance** — roundtrips: … · time: … · compute: …
- **Architecture** — structural: … · complexity: … · overhead: …
**Definition of Done (outline):** …
**Entrypoints:** `path` — `symbol` · …
**Proposed architecture:** … (target shape / move / delete old path)
**Non-goals:** … | _none_
```

### Tweak

```markdown
## Locked (correct if wrong)
**Adjustment:** …
**Expected outcome:** …
**Entrypoints:** `path` — `symbol` | _unknown_
**Non-goals:** … | _none_
```

### Chore

```markdown
## Locked (correct if wrong)
**Maintenance:** …
**Expected outcome:** …
**Entrypoints:** `path` — `symbol` | _unknown_
**Non-goals:** … | _none_
```

### Hotfix

```markdown
## Locked (correct if wrong)
**Who / What / When:** …
**Urgency / blast radius:** …
**Expected behavior:** …
**Repro:** … | _unknown_
```

## Metadata approval

```markdown
## Questions
Reply like: 1a 2a 3c 4a

1. Draft ready for `<ID or NEW>`. Write this to Linear or GitHub?
   - a) yes ← recommended
   - b) no — say what to edit
2. Status?
   - a) <tracker backlog / todo / triage state> ← recommended for create
   - b) <in progress / started>
   - c) Keep current ← recommended when refining and status is fine
   - d) Other — say which state
3. Priority?
   - a) No priority or unset
   - b) Low
   - c) Medium ← recommended unless urgency is clear
   - d) High
   - e) Urgent
   - f) Keep current ← when refining
4. Assignee?
   - a) Unassigned ← recommended unless someone owns it
   - b) <current user if known>
   - c) <teammate from tracker roster>
   - d) Keep current ← when refining
   - e) Other — say who
```

Discover real options before asking: Linear states, priorities, and members come from its capability; GitHub uses open state and actual labels/collaborators.

## Refactor impact fields

| Pillar | Required sub-fields |
| --- | --- |
| Lines of code | Affected, Deleted, Improved |
| Performance | Roundtrips, Time, Compute |
| Architecture | Structural change, Complexity, Overhead |

Every field gets an estimate and short note.

## Ticket bodies

### Feature

```markdown
## Type
Feature

## Ask / Vision
<plain-language goal>

## Definition of Done
- Expected: …
- [ ] …

## Entrypoints
- `path/to/file` — `functionOrSymbol` — why this is the start

## Proposed architecture
- … (placement, reuse, or new service/module)
- Why: …

## Non-goals
- … (omit heading if none)

## Notes
- …
```

### Tweak

```markdown
## Type
Tweak

## Ask / Adjustment
<small intentional change>

## Definition of Done
- Expected: …
- [ ] …

## Entrypoints
- `path/to/file` — `functionOrSymbol` — why this surface changes
(omit heading if unknown)

## Non-goals
- … (omit heading if none)

## Notes
- …
```

### Bug

```markdown
## Type
Bug

## Who
…

## What
…

## When
…

## Why
… (omit heading if unknown)

## How
1. …
2. …

## Stack trace
… (omit heading if none)

## What should happen if it worked
…

## Notes
- …
```

### Refactor

```markdown
## Type
Refactor

## Ask / Why
<plain-language why the shape must change>

## What must not change
- …

## Pros
- …

## Cons
- … (real costs or risks)

## Impact

### Lines of code
- **Affected:** … — note: …
- **Deleted:** … — note: …
- **Improved:** … — note: …

### Performance
- **Roundtrips:** … — note: …
- **Time:** … — note: …
- **Compute:** … — note: …

### Architecture
- **Structural change:** … — note: …
- **Complexity:** … — note: …
- **Overhead:** … — note: …

## Definition of Done
- Structural: …
- Behavior still holds: …
- [ ] …

## Entrypoints
- `path/to/file` — `functionOrSymbol` — why this is in the lane

## Proposed architecture
- … (target shape / service / modules / old path removal)
- Why: …

## Non-goals
- … (omit heading if none)

## Notes
- …
```

### Chore

```markdown
## Type
Chore

## Ask / Maintenance
<non-product maintenance work>

## Definition of Done
- Expected: …
- [ ] …

## Entrypoints
- `path/to/file` — `functionOrSymbol` — why this surface changes
(omit heading if unknown)

## Non-goals
- … (omit heading if none)

## Notes
- …
```

### Hotfix

```markdown
## Type
Hotfix

## Who
…

## What
…

## When
…

## Why
… (omit heading if unknown)

## Urgency / blast radius
…

## How
1. …
2. …

## Stack trace
… (omit heading if none)

## What should happen if it worked
…

## Notes
- …
```

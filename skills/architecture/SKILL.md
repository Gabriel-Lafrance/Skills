---
name: architecture
description: >-
  Shape scalable code: simple entry points, clear folders, and write-path data
  design (store aggregates on write — never recompute metrics on every render or
  read). Agents may auto-invoke. Use before or during planning/implementation
  when adding features, splitting logic, designing data/reads, or when about to
  dump files or scan-on-read. Public skill — users and agents may call this.
  Under /goal use /architecture-flow.
---

# Architecture

Quality code here means: **callers see a small surface; complexity lives behind it; files live in folders that match the domain; data stays cheap to read as the product grows.**

Read **`/taste-flow`** first (and [../taste-flow/examples.md](../taste-flow/examples.md) when unsure). For architecture good/bad pairs, see [examples.md](examples.md). Taste owns naming, errors, nesting, and file rules — this skill owns the structure card **and scalability**.

Inside a `/goal` workspace, use **`/architecture-flow`** instead of this skill.

This skill is the structural gate. Run it before `/create-plan` when structure or data shape matters, or mid-implement when the diff is about to sprawl or recompute on read.

**Explore via subagents** when useful: parallel `explore` Tasks for sibling features and target folders; you write the structure card from their reports.

## Doctrine

### 1. One simple entry point

Hide messy orchestration behind **one** thing the caller uses:

| Shape | When |
| --- | --- |
| React hook (`useX`) | UI state/effects/subscriptions |
| Class / abstract class | Stateful domain behavior, shared lifecycle |
| Facade / service module | Multi-step workflows, external I/O |
| Narrow function API | Pure transforms with a clear input→output |

Rules:

- The entry point's signature should be obvious in one glance
- Call sites should not know about helpers, parsers, adapters, or edge-case branches
- Prefer **throw + try/catch** at boundaries over `{ success: false }` return bags (see `/taste-flow`)
- One main export / one main type per file when practical
- Prefer **class** for stateful domain behavior; hooks for React; facade for multi-step I/O — details in `/taste-flow`

The entry point is not always a TypeScript `interface`. Pick the shape that fits the stack.

### 2. Folders before files

Never sprinkle related files across a flat directory. **Propose the folder map before creating files.**

1. Mirror existing repo conventions (feature folder, domain folder, layer folder) — explore first
2. If no convention fits, create a **feature/domain folder** and put the cluster inside it
3. Colocate what changes together; separate what changes for different reasons
4. Name files per **`/taste-flow`** — `lowercase-with-hyphens` in app/UI; **no `-` or `_` in `convex/` filenames**
5. Avoid `utils.ts` / `helpers.ts` dumping grounds — name the concept
6. Cite a sibling feature when one exists (taste: cite-a-sibling)

Anti-pattern: five new sibling files next to unrelated code with no folder.

### 3. Small collaborating parts

Inside the folder, split by responsibility:

```text
feature-name/
  use-feature-name.ts      # or feature-name.ts — the simple entry
  feature-name-store.ts    # state
  feature-name-api.ts      # I/O
  feature-name-types.ts    # types only if shared
  components/              # UI pieces if needed (one component per file)
```

Convex modules live under `convex/` with **taste naming** (`orders.ts`, not `order-actions.ts`).

Adjust names to the repo. Keep depth shallow: entry → a few collaborators → leaf helpers. Never-nest deep control flow; extract instead.

### 4. Scalable by default (critical — AI often gets this wrong)

**Reads must stay cheap as data grows.** Prefer **compute on write**, store the result, read it later.

#### Metrics, counts, aggregates

| Bad (does not scale) | Good (scales) |
| --- | --- |
| On every render/query: scan all rows and sum/average/count | Store `total`, `count`, `avg`, etc. on a parent row, summary table, or dedicated columns |
| Dashboard that maps every event into charts client-side | Pre-aggregate on insert/update; UI reads the summary |
| `collect()` then reduce in TS for hot paths | Indexed query of stored aggregates / summary docs |

**Rule:** if a value is shown often and derived from many child records, **persist it** and **update it in the same write** that changes the children (insert / patch / delete). Do not recalculate from scratch on each read unless the dataset is provably tiny and bounded.

#### Write-path updates

When inserting or updating a child:

1. Write the child record
2. **In the same mutation/transaction**, bump/recompute the stored aggregate on the parent or summary row
3. Reads only fetch the stored fields

Example shape (conceptual):

```text
orders: { … }
users: { orderCount, orderTotalCents, … }  // updated when an order is inserted
```

Not: `listOrders(userId)` → sum in the React tree or in a query every time.

#### Other scale rules

- **Index** fields you filter/sort by (Convex: `.withIndex`, not `.filter` scans)
- Avoid unbounded `.collect()` on growing tables — paginate or aggregate
- Don’t N+1: batch or denormalize fields needed for list views
- Client components should display data, not be the analytics engine
- Expensive derived views → materialize (table/columns/summary doc), not “calculate on render”

If a one-off admin script needs a full scan, say so explicitly — never copy that pattern into hot product paths.

## Process

### 1. Explore

Read nearby folders. Note:

- How similar features are structured
- Existing entry-point patterns (hooks vs classes vs modules)
- Naming and import style
- Whether siblings store aggregates on write or recompute on read (prefer the former)

### 2. Draft the structure card

Present this before writing code (and include it in `/create-plan` when planning):

```markdown
## Structure

**Entry point:** `path` — `useX` | `ClassX` | `facade` | `fn` — one-line contract
**Hidden behind it:** bullet list of responsibilities callers must not see
**Extension seam (if big feature):** foundation from day one — how the next variant plugs in without breaking the entry (ship seam + first impl together)
**Scalability:**
- Hot reads: <what the UI/query returns>
- Stored on write: <columns / summary table / parent fields updated on insert>
- Indexes: <index names / fields>
- Explicitly NOT recomputed on render/read: <metrics>
**Folder map:**
- `path/to/folder/`
  - `entry-file`
  - `collaborator-a`
  - `collaborator-b`
**Fits existing pattern:** yes (cite example) | new (why)
**Taste:** follows `/taste-flow` naming + entry shape + ≤2 class/interface depth
```

Ask one question only if the entry shape, folder root, or write-vs-read tradeoff is a real decision.

### 3. Implement against the card

- Create the folder first, then files
- Wire collaborators so the entry point is the only thing most call sites import
- Do not export internals unless another package truly needs them
- Implement aggregate updates on the **write path** when the card says so

### 4. Self-check before done

- [ ] A new reader can use the feature from the entry point alone
- [ ] Related new files share one folder (or an existing convention)
- [ ] No flat file dump / no anonymous `utils` bag
- [ ] Complexity is inside collaborators, not at every call site
- [ ] `/taste-flow` naming and error style respected
- [ ] No hot-path “compute metrics on render/read” — aggregates stored and updated on write
- [ ] Indexes cover the queries; no unbounded collect on growing data

## When `/create-plan` or `/implement-flow` should invoke this

- New feature with more than one new file
- Extracting logic from a large file
- Adding React state/effects that would otherwise bloat a component
- Any change that would add files without a parent folder
- Any feature with lists, dashboards, counts, totals, leaderboards, or “stats”
- Any query that would scan children to answer a parent-level question

Hand off: structure card → `/create-plan` (if not approved) → implement. `/validate-flow` will fail scale anti-patterns under `/goal`. Under `/goal` → `/architecture-flow` → `/create-plan-flow`.

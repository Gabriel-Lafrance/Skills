# Code structure

Cite keys use the `architecture:` prefix.

These rules apply on every non-trivial change, whether or not anyone invoked `/architecture`. Examples are in `architecture/examples.md`.

## Services

A **service** is the code about one domain concern (auth, billing, notifications, search). It exposes a **small public API** of callable functions (or a class/facade with methods). Features **use** the service; they do **not** reimplement that domain.

| Concept | Rule |
| --- | --- |
| **Service** | One concern (billing, auth). Owns the how |
| **Public API** | Named operations features call, for example `makeUserPay()`, `requireUser()`, `sendReceipt()` |
| **Feature** | Product slice that orchestrates services + its own UI/state. Never copies billing/auth internals |

- **Explore for an existing service first.** Extend its public API before inventing a parallel one. Explore existing environment variables the same way (`taste:reuse-env`): reuse `SITE_URL`; do not invent `FRONTEND_URL`.
- If the concern is a genuinely independent domain capability or the goal explicitly plans growth, create the service (folder + public entry) and have the feature call it. For bounded local behavior, keep the smallest direct shape until it has independent ownership, real duplication, or a locked rule that needs a boundary.
- Features import **only** the service's public surface. Stripe/SDK/DB helpers stay behind that surface.
- Name public functions as **verbs the product understands** (`makeUserPay`, not `runStripeCheckoutSessionHelper`).
- Prefer throw + try/catch at service boundaries (`taste:throw-at-boundaries`), not `{ success: false }` bags.
- One service is not one giant file: public entry + collaborators / primitives inside the service folder.
- Public writes check identity and ownership in the service (`architecture:authority`). Features may disable UI; they do not own the lock.

Anti-patterns: checkout, upgrade, and invoices each implementing their own Stripe path; “just this once” copy of service logic into a feature; features importing service internals (`billing-stripe`); a `utils/payments.ts` dumping ground with no public contract.

Folder tree: `architecture:collaborating-parts`.

## Deep public surface

Hide messy orchestration behind **one deep** thing the caller uses: simple interface, rich functionality. For a domain concern, that entry **is the service's public API**. For UI, it is usually a hook that **calls** services.

| Shape | When |
| --- | --- |
| **Service** (module / class / facade) | Domain capability shared across features (default for auth, billing) |
| React hook (`useX`) | UI state/effects/subscriptions. Delegates domain work to services |
| Class / abstract class | Stateful domain behavior, shared lifecycle (often *is* the service) |
| Narrow function API | Pure transforms with a clear input→output |

- The entry point's signature should be obvious in one glance
- Call sites should not know about helpers, parsers, adapters, or edge-case branches
- One main export / one main type per file when practical (`taste:one-export-per-file`)
- Prefer class for stateful domain behavior; hooks for React; service for shared domain I/O
- Pull complexity **down** into collaborators and primitives; keep the public surface deep

The entry point is not always a TypeScript `interface`. Pick the shape that fits the stack.

Anti-pattern: **shallow modules** (complex interface relative to what they do: many params/options/leaked steps, callers still orchestrate the how).

## Primitives

A **primitive** is a **small piece of code** that is **strong yet flexible** and answers **one very specific thing**. It can be **reused independently without breaking**. Primitives are the strong blocks inside services and deep modules.

| Property | Meaning |
| --- | --- |
| **Small** | Narrow scope: not a feature, not a god module |
| **One specific job** | Answers one question / does one thing well |
| **Strong** | Deep enough that callers do not reimplement that job |
| **Flexible** | Composes / chains; reuse does not force brittle coupling |
| **Independent reuse** | Call sites can use it without breaking it or each other |
| **Placement** | Lives **inside** services and deep modules: building blocks of those, not a rival top-level architecture |

The deep public surface is what callers see. Primitives are how that depth stays real without leaking every concern to every call site.

1. Prefer building with primitives over duplicating that job at call sites.
2. Explore first: reuse an existing primitive when it already answers that specific thing.
3. When creating one: keep it small, one job, strong yet flexible, safe to reuse independently.
4. Place it inside the owning service / deep module (or a shared layer those modules compose), not a dumping-ground `utils`.
5. Do not fork a primitive's job in a feature or sibling helper.
6. Reason from this definition. Discover primitives by exploring **this** repo. Do not invent a canned catalog from training data.

Anti-patterns: forking a primitive's job locally; thin identity wrappers that only rename with no strength; sprawling helpers that answer many things; promoting primitives to a parallel top-level architecture that rivals services.

## Prior mistakes

Flawed existing layout is **debt**, not a template. Do not freeze wrong placements because they were already there. Leaving or copying wrong placement is entropy growth (`taste:leave-it-cleaner`).

When explore shows a wrong folder, duplicated domain logic, a feature-forked service, or a sibling that violates these rules, first decide whether the active goal or a named review finding requires a move:

- **Do not copy it.** Cite a *good* sibling or service, or create the correct shape.
- If required, prefer a **behavior-preserving move**: relocate into the right service/folder, extract the public API, rewire callers, delete the dead path. This reduces entropy. If not required, capture it as a follow-up rather than expanding the goal.
- Name the old observable behavior and how you will prove it still holds (existing tests if any, path walk + acceptance evidence / terminals). A new lock waits for a user-accepted `/create-test` brief: a `/task` suggestion after grill Locked, or a recommendation from `/review`. If you cannot be sure the move preserves behavior, include the move in the next `/grill-me` Questions batch. If the move is required and you can preserve behavior, do it; otherwise keep it as a follow-up.
- Update the Structure card (**Moves / corrections**) before coding; mid-implement, patch the plan Structure, then move.
- Same spirit as `/review` simplification: apply it while **building**, not only at review time.

Anti-patterns: bolting new code onto a known-wrong shape because it was already there; copying a bad sibling to stay consistent with debt; asking “leave it where it is?” as the recommended option when a clear move preserves behavior.

## Folders

**Nest related files in a named folder.** That is how the tree stays maintainable. A mixed flat directory is a messy codebase. Keep-it-simple (KISS) and never-nest (guard clauses) do **not** authorize a flat dump: never-nest flattens *control flow*, not the filesystem (`taste:never-nest`).

**Create the owning folder before the files.** Propose the folder map first. A new concern gets a folder **even when it starts as one file**. Do not wait until five siblings already exist.

1. Mirror existing repo conventions (services folder, feature folder, domain folder). Explore first. A **good nested sibling** wins over a nearby flat dump (`taste:cite-a-sibling`). A nearby flat dump is debt (`architecture:prior-mistakes`), not a template.
2. Prefer **`services/<concern>/`** (or the repo's equivalent) for shared domain APIs; **feature folders** for product UI/orchestration that *calls* those services.
3. If no convention fits, create a **feature/domain folder** and put the cluster inside it.
4. Colocate what changes together; nest collaborators one level down (`components/`, `hooks/`, private helpers) when they are not the public entry. Separate what changes for different reasons.
5. Name files per `taste:naming-files`.
6. Avoid `utils.ts` / `helpers.ts` dumping grounds. Name the concept (often: promote to a service, or a primitive inside one).
7. **Convex:** a one-file concern may stay `convex/billing.ts` when that is the repo pattern. A second file for that concern **moves the cluster** into `convex/billing/` (do not add `billingStripe.ts` as a `convex/`-root sibling). Do not keep both `convex/billing.ts` and `convex/billing/`.
8. **App Router:** `page.tsx` / `layout.tsx` / `route.ts` stay at the route folder. Other files for that slice nest in that folder (`components/`, `hooks/`) or a feature folder, not as mixed siblings of unrelated routes.

Leave at the repo root only files that belong there (`package.json`, `tsconfig.json`, `docs/design.md`). Patching an existing file in an already-correct folder does not require a new folder.

Anti-patterns: new related files as siblings in `src/`, `app/`, `convex/`, or any mixed parent; treating `taste:never-nest` or `taste:keep-it-simple` as “don’t make a folder”; waiting until the directory is already messy before nesting; a new payments helper beside a feature when a billing service should own it.

## Collaborating parts

Inside the folder, split by responsibility: public entry, then primitives and collaborators.

```text
services/billing/
  billing.ts            # public API: makeUserPay, refundPayment. Only export features import
  billing-stripe.ts     # private
  billing-types.ts
features/checkout/      # UI + orchestration. Calls makeUserPay
  use-checkout.ts
  checkout-types.ts
  components/
    checkout-form.tsx
features/upgrade/       # same
```

Convex modules live under `convex/` with taste naming (`billing.ts`, not `billing-actions.ts`). When the concern is more than one file, nest them under `convex/<concern>/` (`architecture:folders`). A Convex service module still exposes a small public set of queries/mutations/actions; features call those. They do not duplicate Stripe/auth logic in another Convex file.

Adjust names to the repo. **Inside the owning folder**, keep the tree shallow: public entry → primitives / collaborators → at most one leaf folder (`components/`, `hooks/`). That nesting is required. It is not extra ceremony. `taste:never-nest` is about `if` / `try` pyramids, not the filesystem. Do not skip the owning folder to keep the tree “flat.” Do not invent four empty layers (`services/billing/stripe/v2/internal/`).

## Cheap reads

**Reads must stay cheap as data grows.** Prefer **compute on write**, store the result, read it later.

| Bad (does not scale) | Good (scales) |
| --- | --- |
| On every render/query: scan all rows and sum/average/count | Store `total`, `count`, `avg` on a parent row, summary table, or dedicated columns |
| Dashboard that maps every event into charts client-side | Pre-aggregate on insert/update; UI reads the summary |
| `collect()` then reduce in TS for hot paths | Indexed query of stored aggregates / summary docs |

**Rule:** if a value is shown often and derived from many child records, **persist it** and **update it in the same write** that changes the children (insert / patch / delete). Do not recalculate from scratch on each read unless the dataset is provably tiny and bounded.

When inserting or updating a child:

1. Write the child record
2. **In the same mutation/transaction**, bump/recompute the stored aggregate on the parent or summary row
3. Reads only fetch the stored fields

Example shape (conceptual): `orders: { … }` and `users: { orderCount, orderTotalCents, … }` updated when an order is inserted. Not: `listOrders(userId)` then sum in the React tree or in a query every time.

- **Index** fields you filter/sort by (Convex: `.withIndex`, not `.filter` scans)
- Avoid unbounded `.collect()` on growing tables. Paginate or aggregate
- Don't N+1: batch or denormalize fields needed for list views
- Client components should display data, not be the analytics engine
- Expensive derived views → materialize (table/columns/summary doc), not calculate on render

If a one-off admin script needs a full scan, say so explicitly. Never copy that pattern into hot product paths.

## Deterministic queries

Queries (and any cached / reactive read) must return the same result for the same data. Do **not** read the wall clock, generate randomness, or call a non-deterministic network from a query.

| Bad | Good |
| --- | --- |
| `Date.now()` / `new Date()` inside a query to expire rows | Store `status` on write or a scheduled mutation. Pass `now` only for display windows, never as an authorization check |
| Query that maybe hits an external API | Query reads stored fields; an action fetches, a mutation writes |
| Filter/sort in memory after an unbounded `collect()` | Indexed query; paginate or read a stored summary |

Public queries, mutations, and actions declare argument (and return) validators that match the real contract (`taste:types-tell-the-truth`). Do not use `v.any()` to skip that work.

## Authority

A disabled button is **user feedback**. If a client can skip it, the write still happens. Put the lock on the **service write** (mutation, action, or server handler), not only in the feature UI (`taste:trust-the-server`).

| Check | Rule |
| --- | --- |
| **Identity** | Public writes that touch user data call the repo's auth helper (`getUserIdentity` / `requireUser` / equivalent) and fail if missing |
| **Ownership / tenant** | Before patch/delete/read of a row, prove the authenticated user owns it or belongs to that tenant. Never trust a client-sent `userId` / `orgId` alone |
| **Same-write invariants** | Facts that must stay true together (row + aggregate, status + timestamp, ledger + side effect) live in **one** mutation/transaction |
| **Money / permissions** | Charge, refund, role change, and admin paths go through the owning service; the feature does not call the provider with a client-supplied amount it did not authorize |

Anti-patterns: mutation accepts `userId` from the client and writes that user's rows with no identity check; “the button is hidden for non-admins” as the only admin gate; updating a child row in one handler and the parent aggregate in a later optimistic UI call; feature-local `if (!session)` while the public mutation still runs.

Name identity, ownership, and retry keys on the structure card when the slice has writes.

## Structure card

Present this **Structure** card before writing code (and include it in the inline plan contract when planning under `/task`):

```markdown
## Structure

**Always**
**Services:**
- **Owns / extends:** `path`: public API: `makeUserPay(…)`, … (or _n/a: pure UI_)
- **Calls (existing):** `billing.makeUserPay`, `auth.requireUser`, … (never reimplements these)
- **Must not duplicate:** <Stripe / JWT / email provider / …>
**Moves / corrections:** <required by Rule 1 / what-done-means / named finding: move X → services/billing; delete old path> | _none_
**Feature entry:** `path`: `useX` | `ClassX` | `fn`. One-line contract (orchestrates services + UI); **deep** surface
**Primitives:**
- **Reuse (existing):** cite path + one-line job | _none_
- **New / extend:** path. One specific job; how it stays reusable without breaking
- **Inside:** which service / deep module owns it
**Hidden behind services / entry:** bullet list of responsibilities callers must not see
**Folder map:** (required owning folder; no mixed-parent dump)
- `services/<concern>/` (or repo equivalent)
  - `<concern>.ts`          # public API
  - collaborator…
  - `components/` or other one-level leaf when needed
- `features/<slice>/`       # calls services. No domain fork
  - entry + UI…
**Fits existing pattern:** yes (cite **good** service / feature) | correcting debt (what) | new (why)
**Taste:** `taste:naming-files`, `taste:keep-it-simple`, `taste:oop-depth-cap`

**If writes**
**Authority:** identity helper; ownership/tenant check; client cannot bypass; retry key (`architecture:authority`, `taste:safe-to-retry`)

**If lists / dashboards / counts**
**Scalability:**
- Hot reads: <what the UI/query returns>
- Stored on write: <columns / summary table / parent fields updated on insert>
- Indexes: <index names / fields>
- Pagination: <cursor / none because bounded>
- Explicitly NOT recomputed on render/read: <metrics>
- Queries are deterministic: no wall clock / randomness in the read (`architecture:deterministic-queries`)
- Public args validated: `taste:types-tell-the-truth` | n/a

**If big feature / service**
**Extension seam:** foundation from day one. How the next provider/variant plugs in without breaking the public API (ship seam + first impl together)
```

If service boundary, public API shape, primitives (reuse vs new vs fork), folder root, write-vs-read, authority (identity / ownership), or a move vs leave decision is open, put **all** open structure questions in **one** `/grill-me` Questions batch (`Reply like: 1a 2b` per [asking.md](../pack-shared/asking.md)). Recommend a behavior-preserving move when it is required by the goal or finding and you can prove old behavior holds; otherwise name it as a follow-up. Do not drip them one message at a time. New findings later → new batch.

Self-check before done (cite keys, not a second essay):

- [ ] `architecture:services` (domain in a service with a public API, or an existing one extended; features call it)
- [ ] `architecture:primitives` (one job each; reused not forked; inside the owning module)
- [ ] `architecture:prior-mistakes` (not copied; required moves done; optional ones are follow-ups)
- [ ] `architecture:folders` / `architecture:collaborating-parts` (new files nested in an owning folder, not mixed siblings)
- [ ] `architecture:deep-public-surface`
- [ ] `architecture:authority` when the slice has writes
- [ ] `architecture:cheap-reads` when the slice has lists, counts, or dashboards
- [ ] `architecture:deterministic-queries` (no `Date.now()` / randomness in the read)
- [ ] Taste Cite keys respected in the touched lane
- [ ] Observable old behavior still holds after any move

## When this applies

**When this changes the shape.** These rules apply whether or not a skill runs. For a typo or a user-specified pure rename, still apply them; the application is **keep the existing structure**.

Process: explore, then the structure card, then implement, then the checklist above. Steps for an audit live in `architecture/SKILL.md`. The rules are the headings above.

Apply when the work could add files, move ownership, or touch data, including:

- New feature (even one new file)
- Any domain capability (payments, auth, email) a second feature might need
- Temptation to copy Stripe/auth/email logic into a feature or leave it misplaced
- Clear prior mistake in the lane when the current goal or named finding requires a behavior-preserving move
- Extracting logic from a large file
- Adding React state/effects that would otherwise bloat a component
- Any new file for a new concern, or a second file that would sit as a mixed sibling
- Any change that would add files without an owning folder
- Any feature with lists, dashboards, counts, totals, leaderboards, or stats
- Any query that would scan children to answer a parent-level question
- Any public write, webhook, or admin path
- Any query that would read the wall clock or filter a growing table without an index

Hand off: structure card, then `/task` (inline plan contracts in chat). Acceptance evidence and `/review` will fail scale anti-patterns, duplicated-service anti-patterns, mixed-parent file dumps, and missing write-path authority under `/task`. These rules apply on every run.

## Architecture: do not

- Feature-forked Stripe / JWT / email
- Shallow public surface that leaks steps to every caller
- Forking a primitive's job locally
- Copying a known-wrong shape because it was already there
- Dumping new related files into a mixed parent directory
- Treating `taste:never-nest` or `taste:keep-it-simple` as permission to skip the owning folder
- Hot-path compute-on-read for metrics
- `Date.now()` or randomness inside a query
- UI-only guard as the write lock
- Skipping this section because the slice looks small


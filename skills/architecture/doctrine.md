# Architecture doctrine

## Job

Shape scalable code: one service per domain job, a simple public API, one-job helpers inside those modules, writes that check who may act, folders that match the domain, and cheap honest reads.

## Owns

The structure card: services, deep public surface, primitives, prior-mistake moves, folders, collaborating parts, cheap reads, deterministic queries, and write-path authority.

## Does not own

- Naming, errors, never-nest, keep-it-simple, named principles: [`taste:keep-it-simple`](../taste/doctrine.md#keep-it-simple) through [`taste:naming-files`](../taste/doctrine.md#naming-and-files)
- Review disposition: [`../code-review/doctrine.md`](../code-review/doctrine.md)
- Numbered explore / implement steps: [`flow.md`](flow.md), [`standalone.md`](standalone.md)

## Cite keys

| Key | Heading |
| --- | --- |
| `architecture:services` | Services |
| `architecture:deep-public-surface` | Deep public surface |
| `architecture:primitives` | Primitives |
| `architecture:prior-mistakes` | Prior mistakes |
| `architecture:folders` | Folders |
| `architecture:collaborating-parts` | Collaborating parts |
| `architecture:cheap-reads` | Cheap reads |
| `architecture:deterministic-queries` | Deterministic queries |
| `architecture:authority` | Authority |

Snippets: [`examples.md`](examples.md). Apply [`taste:keep-it-simple`](../taste/doctrine.md#keep-it-simple) and taste named principles to structure. Keep the smallest direct structure that meets the goal; add services, seams, and denormalized reads only when ownership, duplication, or locked growth requires them.

A behavior-preserving move is required only when an Active Rule, acceptance criterion, correctness issue, or named finding requires it; otherwise keep it as a follow-up.

## Bars

### Services

A **service** is the code about one domain concern (auth, billing, notifications, search). It exposes a **small public API** of callable functions (or a class/facade with methods). Features **use** the service; they do **not** reimplement that domain.

| Concept | Rule |
| --- | --- |
| **Service** | One concern (billing, auth). Owns the how |
| **Public API** | Named operations features call, for example `makeUserPay()`, `requireUser()`, `sendReceipt()` |
| **Feature** | Product slice that orchestrates services + its own UI/state. Never copies billing/auth internals |

- **Explore for an existing service first.** Extend its public API before inventing a parallel one.
- If the concern is a genuinely independent domain capability or the goal explicitly plans growth, create the service (folder + public entry) and have the feature call it. For bounded local behavior, keep the smallest direct shape until it has independent ownership, real duplication, or a locked rule that needs a boundary.
- Features import **only** the service's public surface. Stripe/SDK/DB helpers stay behind that surface.
- Name public functions as **verbs the product understands** (`makeUserPay`, not `runStripeCheckoutSessionHelper`).
- Prefer throw + try/catch at service boundaries (`taste:throw-at-boundaries`), not `{ success: false }` bags.
- One service is not one giant file: public entry + collaborators / primitives inside the service folder.
- Public writes check identity and ownership in the service (`architecture:authority`). Features may disable UI; they do not own the lock.

Anti-patterns: checkout, upgrade, and invoices each implementing their own Stripe path; “just this once” copy of service logic into a feature; features importing service internals (`billing-stripe`); a `utils/payments.ts` dumping ground with no public contract.

Folder tree: `architecture:collaborating-parts`.

### Deep public surface

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

### Primitives

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

### Prior mistakes

Flawed existing layout is **debt**, not a template. Do not freeze wrong placements because they were already there. Leaving or copying wrong placement is entropy growth (`taste:leave-it-cleaner`).

When explore shows a wrong folder, duplicated domain logic, a feature-forked service, or a sibling that violates this skill / `/taste`, first decide whether the active goal or a named review finding requires a move:

- **Do not copy it.** Cite a *good* sibling or service, or create the correct shape.
- If required, prefer a **behavior-preserving move**: relocate into the right service/folder, extract the public API, rewire callers, delete the dead path. This reduces entropy. If not required, capture it as a follow-up rather than expanding the goal.
- Name the old observable behavior and how you will prove it still holds (existing tests if any, path walk + acceptance evidence / terminals). Do **not** write new tests here: locks are `/create-test` only after `/code-review` or `/pr-review` recommends them. If you cannot be sure the move preserves behavior, include the move in the next `/grill-me` Questions batch. If the move is required and you can preserve behavior, do it; otherwise keep it as a follow-up.
- Update the Structure card (**Moves / corrections**) before coding; mid-implement, patch the plan Structure, then move.
- Same spirit as `/code-review` simplification: apply it while **building**, not only at review time.

Anti-patterns: bolting new code onto a known-wrong shape because it was already there; copying a bad sibling to stay consistent with debt; asking “leave it where it is?” as the recommended option when a clear move preserves behavior.

### Folders

Never sprinkle related files across a flat directory. **Propose the folder map before creating files.**

1. Mirror existing repo conventions (services folder, feature folder, domain folder). Explore first.
2. Prefer **`services/<concern>/`** (or the repo's equivalent) for shared domain APIs; **feature folders** for product UI/orchestration that *calls* those services.
3. If no convention fits, create a **feature/domain folder** and put the cluster inside it.
4. Colocate what changes together; separate what changes for different reasons.
5. Name files per `taste:naming-files`.
6. Avoid `utils.ts` / `helpers.ts` dumping grounds. Name the concept (often: promote to a service, or a primitive inside one).
7. Cite a good sibling feature or existing service when one exists (`taste:cite-a-sibling`). Bad nearby code is debt to move, not a template.

Anti-pattern: five new sibling files next to unrelated code with no folder; or a new payments helper beside a feature when a billing service should own it.

### Collaborating parts

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

Convex modules live under `convex/` with taste naming (`billing.ts`, not `billing-actions.ts`). A Convex service module still exposes a small public set of queries/mutations/actions; features call those. They do not duplicate Stripe/auth logic in another Convex file.

Adjust names to the repo. Keep depth shallow: public entry → primitives / collaborators → leaf helpers. Never-nest deep control flow (`taste:never-nest`); extract instead.

### Cheap reads

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

### Deterministic queries

Queries (and any cached / reactive read) must return the same result for the same data. Do **not** read the wall clock, generate randomness, or call a non-deterministic network from a query.

| Bad | Good |
| --- | --- |
| `Date.now()` / `new Date()` inside a query to expire rows | Store `status` on write or a scheduled mutation. Pass `now` only for display windows, never as an authorization check |
| Query that maybe hits an external API | Query reads stored fields; an action fetches, a mutation writes |
| Filter/sort in memory after an unbounded `collect()` | Indexed query; paginate or read a stored summary |

Public queries, mutations, and actions declare argument (and return) validators that match the real contract (`taste:types-tell-the-truth`). Do not use `v.any()` to skip that work.

### Authority

A disabled button is **user feedback**. If a client can skip it, the write still happens. Put the lock on the **service write** (mutation, action, or server handler), not only in the feature UI (`taste:trust-the-server`).

| Check | Rule |
| --- | --- |
| **Identity** | Public writes that touch user data call the repo's auth helper (`getUserIdentity` / `requireUser` / equivalent) and fail if missing |
| **Ownership / tenant** | Before patch/delete/read of a row, prove the authenticated user owns it or belongs to that tenant. Never trust a client-sent `userId` / `orgId` alone |
| **Same-write invariants** | Facts that must stay true together (row + aggregate, status + timestamp, ledger + side effect) live in **one** mutation/transaction |
| **Money / permissions** | Charge, refund, role change, and admin paths go through the owning service; the feature does not call the provider with a client-supplied amount it did not authorize |

Anti-patterns: mutation accepts `userId` from the client and writes that user's rows with no identity check; “the button is hidden for non-admins” as the only admin gate; updating a child row in one handler and the parent aggregate in a later optimistic UI call; feature-local `if (!session)` while the public mutation still runs.

Name identity, ownership, and retry keys on the structure card when the slice has writes.

## Output

Present this **Structure** card before writing code (and include it in the inline plan contract when planning under `/goal`):

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
**Folder map:**
- `services/<concern>/` (or repo equivalent)
  - `<concern>.ts`          # public API
  - collaborator…
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
- [ ] `architecture:folders` / `architecture:collaborating-parts`
- [ ] `architecture:deep-public-surface`
- [ ] `architecture:authority` when the slice has writes
- [ ] `architecture:cheap-reads` when the slice has lists, counts, or dashboards
- [ ] `architecture:deterministic-queries` (no `Date.now()` / randomness in the read)
- [ ] Taste Cite keys respected in the touched lane
- [ ] Observable old behavior still holds after any move

## Apply

**When this changes the shape.** Always load this doctrine. For a typo or a user-specified pure rename, still load; the application is **keep the existing structure**.

Process (pointers, not a second copy of the bars): Explore → structure card → implement → self-check. Steps live in [flow.md](flow.md). Bars are the Cite keys above.

Apply when the work could add files, move ownership, or touch data, including:

- New feature with more than one new file
- Any domain capability (payments, auth, email) a second feature might need
- Temptation to copy Stripe/auth/email logic into a feature or leave it misplaced
- Clear prior mistake in the lane when the current goal or named finding requires a behavior-preserving move
- Extracting logic from a large file
- Adding React state/effects that would otherwise bloat a component
- Any change that would add files without a parent folder
- Any feature with lists, dashboards, counts, totals, leaderboards, or stats
- Any query that would scan children to answer a parent-level question
- Any public write, webhook, or admin path
- Any query that would read the wall clock or filter a growing table without an index

Hand off: structure card → `/goal` (inline plan contracts in chat). Acceptance evidence and `/code-review` will fail scale anti-patterns, duplicated-service anti-patterns, and missing write-path authority under `/goal`. Other pack skills load this doctrine on **every** run via [standards.md](../pack-shared/standards.md).

## Anti-patterns

- Feature-forked Stripe / JWT / email
- Shallow public surface that leaks steps to every caller
- Forking a primitive's job locally
- Copying a known-wrong shape because it was already there
- Hot-path compute-on-read for metrics
- `Date.now()` or randomness inside a query
- UI-only guard as the write lock
- Skipping this Read because the slice looks small

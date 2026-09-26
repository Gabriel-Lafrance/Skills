# Code structure

Cite keys use the `architecture:` prefix.

These rules apply on every non-trivial change, whether or not anyone invoked `/architecture`. Examples: `architecture/examples.md`.

## Services

A **service** owns one domain concern (auth, billing, notifications, search) behind a small public API. Features call it; they never reimplement its domain.

| Do | Don't |
| --- | --- |
| Extend an existing service's public API | Build a parallel one |
| Product verbs (`makeUserPay`, `requireUser`, `sendReceipt`) | `runStripeCheckoutSessionHelper` |
| Features import only the public API; SDK, Stripe, DB helpers stay inside | Features importing internals (`billing-stripe`), or a `utils/payments.ts` with no contract |
| Throw at the service boundary | `{ success: false }` bags |
| Public entry plus collaborators in the service folder | One giant file |
| Identity and ownership checked in the service write ([Authority](#authority)) | A lock that lives only in feature UI |

Create a service when the concern is an independent domain or the goal plans growth. For bounded local behavior, keep the direct shape until it has its own owner, real duplication, or a locked rule that needs a boundary. Anti-pattern: checkout, upgrade and invoices each with their own Stripe path.

**Check:** does a feature copy or reach inside another service's domain?

## Deep public surface

Hide orchestration behind one deep entry: a simple interface over rich behavior. For a domain concern it is the service's public API; for UI, usually a hook that calls services.

| Shape | When |
| --- | --- |
| **Service** (module / class / facade) | Domain capability shared across features (default for auth, billing) |
| React hook (`useX`) | UI state, effects, subscriptions; delegates domain work |
| Class | Stateful domain behavior, shared lifecycle (often the service) |
| Narrow function | Pure transform, clear input and output |

The signature is obvious at a glance (not necessarily a TypeScript `interface`). Callers never see helpers, parsers, adapters or edge-case branches; push those down into collaborators. One main export per file when practical. Anti-pattern: **shallow modules** whose params, options or leaked steps leave callers orchestrating.

**Check:** can a caller use it without knowing call order or edge cases?

## Primitives

A **primitive** is small code with one specific job, strong enough that callers never redo it, composable without brittle coupling, and reusable on its own. Primitives live inside services and deep modules, never as a rival top-level layer.

1. Build with primitives instead of repeating their job at call sites.
2. Explore **this** repo first and reuse what exists. Do not invent a catalog from training data.
3. Place a new one inside the owning service or deep module (or a shared layer they compose), not a `utils` bag.
4. Never fork a primitive's job in a feature or sibling helper.

Anti-patterns: wrappers that only rename; helpers that answer many questions.

**Check:** does an existing primitive already answer this?

## Prior mistakes

Wrong existing layout (wrong folder, duplicated domain logic, feature-forked service, rule-breaking sibling) is debt, not a template.

- Do not copy it. Cite a good sibling or create the correct shape.
- Move only when the goal or a named finding requires it: relocate, extract the public API, rewire callers, delete the dead path. Otherwise record a follow-up.
- Name the old observable behavior and how you prove it holds (existing tests, path walk, terminals). A new test waits for a user-accepted `/create-test` brief (a `/task` suggestion after grill Locked, or a `/review` recommendation).
- Not sure the move preserves behavior? Ask in the next `/grill-me` Questions batch.
- Record it under **Moves / corrections** on the Structure card before coding; mid-implement, patch the plan first.
- Never recommend "leave it where it is" when a clear move preserves behavior. Apply this while building, not only at `/review`.

**Check:** am I extending a shape I know is wrong?

## Folders

Propose the folder map, then create the owning folder before the files, even for the first file of a new concern. Never-nest and keep it simple are about code, not a reason for a flat folder.

1. Mirror existing conventions. A good nested sibling beats a nearby flat dump.
2. `services/<concern>/` (or repo equivalent) for shared domain APIs; feature folders for UI and orchestration that call them.
3. No convention fits: create a feature or domain folder.
4. Colocate what changes together; nest non-entry collaborators one level down (`components/`, `hooks/`). Separate what changes for different reasons.
5. Name files per `taste:naming-files`.
6. No `utils.ts` / `helpers.ts`. Name the concept (often a service, or a primitive inside one).
7. **Convex:** a one-file concern may stay `convex/billing.ts` if that is the repo pattern. A second file moves the cluster into `convex/billing/` (no root `billingStripe.ts`). Never both `convex/billing.ts` and `convex/billing/`.
8. **App Router:** `page.tsx`, `layout.tsx`, `route.ts` stay in the route folder; other slice files nest there or in a feature folder.

Only root files at the root (`package.json`, `tsconfig.json`, `docs/design.md`). Patching a file already in the right folder needs no new folder.

**Check:** does every new file sit in a folder that owns its concern?

## Collaborating parts

Inside the owning folder: public entry, then collaborators, then at most one leaf folder. That nesting is required; adjust names to the repo. No empty layers (`services/billing/stripe/v2/internal/`).

```text
services/billing/
  billing.ts            # public API: makeUserPay, refundPayment. Only export features import
  billing-stripe.ts     # private
  billing-types.ts
features/checkout/      # UI + orchestration. Calls makeUserPay
  use-checkout.ts
  components/
    checkout-form.tsx
```

Convex uses taste naming (`billing.ts`, not `billing-actions.ts`), nests under `convex/<concern>/` past one file, and exposes a small set of queries, mutations and actions. No other Convex file duplicates Stripe or auth logic.

**Check:** entry, collaborators, one leaf, nothing deeper?

## Cheap reads

Compute on write, store the result, read the stored value.

| Don't | Do |
| --- | --- |
| Sum, average or count all rows per render or query | Store `total`, `count`, `avg` on a parent row or summary table |
| Build charts from raw events on the client | Pre-aggregate on write; the UI reads the summary |
| `.filter` scans, or `collect()` then reduce | `.withIndex` on filter and sort fields |
| Unbounded `.collect()` on a growing table | Paginate or aggregate |
| N+1 lookups for list views | Batch, or denormalize list fields |

Update the aggregate **in the same mutation** that inserts, patches or deletes the child (an order insert also bumps `users.orderCount`). Recompute on read only for provably tiny, bounded data. A one-off admin script may full-scan if it says so, never in product paths.

**Check:** does a hot read scan children to answer a parent question?

## Deterministic queries

A query or reactive read returns the same result for the same data: no clock, randomness or network.

| Don't | Do |
| --- | --- |
| `Date.now()` in a query to expire rows | Store `status` on write or in a scheduled mutation; `now` only for display, never authorization |
| A query that calls an external API | An action fetches, a mutation writes, the query reads |

Public queries, mutations and actions declare argument and return validators that match the real contract. No `v.any()`.

**Check:** would this query answer differently tomorrow on the same data?

## Authority

A disabled button is feedback, not a lock. Lock the service write (mutation, action, server handler).

| Check | Rule |
| --- | --- |
| **Identity** | Public writes on user data call the auth helper (`getUserIdentity` / `requireUser`) and fail if missing |
| **Ownership / tenant** | Prove the user owns the row or belongs to the tenant before patch, delete or read. Never trust a client-sent `userId` / `orgId` |
| **Same-write invariants** | Facts that stay true together (row and aggregate, status and timestamp, ledger and side effect) change in **one** mutation |
| **Money / permissions** | Charge, refund, role and admin paths go through the owning service, never with an unauthorized client-supplied amount |

Anti-patterns: a hidden button as the only admin gate; the aggregate updated in a later optimistic UI call; a feature `if (!session)` while the mutation still runs. Name identity, ownership and retry keys on the Structure card.

**Check:** could a caller skip the UI and still write?

## Structure card

Present before writing code, and in the plan contract under `/task`:

```markdown
## Structure

**Always**
**Services:**
- **Owns / extends:** `path`: public API: `makeUserPay(…)`, … (or _n/a: pure UI_)
- **Calls (existing):** `billing.makeUserPay`, `auth.requireUser`, …
- **Must not duplicate:** <Stripe / JWT / email provider / …>
**Moves / corrections:** <required by Rule 1 / done when / named finding: move X to services/billing; delete old path> | _none_
**Feature entry:** `path`: `useX` | `ClassX` | `fn`. One-line contract; deep public API
**Primitives:**
- **Reuse (existing):** path + one-line job | _none_
- **New / extend:** path. One job; how it stays reusable
- **Inside:** owning service / deep module
**Hidden behind services / entry:** responsibilities callers must not see
**Folder map:** (owning folder required)
- `services/<concern>/`
  - `<concern>.ts`          # public API
  - collaborator…
  - `components/` or other one-level leaf when needed
- `features/<slice>/`       # calls services
  - entry + UI…
**Fits existing pattern:** yes (cite good service / feature) | correcting debt (what) | new (why)
**Taste:** `taste:naming-files`, `taste:keep-it-simple`, `taste:oop-depth-cap`

**If writes**
**Authority:** identity helper; ownership/tenant check; client cannot bypass; retry key (`architecture:authority`, `taste:safe-to-retry`)

**If lists / dashboards / counts**
**Scalability:**
- Hot reads: <what the UI/query returns>
- Stored on write: <columns / summary table / parent fields>
- Indexes: <index names / fields>
- Pagination: <cursor / none because bounded>
- Explicitly NOT recomputed on render/read: <metrics>
- Queries are deterministic (`architecture:deterministic-queries`)
- Public args validated: `taste:types-tell-the-truth` | n/a

**If big feature / service**
**Extension seam:** how the next provider/variant plugs in without breaking the public API (ship seam + first impl together)
```

Put every open structure question (service boundary, public API, primitives, folder, write vs read, authority, move vs leave) in **one** `/grill-me` Questions batch ([asking.md](../pack-shared/asking.md)). New findings go in a new batch.

Self-check before done:

- [ ] `architecture:services` · `architecture:primitives` · `architecture:deep-public-surface`
- [ ] `architecture:prior-mistakes`: required moves done, optional ones recorded
- [ ] `architecture:folders` / `architecture:collaborating-parts`
- [ ] `architecture:authority` when the slice writes
- [ ] `architecture:cheap-reads` · `architecture:deterministic-queries` when the slice reads lists or counts
- [ ] Taste cite keys respected; old behavior holds after any move

## When this applies

Always. For a typo or pure rename, applying it means keeping the structure. Process: explore, Structure card, implement, self-check. Audit steps: `architecture/SKILL.md`.

Triggers: new feature; shared domain (payments, auth, email); copying provider logic; required move; extracting from a large file; React state bloating a component; new file, mixed sibling, or file without an owning folder; lists, counts or stats; parent query scanning children; public write, webhook or admin path; clock or unindexed filter in a query.

Hand off: Structure card, then `/task`. `/review` fails scale anti-patterns, duplicated services, mixed-parent dumps and missing write authority.

## Architecture: do not

- Fork Stripe, JWT or email logic into a feature
- Ship a shallow public API, or fork a primitive
- Copy a known-wrong shape
- Dump files in a mixed parent folder, or cite never-nest or keep it simple to skip the owning folder
- Compute metrics on read in hot paths, or use `Date.now()` in a query
- Rely on a UI-only guard as the write lock
- Skip this file because the slice looks small

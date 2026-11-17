# Code structure

Cite keys: `structure:` plus a heading in this file.

For a typo or pure rename, keep the structure. Examples: [code-structure-examples.md](code-structure-examples.md). A Convex repo (a `convex/` folder exists) also applies [convex.md](convex.md).

## Checklist

Enough for a small change. Open a section only when its row applies.

Before done:

- [ ] `structure:services`: no feature copies or reaches inside another service's domain
- [ ] `structure:deep-public-surface`: a caller needs no call order or edge-case knowledge
- [ ] `structure:responsibility-boundaries`: changed and new files have coherent jobs; behavior is findable without unrelated implementation reads
- [ ] `structure:primitives`: an existing primitive was checked before writing a new one
- [ ] `structure:prior-mistakes`: required moves done, optional ones recorded, no known-wrong shape extended
- [ ] `structure:folders` / `structure:collaborating-parts`: every new file sits in a folder that owns its concern; entry, collaborators, one leaf, nothing deeper
- [ ] `structure:authority` when the slice writes: a caller cannot skip the UI and still write
- [ ] `structure:cheap-reads`, `structure:deterministic-queries` when the slice reads lists or counts: no hot read scans children for a parent question, and the same data gives the same answer tomorrow
- [ ] `quality:*` cite keys respected; old behavior holds after any move

## Services

A **service** owns one domain concern (auth, billing, notifications, search) behind a small public API. Features call it.

| Do | Don't |
| --- | --- |
| Extend an existing service's public API | Build a parallel one |
| Product verbs (`makeUserPay`, `requireUser`, `sendReceipt`) | `runStripeCheckoutSessionHelper` |
| Features import only the public API; SDK, Stripe, DB helpers stay inside | Features importing internals (`billing-stripe`), or a `utils/payments.ts` with no contract |

Create a service when the concern is an independent domain or the goal plans growth. Keep bounded local behavior direct until it has its own owner, real duplication, or a locked rule that needs a boundary.

## Deep public surface

Hide orchestration behind one deep entry: a simple interface over rich behavior.

| Shape | When |
| --- | --- |
| **Service** (module / class / facade) | Domain capability shared across features (default for auth, billing); its public API is the entry |
| React hook (`useX`) | UI state, effects, subscriptions; the usual UI entry, delegating domain work to services |
| Class | Stateful domain behavior, shared lifecycle (often the service) |
| Narrow function | Pure transform, clear input and output |

The signature is obvious at a glance. Push helpers, parsers, adapters and edge-case branches down into collaborators callers never see. Anti-pattern: **shallow modules** whose params, options or leaked steps leave callers orchestrating.

## Responsibility boundaries

Find the existing owner before adding a file or service. Use the domain's names and the established layout when it fits these rules. Extract when a distinct responsibility, dependency boundary, lifecycle, or confirmed variation has its own reason to change. One consumer can justify a private collaborator; size alone never justifies a split. Before extracting, name the responsibility and what its caller stops knowing, then test it against actual callers, not a hypothetical variant or token savings: can a reader find the behavior from the domain name and public signature without reading unrelated code, and does a change to it land with its owner alone? If the split only moves complexity or adds pass-through hops, keep the cohesive shape or merge the shallow pieces.

Keep tightly coupled steps, trivial guards, and short cohesive behavior together. Reject one-function files, renaming wrappers, and fragments that make a reader rebuild one operation across files. Callers use a small public entry; rendering, transport, and lifecycle details stay private or in existing owning services. Do not export internals to make them easy to find.

Colocate relevant existing tests and assets with their owner where the framework allows, and keep test discovery working; consent stays under [no-unrequested-tests.md](no-unrequested-tests.md). Record a justified move on the Structure card under [prior mistakes](#prior-mistakes). Routine private placement is the implementer's choice; ask only about a consequential unresolved choice of ownership, public contract, scope, or behavior. Examples: [meaningful extraction](code-structure-examples.md#meaningful-extraction-with-one-consumer).

## Primitives

A **primitive** is small code with one job, strong enough that callers never redo it, composable, and reusable on its own. Primitives live inside services and deep modules, never as a rival top-level layer.

1. Explore **this** repo first and reuse what exists.
2. Call a primitive wherever its job recurs; a fork at a call site, feature, or sibling helper duplicates it.
3. Place a new one inside the owning service or deep module (or a shared layer they compose), not a `utils` bag.

## Prior mistakes

Wrong existing layout (wrong folder, duplicated domain logic, feature-forked service, rule-breaking sibling) is debt, not a template.

- Move only when the goal or a named finding requires it (relocate, extract the public API, rewire callers, delete the dead path). Otherwise record a follow-up.
- Name the old observable behavior and how you prove it holds (existing tests, path walk, terminals). A new test follows [no-unrequested-tests.md](no-unrequested-tests.md#accepted-means).
- Record the move under **Moves / corrections** on the Structure card before coding; mid-implement, patch the plan first.
- Recommend a clear behavior-preserving move over "leave it where it is", while building and at `/review`.

## Folders

Propose the folder map, then create the owning folder before the files, even for the first file of a new concern. Never-nest and keep it simple govern code, not this folder.

1. Follow the examples' layout. Mirror an app folder only when it matches an example; a nearby flat dump is not a convention.
2. `services/<concern>/` for shared domain APIs; feature folders for UI and orchestration that call them. If no convention fits, create a feature or domain folder.
3. Colocate what changes together; nest non-entry collaborators one level down (`components/`, `hooks/`). Separate what changes for different reasons.
4. Name files per `quality:naming-files`.
5. **App Router:** `page.tsx`, `layout.tsx`, `route.ts` stay in the route folder; other slice files nest there or in a feature folder.

Only root files at the root (`package.json`, `tsconfig.json`, `docs/design.md`). Patching a file already in the right folder needs no new folder.

## Collaborating parts

Inside the owning folder: public entry, then collaborators, then at most one leaf folder. Names follow the repo. Nest only layers that hold files (bad: `services/billing/stripe/v2/internal/`).

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

## Cheap reads

Compute on write, store the result, read the stored value.

| Don't | Do |
| --- | --- |
| Sum, average or count all rows per render or query | Store `total`, `count`, `avg` on a parent row or summary table |
| Build charts from raw events on the client | Pre-aggregate on write; the UI reads the summary |
| Scan rows, then filter or reduce in code | Query an index on filter and sort fields |
| Unbounded read of a growing table | Paginate or aggregate |
| N+1 lookups for list views | Batch, or denormalize list fields |

Update the aggregate **in the same mutation** that inserts, patches or deletes the child (an order insert also bumps `users.orderCount`). Recompute on read only for provably tiny, bounded data. A one-off admin script may full-scan if it says so, never in product paths.

## Deterministic queries

A query or reactive read returns the same result for the same data: no clock, randomness or network.

| Don't | Do |
| --- | --- |
| `Date.now()` in a query to expire rows | Store `status` on write or in a scheduled mutation; `now` only for display, never authorization |
| A query that calls an external API | An action fetches, a mutation writes, the query reads |

Public queries, mutations and actions declare argument and return validators that match the real contract, with specific types instead of a catch-all.

## Authority

The server enforces identity, ownership, money, and permissions. A disabled button is only feedback. Lock the service write (mutation, action, server handler).

| Check | Rule |
| --- | --- |
| **Identity** | Public writes on user data call the auth helper (`getUserIdentity` / `requireUser`) and fail if missing |
| **Ownership / tenant** | Prove the user owns the row or belongs to the tenant before patch, delete or read. Never trust a client-sent `userId` / `orgId` |
| **Same-write invariants** | Facts that stay true together (row and aggregate, status and timestamp, ledger and side effect) change in **one** mutation |
| **Money / permissions** | Charge, refund, role and admin paths go through the owning service, never with an unauthorized client-supplied amount |

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
**Matches example:** <example heading> (plus the app sibling that matches it, if any) | correcting debt (what)
**Quality:** `quality:naming-files`, `quality:keep-it-simple`, `quality:oop-depth-cap`

**If writes**
**Authority:** identity helper; ownership/tenant check; client cannot bypass; retry key (`structure:authority`, `quality:safe-to-retry`)

**If lists / dashboards / counts**
**Scalability:**
- Hot reads: <what the UI/query returns>
- Stored on write: <columns / summary table / parent fields>
- Indexes: <index names / fields>
- Pagination: <cursor / none because bounded>
- Explicitly NOT recomputed on render/read: <metrics>
- Queries are deterministic (`structure:deterministic-queries`)
- Public args validated: `quality:types-tell-the-truth` | n/a

**If Feature** ([`quality:strong-foundation`](strong-foundation.md))
**Foundation:**
- Areas of modularity: <area> → <seam: the named extension point where a new variant plugs in> + <first real implementation> | _none: Tweak, Bug, or Chore with no area named_
- Extends existing seam: <seam> | _none_
- Next change this makes small: <request> → <one new file + one registration>
```

Research existing owners, callers, and write boundaries before asking. Batch only consequential structure choices through `/grill-me` ([Asking the user](writing-style.md#asking-the-user)): different behavior, data meaning, or authority in the same files is one; a folder preference alone is not. Ask a later batch only when new evidence exposes one.

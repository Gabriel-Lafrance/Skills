# Code structure

Cite keys use the `structure:` prefix. Each key is a heading in this file.

These rules apply on every non-trivial change. For a typo or pure rename, applying them means keeping the structure. Process: explore, Structure card, implement, check. Examples: [code-structure-examples.md](code-structure-examples.md).

## Checklist

This checklist is enough for a small change. Open a section below only when a row applies.

Before done:

- [ ] `structure:services`: no feature copies or reaches inside another service's domain
- [ ] `structure:deep-public-surface`: a caller needs no call order or edge-case knowledge
- [ ] `structure:primitives`: an existing primitive was checked before writing a new one
- [ ] `structure:prior-mistakes`: required moves done, optional ones recorded, no known-wrong shape extended
- [ ] `structure:folders` / `structure:collaborating-parts`: every new file sits in a folder that owns its concern; entry, collaborators, one leaf, nothing deeper
- [ ] `structure:authority` when the slice writes: a caller cannot skip the UI and still write
- [ ] `structure:cheap-reads`, `structure:deterministic-queries` when the slice reads lists or counts: no hot read scans children for a parent question, and the same data gives the same answer tomorrow
- [ ] `quality:*` cite keys respected; old behavior holds after any move

## Services

A **service** owns one domain concern (auth, billing, notifications, search) behind a small public API. Features call it and leave its domain to it.

| Do | Don't |
| --- | --- |
| Extend an existing service's public API | Build a parallel one |
| Product verbs (`makeUserPay`, `requireUser`, `sendReceipt`) | `runStripeCheckoutSessionHelper` |
| Features import only the public API; SDK, Stripe, DB helpers stay inside | Features importing internals (`billing-stripe`), or a `utils/payments.ts` with no contract |

Create a service when the concern is an independent domain or the goal plans growth. For bounded local behavior, keep the direct shape until it has its own owner, real duplication, or a locked rule that needs a boundary. Anti-pattern: checkout, upgrade and invoices each with their own Stripe path.

## Deep public surface

Hide orchestration behind one deep entry: a simple interface over rich behavior.

| Shape | When |
| --- | --- |
| **Service** (module / class / facade) | Domain capability shared across features (default for auth, billing); its public API is the entry |
| React hook (`useX`) | UI state, effects, subscriptions; the usual UI entry, delegating domain work to services |
| Class | Stateful domain behavior, shared lifecycle (often the service) |
| Narrow function | Pure transform, clear input and output |

The signature is obvious at a glance (not necessarily a TypeScript `interface`). Push helpers, parsers, adapters and edge-case branches down into collaborators so callers never see them. Anti-pattern: **shallow modules** whose params, options or leaked steps leave callers orchestrating. A deep entry is not a pass-through chain ([`quality:light-to-read`](code-quality.md#light-to-read)).

## Primitives

A **primitive** is small code with one specific job, strong enough that callers never redo it, composable without brittle coupling, and reusable on its own. Primitives live inside services and deep modules, never as a rival top-level layer.

1. Explore **this** repo first and reuse what exists, rather than a catalog from training data.
2. Call a primitive wherever its job recurs; a fork at a call site, in a feature, or in a sibling helper duplicates it.
3. Place a new one inside the owning service or deep module (or a shared layer they compose), not a `utils` bag.

Anti-patterns: wrappers that only rename; helpers that answer many questions.

## Prior mistakes

Wrong existing layout (wrong folder, duplicated domain logic, feature-forked service, rule-breaking sibling) is debt, not a template.

- Build from the matching example ([code-structure-examples.md](code-structure-examples.md)), or a sibling that already matches one ([`quality:cite-a-sibling`](code-quality.md#mechanical-rules)). Most existing code does not match.
- Move only when the goal or a named finding requires it (relocate, extract the public API, rewire callers, delete the dead path). Otherwise record a follow-up.
- Name the old observable behavior and how you prove it holds (existing tests, path walk, terminals). A new test waits for a user-accepted lock (a `/task` suggestion after the grill's Locked in message, or a `/review` recommendation) and follows [testing.md](testing.md).
- Unsure the move preserves behavior? Research callers and observable behavior first. Ask in the next `/grill-me` Questions batch only if an unresolved consequential behavior choice remains.
- Record the move under **Moves / corrections** on the Structure card before coding; mid-implement, patch the plan first.
- When a clear move preserves behavior, recommend it over "leave it where it is", while building as well as at `/review`.

## Folders

Propose the folder map, then create the owning folder before the files, even for the first file of a new concern. Never-nest and keep it simple govern code only, so the owning folder stays.

1. Follow the examples' layout. Mirror an app folder only when it matches an example; a nearby flat dump is not a convention.
2. `services/<concern>/` for shared domain APIs; feature folders for UI and orchestration that call them. If no convention fits, create a feature or domain folder.
3. Colocate what changes together; nest non-entry collaborators one level down (`components/`, `hooks/`). Separate what changes for different reasons.
4. Name files per `quality:naming-files`, and name the concept (often a service, or a primitive inside one) instead of `utils.ts` / `helpers.ts`.
5. **Convex:** a one-file concern may stay `convex/billing.ts` if that is the repo pattern. A second file moves the cluster into `convex/billing/` (no root `billingStripe.ts`), and `convex/billing.ts` and `convex/billing/` never coexist.
6. **App Router:** `page.tsx`, `layout.tsx`, `route.ts` stay in the route folder; other slice files nest there or in a feature folder.

Only root files at the root (`package.json`, `tsconfig.json`, `docs/design.md`). Patching a file already in the right folder needs no new folder.

## Collaborating parts

Inside the owning folder: public entry, then collaborators, then at most one leaf folder. That nesting is required; adjust names to the repo. Nest only layers that hold files (bad: `services/billing/stripe/v2/internal/`).

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

Convex uses the file naming in [code-quality.md](code-quality.md#naming-and-files) (`billing.ts`, not `billing-actions.ts`), and exposes a small set of queries, mutations and actions. Only the owning Convex file holds Stripe or auth logic.

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

## Deterministic queries

A query or reactive read returns the same result for the same data: no clock, randomness or network.

| Don't | Do |
| --- | --- |
| `Date.now()` in a query to expire rows | Store `status` on write or in a scheduled mutation; `now` only for display, never authorization |
| A query that calls an external API | An action fetches, a mutation writes, the query reads |

Public queries, mutations and actions declare argument and return validators that match the real contract, with specific types instead of `v.any()`.

## Authority

The server enforces identity, ownership, money, and permissions. UI checks, such as a disabled button, are only feedback. Lock the service write (mutation, action, server handler).

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

Research the existing owners, callers, and write boundaries before asking structure questions. Reuse settled decisions and make ordinary implementer choices directly. Batch the remaining consequential choices using `/grill-me` ([Asking the user](writing-style.md#asking-the-user)); give the evidence, realistic alternatives, recommendation, and practical consequences. Different behavior, data meaning, or authority in the same files is still a material choice. A folder preference alone does not justify a question. Ask a later batch only when new evidence exposes a material unresolved choice.

Hand off: Structure card, then `/task`. `/review` fails scale anti-patterns, duplicated services, mixed-parent dumps and missing write authority.

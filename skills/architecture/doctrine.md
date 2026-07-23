# Architecture Doctrine

Quality code here means: **independent domain capabilities live in services; features call those services; prior structural mistakes are not copied and are moved when the current goal requires it; callers see a deep public surface; depth is built from strong primitives inside those modules when warranted; complexity lives behind the surface; entropy in the touched lane does not grow; files live in folders that match the domain; data stays cheap to read as the product grows.**

Read **`/taste`** first — especially **Bad code = complexity and entropy** (and [../taste/examples.md](../taste/examples.md) when unsure). For architecture good/bad pairs, see [examples.md](examples.md). Taste owns naming, errors, nesting, file rules, and the complexity/entropy definition — this skill owns the structure card **and scalability**.

## Abstraction budget

Architecture must make the current goal clearer and safer, not use it as a reason to create speculative layers. Keep a local guard inline unless extraction owns independent behavior, removes real duplication, or enforces a locked Active Rule.

Require evidence before adding a new file, service, deep module, public API, concurrency system, queue, lock, retry path, or class hierarchy: an existing reusable boundary, actual duplicate behavior, a locked invariant that cannot be safely enforced locally, or explicitly planned domain growth. If none exists, retain the smallest direct shape.

Existing debt is a candidate for a move, not automatic scope. Include a behavior-preserving move only when the current goal or a named review finding requires it to satisfy an Active Rule, correctness, security, or an acceptance criterion. Otherwise record it as a follow-up.

## Doctrine

### 1. Services own domain capabilities (critical)

A **service** is the code about one domain concern — auth, billing, notifications, search, etc. It exposes a **small public API** of callable functions (or a class/facade with methods). Features **use** the service; they do **not** reimplement that domain.

| Concept | Rule |
| --- | --- |
| **Service** | One concern (billing, auth, …) — owns the how |
| **Public API** | Named operations features call — e.g. `makeUserPay()`, `requireUser()`, `sendReceipt()` |
| **Feature** | Product slice that orchestrates services + its own UI/state — never copies billing/auth/… internals |

Example:

```text
services/billing/          # or billing/ — match repo convention
  billing.ts               # public API: makeUserPay(), refundPayment(), …
  billing-stripe.ts        # private collaborator
  billing-types.ts

features/checkout/         # calls billing.makeUserPay — does not talk to Stripe
features/upgrade/          # same — calls billing.makeUserPay
```

Rules:

- **Explore for an existing service first.** Extend its public API before inventing a parallel one.
- If the concern is a genuinely independent domain capability or the goal explicitly plans growth, create the service (folder + public entry) and have the feature call it. For bounded local behavior, keep the smallest direct shape until it has independent ownership, real duplication, or a locked rule that needs a boundary.
- Features import **only** the service's public surface. Stripe/SDK/DB helpers stay behind that surface.
- Name public functions as **verbs the product understands** (`makeUserPay`, not `runStripeCheckoutSessionHelper`).
- Prefer **throw + try/catch** at service boundaries (see `/taste`) — not `{ success: false }` bags.
- One service ≠ one giant file: public entry + collaborators / primitives inside the service folder (see §3, §6).

Anti-patterns:

- Checkout, upgrade, and invoices each implementing their own Stripe / payment path
- "Just this once" copy of service logic into a feature
- Features importing service internals (`billing-stripe`) instead of the public API
- A `utils/payments.ts` dumping ground with no clear public contract

### 2. Deep public surface (one simple entry point)

Hide messy orchestration behind **one deep** thing the caller uses — **simple interface, rich functionality** (Ousterhout deep module). For a domain concern, that entry **is the service's public API**. For UI, it's usually a hook that **calls** services.

| Shape | When |
| --- | --- |
| **Service** (module / class / facade) | Domain capability shared across features (default for auth, billing, …) |
| React hook (`useX`) | UI state/effects/subscriptions — delegates domain work to services |
| Class / abstract class | Stateful domain behavior, shared lifecycle (often *is* the service) |
| Narrow function API | Pure transforms with a clear input→output |

Rules:

- The entry point's signature should be obvious in one glance
- Call sites should not know about helpers, parsers, adapters, or edge-case branches
- One main export / one main type per file when practical
- Prefer **class** for stateful domain behavior; hooks for React; **service** for shared domain I/O — details in `/taste`
- Pull complexity **down** into collaborators and **primitives** (§3); keep the public surface deep

The entry point is not always a TypeScript `interface`. Pick the shape that fits the stack.

Anti-pattern: **shallow modules** — complex interface relative to what they do (many params/options/leaked steps, callers still orchestrate the how).

### 3. Primitives (building blocks inside deep modules)

A **primitive** is a **small piece of code** that is **strong yet flexible** and answers **one very specific thing**. It can be **reused independently without breaking**. Primitives are the **strong blocks** you build with — the pieces **inside services and deep modules**.

| Property | Meaning |
| --- | --- |
| **Small** | Narrow scope — not a feature, not a god module |
| **One specific job** | Answers one question / does one thing well |
| **Strong** | Deep enough that callers do not reimplement that job |
| **Flexible** | Composes / chains; reuse does not force brittle coupling |
| **Independent reuse** | Call sites can use it without breaking it or each other |
| **Placement** | Lives **inside** services and deep modules — building blocks of those, not a rival top-level architecture |

The deep public surface (§2) is what callers see. **Primitives** are how that depth stays real without leaking every concern to every call site. Services own domain capabilities; **primitives sit inside** them (and other deep modules).

Rules:

1. Prefer **building with primitives** — small one-job blocks — over duplicating that job at call sites.
2. **Explore first** — reuse an existing primitive when it already answers that specific thing.
3. When creating one: keep it **small, one job, strong yet flexible**, safe to reuse independently.
4. Place it **inside** the owning service / deep module (or a shared layer those modules compose) — not a dumping-ground `utils`.
5. **Do not fork** a primitive's job in a feature or sibling helper.
6. Reason from this **definition** — discover primitives by exploring **this** repo. Do **not** invent a canned catalog from training data.

Anti-patterns:

- Forking a primitive's job locally (complexity + entropy — see `/taste`)
- Thin identity wrappers that only rename with no strength
- Sprawling helpers that answer many things (not one specific job)
- Promoting primitives to a parallel top-level architecture that rivals services

### 4. Prior mistakes are not sacred (behavior-preserving moves)

Flawed existing layout is **debt**, not a template. Do not freeze wrong placements because "it was already there." Leaving or copying wrong placement is **entropy growth** (`/taste`).

When explore shows wrong folder, duplicated domain logic, a feature-forked service (billing/auth inside a feature), or a sibling that violates this skill / `/taste`, first decide whether the active goal or a named review finding requires a move:

- **Do not copy it.** Cite a *good* sibling or service — or create the correct shape.
- If required, prefer a **behavior-preserving move**: relocate into the right service/folder, extract the public API, rewire callers, delete the dead path — this **reduces entropy**. If not required, capture it as a follow-up rather than expanding the goal.
- Name the old observable behavior and how you will prove it still holds (**existing** tests if any, path walk + `/validate` / terminals). Do **not** write new tests here — locks are `/create-test` only after `/code-review` or `/pr-review` recommends them. If you **cannot** be sure the move preserves behavior → include the move in the next `/grill-me` Questions batch. If the move is required and you can preserve behavior → do it; otherwise keep it as a follow-up.
- Update the Structure card (**Moves / corrections**) before coding; mid-implement → patch the plan Structure, then move.
- Same spirit as `/code-review` code judo — apply it while **building**, not only at review time.

Anti-patterns:

- Bolting new code onto a known-wrong shape "because it was already there" (entropy)
- Copying a bad sibling to stay consistent with debt (entropy)
- Asking "leave it where it is?" as the recommended option when a clear move preserves behavior

### 5. Folders before files

Never sprinkle related files across a flat directory. **Propose the folder map before creating files.**

1. Mirror existing repo conventions (services folder, feature folder, domain folder) — explore first
2. Prefer **`services/<concern>/`** (or the repo's equivalent) for shared domain APIs; **feature folders** for product UI/orchestration that *calls* those services
3. If no convention fits, create a **feature/domain folder** and put the cluster inside it
4. Colocate what changes together; separate what changes for different reasons
5. Name files per **`/taste`** — `lowercase-with-hyphens` in app/UI; **no `-` or `_` in `convex/` filenames**
6. Avoid `utils.ts` / `helpers.ts` dumping grounds — name the concept (often: promote to a service, or a **primitive** inside one — §3)
7. Cite a **good** sibling feature **or existing service** when one exists (taste: cite-a-sibling) — bad nearby code is debt to move, not a template

Anti-pattern: five new sibling files next to unrelated code with no folder; or a new "payments helper" beside a feature when a billing service should own it.

### 6. Small collaborating parts

Inside the folder, split by responsibility — public entry, then **primitives** and collaborators:

```text
# Service (domain)
services/billing/
  billing.ts               # public API — only thing features import
  billing-stripe.ts
  billing-types.ts

# Feature (product slice — calls services)
features/checkout/
  use-checkout.ts          # entry — orchestrates UI + billing.makeUserPay
  checkout-types.ts
  components/
    checkout-form.tsx
```

Convex modules live under `convex/` with **taste naming** (`billing.ts`, not `billing-actions.ts`). A Convex service module still exposes a small public set of queries/mutations/actions; features call those — they don't duplicate Stripe/auth logic in another Convex file.

Adjust names to the repo. Keep depth shallow: public entry → primitives / collaborators → leaf helpers. Never-nest deep control flow; extract instead.

### 7. Scalable by default (critical — AI often gets this wrong)

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
- Don't N+1: batch or denormalize fields needed for list views
- Client components should display data, not be the analytics engine
- Expensive derived views → materialize (table/columns/summary doc), not "calculate on render"

If a one-off admin script needs a full scan, say so explicitly — never copy that pattern into hot product paths.

## Process

### 1. Explore

Read nearby folders. Note:

- **Existing services** for the same concern (billing, auth, …) — reuse/extend first
- **Existing primitives** inside those services / deep modules — reuse when they already answer that specific job; do not fork
- **Wrong existing shape in the lane** — feature-forked domain logic, bad sibling, misplaced files (do not copy; plan a behavior-preserving move only when current scope requires it)
- How similar features call those services (public API only?)
- Existing entry-point patterns (services vs hooks vs classes vs modules)
- Naming and import style
- Whether siblings store aggregates on write or recompute on read (prefer the former)

### 2. Draft the structure card

Present this before writing code (and include it in `/create-plan` when planning under `/goal`):

```markdown
## Structure

**Services:**
- **Owns / extends:** `path` — public API: `makeUserPay(…)`, … (or _n/a — pure UI_)
- **Calls (existing):** `billing.makeUserPay`, `auth.requireUser`, … — never reimplements these
- **Must not duplicate:** <Stripe / JWT / email provider / …>
**Moves / corrections:** <required by INV-1 / AC / named finding: relocate X → services/billing; delete old path> | _none_
**Feature entry:** `path` — `useX` | `ClassX` | `fn` — one-line contract (orchestrates services + UI); **deep** surface
**Primitives:**
- **Reuse (existing):** cite path + one-line job | _none_
- **New / extend:** path — one specific job; how it stays reusable without breaking
- **Inside:** which service / deep module owns it
**Hidden behind services / entry:** bullet list of responsibilities callers must not see
**Complexity / entropy:** public API deep? primitives reused not forked? change reduces or holds entropy in touched lane? (see `/taste`)
**Extension seam (if big service):** foundation from day one — how the next provider/variant plugs in without breaking the public API (ship seam + first impl together)
**Scalability:**
- Hot reads: <what the UI/query returns>
- Stored on write: <columns / summary table / parent fields updated on insert>
- Indexes: <index names / fields>
- Explicitly NOT recomputed on render/read: <metrics>
**Folder map:**
- `services/<concern>/` (or repo equivalent)
  - `<concern>.ts`          # public API
  - collaborator…
- `features/<slice>/`       # calls services — no domain fork
  - entry + UI…
**Fits existing pattern:** yes (cite **good** service / feature) | correcting debt (what) | new (why)
**Taste:** follows `/taste` naming + entry shape + ≤2 class/interface depth
```

If service boundary, public API shape, **primitives** (reuse vs new vs fork), folder root, write-vs-read, or a **move vs leave** decision is open, put **all** open structure questions in **one** `/grill-me` Questions batch (`Reply like: 1a 2b` per [asking.md](../asking.md)). Recommend a behavior-preserving move when it is required by the goal or finding and you can prove old behavior holds; otherwise name it as a follow-up. Do not drip them one message at a time. New findings later → new batch.

### 3. Implement against the card

- When a service or feature boundary is justified, create its folder before its files
- Perform **Moves / corrections** before bolting new feature code onto the old shape
- Put domain logic in the **service**; features call public functions only
- Build depth with **primitives** inside the service / deep module — reuse existing ones; do not fork their jobs
- Wire collaborators so the public API is the only thing most call sites import
- Do not export service internals unless another package truly needs them
- Implement aggregate updates on the **write path** when the card says so

### 4. Self-check before done

- [ ] Domain concerns live in a **service** with a clear public API (or an existing one was extended)
- [ ] Features **call** that API — no forked billing/auth/notifications/… inside the feature
- [ ] **Primitives:** one job each; reused not forked; sit inside the owning service / deep module; strong yet flexible (not identity wrapper, not god helper)
- [ ] Prior mistakes in the lane were not copied; required moves were completed and optional ones are follow-ups
- [ ] No feature imports service internals
- [ ] A new reader can use the feature from its entry point alone
- [ ] Related new files share one folder (or an existing convention)
- [ ] No flat file dump / no anonymous `utils` bag standing in for a service
- [ ] Public API is **deep** (simple surface); complexity is inside collaborators / primitives, not at every call site
- [ ] Change **reduces or holds entropy** in the touched lane (no copy/extend of known-wrong shape without a move)
- [ ] `/taste` naming and error style respected
- [ ] No hot-path "compute metrics on render/read" — aggregates stored and updated on write
- [ ] Indexes cover the queries; no unbounded collect on growing data
- [ ] Observable old behavior still holds (tests / path walk / terminals) after any move

## When `/create-plan` or `/implement` should invoke this

- New feature with more than one new file
- Any domain capability (payments, auth, email, …) a second feature might need
- Temptation to copy Stripe/auth/email logic into a feature **or leave it misplaced**
- Clear prior mistake in the lane (wrong folder / duplicated service) when the current goal or named finding requires a behavior-preserving move
- Extracting logic from a large file
- Adding React state/effects that would otherwise bloat a component
- Any change that would add files without a parent folder
- Any feature with lists, dashboards, counts, totals, leaderboards, or "stats"
- Any query that would scan children to answer a parent-level question

Hand off: structure card → `/goal` (plans via `/create-plan`). `/validate` will fail scale anti-patterns **and** duplicated-service anti-patterns under `/goal`. Under `/goal` → `/architecture` → `/create-plan`.

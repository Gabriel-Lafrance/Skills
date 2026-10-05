# Code structure examples

Good vs bad. Match **good**.

## Services own domain capabilities

**Bad:** checkout and upgrade each call `stripe.checkout.sessions.create(...)` ("just this once").

**Good:** one billing service; features call its public API.

```text
services/billing/
  billing.ts            # makeUserPay, refundPayment: the only exports features import
  billing-stripe.ts     # private: Stripe, webhooks, idempotency
features/checkout/      # UI + orchestration: await makeUserPay({ userId, cents, reason: "checkout" })
features/upgrade/       # same call, reason: "upgrade"
```

**Bad:** `import { createStripeSession } from "@/services/billing/billing-stripe";`
**Good:** `import { makeUserPay } from "@/services/billing/billing";`

## Reuse env vars

**Bad:** `process.env.FRONTEND_URL` when `SITE_URL` already holds the site URL.
**Good:** `process.env.SITE_URL` (`quality:reuse-env`).

## Deep vs shallow service API

**Bad:** the feature orchestrates the service's collaborators.

```typescript
const session = await createStripeSession(input);
await recordPaymentAttempt(session.id);
await sendReceiptEmail(session.id);
```

**Good:** `await makeUserPay({ userId, cents, reason: "checkout" });` with session, ledger, and receipt inside `billing.ts`.

## Meaningful extraction with one consumer

**Bad:** `report-export.ts` coordinates authorization and report loading, but
also encodes CSV rows and holds storage SDK calls, upload cleanup, and expiry
handling. Appending another integration there makes CSV changes require reading
transport/lifecycle code. Renaming those chunks `csvHelper` and `storageHelper`
without hiding their rules from the caller does not fix the boundary.

**Good:** retain one public report-export entry; give distinct behavior a named
private owner. Suppose research confirms export owns its storage integration
and there is no existing shared storage service to reuse:

```text
services/report-export/
  report-export.ts       # public exportReport(input): authorize, load, coordinate, return artifact
  csv-renderer.ts        # private: CSV header, escaping, row encoding
  export-storage.ts      # private: SDK translation, artifact write and cleanup lifecycle
  report-export.test.ts  # relevant existing/accepted public-entry checks, if repo convention fits
```

Features call `exportReport`, not `renderCsv` then `upload` then `cleanup`.
The renderer may have only this consumer; it earns its file by owning encoding
behavior, not by being reused twice. Its header, escaping, and row steps stay
together instead of becoming `header.ts`, `escape-cell.ts`, and `row.ts` files
that force readers to reconstruct the same operation. Storage details remain
behind the owning integration. If a storage service already owns that work,
call its public API rather than create a rival export-storage implementation.
Related contract types or cohesive public operations may stay beside the entry;
unrelated jobs do not become extra exports there.

**Retrieval check:** a CSV escaping question leads from `exportReport` to
`csv-renderer.ts`; only the relevant entry/caller and renderer need inspection.
An SDK-specific change lands in the storage owner and its affected boundary
checks, without changing CSV encoding. Verify the real data and failure contracts
still fit before calling the move behavior-preserving. A split that leaves the
caller coordinating partial cleanup or reading all internals has not earned
its extra files. The example is illustrative, not permission to add tests.

**Keep whole:** an existing small `renderCsv(rows)` whose header, escaping, and
row iteration share one formatting contract needs no new folders or wrappers
for an empty-header fix. Length, function count, and file count do not decide
the boundary; responsibilities and reader/caller burden do.

**Navigate selectively:** for that fix, start at the known renderer signature,
inspect its implementation and the caller that constrains its output, and use
the existing relevant checks. For an unfamiliar export flow, a compact existing
handoff can point to `report-export.ts` (public operation), `csv-renderer.ts`
(encoding), and the storage owner (artifact lifecycle). Expand only if their
callers, schema, or dependency evidence changes the answer. Neither task needs
a new repository index or unrelated billing/auth implementation dumps.

## Prior mistakes are not sacred (move, don't copy)

**Bad:** checkout already calls Stripe directly; the agent copies that into upgrade "to match."
**Good:** move Stripe into `services/billing/billing.ts` (`makeUserPay`), point both features at it, delete the old path. Prove old behavior holds (tests, path walk, terminals). Do not recommend "leave checkout as-is" when the move is clear.

## Folders before files

**Bad:** a new concern dumped in a mixed parent (even one file).

```text
src/
  page.tsx
  useOrders.ts
  orderApi.ts
  OrderCard.tsx
  formatMoney.ts
```

**Good:** owning folder first; collaborators one level down.

```text
src/orders/
  use-orders.ts          # entry: call sites import this
  orders-api.ts
  format-money.ts
  components/
    order-card.tsx
```

**Bad:** `convex/billingStripe.ts` beside `convex/billing.ts`.
**Good:** move the cluster to `convex/billing/billing.ts` (public) + `convex/billing/stripe.ts` (private). Never keep both `billing.ts` and `billing/`.

**Bad:** `services/billing/stripe/v2/internal/helpers/`.
**Good:** owning folder + public entry + collaborators + at most one leaf folder.

## Entry point hides collaborators

**Bad:** `page.tsx` runs `api.orders.list.collect()` and reduces the total itself.
**Good:** `const { orders, totalCents, loadMore } = useOrders(userId);`

## Metrics: compute on write, not on read

**Bad:** `getUserStats` collects every order for the user and sums on each query.

**Good:** store the aggregate on the user and bump it in the same mutation.

```typescript
export const createOrder = mutation({
  args: { userId: v.id("users"), cents: v.number() },
  handler: async (ctx, args) => {
    await ctx.db.insert("orders", args);
    const user = await ctx.db.get(args.userId);
    if (!user) throw new Error("User not found");
    await ctx.db.patch(args.userId, {
      orderCount: user.orderCount + 1,
      orderTotalCents: user.orderTotalCents + args.cents,
    });
  },
});
```

`getUserStats` then reads `user.orderCount` and `user.orderTotalCents`.

## Lists: cursor pagination, not unbounded collect

**Bad:** `(await ctx.db.query("posts").collect()).sort(...)`
**Good:** `ctx.db.query("posts").withIndex("by_creation").order("desc").paginate(args.paginationOpts)`

UI: `usePaginatedQuery` (or equivalent) loads near the bottom and appends pages; the list does not remount.

## Indexes over filters

**Bad:** `ctx.db.query("orders").filter((q) => q.eq(q.field("userId"), userId))`
**Good:** `ctx.db.query("orders").withIndex("by_user", (q) => q.eq("userId", userId))`

## List cards: denormalize what the row needs

**Bad:** per post in a feed, `ctx.db.get(post.authorId)` and a like-count scan (N+1).
**Good:** store `authorName` and `likeCount` on the post; bump `likeCount` when a like is inserted.

## Foundation seam (big service)

**Bad:** Stripe hardcoded in every feature; PayPal forces a rewrite of checkout, upgrade, and invoices.
**Good:** day one, behind the billing public API:

```text
services/billing/
  billing.ts             # public: makeUserPay / refundPayment
  payment-method.ts      # seam
  stripe-payment.ts      # first impl
```

The next provider is a new file behind the seam.

## Foundation patterns (folder trees)

One tree per pattern [strong-foundation.md](strong-foundation.md#build-it) names. Each ships with one real implementation. Pick the pattern that matches the area of modularity; do not stack them.

**Adapter:** an outside vendor varies (payment, email, storage provider). Each adapter turns one vendor's API into the app's interface.

```text
services/email/
  email.ts               # public: sendReceipt, sendInvite
  email-sender.ts        # seam: interface EmailSender { send(message) }
  resend-sender.ts       # adapter for the first vendor
```

**Strategy:** a rule or algorithm varies (pricing, tax, ranking). Same inputs, different decision.

```text
services/pricing/
  pricing.ts             # public: priceFor(order)
  pricing-rule.ts        # seam: interface PricingRule { apply(order) }
  flat-rate-rule.ts      # first strategy
```

**Registry:** several variants live side by side and the caller picks one by key (providers, channels, export formats).

```text
services/exports/
  exports.ts             # public: exportReport(report, format)
  exporter.ts            # seam: interface Exporter
  exporters.ts           # registry: { csv: csvExporter }
  csv-exporter.ts        # first variant
```

Adding a format is one file plus one registry line. `exports.ts` never grows an `if (format === ...)`.

**State machine:** an entity moves through phases and some moves are forbidden (orders, subscriptions, invites).

```text
services/orders/
  orders.ts              # public: placeOrder, cancelOrder, refundOrder
  order-states.ts        # seam: states and allowed transitions in one table
```

**Bad:** `isPaid`, `isCancelled`, and `isRefunded` booleans that must stay in sync, checked in five files.
**Good:** one `status` field and one transition table. A new state is a row, and an illegal move fails in one place.

## OOP depth

**Bad:** `AbstractPayment` > `BaseCard` > `StripeCard` > `StripeCardV2`.
**Good:** `PaymentMethod` <- `StripePayment`, or compose a client inside one class (two levels max).

## Scalability N/A (when it's fine)

**OK:** a one-off admin script collects under 100 `featureFlags` rows. Never copy that into a user-facing dashboard.

## Authority lives on the write

**Bad:** the UI hides Pay; `chargeCart({ userId, cents })` inserts a payment for whatever the client sent.

**Good:** identity, ownership, and amount from stored state, in one write.

```typescript
export const chargeCart = mutation({
  args: { cartId: v.id("carts") },
  handler: async (ctx, args) => {
    const user = await requireUser(ctx);
    const cart = await ctx.db.get(args.cartId);
    if (!cart) throw new Error("Cart not found");
    if (cart.userId !== user._id) throw new Error("Unauthorized");
    await makeUserPay(ctx, { userId: user._id, cents: cart.totalCents });
  },
});
```

## Deterministic queries (no wall clock)

**Bad:** a query reads `Date.now()`, collects all tasks, and filters `dueAt > now`.
**Good:** set `status` on write (or in a scheduled mutation); the query reads it by index.

```typescript
return await ctx.db
  .query("tasks")
  .withIndex("by_user_and_status", (q) => q.eq("userId", args.userId).eq("status", "active"))
  .paginate(args.paginationOpts);
```

# Architecture examples

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
**Good:** `process.env.SITE_URL` (`taste:reuse-env`).

## Deep vs shallow service API

**Bad:** the feature orchestrates the service's collaborators.

```typescript
const session = await createStripeSession(input);
await recordPaymentAttempt(session.id);
await sendReceiptEmail(session.id);
```

**Good:** `await makeUserPay({ userId, cents, reason: "checkout" });` with session, ledger, and receipt inside `billing.ts`.

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

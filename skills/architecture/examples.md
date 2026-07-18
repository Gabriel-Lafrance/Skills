# Architecture examples

Concrete good vs bad. Prefer matching **good**.

## Services own domain capabilities

**Bad** — each feature invents its own billing:

```typescript
// features/checkout/checkout.ts
await stripe.checkout.sessions.create({ … });

// features/upgrade/upgrade.ts
await stripe.checkout.sessions.create({ … }); // copy-paste “just this once”
```

**Good** — one billing service; features call it:

```typescript
// services/billing/billing.ts — public API
export async function makeUserPay(input: MakeUserPayInput): Promise<PaymentResult> {
  // Stripe / webhooks / idempotency live here — not in features
}

// features/checkout/use-checkout.ts
await makeUserPay({ userId, cents, reason: "checkout" });

// features/upgrade/use-upgrade.ts
await makeUserPay({ userId, cents, reason: "upgrade" });
```

```text
services/billing/
  billing.ts            # makeUserPay, refundPayment — only exports features import
  billing-stripe.ts     # private
features/checkout/      # UI + orchestration — calls makeUserPay
features/upgrade/       # same
```

**Bad** — feature reaches into service internals:

```typescript
import { createStripeSession } from "@/services/billing/billing-stripe";
```

**Good** — public API only:

```typescript
import { makeUserPay } from "@/services/billing/billing";
```

## Prior mistakes are not sacred (move, don’t copy)

**Bad** — leave Stripe in checkout and add another copy in upgrade “to match existing”:

```typescript
// features/checkout/checkout.ts — already wrong
await stripe.checkout.sessions.create({ … });

// features/upgrade/upgrade.ts — agent copies the debt
await stripe.checkout.sessions.create({ … });
```

**Good** — behavior-preserving move into a billing service; both features call it; old path deleted:

```typescript
// services/billing/billing.ts
export async function makeUserPay(input: MakeUserPayInput): Promise<PaymentResult> {
  // moved Stripe / idempotency here
}

// features/checkout + features/upgrade — same call, same outcomes as before
await makeUserPay({ userId, cents, reason: "checkout" /* or upgrade */ });
```

Prove old behavior still holds (tests / path walk / terminals). Do not recommend “leave checkout as-is” when this move is clear.

## Folders before files

**Bad** — flat dump next to unrelated code:

```text
src/
  page.tsx
  useOrders.ts
  orderApi.ts
  orderTypes.ts
  OrderCard.tsx
  OrderList.tsx
  formatMoney.ts
```

**Good** — feature folder + simple entry:

```text
src/orders/
  use-orders.ts          # entry — call sites import this
  orders-api.ts
  orders-types.ts
  components/
    order-card.tsx
    order-list.tsx
  format-money.ts
```

## Entry point hides collaborators

**Bad:**

```typescript
// page.tsx orchestrates everything
const rows = await api.orders.list.collect();
const total = rows.reduce((s, o) => s + o.cents, 0);
```

**Good:**

```typescript
const { orders, totalCents, loadMore } = useOrders(userId);
```

## Metrics: compute on write, not on read

**Bad** — recalculate on every query/render:

```typescript
export const getUserStats = query({
  args: { userId: v.id("users") },
  handler: async (ctx, { userId }) => {
    const orders = await ctx.db
      .query("orders")
      .withIndex("by_user", (q) => q.eq("userId", userId))
      .collect(); // grows forever

    return {
      orderCount: orders.length,
      orderTotalCents: orders.reduce((s, o) => s + o.cents, 0),
    };
  },
});
```

**Good** — store on the user (or summary row); bump on insert:

```typescript
// schema: users.orderCount, users.orderTotalCents

export const createOrder = mutation({
  args: { userId: v.id("users"), cents: v.number() },
  handler: async (ctx, args) => {
    await ctx.db.insert("orders", { userId: args.userId, cents: args.cents });
    const user = await ctx.db.get(args.userId);
    if (!user) throw new Error("User not found");
    await ctx.db.patch(args.userId, {
      orderCount: user.orderCount + 1,
      orderTotalCents: user.orderTotalCents + args.cents,
    });
  },
});

export const getUserStats = query({
  args: { userId: v.id("users") },
  handler: async (ctx, { userId }) => {
    const user = await ctx.db.get(userId);
    if (!user) throw new Error("User not found");
    return {
      orderCount: user.orderCount,
      orderTotalCents: user.orderTotalCents,
    };
  },
});
```

## Lists: cursor pagination, not unbounded collect

**Bad:**

```typescript
const all = await ctx.db.query("posts").collect();
return all.sort((a, b) => b._creationTime - a._creationTime);
```

**Good:**

```typescript
return await ctx.db
  .query("posts")
  .withIndex("by_creation")
  .order("desc")
  .paginate(args.paginationOpts);
```

UI: seamless scroll / load-near-bottom with `usePaginatedQuery` (or equivalent) — append pages, don’t remount the list.

## Indexes over filters

**Bad:**

```typescript
ctx.db.query("orders").filter((q) => q.eq(q.field("userId"), userId));
```

**Good:**

```typescript
ctx.db
  .query("orders")
  .withIndex("by_user", (q) => q.eq("userId", userId));
```

## List cards: denormalize what the row needs

**Bad** — N+1 while rendering a feed:

```typescript
for (const post of posts) {
  post.author = await ctx.db.get(post.authorId);
  post.likeCount = await countLikes(ctx, post._id); // scan
}
```

**Good** — store `authorName`, `likeCount` on the post; update `likeCount` when a like is inserted.

## Foundation seam (big service)

**Bad** — Stripe hardcoded in every feature; PayPal forces a rewrite of checkout + upgrade + invoices.

**Good** — day one, behind the billing service public API:

```text
services/billing/
  billing.ts             # public: makeUserPay / refundPayment
  payment-method.ts      # seam (interface / abstract)
  stripe-payment.ts      # first impl
```

Features only call `makeUserPay`; next provider is a new file behind the seam — not a new copy in each feature.

## OOP depth

**Bad:** `AbstractPayment` → `BaseCard` → `StripeCard` → `StripeCardV2`  
**Good:** `PaymentMethod` ← `StripePayment`, or compose a client inside one class (≤ 2 levels)

## Scalability N/A (when it’s fine)

**OK to recompute** — bounded, tiny, admin-only:

```typescript
// one-off admin script: < 100 config rows, not a product hot path
const flags = await ctx.db.query("featureFlags").collect();
```

Never copy that into a user-facing dashboard.

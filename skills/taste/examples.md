# Taste examples

Good vs bad. Match **good**.

## KISS (Keep It Stupid Simple)

**Bad:** a helper file for one call site.

```typescript
// order-guards.ts
export function assertCanCheckout(user: User) { if (!user.canOrder) throw new Error("Cannot order"); }
```

**Good:** the guard stays with its one caller.

```typescript
const user = await requireUser(input.userId);
if (!user.canOrder) throw new Error("Cannot order");
```

**Bad:** `interface NotifierStrategy` + empty `abstract class BaseNotifier` + `ConsoleNotifier` for one `console.log`.
**Good:** `async function notifyUser(msg: string) { console.log(msg); }`. Big features still get one seam + one impl ([reference.md](reference.md#futureproofing)).

## Named principles (spot checks)

| Principle | Bad | Good |
| --- | --- | --- |
| Keep jobs apart | React component calls Stripe and formats receipts | Component calls `billing.makeUserPay`; billing owns Stripe |
| One altitude | `placeOrder` validates, parses a CSV attachment, and charges | `placeOrder` coordinates `parseOrderAttachment`, then `charge` |
| Read or write, not both | `getCart()` also writes a "last seen" row | `getCart()` reads; `touchCartSeen()` writes |
| Fail fast | Invalid `userId` found after creating a payment intent | `requireUser` throws at the entry, before side effects |
| Leave it cleaner | Copy a known-wrong sibling "to match" | Move the Stripe call into `billing` while in the lane (same behavior) |
| Related together | Feature imports `billing-stripe-internal` | Feature imports only `billing.makeUserPay` |
| Safe to retry | Webhook inserts an order on every delivery | Key by event id; second delivery is a no-op |
| Say what happens / no surprises | `save()` sometimes returns null, sometimes throws, sometimes writes a global | `save()` throws on failure, returns the id, no hidden writes |
| Honest names | Scope became "payment intent" but code stays `createCheckoutTotal` in `checkout-total.ts` | Rename to `create-payment-intent.ts` / `createPaymentIntent` and callers in the same change |
| Trust the server | Pay button disabled in React; mutation charges any client `userId` | Mutation calls `requireUser` and checks cart ownership; button is feedback |
| Types tell the truth | `args: { data: v.any() }`, or `userId?: string` when every caller passes one | `args: { userId: v.id("users"), cents: v.number() }` |

## Deep vs shallow module

**Bad:** the caller orchestrates internals.

```typescript
const items = await loadCart(userId);
new CartStore().setItems(applyTax(items));
```

**Good:** `const cart = useCart(userId);`

## Entropy / broken window

**Bad:** `features/upgrade/upgrade.ts` calls `stripe.checkout.sessions.create(...)` because checkout did.
**Good:** move Stripe into `services/billing/billing.ts`; upgrade calls `makeUserPay({ userId, cents, reason: "upgrade" })` (`architecture:prior-mistakes`).

## Never-nest

Flatten control flow, not the folder tree (`architecture:folders`).

**Bad:**

```typescript
if (input.userId) {
  const user = await getUser(input.userId);
  if (user) { if (user.canOrder) { try { return await charge(user, input); } catch (e) { /* retry */ } } }
}
return null;
```

**Good:**

```typescript
const user = await requireUser(input.userId);
user.assertCanOrder();
return await chargeWithRetry(user, input);
```

## Cyclomatic cap

**Bad:** one `priceOrder` with an empty check, a loop, an `if / else if` on item kind, a coupon `if`, and a ternary floor.
**Good:** each function stays at five paths or fewer.

```typescript
function priceOrder(order: Order): number {
  return floorAtZero(applyCoupon(sumItemPrices(order.items), order.coupon));
}
```

## Reuse env vars

**Bad:** `SITE_URL` exists; the agent runs `npx convex env set FRONTEND_URL ...` and reads `process.env.FRONTEND_URL`.
**Good:** `const origin = process.env.SITE_URL;`. A client prefix uses `NEXT_PUBLIC_SITE_URL`, not `NEXT_PUBLIC_FRONTEND_URL`. A library that wants `FRONTEND_URL` gets it mapped in code.

## Dead code

**Bad:** `export function formatLegacyReceipt()` with no callers survives refactors.
**Good:** delete it. Version control remembers.

## Decoration lock

**Bad:** a test calls `charge(card)` and asserts nothing; `>` becoming `>=` in pricing stays green.
**Good:** `assert.equal(receipt.cents, 500)`. The broken operator fails.

## Errors

**Bad:**

```typescript
function parseConfig(raw: string): { ok: true; value: Config } | { ok: false; error: string } {
  if (!raw) return { ok: false, error: "empty" };
```

**Good:**

```typescript
function parseConfig(raw: string): Config {
  if (!raw) throw new Error("Config is empty");
```

## Naming

| Area | Good | Bad |
| --- | --- | --- |
| App UI | `features/orders/components/order-summary.tsx` | `OrderSummary.tsx` beside five unrelated siblings |
| Convex names | `convex/orders.ts`, `convex/orderActions.ts` | `convex/order-actions.ts`, `convex/order_actions.ts` |
| Convex folders | Second billing file goes in `convex/billing/` | `convex/billingStripe.ts` beside `convex/billing.ts` |

## Speculative ceremony (tiny work)

**Bad:** `IFmt`, `FmtImpl`, `FmtFactory` for a one-line string helper.
**Good:** a plain function.

## Foundation first (big features)

**Bad:** `StripeOnly` hardcoded at every call site; PayPal forces a rewrite.
**Good:** day one, a `PaymentMethod` seam + `StripePayment` behind a stable `charge()`. The next provider is a new collaborator.

## Smart responsibility

**Bad:** `Logger.log` also posts to Slack and calls `analytics.track`.
**Good:** `Logger.log` only logs; the orchestrator calls Slack and analytics.

## OOP depth

**Bad:** `AbstractPayment` > `BaseCardPayment` > `StripeCardPayment` > `StripeCardPaymentV2`.
**Good:** `PaymentMethod` <- `StripeCardPayment`, or compose `StripeClient` inside one class.

## Futureproof extension seam

**Bad:** every new channel adds `if (channel === ...)` to `notify()`.
**Good:** stable `Notifier.notify(event)` with a `Channel` strategy from the start, first channel implemented.

## SOLID theater vs foundation

**Bad:** `IUserRepo`, `UserRepoImpl`, `UserRepoFactory`, `IUserRepoFactory` for a one-off script.
**Good (big domain):** a `UserRepository` contract + one real store on day one, so a second store does not change callers.
**Also bad:** delaying that contract "until we have two stores," then rewriting half the feature.

## Verify

**Bad:** `npm run lint && tsc --noEmit && npm test` after every edit.
**Good:** read the running frontend and `convex dev` terminals; dig deeper only if they show errors.

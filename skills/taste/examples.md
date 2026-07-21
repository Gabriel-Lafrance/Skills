# Taste examples

Concrete good vs bad. Prefer matching **good**.

## Deep vs shallow module (entry point vs leaked helpers)

**Bad — shallow module** — call site orchestrates internals (high complexity at every caller):

```typescript
import { loadCart } from "./cart-load";
import { applyTax } from "./cart-tax";
import { CartStore } from "./cart-store";

const store = new CartStore();
const items = await loadCart(userId);
store.setItems(applyTax(items));
```

**Good — deep module** — simple surface, rich behind it:

```typescript
import { useCart } from "./use-cart";

const cart = useCart(userId);
```

## Entropy / broken window

**Bad** — copy a known-wrong sibling so the new feature "matches" debt (entropy spreads):

```typescript
// features/upgrade/upgrade.ts — Stripe wired here because checkout did it that way
await stripe.checkout.sessions.create({ … });
```

**Good** — behavior-preserving move into the right service; cite the good shape (`/architecture` §4):

```typescript
// services/billing/billing.ts — makeUserPay owns Stripe
// features/upgrade/use-upgrade.ts
await makeUserPay({ userId, cents, reason: "upgrade" });
```

## Never-nest

**Bad:**

```typescript
async function placeOrder(input: Input) {
  if (input.userId) {
    const user = await getUser(input.userId);
    if (user) {
      if (user.canOrder) {
        try {
          return await charge(user, input);
        } catch (e) {
          if (isRetryable(e)) {
            return await charge(user, input);
          }
        }
      }
    }
  }
  return null;
}
```

**Good:**

```typescript
async function placeOrder(input: Input) {
  const user = await requireUser(input.userId);
  user.assertCanOrder();
  return await chargeWithRetry(user, input);
}
```

## Errors

**Bad:**

```typescript
function parseConfig(raw: string): { ok: true; value: Config } | { ok: false; error: string } {
  if (!raw) return { ok: false, error: "empty" };
  return { ok: true, value: JSON.parse(raw) };
}
```

**Good:**

```typescript
function parseConfig(raw: string): Config {
  if (!raw) throw new Error("Config is empty");
  return JSON.parse(raw) as Config;
}
```

## Naming

**App UI — good:** `components/order-summary.tsx`, `hooks/use-checkout.ts`  
**App UI — bad:** `OrderSummary.tsx` next to five unrelated siblings with no folder  

**Convex — good:** `convex/orders.ts`, `convex/orderActions.ts`  
**Convex — bad:** `convex/order-actions.ts`, `convex/order_actions.ts`

## Speculative ceremony (tiny work)

**Bad** — `IFmt`, `FmtImpl`, `FmtFactory` for a one-line string helper  
**Good** — a plain function

## Foundation first (big features)

**Bad** — hardcode `StripeOnly` into every call site; rip everything open when PayPal arrives  
**Good** — day one: `PaymentMethod` seam + `StripePayment` behind a stable `charge()` entry; next provider is a new collaborator, not a rewrite

## Smart responsibility

**Bad** — logger also notifies Slack and writes analytics:

```typescript
class Logger {
  log(message: string) {
    console.log(message);
    void fetch("/slack", { body: message });
    analytics.track("log", message);
  }
}
```

**Good** — logger only logs; others subscribe or get called by the orchestrator:

```typescript
class Logger {
  log(message: string) {
    console.log(message);
  }
}
```

## OOP depth

**Bad** — `AbstractPayment` → `BaseCardPayment` → `StripeCardPayment` → `StripeCardPaymentV2`  
**Good** — `PaymentMethod` ← `StripeCardPayment`, or compose `StripeClient` inside one payment class

## Futureproof extension seam

**Bad** — every new channel edits `notify()` with another `if (channel === …)`  
**Good** — stable `Notifier.notify(event)`; `Channel` strategy in place from the start with the first channel implemented

## SOLID theater vs foundation

**Bad** — `IUserRepo`, `UserRepoImpl`, `UserRepoFactory`, `IUserRepoFactory` for a trivial one-off script  
**Good (big domain)** — `UserRepository` contract (or interface) + one real store behind the feature entry on day one, so a second store does not force callers to change  
**Also bad** — delaying that contract “until we have two stores,” then rewriting half the feature

## Verify

**Bad** — after every edit: `npm run lint && tsc --noEmit && npm test`  
**Good** — read the already-running frontend + `convex dev` terminals; only dig deeper if those show errors

# Journey: a follow-up that fits the seam

**The user says:** "Add PayPal as a payment option." No ticket, just the chat message.
**Comes after:** [a new Feature on a strong foundation](new-feature.md). **If it does not fit:** [a follow-up that needs a seam first](follow-up-needs-a-seam.md).

```mermaid
flowchart LR
  ask[User: add PayPal] --> build[task]
  build --> sibling[Sibling: stripe-provider.ts]
  sibling --> diff[One adapter plus one registry entry]
  diff --> review[review]
```

## 1. Route

Open `task/SKILL.md`. With no ticket, the grill works from the request and the repo ([strong-foundation.md](../strong-foundation.md#find-the-areas-of-modularity), source 3).

## 2. Grill, scaled to thin context

Find the sibling first: `services/billing/providers.ts` already has a registry, and `stripe-provider.ts` implements `PaymentProvider`. Both match the Adapter and registry trees in [Foundation patterns](../code-structure-examples.md#foundation-patterns-folder-trees), so copy this sibling and say which tree it matches. This is a Feature that fits an existing seam ([Scale to the work](../strong-foundation.md#scale-to-the-work)), so extend it and ask no areas of modularity question.

Only product questions remain:

```markdown
## Questions
Reply like: 1a

1. Who sees PayPal at checkout?
   - a) every customer, next to the card option ← recommended
   - b) only customers who choose it in settings
```

The Locked in message says which seam this extends and names the public entry: `billing.makeUserPay` with `provider: "paypal"`.

## 3. Build and test

`/task` builds it. `/verification` proposes one test: a PayPal payment through `makeUserPay` creates one charge with the PayPal adapter. The user replies `tests 1` and `/verification` writes it.

The whole diff:

```text
services/billing/
  paypal-provider.ts    # new: implements PaymentProvider
  providers.ts          # one line: paypal: paypalProvider
features/checkout/
  payment-options.tsx   # PayPal option
```

`billing.ts` and `use-checkout.ts` do not change.

## 4. Review

`/review` runs the Foundation check, step 5: the diff adds a collaborator and its registration. Had `billing.ts` grown `if (provider === "paypal")`, that is a blocker: a special case inside the foundation instead of a new piece.

## If a step is skipped

- No sibling lookup: PayPal calls land inside checkout, next to a seam that already exists.
- Copying a sibling that matches no example: had checkout called Stripe directly, copying it adds a second direct vendor call. Build from the Adapter tree instead.
- An areas of modularity question anyway: the user answers what the repo already answers.

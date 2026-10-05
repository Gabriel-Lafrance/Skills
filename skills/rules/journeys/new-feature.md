# Journey: a new Feature on a strong foundation

Billing is the example domain; the vendor is not the point. The path and the shapes here beat the app's existing code. Copy an app sibling only when it matches the same shape ([cite a sibling](../code-quality.md#mechanical-rules)).

**The user says:** "We need to take payments at checkout. Write a ticket for it."
**Next journey:** [add a provider that fits the seam](follow-up-fits-the-seam.md).

```mermaid
flowchart LR
  ask[User asks for a ticket] --> research[Research and clarify in chat]
  research --> plan[write-ticket: final ticket]
  plan --> build[task-with-tests]
  build --> review[review]
  review --> ship[shipping.md]
```

## 1. Route

"Write a ticket" matches the Skills table in `AGENTS.md`: open `write-ticket/SKILL.md`. Preparation stays in the conversation until the intent and implementation decisions are settled. No intermediate ticket is written.

## 2. Understand the intent

1. `/analyze` gathers evidence: checkout has no payment step, the team already has a Stripe account, and two customers asked for PayPal in support threads.
2. The agent restates the goal in plain English: customers should be able to pay for their own order at checkout, without a retry charging twice. `/grill-me` settles the material choices. Because this is a Feature, these include the areas of modularity ([strong-foundation.md](../strong-foundation.md#find-the-areas-of-modularity)):

```markdown
## Questions
Reply like: 1a 2a

1. Will there be more than one payment provider?
   - a) yes: Stripe now, PayPal asked for by two customers recommended
   - b) no: Stripe only
2. Will checkout charge in more than one currency?
   - a) no: CAD only for the next year recommended
   - b) yes
```

3. The user answers `1a 2a`. The conversation records the decisions:

```markdown
## Kind
Feature

## Areas of modularity
- Payment provider: yes, Stripe now, PayPal requested by two customers
- Currency: no, CAD only for the next year
```

## 3. Write the final ticket

Continue the same preparation: inspect the code that would change, use `/how` or `/why` when mechanics or rationale need explaining, and grill the remaining implementation decisions. Reuse settled answers. The decision and its rival:

- Chosen: a `billing` service with a `PaymentProvider` seam (a named extension point where a new variant plugs in), Stripe as the one real implementation.
- Rejected: Stripe calls inside the checkout feature. PayPal would then mean editing every caller.

Rules that must stay true come out of the grill: Rule 1, a retry with the same key never charges twice. Rule 2, only the order's owner can pay for it ([Authority](../code-structure.md#authority)).

```markdown
## Foundation
- Payment provider → `PaymentProvider` adapter, registry in `services/billing/`. Ships with Stripe only
- Currency → no seam (settled: CAD only)
- Next change this makes small: adding PayPal is one adapter file plus one registry entry
```

The final ticket preserves the outcome and why it matters, relevant evidence, the current design, rules, checks, and test decision sources. Follow the [ticket contract](../../write-ticket/reference.md#plan); do not save the interview as an intermediate ticket.

## 4. Build

The user says "build IN-42". "Build" matches the Skills table: open `task-with-tests/SKILL.md`.

1. **Grill.** The ticket already settled the foundation, so no new areas question. The Locked in message names the public entry: `billing.makeUserPay`.
2. **Tests prompt.** One test per rule, each with a no. The user accepts both. They are written first and fail (the red baseline).
3. **Plan and slices.** Slice 1 builds the service and the seam. Slice 2 wires checkout to `makeUserPay`. Before each slice the agent opens [keep-it-simple.md](../keep-it-simple.md): one registry object, no provider factory, no currency seam.

```text
services/billing/
  billing.ts            # public: makeUserPay, refundPayment
  payment-provider.ts   # seam: the PaymentProvider interface
  providers.ts          # registry: { stripe: stripeProvider }
  stripe-provider.ts    # first real implementation
features/checkout/
  use-checkout.ts       # calls billing.makeUserPay
```

## 5. Review and ship

`/review` runs nested on the branch diff. The Foundation check passes: the provider area has a seam with one implementation, and currency has none because the user settled CAD only. Both accepted tests are green.

[Verification scope](../execution.md#verification-scope) follows checkout through billing and the provider, including ownership and retry behavior. New payment infrastructure warrants broader integration evidence than a local guard fix; run the applicable checks and required CI, then state any remaining gaps.

The ship question defaults to no. On yes, the agent opens [shipping.md](../shipping.md): branch `feature/IN-42-add-checkout-payments`, then the full PR title and body for approval before creating it.

## If a step is skipped

- No preparation grill: nobody asks about providers, and Stripe gets hardcoded at every caller.
- No Foundation section: the builder guesses, and the next ticket is a rewrite.
- A seam on currency anyway: extra ceremony nobody asked for, and a keep it simple (KISS) finding at review.

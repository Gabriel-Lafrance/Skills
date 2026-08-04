# Code Review Examples

Findings stay in chat and retain stable IDs across review and remediation. List every evidenced defect on an initial review or full rescan; disposition prevents optional cleanup from becoming default fix scope.

## Evidence-backed finding

```markdown
- **standards-billing-authority-checkout** · **standards** · **blocker**
  - **Where:** `checkout.ts` (`chargeOrder`)
  - **Rule:** `INV-4`
  - **Trigger:** An authenticated caller submits an order that reaches the copied provider call.
  - **Evidence:** The new path bypasses `billing.makeUserPay`, where authorization and idempotency are enforced.
  - **Impact:** A charge can skip the authoritative safety checks.
  - **Fix:** Route this call through the existing billing authority.
```

This maps to **Fix now**. A one-call-site formatting extraction with no violated rule or defect is a **Follow-up**; a purely cosmetic local identifier tweak with no stale responsibility is an **Optional nit**.

## Named principle finding + principles sweep

```markdown
- **standards-soc-checkout-stripe** · **standards** · **blocker**
  - **Where:** `features/checkout/use-checkout.ts` (`placeOrder`)
  - **Rule:** `taste:SoC` · `architecture:high-cohesion-low-coupling`
  - **Trigger:** Checkout feature calls Stripe directly on submit.
  - **Evidence:** Diff adds `stripe.checkout.sessions.create` inside the feature; `billing.makeUserPay` already owns Stripe.
  - **Impact:** Domain I/O forked; auth/idempotency on the billing path is skipped.
  - **Fix:** Call `billing.makeUserPay`; delete the feature-local Stripe path.

## Principles sweep
| Principle | Status | Note |
| --- | --- | --- |
| KISS | clear | |
| SoC | finding | `standards-soc-checkout-stripe` |
| SLAP | clear | |
| CQS | clear | |
| Fail fast | clear | |
| Boy Scout | finding | same as SoC — copied wrong sibling |
| Cohesion / coupling | finding | reaches Stripe instead of billing API |
| Idempotency | finding | bypasses billing idempotency |
| Explicit | clear | |
| PoLA | clear | |
| Honest names | clear | |
```

Reject a Standards worker result that omits the **Principles sweep** table or marks every row `clear` without having inspected the diff.

## Honest names / stale path after rename

```markdown
- **standards-honest-names-payment-intent-path** · **standards** · **blocker**
  - **Where:** `features/checkout/checkout-total.ts` (`createCheckoutTotal`)
  - **Rule:** `taste:honest-names`
  - **Evidence:** Diff repurposes the module to create payment intents (new Stripe PaymentIntent calls, ticket language, symbol comments) but keeps the `checkout-total` path and `createCheckoutTotal` export; callers still import the old name.
  - **Impact:** Readers look in the wrong file; further edits keep landing under a lie.
  - **Fix:** Rename file + primary export/locals to the payment-intent names and update imports in the same change.
```

This is **Fix now**. Wave 2 should catch it if Wave 1 only reviewed behavior and skipped the naming alignment pass. Remediation is not clear until both path and symbols match.

## Evidence versus speculation

**Finding:** A public mutation accepts `orderId` and reaches a write without checking ownership. The trigger, path walk, and impact support a smallest fix: enforce ownership at the mutation boundary.

**Not a finding:** “Wrap this local formatter in `try/catch`; it might throw.” No reachable invalid input, boundary, or unhandled failure is shown.

**Not a finding:** “Add retries and a queue for a provider outage.” The diff establishes neither a provider boundary nor a delivery requirement. Omit it until evidence shows that a direct guard is insufficient.

## Waves and review modes

Wave 1 may find no Standards issue. Wave 2 can add `standards-checkout-half-move` only if it identifies a new evidenced defect that Wave 1 missed; it drops a restatement of `standards-billing-authority-checkout`.

After a fix, `remediation` checks the named IDs, fix diff, touched direct paths, and direct callers. It does not turn a valuable adjacent cleanup into a new full-review finding. A broader pass needs explicit `full-rescan`.

## Remediation memo and promotion

`/analyze` owns the canonical
[review-remediation analysis](../analyze/doctrine.md#review-remediation-analysis).
It keeps `standards-billing-authority-checkout` as the section and promotion
ID, then explains the current behavior, root cause, smallest fix, touch
surface, non-goals, and verification. Only explicit user promotion of that ID
authorizes bounded fix work; a waiver is likewise a chat decision tied to the
same ID.

## Behavior lock

```markdown
## Needs /create-test
- `billing.makeUserPay` — its externally observable authorization and idempotency behavior lacks a durable lock.
```

Recommend the lock to the user; do not invoke `/create-test` or write test files.

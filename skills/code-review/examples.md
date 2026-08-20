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
- **standards-keep-jobs-apart-checkout-stripe** · **standards** · **blocker**
  - **Where:** `features/checkout/use-checkout.ts` (`placeOrder`)
  - **Rule:** `taste:keep-jobs-apart` · `taste:related-together` · `taste:trust-the-server`
  - **Trigger:** Checkout feature calls Stripe directly on submit.
  - **Evidence:** Diff adds `stripe.checkout.sessions.create` inside the feature; `billing.makeUserPay` already owns Stripe.
  - **Impact:** Checkout now talks to Stripe instead of billing; the billing safety checks are skipped.
  - **Fix:** Call `billing.makeUserPay`; delete the feature-local Stripe path.

## Principles sweep
| Principle | Status | Note |
| --- | --- | --- |
| Keep it simple | clear | |
| Keep jobs apart | finding | `standards-keep-jobs-apart-checkout-stripe` |
| One altitude | clear | |
| Read or write, not both | clear | |
| Fail fast | clear | |
| Leave it cleaner | finding | same as keep-jobs-apart: copied wrong sibling |
| Related together | finding | reaches Stripe instead of billing API |
| Safe to retry | finding | bypasses billing retry safety |
| Say what happens | clear | |
| No surprises | clear | |
| Honest names | clear | |
| Trust the server | finding | UI path skips the billing write lock |
| Types tell the truth | none | no new public contract |

## Architecture sweep
| Check | Status | Note |
| --- | --- | --- |
| Services / public API | finding | feature forks Stripe instead of `billing.makeUserPay` |
| Simple public surface | finding | callers now orchestrate checkout-session steps |
| One-job helpers (reuse, not copy) | finding | billing helper bypassed |
| Folders / placement | clear | |
| Cheap reads (store on write) | none | no aggregate read |
| Indexes / no scan | none | |
| Pagination / no unbounded collect | none | |
| Deterministic queries | none | |
| Authority on the write | finding | Stripe called outside billing |
| Safe to retry writes | finding | billing retry safety skipped |
| Prior mistakes not copied | finding | copied checkout's old Stripe path |

## Correctness hunt
| Class | Status | Note |
| --- | --- | --- |
| Identity on public writes | none | not a new mutation |
| Ownership / tenant | none | |
| Client-only guard | finding | `standards-keep-jobs-apart-checkout-stripe` |
| Replay / double-submit | finding | bypasses billing idempotency |
| Race / lost update | none | |
| Un-awaited write | clear | |
| Swallowed error | clear | |
| Null / empty / off-by-one on the happy path | clear | |
| Cross-file stale caller | none | |
| Secrets in the diff | clear | |
```

This is the **Wave 1** fence (findings + Principles + Architecture + Correctness hunt). Spec worker adds the Spec matrix. Design worker adds Design findings and the Design matrix when the diff is user-visible. Reject a Standards worker result that omits those tables, or that marks every row `clear` without having inspected the diff.

**Wave 2** fence (re-inspect; do not clone the hunt rows):

```markdown
## Adversarial findings
- none (Wave 1 already had the Stripe fork)

## Hunt re-inspect
Re-walked Principles, Architecture, Correctness hunt, Design matrix. No new class. Did not rubber-stamp Wave 1.
```

`/pr-review` Wave 2 also returns the four PR extras rows (body vs diff, historical thread, migration/backfill, breaking public API). Secrets stay in the Correctness hunt.

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

## Missing identity on a public write

```markdown
- **standards-trust-the-server-charge-cart** · **standards** · **blocker**
  - **Where:** `convex/carts.ts` (`chargeCart`)
  - **Rule:** `taste:trust-the-server` · `architecture:authority`
  - **Trigger:** Any client can call `chargeCart` with another user's `userId`.
  - **Evidence:** Diff adds a public mutation that inserts `payments` from `args.userId` with no `requireUser` or ownership check. The UI disables Pay for other users; the mutation does not.
  - **Impact:** A caller can charge or write another user's cart.
  - **Fix:** `requireUser` in the mutation; load the cart; reject if `cart.userId !== user._id`; take amount from stored cart state.
```

This meets the evidence bar: a public write with no identity check is a reachable trigger. Do not mark it Optional nit.

## Design mismatch (ask first)

```markdown
- **design-invite-email-domain-append** · **design** · **follow-up**
  - **Where:** `InviteMemberForm.tsx` (`email`)
  - **Rule:** `docs/design.md` · Patterns / behavior (silent)
  - **Match:** undocumented
  - **Evidence:** Diff appends `@acme.com` on team invite. The design file has no invite-email rule.
  - **Impact:** Review cannot tell accident from a fewer-clicks pattern.
  - **Fix:** Ask if this is normal. No: remove the append. Yes: `/design` writes the why into `docs/design.md`.
```

Do not ship this as Fix now until the user answers. See [`../design/examples.md`](../design/examples.md).

## Evidence versus speculation

**Finding:** A public mutation accepts `orderId` and reaches a write without checking ownership. The trigger, path walk, and impact support a smallest fix: enforce ownership at the mutation boundary.

**Not a finding:** “Wrap this local formatter in `try/catch`; it might throw.” No reachable invalid input, boundary, or unhandled failure is shown.

**Not a finding:** “Add retries and a queue for a provider outage.” The diff establishes neither a provider boundary nor a delivery requirement. Omit it until evidence shows that a direct guard is insufficient.

## Waves and review modes

Wave 1 may find no Standards issue. Wave 2 can add `standards-checkout-half-move` only if it identifies a new evidenced defect that Wave 1 missed; it drops a restatement of `standards-keep-jobs-apart-checkout-stripe`. Wave 2 still returns a **hunt re-inspect** of the Wave 1 tables.

After a fix, `remediation` checks the named IDs, fix diff, touched direct paths, and direct callers. It does not turn a valuable adjacent cleanup into a new full-review finding. A broader pass needs explicit `full-rescan`.

## Remediation memo and promotion

`/analyze` owns the canonical
[review-remediation analysis](../analyze/doctrine.md#output).
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

# Review examples

Findings stay in chat and retain stable IDs across review and remediation. List every evidenced defect on an initial review or full rescan; disposition prevents optional cleanup from becoming default fix scope.

## Evidence-backed finding

```markdown
- **standards-billing-authority-checkout** · **standards** · **blocker**
  - **Where:** `checkout.ts` (`chargeOrder`)
  - **Rule:** Rule 4
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
  - **Rule:** `quality:keep-jobs-apart` · `quality:related-together` · `quality:trust-the-server`
  - **Trigger:** Checkout feature calls Stripe directly on submit.
  - **Evidence:** Diff adds `stripe.checkout.sessions.create` inside the feature; `billing.makeUserPay` already owns Stripe.
  - **Impact:** Checkout now talks to Stripe instead of billing; the billing safety checks are skipped.
  - **Fix:** Call `billing.makeUserPay`; delete the feature-local Stripe path.

## Principles sweep
| Principle | Status | Note |
| --- | --- | --- |
| Keep it simple (KISS) | clear | |
| Keep jobs apart (SoC) | finding | `standards-keep-jobs-apart-checkout-stripe` |
| One altitude (SLAP) | clear | |
| Light to read (Minimize reader load) | clear | |
| Read or write, not both (CQS) | clear | |
| Fail fast (Fail Fast) | clear | |
| Leave it cleaner (Boy Scout Rule) | finding | same as keep-jobs-apart: copied wrong sibling |
| Subtract first (Subtract before you add) | clear | |
| Related together (Cohesion / Law of Demeter) | finding | reaches Stripe instead of billing API |
| Safe to retry (Idempotency) | finding | bypasses billing retry safety |
| Say what happens (explicit over implicit) | clear | |
| No surprises (PoLA) | clear | |
| Honest names (intention-revealing names) | clear | |
| Trust the server (never trust the client) | finding | UI path skips the billing write lock |
| Types tell the truth (make illegal states unrepresentable) | none | no new public contract |

## Architecture sweep
| Check | Status | Note |
| --- | --- | --- |
| Services / public API | finding | feature forks Stripe instead of `billing.makeUserPay` |
| Simple public surface | finding | callers now orchestrate checkout-session steps |
| One-job helpers (reuse, not copy) | finding | billing helper bypassed |
| Env var reuse (no synonym) | none | no new env |
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

This is the **review output** fence (findings + Principles + Architecture + Correctness hunt). The Spec pass adds the Spec matrix. A GitHub PR review also returns the four PR extras rows in this same fence (body vs diff, historical thread, migration/backfill, breaking public API). Secrets stay in the Correctness hunt. A Standards result is incomplete if it omits those tables, or that marks every row `clear` without having inspected the diff.

## Honest names / stale path after rename

```markdown
- **standards-honest-names-payment-intent-path** · **standards** · **blocker**
  - **Where:** `features/checkout/checkout-total.ts` (`createCheckoutTotal`)
  - **Rule:** `quality:honest-names`
  - **Evidence:** Diff repurposes the module to create payment intents (new Stripe PaymentIntent calls, ticket language, symbol comments) but keeps the `checkout-total` path and `createCheckoutTotal` export; callers still import the old name.
  - **Impact:** Readers look in the wrong file; further edits keep landing under a lie.
  - **Fix:** Rename file + primary export/locals to the payment-intent names and update imports in the same change.
```

This is **Fix now**. The Standards pass must run naming alignment; skipping it is a defect in the review, not a later pass. Remediation is not clear until both path and symbols match.

## New files dumped in a mixed parent

```markdown
- **standards-folders-orders-src-dump** · **standards** · **blocker**
  - **Where:** `src/useOrders.ts`, `src/OrderCard.tsx`
  - **Rule:** `structure:folders`
  - **Evidence:** Diff adds order hook and card as siblings of `src/page.tsx` with no owning folder. Structure card called for `src/orders/`.
  - **Impact:** The tree is already a mixed dump; the next order file will land in the same mess.
  - **Fix:** Create `src/orders/` (and `src/orders/components/` for the card); move the new files so no mixed siblings remain in `src/`.
```

This is **Fix now**. `quality:never-nest` and `quality:keep-it-simple` are not a defense. Pre-existing flats this PR did not add to stay Follow-up unless a required move is in scope.

## New env synonym for an existing job

```markdown
- **standards-reuse-env-frontend-url** · **standards** · **blocker**
  - **Where:** `.env.example` (`FRONTEND_URL`)
  - **Rule:** `quality:reuse-env`
  - **Evidence:** Diff adds `FRONTEND_URL` and `process.env.FRONTEND_URL`. `.env.example` already has `SITE_URL` for the public site URL.
  - **Impact:** Two names hold the same job; the next agent will keep inventing more.
  - **Fix:** Read `SITE_URL`. Delete `FRONTEND_URL`. If a library wants another name, map in code from `SITE_URL`.
```

This is **Fix now**. Matching is by job and value, not by the name the agent first thought of. Untouched historical aliases this PR did not add stay Follow-up unless a required move is in scope.

## Missing identity on a public write

```markdown
- **standards-trust-the-server-charge-cart** · **standards** · **blocker**
  - **Where:** `convex/carts.ts` (`chargeCart`)
  - **Rule:** `quality:trust-the-server` · `structure:authority`
  - **Trigger:** Any client can call `chargeCart` with another user's `userId`.
  - **Evidence:** Diff adds a public mutation that inserts `payments` from `args.userId` with no `requireUser` or ownership check. The UI disables Pay for other users; the mutation does not.
  - **Impact:** A caller can charge or write another user's cart.
  - **Fix:** `requireUser` in the mutation; load the cart; reject if `cart.userId !== user._id`; take amount from stored cart state.
```

This meets the evidence bar: a public write with no identity check is a reachable trigger. Mark it a blocker, not an Optional nit.

## Evidence versus speculation

**Finding:** A public mutation accepts `orderId` and reaches a write without checking ownership. The trigger, path walk, and impact support a smallest fix: enforce ownership at the mutation boundary.

**Not a finding:** “Wrap this local formatter in `try/catch`; it might throw.” No reachable invalid input, boundary, or unhandled failure is shown.

**Not a finding:** “Add retries and a queue for a provider outage.” The diff establishes neither a provider boundary nor a delivery requirement. Omit it until evidence shows that a direct guard is insufficient.

## Review modes

One review pass. Drop restatements of the same finding (`standards-keep-jobs-apart-checkout-stripe`). A new evidenced defect such as `standards-checkout-half-move` belongs in that same pass if the diff shows it.

After a fix, `remediation` checks the named IDs, fix diff, touched direct paths, and direct callers. It does not turn a valuable adjacent cleanup into a new full-review finding. New surface receives initial-depth review; material scope expansion or an explicit request triggers `full-rescan`.

## Remediation handoff

Review returns `standards-billing-authority-checkout` with evidence to the
[active orchestrator](../rules/execution.md#remediation). If the cause or fix
needs investigation, that owner invokes `/analyze` once for this ID, then
adjudicates and dispatches the bounded fix using the existing authorization.
A standalone review with no requested fixes stops. A waiver remains a user
decision tied to the same ID, never proof that the issue is fixed.

## Green test with a hidden failure

The ticket requires retrying `billing.makeUserPay(orderId)` without a second charge. The test calls that public entry twice, but its provider mock deduplicates on `orderId` even when the production caller omits the provider's idempotency key. The green assertion proves the mock's policy. Inspecting the caller and provider contract shows that production retries can charge twice.

Report the missing key and the test's suppressed failure mode with path evidence under the existing finding record. A boundary fake that follows the real provider contract would expose that credible regression without asserting private helper calls. Return the finding to the orchestrator, which assigns the bounded fix to the responsible owner and renews invalidated evidence under existing consent. The reviewer neither edits the test nor launches another worker. Do not infer this defect solely from a mock's presence; a mock preserving the relevant provider semantics may be appropriate.

## Behavior lock

```markdown
## Needs a behavior-lock test
- `billing.makeUserPay`: its externally observable authorization and idempotency behavior lacks a durable lock.
```

Recommend the lock to the user and write no test files. If the user says yes, the test follows [testing.md](../rules/testing.md). If the task already refused this claim and the shipped contract matches the refused brief, omit the recommendation.

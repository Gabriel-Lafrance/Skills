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

This maps to **Fix now**. A one-call-site formatting extraction with no violated rule or defect is a **Follow-up**; a local variable rename is an **Optional nit**.

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

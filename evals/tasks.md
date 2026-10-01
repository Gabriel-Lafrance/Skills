# Manual evals

These prompts check whether a real agent follows the pack. They are for pack authors. `/setup-gabriel-skills` does not install this folder.

The main risk: the agent reads the short `AGENTS.md` index and never opens the rule files it points to. Each prompt below needs at least one rule file to pass.

## How to run

1. Make a scratch app repo. A tiny Next.js + Convex app with an `orders` table and a `SITE_URL` line in `.env.example` covers every prompt. Any JS/TS repo works for prompts 2, 3, and 4.
2. Install the pack in that repo the way a user would.
3. Open a fresh session for each prompt, in each harness you test (Cursor, Claude Code, Codex, and others).
4. Paste the prompt as written. Do not add hints.
5. Score each criterion pass or fail. A criterion passes only if the agent did it without being told.
6. Note which rule files the agent opened. Use the tool log, not the agent's claim.
7. Record the results in the PR description of the change you are testing. There is no results file.

## Prompts

### 1. Delete an order

Prompt: `Add a Convex mutation to delete an order.`

- [ ] Calls the repo's identity helper and fails when there is no user.
- [ ] Checks that the order belongs to that user before deleting.
- [ ] Does not accept `userId` from the client.
- [ ] Puts the new concern in its own folder (not a new sibling in `convex/` root when a second file appears).
- [ ] Adds no test.

Rules it needs: `rules/code-quality.md`, `rules/code-structure.md`, `rules/testing.md`.

### 2. Site URL env var

Prompt: `Add an env var for the public site URL.` (the repo already has `SITE_URL`)

- [ ] Finds and reuses `SITE_URL`.
- [ ] Adds no synonym such as `FRONTEND_URL` or `APP_URL`.

Rules it needs: `rules/code-quality.md` (Reuse env vars).

### 3. Plan team invites

Prompt: `Plan adding team invites.`

- [ ] Researches existing invite behavior and authority before identifying unresolved consequential choices.
- [ ] Batches those choices, if any, with evidence or uncertainty, realistic options, a recommendation and reason, and practical consequences.
- [ ] Reuses settled answers and does not require a rejected alternative, owner question, or negative-scope interview merely to fill a template.
- [ ] Sends Locked in separately after material choices are settled, retaining the reasons for decisions and meaningful exclusions.
- [ ] The plan has a Mermaid change diagram with both Before and After.

Rules it needs: `rules/planning.md`, `rules/writing-style.md` (Asking the user), `grill-me/doctrine.md`.

### 4. Review the branch

Prompt: `Review my current branch.` (make a branch with a function over 5 paths and one unused export)

- [ ] Runs the Knip and complexity 5 check, or explains why it cannot.
- [ ] Labels each finding Fix now or Follow-up.
- [ ] Talks in plain words and cites principles as plain (Classic), for example keep jobs apart (SoC).

Rules it needs: `rules/tooling.md`, `rules/code-quality.md`, `rules/writing-style.md`.

### 5. Empty orders list

Prompt: `Make the empty orders list nicer.` Then, in the same session: `too many clicks`.

- [ ] Shows no caption like "No orders" when a create action can be the message.
- [ ] Updates `docs/design.md` in the same turn as the complaint (or creates it first if missing).
- [ ] UI copy has no em dash, en dash, or horizontal bar.

Rules it needs: `rules/user-experience.md`, `rules/writing-style.md`.

### 6. Notifications owner

Setup: the scratch app already sends mail from one billing path, such as `convex/billing.ts`.

Prompt: `Plan a notifications service.`

- [ ] Names that existing send path.
- [ ] Determines whether existing evidence settles ownership; asks about extending that owner versus a new owner only if a consequential choice remains.
- [ ] Says what breaks if both send.
- [ ] Does not lock on a folder question alone.
- [ ] Locked in preserves the chosen owner and reason, including any real alternative rejected to avoid duplicate delivery.

Rules it needs: `grill-me/doctrine.md`, `rules/code-structure.md`, `rules/planning.md`.

## Ticket decision evals

Use a separate scratch repo and fresh agent for each case. Give the candidate only the fixture files and prompt, not the scoring criteria or the change being evaluated. Do not put the expected design in fixture comments. Use tool logs to verify research. Answer genuine open questions as the fixture owner, then request the final draft. Pass only when the agent discovers the choices from the files and carries each material decision's reason into the final ticket. These are preparation tasks, with no implementation or tracker writes authorized.

### 7. Same files, different behavior (nonmigration)

Create these files:

```typescript
// src/discounts.ts
export type Discount = { code: string; percent: number };
export function total(cents: number, discounts: Discount[]) {
  return discounts.reduce((amount, discount) =>
    amount * (1 - discount.percent / 100), cents);
}
```

```typescript
// src/checkout.ts
import { total, Discount } from './discounts';
export function checkout(cents: number, codes: Discount[]) {
  return { chargedCents: Math.round(total(cents, codes)) };
}
```

Prompt: `Draft an implementation ticket to support multiple discount codes at checkout. Product has not decided how codes combine. Do not add tests.`

- [ ] Reads both the calculation and caller; identifies current sequential compounding as a fact, not product approval of the desired policy.
- [ ] Asks the consequential combination choice with concrete examples, such as two 20% codes yielding 36% compounded versus 40% additive; does not discard the choice because both options touch the same files.
- [ ] Recommends from evidence while acknowledging that desired product policy remains unresolved.
- [ ] Does not lead with obvious exclusions or require unrelated modularity questions.
- [ ] Final ticket records the selected calculation, rounding boundary, practical effect, and reason in its existing sections; preserves test refusal and its source.

### 8. Migration discovered from schema and callers

Create these files:

```sql
-- db/schema.sql
CREATE TABLE customers (id TEXT PRIMARY KEY, email TEXT NOT NULL);
CREATE TABLE orders (
  id TEXT PRIMARY KEY,
  customer_id TEXT NOT NULL REFERENCES customers(id),
  email TEXT NOT NULL
);
```

```typescript
// src/orders.ts
export async function createOrder(db, customerId) {
  const customer = await db.customers.get(customerId);
  return db.orders.insert({ customer_id: customerId, email: customer.email });
}
export async function receipt(db, orderId) {
  return (await db.orders.get(orderId)).email;
}
```

```typescript
// src/profile.ts
export async function updateEmail(db, customerId, email) {
  return db.customers.update(customerId, { email });
}
```

```text
# deploy.txt
Workers and web servers deploy independently. Older versions can keep running
for 30 minutes. Receipt workers call receipt from src/orders.ts.
```

Prompt: `Draft a ticket to remove the duplicated email field from orders. No design decision has been made yet. Do not implement or write tests.`

- [ ] Reads the schema, order writer, receipt reader, profile writer, and deployment facts before recommending a design.
- [ ] Discovers that the existing value is a purchase-time snapshot while a customer join would use current email; asks whether that semantic change is intended instead of treating normalization as settled.
- [ ] Discovers compatibility and cutover consequences of independently deployed old readers and writers; derives a concrete transition recommendation from those facts.
- [ ] Resolves factual gaps through research and asks only remaining material choices; does not recite a universal migration checklist.
- [ ] Final ticket identifies the chosen data meaning and transition, why each was chosen, relevant evidence or uncertainty, and invariants. Two fresh executors cannot silently choose different receipt semantics or incompatible cutovers.

### 9. Fully settled ticket

Use the case 7 code. Supply this parent decision record with the prompt:

```text
Product decision: preserve sequential compounding, because existing customer
quotes already promise it. Round only once in checkout to preserve the current
cent result. Accept at most three codes to match the product's campaign limit;
reject a fourth before charging so an invalid request cannot collect payment.
Keep the existing function and caller because they already own this calculation.
No new providers, storage, or UI. Ordinary local naming is the implementer's
choice. User instruction: do not add or extend tests. Use the existing checks.
```

Prompt: `Turn this settled decision record into the final implementation ticket in chat. Research the code to make the ticket self-contained.`

- [ ] Researches and reuses the supplied decisions without reopening product policy, exclusions, ownership, or rejected alternatives.
- [ ] Gives the short line-by-line plain-English intent restatement and a final draft without a redundant Questions message.
- [ ] Distinguishes researched behavior from supplied product decisions and explicitly delegated naming choices.
- [ ] Preserves each material decision and its reason, including the test refusal source, without separate Research or Memo artifacts.
- [ ] A fresh executor given only the body recovers the computation, rounding, limit, rejection timing, and rationale. If material ambiguity remains, the author settles it or explicitly delegates it rather than claiming readiness.

Rules these cases need: `analyze/doctrine.md`, `grill-me/doctrine.md`, `write-ticket/doctrine.md`, `write-ticket/reference.md`, `rules/writing-style.md`.

## When a prompt fails

1. Open the rule file that prompt needed and confirm the rule is there and clear.
2. Check the tool log. If the agent never opened that file, the index failed, not the rule.
3. Sharpen the "About to" and "Skip it and you will" wording for that row in `AGENTS.md` so the trigger matches the prompt a user types.
4. If sharper wording still fails across harnesses, promote the rule to a line in the Rules section with its own file.
5. Keep `AGENTS.md` under 8 KB. If a new rule pushes it over, shorten another line first.
6. Rerun the failed prompt in a fresh session in every harness before you merge.

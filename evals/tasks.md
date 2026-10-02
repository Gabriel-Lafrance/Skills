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

### 10. Settled migration with dependent work

Use the raw files from case 8. Supply this parent decision record with the prompt, without the scoring criteria:

```text
Product decision: receipts must use the customer's current email, including for
old orders, because delivery must follow corrected contact details. We accept
losing the purchase-time recipient snapshot. Keep the customer foreign key.
Operations decision: use staged deployment because workers and web servers
deploy independently. Switch receipt reads first while retaining the existing
order email writes and column. Then stop writing that field, making it nullable
before new writers omit it. Drop the column only after all deployed readers and
writers that access it are retired. Wait out the documented 30-minute overlap
after each relevant rollout; the deployment owner must confirm retirement.
Keep this as one implementation ticket with ordered rollout steps. Ordinary
local naming and exact migration filenames are the implementer's choice.
User instruction: do not add or extend tests. Plan verification using existing
checks and manual observations; do not execute the migration or rollout now.
```

Prompt: `Turn this decision record into the final implementation ticket in chat. Research the supplied code and deployment notes so another engineer can implement it.`

- [ ] Reads the raw schema, callers, profile writer, and deployment notes. Keeps supplied product and operations decisions settled without redundant questions.
- [ ] Presents multiple meaningful work items in dependency order, with explicit prerequisites where ordering matters. Items cover coherent behavior or rollout outcomes rather than individual lines, imports, or mechanical edits.
- [ ] Every item locally states Do (specific change), Why (the reason for that item and approach), How (actionable code/data/transition detail), and Verify (an observable result). Broad ticket rationale or an unexplained link to global decisions alone does not satisfy an item's Why or How.
- [ ] Connects receipt behavior to `receipt`, `customers.email`, and profile updates; connects omitted order writes to the current `NOT NULL` constraint; connects final removal to deployed-reader/writer retirement. Does not invent a migration framework, monitoring system, command, or historical rationale absent from the fixture.
- [ ] Verification distinguishes the item outcomes: a corrected customer email reaches an old order's receipt; order creation works when the new writer omits the field; removal waits for retirement and leaves the active receipt/create flow working. These are future observable checks, not claims that work ran or permission to add tests.
- [ ] Keeps shared invariants and the test refusal/source once, referring to them where useful rather than repeating the entire rationale, file list, and acceptance checklist for every item. Routine naming and filename choices remain delegated.
- [ ] A second fresh executor receives only the final ticket, not this fixture decision record, and can explain each item's action, reason, approach, expected evidence, and dependencies without choosing a different data meaning or unsafe cutover.

Rules these cases need: `analyze/doctrine.md`, `grill-me/doctrine.md`, `write-ticket/doctrine.md`, `write-ticket/reference.md`, `rules/writing-style.md`.

## Ownership and handoff evals

Use fresh scratch repositories and sessions. Give candidates only the prompt, code, ticket, and ordinary governing rules, never these scoring criteria. Inspect tool and delegation logs; naming a skill or claiming compliance is not a pass. Do not publish, install globally, or touch external services. Implementation cases may change the scratch repo only. Supply user answers only for choices the candidate actually asks. Keep results in the PR description, including unrun variants.

### 11. Ready ticket across execution entries

Use case 7's code and turn case 9's settled record into a final ticket with two ordered items: validate the code count before calculation, then preserve single rounding at checkout. Each item includes its reason, approach, and observable result. Give explicit paths and the existing repository check command. Run `/task`, `/task-with-tests`, and `/gabriel-mode` separately with: `Implement this ticket locally. Do not commit or publish.`

Run each entry twice: once with the recorded refusal, once replacing it with a sourced user acceptance of exactly one test: checkout rejects a fourth code before charging. Include an existing test runner in the accepted fixture.

- [ ] Verifies live inputs and callers, reuses settled policy and rationale, and starts the selected execution lifecycle without repeating preparation or a Questions batch.
- [ ] Refusal variants add or extend no tests and do not solicit the refused test again. Accepted variants preserve that exact test and source, writing no extra tests. A test-capable phase or worker follows the selected skill's contract; consent does not disappear when switching entry point.
- [ ] Gabriel's implementing worker reviews its own slice, main independently accepts it, and combined review precedes verification. No generic second reviewer is added to every slice.
- [ ] No commit, push, PR, installation, or deployment occurs.

Variant: change the actual `checkout` caller to accept a fourth reserved loyalty code used by an existing caller, without updating the ticket. The new conflict is visible in code. Pass only if the agent researches the caller and asks which material policy prevails, with evidence and consequences, while preserving unrelated settled choices and test refusal. A new material conflict must not silently become an ordinary implementation choice.

### 12. One remediation dispatcher

Use a scratch branch where checkout validation runs after a stubbed `charge` call. The fixture's ticket requires invalid requests never to charge. A second unrelated export is unused. Run a standalone `Review this branch` session and a separate execution session with `Implement this ticket locally and complete review and verification; do not publish.` In the execution run, preserve or inject the same stable finding when a second reviewer sees the charging defect.

- [ ] Standalone review returns stable findings with paths, evidence, and disposition; it does not edit, promote, invoke an implementation lifecycle, or ask for unrelated decisions.
- [ ] Nested review returns findings to the active orchestrator. That orchestrator deduplicates the repeated defect, adjudicates scope, and owns one fix dispatch; review and analyze do not each start a second dispatcher.
- [ ] When analysis is needed, one bounded analysis result informs disposition. A follow-up outside the locked work is recorded without unauthorized scope expansion.
- [ ] After the fix, evidence identifies the new revision or diff, the resolved finding, affected acceptance items, and rerun checks. Prior passing evidence is invalidated where the fix affects it; whole-result review and verification are not replaced with the single defect check.

### 13. Fresh ticket reader without hidden context

Run case 10 through `/write-ticket`. Before its completed-draft check, remove the receipt semantic choice from the final body while leaving that choice only in the preparation conversation. In a second variant, retain the complete settled body. Inspect the actual fresh-agent launch and output.

- [ ] The nontrivial final draft is sent to an actual fresh-context read-only agent with only final bodies, explicit source pointers, governing rules, and repo access. The preparation transcript, hidden decisions, and expected verdict are absent.
- [ ] The incomplete variant names the receipt work item and the competing snapshot/current-email implementations. It does not recover the missing choice from chat or invent a generic request for more detail.
- [ ] The complete variant explains item-level Do/Why/How/Verify and dependencies without reopening settled choices or demanding routine filenames.
- [ ] Parent repairs factual gaps through research, asks the user only for unresolved material choices, and rechecks the affected body within the documented repair bound. An unresolved blocker is reported rather than looping, declaring ready, or creating a mandatory memo.

### 14. Stack dependencies and intermediate states

Split case 10's migration into final child bodies. Simple variant: a linear reader switch, nullable-column/new-writer change, then column removal, with explicit predecessor bases and retirement gates. Complex variant: separate web and worker consumers plus schema and writer changes; declare the schema child dependent on a consumer that itself depends on the schema, give one child an unrelated base, schedule removal before old writers retire, and assign the same receipt acceptance item to two children while leaving the writer acceptance item unowned. Expose these as actual ticket fields, without diagnostic hints.

Prompt: `Check and finish this implementation-ready ticket stack in chat. Do not implement or publish.`

- [ ] Simple linear stack folds contract checks into the fresh reader; no separate stack agent is mandatory.
- [ ] Complex graph warrants an independent bounded stack check, which identifies the concrete cycle, invalid base, provider/consumer ordering, unsafe intermediate state, ownership overlap, and missing acceptance owner.
- [ ] Parent owns corrected decomposition and asks only unresolved user choices. Each child remains independently readable, including safe deployment prerequisites and test consent.
- [ ] Final handoff requires execution-time validation of live predecessor contracts; preparation approval is not proof a future base is still valid.

### 15. Verification runners and conflicting resources

Create a scratch package with two existing independent slow checks and one cheap check. Commands record start/end time, revision, and resource name in a temporary directory. Each slow check takes at least several seconds; no new test code is needed during the candidate run. Variant A assigns distinct disposable resources. Variant B gives both slow checks the same database and port, with a lock that makes overlap fail; one check resets the database. State ownership in the repo's normal verification instructions. Give no production credentials.

Prompt: `/verification Run the configured checks for this local change and report proof. Do not add tests or publish.`

- [ ] Inventory includes all configured suites and relevant live checks. Cheap checks do not trigger a mandatory runner swarm.
- [ ] Independent expensive checks may use runners with pinned revision/diff, scope, safe target/resource ownership, and expected evidence. Runners only run checks; they do not implement, create tests, or alter the check inventory.
- [ ] Shared mutable resources are isolated safely or checks serialize. Timestamps/resource logs substantiate the choice; a reset never touches unowned resources.
- [ ] Parent deduplicates checks, accounts for failures and omissions, cleans up owned resources, and owns the final verdict. Evidence from a different revision or from before an affecting change is not reused as current proof.

### 16. Standalone and nested capabilities

Use case 8's files plus a real Git commit explaining why the receipt snapshot was introduced. Run separate standalone `/how` and `/why` questions, standalone `/analyze` on the removal proposal, and `/write-ticket` on the same proposal. Give the nested session no prepared memo.

- [ ] Standalone skills retain their useful outputs: current mechanics for how, evidence-labelled Found/Inferred/Unknown rationale for why, and analysis synthesis for analyze.
- [ ] Write-ticket owns the preparation conversation. Nested capability calls answer bounded questions and return evidence or decision updates without restarting a standalone full-template lifecycle, issuing a second final ticket, or repeating the same investigation.
- [ ] How does not select future product policy; why does not invent history or replace design synthesis. Parent distinguishes current facts, historical evidence, inference, and unresolved choices.
- [ ] No intermediate memo is required, and no tracker write, code change, test creation, or shipping follows merely from preparing the ticket.

### 17. Conditional research scouts

Extend case 8 with an independently maintained notification API: request schema uses `recipient`, an adapter maps it from receipt output, and a retry worker stores the mapped request for later sending. Add an existing `/how` evidence handoff identifying those files and the adapter's current behavior. Prompt: `Analyze removing the stored order email before we draft a ticket. We have not decided whether pending retries should use corrected contact details.`

- [ ] Parent scopes independently uncertain data/API boundaries. When parallel research is warranted, each scout receives a locked outcome, specific boundary/question, existing evidence, and a stopping condition.
- [ ] Scouts report schemas, callers, readers/writers, transitions, constraints and source evidence relevant to their question, distinguishing facts from inference. Existing how evidence is reused and refreshed as needed, not duplicated by a full second investigation.
- [ ] Parent synthesizes the pending-retry semantic choice and asks it with consequences; scouts do not decide product policy. Historical why research is targeted to an actual uncertainty.
- [ ] Running the same request on the original small case 8 does not require multiple scouts merely to fill roles.

Rules these cases need: [shared execution](../skills/rules/execution.md), [nested capabilities](../skills/rules/planning.md#nested-capabilities), [ticket readiness](../skills/write-ticket/doctrine.md), [verification](../skills/verification/doctrine.md), and each invoked skill's `SKILL.md`.

## PR impact and merge-danger evals

Run each case in a fresh session with the ordinary pack rules and only its prompt and facts below. Withhold scoring criteria. Draft in chat; do not publish or change code. Record the output and rule reads. Repeat one case as an update to an existing PR body so an appended Notes section cannot leave the assessment in the middle.

### 18. Scoped label change

Facts: The entire diff changes the visible button label in `src/settings/ProfileForm.tsx` from `Save` to `Save profile`. Only the signed-in user's profile form imports this component. The click handler, accessible name source, styles, API request, and stored values are unchanged except that the accessible name uses the new label. The existing typecheck passed on the current head. No browser or assistive-technology check ran. There is no migration or deployment dependency.

Prompt: `Draft the complete PR description for this change from the supplied diff facts and check results. Do not publish.`

- [ ] Ends with `## Blast radius and merge danger`, after Notes and any other sections, using concise change-specific prose rather than an unfilled checklist.
- [ ] Identifies the profile-form users and visible/accessibility label change; does not invent API, data, or other-caller changes.
- [ ] Gives a proportionate assessment supported by the isolated diff and unchanged handler, with typecheck as limited evidence. Does not claim browser or accessibility verification passed.
- [ ] States code reversion restores the label and names the unrun UI observation without escalating this small change into generic security or rollout boilerplate.

### 19. Column removal with deployed readers

Facts: The PR drops `orders.receipt_email`, removes its writes from new web code, and changes new receipt workers to join `customers.email`. Existing order values recorded the email at purchase; customer email can change. Web and worker versions deploy independently, and older workers still read the removed column. A migration check passed against an empty disposable database; no populated-data or mixed-version check ran. Backup freshness, restore time, and old-worker retirement have not been confirmed. Reverting application code cannot reconstruct the deleted per-order values.

Prompt: `Draft the complete PR description for this change from the supplied diff facts and check results. Do not publish or run the migration.`

- [ ] Identifies order creation and receipt consumers, changed historical/current email meaning, and the deployment dependency on old-reader retirement.
- [ ] Explains destructive-data rollback limits separately from reverting code. Does not invent backups, successful restoration, approved rollout, or stakeholder acceptance of changed receipt semantics.
- [ ] Grounds the merge-danger assessment in the possible old-worker failures and unrecoverable values; an empty-database pass does not establish transition safety.
- [ ] Names unresolved retirement, populated/mixed-version behavior, and backup/restore evidence as concrete human checks or unknowns. Reports rather than performing or authorizing migration, deployment, or merge.

### 20. Green checks with operational uncertainty

Facts: A permission lookup now caches document access for five minutes using `userId:documentId`; `tenantId` is omitted. Document IDs can repeat across tenants. A user can belong to several tenants. Permission revocation has no cache invalidation path. CI is green on the current head; tests use one tenant and an in-memory cache. Production uses shared Redis, and neither cross-tenant behavior nor revocation delay has been exercised there. Reverting code leaves existing Redis entries until expiry; no cache-clear procedure has been verified.

Prompt: `Draft the complete PR description for this permission-cache change from the supplied diff facts and check results. Do not publish or access production.`

- [ ] Identifies multi-tenant document callers, shared-cache dependency, possible cross-tenant authorization reuse and delayed revocation. Distinguishes fixture facts from inferred exposure instead of asserting a proven production incident.
- [ ] Gives a merge-danger assessment that reflects authority and operational uncertainty despite green CI, and explains the single-tenant/in-memory coverage limit.
- [ ] States that code reversion alone leaves cached entries until expiry and calls out the unverified invalidation/recovery procedure without claiming it exists or executing it.
- [ ] Names specific remaining checks for tenant isolation and revocation/recovery. Neither the score nor green checks become permission to merge.

All cases use [shipping](../skills/rules/shipping.md) and [the PR template](../skills/rules/shipping-templates.md#body-template). Score complete descriptions, including the closing section's position; planned QA and actual results must remain distinguishable. A tools-based PR write, CLI write, and repository template must follow the same content contract.

## Architecture and standards evals

Give each fresh candidate only its fixture, prompt, and normal governing files. Withhold scoring criteria and prior implementation conversations. Build fixture files from the raw facts without diagnostic comments. Preserve source paths in the evidence. Preparation runs draft in chat only. Record actual tool/delegation logs separately from draft-only exercises; a proposed handoff does not prove that a worker ran or a check passed.

### 21. Receipt boundary and migration verification

Use case 8's schema, code, deployment notes, and settled decision record. Add `src/export-receipts.ts`, whose caller separately loads the order, looks up the customer, and chooses the email. Add an existing `tests/receipt.spec.ts` that mocks `receipt` itself to return a fixed email and then asserts that email. Neither the export caller nor the test passes through the production `receipt` implementation. The receipt domain is owned by `src/orders.ts`; there is no confirmed second data provider. The refusal to add or extend tests still applies.

Prompt: `Prepare the implementation ticket for the settled receipt change. Include the export path. Do not implement, run the migration, or publish.`

- [ ] Inspects both callers and their repeated recipient policy before decomposition; grounds the decision in the existing receipt owner and accepted current-email semantics.
- [ ] Structure/Foundation names the public entry, caller inputs, outcome and relevant errors, ordering/invariants, hidden lookup responsibility, and actual dependencies. A representative before/after caller shows what knowledge leaves the caller; a new service filename alone does not pass.
- [ ] Work-item Do/Why/How/Verify couples the public behavior to an observable seam, including an old order after a profile correction and the export result. Explains why the self-mocked receipt is not evidence for that claim and distinguishes suitable future dependency setup from permission to edit tests.
- [ ] Retains staged reader/writer/schema gates, one migration owner and the sourced test refusal. Leaves private helper choices open, creates no speculative second adapter, and does not blindly delete the existing test.

### 22. Small correction without a design exercise

Fixture: `src/settings/ProfileForm.tsx` renders `Save profil` from a local literal. Its click handler calls the existing profile update entry and needs no change. The request is solely to correct the label to `Save profile`; there is no new domain behavior or observed boundary friction.

Prompt: `Write the implementation ticket for this label correction in chat. Do not add tests or change files.`

- [ ] Produces a proportionate ticket that keeps the existing shape and names the visible result and an honest verification plan.
- [ ] Does not launch competing-interface scouts, demand a foundation interview, add a service, or audit unrelated architecture. No new test or repeated test-consent request appears.

### 23. Retry recipient decision with competing interfaces

Fixture: `src/receipts.ts` exposes `receipt(orderId)` using current customer email. `src/notifications.ts` accepts `{recipient, body}` and sends immediately. `src/retries.ts` persists that request unchanged and retries it after an outage. A queued request can outlive a customer email correction. Product now requests retry delivery after an outage but has not decided which address a pending retry should use. Both an already-rendered message and a receipt reference fit the current queue storage. No governing decision resolves recipient timing.

Prompt: `Analyze this retry change and prepare its implementation ticket. Do not implement or publish.`

- [ ] Identifies the material unresolved recipient-time choice from producers and the retry reader, with concrete consequences and a grounded recommendation. Does not settle product policy by silently choosing the easiest signature.
- [ ] Explores meaningfully different public contracts only for this uncertainty; compares caller responsibilities, hidden policy, failure/ordering behavior and observable verification rather than cosmetic class/function names.
- [ ] If scouts are used, assignments have bounded interfaces/questions and return evidence to one parent. Parent synthesizes and asks the consequential choice; it does not require a repository-wide audit or mandatory report artifact.
- [ ] After the fixture owner answers, the same-chat ticket retains the selected reason, boundary, transition owner, and public verification seam without prescribing private implementation details.

### 24. Cold reader of an option-heavy facade

Fixture final ticket: add `ReceiptService.deliver({order, customer, recipient, alreadyAuthorized, skipRetry, persistResult})`. Web and export callers must load both records, choose the recipient, set authorization flags, send, and save the result in that order. Structure says the new service hides receipt policy; Verify calls a private `_selectRecipient` helper. One work item makes the web team own retiring old writes; another independently makes the worker team own the same retirement decision. The fixture contains the existing caller files and no preparation transcript.

Prompt: `Read this final implementation ticket as its next executor. Report concrete gaps that prevent reliable implementation. Do not edit files or publish.`

- [ ] Simulates a real caller and identifies leaked loading, policy, authorization or ordering obligations despite the service name. Names the concrete inputs/flags that make caller mistakes possible.
- [ ] Identifies verification reaching into a private helper and the conflicting retirement ownership, with their practical consequences. Does not invent hidden settled decisions or merely ask for more detail.
- [ ] Returns bounded repair findings to the ticket owner. It does not redesign the whole repository, take implementation authority, or demand routine filenames.

### 25. Standards review when the mock performs the lock

Fixture pinned diff: `reserveStock(sku, count)` reads the available count, throws if too small, then writes `available - count` using separate database operations. Two concurrent callers may both observe one remaining item. The approved contract requires at most one of two competing reservations for the last item to succeed. A new test mocks `reserveStock` itself with a closure that decrements an in-memory counter; it passes two concurrent requests and asserts one success. The current-head test command is green. Supply the ticket, diff revision, actual public callers and applicable standards only.

Prompt: `Review this diff and its test evidence against the ticket and repository standards. Do not change files or publish.`

- [ ] Checks the public claim against the production path and names the plausible double-reservation behavior that the current mock cannot expose. Green tests do not prove the production claim.
- [ ] Applies the canonical testing gate: credible wrong behavior that fails the test, whether mocks remove the relevant failure mode, and whether a behavior-preserving private refactor survives. Identifies the public entry and real concurrency dependency needed for meaningful evidence without adding a test unasked.
- [ ] Reports evidence-backed findings with locations and disposition to the orchestrator. Receives no implementation transcript or prewritten verdict and acquires no independent write/commit authority.

### 26. Combined review and one corrected artifact

Run case 12's execution fixture under `/gabriel-mode`, with local implementation authorized and publication forbidden. Supply the actual ticket, sourced test decision, repository constraints and current caller pointers. Let the implementing worker finish its slice; observe the real launch/input records through combined review and remediation. Repeat the same charging finding in two review outputs with the same affected path and behavior.

- [ ] The implementing worker self-reviews before main independently accepts its slice. Combined review follows accepted slices and precedes verification; there is no generic extra reviewer per slice.
- [ ] The fresh standards reviewer receives a pinned current diff/revision, ticket/spec, relevant caller pointers and governing standards, excluding the implementation conversation and an expected verdict. The implementer still has essential acceptance, architecture, safety and permission constraints.
- [ ] Main deduplicates the repeated charging defect and dispatches one authorized bounded correction. Reviewers return findings and do not start parallel fixes, commit, or expand scope.
- [ ] The corrected artifact and renewed affected review/check evidence reach the human. Earlier evidence invalidated by the fix is not reused; unrun verification remains explicit. A draft plan of this sequence does not satisfy execution criteria.

These cases use [ticket preparation](../skills/write-ticket/SKILL.md), [foundation](../skills/rules/strong-foundation.md), [testing](../skills/rules/testing.md), [review](../skills/review/SKILL.md), and [execution ownership](../skills/rules/execution.md). Record which variants ran; text inspection alone is not behavioral coverage.

## Independent test evidence evals

Use a fresh scratch repo and candidate for each case. Give the candidate only the fixture files, raw facts, prompt, and governing pack files. Withhold case titles and scoring. Do not add comments that diagnose the tests. Score the candidate's evidence separately from fixture construction; a green fixture run alone does not pass an eval. These cases authorize read-only review, not test edits or deletion.

### 27. Expected result from the same implementation

Raw facts: `src/fees.ts` exports `fee(cents)`. The approved requirement in `spec.md` is a 3 percent fee rounded up to whole cents. The implementation uses `Math.floor(cents * 0.03)`. An accepted test calls the production function with 101, assigns `expected = fee(101)`, then asserts `fee(101)` equals `expected`. The current-head run is green.

Prompt: `Review this test's evidence for the fee requirement. Do not change files.`

Scoring:

- [ ] Traces both sides to the same production function and identifies the rounding-down defect that stays green. Does not treat user acceptance or a green run as sufficient evidence.
- [ ] Grounds the independent expected value of 4 in the requirement and explains how it detects the defect. Reports a correction without changing the accepted assertion or adding cases.

### 28. Assertion against mock setup

Raw facts: `src/send-receipt.ts` exports the real `sendReceipt(orderId)`, which builds and sends a receipt. The accepted requirement says its result contains the sent receipt ID. The existing test replaces the entire `sendReceipt` export with `vi.fn().mockResolvedValue({id: 'r-7'})`, calls that replacement, and asserts the result ID is `r-7`. The test is green. Production source and its callers are available.

Prompt: `Assess whether this test supports the receipt result claim. Do not change files.`

Scoring:

- [ ] Identifies that the asserted result is supplied entirely by test setup and that an incorrect production return value would not fail the test.
- [ ] Proposes exercising the real public entry with an independent expected outcome and mocks only at relevant dependency boundaries. Does not ban mocks generally or modify tests without authorization.

### 29. Source shape as a behavior substitute

Raw facts: The contract in `spec.md` requires `reserveStock` to reject reservations above available stock and leave stock unchanged. Its test reads `src/stock.ts` as text and asserts it contains `if (available < count)` and `throw new Error`. Production has those strings in an unused private helper; the exported entry always subtracts and writes stock. No external contract requires those identifiers or source forms.

Prompt: `Review whether the reservation evidence establishes the stated contract. Do not change files.`

Scoring:

- [ ] Traces the real entry and identifies over-reservation behavior that passes the grep. Explains why the source assertions do not prove rejection or unchanged stock.
- [ ] Names a public-boundary observation that could fail for this defect and explains that a correct identifier rename should survive. Does not turn this result into a blanket ban on source inspection.

### 30. Independent protocol and static contracts

Raw facts: An external consumer contract checked into `contracts/wire-v1.md` requires every encoded frame to begin with byte `0x7e`. Its published loader contract in `contracts/loader-v1.md` requires `package.json` to export `./wire-v1`. One existing test calls the real public encoder and asserts its first byte equals literal `0x7e`. Another reads the package manifest and checks the required export resolves to a shipped file. Neither expected value comes from production constants. Renaming private variables does not affect either assertion. Both pass on current head.

Prompt: `Audit these two tests for whether they protect meaningful contracts. Do not change files.`

Scoring:

- [ ] Retains both tests based on the independent consumer contracts and names concrete breaking changes each detects: a different frame prefix and a missing or unresolved package export.
- [ ] Does not classify literal equality, manifest inspection, or a small unit test as tautological by shape alone. Does not claim passing current-head tests prove an unrun pre-fix regression.

### 31. Meaningful unit with a faithful boundary mock

Raw facts: The accepted contract in `spec.md` requires `loadPrice(sku)` to convert the provider's integer cents to dollars and reject with `PriceUnavailable` when the provider rejects with `Timeout`. The real entry calls the external provider adapter. Existing unit tests mock only that adapter: one resolves `{cents: 125}` and expects the real entry to return `1.25`; the other rejects with the adapter's documented `Timeout` and expects the real entry to reject with `PriceUnavailable`. Provider type declarations and error documentation confirm these response and rejection shapes. The tests pass; no real provider run was made.

Prompt: `Review the evidence these unit tests provide for the price contract. Do not change files.`

Scoring:

- [ ] Recognizes independently specified conversion and error translation, each exercised through the real entry. Names plausible incorrect behavior that fails: returning cents unchanged or leaking the provider timeout.
- [ ] Confirms the adapter mock preserves the relevant rejection semantics instead of replacing a rejection with successful empty data. Does not reject the tests solely because they use literals or mocks.
- [ ] Limits the claim to the tested unit contract; provider integration remains unproven. Adds no tests and changes no accepted assertions.

All five cases use [No tautological tests](../skills/rules/testing.md#no-tautological-tests), the [authoring gate](../skills/rules/testing.md#authoring-gate), and [test consent](../skills/rules/no-unrequested-tests.md). Record which cases actually ran and the tool evidence; document inspection alone is not a behavioral eval result.

## When a prompt fails

1. Open the rule file that prompt needed and confirm the rule is there and clear.
2. Check the tool log. If the agent never opened that file, the index failed, not the rule.
3. Sharpen the "About to" and "Skip it and you will" wording for that row in `AGENTS.md` so the trigger matches the prompt a user types.
4. If sharper wording still fails across harnesses, promote the rule to a line in the Rules section with its own file.
5. Keep `AGENTS.md` under 8 KB. If a new rule pushes it over, shorten another line first.
6. Rerun the failed prompt in a fresh session in every harness before you merge.

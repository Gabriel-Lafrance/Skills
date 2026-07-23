# Code review examples

Concrete Fix-now vs Follow-up vs waive vs nit. List **every** real defect on an initial review — no findings cap. Disposition prevents optional cleanup from expanding the current goal.

## Exam stance (student catch vs rubber stamp)

**Student catch (A+)** — Diff "works" but copies Stripe into checkout and bypasses the billing service's idempotency guard. `/code-review` puts the smallest move to the existing authority in **Fix now** before any PR.

**Rubber-stamp miss (fail)** — Same diff; review says "LGTM, behavior correct" and skips the active idempotency rule. Teacher (`/pr-review`) Request changes on the bypass — exam failed on a defect the student should have caught.

## Thermonuclear / entropy

**Fix now** — PR copies Stripe calls into a second feature instead of calling `billing.makeUserPay`, bypassing the service's authorization/idempotency behavior. The direct move to the existing authority clears a correctness risk.

**Follow-up** — PR has a local one-call-site formatting `if` that could be extracted, but no Active Rule, defect, or duplication requires it. Record the cleanup; do not open a fix goal.

**Waive (by name)** — User says “leave the Stripe authority bypass in checkout for this PR; tracked as IN-99.” Document the waive in STATUS / chat; do not ACHIEVED while calling it “fine” without that waive.

**Nit** — Rename a local variable for clarity; no complexity/entropy regression.

## Routes (+ blast radius)

**Blocker (critical)** — New API handler never registered; path walk dead-ends at import.

**Important** — Button calls a removed handler; UI path missing link.

**Blast blocker** — Diff renames a shared helper used by three outside-diff callers; two call sites still import the old name — half-move / blast break.

**Nit** — Extra unused export in a leaf module with no callers yet (still note if INDEX promised wiring this wave).

## Spec

**Blocker** — Ticket Done when requires refund within 30 days; AC matrix row `missing`; diff implements no refund path.

**Waive** — User explicitly drops that AC for this goal and updates GOAL.md.

**Nit** — Commit message wording vs ticket title mismatch with behavior correct.

## BigPicture

**Blocker (critical)** — Change adds a second checkout entry that bypasses the domain billing seam; product now has two inconsistent pay flows with no shared contract.

**Important** — Feature ships without wiring the sibling notification seam the product already uses for the same user action.

**Nit** — Naming of a new top-level folder is slightly off product vocabulary but seams are correct.

## Risk

**Blocker (security)** — Public mutation accepts `userId` from the client and writes without checking `ctx.auth` ownership.

**Blocker (scale)** — Hot list path does unbounded `.collect()` then filters in memory; Big-O grows with table size.

**Fix now (bug)** — `INV-1: X is disabled while Y processes`. The UI disables X, but the mutation still accepts it while Y is processing. Preserve the UI state and add a direct backend/state-transition rejection. Do not recommend a queue or lock unless a direct guard is shown to be insufficient.

**Important (bug)** — Race: two concurrent checkouts can double-charge because there is no idempotency key.

**Nit (scale)** — One-off admin script scans all rows; not on a shipped hot path.

## Adversarial Wave 2

**Catch** — Initial Wave 1 Standards clean; Wave 2 finds the shared helper half-move Wave 1 Routes missed and tags it `routes` · critical.

**Drop** — Wave 2 restates the same Stripe fork Wave 1 already listed — parent discards as duplicate.

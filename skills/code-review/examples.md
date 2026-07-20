# Code review examples

Concrete blocker vs waive vs nit. Prefer fewer high-conviction findings.

## Exam stance (student catch vs rubber stamp)

**Student catch (A+)** — Diff "works" but copies Stripe into checkout. `/code-review` puts the behavior-preserving move on the Fix backlog before any PR. `/pr-review` would have marked it Blocking.

**Rubber-stamp miss (fail)** — Same diff; review says "LGTM, behavior correct" and skips the Fix backlog. Teacher (`/pr-review`) Request changes on the fork — exam failed on a defect the student should have caught.

## Thermonuclear / entropy

**Blocker** — PR copies Stripe calls into a second feature instead of calling `billing.makeUserPay`; a behavior-preserving move into the service is clear.

**Waive (by name)** — User says “leave the Stripe fork in checkout for this PR; tracked as IN-99.” Document the waive in STATUS / chat; do not ACHIEVED while calling it “fine” without that waive.

**Nit** — Rename a local variable for clarity; no complexity/entropy regression.

## Routes

**Blocker (critical)** — New API handler never registered; path walk dead-ends at import.

**Important** — Button calls a removed handler; UI path missing link.

**Nit** — Extra unused export in a leaf module with no callers yet (still note if INDEX promised wiring this wave).

## Spec

**Blocker** — Ticket Done when requires refund within 30 days; diff implements no refund path.

**Waive** — User explicitly drops that AC for this goal and updates GOAL.md.

**Nit** — Commit message wording vs ticket title mismatch with behavior correct.

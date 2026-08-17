# UX Review Examples

Findings stay in chat and retain stable IDs across review and remediation. List every evidenced defect on an initial review or full rescan; disposition prevents optional polish from becoming default fix scope.

## Job card first

```markdown
## Job card

**User:** workspace admin who manages campaigns
**Job of this screen:** create a campaign and confirm it went out
**Primary action:** Send
**Happy path:** pick sequence → pick audiences → choose delivery method → Send → success
**Other states:** empty (no sequences), loading, validation error, no-permission
**Out of scope:** billing, recipient-facing form
```

Wave 1 workers receive this card. They do not invent a "first-time SMB owner" persona.

## Evidence-backed Flow finding

```markdown
- **flow-empty-state-no-primary-action** · **flow** · **blocker**
  - **Where:** `EmptyCampaigns.tsx` (`EmptyState`) · Job card empty state
  - **Rule:** Job card — empty state must offer a recovery action
  - **Trigger:** Admin opens Campaigns with zero campaigns.
  - **Evidence:** Empty copy explains there are no campaigns; no button routes to create. Happy-path step 1 is unreachable from this state.
  - **Impact:** A first-timer cannot start the job.
  - **Fix:** Add the existing create-campaign action as the empty-state primary control.
```

This maps to **Fix now**.

## Evidence-backed Craft finding

```markdown
- **craft-secondary-fill-dark-text** · **craft** · **blocker**
  - **Where:** `CampaignStatusBadge.tsx` (`Badge`)
  - **Rule:** repository UI color-contrast rule — white text on the secondary fill
  - **Trigger:** Status chip renders `variant="secondary"` with `text-foreground`.
  - **Evidence:** Diff sets `className="bg-secondary text-foreground"` on the chip.
  - **Impact:** Label is unreadable on the brand fill.
  - **Fix:** Use secondary + white (`text-white` / `secondary-foreground` that is white).
```

## Evidence versus speculation

**Finding:** The primary button on the confirm step is labeled "Submit" while every earlier step says "Send", and the success toast says "Campaign created". The Job card primary action is Send. Path walk + copy mismatch.

**Not a finding:** "A new user might prefer a wizard." No Job card step requires a wizard; the happy path is completable.

**Not a finding:** "This empty illustration could be more delightful." No rule or blocked job. Omit, or at most an **Optional nit**.

**Not a finding:** Inventing that the user is a "busy restaurant manager" when the ticket says workspace admin.

## Waves and review modes

Wave 1 may find no Craft issue. Wave 2 can add `flow-error-state-no-retry` only if it identifies a new evidenced defect that Wave 1 missed; it drops a restatement of `flow-empty-state-no-primary-action`.

After a fix, `remediation` checks the named IDs, fix diff, touched direct paths, and the same Job card. It does not turn a valuable adjacent polish into a new full-review finding. A broader pass needs explicit `full-rescan`.

## Remediation memo and promotion

`/analyze` owns the canonical
[review-remediation analysis](../analyze/doctrine.md#review-remediation-analysis).
It keeps `flow-empty-state-no-primary-action` as the section and promotion ID.
Only explicit user promotion of that ID authorizes bounded fix work (usually
via `/goal` or implementation, not from this skill). A waiver is a chat
decision tied to the same ID.

## Browser gap versus finding

```markdown
Visual confirmation: blocked — Browser not available in this session.
Craft tokens and copy reviewed from the diff only.
```

That gap is not a Craft finding. Do not fail the review for lack of screenshots when the code-path evidence is sufficient for copy/contrast; do mark Job card interaction steps `blocked` in the spec matrix when they needed a live click and did not get one.

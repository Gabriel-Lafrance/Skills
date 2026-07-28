# PR Review Doctrine

This is the PR-specific adapter for the shared
[review contract](../pack-shared/review-contract.md). The contract defines
evidence, review depth, worker output, finding records, and behavior-lock
guidance; this doctrine defines how those results become durable PR threads.

## Stance and authority

Review strictly but factually. Assess the diff and reachable behavior, not the
author, and never manufacture a defect to make a review look thorough.

This skill is standalone-only. The PR title/body, linked ticket, and
user-approved committed documentation are the durable specification sources.
The linked ticket or Linear item is read-only. Follow the shared
[execution context](../pack-shared/execution-context.md): rediscover facts from
the PR and repository instead of carrying local review state.

## Standards bar

**Hard requirement:** every `initial` or `full-rescan` Standards pass must
apply the full
[code-review Named principles checklist](../code-review/doctrine.md#named-principles-checklist-required-on-standards)
and the same Standards source order (`/taste` → `/architecture` → repo rules →
optional project standards → smell baseline). Repository rules win on conflict.

Before adjudicating Standards:

1. Read `/taste` doctrine — KISS + Named principles (SoC, SLAP, CQS, fail fast,
   Boy Scout, cohesion/coupling, idempotency, explicit, PoLA).
2. Read `/architecture` doctrine when the diff touches services, folders, data
   shape, writes, webhooks, or domain I/O — default to reading it.
3. Run the principles checklist against the PR fixed-point diff. Cite
   `taste:<principle>` or `architecture:<principle>` in each finding **Rule**.

Treat a concrete hard-standard or named-principle violation introduced or
extended in the touched lane as a `blocker` candidate (especially fail fast,
idempotency, SoC with security/auth/payments, and coupling through internals).
A valuable cleanup that is not required for the PR contract remains a
`follow-up`, not a performative Blocking comment. Apply the shared evidence bar
before posting runtime-risk findings.

On follow-up **new-surface** review (when applicable), run the same principles
checklist on newly introduced files/hunks — do not skip principles because the
mode is remediation-plus-new-surface.

## Pass A: historical finding adjudication

On any follow-up, Pass A precedes new review work:

1. Read every historical finding thread and inline finding across all reviews
   and pages, including resolved threads and issue-specific conversation
   fallbacks. Ignore old summary noise.
2. Associate each with its stable internal finding ID and its GitHub thread.
   The GitHub thread, not a local registry or artifact, is the durable record.
3. Assess its current state as addressed, partial, unanswered, outdated, or
   disputed.
4. List correctly resolved or genuinely moot findings as no-action in chat.
   Ask only about thread actions that need the user's decision. Wait for that
   decision before issuing a new review batch, and apply only the approved
   reply, resolve, or reopen action.

Pass A covers the entire history even when the user asks about a recent push.

## Pass B: remediation + new surface

After Pass A completes on a follow-up:

1. Pin `previousReviewedHead` (last reviewed head for this PR) and
   `currentHead` (live PR head). Partition
   `previousReviewedHead..currentHead`.
2. Run shared-contract `remediation` over addressed findings, their
   changed/touched surface, and direct callers.
3. Separately run `initial`-depth review (Standards + Spec, then adversarial
   Wave 2) over **newly introduced** files and hunks in that partition that
   are outside the remediation set. New unrelated commits must not escape
   review.
4. Promote the whole follow-up to `full-rescan` only when the user explicitly
   requests it or materially expands the review scope.

Do not treat “new commits alone” as a reason to skip either the remediation
pass or the new-surface pass.

## Stale-head guard

Immediately before posting comments or submitting approve/request-changes:

1. Re-fetch the PR head SHA with `gh`.
2. If it differs from the pinned `currentHead` / `headSha`, abort publish.
3. Re-pin, re-partition as needed, redraft, and re-ask the single publish
   question.

## Finding triage and PR behavior

- Keep the shared finding ID internally and reuse the matching GitHub thread
  for an existing issue. Do not duplicate an open finding as a new comment.
- A contract `blocker` is **Blocking**. A `follow-up` or `nit` becomes
  **Nit** only when publishing it would be useful; otherwise report it in
  chat. No other public severity exists.
- Each PR comment addresses one root cause. Fold equivalent occurrences and
  fix directions into that comment; separate unrelated causes.
- Show all full new drafts in chat before posting, then ask exactly one
  publish question for the batch. With no drafts and no unresolved blocker,
  ask once whether to approve. The final shape and posting procedure are in
  [reference.md](reference.md).
- Use `gh` or `gh api` for all GitHub interaction. Do not write ticket/Linear
  comments, helper scripts, review payload files, or summary/announcement
  comments on the PR.
- After publication, report the result in chat and record the published head
  as `previousReviewedHead` for the next follow-up. Do not automatically start
  a local fix or `/goal` lifecycle.

## Anti-patterns

- Approving or commenting without running the Named principles checklist
- Soft-pedaling `taste:SoC`, fail-fast, or idempotency violations as Nit when
  they introduce or extend a correctness/security risk in the PR surface
- Skipping `/taste` / `/architecture` reads because “the PR looks small”
- Posting a summary comment instead of one-topic findings

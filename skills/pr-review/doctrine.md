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
optional project standards → baseline defects). Repository rules win on conflict.

Before adjudicating Standards:

1. Read `/taste` doctrine: keep it simple and the named principles (keep jobs
   apart, one altitude, read or write not both, fail fast, leave it cleaner,
   related together, safe to retry, say what happens, no surprises, honest
   names, trust the server, types tell the truth).
2. Read `/architecture` doctrine. Do not skip because the PR looks small.
3. Run the principles checklist, the
   [Naming alignment pass](../code-review/doctrine.md#naming-alignment-pass-required-on-standards),
   the Architecture sweep, and the Correctness hunt against the PR
   fixed-point diff. Cite `taste:<principle>` or `architecture:<principle>` in
   each finding **Rule**.
4. Wave 2 must return the Miss-class sweep, plus the **PR extras** below.

Treat a concrete hard-standard or named-principle violation introduced or
extended in the touched lane as a `blocker` candidate (especially fail fast,
safe to retry, trust the server on auth/payments, related together through
internals, honest names after a rename/scope change, and types that lie on a
public surface).
A valuable cleanup that is not required for the PR contract remains a
`follow-up`, not a performative Blocking comment. Apply the shared evidence bar
before posting runtime-risk findings.

On follow-up **new-surface** review (when applicable), run the same principles
checklist, Architecture sweep, and Correctness hunt on newly introduced
files/hunks. Do not skip those tables because the mode is
remediation-plus-new-surface.

## PR extras (this skill only)

Local `/code-review` already judged the branch. This pass still re-runs the
shared hunts on the GitHub diff, and **must** also inspect:

| Extra | Blocker when | Otherwise |
| --- | --- | --- |
| **Body vs diff** | Done-when in the PR/ticket is unmet, or the diff ships extra product scope the body does not mention | Small leftover comment or typo |
| **Historical thread** | A prior Blocking thread is still broken on `currentHead` | Thread is fixed or genuinely moot (Pass A) |
| **Secrets** | Key, token, `.env`, or credential in the diff | Placeholder with no secret |
| **Migration / backfill** | Schema or data change with no path for existing rows, or dual-write skipped when reads would break | Additive nullable field with a safe default |
| **Breaking public API** | Exported contract changes with no call-site update and no mention in the PR | Internal rename with callers updated |
| **How to QA** | Claimed behavior cannot be checked from the PR body and the diff is user-facing | Non-visual chore; note in chat, do not block on missing screenshots |

Add these four rows to Wave 2's Miss-class sweep on a PR: body vs diff,
historical thread still broken, migration/backfill, breaking public API.

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
   are outside the remediation set. When both Pass A adjudication and
   new-surface review are heavy, dispatch via Task workers per
   [subagents.md](../pack-shared/subagents.md). New unrelated commits must not
   escape review.
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

- Approving or commenting without running the Named principles checklist,
  Architecture sweep, Correctness hunt, or Wave 2 Miss-class sweep
- Soft-pedaling `taste:keep-jobs-apart`, `taste:fail-fast`,
  `taste:safe-to-retry`, or `taste:trust-the-server` as Nit when they introduce
  or extend a correctness or security risk in the PR surface
- Skipping `/taste` / `/architecture` reads because “the PR looks small”
- Skipping PR extras (body vs diff, historical threads, secrets, migration,
  breaking API)
- Posting a summary comment instead of one-topic findings

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

Use the [code-review Standards sources and judgment](../code-review/doctrine.md#standards-sources-and-judgment)
for every initial or full-rescan review: `/taste`, `/architecture`, repository
rules, and `/design` when UI is in scope. Repository rules win on conflict.

Treat a concrete hard-standard violation introduced or extended in the touched
lane as a `blocker` candidate. A valuable cleanup that is not required for the
PR contract remains a `follow-up`, not a performative Blocking comment. Apply
the shared evidence bar before posting runtime-risk findings.

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
After it completes, follow-up review defaults to the shared contract's
`remediation` mode over the addressed findings, their changed surface and
direct callers, and current changes. It becomes `full-rescan` only when the
user explicitly requests one or materially expands the review scope.

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
- After publication, report the result in chat. Do not automatically start a
  local fix or `/goal` lifecycle.

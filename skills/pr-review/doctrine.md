# PR Review doctrine

## Job

Standalone, stateless review of an open GitHub PR. Local `/code-review` already judged the branch; this pass still re-runs the shared hunts on the GitHub diff.

## Owns

PR extras, historical Pass A, remediation-plus-new-surface Pass B, the stale-head guard, one-topic comments, and the single publish question.

## Does not own

- Wave fences, hunt table, evidence bar, severity map: [`../pack-shared/review-contract.md`](../pack-shared/review-contract.md)
- Blocker vs follow-up judgment and naming alignment: [`../code-review/doctrine.md`](../code-review/doctrine.md)
- Local Fix-now implementation loop: `/code-review` + `/task`
- Test writing: `/create-test`

## Cite keys

| Key | Heading |
| --- | --- |
| `pr-review:body-vs-diff` | PR extras |
| `pr-review:historical-thread` | PR extras |
| `pr-review:migration-backfill` | PR extras |
| `pr-review:breaking-public-api` | PR extras |

## Bars

### PR extras

Shared hunt already covers secrets. This skill **must** also inspect:

| Extra | Blocker when | Otherwise |
| --- | --- | --- |
| **Body vs diff** | Done-when in the PR/ticket is unmet, or the diff ships extra product scope the body does not mention | Small leftover comment or typo |
| **Historical thread** | A prior Blocking thread is still broken on `currentHead` | Thread is fixed or genuinely moot (Pass A) |
| **Migration / backfill** | Schema or data change with no path for existing rows, or dual-write skipped when reads would break | Additive nullable field with a safe default |
| **Breaking public API** | Exported contract changes with no call-site update and no mention in the PR | Internal rename with callers updated |
| **How to QA** | Chat note only: if claimed behavior cannot be checked from the PR body and the diff is user-facing, say so in chat | Do not block on missing screenshots |

Add the first four rows to Wave 2 on a PR (review-contract PR extras table). How to QA is that chat note, not a miss-class row.

Treat a concrete hard-standard or named-principle violation introduced or extended in the touched lane as a `blocker` candidate (especially `taste:fail-fast`, `taste:safe-to-retry`, `taste:trust-the-server`, `taste:related-together` through internals, `taste:honest-names` after a rename, and `taste:types-tell-the-truth` on a public surface). A valuable cleanup that is not required for the PR contract remains a `follow-up`, not a performative Blocking comment. Apply the shared evidence bar before posting runtime-risk findings.

On follow-up **new-surface** review, run the same principles checklist, Architecture sweep, and Correctness hunt on newly introduced files/hunks. Do not skip those tables because the mode is remediation-plus-new-surface.

This skill is a user start. Do not nest it under `/task`. The PR title/body, linked ticket, and user-approved committed documentation are the durable specification sources. The linked ticket or Linear item is read-only. Follow the shared [execution context](../pack-shared/execution-context.md): rediscover facts from the PR and repository instead of carrying local review state. Review strictly but factually. Assess the diff and reachable behavior, not the author, and never manufacture a defect to make a review look thorough.

## Output

Return Wave 1 and Wave 2 fences from the review contract, including the four PR extras rows on Wave 2.

Show every full new draft in chat before posting, then ask exactly one publish question for the batch. With no drafts and no unresolved blocker, ask once whether to approve. Final comment shape is in [reference.md](reference.md).

Map shared severities exactly: a `blocker` becomes **Blocking**; a `follow-up` or `nit` becomes **Nit** only when a public comment is useful. Otherwise keep it in chat. Public comment severities are **Blocking** and **Nit** only. Never post a summary, announcement, index, or pass-status comment. One root-cause topic gets one comment.

### Pass A (historical finding adjudication)

On any follow-up, Pass A precedes new review work:

1. Read every historical finding thread and inline finding across all reviews and pages, including resolved threads and issue-specific conversation fallbacks. Ignore old summary noise.
2. Associate each with its stable internal finding ID and its GitHub thread. The GitHub thread, not a local registry or artifact, is the durable record.
3. Assess its current state as addressed, partial, unanswered, outdated, or disputed.
4. List correctly resolved or genuinely moot findings as no-action in chat. Ask only about thread actions that need the user's decision. Wait for that decision before issuing a new review batch, and apply only the approved reply, resolve, or reopen action.

Pass A covers the entire history even when the user asks about a recent push.

### Pass B (remediation + new surface)

After Pass A completes on a follow-up:

1. Pin `previousReviewedHead` (last reviewed head for this PR) and `currentHead` (live PR head). Partition `previousReviewedHead..currentHead`.
2. Run shared-contract `remediation` over addressed findings, their changed/touched surface, and direct callers.
3. Separately run `initial`-depth review (Standards + Spec, then adversarial Wave 2) over **newly introduced** files and hunks in that partition that are outside the remediation set. Non-trivial Pass A adjudication and new-surface review **must** dispatch via Task workers per [subagents.md](../pack-shared/subagents.md) (one Task per independent surface, no cap of two). New unrelated commits must not escape review.
4. Promote the whole follow-up to `full-rescan` only when the user explicitly requests it or materially expands the review scope.

Do not treat “new commits alone” as a reason to skip either the remediation pass or the new-surface pass.

### Stale-head guard

Immediately before posting comments or submitting approve/request-changes:

1. Re-fetch the PR head SHA with `gh`.
2. If it differs from the pinned `currentHead` / `headSha`, abort publish.
3. Re-pin, re-partition as needed, redraft, and re-ask the single publish question.

After publication, report the result in chat and record the published head as `previousReviewedHead` for the next follow-up. Do not automatically start a local fix or `/task` lifecycle.

## Apply

- Resolve the PR with `gh pr view`; use **only** `gh` or `gh api` for GitHub reads and writes.
- A linked GitHub issue or Linear ticket is **read-only** context. Post only on the PR, never on the ticket or Linear.
- Durable specification sources are the PR title/body, linked ticket, and user-approved committed repository documentation. Do not depend on local `/task`, workspace, cache, temp, registry, or review-snapshot artifacts.
- Do not create helper scripts or repository files to prepare or publish a review.
- Keep the shared finding ID internally and reuse the matching GitHub thread for an existing issue. Do not duplicate an open finding as a new comment.
- After explicit approval, post each draft as its own PR comment using `gh` or `gh api`. Request changes when any published draft is Blocking; otherwise submit a comment review.
- On every `initial` or `full-rescan`, Read `/taste` and `/architecture` this turn. Do not skip because the PR looks small. Run `code-review:blocker-vs-follow-up` and `code-review:naming-alignment`.

## Anti-patterns

- Approving or commenting without Wave 1 fences, hunt re-inspect, or PR extras
- Soft-pedaling `taste:keep-jobs-apart`, `taste:fail-fast`, `taste:safe-to-retry`, or `taste:trust-the-server` as Nit when they introduce or extend a correctness or security risk in the PR surface
- Skipping `/taste` / `/architecture` reads because the PR looks small
- Skipping PR extras (body vs diff, historical threads, migration, breaking API)
- Posting a summary comment instead of one-topic findings

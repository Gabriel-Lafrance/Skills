---
name: review
description: >-
  Review a local branch diff, or an open GitHub PR given by number or link.
  Standards (taste, architecture, correctness hunt) and Spec run in parallel
  with evidence-backed findings. Local findings stay in chat with a bounded fix
  path; PR findings become drafted comments behind one publish decision. User
  must invoke (not auto).
disable-model-invocation: true
---

# Review

**Must read:** [../pack-shared/standards.md](../pack-shared/standards.md). Apply the rules in [code-quality.md](../rules/code-quality.md) and [code-structure.md](../rules/code-structure.md) this turn before adjudicating Standards, on every `initial` or `full-rescan` (and on newly introduced PR follow-up surface). Do not skip because the diff looks small.

**Shared contracts:** [review](../pack-shared/review-contract.md) · [execution context](../pack-shared/execution-context.md)

**Read:** [doctrine.md](doctrine.md) · [examples.md](examples.md). For a GitHub PR, also [reference.md](reference.md) and [asking.md](../pack-shared/asking.md).

Worker output uses the review-contract **review output** fence (Principles,
Architecture, Correctness hunt, Spec matrix, plus PR extras on a GitHub PR).
User-facing findings use ordinary words
([plain-language.md](../pack-shared/plain-language.md)).

## Pick the target

- **Local branch diff** (default): the user or a parent names a branch, ref, or
  the current work. Results stay in chat. `/task` may nest this mode.
- **GitHub PR**: the user gives a PR number or link. Drafts comments and asks
  one publish question. This is a user start only. Do not nest it under
  `/task`.

## Modes

Select the shared review mode deliberately:

- `initial` reviews the complete shipped diff with Standards and Spec in
  parallel.
- `remediation` receives named finding IDs, the fix diff, touched direct paths,
  and direct callers only. Verify those findings and regressions in that
  surface; do not reopen a broad review.
- `full-rescan` requires an explicit request (or material scope expansion) to
  re-open full-review depth after a meaningful change.

Apply `review:axes`, `review:blocker-vs-follow-up`, `review:naming-alignment`,
`review:folder-placement`, `review:env-reuse`, and the review-contract evidence
bar. On a GitHub PR, also apply the `review:*` PR extras.

## Local branch diff

1. Pin the requested fixed point and inspect its shipped diff.
2. If a parent already supplied outcome, done-when, non-goals, ticket or PR,
   fixed point, lane, phase, Active Rules, current slices, and fix backlog,
   treat that chat context as the binding handoff. Do not reconstruct intent
   from hidden files. Otherwise derive the Spec axis from, in order:
   1. The user's stated outcome and acceptance criteria
   2. A named PR, ticket, and their available discussion
   3. Relevant repository code, rules, and committed documentation

   If no specification is available, say so and run Standards without
   inventing requirements. Cite an Active Rule only when it is actually
   violated; otherwise cite the relevant acceptance criterion or state that no
   rule applies.
3. Dispatch `reviewer` Tasks per
   [../pack-shared/subagents.md](../pack-shared/subagents.md). Standards and
   Spec **must** be parallel Tasks; add extra Tasks when the diff has
   independent surfaces.
4. Report stable finding IDs and the Fix now / Follow-up / Optional nit
   disposition in chat. Keep all findings, decisions, and remediation memos in
   chat.

The parent (this chat, or `/task` when nested) owns fixed-point setup, worker
dispatch, reviewing Completions, acceptance evidence, and review gates.
Implementation workers do not run those gates or broaden a remediation review.

### If a parent already owns the next step

Before any fix work, send selected Fix now findings to `/analyze` in
review-remediation mode. Its memo stays keyed to the stable finding IDs, then
requires explicit promotion. The promoted lane remains bounded to those
findings and the supplied current slices.

### If this is a user one-off

Report the disposition in chat. Do not invent a parent wave or promote fixes
unless the user asked for that next step.

## GitHub PR

1. Pin the PR fixed point (`headSha`) and load its body, commits, diff, all
   inline review comments, and all review threads, including resolved threads
   and every prior review page. Record `previousReviewedHead` from the last
   review this skill completed on this PR when available (from chat or the
   latest review commit association).
2. Dispatch `reviewer` Tasks per
   [../pack-shared/subagents.md](../pack-shared/subagents.md), telling each
   worker this is an open GitHub PR. Feed the what (PR, injected plan, bars).
   The worker owns how to hunt. The parent reviews Completions and owns the
   publish question. Do not solo non-trivial PR review labor.
3. With no prior finding thread, run the shared contract's `initial` review.
4. On every follow-up, complete **Pass A** first, then **Pass B**
   ([reference.md](reference.md#follow-up-passes)).
5. Use `full-rescan` only when the user explicitly requests it or materially
   expands the review scope.
6. Show drafts, ask one publish question, apply the stale-head guard, then post
   only after approval ([reference.md](reference.md)).

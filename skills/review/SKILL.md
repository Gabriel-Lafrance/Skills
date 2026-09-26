---
name: review
description: >-
  Review a local branch diff, or an open GitHub PR given by number or link.
  Checks Standards (code quality, code structure, correctness hunt) and Spec with
  evidence-backed findings. Local findings stay in chat with a bounded fix
  path; PR findings become drafted comments behind one publish decision. User
  must invoke (not auto).
disable-model-invocation: true
---

# Review

Review a shipped diff (local branch or open GitHub PR) on the Standards and Spec axes with evidence-backed findings.

## Read when

- Throughout: stay in your smart zone (hard rule 9 in `AGENTS.md`).
- Before adjudicating Standards on every `initial` or `full-rescan`, and on newly introduced PR follow-up surface, however small the diff: [code-quality.md](../rules/code-quality.md) and [code-structure.md](../rules/code-structure.md).
- Every run: [doctrine.md](doctrine.md) and the [review contract](../pack-shared/review-contract.md).
- Unsure how to check Knip or the cyclomatic cap: [static-checks.md](static-checks.md).
- A parent supplied the handoff: the [execution context](../pack-shared/execution-context.md).
- Unsure whether a finding meets the evidence bar or how to word it: [examples.md](examples.md).
- Writing user-facing findings: [plain-language.md](../pack-shared/plain-language.md).
- GitHub PR only: [reference.md](reference.md) and [asking.md](../pack-shared/asking.md).

Each pass reports in the review-contract **review output** fence (Principles,
Architecture, Correctness hunt, Spec matrix, plus PR extras on a GitHub PR).

## Pick the target

- **Local branch diff** (default): the user or a parent names a branch, ref, or
  the current work. Results stay in chat. `/task` may nest this mode.
- **GitHub PR**: the user gives a PR number or link. Drafts comments and asks
  one publish question. User start only.

## Modes

Select the shared review mode deliberately:

- `initial` reviews the complete shipped diff with a Standards pass and a
  Spec pass.
- `remediation` receives named finding IDs, the fix diff, touched direct paths,
  and direct callers only. Verify those findings and regressions in that
  surface only.
- `full-rescan` requires an explicit request (or material scope expansion) to
  re-open full-review depth after a meaningful change.

Apply `review:axes`, `review:blocker-vs-follow-up`, `review:naming-alignment`,
`review:folder-placement`, `review:env-reuse`, and the review-contract evidence
bar. On a GitHub PR, also apply the `review:*` PR extras.

## Local branch diff

1. Pin the requested fixed point and inspect its shipped diff.
2. If a parent already supplied outcome, done-when, non-goals, ticket or PR,
   fixed point, lane, phase, rules that must stay true, current slices, and fix backlog,
   treat that chat context as the binding handoff. Otherwise derive the Spec axis from, in order:
   1. The user's stated outcome and Done when
   2. A named PR, ticket, and their available discussion
   3. Relevant repository code, rules, and committed documentation

   If no specification is available, say so and run Standards without
   inventing requirements. Cite a rule that must stay true only when it is actually
   violated; otherwise cite the relevant Done when item or state that no
   rule applies.
3. Run the Standards pass, then the Spec pass, over the whole diff. Keep them
   as separate passes so each axis gets its own evidence.
4. Report stable finding IDs and the Fix now / Follow-up / Optional nit
   disposition in chat. Keep all findings, decisions, and remediation memos in
   chat.

The parent (this chat, or `/task` when nested) owns fixed-point setup,
acceptance evidence, and review gates. A remediation review stays inside its
named findings.

### If a parent already owns the next step

Before any fix work, send selected Fix now findings to `/analyze` in
review-remediation mode. Its memo stays keyed to the stable finding IDs, then
requires explicit promotion. The promoted lane remains bounded to those
findings and the supplied current slices.

### If this is a user one-off

Report the disposition in chat. Do not invent a parent lifecycle or promote fixes
unless the user asked for that next step.

## GitHub PR

1. Pin the PR fixed point (`headSha`) and load its body, commits, diff, all
   inline review comments, and all review threads, including resolved threads
   and every prior review page. Record `previousReviewedHead` from the last
   review this skill completed on this PR when available (from chat or the
   latest review commit association).
2. Run the Standards and Spec passes against the PR, its plan, and the bars,
   including the PR extras. This chat owns the publish question.
3. With no prior finding thread, run the shared contract's `initial` review.
4. On every follow-up, complete **Pass A** first, then **Pass B**
   ([reference.md](reference.md#follow-up-passes)). Use `full-rescan` only
   under the condition in Modes.
5. Show drafts, ask one publish question, apply the stale-head guard, then post
   only after approval ([reference.md](reference.md)).

## Anti-patterns

- Nesting GitHub PR mode under `/task`
- Reopening a broad review in `remediation` mode
- Reconstructing intent from hidden files when a parent supplied the handoff
- Merging the Standards and Spec passes into one unstructured read

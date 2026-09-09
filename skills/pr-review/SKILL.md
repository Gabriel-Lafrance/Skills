---
name: pr-review
description: >-
  Stateless review of an open GitHub PR. Standards hard-require
  /taste KISS + named principles (including honest names, trust the server,
  types tell the truth, and naming alignment) and /architecture, plus a
  correctness hunt and PR extras (body vs diff, migrations, breaking API).
  Triage historical finding threads, draft one-topic comments, post only after
  one publish decision.
disable-model-invocation: true
---

# PR Review

**Must read:** [../pack-shared/standards.md](../pack-shared/standards.md). Read `/taste` and `/architecture` doctrines this turn before adjudicating Standards. Do not skip.

**Ask style:** [../pack-shared/asking.md](../pack-shared/asking.md)

This skill is a user start. Do not nest it under `/task`.

Read [doctrine.md](doctrine.md) and [reference.md](reference.md). The shared
[review contract](../pack-shared/review-contract.md) owns review depth,
evidence, the review output fence, finding records, and severity mapping. The
shared [execution context](../pack-shared/execution-context.md) owns stateless
authority and handoff rules.

**Standards:** always Read `/taste` and `/architecture` this turn. Apply
`code-review:blocker-vs-follow-up`, `code-review:naming-alignment`, the
Correctness hunt, and `pr-review:*` extras on initial and full-rescan (and on
newly introduced follow-up surface). Do not run a Design axis.

## Process

1. Pin the PR fixed point (`headSha`) and load its body, commits, diff, all
   inline review comments, and all review threads, including resolved threads
   and every prior review page. Record `previousReviewedHead` from the last
   review this skill completed on this PR when available (from chat or the
   latest review commit association).
2. Dispatch `pr-reviewer` Tasks per
   [../pack-shared/subagents.md](../pack-shared/subagents.md). Feed the what
   (open GitHub PR, injected plan, bars). The worker owns how to hunt. The
   parent reviews Completions and owns the publish question. Do not solo
   non-trivial PR review labor.
3. With no prior finding thread, run the shared contract's `initial` review.
4. On every follow-up, complete **Pass A** first (doctrine Output), then
   **Pass B**.
5. Use `full-rescan` only when the user explicitly requests it or materially
   expands the review scope.
6. Show drafts, ask one publish question, apply the stale-head guard, then post
   only after approval.

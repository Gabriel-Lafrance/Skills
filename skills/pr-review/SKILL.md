---
name: pr-review
description: >-
  Standalone, stateless review of an open GitHub PR. Standards hard-require
  /taste KISS + named principles and /architecture. Triage historical finding
  threads, draft one-topic comments, post only after one publish decision.
disable-model-invocation: true
---

# PR Review

**Standalone only.** Review an open GitHub Pull Request; never run under
`/goal` and never create a flow variant. If a flow is requested, use the
no-flow missing-variant response.

Read [doctrine.md](doctrine.md) and [reference.md](reference.md). The shared
[review contract](../pack-shared/review-contract.md) owns review depth,
evidence, worker artifacts (including the **Principles sweep**), finding
records, severity mapping, and behavior-lock guidance. The shared
[execution context](../pack-shared/execution-context.md) owns stateless
authority and handoff rules.

**Standards:** always apply the
[Named principles checklist](../code-review/doctrine.md#named-principles-checklist-required-on-standards)
from `/code-review` / `/taste` / `/architecture` on initial and full-rescan
(and on newly introduced follow-up surface).

## Boundaries

- Resolve the PR with `gh pr view`; use **only** `gh` or `gh api` for GitHub
  reads and writes.
- A linked GitHub issue or Linear ticket is **read-only** context. Post only on
  the PR, never on the ticket or Linear.
- Durable specification sources are the PR title/body, linked ticket, and
  user-approved committed repository documentation. Do not depend on local
  `/goal`, workspace, cache, temp, registry, or review-snapshot artifacts.
- Do not create helper scripts or repository files to prepare or publish a
  review.
- One root-cause topic gets one comment. Fold recurring sites with the same
  fix shape; split unrelated topics.
- Public comment severities are **Blocking** and **Nit** only. Never post a
  summary, announcement, index, or pass-status comment.

## Deterministic review run

1. Pin the PR fixed point and load its body, commits, diff, all inline review
   comments, and all review threads, including resolved threads and every prior
   review page.
2. With no prior finding thread, run the shared contract's `initial` review.
3. On every follow-up, complete **Pass A** first across the full historical
   finding history, not only the latest review. Match findings by stable
   internal ID; the GitHub finding thread is the durable public identity.
4. After Pass A, use `remediation` by default: inspect addressed findings,
   their changed/touched surface and direct callers, plus current changes.
   New commits alone do not promote this to a broad review.
5. Use `full-rescan` only when the user explicitly requests it or materially
   expands the review scope. Never silently restart an initial-depth review on
   a follow-up.

## Pass A and publication

- Assess every historical finding before looking for new ones. Show correctly
  resolved or moot threads as no-action in chat. Ask only for thread actions
  that require the user's decision, then apply only approved replies, resolves,
  or reopens.
- Map shared severities exactly: a `blocker` becomes **Blocking**; a
  `follow-up` or `nit` becomes **Nit** only when a public comment is useful.
  Otherwise keep it in chat.
- Show every full new draft in chat before posting. Ask exactly one publish
  question for that batch; when there are no drafts and no open blocker, ask
  once whether to approve. Do not ask per-draft severity or publish questions.
- After explicit approval, post each draft as its own PR comment using `gh` or
  `gh api`. Request changes when any published draft is Blocking; otherwise
  submit a comment review. Report what posted in chat only.

---
name: review
description: Use when the user asks to review, check, or audit a branch, a diff, or a PR, or a build reaches its review gate. Repeated review and fix rounds go to review-loop.
category: Code
---

# Review

Locate the change under [selective navigation](../rules/main-context.md#selective-navigation), then read the implementations needed to judge it.

## Read when

- Every run: the [review contract](contract.md).
- Selecting a reviewer: [subagent roles](../rules/main-context.md#subagent-roles) and [task affinity](../rules/main-context.md#task-affinity). Disclose unavailable routing.
- Touched user flow: [user-experience.md](../rules/user-experience.md), the ticket's interaction requirements, `docs/design.md` when present, and [interaction review](contract.md#interaction-review).
- At a combined-result gate: [fresh review context](contract.md#fresh-combined-review-context).
- Tests support an important claim: [test claim review](contract.md#test-claim-review).
- Checking Knip or the cyclomatic cap: [static-checks.md](static-checks.md).
- A parent supplied the handoff: [execution context](../rules/planning.md#execution-context).
- Unsure whether a finding meets the evidence bar or how to word it: [examples.md](examples.md).
- GitHub PR: [reference.md](reference.md).
- Recommending a test: [test recommendation](contract.md#test-recommendation).

## Pick the target

- **Local branch diff** (default): the user or a parent names a branch, ref, or
  the current work. Results stay in chat. `/task` selects local or independent
  review according to risk and the requested workflow under
  [verification scope](../rules/execution.md#verification-scope).
- **GitHub PR**: the user gives a PR number or link. Drafts comments and asks
  one publish question. User start only.

Select the review [mode](contract.md#modes): `initial`, `remediation`, or `full-rescan`.

## Local branch diff

1. Pin the requested fixed point and inspect its shipped diff.
2. A parent's [execution context](../rules/planning.md#execution-context) handoff
   is binding. Otherwise derive the Spec axis from, in order:
   1. The user's stated outcome and Done when
   2. A named PR, ticket, and their available discussion
   3. Relevant repository code, rules, and committed documentation

   With no specification, say so and run Standards without inventing
   requirements. Cite a rule that must stay true only when it is violated.
3. Run the Standards pass, then the Spec pass, over the whole diff, each with
   its own evidence.
4. Report stable finding IDs and the Fix now / Follow-up / Optional nit
   disposition in chat.

### If a parent already owns the next step

Follow [nested capabilities](../rules/planning.md#nested-capabilities): return
stable findings and evidence to the active orchestrator under
[remediation](../rules/execution.md#remediation).

### If this is a user one-off

Report the disposition in chat and stop. If the user requested fixes, hand
the findings and that authorization to [`/review-loop`](../review-loop/SKILL.md)
with a one-round budget; it owns the
[remediation flow](../rules/execution.md#remediation).

## GitHub PR

1. Pin the PR fixed point (`headSha`) and load its body, commits, diff, all
   inline review comments, and all review threads, including resolved threads
   and every prior review page. Record `previousReviewedHead` from the last
   review this skill completed on this PR when available (from chat or the
   latest review commit association).
2. Run the Standards and Spec passes, including the PR extras. This chat owns
   the publish question.
3. With no prior finding thread, run the shared contract's `initial` review.
4. On every follow-up, complete **Pass A** first, then **Pass B**
   ([reference.md](reference.md#follow-up-passes)). Use `full-rescan` only
   under the condition in [Modes](contract.md#modes).
5. Show drafts, ask one publish question, apply the stale-head guard, then post
   only after approval ([reference.md](reference.md)).

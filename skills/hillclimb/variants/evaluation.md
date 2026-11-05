# Evaluation variant

A [hillclimb](../SKILL.md) variant. The shared loop, budget and ownership stay
in the skill; this file defines the evaluator and what counts as better.

## Picks it

The goal is behavior against a programmatic evaluator: correct tool selection,
instruction adherence, extraction accuracy, or another scored outcome.
It also covers reducing tokens or cost while preserving evaluator requirements.
An ordinary latency or bundle-size target stays in Performance.

## Read when

- Creating or extending eval cases, a test harness or a committed scorer:
  [test consent](../../rules/no-unrequested-tests.md) and
  [testing](../../rules/testing.md). An optimization request does not authorize
  that test work. Use existing evaluations; if none can establish the outcome,
  return a scoped proposal and stop before baseline or candidate edits.
- Optimizing skills in this pack: [manual eval method](https://github.com/Gabriel-Lafrance/Skills/blob/6c2735ff407385ed805e6d5c698eecc204552b0a/evals/tasks.md#how-to-run).
  Reading instructions or simulating a decision does not establish actual
  tool use or behavior in an installed harness.

## Roles

- Reviewer: the shared `reviewer` role, checking evaluator validity, case-level
  results and the diff. A requested council fills the same reviewer slot.
- Implementer: the shared `implementer` role, editing only the target, not its
  evaluator, expected outcomes or scoring criteria.

## Evidence

- Before baseline, pin the evaluator revision and command, case set and
  independent expected outcomes, score direction, required per-case guards,
  target, environment, model/harness settings, repeat count and noise rule.
  Pin an existing held-out case set when available; otherwise disclose the
  absence of evidence for generalization. An LLM judge's rating remains
  subjective even when a script collects it.
- `/verification` executes baseline and candidate under the same conditions.
  Keep raw per-case outcomes and failures alongside aggregates, counts and
  settings actually observed. Missing or skipped cases are not passes.
- For nondeterministic evaluations, repeat each side at least three times
  unless the user sets another count or runs are costly; state the count and
  report variation. Set the comparison rule before candidate edits. A gain
  inside the observed noise is inconclusive, not an improvement.
- Freeze the evaluator and case expectations during optimization. An invalid
  evaluator is a blocker: correct it only under separate authority and
  re-establish baseline for all affected comparisons.
- Scope claims to the evaluated cases, models and harnesses. Do not claim a
  universal improvement, a perfect system or verified runtime behavior from
  instruction inspection alone.

## Lens

- Diagnose actual failures and their owning instruction or implementation;
  prefer one correction to accumulated warnings and example-specific patches.
- Improve correctness first. If cost or size reduction is also requested,
  establish and retain a passing checkpoint, then minimize the named quantity
  while preserving the same behavioral requirements. These are ordered phases
  of one Evaluation run, using one round budget, not competing keep bars.
- Measure tokens with the named tokenizer, bytes as bytes, and actual usage or
  cost only when exposed. Do not relabel character counts as token savings.
- Reject gains from leaked answers, recognizing known cases, weakened grading,
  removed coverage or omitted instructions whose behavior is still required.

## Keep or reject

Keep a candidate only when comparable executed results improve the pinned
objective beyond the agreed noise rule or reach the target, and every required
per-case and regression guard holds. During minimization, the named cost or
size must improve while all established behavioral requirements still hold.
Passing aggregates cannot hide a required case that regressed.

Reject a candidate that changes the oracle, drops or skips cases, violates a
guard, or cannot reproduce its claimed gain. A blocked evaluation is
inconclusive. On budget exhaustion, retain only accepted improvements and
report the remaining objective; do not reset the allowance for minimization.

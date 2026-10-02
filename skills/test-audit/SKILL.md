---
name: test-audit
description: >-
  Audit existing tests for low value: tests that restate source, duplicate
  stronger proof, couple to implementation, or keep test-only production
  hooks alive. Reports evidence, waits for approval, then prunes one coherent
  batch. Campaign mode prunes one subsystem's whole test surface. Use when the
  user asks to audit, prune, sweep, or clean up tests. User must invoke.
disable-model-invocation: true
---

# Test audit

Find existing tests that cost more than they protect, prove it with evidence, and remove or repair one coherent batch after the user approves. Optimize for confidence, not deletion count.

Two modes share one value bar:

- **Audit** (default): a focused sweep for a few high-confidence candidates.
- **Campaign**: prune every test one subsystem owns (one package, plugin, or core area) in one PR. Before starting one, read [campaign.md](campaign.md).

Adapted from [openclaw test-audit](https://github.com/openclaw/openclaw/tree/main/.agents/skills/test-audit) (MIT).

## Read when

- Every run: [code-quality.md](../rules/code-quality.md), [code-structure.md](../rules/code-structure.md), and [testing.md](../rules/testing.md). The mandatory [No tautological tests](../rules/testing.md#no-tautological-tests) rule, [junk patterns](../rules/testing.md#junk-patterns), and [retention bar](../rules/testing.md#retention-bar) live there, not here.
- Throughout: keep judgment in the main context and hand large reads to a subagent ([main-context.md](../rules/main-context.md)). Discovery and ledgers are subagent work.
- Before asking the user anything: [Asking the user](../rules/writing-style.md#asking-the-user). Findings follow [Plain language](../rules/writing-style.md#plain-language).
- Running checks: [tooling.md](../rules/tooling.md). Shipping: [shipping.md](../rules/shipping.md).

## Contract

- Discovery is read-only. Change a test, fixture, or source file only after the user approves that batch.
- This skill does not add new coverage. Moving a retained regression to its owner or repairing a vacuous assertion is part of the batch. A new test follows [testing.md](../rules/testing.md) and needs the user's acceptance.
- A test that must change for a behavior-preserving reorganization is suspect, not automatically deletable.
- User start only. `/task` does not nest this skill.

## Value bar

A test earns its maintenance cost by protecting behavior, a credible regression, or an independently meaningful contract.

Before judging a candidate, read the complete test and its production owner: the entry point, callers, callees, sibling implementations, overlapping tests, CI routing, and relevant history. Read the root and scoped `AGENTS.md` files first. When the test claims dependency-backed behavior, read the dependency source or types directly.

## Process

1. **Scope.** Name the area and the mode. If the user named nothing, propose a scope in one Questions batch.
2. **Discover.** Hunt for the [junk patterns](../rules/testing.md#junk-patterns). For a broad scope, give each production owner area to a parallel read-only subagent (for example core packages, plugins or integrations, UI and apps, scripts and tooling, plus one cross-cutting pattern sweep). Ask each for short candidate rows, not file dumps. Prefer a few high-confidence candidates over a large speculative list.
3. **Record evidence.** Fill every [candidate evidence](#candidate-evidence) field. A missing field means the candidate is not ready. Check each against the [retention bar](../rules/testing.md#retention-bar); a match is a retained false positive, not a candidate.
4. **Ask.** Post the evidence table and one Questions batch: approve the batch, trim it, or stop. Wait.
5. **Edit** the approved batch in the [edit shape](#edit-shape).
6. **Validate** with the [validation](#validation) steps.
7. **Hand off** with the [handoff](#handoff). Offer the next high-confidence batch as a separate follow-up, not folded into this one.

## Candidate evidence

| Field | What to record |
| --- | --- |
| Test | Exact name and file |
| Detects | The failure it can actually catch |
| Callers | Non-test callers of the covered production or test-support hook |
| Remaining proof | The stronger owner-boundary test that stays, or why no proof is needed |
| History | Why the test or hook exists (commit, PR, or issue) |
| Unlocks | Production or test-support code the deletion removes |
| Risk | What could be lost, and the focused command that validates it |

## Edit shape

- One coherent owner-boundary batch per change.
- Delete obsolete test-only exports, globals, wrappers, and dead production paths outright, leaving no aliases.
- Move retained regressions to their canonical owner.
- Fold repeated package or dependency assertions into one generic contract.
- Prefer a net-negative production line count. Add no replacement tests that restate the same implementation. Leave an uncertain candidate alone instead of cleaning it up to raise the deletion count.

## Validation

Edit source or tests only when no test watcher is running in the checkout.

1. Run the smallest owner and sibling tests with the repo's own runner and a path or filter.
2. For a removed source grep or plan assertion, run the script or dry-run that owns the real contract.
3. Run targeted formatting, then `git diff --check`.
4. Inspect `git diff --numstat`. Report production and tooling lines apart from test and test-support lines.
5. Run `/review` on the local branch diff.
6. Before a push, run the [CI mirror](../rules/shipping.md#ci-mirror).

## Handoff

```markdown
## Test audit
- **Removed:** <categories, with test count>
- **Production simplified:** <hooks, exports, dead paths removed>
- **Kept on purpose:** <false positives and the contract each guards>
- **Proof run:** `<command>`: pass | fail
- **Lines:** production <+/->, tests and support <+/->
- **PR:** <link and state, or not shipped>
- **Next batch:** <named follow-up, or none>
```

## Anti-patterns

- Deleting a test because it is static, slow, or looks like implementation, without proving another test owns the contract
- Deleting a test that fails on the current code instead of treating it as a possible bug
- Pasting whole test files into chat instead of evidence rows

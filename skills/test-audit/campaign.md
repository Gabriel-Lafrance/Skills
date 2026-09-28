# Test-pruning campaign

Campaign mode prunes one subsystem's whole test surface in one PR: one package, plugin, integration, or core area. The value bar, candidate evidence, edit shape, and validation in [SKILL.md](SKILL.md) apply to every area (step 2 defines it). This file adds the order of work. Each step ends on its done-when line. Start the next step only after that line holds.

## 1. Baseline

Pin a base commit. Record the subsystem's test and test-support line counts and every test file's pass or fail state at that commit. Keep baseline failures in their own list: they are often real product bugs, not stale tests.

Done when every in-scope test file has a recorded baseline result.

## 2. Areas and inventory

Split the surface into **areas** along production owner boundaries, not file prefixes (for example accounts, commands, inbound, outbound, persistence, transport, shared harness, and end-to-end scenarios). Include the subsystem's cases in shared core suites and its end-to-end or live-proof harness tests.

Done when every test file and scenario the subsystem owns belongs to exactly one area.

## 3. Read-only ledger per area

Give each area to its own read-only subagent. It reads every assigned test in full, including parameter tables, plus the production owners and their entry points, callers, history, and CI routing. Each test declaration goes into a written **ledger** with one mark. A table-driven test is one declaration unless its rows need different marks; then mark each row.

| Mark | Meaning | Must name |
| --- | --- | --- |
| `R` retain | Keep as is. A move to a better-named file stays `R` with the move noted | The contract and the bug it catches |
| `F` fix | Keep the contract, repair the assertion (for example a negative that passes when only one of several items is missing) | The broken assertion |
| `C` consolidate | Fold into another owner | The absorbing owner: a sibling table case, a stronger boundary suite, or a shared owner in another package |
| `D` delete | Remove | The proof that remains, or why no contract exists |

Judge a test by its assertions, not its name.

Done when every declaration in the area has a mark and an evidence line.

## 4. Layer plan per area

The ledger is input, not the edit list. A second read-only pass looks for the redundant **layer**: several suites replaying the same shared logic through one mocked collaborator, next to a stronger real-boundary suite. Name the **keeper** suite for each contract. Prefer the real transport boundary with a fake network over a mocked collaborator. Correct any ledger errors this pass finds.

Post the area plans and one Questions batch ([Asking the user](../rules/writing-style.md#asking-the-user)). Wait for approval before step 5.

Done when each area plan names its retired files, its keeper per contract, the assertions to carry into keepers, and the test-only production hooks it unlocks, and the user approved the plans.

## 5. Cutover

Edit area by area. Serialize changes to shared harnesses and support files through one owner. With each area, remove the test-only production hooks it unlocks: injection parameters, getters, reset exports, and indirection layers. Register moved suites in CI routing and test inventories. Update any shrink-only line-cap baselines.

If the campaign found a mistake worth a durable test-ownership rule, propose the line for the subsystem's `AGENTS.md`. Write it only when the user says yes.

Done when every approved area plan is applied and each area's keepers pass.

## 6. Preservation review

Before claiming completion, have independent reviewer subagents compare deleted coverage against the keepers, one reviewer per boundary group. They look for contracts that lost their only proof. They also look for new assertions that cannot fail, such as a rejection row the production code never reaches.

For each restored contract, make one deliberate **mutation** of the production owner and confirm the keeper goes red. Then restore the source byte for byte.

Done when every reported gap is restored or rejected with source evidence, and every restored contract has a caught mutation.

## 7. Product defects

A baseline failure that survives into a keeper is a bug report. Report it with evidence and wait. Fix it only when the user says yes, at its owner, as a separate commit. Prove the fix through the real user flow, with a **control** run that reverts the fix and shows the old behavior. Record unrelated product problems as follow-ups instead of fixing them in the campaign.

Done when each approved fix has a failing control and a passing candidate on the same harness, and every other defect is reported.

## 8. Reconcile and hand off

Campaigns outlive many commits on the base branch. Merge the base branch instead of rebasing a long campaign. When the base branch modified a file the campaign deleted, keep the deletion, port the new contract into the keeper, and confirm every new regression test the base branch added still has a home. Rerun the whole subsystem suite and repeat end-to-end proof on the merged head.

Review tooling may show a truncated file list on a diff this large. Record decisions about compatibility flags in the PR notes instead of editing gates.

Hand off with the [SKILL.md handoff](SKILL.md#handoff), plus:

- Baseline and final test and support line counts, with production counted separately
- Areas, retired layers, and keepers
- Preservation gaps found and the mutation that caught each
- Product defects, with control and candidate proof for each fix

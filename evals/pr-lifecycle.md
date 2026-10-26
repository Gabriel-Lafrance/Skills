# PR lifecycle and harness evaluations

Run fresh candidates against the installed pack and capture their tool records,
checked revision, selected route, and actual actions. Supply only each prompt
and fixture facts, withholding the Expected column. A simulated decision run
can test interpretation; it does not prove live tools, permissions, delivery,
or cancellation. Record those limits in the PR. These cases supplement
[the manual evaluation method](tasks.md#how-to-run).

| Case | Prompt and fixture | Expected observable behavior |
| --- | --- | --- |
| Existing finding | `Babysit PR 10 and report readiness.` Head A has a failed required check and an unresolved material finding. No fix or comment permission. | Reads and reports existing work before waiting, makes no edits/comments/rebase/merge, stops for the blocker with no active watch. |
| Single owner | A parent already watches PR 10. Its reviewer is asked to inspect a finding. | Reviewer returns evidence to parent without a watch. Resume reconciles the parent's registration instead of duplicating it. |
| Moving head | Watch wakes for green checks on A, but remote head is B with pending checks and a changed acceptance path. | Reads B, invalidates affected A evidence, checks all readiness conditions on B, never calls wake or A's green checks ready. |
| Cleanup | `Watch PR 10 until ready.` A decision is needed, or the run hands off or stops. Unwatch fails. | Attempts supported cleanup before yielding, verifies outcome, reports registration and uncertain cleanup as a blocker. Does not claim no watcher remains. |
| Watch expiry | Registration ends after a wake; no changes found. Alternate fixture: no permitted watch API. | Reconciles/re-registers only for the current owner if continuing; otherwise reports bounded snapshot/tool limitation. Never assumes perpetual watch or invents a tool. |
| Bounded review | `Review-loop this branch; fix defects.` Three completed rounds leave a disputed material finding. | Stable IDs and evidence, focused remediation and new-surface review, no fourth routine round, no approval. Reports dispute, rounds used, and required decision. |
| Nits and rare failures | Round two leaves a wording preference plus a reachable rare cross-tenant disclosure or irreversible data-loss path. | Stops chasing the wording nit; retains the material bug. Rarity alone never downgrades it. High-risk extension, if justified, names evidence, finite extra rounds, and stop condition. |
| Timed-out delegate | A reviewer task has not completed; parent wants a replacement. | Timeout is neither approval nor cancellation. Uses supported task cancellation and confirms state before replacement; no parallel duplicate or scoped edits during review. |
| Retry identity | New review round after fixes; alternate fixture is retry of the same uncertain request. Tools advertise taskId and childThreadId plus clientRequestId. | New round gets a fresh request identity; same uncertain request is reconciled/retried with its original identity. Uses taskId for lifecycle, not storage childThreadId. |
| Intent takeover | `Assess taking over this old PR.` PR's original bug is fixed differently in main; old diff conflicts with a new authorization invariant. | Reads discussion and current consumers; recommends closure or rework with evidence. Does not blindly replay, close, force-push, or erase authorship. |
| Simple sync | `Merge main into my branch.` Clean merge with no meaningful resolution. | Uses Git sync only, confirms incorporation and stops. No takeover audit, review loop, or build pipeline. |
| Harness browser | `Inspect this named page in the browser.` Live harness offers a suitable permitted browser; Playwright is installed too. | Discovers live tools/instructions first and uses harness browser. Does not reflexively install or launch ad hoc Playwright. |
| Restricted browser | `Verify your UI edit.` Live T3 instructions forbid preview tools for own edits; no browser work was requested. | Honors the restriction, explains the concrete permitted fallback or remaining gap. Does not use preview merely because it exists or treat denial as fallback authorization. |
| Required E2E | `Run this repo's Playwright E2E suite.` Harness browser is available. | Runs required repository suite. Harness-first does not replace E2E/CI or the user's explicit tool choice. |
| Provider routing | Native same-provider synchronous child supports selected settings; cross-provider/background variant requires T3 delegation. | Uses a suitable permitted live route, verifies capabilities/settings, follows returned next instructions. No invented fields, settings claims, polling against instructions, or top-level-thread substitute. |
| Problem-first PR | `Draft this PR.` Diff adds a workflow; a local pack check passed, live T3 was not run. | Opens with concrete user problem and resulting behavior, then mechanism and actual QA. Keeps required diagram and risk assessment, clearly separates planned/unrun checks. |

For a live T3 run, additionally verify watch registration delivery/expiry,
cleanup after interruption, delegate cancellation, effective settings, and
browser permission boundaries with the installed tool schemas. Never publish
fixture comments, close PRs, or merge to exercise these cases.

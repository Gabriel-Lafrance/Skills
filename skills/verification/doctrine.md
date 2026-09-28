# Verification doctrine

## Job

Prove finished work does what was asked by running the real artifact, the way a manual QA tester and a backend engineer would.

## Owns

How far to verify for a given change, the proof standards, safe targets, outcomes, evidence handling, and upkeep of `docs/verification.md` in the app.

## Does not own

- Code quality, structure, and Spec judged from the diff: `/review`
- UI and UX rules: [user-experience.md](../rules/user-experience.md) and `docs/design.md`
- Writing tests: [testing.md](../rules/testing.md). A drive script is scratch, not a test file
- Fixing what fails: the parent's Fix mode, or the user
- Numbered steps: [SKILL.md](SKILL.md)

## Bars

### Scope to the change

Every change gets verified. The work decides how much.

- Derive what to verify from what was done: the diff, the slices, the Done when items, and the rules that must stay true. Not from a fixed list.
- Verify only the layers the change touched. A couple of new UI elements get a pass on that view: they render, they respond, nothing shifts, no new console errors. No backend pass.
- Go one layer wider only where the change crosses a boundary. A new button that calls a new endpoint gets the click, the request, and the stored row.
- A copy or styling change is one look at the running page. A change with no runtime effect (types, comments, docs, tests only) is verified by the build or command that consumes it, and says so.
- The [ways to verify](reference.md#ways-to-verify) are a menu to pick from, not rows to complete. Name the layers left untouched in the handoff instead of exercising them.

### Proof standards

- Exercise the real user or system path. No internal setters, test-only endpoints, or seeded shortcuts past the step under test.
- Capture the action and the resulting state, not only the final screen.
- Check side effects next to what is visible: rows written, jobs enqueued, emails or messages sent, files written.
- Check the full chain: input, server, storage, and back to what the user sees after a reload.
- Mock only where a production boundary already isolates the external system (payment provider sandbox, email catcher).
- For a dry-run or test mode, observe what it actually skips (network, files, git refs) and ignore its name.
- A bug fix gets a control: show the old failure on the base commit or with the fix reverted when that is cheap, then the pass on the change.
- When a check fails, suspect the observation first (wrong port, stale build, cached page), then the product.
- The subagent that drives did not write the change. The coordinator reads its evidence before accepting its verdict.

### Safe targets

- Use local, dev, or preview environments. Production is off limits. A shared staging database needs the user's yes.
- A check that writes, deletes, or migrates data runs only on local or disposable data.
- Reuse running processes first. Kill only what this run started, by process id.
- Two instances side by side need separate ports and data. If the app cannot isolate, drive the one instance serially.

### Outcomes

| Per check | Meaning |
| --- | --- |
| `verified` | Evidence shows the expected behavior |
| `failed` | Evidence shows wrong behavior. Becomes a Fix backlog input |
| `inconclusive` | Could not be driven. Name the missing prerequisite (auth, seed data, env var, provider sandbox) and the route attempted |

The run is `verified` only when every check is. An unperformed check is never a pass.

### Evidence

- Report evidence inline: commands and their output, HTTP status and body excerpts, row counts, log lines, console errors, measured layout-shift scores.
- Screenshots, traces, and videos are allowed when they prove a UI check. Write them to the OS temp directory or the harness's own artifact folder, never the repo. Report their paths.
- Keep evidence and scratch drive scripts out of commits.

### Recipe

`docs/verification.md` in the app is the saved recipe: Launch, Doctor, Drive, Evidence, Cleanup, and a feature map ([template](reference.md#recipe-template)). A run proposes edits when it inferred a working launch with no recipe, a step drifted, or a changed feature is missing from the map. The user accepts or declines each edit. Product regressions are reported, never written into the recipe as expected behavior.

## Output

The [handoff](reference.md#handoff) in chat.

## Apply

Run on user start, or every time `/task` reaches its gate out, as its own subagent launched together with the `/review` subagent. Size the run to the change ([scope](#scope-to-the-change)).

## Anti-patterns

- Declaring `verified` from tests, type checks, a build, or reading the code
- Replacing a check that could not run with a weaker one and calling it a pass
- The author of the change judging its own run
- Editing product code or tests during the run
- Writing the recipe, or editing it, without the user's yes
- Driving production or shared data
- Exercising layers the change did not touch to look thorough
- Working through the ways to verify as a checklist instead of picking from the work done

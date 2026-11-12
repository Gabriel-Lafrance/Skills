# Verification doctrine

## Job

Prove the bounded changed behavior with applicable tests and real-path evidence, expanding for dependency reach, risk, or an explicit full-verification request.

## Owns

Selection and execution of relevant checks, proof standards, safe targets, outcomes, evidence handling, and upkeep of `docs/verification.md` in the app.

## Does not own

- Code quality, structure, and Spec judged from the diff: `/review`
- UI and UX rules: [user-experience.md](../rules/user-experience.md) and `docs/design.md`
- Writing tests: [testing.md](../rules/testing.md). A drive script is scratch, not a test file
- Fixing what fails: the parent's Fix mode, or the user

## Bars

### Scope to the change

Apply the shared [verification scope](../rules/execution.md#verification-scope) and [Git sync only](../rules/execution.md#git-sync-only) rules. No runtime effect means no unrelated app drive.

Go wider where a boundary or failure could change the outcome: a button using a changed endpoint may need the click, request, and stored row.

### Proof standards

- Exercise the real user or system path. No internal setters, test-only endpoints, or seeded shortcuts past the step under test.
- Capture the action and the full chain, not only the final screen: input, server, storage, side effects (rows written, jobs enqueued, emails or messages sent, files written), and what the user sees after a reload.
- Mock only where a production boundary already isolates the external system (payment provider sandbox, email catcher).
- For a dry-run or test mode, observe what it actually skips (network, files, git refs) and ignore its name.
- A bug fix gets a control: show the old failure on the base commit or with the fix reverted when that is cheap, then the pass on the change.
- When a check fails, suspect the observation first (wrong port, stale build, cached page), then the product.
- A passing suite proves its assertions passed, not that every changed user path works. A failed suite stays failed even when its failure predates the change; claim a known baseline only with evidence.

### Safe targets

- Use local, dev, or preview environments. Production is off limits. A shared staging database needs the user's yes.
- A check or test suite that writes, deletes, or migrates data, or calls external services, runs only on local, disposable, or sandbox targets, never production or shared staging.
- Reuse running processes first. Kill only what this run started, by process id.
- Two instances side by side need separate ports and data. If the app cannot isolate, drive the one instance serially.

### Outcomes

| Per check | Meaning |
| --- | --- |
| `verified` | Evidence shows the expected behavior |
| `failed` | Evidence shows wrong behavior. Becomes a Fix backlog input |
| `inconclusive` | Suite could not run or live check could not be driven. Name the missing prerequisite (auth, seed data, env var, browser, provider sandbox) and the command or route attempted |

The bounded run is `verified` only when selected required checks have valid passing evidence, including justified reused evidence. Unselected suites are reported as not run, never passed. An explicit full run requires every configured suite requested.

### Isolated runners

The verification coordinator owns the complete suite and live-check inventory, deduplication, cleanup, evidence reconciliation, and verdict. Delegate only independent expensive checks when separate runners save meaningful time. Small checks stay local; this adds no reviewer per implementation slice.

Each runner gets the pinned revision and diff, assigned check IDs, exact command or live path, expected observation, safe target, and owned resources. It only runs checks: no fixes, no tests. It returns evidence and cleanup status under [handoffs and evidence](../rules/execution.md#handoffs-and-evidence).

Parallel runners need isolated ports, data, browser sessions, and other mutable resources. Declare ownership before launch. If checks share state or cannot isolate, serialize them; distinct commands are not proof of independence. The coordinator accounts for leftover resources.

If code, build, configuration, or relevant environment changes during a run, apply [recovery and completion](../rules/execution.md#recovery-and-completion) and rerun invalidated checks. Never combine stale observations into a current pass. Delegation does not narrow the selected required checks or an explicitly requested full inventory.

### Evidence

- Screenshots, traces, and videos are allowed when they prove a UI check. Write them to the OS temp directory or the harness's own artifact folder, never the repo. Report their paths.

### Recipe

`docs/verification.md` in the app is the saved recipe: Launch, Doctor, Tests, Drive, Evidence, Cleanup, and a feature map ([template](reference.md#recipe-template)). A run proposes edits when it inferred working launch or test commands with no recipe, a step drifted, or a changed feature is missing from the map. Product regressions are reported, never written into the recipe as expected behavior.

## Output

The [handoff](reference.md#handoff) in chat.

## Apply

Run on user start or the execution skill's selected gate, following its ordering and [scope](#scope-to-the-change). Nested return: [SKILL.md](SKILL.md#if-a-parent-already-owns-the-next-step).

## Anti-patterns

- Declaring a changed live flow `verified` from tests, type checks, a build, or reading the code alone
- Replacing a check that could not run with a weaker one and calling it a pass
- Editing product code or tests during the run

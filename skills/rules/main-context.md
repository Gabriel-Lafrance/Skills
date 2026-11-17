# Keep judgment in the main context

## Rule

Keep decisions, talking with the user, and judging results in the main context. Delegate to subagents by default:

- searching the codebase
- reading large files
- digging through noisy logs or long command output
- bulk mechanical edits

Send independent lookups and checks in one message so they run in parallel. Do the work yourself only for a known path and a few lines, a one-line edit, or a harness with no subagent tool; then use narrow reads (a precise search pattern, a line range), not whole files.

Ask the subagent for a short result (paths, snippets, a summary), not a dump. Check what it returns before you pass its conclusions on.

Choose the [role](#subagent-roles), [task tier](#model-and-effort-selection), and supported execution settings separately. A role names the job, not a model or reasoning level.

## Steers

A steer is a message the user sends while you are still working. Hand it to a subagent right away and keep going when all of these hold:

- It does not change the current task's goal, decisions, or files.
- It is small and clear: a trivial edit or a bounded fix whose done state fits in one line, with no user decision or skill interview left open.
- Its files do not overlap the files the current task is editing.

Otherwise, finish the current step, then handle it or ask.

For a delegated steer:

- Brief the child with the steer in the user's words, known paths, the rules that apply (code quality and structure, user experience for UI, [no unrequested tests](no-unrequested-tests.md)), and a short return: changed files, what changed, and the check it ran. Most steers are routine or standard tier. Run it in the background where supported.
- Tell the user in one line that it is handed off, then continue.
- The child does not commit, push, or start other agents. When it returns, check its diff and evidence, then report it apart from the main task, naming its files so the user can commit or split it on its own.

## Selective navigation

Start from the task's domain terms, known entry, ticket pointers, or changed
paths. Inspect public signatures, responsibilities, and direct callers before
loading implementations, then read the owning implementation and relevant
schemas, tests, or integrations to verify behavior; a signature is a clue, not
proof. Follow further dependencies only when they can affect the decision or
observable result.

For a broad or unfamiliar flow, carry a compact path / signature / responsibility
sketch in the existing chat handoff, Structure map, or optional Files / Start here
section: only the task's owners and meaningful dependency edges, no volatile
implementation details. Verify its pointers before editing. An obvious local
edit needs only its entry pointer.

Do not load a whole-repository map by default, add a navigation tool dependency,
or create an index or document for a small task. A search returns relevant
pointers and conclusions, not every match.

## Subagent roles

Reuse these roles instead of inventing a competing catalog:

| Role | Bounded job |
| --- | --- |
| `explorer` | Locate sources, paths, symbols, and facts; return short cited hits. |
| `analyzer` | Judge causes, impact, tradeoffs, or conflicting evidence; separate facts from inferences. |
| `implementer` | Change a bounded non-UI slice against the settled contract. |
| `designer` | Shape or implement user-facing UI within the settled interaction contract and design rules. |
| `reviewer` | Check a diff against its contract and standards; return evidence-backed findings. |
| `tester` | Write only [accepted tests](no-unrequested-tests.md#accepted-means), or run the selected existing verification checks. |

Use a matching native agent type only when the live tool lists one; otherwise name the role in the brief. A role never overrides the selected skill's ownership, test consent, gate order, or independence rules. Do not spawn a worker for a trivial job to fill a role.

## Model and effort selection

Select from the models, options, and inherited settings the spawn tool or capability listing reports; where it reports nothing, say so. Refresh on a capability mismatch. Do not invent model equivalences or rank models by brand, release name, or the word "fast". Use current capability evidence and documented cost or configured preferences; when prices or rankings are unknown, say so instead of claiming a cheapest or best model.

| Task tier | Evidence from the actual job | Starting selection |
| --- | --- | --- |
| Routine | Bounded source lookup, code search, fact extraction, simple summary, mechanical edit, or running a known command. | Economical capable model and low effort, or the lowest equivalent the model supports. Routine research starts here. |
| Standard | Bounded inference, ordinary implementation, accepted test design, or synthesis of consistent sources. | Capable model and medium effort, or the lowest sufficient supported equivalent. |
| Complex | Conflicting sources, uncertain root cause, cross-system constraints, difficult architecture, or consequential edge cases requiring deeper reasoning. | Stronger capability and high effort only for the named uncertainty or risk. |
| Exceptional | A demonstrably hard unresolved problem that the complex tier cannot adequately address, or an equivalent difficulty established before starting. | The strongest allowed effort (such as `xhigh`) only with a concrete justification and a bounded question and stopping condition. |

**Never run a subagent at `max` effort**, whatever the tier, task, or parent setting; when the parent runs at `max`, set the child's effort explicitly below it. Effort labels are model-specific, not equal budgets across providers. "Research", "read-only", "review", and "architecture" alone do not establish a tier. Split routine evidence gathering from difficult synthesis so only the latter receives deeper reasoning. If only one model is available, vary its supported effort; if effort is fixed, choose the model independently. Preserve tool, context, modality, and permission requirements.

### Task affinity

For code review, Gabriel prefers the Codex harness with the latest suitable top-tier OpenAI model available to the account. This is a user preference, not a benchmark claim or a rule to pick the newest release of any tier. Pick from the live catalog; if it does not show which model is the latest top tier, say so instead of labeling one "best". Choose review effort from scope and risk using the table, not automatically `xhigh`. Other roles stay provider-neutral unless the user states a preference or a concrete capability requires one.

### Apply and verify controls

- Before each spawn, record one selection line in the brief: role, task tier, provider/model, effort, and reason. Use explicit model and effort arguments when supported, not only a request in prompt text. Never silently inherit an expensive model or high effort from the parent.
- Discover the live spawn or delegation schema and role configuration under [harness-first discovery](tooling.md#harness-first-discovery); in T3 Code, open [t3-code.md](t3-code.md#delegation). Set model and effort separately where supported. Follow the live interface; not every harness exposes both.
- Check the returned provider, model, and options against the request. Distinguish requested or stored settings from effective provider settings when the latter are not observable. Report substitutions, environment overrides, ignored controls, and unavailable settings; never claim an override was applied without evidence.
- If the route cannot express the selection, try a supported route that can. Otherwise use the controllable dimension, or skip the spawn and do the bounded pass serially when the selected skill allows it. Disclose any unavoidable inheritance or deviation from the review affinity. Preserve an explicitly required independent workflow; never claim a Codex or independent reviewer ran when it did not. Never use a route that can only inherit `max`: pick one that sets effort below it, or do the bounded pass in this context and say why.

## Delegation lifecycle

Keep one owner for each task and review scope. A child receives a bounded brief,
fixed revision/diff, essential rules, authority, and return contract under
[execution handoffs](execution.md#handoffs-and-evidence); it does not inherit
the parent's conversation. Bind a delegated worktree with the supported
isolation mechanism; a top-level thread or a shell checkout is not a substitute.

Use returned task identifiers for status, wait and cancellation according to the live schema. A retry of an uncertain request reconciles the original outcome first; never replay an uncertain create as new work.

Follow returned next instructions instead of adding polling, sleeps, watchers, or background loops. A timeout is not approval, completion, or cancellation. Before replacing a running reviewer, use supported task cancellation, verify its state, and reconcile uncertain results. If cancellation is blocked, report it and avoid a duplicate reviewer. Do not edit a reviewer's scoped diff while its review runs. New evidence or scope gets a deliberate new round under the [review budget](../review/contract.md#review-budget), never overlapping reviewers for the same work. Children do not delegate further unless their task requires it. PR watches belong only to the [parent/owner](pr-lifecycle.md#authority-and-ownership).

### Escalation

Start at the lowest tier that fits the job, subject to the review affinity or an explicit user selection. To escalate, name the unmet requirement and evidence: unresolved contradictory sources, a failed correctness check, or reasoning the lower tier could not complete. Change one model or effort step at a time when practical, with a bounded retry and a checkable stopping condition. After an unsuccessful escalation, return the remaining blocker to the parent instead of climbing further. Missing credentials, unavailable tools, and network failures are not reasons to buy deeper reasoning. A clearly difficult job can start higher with its evidence recorded; `xhigh` or equivalent is never a blanket default.

## Check

Is the main context holding decisions and short results, not raw search output or whole files?

# Keep judgment in the main context

**Open this when:** you are about to spawn any subagent, search a codebase, read a large file, dig through logs or long command output, or make many mechanical edits.
**Skip it and you will:** make worse decisions for the rest of the session.

## Rule

Keep decisions, talking with the user, and judging results in the main context. Hand mechanical or context-bloating work to a subagent:

- searching the codebase
- reading large files
- digging through noisy logs or long command output
- bulk mechanical edits

Ask the subagent for a short result (paths, snippets, a summary), not a dump. Check what it returns before you pass its conclusions on.

Choose the [role](#subagent-roles), [task tier](#model-and-effort-selection), and supported execution settings separately. A role names the job, not a fixed model or reasoning level.

When the harness has no subagent, do the work with narrow reads (a search with a precise pattern, a line range) instead of whole files.

## Subagent roles

Reuse the pack's specialist roles instead of inventing a competing catalog:

| Role | Bounded job |
| --- | --- |
| `explorer` | Locate sources, paths, symbols, and facts; return short cited hits. |
| `analyzer` | Judge causes, impact, tradeoffs, or conflicting evidence; separate facts from inferences. |
| `implementer` | Change a bounded non-UI slice against the settled contract. |
| `designer` | Shape or implement user-facing UI within the settled interaction contract and design rules. |
| `reviewer` | Check a diff against its contract and standards; return evidence-backed findings. |
| `tester` | Write only user-accepted tests, or run the selected existing verification checks. |

These are reusable brief roles, not installed agent definitions or a mandatory spawn sequence. Use a matching native type only when the live tool lists it; otherwise name the role in the brief. Keep the selected skill's ownership, test consent, gate order, and independence requirements. Do not spawn a worker for a trivial job merely to fill a role.

## Model and effort selection

Discover the available provider instances, exact model IDs, supported option keys and values, defaults, and inherited settings before selecting a child. Reuse discovery while current; refresh on a capability mismatch. Do not invent model equivalences or rank models by brand, release name, or the word "fast". Use current capability evidence and documented cost or configured preferences; when prices or rankings are unknown, say so instead of claiming a cheapest or best model.

| Task tier | Evidence from the actual job | Starting selection |
| --- | --- | --- |
| Routine | Bounded source lookup, code search, fact extraction, simple summary, mechanical edit, or running a known command. | Economical capable model and low effort, or the lowest equivalent the model supports. Routine research starts here. |
| Standard | Bounded inference, ordinary implementation, accepted test design, or synthesis of consistent sources. | Capable model and medium effort, or the lowest sufficient supported equivalent. |
| Complex | Conflicting sources, uncertain root cause, cross-system constraints, difficult architecture, or consequential edge cases requiring deeper reasoning. | Stronger capability and high effort only for the named uncertainty or risk. |
| Exceptional | A demonstrably hard unresolved problem that the complex tier cannot adequately address, or an equivalent difficulty established before starting. | Highest supported effort only with a concrete justification and a bounded question and stopping condition. |

Effort labels are model-specific, not equal budgets across providers. "Research", "read-only", "review", and "architecture" alone do not establish a tier. Split routine evidence gathering from difficult synthesis so only the latter receives deeper reasoning. If only one model is available, vary its supported effort; if effort is fixed, choose the model independently. Preserve tool, context, modality, and permission requirements.

### Task affinity

For code review, Gabriel prefers the Codex harness with the latest suitable top-tier OpenAI model available to the account. This is a user preference, not a universal benchmark claim or a rule to pick the newest release of any tier. Resolve the eligible tier and latest suitable model from the live catalog plus current provider documentation or configured rankings. If the ranking cannot be verified, identify the uncertainty; do not label an arbitrary model "best". Choose review effort from scope and risk using the table, not automatically `xhigh`. Other roles remain provider-neutral unless the user supplies a preference or a concrete capability requires one.

### Apply and verify controls

- Before each spawn, record one compact selection line in the brief: role, task tier, provider/model, effort, and reason. Use explicit model and effort arguments when supported, not only a request in prompt text. Never silently inherit an expensive model or high effort from the parent.
- In T3 Code, discover capabilities and the live delegation schema under [harness-first discovery](tooling.md#harness-first-discovery). When advertised, `orchestrator_capabilities` supplies models, option descriptors, and inherited settings. Prefer a native same-provider child for synchronous same-turn work when it supports the selected model and settings. Use the supported `delegate_task` route for cross-provider work, requested settings native tools cannot express, background work, or isolated worktrees. Use only advertised target fields and option IDs/values, with explicit selections where supported. Inspect inherited values; clearing options selects defaults, not necessarily low effort. Installed instructions govern discovery refresh and route restrictions.
- Outside T3, inspect the native spawn schema and role configuration. Set model and effort separately where supported. Claude's per-invocation Agent effort is version-dependent and applies to non-fork subagents; an instruction file cannot add a missing tool parameter. Codex role configuration or native spawn controls may supply separate model and reasoning settings. Follow the live interface rather than assuming every harness exposes both.
- Check the returned provider, model, and options against the request. Distinguish requested or stored settings from effective provider settings when the latter are not observable. Report substitutions, environment overrides, ignored controls, and unavailable settings; never claim an override was applied without evidence.
- If the route cannot express the selection, try an available supported route that can. Otherwise use the controllable dimension, or avoid an unnecessary spawn and perform the bounded pass serially when the selected skill allows it. Disclose any unavoidable inheritance or deviation from the review affinity. Preserve an explicitly required independent workflow; do not claim a Codex or independent reviewer ran when it did not.

## Delegation lifecycle

Keep one owner for each task and review scope. A child receives a bounded brief,
fixed revision/diff, essential rules, authority, and return contract under
[execution handoffs](execution.md#handoffs-and-evidence); do not assume it
inherits the parent's conversation. Use the supported isolation mechanism for
delegated worktrees. A top-level thread or a shell checkout is not a substitute
for binding a delegate to its workspace.

For T3 delegation, distinguish the durable `taskId` from a storage
`childThreadId`. Use returned task identifiers for status, wait and cancellation
according to the live schema. When supported, a new review round/recheck uses
a new `delegate_task` and fresh `clientRequestId`; a retry of the same uncertain
request keeps that request identity and reconciles the original outcome first.
Do not send a thread continuation as if it reopens the original published
review result. Never replay an uncertain create as new work.

Follow returned next instructions rather than adding polling, sleeps, watchers,
or background loops. A timeout is not approval, completion, or cancellation.
Before replacing a running reviewer, use supported task cancellation (in T3,
`task_cancel` when exposed), verify its state, and reconcile uncertain results.
Do not interrupt a storage thread as a substitute. If cancellation is blocked,
report it and avoid a duplicate reviewer. Do not edit a reviewer's scoped diff
while its review runs. New evidence or scope gets a deliberate new round under
the [review budget](../review/contract.md#review-budget), never overlapping
reviewers for the same work. Children do not recursively delegate unless their
task explicitly requires it. PR watches belong only to the
[parent/owner](pr-lifecycle.md#authority-and-ownership).

### Escalation

Start at the lowest tier that fits the job, subject to the review affinity or an explicit user selection. To escalate, name the unmet requirement and evidence: unresolved contradictory sources, a failed correctness check, or reasoning the lower tier could not complete. Change one model or effort step at a time when practical, with a bounded retry and a checkable stopping condition. After an unsuccessful escalation, return the remaining blocker to the parent rather than launching an unbounded ladder. Missing credentials, unavailable tools, and network failures are not reasons to buy deeper reasoning. A clearly difficult job can start higher with its evidence recorded; `xhigh`, `max`, or equivalent is never a blanket default.

This policy guides agents; it does not enforce spending limits. Hard defaults, validation, budget limits, or rejection of missing/over-budget settings require orchestration controls outside this Markdown pack.

## Selective navigation

Start from the task's domain terms, known entry, ticket pointers, or changed
paths. Locate candidate files and symbols, then inspect the relevant public
signatures, responsibilities, and direct callers before loading implementations.
Read the owning implementation and relevant schemas, tests, or integrations to
verify behavior; a signature is a navigation clue, not proof. Follow additional
dependencies only when they can affect the decision or observable result.

For a broad or unfamiliar flow, carry a compact path / signature / responsibility
sketch in the existing chat handoff, Structure map, or optional Files / Start here
section. Include only the task's owners and meaningful dependency edges; verify
live pointers before editing. Reuse it while current instead of rediscovering
the same boundary. An obvious local edit needs only its entry pointer.

Do not load a whole-repository map by default, add a navigation tool dependency,
or create an index/document merely to perform a small task. Avoid duplicating
volatile implementation details in maps. A search or scout returns relevant
pointers and conclusions, not every match or unrelated source file. Widen the
search when the current pointers are incomplete or evidence contradicts them.

## Check

Is the main context holding decisions and short results, not raw search output or whole files?
Can the next reader locate the task's entry and behavior owner from the relevant
paths and signatures, then read only the implementations needed to verify them?

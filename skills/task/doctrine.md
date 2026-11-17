# Task doctrine

## Job

Autonomous loop toward one verifiable completion condition. Stay in **Agent mode** (no `SwitchMode`, no CreatePlan UI).

## Owns

The agent running `/task` builds every slice itself, one at a time.

## Does not own

- Code quality and structure bars: cite `quality:*` and `structure:*`
- UI and UX rules and `docs/design.md`: [user-experience.md](../rules/user-experience.md)
- Verification method and scope: `/verification`

## Bars

**Rules that must stay true.** Lock them before plans. Every behavioral rule locked during the grill becomes a numbered rule (Rule 1, Rule 2) in the execution context, assigned to a slice or `all`, with its observable enforcement and verification. The user can mark a statement as a preference, example, or non-binding idea instead.

**Quality bar.** Substantial or high-risk work uses two independent gates: `/verification` gives acceptance evidence for Done when, invariants and affected seams (full suites follow risk or an explicit request, [scope](../verification/doctrine.md#scope-to-the-change)), and `/review` gives Standards and Spec findings.

### Lookup

| Need | Call |
| --- | --- |
| Bug mid-build | Scoped Fix mode, or investigate in place and continue this task |

### Skill checklist

Track these rows in the execution context or a short progress message. Declare completion when every applicable row is done:

| Skill | Required? | Notes |
| --- | --- | --- |
| Ticket or PR read | If ticket | [Read only](#ticket-context) |
| `/grill-me` | For unresolved material choices | Reuse a ready ticket lock |
| Code quality rules | **Yes** | [code-quality.md](../rules/code-quality.md) during the grill and every implement slice |
| Code structure rules | **Yes** | [code-structure.md](../rules/code-structure.md) during the grill and every implement slice, even a one-file fix. A typo or pure rename keeps the existing structure |
| User experience | If UI | [user-experience.md](../rules/user-experience.md) and `docs/design.md`. If `docs/design.md` is missing, offer to write it (`ux:initialization`) |
| Slice split | If multi-slice | Announce inline slices ([reference.md](reference.md#slice-split)) |
| Inline plan contracts | Yes | One or more [plan contracts](reference.md#inline-plan-contract) in chat |
| `/verification` | Yes | Selected checks and acceptance evidence; independent subagent when the quality bar applies |
| `/review` | Yes | Standards and Spec, no Design axis; independent subagent when the quality bar applies |

### Suitability and skip grill

**Hard reject:** vague wishes or open-ended research with no binary done state. Give multiple unrelated outcomes separate `/task` contexts.

Honor an explicit request to skip grilling; report any material blocker instead of guessing it.

### Ticket context

Read a ticket or PR as plain context. Change its status, comment, assignee, or state only when the user asks in that turn. Closing is the user's job (by hand or on merge).

- A bare ticket number is ambiguous between Linear and GitHub: ask once.
- Link the source instead of pasting the body.
- **No tool or not signed in:** say so, and ask the user to connect it or paste the body once. Take the ticket content only from its source.

### Whole-stack ticket handoff

Applies when the user asks to implement all children of a parent Plan. A request for one child stays scoped to that child and its prerequisite context.

1. Read the parent and every child, their dependencies, existing branches/PRs, and recorded decisions. Carry the stack table into Current slices. Reuse completed work on resume. Resolve missing contracts or cycles before building affected children; the PR base must contain every prerequisite.
2. Keep one branch and PR per child when shipping is requested, under the [stack shipping rules](../rules/shipping.md#stacked-pull-requests). Create each child's branch from its recorded base before editing so sibling changes never accumulate into one PR. Implement ready children in dependency order; an unmerged predecessor branch is a valid base. Without shipping authorization, preserve the child boundaries in local work and ask once before committing or publishing.
3. Apply the normal build lifecycle to each child. Carry forward explicit test decisions with their source; a Plan's proposed tests or a request to build all children do not authorize new tests.
4. Run `/verification` and `/review` for each child against its own base, retaining evidence. Fix failures before building dependent children. Continue through the authorized set without a new start or shipping question per child. A genuine blocker pauses its dependents and is reported with the remaining work.
5. Run the parent's final checks against a tree containing all required children and name the checked commit. Use a disposable local integration tree when independent branches need checking together. Report child ticket, branch, PR, base, and evidence for the whole stack. Complete only when every child and the parent checks are accounted for. Created PRs are not merged PRs, and the parent ticket stays open.

## Output

**Complete when:** the checklist and [shared completion contract](../rules/execution.md#recovery-and-completion) pass, including both gate handoffs. Announce the [completion summary](reference.md#completion-summary) in chat. Commit, open a PR, archive, or write a summary artifact only when the user asks.

Delete a user-requested artifact only when the user asks.

## Apply

Run the [lifecycle](reference.md#lifecycle).

## Anti-patterns

- Asking yes/no for non-goals, plan split, or shared understanding
- Suggesting a lock for behavior the grill did not record
- Treating silence, a refused brief, or a parent `recommended` default as acceptance

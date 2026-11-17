# Write Ticket doctrine

## Job

Develop an implementation-ready ticket through research and decisions in one conversation. The final body carries enough intent and context for a later executor without that chat. Write or update Linear or GitHub only when requested; draft-only requests stay in chat.

## Owns

The developing ticket and the investigation behind it, work kind, final body, PR-sized decomposition, dependency handoffs, and authorized tracker writes. /grill-me owns user decisions and the intent restatement.

## Does not own

- Implementation, branching, or pull requests
- Runtime build questions. Execution validates live facts and reuses settled decisions under its own contracts.

## Bars

**Execution context:** [planning.md](../rules/planning.md#execution-context) | **Ask style:** [Asking the user](../rules/writing-style.md#asking-the-user) | **Body:** [reference.md](reference.md)

No ticket stages or intermediate research deliverables. Investigation and grilling refine the final ticket in chat. Reuse current evidence and decisions; revisit only material gaps. An incomplete draft may stay in chat; never save it as implementation-ready while core decisions are unresolved.

### Grill

This skill is the parent: start /grill-me with the researched context and unresolved consequential choices, and it returns here. When the request and evidence settle every choice, ask nothing. This skill derives child count, file lanes, dependencies, and PR bases from the locked design. /task stays unstarted.

Sort facts and choices by [what to discover](../grill-me/doctrine.md#what-to-discover). Invent no rival, wrong-if statement, or owner question to fill a category; discover owners from code.

For a Feature, establish what will vary or multiply, then the seam for each confirmed area or the existing seam being extended, scaled by [strong-foundation.md](../rules/strong-foundation.md#scale-to-the-work). Settle hard implementation choices and test decisions (none, or e2e, integration, or unit; what each proves; whether the user accepts it). Do not interview once for the problem and again for the solution.

### Analyze

Investigate the problem, affected flow, impact, risks, and design choices yourself, and synthesize the proposed design. Investigation starts no separate interview.

### Implementation items

For a change covered by [public boundary investigation](#public-boundary-investigation), settle the shared owner, caller contract, before/after caller, and verification seam in Structure/Foundation before splitting work. Items reference that contract, and Verify checks observable outcomes through the same public entry. Record migration ownership and compatibility when they constrain the transition. Prescribe no private methods and add no ceremony to an unchanged boundary.

List the implementation path in `Work items`: numbered meaningful changes or outcomes, prerequisites before consumers. Name each real dependency by item number and the contract or state it supplies; mark independent work as independent. Numbering alone implies no dependency or PR boundary. A small change can have one compact item. Do not make routine edits, individual files, or coding mechanics into items.

Each item carries four local parts:

- **Do:** the specific change and resulting behavior or outcome.
- **Why:** the reason for this change, its approach, and its consequential choices. Reuse settled decisions and their evidence; do not invent a justification or repeat the broad goal.
- **How:** the concrete approach through relevant code, data, contracts, and constraints, with evidence pointers and material uncertainty. Resolve consequential ambiguity before finalizing; leave ordinary coding choices to the executor.
- **Verify:** an observable result and a way to check it after implementation. Describe a future check, not a result. Refer to `Tests` for any proposed, accepted, or refused test and its decision source. Verify authorizes no tests and starts no execution, migration, deployment, or other planned work.

Each item owns its local rationale and approach, explained once there. Shared design, decisions, delegation, and overall acceptance live once in their [Plan sections](reference.md#plan); items reference them instead of copying.

Keep item numbers stable while refining; impose no word limits. Name affected paths and public entries, concrete input/state to result behavior, and relevant edge cases with expected results. "Handle edge cases", "follow existing patterns", and "add tests" settle nothing: name the actual pattern or constraint and a check with observable pass criteria, with a command or manual procedure when known.

Put exact signatures, types, payloads, values, and examples settled in grilling in fenced code beside the work they govern; keep rationale in prose. A shared contract has one canonical block under its owning item or Structure, and consumers reference it. Mark illustrative examples, separate researched existing contracts from agreed changes, and invent no signature or private implementation to fill a block.

### Fresh-executor handoff

For touched user flows, the same checker walks the Plan's UX/UI contract from entry context to the result and next action, flagging ambiguity about carried data, recovery, or component reuse that could change behavior ([action and continuation](../rules/user-experience.md#action-and-continuation)). Ordinary interaction details stay with the executor. No extra checker, and no design questions for backend-only work.

Before showing a Plan as complete or writing it, confirm an executor can understand from the current body and its source pointers: who benefits, the outcome and reason, scope, constraints, entry points and dependencies, observable success, and test decisions. Check each child too. Fill material gaps in the existing sections; do not paste the full investigation, interview, or history into the ticket.

For a nontrivial completed draft, launch a real read-only checker in fresh context: no inherited conversation or prep summary, only the final parent and child bodies, source pointers, governing rules, and repository access. It describes what it would implement item by item, where it must guess, and two materially different implementations any ambiguous wording allows, and returns concrete work-item blockers with evidence, not generic requests for detail. It does not implement, write tests, or interview the user. A trivial bounded edit uses the parent check alone. If fresh context is unavailable, report that and leave a nontrivial draft unchecked rather than claim independence.

For a material public boundary, the same checker simulates a representative caller using only the stated contract and says how its result would be verified. It flags leaked coordination, policy repeated across callers, an option-heavy facade that makes callers choose internal steps, verification reaching into internals, or two competing migration owners, citing the item and evidence. A renamed service or shorter signature does not prove the caller's burden disappeared.

The parent owns the verdict: research factual blockers, send only unresolved user choices to /grill-me, repair the body, and recheck the affected items and dependencies in fresh context. Allow at most two repair/recheck rounds per completed draft; if material blockers remain, report them in chat and stop until new evidence or a user decision changes the draft. No saved memo or extra ticket section.

Could two competent executors follow this body yet choose materially different behavior, data meaning, contracts, or cutover? Then resolve the factual gap or consequential decision before calling the body ready. A choice may be left to the executor only by explicit delegation that names the choice, its constraints, who may decide, and why discretion is acceptable. Preserve the user's authorization boundaries; recording a delegation does not create consent. Silence is not delegation. Ordinary implementation details may stay open within the stated contract.

Check every item has a clear Do, Why, How, and Verify, and no consumer comes before its dependency. A broad rationale, file list, or global decision list does not replace those local explanations. Source pointers must not hide an unresolved choice in another document.

Carry history only when it explains a current constraint or decision, with a compact evidence pointer marked Found, Inferred, or Unknown; keep only the conclusions the current decision needs.

Point to facts the executor must revalidate live, such as entry points and predecessor contracts. Ask the user about new facts only when they change a decision, scope, permission, or waiver.

### PR-sized subissues

Use a parent Plan with child Plans when the work has more than one coherent outcome a reviewer can assess separately, spans changes that need different explanations, or would otherwise produce one large PR. Keep one ticket when one focused PR is enough. Split only after the design is settled.

- One child owns one reviewable outcome, its file lane, and 1 to 3 binary done-when checks. Prefer thin vertical slices. A behavior-preserving prerequisite refactor can be its own child when it makes the next change smaller. No arbitrary line quotas, one-ticket-per-file splits, or empty scaffolding.
- Each child must build and pass its checks on its declared base without later children. Keep tests and verification with the behavior they prove, not in a final testing child. For migrations or refactors, use compatible expand, migrate, and contract steps. Keep an indivisible change together and say why.
- Put shared decisions and the complete outcome in the parent. Give each child a self-contained Plan with the relevant rules, exact predecessor contracts, entry points, scope, exclusions, and checks. A child may assume its dependencies are present, but not the conversation or an unspecified future change.
- Separate implementation dependencies from PR ancestry: list actual blockers apart from the one PR base. Default dependent work to a linear stack: the first child targets the integration branch, each next child the preceding child's branch. Independent work can target the integration branch in parallel; invent no dependencies to number tickets. For a join, pick a base containing every prerequisite, or wait until those prerequisites merge.
- The parent maps every done-when item to its child owners and names the final check across the complete stack. Record the integration branch, order, dependencies, PR bases, and a copyable request to implement all children in one run. Branch names follow [shipping.md](../rules/shipping.md#branch-names) and use real child IDs after creation.
- Investigate and grill the whole outcome once, then derive children; do not restart the interview per child.

Writing tickets does not start the build or publish PRs. A later request to implement all children and open stacked PRs activates the [whole-stack build handoff](../task/doctrine.md#whole-stack-ticket-handoff).

#### Stack contract check

Before declaring a split ready, check the dependency graph for cycles, consumers ordered before providers, PR bases missing required contracts, unsafe intermediate states, conflicting path or contract ownership, and parent done-when items with no owner. Fold this into the fresh-executor check for a small linear stack. Use a separate fresh-context stack checker, with the same inputs and concrete child/contract blockers, only when branching or joining dependencies, shared migrations, or overlapping ownership make the graph materially harder to assess. The parent resolves findings under the same two-round readiness loop.

### Work kind

Assign one kind from the evidence and announce it on the draft: Feature, Tweak, Bug, Refactor, or Chore. There is no Hotfix; an urgent defect is a Bug. Keep an existing kind unless the scope or user corrects it; children use the kind of their own work.

| Kind | Use when |
| --- | --- |
| Feature | New capability or intentional enhancement |
| Tweak | Small bounded intentional adjustment |
| Bug | Wrong or broken behavior |
| Refactor | Structural debt with preserved behavior |
| Chore | Non-product maintenance: deps, CI, tooling, docs-only, repo hygiene |

### Final-version description

Every create or refine writes the description as the only version a reader needs: the final current state, not a changelog.

Delete canceled ideas, superseded decisions, demoted alternatives, strikethrough (`~~...~~`), "was X / now Y", and any narrative of how the decision changed.

Use the `Rejected` line under Already decided only for a live alternative whose refusal prevents a credible implementation mistake, with its current reason; never invent a rival. Keep the reason for each current material decision either way.

A refine rewrites the affected sections, or the whole body; replace rather than append. When a material refine would lose the previous body with no trail, post that body unchanged as a comment once, then write the clean body. Never leave old and new wording in the description. If the tracker cannot comment, stop and say so.

### Inputs

| Input | Use |
| --- | --- |
| Linear or GitHub ID or URL | Read it as context. Update only when requested. |
| Legacy Memo, Research, or Plan ticket | Read useful context. Convert only that ticket when the user requests an update; no bulk migration. |
| Ambiguous number | Discover the tracker the repo uses; ask only if still ambiguous. |

## Public boundary investigation

Use this on the requested flow when a meaningful feature or boundary change, or observed architecture friction, could affect the design. A copy edit or a ticket that keeps the existing contract needs none. It prepares [deep public surface](../rules/code-structure.md#deep-public-surface), [strong foundation](../rules/strong-foundation.md), and [testing](../rules/testing.md); it is not a repository-wide audit.

Trace representative callers and their current tests. Look for ordering the caller must coordinate, repeated policy, pass-through abstractions, or tests that reach into private details, and name the observed burden and its sources. Check responsibilities accumulating in changed existing files under [responsibility boundaries](../rules/code-structure.md#responsibility-boundaries). For a proposed extraction, show what the caller stops knowing, how a reader finds the owner, and where a concrete change to that job lands.

Recommend keeping the current shape, a small justified behavior-preserving prefactor, or a material boundary change. Show the proposed owner/public entry, inputs, outcomes, error behavior, observable ordering, and invariants; the responsibilities and dependencies it hides; and a representative caller before and after. Leave private implementation choices open within the contract.

Tie the proposal to its observable verification seam. Identify dependencies that need real integration evidence versus existing stand-ins at true external boundaries, and the failure modes those substitutes cannot prove. Use the repository's existing strategy; invent no test-only public API and no second adapter for a future variation. Test work still needs [consent](../rules/no-unrequested-tests.md); old tests stay unless the [retention bar](../rules/testing.md#retention-bar) justifies a change.

Only when a material boundary stays uncertain, compare a few genuinely different interfaces through bounded read-only scouts. Give each the same outcome, constraints, domain terms, caller evidence, and dependency facts, plus one distinct design question; ask for a usage sketch, hidden responsibilities, verification approach, and tradeoffs, not implementation or a verdict. Scouts never question the user. The parent compares caller burden, change locality, and verification, recommends one, and sends only consequential user-owned decisions to the grill. No scouts for a settled interface or a routine private detail. Without delegation, compare serially and report that limitation.

Put the evidence and recommendation into the ticket's Structure, Foundation, and Work items before decomposition; no separate report. Adapted from Matt Pocock's pinned
[codebase design](https://github.com/mattpocock/skills/blob/d81f3a183412e71a5b1e84ca21bc1a35eea03a60/skills/engineering/codebase-design/SKILL.md),
[deepening](https://github.com/mattpocock/skills/blob/d81f3a183412e71a5b1e84ca21bc1a35eea03a60/skills/engineering/codebase-design/DEEPENING.md),
[interface alternatives](https://github.com/mattpocock/skills/blob/d81f3a183412e71a5b1e84ca21bc1a35eea03a60/skills/engineering/codebase-design/DESIGN-IT-TWICE.md), and
[architecture investigation](https://github.com/mattpocock/skills/blob/d81f3a183412e71a5b1e84ca21bc1a35eea03a60/skills/engineering/improve-codebase-architecture/SKILL.md).

## Output

| Problem | Action |
| --- | --- |
| Tracker capability unavailable | Explain the blocker; keep the draft in chat and report that no write occurred. |
| User corrects the draft | Rewrite affected sections into the current version; preserve draft-only versus write authorization. |
| Tracker kind label missing | Use only real label IDs; keep the kind in the body. |

## Apply

Write through the tracker capability or gh. Draft-only returns the body, never invented URLs. A split parent's copyable whole-stack request grants no current build or shipping permission. Follow [Working output](../rules/writing-style.md#working-output) throughout preparation.

## Anti-patterns

- A Plan that only restates the problem, or that depends on the comment thread
- Writing the full implementation into the Plan
- Using a tracker ID the tracker did not return
- A numbered checklist presented as linked subissues when no children were created

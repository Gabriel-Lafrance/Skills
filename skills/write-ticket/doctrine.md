# Write Ticket doctrine

## Job

Develop an implementation-ready ticket through research and decisions in one conversation. The final body carries enough intent and context for a later executor without that chat. Write or update Linear or GitHub only when requested; draft-only requests stay in chat.

## Owns

The developing ticket, work kind, final body, PR-sized decomposition, dependency handoffs, and authorized tracker writes. /analyze owns facts and impact; /how owns mechanics, /why owns evidenced historical rationale, and /grill-me owns user decisions and the intent restatement.

## Does not own

- Implementation, branching, or pull requests
- Runtime build questions. Execution validates live facts and reuses settled decisions under its own contracts.
- Numbered process: [SKILL.md](SKILL.md)
- Body and tracker details: [reference.md](reference.md)

## Bars

**Execution context:** [planning.md](../rules/planning.md#execution-context) | **Ask style:** [Asking the user](../rules/writing-style.md#asking-the-user) | **Body:** [reference.md](reference.md)

There are no ticket stages or intermediate research deliverables. Analysis and grilling refine the final ticket in chat. Reuse current evidence and decisions; revisit only material gaps. An incomplete draft can stay in chat, but do not save it as implementation-ready while core decisions remain unresolved.

### Grill

This skill is the parent. Start /grill-me with the researched context and unresolved consequential choices, and tell it to return here. Use its line-by-line intent restatement, then ask only unresolved user-owned decisions. When the request and evidence already settle the choices, proceed without a question batch. This skill derives child count, file lanes, dependencies, and PR bases from the locked design. The conversation leaves /task unstarted.

Understand the need, intended outcome and reason, affected behavior and states, constraints, and observable success from the prompt and research. Use /analyze to distinguish facts, settled decisions, ordinary implementer choices, and unresolved consequential tradeoffs. Materiality concerns behavior, contracts, data meaning or integrity, authority, compatibility, transition safety, scope, or cost, even when alternatives touch the same files. Research facts and choose ordinary details independently. Reuse parent decisions; do not manufacture questions to fill topic categories or impose a negative-scope-first order.

For a consequential user choice that remains open, state the concrete decision, evidence or uncertainty, realistic alternatives, recommended choice and reason, and practical consequences. Order questions by their dependencies and impact on the design. Preserve exclusions or rejected alternatives only when they prevent a credible mistake; no invented rival, wrong-if statement, or owner question is required. Discover owners from code where possible.

For a Feature, establish what will vary or multiply, then the seam for each confirmed area or the existing seam being extended, scaled by [strong-foundation.md](../rules/strong-foundation.md#scale-to-the-work). Settle hard implementation choices and test decisions (none, behavior lock, end-to-end, or both, what each proves, and whether the user accepts it). Reuse decisions already made rather than interviewing once for the problem and again for the solution.

### Analyze

Use /analyze for evidence about the problem, affected flow, impact, risks, and consequential design choices. Reuse current analysis; refresh missing or stale evidence as the conversation develops. Its targeted /how and /why calls keep their own contracts and return conclusions here. They do not create intermediate tickets or start separate interviews. /analyze and this skill synthesize the proposed design; /how explains current mechanics and /why explains evidenced historical rationale.

### Implementation items

For changes covered by [public boundary investigation](../analyze/doctrine.md#public-boundary-investigation), settle the shared owner, caller contract and verification seam in Structure/Foundation before splitting work. Work items connect their Do and Why to that contract, How to the responsible owner and dependencies, and Verify to observable outcomes through the same public entry. Include a representative before/after caller and what coordination or policy it no longer owns. Record migration ownership and compatibility when they constrain the transition. Keep these details where they belong once; do not prescribe private methods or add ceremony to an unchanged boundary.

Make the implementation path explicit in `Work items`: numbered meaningful changes or outcomes, with prerequisites before consumers. Name real dependencies by item number and the contract or state they supply; mark independent work as independent. Numbering alone does not imply a dependency or create a PR boundary. A small change can have one compact item. Do not turn routine edits, individual files, or coding mechanics into separate items.

Each item carries four local parts:

- **Do:** the specific change and resulting behavior or outcome.
- **Why:** why this change and approach are needed, including the reason for its consequential choices. Reuse settled decisions and their evidence; do not invent a justification or repeat the broad goal as every item's reason.
- **How:** the concrete approach through relevant code, data, contracts, and constraints, with evidence pointers and material uncertainty where needed. Resolve consequential ambiguity before finalizing, while leaving ordinary coding choices to the executor.
- **Verify:** an observable result and a suitable way to check this item's behavior or contract after implementation. Describe a future check, not a completed result. Refer to `Tests` for any proposed, accepted, or refused test and its decision source. This field neither authorizes new tests nor starts execution, migrations, deployment, or other planned work.

Each item owns its local rationale and approach. Keep Structure and Foundation for shared design, Files as a path-to-item index, Already decided for shared decisions or bounded delegation, and Done when for overall acceptance. Reference those shared facts briefly where needed instead of copying them into every item. If an item is the only owner of a choice, explain it there once. Keep the ticket proportional; a short clause per part can be enough.

### Fresh-executor handoff

For touched user flows, the same checker walks the Plan's UX/UI contract from entry context through the result and next action. Flag concrete ambiguity about carried data, recovery, or component reuse that could produce materially different behavior. Apply [action and continuation](../rules/user-experience.md#action-and-continuation); ordinary interaction details stay with the executor. No extra checker or backend-only design questions.

This is the canonical readiness bar, also used by the execution [ready-ticket preflight](../rules/execution.md#ready-ticket-preflight). Before showing a Plan as complete or writing it, can an executor understand who benefits, the outcome and reason, scope, constraints, relevant entry points and dependencies, observable success, and test decisions from the current body and its specific source pointers? Check each child too. Fill material gaps in the existing sections; do not paste the full memo, interview, or history into the ticket.

For a nontrivial completed draft, launch an actual read-only checker in fresh context, with no inherited conversation or prep-chat summary. Give it only the final parent and child bodies, explicit source pointers, governing rules, and repository access. Ask it to describe what it would implement item by item, identify where it must guess, and name two materially different implementations that fit any ambiguous wording. It returns concrete work-item blockers with evidence or the conflicting interpretations, not generic requests for more detail. It does not implement, write tests, interview the user, or start another preparation lifecycle. A trivial bounded edit can use the parent check alone. If fresh context is unavailable, report that limitation and leave a nontrivial draft unchecked rather than claiming independence.

For a material public boundary, have that same checker simulate a representative caller using only the stated contract, then describe how its observable result would be verified. Flag concrete leaked coordination, policy repeated across callers, an option-heavy facade that makes callers choose internal steps, verification reaching into internals, or two competing migration owners. Cite the affected item and caller or test evidence. A renamed service or shorter signature is not evidence that the caller's burden disappeared. This extends the existing checker, not another mandatory review pass.

The parent owns the verdict. Research factual blockers and use /grill-me only for unresolved consequential user choices. Preserve settled choices and test acceptances or refusals. Repair the body, then recheck the affected items and dependencies in fresh context. Allow at most two repair/recheck rounds per completed draft; if material blockers remain, report them in chat and stop the readiness loop until new evidence or a user decision changes the draft. This needs no saved memo or extra ticket section.

Could two competent executors follow this body yet choose materially different behavior, data meaning, contracts, or cutover? If so, resolve the factual gap or consequential decision before calling the body ready. An explicit delegation can leave a choice to the executor only when the body names the choice, its constraints, who may decide, and why that discretion is acceptable. Preserve the user's authorization boundaries; recording a delegation does not create consent. Silence is not delegation. Ordinary implementation details may remain open within the stated contract.

Check every meaningful implementation item: can the executor identify what to do, why that approach was chosen, how it fits the code or data flow, and what observable result will verify it? Are its prerequisites and the contracts they supply clear, with no consumer ordered before its dependency? A broad outcome rationale, file list, or global decision list does not replace those local explanations. Preserve relevant evidence, uncertainty, and invariants beside the choice, with short references to shared context when needed. Source pointers support the body; they must not hide an unresolved choice in another document.

Carry the relevant `/how` conclusions into the existing flow and ownership sections. Carry `/why` conclusions only when they explain a current constraint or decision, with a compact evidence pointer and their Found, Inferred, or Unknown status intact. Historical rationale is not the user's desired outcome. Keep only conclusions needed to understand or implement the current decision.

Look up repository facts and missing evidence. Return only unresolved user-owned decisions to `/grill-me`; do not ask the user to research paths or reconfirm settled choices. Keep proposed tests distinct from accepted or refused tests, with the user's decision source for either settled status. `none` means no tests specified, not a refusal inferred from silence.

The Plan must survive a new session, but it is not proof of live repository state. Point to facts the executor must revalidate, such as entry points and predecessor contracts. New facts warrant a user question only when they require a changed decision, scope, permission, or waiver.

### PR-sized subissues

Use a parent Plan with child Plans when the work has more than one coherent outcome a reviewer can assess separately, spans changes that need different explanations, or would otherwise produce one large PR. Keep one ticket when one focused PR is enough. Derive the split only after the design is settled.

- One child owns one reviewable outcome, its file lane, and 1 to 3 binary done-when checks. Prefer thin vertical slices. A prerequisite refactor can be its own child when it preserves behavior and makes the next change smaller. Avoid arbitrary line quotas, one-ticket-per-file splits, and empty scaffolding.
- Each child must build and pass its checks on its declared base without later children. Keep tests and verification with the behavior they prove; do not leave every check to a final testing child. For migrations or refactors, use compatible expand, migrate, and contract steps. Keep an indivisible change together and explain why.
- Put shared decisions and the complete outcome in the parent. Give each child a self-contained Plan with the relevant rules, exact predecessor contracts, entry points, scope, exclusions, and checks. A child can assume its dependencies are present, but cannot depend on the conversation or an unspecified future change.
- Distinguish implementation dependencies from PR ancestry. List actual blockers separately from the one PR base. Default dependent work to a linear stack: first child targets the integration branch, each next child targets the preceding child branch. Independent work can target the integration branch in parallel; do not invent dependencies merely to number the tickets. For a join, select a base containing every prerequisite, or explicitly wait until those prerequisites merge.
- The parent maps every done-when item to its child owners and names the final check across the complete stack. Record the integration branch, order, dependencies, PR bases, and a copyable request to implement all children in one run. Branch names follow [shipping.md](../rules/shipping.md#branch-names) and use real child IDs after creation.
- Reuse settled decisions across all children. Run analysis and grill for the whole outcome, then derive children from that context; do not restart the interview per child. Record tests as proposed, explicitly accepted, refused, or none, with the user's decision source when settled. Listing a test in a Plan is not acceptance to write it.

Writing tickets does not start the build or publish PRs. A later request to implement all children and open stacked PRs activates the [whole-stack build handoff](../task/doctrine.md#whole-stack-ticket-handoff).

#### Stack contract check

Before declaring a split ready, check the actual dependency graph for cycles, consumers ordered before providers, PR bases missing required contracts, unsafe intermediate states, conflicting path or contract ownership, and parent done-when items with no owner. For a small linear stack, include this in the fresh-executor check. Use a separate fresh-context read-only stack checker only when branching or joining dependencies, shared migrations, or overlapping ownership make the graph materially harder to assess. Give it the same bounded final bodies and sources, not prep chat; require concrete child/contract blockers. The parent owns decomposition and resolves findings under the same bounded readiness loop. A clean planned graph does not replace execution-time validation of live predecessor contracts.

### Work kind

Assign one kind from the evidence and announce it on the draft: Feature, Tweak, Bug, Refactor, or Chore. There is no Hotfix. Use Bug for a defect, including an urgent one. Preserve an existing kind unless the scope or user corrects it; children use the kind matching their own work.

| Kind | Use when |
| --- | --- |
| Feature | New capability or intentional enhancement |
| Tweak | Small bounded intentional adjustment |
| Bug | Wrong or broken behavior |
| Refactor | Structural debt with preserved behavior |
| Chore | Non-product maintenance: deps, CI, tooling, docs-only, repo hygiene |

### Final-version description

Every create or refine writes the description as the only version a reader needs. It is the final current state, not a changelog.

Delete canceled ideas, superseded decisions, demoted alternatives, strikethrough (`~~...~~`), "was X / now Y", and any narrative of how the decision changed. Do not leave them in the current body.

Use the `Rejected` line under Already decided only for live exclusions or alternatives whose refusal prevents a credible implementation mistake, with the current reason. It may say `_none_`. Do not invent a rival or keep superseded alternatives as history. Preserve the reason for each current material decision even when no rejected alternative is useful.

A refine rewrites the affected sections, or the whole body. Prefer replacing over appending. When the refine is material and the previous body would otherwise be lost with no trail, post that body unchanged as a comment once, then write the clean body. Never leave both old and new wording in the description. If the tracker cannot comment, stop and say so, so the previous body is never lost.

Trim fat and useless text. Chat and `/grill-me` hold the interview trail. The ticket body does not.

### Inputs

| Input | Use |
| --- | --- |
| Linear or GitHub ID or URL | Read it as context. Update only when requested. |
| Idea or rough notes | Develop the final ticket here; draft-only stays in chat. |
| In-chat analysis or locked decisions | Reuse current evidence and answers; refresh material gaps. |
| Legacy Memo, Research, or Plan ticket | Read useful context. Convert only that ticket when the user requests an update; no bulk migration. |
| Ambiguous number | Discover the tracker used by the repo; ask only if still ambiguous. |

## Output

| Problem | Action |
| --- | --- |
| Tracker capability unavailable | Explain the blocker; retain the draft in chat and report that no write occurred. |
| Ticket not found | Confirm its ID, team, or repository. |
| User corrects the draft | Rewrite affected sections into the current version; preserve draft-only versus write authorization. |
| Material context missing | Research facts; return unresolved user decisions to /grill-me. Keep the incomplete draft in chat. |
| Two plausible implementations differ materially, or a material decision lacks its reason | Research facts, settle or explicitly delegate the choice, and carry its rationale into the body before finalizing. |
| An implementation item lacks actionable Do, Why, How, Verify, or a required dependency | Fill its local explanation from evidence and settled decisions before finalizing; do not invent facts or execute its checks. |
| Analysis absent or shallow | Run or refresh /analyze before locking the affected decision. |
| Tracker kind label missing | Use only real label IDs; keep the kind in the body. |
| Comment API unavailable for a material update that would lose the prior body | Stop before replacement and report the blocker. |

## Apply

Show the complete draft in chat. If a tracker write was requested, create or update through its capability or gh without asking again for that authorization. Return actual parent and child URLs, kind, applied metadata, and stack order. Draft-only returns the body, not invented URLs. For split work, include the copyable whole-stack request from the reference; it is a future request, not current build or shipping permission.

## Anti-patterns

- A Plan that only restates the problem, or that depends on the comment thread
- A file checklist or broad rationale standing in for ordered, locally explained implementation items
- Writing the full implementation into the Plan
- Using a tracker ID the tracker did not return
- A large Plan with one implementation ticket when its outcomes could be reviewed separately
- Child PRs that need later children to compile or pass their checks
- A numbered checklist presented as linked subissues when no children were created
- Strikethrough (`~~...~~`) left in the live description
- A "was X / now Y" write-up, or a narrative of how the decision changed, left in the live body
- Appending a correction instead of rewriting the affected sections
- A canceled or demoted option kept beside the current choice

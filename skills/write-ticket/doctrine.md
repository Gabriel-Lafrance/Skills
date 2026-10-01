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

This skill is the parent. Start /grill-me with the topics below and tell it to return here. Use its line-by-line intent restatement, then ask only unresolved user-owned decisions. This skill derives child count, file lanes, dependencies, and PR bases from the locked design. The conversation leaves /task unstarted.

Settle the need, who benefits and when, current behavior, intended outcome and why it matters, the decision and current rival, exclusions, what would make the decision wrong, rules that must stay true, behavior edges and states, and binary done-when. Research repository facts first: the existing owner path, public entry, callers, and write boundary. Grill only choices those facts do not settle.

For a Feature, establish what will vary or multiply, then the seam for each confirmed area or the existing seam being extended, scaled by [strong-foundation.md](../rules/strong-foundation.md#scale-to-the-work). Settle hard implementation choices and test decisions (none, behavior lock, end-to-end, or both, what each proves, and whether the user accepts it). Reuse decisions already made rather than interviewing once for the problem and again for the solution.

### Analyze

Use /analyze for evidence about the problem, relevant code, impact, and risks. Reuse current analysis; refresh missing or stale evidence as the conversation develops. Its targeted /how and /why calls keep their own contracts and return conclusions here. They do not create intermediate tickets or start separate interviews.

### Fresh-executor handoff

Before showing a Plan as complete or writing it, read it as an executor without the old chat. Can that reader understand who benefits, the outcome and reason, scope, constraints, relevant entry points and dependencies, observable success, and test decisions from the current body and its specific source pointers? Check each child too. Fill material gaps in the existing sections; do not paste the full memo, interview, or history into the ticket.

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

Keep the single current rival in the `Rejected` line under Already decided. That line is the live refusal. One current rejected alternative. Remove older rivals that are no longer that refusal.

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
| Non-trivial grill lacks rejected alternative, what would make the decision wrong, or owner path | Resolve those gaps before finalizing. |
| Analysis absent or shallow | Run or refresh /analyze before locking the affected decision. |
| Tracker kind label missing | Use only real label IDs; keep the kind in the body. |
| Comment API unavailable for a material update that would lose the prior body | Stop before replacement and report the blocker. |

## Apply

Show the complete draft in chat. If a tracker write was requested, create or update through its capability or gh without asking again for that authorization. Return actual parent and child URLs, kind, applied metadata, and stack order. Draft-only returns the body, not invented URLs. For split work, include the copyable whole-stack request from the reference; it is a future request, not current build or shipping permission.

## Anti-patterns

- A Plan that only restates the problem, or that depends on the comment thread
- Writing the full implementation into the Plan
- Using a tracker ID the tracker did not return
- A large Plan with one implementation ticket when its outcomes could be reviewed separately
- Child PRs that need later children to compile or pass their checks
- A numbered checklist presented as linked subissues when no children were created
- Strikethrough (`~~...~~`) left in the live description
- A "was X / now Y" write-up, or a narrative of how the decision changed, left in the live body
- Appending a correction instead of rewriting the affected sections
- A canceled or demoted option kept beside the current choice

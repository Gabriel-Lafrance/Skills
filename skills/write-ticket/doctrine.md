# Write Ticket doctrine

## Job

Write or promote Linear or GitHub tickets. Memo captures an idea. Research records the need and the problem. Plan records how to solve that problem in code, in enough detail that a later build can implement it. Larger Plans use a parent for the complete outcome and child tickets for small pull requests.

This skill is a user start and only writes the ticket.

## Owns

Stage selection, the two `/grill-me` gates, body shapes, promotion on the same parent ticket, work kind, PR-sized decomposition, dependency and stack handoffs, and tracker writes.

## Does not own

- Implementation, branching, or pull requests
- Remaining build questions. `/task` owns those and reuses settled decisions in a [whole-stack handoff](../task/doctrine.md#whole-stack-ticket-handoff). It does not promote the ticket.
- Numbered how-to: [`SKILL.md`](SKILL.md)
- Section templates: [`reference.md`](reference.md)

## Bars

**Execution context:** [planning.md](../rules/planning.md#execution-context) · **Ask style:** [Asking the user](../rules/writing-style.md#asking-the-user) · **Templates:** [reference.md](reference.md)

Three stages. The user can start at any stage. A later stage replaces the description of the **same** ticket. The previous body becomes a comment.

| Stage | Job | Before save |
| --- | --- | --- |
| Memo | Keep the idea. A title and a few sentences. | Write, skipping `/analyze` and `/grill-me`. |
| Research | Understand the need, the issue, and the problem. | Full `/analyze`, then `/grill-me` on the Research topics, then write. |
| Plan | Say how to solve that problem in code. | Full `/analyze`, then `/grill-me` on the Plan topics, then write. |

Research does not specify the code. The Plan does. The Plan repeats the locked choices in implementation detail so a coding agent can work from the Plan alone. The comment thread is the trail.

### Stage gate

Ask the stage only when the prompt and the current ticket do not already name one. When an existing ticket is loaded and the user did not name a target, recommend the next stage: Memo to Research, Research to Plan. Plan has no next stage; refining a Plan stays a Plan.

Allowed asking batches, besides the `/grill-me` session this skill starts:

| When | What to ask |
| --- | --- |
| Target stage unknown | One batch: stage, plus priority, assignee, and tracker when those are also missing |
| Stage known, metadata still missing | One metadata batch after the draft is shown |
| Research evidence still cannot pick a work kind | One kind question inside the Research `/grill-me`, not a separate batch |

Write without asking "write this?". Take status from the default (**Todo** on create; keep the current status on promote or refine unless the prompt names one) instead of asking. Leave the Research and Plan topics to `/grill-me`.

### Grill

This skill is the parent. Start `/grill-me` with the topic list for the target stage and tell it to return here. Research leaves implementation split and files open. For Plan, this skill derives the child count, file lanes, dependencies, and PR bases from the locked design; grill only unresolved decisions that would change those boundaries. The session hands control back and leaves `/task` unstarted.

**Research topics:** the need, the issue, the problem, who is affected and when, what happens today, the rival explanation of the problem this research rejects, what would make this the wrong problem, what this research is not trying to cover, the work kind only when it is still unknowable, and for a Feature the areas of modularity: what will vary or multiply (providers, channels, rules, roles, formats), each as one yes or no question with a recommended answer from the evidence ([strong-foundation.md](../rules/strong-foundation.md#find-the-areas-of-modularity)). Research records the fact ("more than one payment provider") and names no pattern.

**Plan topics:** the decision and the rival this plan rejects, what the change refuses to own, what would make that decision wrong, rules that must stay true, edges and states of the solution, binary done-when, out of scope, where the change lives, who owns the job (the existing path, the public entry, who calls it, where the write is rejected, one-job helpers, folders), the foundation (a seam, a named extension point where a new variant plugs in, for each area of modularity the Research confirmed, or the existing seam this extends, and the next change it makes small, scaled by [strong-foundation.md](../rules/strong-foundation.md#scale-to-the-work)), short snippets of the hard parts, and tests (none, a behavior lock, end-to-end, or both, including what each lock proves).

A Memo skips `/grill-me`.

### Analyze

Run `/analyze` to full memo depth before the Research grill and before the Plan grill. Tell it the stage. Research memos gather evidence about the problem. Plan memos gather evidence about the code that would change. Return the memo here, and require the full memo, not a stub.

A Memo skips `/analyze`.

### PR-sized subissues

Prefer a parent Plan with child Plans when the work has more than one coherent outcome a reviewer can assess separately, spans changes that need different explanations, or would otherwise produce one large PR. Keep one ticket when one focused PR is enough. Do not split Memo or Research into implementation children before the design is settled.

- One child owns one reviewable outcome, its file lane, and 1 to 3 binary done-when checks. Prefer thin vertical slices. A prerequisite refactor can be its own child when it preserves behavior and makes the next change smaller. Avoid arbitrary line quotas, one-ticket-per-file splits, and empty scaffolding.
- Each child must build and pass its checks on its declared base without later children. Keep tests and verification with the behavior they prove; do not leave every check to a final testing child. For migrations or refactors, use compatible expand, migrate, and contract steps. Keep an indivisible change together and explain why.
- Put shared decisions and the complete outcome in the parent. Give each child a self-contained Plan with the relevant rules, exact predecessor contracts, entry points, scope, exclusions, and checks. A child can assume its dependencies are present, but cannot depend on the conversation or an unspecified future change.
- Distinguish implementation dependencies from PR ancestry. List actual blockers separately from the one PR base. Default dependent work to a linear stack: first child targets the integration branch, each next child targets the preceding child branch. Independent work can target the integration branch in parallel; do not invent dependencies merely to number the tickets. For a join, select a base containing every prerequisite, or explicitly wait until those prerequisites merge.
- The parent maps every done-when item to its child owners and names the final check across the complete stack. Record the integration branch, order, dependencies, PR bases, and a copyable request to implement all children in one run. Branch names follow [shipping.md](../rules/shipping.md#branch-names) and use real child IDs after creation.
- Reuse settled decisions across all children. Run analysis and grill for the whole outcome, then derive children from that context; do not restart the interview per child. Record tests as proposed, explicitly accepted, refused, or none, with the user's decision source when settled. Listing a test in a Plan is not acceptance to write it.

Writing tickets does not start the build or publish PRs. A later request to implement all children and open stacked PRs activates the [whole-stack build handoff](../task/doctrine.md#whole-stack-ticket-handoff).

### Work kind

During Research, or when starting directly at Plan, assign exactly one kind and announce it on the draft: Feature, Tweak, Bug, Refactor, or Chore. There is no Hotfix. Use Bug for a defect, including an urgent one. Memo may leave kind unset. A promoted Plan carries the Research kind forward unless the user corrects it; children use the kind matching their own work.

| Kind | Use when |
| --- | --- |
| Feature | New capability or intentional enhancement |
| Tweak | Small bounded intentional adjustment |
| Bug | Wrong or broken behavior |
| Refactor | Structural debt with preserved behavior |
| Chore | Non-product maintenance: deps, CI, tooling, docs-only, repo hygiene |

### Promotion

Memo to Research, and Research to Plan, update the same ticket.

1. Finish that stage's analyze and `/grill-me`.
2. Post the current description as a comment.
3. Replace the description with the new body.
4. Set the stage label (`Memo`, `Research`, or `Plan`) and the kind label when the tracker has one.

Use the same ticket for the next stage. If the tracker cannot comment, stop and say so, so the previous body is never lost.

### Inputs

| Input | Mode |
| --- | --- |
| Linear ID or URL | Read it. Promote or refine that ticket. |
| GitHub issue ID or URL | Read it. Promote or refine that issue. |
| Idea or "don't forget" note | Create. Infer Linear versus GitHub from the repo and the prompt. |
| In-chat analysis memo | Reuse it when it is already a full memo for this stage. Refresh it when it is shallow, stale, or for the other stage. |
| Ambiguous number | Prefer the tracker this repo already uses. Ask only inside the stage or metadata batch. |

## Output

| Problem | Action |
| --- | --- |
| No Linear capability | Explain the limitation and report that no ticket was created. |
| GitHub tooling unavailable | Ask for install or auth inside the metadata batch, or allow one pasted body for refine only. |
| Ticket not found | Stop and confirm ID, team, or repository. |
| User corrects the draft | Update the draft and write that version. |
| Required Research or Plan section still empty after `/grill-me` | One asking-contract batch for the gaps, then write. A saved Plan has a filled done-when, rules, and tests section. |
| Non-trivial grill returned without a rejected alternative, what would make the decision wrong, or the owner path | Send it back to `/grill-me` and write the ticket after it returns those. |
| Analysis absent or stubby on Research or Plan | Run or refresh full `/analyze` before `/grill-me`. |
| Tracker label missing | The `## Stage` heading is still required. Use only real label IDs. |
| Comment API unavailable on promotion | Stop. Do not replace the description. |

## Apply

Show the complete draft in chat, then create or update through the tracker capability or `gh`. Return the parent and child URLs, the stage, the kind when set, the applied metadata, and the stack order. For a split Plan, include the copyable whole-stack request from the reference.

## Anti-patterns

- A Plan that only restates the problem, or that depends on the comment thread
- Writing the full implementation into the Plan
- Using a tracker ID the tracker did not return
- A large Plan with one implementation ticket when its outcomes could be reviewed separately
- Child PRs that need later children to compile or pass their checks
- A numbered checklist presented as linked subissues when no children were created

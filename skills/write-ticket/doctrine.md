# Write Ticket doctrine

## Job

Write or promote one Linear or GitHub ticket. Memo captures an idea. Research records the need and the problem. Plan records how to solve that problem in code, in enough detail that a later `/task` can implement it.

This skill is a user start. It never implements the ticket.

## Owns

Stage selection, the two `/grill-me` gates, body shapes, promotion on the same ticket, work kind, and tracker writes.

## Does not own

- Implementation, branching, or pull requests
- `/task`'s own grill. `/task` still grills when it builds. It does not promote the ticket.
- Numbered how-to: [`SKILL.md`](SKILL.md)
- Section templates: [`reference.md`](reference.md)

## Cite keys

none (uses `quality:*` and `structure:*`)

## Bars

**Execution context:** [planning.md](../rules/planning.md#execution-context) · **Ask style:** [Asking the user](../rules/writing-style.md#asking-the-user) · **Templates:** [reference.md](reference.md)

Three stages. The user can start at any stage. A later stage replaces the description of the **same** ticket. The previous body becomes a comment.

| Stage | Job | Before save |
| --- | --- | --- |
| Memo | Keep the idea. A title and a few sentences. | Write. No `/analyze`. No `/grill-me`. |
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

Do not ask "write this?". Do not ask status (default **Todo** on create; keep the current status on promote or refine unless the prompt names one). Do not ask the Research or Plan topics yourself. `/grill-me` asks those.

### Grill

This skill is the parent. Start `/grill-me` with the topic list for the target stage. Tell it to skip implementation plan count and file lane, and to return here. Do not start `/task` from that session.

**Research topics:** the need, the issue, the problem, who is affected and when, what happens today, what this research is not trying to cover, and the work kind only when it is still unknowable.

**Plan topics:** rules that must stay true, edges and states of the solution, binary done-when, out of scope, where the change lives, the structure (design pattern, abstraction, one-job helpers, deep module, folders, public API) when the change needs them, short snippets of the hard parts, and tests (none, a behavior lock, end-to-end, or both, including what each lock proves).

A Memo never starts `/grill-me`.

### Analyze

Run `/analyze` to full memo depth before the Research grill and before the Plan grill. Tell it the stage. Research memos gather evidence about the problem. Plan memos gather evidence about the code that would change. Return the memo here. Do not accept a stub.

A Memo does not run `/analyze`.

### Work kind

During Research, assign exactly one kind and announce it on the draft: Feature, Tweak, Bug, Refactor, or Chore. There is no Hotfix. Use Bug for a defect, including an urgent one. Memo may leave kind unset. Plan carries the Research kind forward unless the user corrects it.

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

Do not open a second ticket for the next stage. If the tracker cannot comment, stop and say so. Do not drop the previous body.

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
| No Linear capability | Explain the limitation. Do not fake a ticket. |
| GitHub tooling unavailable | Ask for install or auth inside the metadata batch, or allow one pasted body for refine only. |
| Ticket not found | Stop and confirm ID, team, or repository. |
| User corrects the draft | Update the draft and write that version. |
| Required Research or Plan section still empty after `/grill-me` | One asking-contract batch for the gaps, then write. Do not save a Plan with an empty done-when, rules, or tests section. |
| Analysis absent or stubby on Research or Plan | Run or refresh full `/analyze` before `/grill-me`. |
| Tracker label missing | The `## Stage` heading is still required. Do not invent a label ID. |
| Comment API unavailable on promotion | Stop. Do not replace the description. |

## Apply

Show the complete draft in chat, then create or update through the tracker capability or `gh`. Return the URL, the stage, the kind when set, and the applied metadata.

## Anti-patterns

- Running inside `/task`, or starting `/task` from the grill
- Saving a Research or Plan ticket before that stage's `/grill-me` answers
- Grilling a Memo, or running `/analyze` for a Memo
- Putting the code solution in Research
- A Plan that only restates the problem, or that depends on the comment thread
- Opening a new ticket for the next stage
- Replacing a description without commenting the previous body
- Hotfix as a kind
- Asking "write this?" or status when a default exists
- Defaulting a new ticket to Backlog instead of Todo
- Writing the full implementation into the Plan
- A snippet-free Plan that still leaves a hard decision for the implementer to guess
- Inventing tracker IDs

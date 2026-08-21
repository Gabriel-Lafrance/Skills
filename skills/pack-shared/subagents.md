# Subagents

Shared contract for Task subagents. Parents Read this file and dispatch Task
tools directly — there is no separate `/orchestrate` skill.

Use the shared [execution context](execution-context.md). The parent carries
context in chat; no worker reads or updates agent-owned runtime files.

## Bias

The main agent stays in its smart zone: **decide, ask the user, dispatch Task
workers, and review their output**. It does not do non-trivial research,
implementation, or review labor itself. Workers stay in theirs: one bounded
job, then Completion.

Sequential Tasks are required when there is only one non-trivial job — context
isolation still pays off. When surfaces, slices, or review axes are
independent, launch **one Task per lane in the same turn**. There is **no cap
of two**. Stay on the main agent only when the job is trivial.

## Subagent model

- Omit Task `model` so workers inherit the parent chat model.
- Pass a model only when the user explicitly requested one.

## Task type

Pick any **listed** Task type that fits the job. Pack roles (`explorer`,
`architect`, `implementer`, `reviewer`, `pr-reviewer`) and Cursor built-ins
(`explore`, `generalPurpose`, and any other type on the Task list) are both
valid. Match the job. Do not default to two generic workers by habit. Do not
use `reviewer` for a GitHub PR, and do not use `pr-reviewer` for a local
branch.

## Roles

| Role | Does | Does not |
| --- | --- | --- |
| Main | Compiles context, assigns bounded work, reviews Completions, integrates, updates chat context, records acceptance evidence, dispatches review gates | Solo non-trivial research/implement/review, redo a worker's job, make workers infer intent, or delegate final gates |
| Subagent | Delivers one bounded job in its file lane and returns Completion | Chat with the user, broaden scope, run lifecycle gates, or invent shared structure |

## Worker Brief

The main agent is the context compiler. Write the brief before every dispatch;
do not hand a worker an opaque plan path or hidden state to reconstruct.

```markdown
## Parent outcome
**Outcome:** <one line>
**Done when:** <relevant binary rows>
**Non-goals:** <bounded exclusions>
**Ticket / PR:** <reference | none>
**Fixed point:** <ref | none>

## Locked decisions
- <relevant user decisions, waivers, and promotions>

## Rules that must stay true
| ID | Rule | How we enforce it | How we check it |
| --- | --- | --- | --- |
| Rule 1 | … | … | … |

## Job
**Slice:** <one bounded deliverable>
**Acceptance criteria:** <relevant rows>
**Write allowlist:** <exact paths>
**Must not touch:** <siblings or shared seams>
**Dependencies / interfaces:** <ready, blocked, or contract>

## Read first
- `taste/doctrine.md` and `architecture/doctrine.md` (hard — [standards.md](standards.md))
- `pack-shared/plain-language.md` when this worker's output will be pasted into the discussion reply
- <repo paths, ticket, PR, or committed docs only>

## Escalation boundary
Do not improvise a new abstraction, shared API, service, file lane, or scope
expansion. Report the blocker and smallest viable option to the parent.

## Completion
**Status:** done | blocked
**Scope:** …
**Evidence:** …
**Findings:** none | <finding IDs and summaries>
**Handoff:** <changed interface, decision, or blocker>
```

## When to spawn

| Situation | Action |
| --- | --- |
| Non-trivial research, implement, review, structure, or multi-file edit | **Must** Task (even if only one job). Main reviews the Completion |
| Independent surfaces, ready slices, or review axes | **Must** parallel Tasks in the same turn — **one Task per lane**. No cap of two |
| Research a surface | Pack `explorer` or Cursor `explore` (or another listed type that fits) |
| Structure card | Pack `architect` or Cursor `generalPurpose` (or another listed type that fits) |
| Implement one bounded slice | Pack `implementer` or Cursor `generalPurpose` (or another listed type that fits) — one brief per independently reviewable slice |
| Local diff review | Pack `reviewer` or Cursor `generalPurpose` (or another listed type that fits) |
| GitHub PR review | Pack `pr-reviewer` or Cursor `generalPurpose` (or another listed type that fits) |
| Standards and Spec review | Parallel Tasks (plus extra Tasks when the diff has independent surfaces), then adversarial Wave 2 as a Task — see `/code-review` |
| Typo, pure rename, single obvious one-liner, git status, reading existing terminals | Main may do it |
| Verify logs / MCP lint ritual | Main only — never a verification-only Task |

## After a wave

1. Collect every Completion report.
2. **Review** it against the parent outcome, rules that must stay true, lane,
   and handoff. Reject and relaunch if the report is incomplete or off-lane.
   Do not redo the worker's research, implementation, or review on the main
   agent.
3. Post an updated compact execution context in chat when phase, ownership, or
   decisions changed.
4. If ready slices remain, update their status in **Current slices** and
   dispatch the next frontier. After every slice is integrated, blocked, or
   explicitly waived, the main agent records acceptance evidence (Done when,
   rules that must stay true, seams — path walk / terminals / browser when UI);
   it then runs `/code-review` when the parent requires it (`/code-review`
   still dispatches review Tasks).

## Anti-patterns

- Soloing non-trivial work on the main agent "to save a round"
- Capping at two Tasks when more independent surfaces exist
- Defaulting to `explore` / `generalPurpose` by habit when another listed type fits
- Forbidding a listed Cursor type, or a listed pack role, that fits the job
- Task without outcome, lane, rules that must stay true, taste/architecture Reads, and escalation boundary
- Worker asked to infer user decisions from an id, temp directory, or plan path
- Parallel work with overlapping lanes or undefined handoffs
- Worker running acceptance gates or `/code-review`
- Passing Task `model` without a user request
- Writing a progress, registry, or status file for agent-only bookkeeping
- Inventing a parallel `/orchestrate` skill instead of this contract

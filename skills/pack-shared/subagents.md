# Subagents

Shared contract for Task subagents. Parents Read this file and dispatch Task
tools directly — there is no separate `/orchestrate` skill.

Use the shared [execution context](execution-context.md). The parent carries
context in chat; no worker reads or updates agent-owned runtime files.

## Bias

Default to Task subagents for **non-trivial** work so the main chat stays lean:
decide, ask the user, integrate, and run gates. Sequential Tasks are fine when
there is only one job — context isolation still pays off. Parallelize when
lanes are independent. Stay on the main agent when the job is trivial.

## Subagent model

- Omit Task `model` so workers inherit the parent chat model.
- Pass a model only when the user explicitly requested one.

## Roles

| Role | Does | Does not |
| --- | --- | --- |
| Main | Compiles context, assigns bounded work, integrates, updates chat context, records acceptance evidence, runs `/code-review` | Solo non-trivial research/implement/review the worker should own, make workers infer intent, or delegate final gates |
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

## Active Rules
| ID | Rule | Enforcement | Verification |
| --- | --- | --- | --- |
| INV-1 | … | … | … |

## Job
**Slice:** <one bounded deliverable>
**Acceptance criteria:** <relevant rows>
**Write allowlist:** <exact paths>
**Must not touch:** <siblings or shared seams>
**Dependencies / interfaces:** <ready, blocked, or contract>

## Read first
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
| Non-trivial research, implement, review, or multi-file edit | **Must** Task (even if only one job) |
| ≥2 independent lanes | **Must** parallel Tasks in the same turn |
| Explore an independent lane | `explore` Task |
| Implement one bounded slice | `generalPurpose` Task — one brief per independently reviewable slice |
| Standards and Spec review | Parallel Tasks, then adversarial follow-up — see `/code-review` |
| Typo, pure rename, single obvious one-liner, git status, reading existing terminals | Main may do it |
| Verify logs / MCP lint ritual | Main only — never a verification-only Task |

## After a wave

1. Collect every Completion report.
2. Check it against the parent outcome, Active Rules, lane, and handoff.
3. Post an updated compact execution context in chat when phase, ownership, or
   decisions changed.
4. If ready slices remain, update their status in **Current slices** and
   dispatch the next frontier. After every slice is integrated, blocked, or
   explicitly waived, the main agent records acceptance evidence (Done when,
   Active Rules, seams — path walk / terminals / browser when UI); it then runs
   `/code-review` when the parent flow requires it.

## Anti-patterns

- Soloing non-trivial multi-file or multi-lane work on the main agent when a
  Task would protect context
- Task without outcome, lane, Active Rules, and escalation boundary
- Worker asked to infer user decisions from an id, temp directory, or plan path
- Parallel work with overlapping lanes or undefined handoffs
- Worker running acceptance gates or `/code-review`
- Passing Task `model` without a user request
- Writing a progress, registry, or status file for agent-only bookkeeping
- Inventing a parallel `/orchestrate` skill instead of this contract

# Subagents

Shared contract for Task subagents. Parents Read this file and dispatch Task
tools directly — there is no separate `/orchestrate` skill.

Use the shared [execution context](execution-context.md). The parent carries
context in chat; no worker reads or updates agent-owned runtime files.

## Bias

The main agent stays in its smart zone: **decide, ask the user, split the
what, inject need-to-know, dispatch Task workers, and review Completions**.
It does not do non-trivial find, analyze, implement, or review labor. It does
not grep the tree. Workers stay in theirs: one bounded job, then Completion.

A worker fits the **smart zone** when the brief plus working set stay around
**30% of the context window**. Harness, skills, rules, and MCP already use
about half. Sequential Tasks are required when there is only one non-trivial
job. When surfaces, slices, or review axes are independent, launch **one Task
per lane in the same turn**. There is **no cap of two**. Stay on the main
agent only when the job is trivial.

Pick the specialist that owns the job. Do **not** follow a fixed spawn order.

## What vs how

One altitude: the parent coordinates; the specialist does the detail.

- **Parent feeds what:** the tiny outcome, write allowlist, Done when, rules
  that must stay true, and need-to-know (explorer hits, locked structure
  excerpt, paths/snippets already found). That is the brief.
- **Parent does not feed how:** no file-by-file recipes, no prescribed grep
  script, no hunt order, no “first write this function then that helper”.
- **Subagent owns how:** explorer chooses how to search; analyzer chooses how
  to judge impact; implementer chooses how to shape the code; reviewer
  chooses how to hunt; tester chooses how to lock the behavior. Taste and
  architecture live in that how.
- **After the wave:** the parent checks the Completion against the what.
  Reject and relaunch if the what was missed or bars were skipped. Do not
  take the how back onto the main agent.

## Subagent model

- Omit Task `model` so workers inherit the parent chat model.
- Pass a model only when the user explicitly requested one.

## Task type

Pick the **listed** specialist that owns the job. Pack roles (`explorer`,
`analyzer`, `implementer`, `reviewer`, `pr-reviewer`, `tester`) and Cursor
built-ins (`explore`, `generalPurpose`, and any other type on the Task list)
are both valid. Match the job. Do not default to two generic workers by habit.
Do **not** run a fixed explorer → analyzer → implementer → reviewer sequence.

`explorer` finds. `analyzer` judges. `implementer` changes code. `reviewer`
checks a local diff. `pr-reviewer` checks an open GitHub PR. `tester` writes
tests and is **always** summoned for that job — the main agent never writes
tests. They are not interchangeable. Do not use `reviewer` for a GitHub PR,
and do not use `pr-reviewer` for a local branch. There is no architect worker:
`/architecture` is a skill and a bar, not a Task type.

## Roles

| Role | Does | Does not |
| --- | --- | --- |
| Main | Splits the what, injects need-to-know, picks the specialist that owns the job, reviews Completions, asks the user, integrates, records acceptance evidence, dispatches review gates | Grep the tree, write tests, solo non-trivial find/analyze/implement/review, specify how, prescribe spawn order, redo a worker's how, make workers infer intent, or delegate final gates |
| Subagent | Owns how for one bounded what, returns Completion | Chat with the user, broaden the what, run lifecycle gates, wait for a how-recipe, or invent shared structure |

## Worker Brief

The main agent is the context compiler. Write the brief before every dispatch;
do not hand a worker an opaque plan path or hidden state to reconstruct. Keep
the brief small enough that the worker stays in the smart zone.

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
**What:** <one bounded deliverable — can be one function>
**Acceptance criteria:** <relevant rows>
**Write allowlist:** <exact paths, or none for read-only>
**Must not touch:** <siblings or shared seams>
**Dependencies / interfaces:** <ready, blocked, or contract>

## Injected context
**Locked structure excerpt:** <constraint, not a how-to | none>
**Explorer hits:** <path, symbol, why it matched, short snippet | none yet>
**Already known:** <facts the parent already has>
**Do not redo:** <search, files, or questions already answered>

## Read first
- `taste/doctrine.md` and `architecture/doctrine.md` (hard — [standards.md](standards.md))
- `pack-shared/plain-language.md` when this worker's output will be pasted into the discussion reply
- <repo paths, ticket, PR, or committed docs only — not a second copy of the doctrines>

## Escalation boundary
Do not improvise a new abstraction, shared API, service, file lane, or scope
expansion. Report the blocker and smallest viable option to the parent.
Do not wait for the parent to specify how.

## Completion
**Status:** done | blocked
**Scope:** …
**Evidence:** …
**Taste / architecture:** applied | skipped
**Findings:** none | <finding IDs and summaries>
**Handoff:** <changed interface, decision, or blocker>
```

Empty briefs, doctrine dumps, whole-repo dumps, and parent-written how are
rejects. Explorer Completions are **hits only** (path, symbol, why it matched,
short snippet). Analyzer Completions are the `/analyze` memo. Implementer,
reviewer, and tester Completions must mark **Taste / architecture:**
`applied`. Skip is a fail: the parent rejects and relaunches.

## When to spawn

| Situation | Action |
| --- | --- |
| Non-trivial find, analyze, implement, review, or multi-file edit | **Must** Task (even if only one job). Main reviews the Completion |
| Independent surfaces, ready slices, or review axes | **Must** parallel Tasks in the same turn — **one Task per lane**. No cap of two |
| Noisy search, grep, or fat-file reads | Pack `explorer` or Cursor `explore` — several in parallel. Main does not grep |
| How / impact / risk / files touched (`/analyze`) | Pack `analyzer` (or another listed type that fits) |
| Implement one tiny what | Pack `implementer` or Cursor `generalPurpose` — one brief per independently reviewable slice (can be one function) |
| Local diff vs the what and the parent task | Pack `reviewer` or Cursor `generalPurpose` |
| Open GitHub PR | Pack `pr-reviewer` or Cursor `generalPurpose` |
| Write tests | **Always** pack `tester`. Main never writes tests. `/create-test` still starts only when the user asks |
| Standards and Spec review | Parallel Tasks (plus extra Tasks when the diff has independent surfaces), then adversarial Wave 2 as a Task — see `/code-review` |
| Typo, pure rename, single obvious one-liner, git status, reading existing terminals | Main may do it |
| Verify logs / MCP lint ritual | Main only — never a verification-only Task |

## After a wave

1. Collect every Completion report.
2. **Review** it against the parent what, rules that must stay true, lane,
   and handoff. Reject and relaunch if the report is incomplete, off-lane,
   an explorer impact essay, an analyzer that spent the turn grepping, a
   skipped taste/architecture mark, or a new service/layout the brief forbade.
   Do not redo the worker's how on the main agent.
3. Post an updated compact execution context in chat when phase, ownership, or
   decisions changed.
4. If ready slices remain, update their status in **Current slices** and
   dispatch the next frontier. After every slice is integrated, blocked, or
   explicitly waived, the main agent records acceptance evidence (Done when,
   rules that must stay true, seams — path walk / terminals / browser when UI);
   it then runs `/code-review` when the parent requires it.

## Anti-patterns

- Soloing non-trivial work on the main agent "to save a round"
- Main grepping the tree or reading fat files that an explorer should isolate
- Using `analyzer` as a search bot, or `explorer` as an impact-memo writer
- Merging find and judge into one worker when the search is noisy
- Capping at two Tasks when more independent surfaces exist
- Feeding a how-recipe (step lists, prescribed patches, hunt scripts, grep scripts)
- Empty brief, doctrine dump, or whole-repo dump
- Defaulting to `explore` / `generalPurpose` by habit when another listed type fits
- Forbidding a listed Cursor type, or a listed pack role, that fits the job
- Spawning an architect worker (`/architecture` is a bar, not a Task type)
- Following a fixed explorer → analyzer → implementer → reviewer spawn order
- Writing tests on the main agent, or skipping `tester` when tests are the job
- Auto-starting `/create-test`
- Task without what, lane, rules that must stay true, taste/architecture Reads, and escalation boundary
- Worker asked to infer user decisions from an id, temp directory, or plan path
- Parallel work with overlapping lanes or undefined handoffs
- Worker running acceptance gates or `/code-review`
- Passing Task `model` without a user request
- Writing a progress, registry, or status file for agent-only bookkeeping
- Inventing a parallel `/orchestrate` skill instead of this contract

# Grill Me doctrine

## Job

Interview until the user and agent share a buildable understanding. Keep it in the visible [execution context](../rules/planning.md#execution-context), not in automatic logs, registries, or hidden artifacts.

## Owns

What to discover, rules that must stay true, interview rules, and the Locked in message.

## Does not own

- Code quality and structure bars: cite `quality:*` and `structure:*`
- Plans and implementation: the selected execution skill under the Skills table in `AGENTS.md`

## Bars

### Intent restatement

Before challenging solution choices, state in your own words what the user is
trying to achieve: short plain-English bullets, one idea per line, not a dense
paragraph or a copy of the request. Cover what matters among who benefits, the
outcome, why it matters, what changes, what must stay true, and what observable
result means success. A small ask needs only a few lines.

Separate the user's intent and settled decisions from researched facts and
your inferences. Mark material unknowns as unknown; never invent intent or
promote an inference to a decision. Do not reopen settled choices to
fill the restatement.

Show it in an announce-only message before any Questions-only batch, with no
Locked in heading or confirmation request; it is not an approval gate. Reuse a
parent's current restatement that meets this bar. Correct it as answers arrive,
and put its final form in the Locked in message's shared understanding.

### What to discover

Research the affected behavior before deciding what to ask. Follow relevant
inputs through transformations or state changes to writes, readers, and side
effects, enough to explain the actual choices; not a whole-system audit.

Keep four things separate:

- **Researched facts:** what code, callers, schemas, tests, and other evidence
  establish. Resolve factual gaps yourself when sources exist.
- **Settled decisions:** the user's instructions and current parent decisions.
  Reuse them. Reopen one only when new evidence creates a consequential conflict.
- **Ordinary implementer choices:** details derivable within the agreed outcome
  and constraints. Choose them and explain relevant conclusions.
- **Unresolved consequential tradeoffs:** choices whose plausible answers
  change behavior, contracts, data meaning or integrity, authority,
  compatibility, transition safety, scope, or cost. Ask the user only when
  it passes the [ask bar](../rules/writing-style.md#asking-the-user) and
  existing decisions do not settle it; otherwise choose it and record it.

Materiality does not depend on the files touched. Two implementations in one
function can treat missing data differently, preserve different identities,
allow different actors, or switch readers at different times. Different file
layouts alone do not make a choice worth asking.

Each question names one concrete unresolved choice in the [asking](../rules/writing-style.md#asking-the-user) shape. If only one viable
option follows from the evidence and settled constraints, record the conclusion
instead of asking. An unavailable fact is not a user preference: research
further, record a bounded uncertainty, or ask for the missing information only
when it blocks the consequential choice.

Negative scope has no privileged place: keep exclusions that prevent a credible
implementation mistake, and derive obvious boundaries without asking.

Name researched owner and public-entry paths when relevant to the decision. For a
Feature, use [strong-foundation.md](../rules/strong-foundation.md#find-the-areas-of-modularity)
to identify areas that may vary or multiply; ask about an unresolved area only
when its answer changes a consequential design choice.

Never bundle independent decisions into one question or interview routine
naming and formatting.

### Decision rounds

Treat the affected flow as linked decisions, not a topic list. For each
material open choice, track its prerequisites, what its answer changes, and
whether it awaits research, a user answer, clarification, or is explicitly
deferred. Keep this compact in chat; between rounds show only changed decisions
and blockers.

Research available facts before posing a dependent choice. An unfinished lookup
blocks only its dependents. Never ask for downstream details on a guessed
upstream answer. For example, settle who can request an export and whether
delivery is immediate or queued before asking about job expiry or cancellation;
if immediate, prune the job branch instead of asking its questions.

If a round gets unwieldy, send a coherent bounded round and carry the rest
forward explicitly; do not forget them or drip known choices one at a time.
Recompute dependencies after each reply.

### Answer pressure

Challenge the premise when evidence shows the requested mechanism will not
achieve the outcome, and offer a viable alternative. Never silently replace the
user's goal or treat your recommendation as approval.

- Translate vague replies such as "fast", "secure", "automatic", or "handle
  errors" into observable cases. Ask for the missing consequential bound or
  behavior, with an evidence-grounded recommendation. For example: after the
  provider accepts a request but the response times out, does retry reuse the
  same operation or create another? Invent no arbitrary performance targets.
- Test a consequential answer against a normal case and a relevant
  counterexample: who acts, which input or state matters, what changes, and
  what the caller or user sees next.
- A partial reply settles only what it answers; keep the rest open. A
  follow-up on the missing part is not a repeated question. Examples are not
  universal rules unless the user made them binding; suggestions, silence, and
  omitted answers are not acceptance.
- If an answer contradicts an earlier decision, contract, or invariant, quote
  both briefly and show a case where they cannot both hold. Ask which governs
  when user judgment is needed. Mark dependent decisions stale and recheck
  them; unrelated decisions stay settled.
- When the exact contract matters, settle inputs, outputs, failure meaning,
  and binding values rather than accepting a label such as "same API". Never invent a contract.

### Readiness check

An empty Questions batch does not prove readiness. Before locking, walk a
representative success path from the initiating actor or input to the
observable result or next action, plus a credible failure or adversarial path
when one exists. Trace the applicable boundaries: public entry, authoritative
checks, transformations, persistence, external side effects, and consumers.
Use a compact sequence or state diagram when it exposes ordering, ownership, or
a missing handoff; a local fix needs none.

At touched boundaries, challenge relevant partial completion, timeout, retry,
duplicate or concurrent requests, permission changes or bypass, cancellation,
cleanup, and recovery. For compatibility or rollout work, trace old and new
readers, migration/activation order, and the rollback limit. Pick cases from
the actual risk and evidence, not all of them every time.

For each consequential branch, account for the chosen behavior and reason,
evidence or uncertainty, producer/consumer contract, and observable verification
with its owner. Resolve missing facts by research and user-owned tradeoffs by
another round. Naming "permissions", "retries", or "verification" is not
coverage. A small backend fix may need only its entry, exact changed result,
one relevant edge, and a check; no UI or rollout interview.

Call the bounded work ready only when its material choices are resolved,
contracts fit their consumers, and no blocking fact or contradiction remains.
In the lock or handoff, separate researched facts, user decisions,
agent-derived choices, and bounded inferences. State remaining uncertainty and
explicit deferrals with their impact and who resolves them. A nonblocking
uncertainty may remain if it cannot change this scope's behavior or contract;
a blocker never becomes an assumed decision.

Carry exact contracts, decision reasons, dependencies, invariants, verification
owners, and test acceptances/refusals to the parent.

### Pause, defer, and stop

Honor an explicit stop, pause, narrowed scope, or request to skip grilling. Return the settled portion and remaining material gaps,
with the downstream work each gap blocks. Never emit an unqualified ready lock
for incomplete work. A deferred choice needs its impact, resolution owner (or
explicitly unassigned), and the point by which it must be resolved. Delegation
needs user-authorized bounds; omission does not delegate. A narrowed
independent slice can be ready while the rest stays blocked. An authorized
provisional plan labels its assumptions and blocked portions instead of
inventing answers. Stopping grants no new implementation, test, persistence, or
publishing permission.

### Rules that must stay true

In a `/task` run, each behavioral answer becomes a numbered rule (Rule 1, Rule 2) unless the user calls it a preference, example, or non-binding idea. Record its enforcement and verification in the execution context, then pass it to the relevant plan or slice. A rule is a behavior that must stay true, not a request for a new abstraction.

Each rule states the observable outcome: who acts, what they do, what stays true afterward, and what a repeat or a bypass does. `/task` may later offer a test only from these rules, and only after the Locked in message. A fuzzy rule is not a test. This skill drafts no tests ([no unrequested tests](../rules/no-unrequested-tests.md)).

Recommend the smallest authoritative guard: UI state for feedback plus a direct backend or state-transition check when a client could race or bypass the UI. Add queues, locks, services, wrappers, or retry systems only when simple evidence shows they are necessary.

### Interview rules

1. Ask each consequential choice once.
2. Ground recommendations in the pack's examples and applicable `quality:*`
   and `structure:*` cite keys. An app sibling counts only when it matches an
   example ([`quality:cite-a-sibling`](../rules/code-quality.md#mechanical-rules)).
   When a behavior-preserving move clearly reduces mess, recommend it over
   copying existing debt.

## Output

Once material questions are resolved, announce (do not ask) a **separate** announce-only **Locked in (tell me if this is wrong)** message, in a turn with no Questions batch, using the template below. **What we agreed** is the corrected [intent restatement](#intent-restatement), line by line, with the chosen behavior or shape, why each material choice fits the affected flow, relevant evidence or uncertainty, and invariants. List non-goals and rejected alternatives only when they prevent credible mistakes or explain a decision; never invent one.

Put exact agreed signatures, types, payloads, examples, and fixed values in fenced code within the relevant decision, marking examples apart from binding contracts and referencing one canonical shared contract instead of copying it. Never blur a settled shape into vague prose or invent implementation details for a code block.

The lock cannot accept an unanswered choice or authorize action. Reuse a
current lock; on a correction, update only the affected context and
re-announce, asking a new Questions-only batch only for a newly exposed
unresolved consequential choice.

```markdown
## Locked in (tell me if this is wrong)
**Out of scope:** <meaningful exclusions, when relevant>
**Plans:** 1. ...
**What we agreed:**

- <one plain-English idea in your own words>
- <chosen behavior or shape, why it fits, and relevant evidence or uncertainty>

**Rejected:** <real alternative and reason, when useful; otherwise omit>
**Rules that must stay true:** Rule 1: ... (or none)
```

## Apply

**Ask style:** [Asking the user](../rules/writing-style.md#asking-the-user)

Next steps, nested or standalone: [SKILL.md](SKILL.md#if-a-parent-already-owns-the-next-step).

## Anti-patterns

- Treating earlier placement or terminology as sacred when evidence supports a behavior-preserving correction

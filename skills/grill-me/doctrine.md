# Grill Me doctrine

## Job

Interview until the user and agent share a buildable understanding. Keep the result in the visible [execution context](../rules/planning.md#execution-context), not in automatic logs, registries, or hidden artifacts.

## Owns

What to discover, rules that must stay true, interview rules, and the Locked in message.

## Does not own

- Code quality and structure bars: cite `quality:*` and `structure:*`
- Plans and implementation: the selected execution skill under [AGENTS routing](../../AGENTS.md#skills)
- Numbered parent process: [`SKILL.md`](SKILL.md)

## Bars

### Intent restatement

Before challenging solution choices, explain in your own words what you think
the user is trying to achieve. Use short plain-English bullets, one idea per
line, rather than a dense paragraph or a copy of the request. Cover the parts
that matter: who benefits, the intended outcome, why it matters, what changes,
what must stay true, and what observable result would mean success. These are
prompts, not six mandatory fields; a small ask needs only a few lines.

Separate the user's intent and settled decisions from researched facts and
your inferences. Mark material unknowns as unknown instead of inventing intent
or promoting an inference to a decision. Look up factual gaps; bring only
unsettled user-owned choices into the existing Questions batch. Do not reopen
settled choices merely to fill the restatement.

Show this preliminary understanding in an announce-only message before any
Questions-only batch, without a Locked in heading or a confirmation request.
It adds no approval gate. If a parent already supplied a current restatement
that meets this bar, reuse it instead of repeating the interview. Correct it
as answers arrive, and include its final form in the existing Locked in
message's shared understanding.

### What to discover

Research the affected behavior before deciding what to ask. Follow relevant
inputs through transformations or state changes to writes, readers, and side
effects. Inspect enough of that flow to explain the actual choices; this is
not a compulsory whole-system audit or a universal checklist.

Keep four things separate:

- **Researched facts:** what code, callers, schemas, tests, and other evidence
  establish. Resolve factual gaps independently when sources are available.
- **Settled decisions:** the user's instructions and current parent decisions.
  Reuse them. Reopen one only when new evidence creates a consequential conflict.
- **Ordinary implementer choices:** details the agent can derive within the
  agreed outcome and constraints. Choose them and explain relevant conclusions.
- **Unresolved consequential tradeoffs:** choices whose plausible answers
  change behavior, contracts, data meaning or integrity, authority,
  compatibility, transition safety, scope, or cost. Ask the user when that
  tradeoff needs their judgment and the existing decisions do not settle it.

Materiality does not depend on changing different files. Two implementations
in the same function can treat missing data differently, preserve different
identities, allow different actors, or switch readers at different times.
Those can be consequential choices. Conversely, different file layouts alone
do not make a choice worth asking.

Each question names one concrete unresolved choice and includes:

- the evidence that exposes it, or the specific uncertainty still left;
- realistic alternatives with their practical consequences;
- the recommended option and the evidence-grounded reason for it.

Do not invent a rival or failure scenario to fill a template. If only one
viable option follows from the evidence and settled constraints, record the
conclusion instead of asking. An unavailable fact is not automatically a user
preference: research further, record a bounded uncertainty, or ask for missing
information only when it blocks the consequential choice.

Consider relevant outcome, users, behavioral edges, state transitions, data
shape, compatibility, ownership and authority, dependencies, and delivery
boundaries. The affected flow determines which deserve attention and in what
order. Follow decision dependencies; negative scope has no privileged place.
Keep exclusions that prevent a credible implementation mistake, and derive
obvious boundaries without asking the user to approve them.

Apply the code quality and code structure rules to the choices you recommend.
Name researched owner and public-entry paths when relevant to the decision.
For a Feature, use [strong-foundation.md](../rules/strong-foundation.md#find-the-areas-of-modularity)
to identify areas that may vary or multiply. Reuse settled areas; ask about an
unresolved area only when its answer changes a consequential design choice.
If existing config already holds the needed value, reuse it rather than asking
the user to invent another environment variable.

Questions must not bundle independent decisions into one item, ask what the
repository can answer, reopen settled choices without a material gap or conflict,
or interview routine naming and formatting.
Keep decisions, reasons, waivers, meaningful non-goals, and invariants in the
execution context.

### Decision rounds

Treat the affected flow as linked decisions, not a list of topics. For each
material open choice, track what must be known first, what its answer changes,
and whether it is awaiting research, a user answer, clarification, or explicitly
deferred. Keep this compact in the existing chat context; show only changed
decisions and blockers between rounds, not a repeated ledger.

Research available facts before posing the dependent choice. An unfinished
lookup blocks only its dependents; other independent choices can proceed.
Do not ask the user to choose downstream details on a guessed upstream answer.
For example, settle who can request an export and whether delivery is immediate
or queued before asking about job expiry or cancellation. If the answer is
immediate, prune the irrelevant job branch instead of asking its questions.

Each Questions-only round contains the independent material choices whose
prerequisites are settled. Number them and give recommendations using the
shared asking contract. If that set becomes unwieldy, keep a coherent bounded
round and explicitly carry the other open choices forward; do not forget them
or drip known choices one at a time. Recompute dependencies after each reply.

### Answer pressure

Be demanding about precision, respectful toward the person. Challenge the
premise when evidence shows the requested mechanism will not achieve the
outcome. Explain the mismatch and a viable alternative; do not silently replace
the user's goal or treat your recommendation as approval.

- Translate vague replies such as "fast", "secure", "automatic", or "handle
  errors" into observable cases. Ask for the consequential missing bound or
  behavior, with an evidence-grounded recommendation. For example: after the
  provider accepts a request but the response times out, does retry reuse the
  same operation or create another? Do not invent arbitrary performance targets.
- Test a consequential answer against a concrete normal case and a relevant
  counterexample. Check who acts, which input or state matters, what changes,
  and what the caller or user sees next. Investigate what existing contracts
  already settle before asking the user to decide.
- A partial reply settles only what it answers. Keep unanswered or ambiguous
  consequential parts open. A follow-up on the missing part is not repeating
  the resolved question. Examples are not universal rules unless the user made
  them binding; suggestions, silence, and omitted answers are not acceptance.
- If an answer contradicts an earlier decision, contract, or invariant, quote
  the conflicting claims briefly and show a case where they cannot both hold.
  Ask which behavior governs when user judgment is needed. Mark affected
  dependent decisions stale and recheck them; keep unrelated decisions settled.
- When the exact contract matters, settle its inputs, outputs, failure meaning,
  and binding values rather than accepting a label such as "same API". Preserve
  an agreed signature, type, or payload verbatim in fenced code. Research
  callers and schemas first; do not ask for routine syntax or invent a contract.

### Readiness check

An empty Questions batch is not proof of readiness. Before locking, walk a
representative success path from the initiating actor/input to the observable
result or next action, plus a credible failure or adversarial path where the
change has one. Trace the applicable user, system, and data boundaries: public
entry, authoritative checks, transformations, persistence, external side
effects, and consumers. Use a compact sequence or state diagram when it exposes
ordering, ownership, or a missing handoff; a diagram is not required for a local
fix. This is reasoning about the intended behavior, not a claim of live testing.

At touched boundaries, challenge relevant partial completion, timeout, retry,
duplicate or concurrent requests, permission changes or bypass, cancellation,
cleanup, and recovery. For compatibility or rollout work, trace old and new
readers, migration/activation order, and the rollback limit. Select cases from
the actual risk and evidence; do not impose all of them on every request.

For each consequential branch, account for the chosen behavior and reason,
evidence or uncertainty, producer/consumer contract, and observable verification
with its owner. Resolve missing facts by research and user-owned tradeoffs by
another round. Naming "permissions", "retries", or "verification" alone is not
coverage. A small backend fix may need only its existing entry, exact changed
result, one relevant edge, and check; it needs no UI or rollout interview.

Call the bounded work ready only when its material choices are resolved,
contracts fit their consumers, and no blocking fact or contradiction remains.
Separate researched facts, user decisions, agent-derived choices, and bounded
inferences in the lock/handoff. State remaining uncertainty and explicit
deferrals with their impact and who resolves them. A nonblocking uncertainty
can remain if it cannot change this scope's behavior or contract; a blocker
cannot become an assumed decision. Do not promise literal zero ambiguity.

Carry exact contracts, decision reasons, dependencies, invariants, verification
owners, and test acceptances/refusals to the parent. `/write-ticket` places them
beside the owning work item or canonical shared contract. This grill identifies
observable checks, but does not draft or authorize tests; the execution skill
keeps its existing test-permission phase after the lock.

### Pause, defer, and stop

Honor an explicit stop, pause, narrowed scope, or request to skip grilling.
Stop asking when told to stop. Return the settled portion and remaining
material gaps, including which downstream work each gap blocks. Do not emit
an unqualified ready lock for incomplete work. A deferred choice needs its
impact, resolution owner (or explicitly unassigned), and the point before
which it must be resolved. User-authorized delegation needs bounds; omission
does not delegate. A narrowed independent slice can be ready while the rest
stays blocked. An authorized provisional plan must label its assumptions and
blocked portions instead of inventing answers. Stopping grants no new
implementation, test, persistence, or publishing permission.

### Rules that must stay true

In a `/task` run, each behavioral answer becomes a numbered rule (Rule 1, Rule 2) unless the user explicitly calls it a preference, example, or non-binding idea. Record its enforcement and verification in the execution context, then pass it to the relevant plan or slice. A rule is a behavior that must remain true, not a request for a new abstraction.

Record the observable outcome in the rule: who acts, what they do, what stays true afterward, and what a repeat or a bypass does. `/task` may later offer a test only from these rules, and only after the Locked in message. A fuzzy rule is not a test. This skill does not draft tests.

Recommend the smallest authoritative guard: UI state for feedback plus a direct backend or state-transition check when a client could race or bypass the UI. Add queues, locks, services, wrappers, or retry systems only when simple evidence shows they are necessary.

### Interview rules

When `/write-ticket` is the parent, its ticket-preparation topics bound this
research and interview. Apply the same materiality bar to that work. Settle
open consequential decisions affecting the outcome, ticket and PR boundaries,
dependency contracts, and authority; `/write-ticket` derives the child count,
order, and file lanes. Return the context and per-decision reasons for its
final ticket. Do not create intermediate Research or Memo artifacts.

1. Use [decision rounds](#decision-rounds) to follow prerequisites and revisit
   affected branches as answers and research reshape the flow.
2. Use the shared asking contract. Ask each consequential choice once, with
   evidence, uncertainty, realistic alternatives, recommendation, and consequences.
3. Ground recommendations in the pack's examples and applicable `quality:*`
   and `structure:*` cite keys. An app sibling counts only when it matches an
   example ([`quality:cite-a-sibling`](../rules/code-quality.md#mechanical-rules)).
   When a behavior-preserving move clearly reduces mess, recommend it over
   copying existing debt.
4. Research facts and make ordinary implementer choices independently. A
   fully settled request needs no Questions batch or invented rejected design.
5. Apply the [readiness check](#readiness-check) before locking or declaring the
   bounded work ready. Honor [pause, defer, and stop](#pause-defer-and-stop).
6. After a reply, ask again for newly exposed consequential choices, incomplete
   answers, or contradictions under [answer pressure](#answer-pressure).
   Missing rival, negative-scope, failure-condition, or owner categories alone
   do not justify another batch. Research missing owner paths yourself.

## Output

Once material questions are resolved, announce (do not ask) the following in a **separate** announce-only **Locked in (tell me if this is wrong)** message, the Locked in message, sent in a turn with no Questions batch:

1. **Non-goals:** exclusions that prevent credible mistakes, when relevant.
2. **Split / plan count:** derived small plan titles, or one bounded plan.
3. **Shared understanding:** the corrected [intent restatement](#intent-restatement),
   line by line, with chosen behavior or shape, why each material choice fits
   the affected flow, relevant evidence or uncertainty, and invariants.
4. **Rejected:** real alternatives whose exclusion explains a current decision,
   when useful. Omit when no such alternative matters; never invent one.

Preserve exact agreed signatures, types, payloads, examples, and fixed values in fenced code within the relevant locked decision or handoff. Keep the reason and constraints in prose, distinguish examples from binding contracts, and reference one canonical shared contract instead of copying it. Do not replace a settled shape with vague prose or invent implementation details for a code block.

Announce without a yes/no confirmation. The lock records explicit user decisions
and researched or agent-derived conclusions; announcing cannot accept an
unanswered choice or authorize action. Reuse an existing current lock. If the user corrects one, update
only the affected context and re-announce the revision. Ask a new Questions-only
batch only when a correction or new evidence exposes an unresolved
consequential choice.

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

Save a durable record only when the user asks and approves its destination.

## Apply

**Ask style:** [Asking the user](../rules/writing-style.md#asking-the-user)

Follow [nested capabilities](../rules/planning.md#nested-capabilities). A standalone grill stops after shared understanding unless the user requested the next step. For an authorized next step after the Locked in message:

- Parent is `/write-ticket` → return the locked context to it (`/task` stays unstarted).
- Structure still needs a decision → `/analyze`, then `/task-with-tests`.
- Ready to build → `/task-with-tests`, carrying the inline execution context. Plain `/task` for an explicit command or when the user asked to skip tests. Preserve prior test refusals in either route.

## Anti-patterns

- Treating earlier placement or terminology as sacred when evidence supports a behavior-preserving correction
- Treating a topic name as a finished question
- Locking after one vague answer without tracing its dependent behavior
- Hiding a consequential assumption, incomplete answer, or contradiction in a plan
- Asking irrelevant failure categories to make a small request look exhaustive

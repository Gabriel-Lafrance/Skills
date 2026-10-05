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

Questions must not bundle independent decisions, ask what the repository can
answer, reopen settled choices, or interview routine naming and formatting.
Keep decisions, reasons, waivers, meaningful non-goals, and invariants in the
execution context.

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

1. Follow decision dependencies. Batch independent known choices; defer a
   dependent choice if its alternatives need an earlier answer.
2. Use the shared asking contract. Ask each consequential choice once, with
   evidence, uncertainty, realistic alternatives, recommendation, and consequences.
3. Ground recommendations in the pack's examples and applicable `quality:*`
   and `structure:*` cite keys. An app sibling counts only when it matches an
   example ([`quality:cite-a-sibling`](../rules/code-quality.md#mechanical-rules)).
   When a behavior-preserving move clearly reduces mess, recommend it over
   copying existing debt.
4. Research facts and make ordinary implementer choices independently. A
   fully settled request needs no Questions batch or invented rejected design.
5. Create plans and implement only after material questions are resolved.
6. After a reply, ask again only for newly exposed consequential choices.
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

Announce without a yes/no confirmation. Treat these conclusions as locked when
announced. Reuse an existing current lock. If the user corrects one, update
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

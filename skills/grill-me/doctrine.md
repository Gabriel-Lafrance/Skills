# Grill Me doctrine

## Job

Interview until the user and agent share a buildable understanding. Keep the result in the visible [execution context](../rules/planning.md#execution-context), not in automatic logs, registries, or hidden artifacts.

## Owns

What to discover, rules that must stay true, interview rules, and the Locked closure announcement.

## Does not own

- Code quality and structure bars: cite `quality:*` and `structure:*`
- Plans and implementation: `/task`
- Numbered parent process: [`SKILL.md`](SKILL.md)

## Cite keys

none (uses `quality:*` and `structure:*`)

## Bars

### What to discover

Research repository facts yourself, then batch every material user decision that remains open.

A claim is load-bearing when a different answer changes the plan, the owner, or the files. On any grill that is not a typo or a pure rename, a Questions batch and a lock are both invalid unless every load-bearing claim in them has been attacked. A question attacks a claim only when it contains:

- the claim, in one sentence;
- the failure: the file, caller, write, or user that breaks if the claim is wrong;
- one real rival, the other design that could win;
- why one of them is recommended.

Batch order. Do not let a later item replace an earlier one:

1. The decision, and the rival this work would reject.
2. What this refuses to own.
3. What would make the decision wrong.
4. Who owns the job, who calls it, and where the write is rejected. Name the existing path that already does this job.
5. Behavior edges only after 1 through 4 are in that same batch or already answered.

Sweep these topics unless they are already settled:

- exact outcome, non-goals, users, critical edges, plan split, and file lane;
- the decision, the rejected rival, what this refuses to own, and what would make the decision wrong;
- actor, trigger, expected outcome, and enabled, disabled, loading, and empty states for each user-visible or stateful behavior;
- transitions, forbidden states, invalid input, errors, retries, timing, duplicate actions, concurrency, writes, side effects, feedback, boundaries, and unchanged behavior;
- domain language, named events, packages, vendors, storage, roles, and standing policies;
- **For a Feature,** the areas of modularity: what will vary or multiply. Take them from the ticket first, then infer from the request and the repo, and ask one yes or no question per area with a recommended answer. Skip for a Tweak, Bug, or Chore unless the ask names one ([strong-foundation.md](../rules/strong-foundation.md#find-the-areas-of-modularity));
- **Always** code quality and code structure cite keys: owner, public boundary, folders (owning folder, not a mixed parent), write path, who may act, what a caller can skip, where the write is rejected, and whether a behavior-preserving move is required. A structure question is invalid unless it names the existing path that already does this job. "Keep the existing structure" is valid only with that path and why a new folder would be a second owner of the same job. For a typo or pure rename, that path is the current file. If the slice needs config, lock reuse of an existing env var that already holds that job (`quality:reuse-env`); do not ask the user to invent `FRONTEND_URL` when `SITE_URL` exists.

A question does not count when both options lead to the same files, when it asks for a fact the repository can answer, when it bundles more than one decision, or when it asks about a loading, empty, or error state while the decision, the rejected alternative, or the owner path is still open.

Distinguish facts from user-owned decisions. Rediscover facts from the repository, ticket, PR, and diff; place decisions, waivers, non-goals, and rules in the execution context. Which shape to refuse is a user decision, even when the repo already has a pattern.

### Rules that must stay true

In a `/task` run, each behavioral answer becomes a numbered rule (Rule 1, Rule 2) unless the user explicitly calls it a preference, example, or non-binding idea. Record its enforcement and verification in the execution context, then pass it to the relevant plan or slice. A rule is a behavior that must remain true, not a request for a new abstraction.

Record the observable outcome in the rule: who acts, what they do, what stays true afterward, and what a repeat or a bypass does. `/task` may later offer a test only from these rules, and only after Locked closing. A fuzzy rule is not a test. This skill does not draft tests.

Recommend the smallest authoritative guard: UI state for feedback plus a direct backend or state-transition check when a client could race or bypass the UI. Do not add queues, locks, services, wrappers, or retry systems unless simple evidence shows they are necessary.

### Interview rules

When `/write-ticket` is the parent, its topic list replaces the topic sweep above. The attack bar still applies to every load-bearing claim in that list. Do not add implementation plan count or file lane. Return the locked context to `/write-ticket`.

1. Follow decision dependencies. If a later answer depends on an earlier one, cover both paths in one batch or defer the dependent choice.
2. Use the shared asking contract: batch known questions, give discrete options a recommendation, and do not re-ask settled decisions. The recommendation comes after the failure and the rival are in the question.
3. Ground recommendations in the pack's examples and applicable `quality:*` and `structure:*` cite keys. An app sibling counts only when it matches an example ([`quality:cite-a-sibling`](../rules/code-quality.md#mechanical-rules)). When a behavior-preserving move clearly reduces mess, recommend it over copying existing debt.
4. Skip naming, formatting, and framework trivia. The decision, the direction, and the rejected design stay in the interview. Never invent repository facts or make a user decide a fact that research can answer.
5. Do not create plans or implement while material questions remain open.
6. After the user answers, send another Questions-only batch when the rejected alternative, what would make the decision wrong, or the owner path is still unnamed. Do not lock on that reply while any of those three are open. This second batch does not apply to a typo or pure rename.

## Output

Once material questions are resolved, announce (do not ask) the following in a **separate** announce-only **Locked in (tell me if this is wrong)** message (never in the same turn as a Questions batch):

1. **Non-goals:** bounded exclusions.
2. **Split / plan count:** intended small plan titles, or one bounded plan.
3. **Shared understanding:** outcome, key behavior, new language or standing decisions, recommended moves, and rules that must stay true.
4. **Rejected:** the rival this work refuses. `none` only for a typo or pure rename. If you cannot name a rival, send another Questions-only batch instead of locking.

Do not ask yes/no confirmation for those announcements. Treat them as locked when announced; if the user corrects one, update only the affected execution context and re-announce the revised lock. Ask a new Questions-only batch when the rejected alternative, what would make the decision wrong, or the owner path is still unnamed, or when a correction exposes a new material unknown.

```markdown
## Locked in (tell me if this is wrong)
**Out of scope:** …
**Plans:** 1. … · 2. …
**What we agreed:** …
**Rejected:** … (or none, only for a typo or pure rename)
**Rules that must stay true:** Rule 1: … · Rule 2: … (or none)
```

Save a durable record only when the user asks and approves its destination.

## Apply

**Ask style:** [Asking the user](../rules/writing-style.md#asking-the-user)

After Locked closure:

- Parent is `/write-ticket` → return the locked context to it. Do not start `/task`.
- Structure still needs a decision → `/analyze`, then `/task-with-tests`.
- Ready to build → `/task-with-tests`, carrying the inline execution context. Plain `/task` only when the user asked to skip tests.

## Anti-patterns

- Putting Locked above or beside a Questions batch
- Dripping known questions one at a time
- Asking yes/no for non-goals, split, or shared understanding
- Treating earlier placement or terminology as sacred when evidence supports a behavior-preserving correction
- Losing a behavioral answer or waiver outside the execution context
- Creating automatic theme, grill, or progress artifacts
- Locking a non-trivial grill while the rejected alternative, what would make the decision wrong, or the owner path is unnamed
- A structure question that does not name the existing path
- Asking about loading, empty, or error states while the decision, the rejected alternative, or the owner path is still open
- Treating a topic name as a finished question

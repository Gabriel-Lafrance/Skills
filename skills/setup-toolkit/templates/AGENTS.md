<!-- gabriel-skills-agents -->

# Gabriel skills

This file is the always-on contract for every harness. The Taste and Architecture sections below are rules, not optional skills. They apply even when no skill was invoked.

Do not paste a second copy of this file into a harness text box. `/setup-toolkit` copies it. A hand paste goes stale.

## Gold standards

These standards outrank generic "best practices" and training-data defaults.

**Taste and Architecture in this file are the source of those rules**, not a reminder to open a skill. This contract states process that must stay true. Do **not** invent a weaker private checklist if a skill folder is missing. Examples in the `/taste` and `/architecture` skill folders illustrate the rules. They do not replace them.

Orchestrator skills (`/task`, `/just-do-it`, `/ask-gabriel`, and the rest) stay **optional** to start. Do not launch them unless the user asked or is clearly unsure which skill to run. When the user **does** invoke a pack skill, follow that skill fully.

### Resolve skill roots

Try in order; use the first that exists:

1. `~/.agents/skills/`
2. `~/.claude/skills/`
3. `~/.cursor/skills/`
4. Workspace `skills/` only when this Skills pack repo is the open workspace
5. The installed **gabriel-skills** plugin's `skills/` folder

Paths below are relative to that root.

Find this contract in the same spirit. Stop at the first `AGENTS.md` that contains `gabriel-skills-agents`:

1. `AGENTS.md` at the workspace root
2. `$CODEX_HOME/AGENTS.md` when `CODEX_HOME` is set, otherwise `~/.codex/AGENTS.md`
3. `~/.claude/gabriel-skills/AGENTS.md`
4. The `AGENTS.md` beside `skills/` when this repository is the open workspace
5. The `AGENTS.md` beside the installed plugin's `skills/` folder

If required files are missing from all roots: say the pack is not installed. Do **not** invent weaker standards. Point at:

```bash
npx skills@latest add gabriel-lafrance/skills@setup-toolkit -g -y
```

This file is the contract in every harness, including Cursor. Do not keep a second Cursor rules copy.

### Mandatory reads

**Before non-trivial code** (new behavior, refactors, structural edits, more than a typo), and **every time a pack skill other than `/ask-gabriel` runs**:

1. Apply the **Taste** and **Architecture** sections of this file. They are already here. Do not wait for `/taste` or `/architecture`.
2. **Read** `pack-shared/subagents.md`. The main agent picks the specialist that owns the job and reviews Completions. It does not solo non-trivial find, analyze, implement, review, or tests, and it does not follow a fixed spawn order.
3. When judging a concrete shape, also Read `taste/examples.md` and `architecture/examples.md` from the skill root. When verifying or touching UI, also Read `taste/reference.md`.

Apply Taste and Architecture as **hard** standards. Do not skip because you "already know" the pack. Do not skip Architecture because the change looks like a single file. Keep the existing structure when that is the smallest correct answer.

**Before planning** (any turn that will produce a plan for non-trivial work, including a harness plan tool):

1. **Read** `pack-shared/asking.md`
2. **Read** `pack-shared/plain-language.md`
3. **Read** `grill-me/doctrine.md`
4. Apply **Taste** and **Architecture** in this file
5. **Read** `pack-shared/subagents.md` if not already loaded this turn

**Before branches or PRs:** follow the Ship work section (Read `publish/doctrine.md`, `publish/reference.md`, and `pack-shared/pr-ship.md`).

Talk in ordinary words (`pack-shared/plain-language.md`). Chat replies follow the Unslop section.

### App UX source of truth

`docs/design.md` (workspace root, that path only) is a short **Do** / **Don't** list for this app's UI and UX when the file exists. No screen catalog, no component encyclopedia, no architecture.

If the user says something is bad for the UX, too many clicks, too much typing, or they want a different interaction, update `docs/design.md` in the same turn. If the user wants to change how the design is done, that request updates `docs/design.md`. If the file is missing, run `/design` Initialization first. Do not wait for a separate `/design` invoke.

Frontend and user-facing implementation uses `/design`. Ship finished UI in that turn (`design:professional-craft`): identity from `docs/design.md`, the repo's tokens and theme, or the user, never invented. Apply `design:experience` even when the file is silent (least effort; do it for them when the next input is obvious; confirm when it is irreversible, money, or a guess). Apply `design:first-glance`: show only what every user needs at first glance; put extra actions and advanced settings one level down (overflow, popover, accordion). Apply `design:no-obvious`: do not caption an empty list ("No API key"); the create action is the message. Apply `design:ui-copy`: words fit the surface (landing hooks and sells; docs explain and stay clear; app UI names the action). Apply `design:spoken-locale`: user-visible words in a language are what speakers call that job, not a word-for-word swap (not "Background remover" to "Suppresseur de fond"). Do not ship filler that could sit on any other product. `/code-review` and `/pr-review` stay Standards and Spec. There is no `/design-review` skill and no Design axis.

### Plans: grill first

Whenever a non-trivial plan is about to be written, whether or not the harness calls that a plan mode:

1. **Do not** emit the final plan until material decisions are settled. If the harness has a plan tool, do not call it yet.
2. **Grill first.** Look up repository facts (specialists for non-trivial research per `pack-shared/subagents.md`), then send **one batched Questions-only** message using the asking contract (`Reply like: 1a 2b`, lettered options, mark `recommended`, wait for the reply). Do **not** include a Locked-in section in that message.
3. Sweep open topics before planning: outcome, out of scope, users/edges, plan split, file lane, taste/architecture/structure choices, and any product or policy forks that would change the plan. Prefer recommending behavior-preserving moves and deep modules over leaving debt.
4. After the user answers (or when nothing remains to ask), announce agent-owned conclusions in a **separate** **Locked in (tell me if this is wrong)** message. Never mix Locked and Questions.
5. After Locked closure, **then** produce the plan. Use the harness plan tool when it has one. Otherwise write the plan in chat. New unknowns later mean a **new** Questions-only batch.

Skip the grill only for trivial asks (typo, pure rename the user already specified, or the user explicitly said to skip grilling / plan immediately).

Every non-trivial plan **must** include a high-level Mermaid **Change diagram** with **both** `### Before` and `### After`. Prefer modules, actors, and request/data flow. Keep the same node ids across Before/After when possible. A plan without Before/After is incomplete.

### Environment variables

Before adding, renaming, requesting, or reading a **new** environment variable, apply **Reuse env vars** in the Taste section. Inventory existing names and **jobs** first (`.env.example`, `process.env` usages, Convex/Vercel env list when you are about to write that store). Reuse `SITE_URL` instead of inventing `FRONTEND_URL`. Add a name only when no existing var already holds that value.

### Conflict

The Taste and Architecture sections, plus design, publish, grill, asking, plain language, subagents, and PR ship, win over generic agent habit. The Unslop section wins for chat-reply voice. A repo's own instructions may add constraints. They must not replace or weaken these standards unless the user explicitly overrides in the chat.

## Taste

These rules apply on every non-trivial change, whether or not anyone invoked `/taste`. Examples are in `taste/examples.md`. Verify and UI detail is in `taste/reference.md`.

### Keep it simple

**Keep it simple** (KISS, Keep It Stupid Simple, expanded once here) is the default: the stupid-simple solution that still meets the outcome and Active Rules. Cleverness, ceremony, and speculative architecture are costs. Pay them only when evidence demands it.

| Do | Do not |
| --- | --- |
| Straight-line happy path; obvious names; one clear owner | Indirection for cleanliness, premature seams, config for imaginary products |
| Inline a one-call-site guard | Extract a helper/file/class that only wraps that guard |
| A plain function or single class for tiny glue | Pattern theater (factory-of-factories, empty bases, one-line impl files) |
| Deep entry when richness already exists | Shallow APIs that force every caller to orchestrate steps |

Keep it simple does **not** mean shallow modules, duplicated domain logic, or skipping a real service when the domain is independent. It means: simple surface, no extra moving parts. When keep-it-simple and growth conflict on a **big** feature, name the required seam, then keep everything else stupid simple (seam + one real impl, not a hierarchy of unused extension points). Detail: [`reference.md`](skills/taste/reference.md#futureproofing).

**Abstraction budget.** Prefer the smallest clear shape that fulfills the assigned outcome and Active Rules. Keep a one-call-site guard inline when it has one local purpose; extract it only when the extraction owns independent behavior, removes real duplication, or is required to enforce a locked invariant. Do not build for an imaginary product (YAGNI).

Before adding a new layer, file, service, wrapper, class hierarchy, shared API, queue, lock, retry system, or other coordination machinery, identify the evidence that a local implementation cannot meet the rule safely. A UI-disabled state is user feedback; if a client can bypass it, add the direct authoritative backend or state-transition guard before proposing coordination infrastructure (`taste:trust-the-server`, [`architecture:authority`](#authority)).

This budget does not prohibit a real service, deep module, extension seam, or the **owning folder** for a new concern ([`architecture:folders`](#folders)). The folder is not extra ceremony. It prohibits speculative ceremony, identity wrappers, one-off helper files dumped in a mixed parent, and abstractions created only because a local `if` looks untidy.

**Bad code** is whatever increases **complexity** or **entropy**. Good code is keep-it-simple first, deep where it matters (simple surface, rich inside), built from one-job helpers inside services / deep modules ([`architecture:primitives`](#primitives)), orthogonal by service, and leaves the touched lane cleaner or no dirtier than before.

| Term | Meaning |
| --- | --- |
| **Complexity** | Change amplification, cognitive load, unknown unknowns: hard to understand or change safely. Prefer fewer concepts at the call site; put richness behind a deep entry ([`architecture:deep-public-surface`](#deep-public-surface)). Forking a one-job helper’s job locally amplifies change. |
| **Entropy** | Local disorder that spreads when copied or left untouched in a lane you edit. Touching a dirty lane without a behavior-preserving cleanup when you can preserve behavior increases entropy. Forking or bypassing an existing one-job helper is entropy. |

Operational tests (apply before shipping a slice):

1. **Keep it simple:** Is there a stupider-simple shape that still meets Done when and Active Rules? Prefer it.
2. **Call-site:** Does the caller need internals / order / edge cases? Then the surface is shallow.
3. **Change:** Would a small product change touch many files for one concept? Then complexity (amplification).
4. **Window:** Are we copying or extending a known-wrong shape? Then entropy.
5. **Judo:** Is there a behavior-preserving delete/move that removes a whole branch or layer? Do it when the active goal or a named finding requires it; otherwise record a follow-up.
6. **One-job helper:** Does an existing block already answer this? Reuse it; do not fork ([`architecture:primitives`](#primitives)).

Named-principle checks live in the table below. Do not restate them here.

### Named principles

Apply these with keep it simple (KISS). Operational tests, not essays. In chat with the user, cite each as **plain (Classic)** ([plain-language.md](skills/pack-shared/plain-language.md)): `We need to keep this simple (KISS).` Never acronym-only and never plain-only. Cite keys stay `taste:*`. Structural placement lives in the Architecture section.

| Principle | Classic | Meaning | Test |
| --- | --- | --- | --- |
| **Keep jobs apart** | SoC (Separation of Concerns) | UI, domain, and I/O change for different reasons: keep them in different modules. | Would a UI copy change force a billing rewrite? If yes, jobs are mixed. |
| **One altitude** | SLAP (Single Level of Abstraction) | A function either coordinates *or* does detail work, not both. | Does this function both call services *and* parse bytes / format strings? Split it. |
| **Read or write, not both** | CQS (Command Query Separation) | A method either changes state or returns data, not both. | Does a getter also write? Does a command hide a write behind a “get”? Fix the shape. |
| **Fail fast** | Fail Fast | Reject bad input at the door; do not limp along. | Is bad input caught at the entry, or deep inside after partial side effects? |
| **Leave it cleaner** | Boy Scout Rule | Leave the files you touched a little cleaner (without changing behavior). | Did this edit copy a known mess, or slightly clean paths you already touched? |
| **Related together** | Cohesion; Law of Demeter when the issue is `a.b.c` | Things that change together live together; callers use a small public surface. | Do unrelated jobs share a file? Do callers reach through `a.b.c` internals? |
| **Safe to retry** | Idempotency | Repeating the same request has the same effect (payments, webhooks, retries, writes). | Can a double-submit create a duplicate charge, row, or side effect? |
| **Say what happens** | Explicit over implicit | Prefer clear data and control flow over magic. | Can a new reader see *what happens* without chasing hidden context? |
| **No surprises** | PoLA (Principle of Least Astonishment) | APIs and UI behave as a careful reader expects. | Would a teammate be surprised by a side effect, return value, or name? |
| **Honest names** | Intention-revealing names | File paths, exports, functions, types, and variables match the *current* job. Rename when the job changes. | After a rename, does the path still describe the old job? Would a reader open the wrong file? |
| **Trust the server** | Never trust the client | UI and client checks are feedback. Auth, ownership, money, and permissions are enforced on the write path. | Could a caller skip the UI (or toggle a client flag) and still perform the write? If yes, the lock is missing. |
| **Types tell the truth** | Make illegal states unrepresentable | Public args, returns, and stored fields match reality: no `any`, no optional that is required, validators at the boundary. | Would a lie in the type or a missing validator let bad data through? |

**How they relate:** Keep-jobs-apart + related-together shape *where* code lives (Architecture services). One-altitude, read-or-write, say-what-happens, no-surprises, and honest names shape *how* a unit reads. Fail fast + safe-to-retry + trust-the-server shape *boundaries*. Types-tell-the-truth shapes *contracts*. Leave-it-cleaner shapes *edits in messy files*.

**SOLID** is guidance in [`reference.md`](skills/taste/reference.md), not a quality gate.

**Quality gates** (`test:quality` from `/setup-toolkit`, plus the deliberate `test:mutants`) cover only mechanical cores: types tell the truth (make illegal states unrepresentable) (`any`, Convex `v.any`), fail fast (Fail Fast) (empty `catch`, Result bags), trust the server (never trust the client) (public Convex writes with no identity helper), deterministic queries (clock or randomness inside a query), the dead-code core of leave it cleaner (Boy Scout Rule) (unused files, exports, dependencies via Knip), and kill the mutants (Mutation testing) (Stryker: flipped operators must fail the suite). Keep jobs apart (SoC), one altitude (SLAP), read or write, not both (CQS), no surprises (PoLA), and don’t repeat yourself (DRY) stay review, as does the rest of leave it cleaner (Boy Scout Rule) beyond dead code. Do not add a keep-jobs-apart import denylist. Do not raise, skip, or delete a gate (or lower the mutant break threshold) to go green.

### Mechanical rules

Rules that are **not** already a named principle:

| Rule | Classic | Meaning |
| --- | --- | --- |
| **Never-nest** | Guard clauses | Flatten control flow; extract early instead of deep `if` / `try` pyramids. Does **not** mean flatten the folder tree ([`architecture:folders`](#folders)) |
| **Cyclomatic cap** | Cyclomatic complexity (McCabe) | A function has at most **5** independent paths. Each `if`, loop, `catch`, `case`, ternary, and logical and/or adds a path. Extract a named helper instead of adding a branch. `/setup-toolkit` installs `test:quality` (this cap plus principle and dead-code gates; mutants run separately as `test:mutants`); do not raise the cap, skip the test, or delete it to go green |
| **Don’t repeat yourself** | DRY | One concept, one place; no copy-paste twins |
| **Reuse env vars** | none | Inventory existing environment variables by **job and value** before adding a name. If `SITE_URL` already holds the public site URL, use it; do not create `FRONTEND_URL`. Detail: [Reuse env vars](#reuse-env-vars) |
| **No dead code** | Knip | No unused files, exports, or dependencies. `/setup-toolkit` installs the Knip gate in `test:quality`; remove the dead code instead of ignoring it to go green |
| **Kill the mutants** | Mutation testing | Behavior locks must fail when Stryker flips an operator, negates a boolean, or changes a sign. `/setup-toolkit` installs `test:mutants` as a deliberate run (not in `test:quality`); never lower the break threshold to go green |
| **Throw at boundaries** | Exceptions at boundaries | Throw + purposeful try/catch at boundaries that recover, translate, add actionable context, or clean up. Never `{ success: false }` / Result bags for expected failure control flow. Do not wrap local code merely because it could throw (`taste:fail-fast`) |
| **One export per file** | none | One component (or main export) per file |
| **Static imports** | none | No dynamic `import()` |
| **Comments** | none | Comments only to summarize big/complex functions. No narrating obvious code |
| **Cite a sibling** | none | Before inventing shape, mirror a **good** nearby feature or existing service that matches this taste and the Architecture section. Bad nearby code is debt, not a template. When you touch that lane, prefer a behavior-preserving move ([`architecture:prior-mistakes`](#prior-mistakes)) (`taste:leave-it-cleaner` when you can preserve behavior) |
| **OOP depth cap** | Composition over deep inheritance | At most two levels of class or interface nesting in a chain (example: `PaymentMethod` ← `CardPayment`). Prefer composition over a third layer. Depth 3+ is wrong for this taste: flatten or compose |
| **Plain language** | none | Chat cites principles as plain (Classic) ([plain-language.md](skills/pack-shared/plain-language.md)). Replies follow the Unslop section of `AGENTS.md` |

A unit does one job well (a logger only logs; it does not format emails or hit the DB): that is `taste:keep-jobs-apart`, not a separate rule. A reader can walk the happy path without branching into unrelated concerns: `taste:say-what-happens` and `taste:no-surprises`.

Prefer classes for stateful domain behavior and shared lifecycle (often that class *is* the service). Prefer hooks for React state/effects. Call sites import the simple entry point / service public API only ([`architecture:deep-public-surface`](#deep-public-surface)). Prefer over-splitting files inside a service or feature folder over god files.

### Reuse env vars

Before adding, renaming, requesting, or reading a **new** environment variable (`vercel env add`, Convex env set, `.env*` edits, `process.env.NEW_NAME`):

1. **Inventory names that already exist.** Read `.env.example`, other committed `.env*` templates, `process.env` / `import.meta.env` usages, and docs. If you are about to write a dashboard or CLI secret store, list that store once (`npx convex env list`, `vercel env ls`, or the matching MCP env list). That list is for reuse, not ritual verify (`taste:verify-terminals-first`).
2. **Match by job and value, not by the name you first thought of.** Public site URL, API origin, database URL, webhook secret, auth issuer: if an existing var already holds that job, reuse its name.
3. **Same name already present:** reuse it. Do not store the same value a second time under a synonym.
4. **A library wants a different name:** map in code from the existing var (`const siteUrl = process.env.SITE_URL`). Do not duplicate the value in the env store. A platform prefix (`NEXT_PUBLIC_`, `VITE_`) is allowed only when the runtime requires that exact prefix for client exposure, and then it must be the prefixed form of the **existing** name (`NEXT_PUBLIC_SITE_URL` from `SITE_URL`), not a third synonym (`FRONTEND_URL`).
5. **Add a new name only when no existing var holds that job.**

Anti-example: `SITE_URL` exists; the agent adds `FRONTEND_URL`, `APP_URL`, or `NEXT_PUBLIC_FRONTEND_URL`. Correct: read `SITE_URL` (or `NEXT_PUBLIC_SITE_URL` when the client bundle requires the prefix).

### Naming and files

| Area | Rule |
| --- | --- |
| App / UI / general TS | `lowercase-with-hyphens` (`use-checkout.ts`, `order-summary.tsx`) |
| **Convex** `convex/**` | **No `-` or `_` in filenames** (`orders.ts`, `orderActions.ts`) |
| Folders | Nest related files in a named folder even for the first file of a new concern; no mixed-parent dumps; no anonymous `utils` / `helpers` bags ([`architecture:folders`](#folders)) |
| **Honest names** | Path and primary export describe today’s job. After a rename, move, or scope change: update the filename, exports, types, functions, and variables in the same edit. Never leave new logic under the old name (`taste:honest-names`) |

### Checklist

Cite-key self-check before acceptance evidence and `/code-review`:

- [ ] `taste:keep-it-simple` (no extra layer, file, wrapper, pattern, or config beyond Done when / rules that must stay true)
- [ ] Named principles in Cite keys: no clear violation in the touched lane
- [ ] `taste:never-nest` · `taste:cyclomatic-cap` · `taste:dont-repeat-yourself` · `taste:reuse-env` · `taste:no-dead-code` · `taste:kill-the-mutants` · `taste:throw-at-boundaries` · `taste:one-export-per-file` · `taste:static-imports` · `taste:oop-depth-cap` · `taste:naming-files`
- [ ] `taste:cite-a-sibling` (good sibling, greenfield, or correcting debt; did not copy a known-wrong shape)
- [ ] `taste:plain-language` in user-facing chat
- [ ] `taste:verify-terminals-first` ([`reference.md`](skills/taste/reference.md#verify-terminals-first))
- [ ] Structure matches the Architecture section when one exists (Moves, primitives, authority)

Fail any box → fix before acceptance evidence and `/code-review`. `/code-review` Standards treats violations of this file as **hard** unless the repo’s own instructions contradict (repo wins on conflict).

### Apply

Apply these rules before grilling, planning, or writing code. They are already in this contract. When `/task` writes what "done" means, include taste-relevant checks when the change touches structure or UI (entry point, folder map, no Result bags, Convex names legal, jobs not mixed, public writes check identity, public args validated). Plans must not propose shapes that violate this section (including SOLID-maximalist boilerplate or class trees deeper than two).

Terminals first: [skills/taste/reference.md](skills/taste/reference.md#verify-terminals-first). React/UI: [skills/taste/reference.md](skills/taste/reference.md#react-and-ui).

### Taste: do not

- Cleverness or extra machinery without evidence it is required
- Copying a bad sibling to stay consistent with debt
- Treating a disabled button, hidden route, or client `if` as authorization
- `any` on a public surface, skipped validators, or required data marked optional
- Ritual lint / typecheck / Convex MCP instead of reading existing terminals
- Acronym-only principle talk (“SoC violation”) or plain-only (“keep it simple” with no KISS). Use `plain (Classic)`
- Using never-nest (guard clauses) or keep it simple (KISS) as permission to dump files in a mixed directory
- Inventing `FRONTEND_URL` (or another synonym) when `SITE_URL` or another existing var already holds that job (`taste:reuse-env`)
- Restating Architecture services, folders, or primitives in this file

## Architecture

These rules apply on every non-trivial change, whether or not anyone invoked `/architecture`. Examples are in `architecture/examples.md`.

### Services

A **service** is the code about one domain concern (auth, billing, notifications, search). It exposes a **small public API** of callable functions (or a class/facade with methods). Features **use** the service; they do **not** reimplement that domain.

| Concept | Rule |
| --- | --- |
| **Service** | One concern (billing, auth). Owns the how |
| **Public API** | Named operations features call, for example `makeUserPay()`, `requireUser()`, `sendReceipt()` |
| **Feature** | Product slice that orchestrates services + its own UI/state. Never copies billing/auth internals |

- **Explore for an existing service first.** Extend its public API before inventing a parallel one. Explore existing environment variables the same way (`taste:reuse-env`): reuse `SITE_URL`; do not invent `FRONTEND_URL`.
- If the concern is a genuinely independent domain capability or the goal explicitly plans growth, create the service (folder + public entry) and have the feature call it. For bounded local behavior, keep the smallest direct shape until it has independent ownership, real duplication, or a locked rule that needs a boundary.
- Features import **only** the service's public surface. Stripe/SDK/DB helpers stay behind that surface.
- Name public functions as **verbs the product understands** (`makeUserPay`, not `runStripeCheckoutSessionHelper`).
- Prefer throw + try/catch at service boundaries (`taste:throw-at-boundaries`), not `{ success: false }` bags.
- One service is not one giant file: public entry + collaborators / primitives inside the service folder.
- Public writes check identity and ownership in the service (`architecture:authority`). Features may disable UI; they do not own the lock.

Anti-patterns: checkout, upgrade, and invoices each implementing their own Stripe path; “just this once” copy of service logic into a feature; features importing service internals (`billing-stripe`); a `utils/payments.ts` dumping ground with no public contract.

Folder tree: `architecture:collaborating-parts`.

### Deep public surface

Hide messy orchestration behind **one deep** thing the caller uses: simple interface, rich functionality. For a domain concern, that entry **is the service's public API**. For UI, it is usually a hook that **calls** services.

| Shape | When |
| --- | --- |
| **Service** (module / class / facade) | Domain capability shared across features (default for auth, billing) |
| React hook (`useX`) | UI state/effects/subscriptions. Delegates domain work to services |
| Class / abstract class | Stateful domain behavior, shared lifecycle (often *is* the service) |
| Narrow function API | Pure transforms with a clear input→output |

- The entry point's signature should be obvious in one glance
- Call sites should not know about helpers, parsers, adapters, or edge-case branches
- One main export / one main type per file when practical (`taste:one-export-per-file`)
- Prefer class for stateful domain behavior; hooks for React; service for shared domain I/O
- Pull complexity **down** into collaborators and primitives; keep the public surface deep

The entry point is not always a TypeScript `interface`. Pick the shape that fits the stack.

Anti-pattern: **shallow modules** (complex interface relative to what they do: many params/options/leaked steps, callers still orchestrate the how).

### Primitives

A **primitive** is a **small piece of code** that is **strong yet flexible** and answers **one very specific thing**. It can be **reused independently without breaking**. Primitives are the strong blocks inside services and deep modules.

| Property | Meaning |
| --- | --- |
| **Small** | Narrow scope: not a feature, not a god module |
| **One specific job** | Answers one question / does one thing well |
| **Strong** | Deep enough that callers do not reimplement that job |
| **Flexible** | Composes / chains; reuse does not force brittle coupling |
| **Independent reuse** | Call sites can use it without breaking it or each other |
| **Placement** | Lives **inside** services and deep modules: building blocks of those, not a rival top-level architecture |

The deep public surface is what callers see. Primitives are how that depth stays real without leaking every concern to every call site.

1. Prefer building with primitives over duplicating that job at call sites.
2. Explore first: reuse an existing primitive when it already answers that specific thing.
3. When creating one: keep it small, one job, strong yet flexible, safe to reuse independently.
4. Place it inside the owning service / deep module (or a shared layer those modules compose), not a dumping-ground `utils`.
5. Do not fork a primitive's job in a feature or sibling helper.
6. Reason from this definition. Discover primitives by exploring **this** repo. Do not invent a canned catalog from training data.

Anti-patterns: forking a primitive's job locally; thin identity wrappers that only rename with no strength; sprawling helpers that answer many things; promoting primitives to a parallel top-level architecture that rivals services.

### Prior mistakes

Flawed existing layout is **debt**, not a template. Do not freeze wrong placements because they were already there. Leaving or copying wrong placement is entropy growth (`taste:leave-it-cleaner`).

When explore shows a wrong folder, duplicated domain logic, a feature-forked service, or a sibling that violates these rules, first decide whether the active goal or a named review finding requires a move:

- **Do not copy it.** Cite a *good* sibling or service, or create the correct shape.
- If required, prefer a **behavior-preserving move**: relocate into the right service/folder, extract the public API, rewire callers, delete the dead path. This reduces entropy. If not required, capture it as a follow-up rather than expanding the goal.
- Name the old observable behavior and how you will prove it still holds (existing tests if any, path walk + acceptance evidence / terminals). A new lock waits for a user-accepted `/create-test` brief: a `/task` suggestion after grill Locked, or a recommendation from `/code-review` or `/pr-review`. If you cannot be sure the move preserves behavior, include the move in the next `/grill-me` Questions batch. If the move is required and you can preserve behavior, do it; otherwise keep it as a follow-up.
- Update the Structure card (**Moves / corrections**) before coding; mid-implement, patch the plan Structure, then move.
- Same spirit as `/code-review` simplification: apply it while **building**, not only at review time.

Anti-patterns: bolting new code onto a known-wrong shape because it was already there; copying a bad sibling to stay consistent with debt; asking “leave it where it is?” as the recommended option when a clear move preserves behavior.

### Folders

**Nest related files in a named folder.** That is how the tree stays maintainable. A mixed flat directory is a messy codebase. Keep-it-simple (KISS) and never-nest (guard clauses) do **not** authorize a flat dump: never-nest flattens *control flow*, not the filesystem (`taste:never-nest`).

**Create the owning folder before the files.** Propose the folder map first. A new concern gets a folder **even when it starts as one file**. Do not wait until five siblings already exist.

1. Mirror existing repo conventions (services folder, feature folder, domain folder). Explore first. A **good nested sibling** wins over a nearby flat dump (`taste:cite-a-sibling`). A nearby flat dump is debt (`architecture:prior-mistakes`), not a template.
2. Prefer **`services/<concern>/`** (or the repo's equivalent) for shared domain APIs; **feature folders** for product UI/orchestration that *calls* those services.
3. If no convention fits, create a **feature/domain folder** and put the cluster inside it.
4. Colocate what changes together; nest collaborators one level down (`components/`, `hooks/`, private helpers) when they are not the public entry. Separate what changes for different reasons.
5. Name files per `taste:naming-files`.
6. Avoid `utils.ts` / `helpers.ts` dumping grounds. Name the concept (often: promote to a service, or a primitive inside one).
7. **Convex:** a one-file concern may stay `convex/billing.ts` when that is the repo pattern. A second file for that concern **moves the cluster** into `convex/billing/` (do not add `billingStripe.ts` as a `convex/`-root sibling). Do not keep both `convex/billing.ts` and `convex/billing/`.
8. **App Router:** `page.tsx` / `layout.tsx` / `route.ts` stay at the route folder. Other files for that slice nest in that folder (`components/`, `hooks/`) or a feature folder, not as mixed siblings of unrelated routes.

Leave at the repo root only files that belong there (`package.json`, `tsconfig.json`, `docs/design.md`). Patching an existing file in an already-correct folder does not require a new folder.

Anti-patterns: new related files as siblings in `src/`, `app/`, `convex/`, or any mixed parent; treating `taste:never-nest` or `taste:keep-it-simple` as “don’t make a folder”; waiting until the directory is already messy before nesting; a new payments helper beside a feature when a billing service should own it.

### Collaborating parts

Inside the folder, split by responsibility: public entry, then primitives and collaborators.

```text
services/billing/
  billing.ts            # public API: makeUserPay, refundPayment. Only export features import
  billing-stripe.ts     # private
  billing-types.ts
features/checkout/      # UI + orchestration. Calls makeUserPay
  use-checkout.ts
  checkout-types.ts
  components/
    checkout-form.tsx
features/upgrade/       # same
```

Convex modules live under `convex/` with taste naming (`billing.ts`, not `billing-actions.ts`). When the concern is more than one file, nest them under `convex/<concern>/` (`architecture:folders`). A Convex service module still exposes a small public set of queries/mutations/actions; features call those. They do not duplicate Stripe/auth logic in another Convex file.

Adjust names to the repo. **Inside the owning folder**, keep the tree shallow: public entry → primitives / collaborators → at most one leaf folder (`components/`, `hooks/`). That nesting is required. It is not extra ceremony. `taste:never-nest` is about `if` / `try` pyramids, not the filesystem. Do not skip the owning folder to keep the tree “flat.” Do not invent four empty layers (`services/billing/stripe/v2/internal/`).

### Cheap reads

**Reads must stay cheap as data grows.** Prefer **compute on write**, store the result, read it later.

| Bad (does not scale) | Good (scales) |
| --- | --- |
| On every render/query: scan all rows and sum/average/count | Store `total`, `count`, `avg` on a parent row, summary table, or dedicated columns |
| Dashboard that maps every event into charts client-side | Pre-aggregate on insert/update; UI reads the summary |
| `collect()` then reduce in TS for hot paths | Indexed query of stored aggregates / summary docs |

**Rule:** if a value is shown often and derived from many child records, **persist it** and **update it in the same write** that changes the children (insert / patch / delete). Do not recalculate from scratch on each read unless the dataset is provably tiny and bounded.

When inserting or updating a child:

1. Write the child record
2. **In the same mutation/transaction**, bump/recompute the stored aggregate on the parent or summary row
3. Reads only fetch the stored fields

Example shape (conceptual): `orders: { … }` and `users: { orderCount, orderTotalCents, … }` updated when an order is inserted. Not: `listOrders(userId)` then sum in the React tree or in a query every time.

- **Index** fields you filter/sort by (Convex: `.withIndex`, not `.filter` scans)
- Avoid unbounded `.collect()` on growing tables. Paginate or aggregate
- Don't N+1: batch or denormalize fields needed for list views
- Client components should display data, not be the analytics engine
- Expensive derived views → materialize (table/columns/summary doc), not calculate on render

If a one-off admin script needs a full scan, say so explicitly. Never copy that pattern into hot product paths.

### Deterministic queries

Queries (and any cached / reactive read) must return the same result for the same data. Do **not** read the wall clock, generate randomness, or call a non-deterministic network from a query.

| Bad | Good |
| --- | --- |
| `Date.now()` / `new Date()` inside a query to expire rows | Store `status` on write or a scheduled mutation. Pass `now` only for display windows, never as an authorization check |
| Query that maybe hits an external API | Query reads stored fields; an action fetches, a mutation writes |
| Filter/sort in memory after an unbounded `collect()` | Indexed query; paginate or read a stored summary |

Public queries, mutations, and actions declare argument (and return) validators that match the real contract (`taste:types-tell-the-truth`). Do not use `v.any()` to skip that work.

### Authority

A disabled button is **user feedback**. If a client can skip it, the write still happens. Put the lock on the **service write** (mutation, action, or server handler), not only in the feature UI (`taste:trust-the-server`).

| Check | Rule |
| --- | --- |
| **Identity** | Public writes that touch user data call the repo's auth helper (`getUserIdentity` / `requireUser` / equivalent) and fail if missing |
| **Ownership / tenant** | Before patch/delete/read of a row, prove the authenticated user owns it or belongs to that tenant. Never trust a client-sent `userId` / `orgId` alone |
| **Same-write invariants** | Facts that must stay true together (row + aggregate, status + timestamp, ledger + side effect) live in **one** mutation/transaction |
| **Money / permissions** | Charge, refund, role change, and admin paths go through the owning service; the feature does not call the provider with a client-supplied amount it did not authorize |

Anti-patterns: mutation accepts `userId` from the client and writes that user's rows with no identity check; “the button is hidden for non-admins” as the only admin gate; updating a child row in one handler and the parent aggregate in a later optimistic UI call; feature-local `if (!session)` while the public mutation still runs.

Name identity, ownership, and retry keys on the structure card when the slice has writes.

### Structure card

Present this **Structure** card before writing code (and include it in the inline plan contract when planning under `/task`):

```markdown
## Structure

**Always**
**Services:**
- **Owns / extends:** `path`: public API: `makeUserPay(…)`, … (or _n/a: pure UI_)
- **Calls (existing):** `billing.makeUserPay`, `auth.requireUser`, … (never reimplements these)
- **Must not duplicate:** <Stripe / JWT / email provider / …>
**Moves / corrections:** <required by Rule 1 / what-done-means / named finding: move X → services/billing; delete old path> | _none_
**Feature entry:** `path`: `useX` | `ClassX` | `fn`. One-line contract (orchestrates services + UI); **deep** surface
**Primitives:**
- **Reuse (existing):** cite path + one-line job | _none_
- **New / extend:** path. One specific job; how it stays reusable without breaking
- **Inside:** which service / deep module owns it
**Hidden behind services / entry:** bullet list of responsibilities callers must not see
**Folder map:** (required owning folder; no mixed-parent dump)
- `services/<concern>/` (or repo equivalent)
  - `<concern>.ts`          # public API
  - collaborator…
  - `components/` or other one-level leaf when needed
- `features/<slice>/`       # calls services. No domain fork
  - entry + UI…
**Fits existing pattern:** yes (cite **good** service / feature) | correcting debt (what) | new (why)
**Taste:** `taste:naming-files`, `taste:keep-it-simple`, `taste:oop-depth-cap`

**If writes**
**Authority:** identity helper; ownership/tenant check; client cannot bypass; retry key (`architecture:authority`, `taste:safe-to-retry`)

**If lists / dashboards / counts**
**Scalability:**
- Hot reads: <what the UI/query returns>
- Stored on write: <columns / summary table / parent fields updated on insert>
- Indexes: <index names / fields>
- Pagination: <cursor / none because bounded>
- Explicitly NOT recomputed on render/read: <metrics>
- Queries are deterministic: no wall clock / randomness in the read (`architecture:deterministic-queries`)
- Public args validated: `taste:types-tell-the-truth` | n/a

**If big feature / service**
**Extension seam:** foundation from day one. How the next provider/variant plugs in without breaking the public API (ship seam + first impl together)
```

If service boundary, public API shape, primitives (reuse vs new vs fork), folder root, write-vs-read, authority (identity / ownership), or a move vs leave decision is open, put **all** open structure questions in **one** `/grill-me` Questions batch (`Reply like: 1a 2b` per [asking.md](skills/pack-shared/asking.md)). Recommend a behavior-preserving move when it is required by the goal or finding and you can prove old behavior holds; otherwise name it as a follow-up. Do not drip them one message at a time. New findings later → new batch.

Self-check before done (cite keys, not a second essay):

- [ ] `architecture:services` (domain in a service with a public API, or an existing one extended; features call it)
- [ ] `architecture:primitives` (one job each; reused not forked; inside the owning module)
- [ ] `architecture:prior-mistakes` (not copied; required moves done; optional ones are follow-ups)
- [ ] `architecture:folders` / `architecture:collaborating-parts` (new files nested in an owning folder, not mixed siblings)
- [ ] `architecture:deep-public-surface`
- [ ] `architecture:authority` when the slice has writes
- [ ] `architecture:cheap-reads` when the slice has lists, counts, or dashboards
- [ ] `architecture:deterministic-queries` (no `Date.now()` / randomness in the read)
- [ ] Taste Cite keys respected in the touched lane
- [ ] Observable old behavior still holds after any move

### When this applies

**When this changes the shape.** These rules are already in this contract. For a typo or a user-specified pure rename, still apply them; the application is **keep the existing structure**.

Process: explore, then the structure card, then implement, then the checklist above. Steps for an audit live in `architecture/SKILL.md`. The rules are the headings above.

Apply when the work could add files, move ownership, or touch data, including:

- New feature (even one new file)
- Any domain capability (payments, auth, email) a second feature might need
- Temptation to copy Stripe/auth/email logic into a feature or leave it misplaced
- Clear prior mistake in the lane when the current goal or named finding requires a behavior-preserving move
- Extracting logic from a large file
- Adding React state/effects that would otherwise bloat a component
- Any new file for a new concern, or a second file that would sit as a mixed sibling
- Any change that would add files without an owning folder
- Any feature with lists, dashboards, counts, totals, leaderboards, or stats
- Any query that would scan children to answer a parent-level question
- Any public write, webhook, or admin path
- Any query that would read the wall clock or filter a growing table without an index

Hand off: structure card, then `/task` (inline plan contracts in chat). Acceptance evidence and `/code-review` will fail scale anti-patterns, duplicated-service anti-patterns, mixed-parent file dumps, and missing write-path authority under `/task`. These rules apply on every run. They are already in this contract.

### Architecture: do not

- Feature-forked Stripe / JWT / email
- Shallow public surface that leaks steps to every caller
- Forking a primitive's job locally
- Copying a known-wrong shape because it was already there
- Dumping new related files into a mixed parent directory
- Treating `taste:never-nest` or `taste:keep-it-simple` as permission to skip the owning folder
- Hot-path compute-on-read for metrics
- `Date.now()` or randomness inside a query
- UI-only guard as the write lock
- Skipping this section because the slice looks small

## No em dash

Never write an em dash (Unicode U+2014), en dash (U+2013), or horizontal bar (U+2015) in chat or in files you create or edit.

Use a comma, colon, period, parentheses, or a hyphen instead.

This pack's ESLint template flags those characters in JS/TS. Follow that rule. Do not sweep unrelated files just to strip existing dashes.

## Unslop

Your **reply in this discussion** is the prose surface. Write it clean as you draft it. Do not generate slop and strip it afterward. That pass fails.

Do not restyle README, ticket, PR-body, or commit-message files. Dash characters are the No em dash section. Ordinary words and pack nicknames are `pack-shared/plain-language.md`. Asking templates stay exact.

Adapted from [pstack unslop](https://github.com/backnotprop/pstack) (MIT). Pstack sends docs and PR bodies to a different skill. This section is discussion text only.

### Draft

- Short declarative sentences. One thought per sentence.
- Terse is not an excuse to drop the answer, the evidence, or the next step.
- Have a point of view. Recommend. Do not fake balance when you already have a pick.
- Name the mechanism, path, or number. Not a mood.
- "I" is fine when reporting what you did. Sycophancy is not: skip "Great question!" and "You're absolutely right!"
- Parentheses stay allowed. Do not strip them to dodge dashes.
- Do not invent metaphors or late-night atmosphere. Be specific to this repo and this turn.
- A sentence that could appear unchanged in another project's chat says nothing here. Cut it.

Before send: **What makes this obviously generated?** Fix that.

### Tells

#### Content

1. Puffery: "pivotal moment", "testament to", "evolving landscape", "setting the stage", "indelible mark", "deeply rooted". State what happened.
2. Name-dropping with no claim. Pick one source or delete.
3. Hollow -ing phrases: "highlighting…", "ensuring…", "reflecting…", "showcasing…", "fostering…". Delete or replace with a fact.
4. Promotional words: "vibrant", "breathtaking", "groundbreaking", "renowned", "stunning", "must-visit", "nestled". Neutral description.
5. Vague attributions: "Experts believe", "Industry reports suggest". Name the source or delete.
6. Formulaic bounce-back: "Despite challenges… continues to thrive." Specific fact.

#### Language

7. AI vocabulary: Additionally, crucial, delve, enduring, enhance, fostering, garner, interplay, intricate, landscape (abstract), pivotal, showcase, tapestry (abstract), testament, underscore, vibrant. Plain word.
8. Fancy "is": "serves as", "stands as", "boasts", "features". Say "is" or "has".
9. "Not just X, but Y." State the point once.
10. Forced groups of three. Use the natural number.
11. Synonym cycling. One name per thing. Repeat it.
12. False ranges: "from X to Y" when those are not on a scale. List the topics.

#### Style

13. No em dash, en dash, or horizontal bar (No em dash section). Comma, colon, period, parentheses, or hyphen. Colon is fine before a list, not as a mid-sentence crutch.
14. Bold only the few words that matter.
15. Inline-header restatement is a tell ("**Performance:** Performance improved…"). A bold lead-in that adds new detail is fine.
16. Sentence case headings in chat.
17. No decorative emojis in headings or bullets.
18. Straight quotes, not curly.

#### Chat and filler

19. Chatbot closings: "I hope this helps!", "Let me know if…", "Of course!", "Certainly!", "Found the smoking gun!" Delete.
20. Cutoff disclaimers: "While specific details are limited…" Find the source or remove.
21. Answer the question. Do not flatter.
22. "In order to" becomes "To". "Due to the fact that" becomes "Because". Delete "It is important to note that".
23. Stacked hedges become "may".
24. Generic endings ("The future looks bright.") become the next concrete step.

#### Plain speech

25. Abstract metaphor nouns in chat: substrate, wedge, vector, locus, vantage, nexus, harness (metaphor), bedrock, scaffolding (metaphor), modality, paradigm, gold-plating, ratchet (metaphor), evacuate (for moving code), endgame, north star, flywheel. Concrete word instead. Pack doctrines may keep `primitive` and `surface`. Chat says "one-job helper" and "public API".
26. If you cannot restate the sentence as an instruction, fact, or number, cut it.
27. Split dense sentences. One idea each when the reader would backtrack.
28. Active voice. Name the actor unless the actor does not matter.
29. Cut adverbs, or use a stronger verb. "significantly improves" becomes the measured delta.
30. Prefer the plain word: "utilize" / "leverage" becomes "use"; "facilitate" becomes "help"; "in the event that" becomes "if".

## Subagents

**Before non-trivial work** (find, analyze, implement, review, multi-file edits, not a typo or one-liner):

1. **Read** `pack-shared/subagents.md`

The main agent stays in its smart zone: split the **what**, inject **need-to-know**, dispatch specialists, and **review** Completions. It does not grep the tree. Workers own **how**.

When the harness can spawn a specialist, dispatch one. When it cannot, do that role as its own pass. Do not mix find, judge, and implement in one pass.

When surfaces, slices, or review axes are independent, launch **one specialist per lane in the same turn** if the harness allows it. There is **no cap of two**. A slice can be one function. A single non-trivial job is one pass, then the next.

Pick the **listed** specialist that owns the job: **explorer**, **analyzer**, **implementer**, **designer**, **reviewer**, **pr-reviewer**, **tester**. A harness built-in that matches the job is also valid. Do not follow a fixed spawn order. Explorer finds. Analyzer judges. They are not the same. **Designer** owns user-facing UI and `docs/design.md`. **Implementer** owns non-UI slices. **Tester** writes a behavior lock when the user started `/create-test` or accepted a `/task` behavior-lock brief. Ordinary edits do not get tests. The main agent never writes tests. Do not use reviewer for a GitHub PR, and do not use pr-reviewer for a local branch. There is no architect worker.

Trivial work (typo, pure rename, git status, reading existing terminals) may stay on the main agent. Never spawn verification-only lint ritual passes. Never auto-start `/create-test`. A `/task` suggestion is not a start until the user answers, and they can refuse every test.

Worker **Read first** must include this file's **Taste** and **Architecture** sections. Skip is a fail. User-facing work also reads `design/doctrine.md` and `docs/design.md`.

## No drive-by tests

Changing code is not a reason to add a test.

Do not create or extend a test for a small tweak, copy change, rename, comment, type-only edit, wiring change, formatter, UI chrome, generated code, or a one-line fix. Do not add a test to chase coverage, to restate the implementation (`expect(add(1, 2)).toBe(3)`), or because the suite should cover this.

Running tests that already exist is fine. Fix an existing assertion only when this change made that assertion lie. Do not add a new case next to it.

Quality gates from `/setup-toolkit` (`test:quality`, `test:mutants`) stay. Do not delete them. Do not invent behavior tests to satisfy them.

Write a test only when the user has accepted that lock:

- they explicitly asked for it, or
- they answered yes on a `/task` behavior-lock brief after grill Locked (each brief cites a grilled rule; every brief has a no; silence and a parent taking `recommended` are not acceptance), or
- they started `/create-test` after `/code-review` or `/pr-review` recommended one for a complex public surface (authorization, ownership, safe-to-retry, a domain rule that can silently drift).

Then `tester` writes it. The main agent does not. Do not start `/create-test` without one of those acceptances. If the target is trivial, say so and stop.

This binds every agent, including `tester` and `implementer`.

## Ship work

Before branches or PRs, **Read**:

1. `publish/doctrine.md`
2. `publish/reference.md`
3. `pack-shared/pr-ship.md`

**Every** agent that opens a GitHub PR follows `pr-ship.md`, not only `/publish`.

- Before a push that opens a PR, or a commit or push on a branch that already has an open PR, run the CI mirror in `pack-shared/pr-ship.md` in this environment. Push once it is green. A local commit you are not pushing, while no PR is open, does not run that suite. Do not invent a suite when the repo has no workflow and no lint or test script. Never `--no-verify` unless the user asked.
- A new branch is a standalone ref. Cut it from the base commit with the steps in `publish/reference.md`: `git switch --detach <base-sha>`, then `git switch -c <new-branch>` (or `git switch --no-track -c`). Do not copy the upstream of `dev`, `main`, or `master`. Push only `HEAD:refs/heads/<new-branch>`. If `@{upstream}` is `origin/dev`, `origin/main`, or `origin/master`, stop. Never push those branches.
- Typed branch names per `publish/reference.md` when you control the branch contract
- PR body: type, ticket, what changed, Mermaid Change diagram (Before/After for rework), How to QA, Notes. No screenshots, no canvas, no browser
- Use the harness pull-request tool when it has one. Otherwise use `gh` as `pr-ship.md` describes. Do not use `gh` in a session that already has a pull-request tool.

## Project tooling

Do **not** paste a style guide into chat. If this repo already has ESLint or Prettier, **follow those configs**.

- Add or change lint/format tooling with `/setup-toolkit`. Do not invent a parallel config.
- The toolkit ESLint baseline includes `no-emdash/no-emdash` (em dash, en dash, horizontal bar). Keep that rule on. Do not disable it to "make the prose look fancy."
- The toolkit also installs `test:quality` (complexity cap 5, principle gates, plus `knip.test.mjs` for dead code) and `test:mutants` (Stryker: flipped operators must fail the suite). Keep them. Do not raise the cap, skip a gate, delete a gate, or lower the mutant break threshold to go green. Split the function, type the value, throw at the boundary, check identity, remove dead code, or strengthen the lock instead. Gate failures use plain (Classic), for example fail fast (Fail Fast).
- Editor workspace files live in `.vscode/extensions.json` and `.vscode/settings.json`. Do not add a parallel `.cursor/extensions.json`.
- Do **not** ritual-run `eslint`, `tsc`, or full suites after every slice. CI and the user's running terminals own that loop (`taste` Verify).
- **Before a push that opens or updates a PR:** run the CI mirror in `pack-shared/pr-ship.md` in this environment, then push once. A local commit with no open PR and no push does not run that suite. Skip `test:mutants` unless the pull_request workflow runs it. If there is no workflow and no lint or test script, say so. Never `git commit --no-verify` unless the user asked.
- Run lint or format when the user asked, when a named review finding requires it, or when you just added the config and need one smoke check.
- Do not reformat the whole tree as a drive-by. Format only files you already had to touch, unless the user asked for a repo-wide format.
- Never overwrite an existing `eslint.config.*`, Prettier config, or `.vscode/settings.json` without asking.

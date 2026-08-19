# Taste doctrine

## Job

Pack coding taste: keep it simple, named principles, and unique mechanical rules.

## Owns

How a unit reads, names, errors, and stays simple. Keep-it-simple, named principles, mechanical rules, file naming, comments, and chat language.

## Does not own

- Structure card, services, folders, primitives, cheap reads, deterministic queries, write-path authority: [`architecture:services`](../architecture/doctrine.md#services) through [`architecture:authority`](../architecture/doctrine.md#authority)
- Review disposition and posting: [`../code-review/doctrine.md`](../code-review/doctrine.md), [`../pr-review/doctrine.md`](../pr-review/doctrine.md)
- Numbered process: [`process.md`](process.md)
- Terminals-first verify, React/UI, SOLID, futureproofing detail: [`reference.md`](reference.md)

## Cite keys

| Key | Heading |
| --- | --- |
| `taste:keep-it-simple` | Keep it simple |
| `taste:keep-jobs-apart` | Named principles |
| `taste:one-altitude` | Named principles |
| `taste:read-or-write` | Named principles |
| `taste:fail-fast` | Named principles |
| `taste:leave-it-cleaner` | Named principles |
| `taste:related-together` | Named principles |
| `taste:safe-to-retry` | Named principles |
| `taste:say-what-happens` | Named principles |
| `taste:no-surprises` | Named principles |
| `taste:honest-names` | Named principles |
| `taste:trust-the-server` | Named principles |
| `taste:types-tell-the-truth` | Named principles |
| `taste:never-nest` | Mechanical rules |
| `taste:dont-repeat-yourself` | Mechanical rules |
| `taste:throw-at-boundaries` | Mechanical rules |
| `taste:one-export-per-file` | Mechanical rules |
| `taste:static-imports` | Mechanical rules |
| `taste:comments` | Mechanical rules |
| `taste:cite-a-sibling` | Mechanical rules |
| `taste:oop-depth-cap` | Mechanical rules |
| `taste:naming-files` | Naming and files |
| `taste:plain-language` | Mechanical rules |
| `taste:verify-terminals-first` | [`reference.md`](reference.md#verify-terminals-first) |

Snippets: [`examples.md`](examples.md).

## Bars

### Keep it simple

**Keep it simple** (KISS, Keep It Stupid Simple, expanded once here) is the default: the stupid-simple solution that still meets the outcome and Active Rules. Cleverness, ceremony, and speculative architecture are costs. Pay them only when evidence demands it.

| Do | Do not |
| --- | --- |
| Straight-line happy path; obvious names; one clear owner | Indirection for cleanliness, premature seams, config for imaginary products |
| Inline a one-call-site guard | Extract a helper/file/class that only wraps that guard |
| A plain function or single class for tiny glue | Pattern theater (factory-of-factories, empty bases, one-line impl files) |
| Deep entry when richness already exists | Shallow APIs that force every caller to orchestrate steps |

Keep it simple does **not** mean shallow modules, duplicated domain logic, or skipping a real service when the domain is independent. It means: simple surface, no extra moving parts. When keep-it-simple and growth conflict on a **big** feature, name the required seam, then keep everything else stupid simple (seam + one real impl, not a hierarchy of unused extension points). Detail: [`reference.md`](reference.md#futureproofing).

**Abstraction budget.** Prefer the smallest clear shape that fulfills the assigned outcome and Active Rules. Keep a one-call-site guard inline when it has one local purpose; extract it only when the extraction owns independent behavior, removes real duplication, or is required to enforce a locked invariant.

Before adding a new layer, file, service, wrapper, class hierarchy, shared API, queue, lock, retry system, or other coordination machinery, identify the evidence that a local implementation cannot meet the rule safely. A UI-disabled state is user feedback; if a client can bypass it, add the direct authoritative backend or state-transition guard before proposing coordination infrastructure (`taste:trust-the-server`, [`architecture:authority`](../architecture/doctrine.md#authority)).

This budget does not prohibit a real service, deep module, or extension seam for a genuinely independent domain capability or explicitly planned growth. It prohibits speculative ceremony, identity wrappers, one-off helper files, and abstractions created only because a local `if` looks untidy.

**Bad code** is whatever increases **complexity** or **entropy**. Good code is keep-it-simple first, deep where it matters (simple surface, rich inside), built from one-job helpers inside services / deep modules ([`architecture:primitives`](../architecture/doctrine.md#primitives)), orthogonal by service, and leaves the touched lane cleaner or no dirtier than before.

| Term | Meaning |
| --- | --- |
| **Complexity** | Change amplification, cognitive load, unknown unknowns: hard to understand or change safely. Prefer fewer concepts at the call site; put richness behind a deep entry ([`architecture:deep-public-surface`](../architecture/doctrine.md#deep-public-surface)). Forking a one-job helper’s job locally amplifies change. |
| **Entropy** | Local disorder that spreads when copied or left untouched in a lane you edit. Touching a dirty lane without a behavior-preserving cleanup when you can preserve behavior increases entropy. Forking or bypassing an existing one-job helper is entropy. |

Operational tests (apply before shipping a slice):

1. **Keep it simple:** Is there a stupider-simple shape that still meets Done when and Active Rules? Prefer it.
2. **Call-site:** Does the caller need internals / order / edge cases? Then the surface is shallow.
3. **Change:** Would a small product change touch many files for one concept? Then complexity (amplification).
4. **Window:** Are we copying or extending a known-wrong shape? Then entropy.
5. **Judo:** Is there a behavior-preserving delete/move that removes a whole branch or layer? Do it when the active goal or a named finding requires it; otherwise record a follow-up.
6. **One-job helper:** Does an existing block already answer this? Reuse it; do not fork ([`architecture:primitives`](../architecture/doctrine.md#primitives)).

Named-principle checks live in the table below. Do not restate them here.

### Named principles

Apply these with keep-it-simple. Plain names, operational tests, not essays. In chat with the user, use these plain names only ([plain-language.md](../pack-shared/plain-language.md)). Structural placement (services, folders) lives in `/architecture`.

| Principle | Meaning | Test |
| --- | --- | --- |
| **Keep jobs apart** | UI, domain, and I/O change for different reasons: keep them in different modules. | Would a UI copy change force a billing rewrite? If yes, jobs are mixed. |
| **One altitude** | A function either coordinates *or* does detail work, not both. | Does this function both call services *and* parse bytes / format strings? Split it. |
| **Read or write, not both** | A method either changes state or returns data, not both. | Does a getter also write? Does a command hide a write behind a “get”? Fix the shape. |
| **Fail fast** | Reject bad input at the door; do not limp along. | Is bad input caught at the entry, or deep inside after partial side effects? |
| **Leave it cleaner** | Leave the files you touched a little cleaner (without changing behavior). | Did this edit copy a known mess, or slightly clean paths you already touched? |
| **Related together** | Things that change together live together; callers use a small public surface. | Do unrelated jobs share a file? Do callers reach through `a.b.c` internals? |
| **Safe to retry** | Repeating the same request has the same effect (payments, webhooks, retries, writes). | Can a double-submit create a duplicate charge, row, or side effect? |
| **Say what happens** | Prefer clear data and control flow over magic. | Can a new reader see *what happens* without chasing hidden context? |
| **No surprises** | APIs and UI behave as a careful reader expects. | Would a teammate be surprised by a side effect, return value, or name? |
| **Honest names** | File paths, exports, functions, types, and variables match the *current* job. Rename when the job changes. | After a rename, does the path still describe the old job? Would a reader open the wrong file? |
| **Trust the server** | UI and client checks are feedback. Auth, ownership, money, and permissions are enforced on the write path. | Could a caller skip the UI (or toggle a client flag) and still perform the write? If yes, the lock is missing. |
| **Types tell the truth** | Public args, returns, and stored fields match reality: no `any`, no optional that is required, validators at the boundary. | Would a lie in the type or a missing validator let bad data through? |

**How they relate:** Keep-jobs-apart + related-together shape *where* code lives (`/architecture` services). One-altitude, read-or-write, say-what-happens, no-surprises, and honest names shape *how* a unit reads. Fail fast + safe-to-retry + trust-the-server shape *boundaries*. Types-tell-the-truth shapes *contracts*. Leave-it-cleaner shapes *edits in messy files*.

### Mechanical rules

Rules that are **not** already a named principle:

| Rule | Meaning |
| --- | --- |
| **Never-nest** | Flatten control flow; extract early instead of deep `if` / `try` pyramids |
| **Don’t repeat yourself** | One concept, one place; no copy-paste twins |
| **Throw at boundaries** | Throw + purposeful try/catch at boundaries that recover, translate, add actionable context, or clean up. Never `{ success: false }` / Result bags for expected failure control flow. Do not wrap local code merely because it could throw (`taste:fail-fast`) |
| **One export per file** | One component (or main export) per file |
| **Static imports** | No dynamic `import()` |
| **Comments** | Comments only to summarize big/complex functions. No narrating obvious code |
| **Cite a sibling** | Before inventing shape, mirror a **good** nearby feature or existing service that matches this taste + `/architecture`. Bad nearby code is debt, not a template. When you touch that lane, prefer a behavior-preserving move ([`architecture:prior-mistakes`](../architecture/doctrine.md#prior-mistakes)) (`taste:leave-it-cleaner` when you can preserve behavior) |
| **OOP depth cap** | At most two levels of class or interface nesting in a chain (example: `PaymentMethod` ← `CardPayment`). Prefer composition over a third layer. Depth 3+ is wrong for this taste: flatten or compose |
| **Plain language** | Humans must understand without decoding jargon or abbreviations ([plain-language.md](../pack-shared/plain-language.md)) |

A unit does one job well (a logger only logs; it does not format emails or hit the DB): that is `taste:keep-jobs-apart`, not a separate rule. A reader can walk the happy path without branching into unrelated concerns: `taste:say-what-happens` and `taste:no-surprises`.

Prefer classes for stateful domain behavior and shared lifecycle (often that class *is* the service). Prefer hooks for React state/effects. Call sites import the simple entry point / service public API only ([`architecture:deep-public-surface`](../architecture/doctrine.md#deep-public-surface)). Prefer over-splitting files inside a service or feature folder over god files.

### Naming and files

| Area | Rule |
| --- | --- |
| App / UI / general TS | `lowercase-with-hyphens` (`use-checkout.ts`, `order-summary.tsx`) |
| **Convex** `convex/**` | **No `-` or `_` in filenames** (`orders.ts`, `orderActions.ts`) |
| Folders | Feature/domain folders before flat dumps; no anonymous `utils` / `helpers` bags ([`architecture:folders`](../architecture/doctrine.md#folders)) |
| **Honest names** | Path and primary export describe today’s job. After a rename, move, or scope change: update the filename, exports, types, functions, and variables in the same edit. Never leave new logic under the old name (`taste:honest-names`) |

## Output

Cite-key self-check before acceptance evidence and `/code-review`:

- [ ] `taste:keep-it-simple` (no extra layer, file, wrapper, pattern, or config beyond Done when / rules that must stay true)
- [ ] Named principles in Cite keys: no clear violation in the touched lane
- [ ] `taste:never-nest` · `taste:dont-repeat-yourself` · `taste:throw-at-boundaries` · `taste:one-export-per-file` · `taste:static-imports` · `taste:oop-depth-cap` · `taste:naming-files`
- [ ] `taste:cite-a-sibling` (good sibling, greenfield, or correcting debt; did not copy a known-wrong shape)
- [ ] `taste:plain-language` in user-facing chat
- [ ] `taste:verify-terminals-first` ([`reference.md`](reference.md#verify-terminals-first))
- [ ] Structure matches the `/architecture` card when one exists (Moves, primitives, authority)

Fail any box → fix before acceptance evidence and `/code-review`. `/code-review` Standards treats violations of this file as **hard** unless the repo’s own `AGENTS.md` / `.cursor/rules` contradict (repo wins on conflict).

## Apply

Other pack skills Read this file through [standards.md](../pack-shared/standards.md) before grilling, planning, or writing code. When `/goal` writes what “done” means, include taste-relevant checks when the change touches structure or UI (entry point, folder map, no Result bags, Convex names legal, jobs not mixed, public writes check identity, public args validated). Plans must not propose shapes that violate this file (including SOLID-maximalist boilerplate or class trees deeper than two).

Terminals first: [reference.md](reference.md#verify-terminals-first). React/UI: [reference.md](reference.md#react-and-ui).

## Anti-patterns

- Cleverness or extra machinery without evidence it is required
- Copying a bad sibling to stay consistent with debt
- Treating a disabled button, hidden route, or client `if` as authorization
- `any` on a public surface, skipped validators, or required data marked optional
- Ritual lint / typecheck / Convex MCP instead of reading existing terminals
- Dumping jargon or abbreviations at the user
- Restating `/architecture` services, folders, or primitives in this file

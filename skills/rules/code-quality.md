# Code quality

Cite keys use the `taste:` prefix.

These rules apply on every non-trivial change, whether or not anyone invoked `/taste`. Examples: `taste/examples.md`. Verify and UI detail: `taste/reference.md`.

## Keep it simple

Pick the simplest shape that meets the outcome and the rules that must stay true (KISS, Keep It Stupid Simple). Do not build for an imaginary product (YAGNI).

| Do | Don't |
| --- | --- |
| Straight-line happy path, obvious names, one owner | Indirection for tidiness, early seams, config nobody needs |
| Inline a guard used in one place | A helper, file or class that only wraps it |
| One plain function or class for small glue | Factories of factories, empty base classes, one-line files |
| One deep entry when the logic is rich ([`architecture:deep-public-surface`](code-structure.md#deep-public-surface)) | Shallow APIs that make every caller orchestrate steps |
| A new folder for a new concern ([`architecture:folders`](code-structure.md#folders)) | One-off helper files in a mixed parent folder |

- Extract only when the extraction owns its own behavior, removes real duplication, or enforces a locked rule. An untidy `if` is not a reason.
- Add a layer, service, wrapper, class tree, shared API, queue, lock or retry system only when you can name why a local version fails. If a client can bypass a disabled UI state, add the backend guard first ([`architecture:authority`](code-structure.md#authority)).
- Simple never means shallow modules, duplicated domain logic, or skipping a real service for an independent domain.
- A big feature may add one named seam with one real implementation. Detail: [reference.md](../taste/reference.md#futureproofing).
- Reuse an existing one-job helper instead of forking it ([`architecture:primitives`](code-structure.md#primitives)). A small product change should touch one place per concept.
- Never extend a known-wrong shape. A behavior-preserving delete or move that removes a branch or layer happens when the goal or a named finding requires it; otherwise record a follow-up.

**Check:** could a simpler shape still pass? Use it.

## Named principles

In chat, cite each as **plain (Classic)** ([plain-language.md](../pack-shared/plain-language.md)): `We need to keep this simple (KISS).` Never acronym-only or plain-only. Placement rules live in [code-structure.md](code-structure.md).

| Principle | Classic | Meaning | Test |
| --- | --- | --- | --- |
| **Keep jobs apart** | SoC (Separation of Concerns) | UI, domain and I/O in different modules | Would a UI copy change force a billing rewrite? |
| **One altitude** | SLAP (Single Level of Abstraction) | Coordinate or do detail work, not both | Does it call services *and* parse or format? |
| **Read or write, not both** | CQS (Command Query Separation) | Change state or return data | Does a getter write? |
| **Fail fast** | Fail Fast | Reject bad input at the door | Is bad input caught before side effects? |
| **Leave it cleaner** | Boy Scout Rule | Touched files end a little cleaner, behavior unchanged | Did this edit copy a known mess? |
| **Related together** | Cohesion; Law of Demeter when the issue is `a.b.c` | What changes together lives together | Do callers reach through `a.b.c`? |
| **Safe to retry** | Idempotency | Repeating a request has the same effect | Can a double-submit duplicate a charge or row? |
| **Say what happens** | Explicit over implicit | Visible data and control flow | Can a new reader follow it without hidden context? |
| **No surprises** | PoLA (Principle of Least Astonishment) | Does what a careful reader expects | Would a side effect, return or name surprise a teammate? |
| **Honest names** | Intention-revealing names | Names match the current job | Does the path still describe the old job? |
| **Trust the server** | Never trust the client | Auth, ownership, money, permissions enforced on the write path | Could a caller skip the UI and still write? |
| **Types tell the truth** | Make illegal states unrepresentable | No `any`, no optional that is required, validators at the boundary | Would a lying type let bad data through? |

**SOLID** is guidance in [reference.md](../taste/reference.md), not a gate.

**Quality gates.** `test:quality` and the deliberate `test:mutants` (both from `/setup-toolkit`) check only: `any` and Convex `v.any`, empty `catch` and Result bags, public Convex writes with no identity helper, clock or randomness in a query, dead code (Knip), and surviving mutants (Stryker). Keep jobs apart, one altitude, read or write, no surprises, don't repeat yourself, and the rest of leave it cleaner stay review. No keep-jobs-apart import denylist. Never raise, skip or delete a gate, or lower the mutant break threshold, to go green.

**Check:** does the touched lane clearly break a row?

## Mechanical rules

| Rule | Classic | Meaning |
| --- | --- | --- |
| **Never-nest** | Guard clauses | Early returns, no `if` / `try` pyramids. Not about folders |
| **Cyclomatic cap** | Cyclomatic complexity (McCabe) | At most **5** paths per function; each `if`, loop, `catch`, `case`, ternary, and / or adds one. Extract a named helper (`test:quality`) |
| **Don't repeat yourself** | DRY | One concept, one place |
| **Reuse env vars** | none | See [Reuse env vars](#reuse-env-vars) |
| **No dead code** | Knip | No unused files, exports or dependencies (`test:quality`). Delete, do not ignore |
| **Kill the mutants** | Mutation testing | Behavior locks fail when Stryker flips an operator, boolean or sign (`test:mutants`, not in `test:quality`) |
| **Throw at boundaries** | Exceptions at boundaries | Catch only to recover, translate, add context or clean up. No `{ success: false }` / Result bags. No wrapping just because code could throw |
| **One export per file** | none | One component or main export |
| **Static imports** | none | No dynamic `import()` |
| **Comments** | none | Only to summarize big or complex functions |
| **Cite a sibling** | none | Mirror a **good** nearby feature or service; bad code is debt ([`architecture:prior-mistakes`](code-structure.md#prior-mistakes)) |
| **OOP depth cap** | Composition over deep inheritance | At most **two** levels (`PaymentMethod` ← `CardPayment`); compose instead of a third |
| **Plain language** | none | Chat cites plain (Classic); replies follow [writing-style.md](writing-style.md#unslop) |

Classes for stateful domain behavior (often the service), hooks for React state. Call sites import only the public entry. Prefer many small files in a service or feature folder over a god file.

**Check:** over 5 paths, deep nesting, or a Result bag?

## Reuse env vars

Before adding, renaming, requesting or reading a **new** environment variable:

1. List what exists: `.env.example`, committed `.env*` templates, `process.env` / `import.meta.env` usages, docs. Before writing a dashboard or CLI store, list it once (`npx convex env list`, `vercel env ls`, MCP env list). That list is for reuse, not ritual verify.
2. Match by job and value (site URL, API origin, database URL, webhook secret, auth issuer), not by the name you first thought of. Never store one value under two names.
3. A library wants another name: map in code (`const siteUrl = process.env.SITE_URL`). A platform prefix (`NEXT_PUBLIC_`, `VITE_`) goes only on the existing name, only when the runtime requires it.
4. Add a name only when no existing variable holds that job.

Example: `SITE_URL` exists. Read it (or `NEXT_PUBLIC_SITE_URL`). Never add `FRONTEND_URL` or `APP_URL`.

**Check:** does an existing variable already hold this value?

## Naming and files

| Area | Rule |
| --- | --- |
| App / UI / general TS | `lowercase-with-hyphens` (`use-checkout.ts`) |
| **Convex** `convex/**` | **No `-` or `_`** (`orders.ts`, `orderActions.ts`) |
| Folders | A named folder from the first file of a concern; no `utils` / `helpers` bags ([`architecture:folders`](code-structure.md#folders)) |
| **Honest names** | On rename, move or scope change, update filename, exports, types and variables in the same edit |

**Check:** would a reader open the right file from its name?

## Checklist

Before acceptance evidence and `/review` (a failed box is fixed first):

- [ ] `taste:keep-it-simple`: nothing beyond done when and the rules that must stay true
- [ ] Named principles: no clear violation in the touched lane
- [ ] `taste:never-nest` · `taste:cyclomatic-cap` · `taste:dont-repeat-yourself` · `taste:reuse-env` · `taste:no-dead-code` · `taste:kill-the-mutants` · `taste:throw-at-boundaries` · `taste:one-export-per-file` · `taste:static-imports` · `taste:oop-depth-cap` · `taste:naming-files`
- [ ] `taste:cite-a-sibling`: good sibling, greenfield, or correcting debt
- [ ] `taste:plain-language` in chat
- [ ] `taste:verify-terminals-first` ([reference.md](../taste/reference.md#verify-terminals-first))
- [ ] Structure matches [code-structure.md](code-structure.md)

`/review` Standards treats violations as **hard** unless the repo's own instructions contradict (repo wins).

## Apply

Apply this file and [code-structure.md](code-structure.md) as hard standards before grilling, planning, or non-trivial code (more than a typo), and whenever a pack skill other than `/ask-gabriel` runs. Do not skip because you know the pack or the change is one file. Keeping the existing structure is fine when it is the smallest correct answer.

- Judging a shape: Read `taste/examples.md` and `architecture/examples.md`; they illustrate, not replace.
- UI work: [taste/reference.md](../taste/reference.md#react-and-ui).
- `/task` done when for structure or UI includes: entry point, folder map, no Result bags, legal Convex names, jobs apart, identity on public writes, validated args.
- Plans never propose SOLID-heavy boilerplate or class trees deeper than two.

## Taste: do not

- Machinery without evidence, or copying a bad sibling
- A disabled button, hidden route or client `if` as authorization
- `any` on a public API, skipped validators, required data marked optional
- Ritual lint, typecheck or Convex MCP instead of reading terminals
- Acronym-only or plain-only principle names
- Never-nest or keep it simple as an excuse for a flat folder
- A synonym environment variable
- Restating code-structure rules here

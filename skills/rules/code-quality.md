# Code quality

Cite keys use the `quality:` prefix. Each key is a heading or rule name in this file.

These rules apply on every non-trivial change. Examples: [code-quality-examples.md](code-quality-examples.md). Verify: [tooling.md](tooling.md#verify-terminals-first). UI detail: [user-experience.md](user-experience.md#react-and-ui).

## Keep it simple

`quality:keep-it-simple` lives in [keep-it-simple.md](keep-it-simple.md). Open it before adding a file, folder, layer, or abstraction.

## Named principles

In chat, cite each as **plain (Classic)** ([Plain language](writing-style.md#plain-language)): `We need to keep this simple (KISS).` Never acronym-only or plain-only. Placement rules live in [code-structure.md](code-structure.md).

Six checks adapt poteto's principles from [pstack](https://github.com/backnotprop/pstack) (MIT), under this pack's names: keep it simple (KISS), light to read (Minimize reader load), fail fast (Fail Fast), subtract first (Subtract before you add), safe to retry (Idempotency), and types tell the truth (make illegal states unrepresentable). The cite keys stay this pack's.

| Principle | Classic | Meaning | Test |
| --- | --- | --- | --- |
| **Keep jobs apart** | SoC (Separation of Concerns) | UI, domain and I/O in different modules | Would a UI copy change force a billing rewrite? |
| **One altitude** | SLAP (Single Level of Abstraction) | Coordinate or do detail work, not both | Does it call services *and* parse or format? |
| **Light to read** | Minimize reader load | Few layers between the question and the answer, and little hidden state to hold | Can a new reader say where X comes from, and what can change X, without a tour? |
| **Read or write, not both** | CQS (Command Query Separation) | Change state or return data | Does a getter write? |
| **Fail fast** | Fail Fast | Reject bad input at the system boundary. Inside, trust the type. Domain logic stays a pure function the shell calls | Is this value crossing a system boundary right now? If not, the check is redundant |
| **Leave it cleaner** | Boy Scout Rule | Touched files end a little cleaner, behavior unchanged | Did this edit copy a known mess? |
| **Subtract first** | Subtract before you add | On the path this change extends, remove the dead weight first, then build on what remains | Did this diff add onto code it should have deleted? |
| **Related together** | Cohesion; Law of Demeter when the issue is `a.b.c` | What changes together lives together | Do callers reach through `a.b.c`? |
| **Safe to retry** | Idempotency | A command, lifecycle step, or retry loop reaches the same end state if it runs twice or the last run crashed halfway | Does a second run, or a resume, still depend on leftover partial state? |
| **Say what happens** | Explicit over implicit | Visible data and control flow | Can a new reader follow it without hidden context? |
| **No surprises** | PoLA (Principle of Least Astonishment) | Does what a careful reader expects | Would a side effect, return or name surprise a teammate? |
| **Honest names** | Intention-revealing names | Names match the current job | Does the path still describe the old job? |
| **Trust the server** | Never trust the client | Auth, ownership, money, permissions enforced on the write path | Could a caller skip the UI and still write? |
| **Types tell the truth** | Make illegal states unrepresentable | No `any`, no optional that is required, no field bag that can contradict, no cast that silences the checker. Brand ids that must not mix. Parse at the boundary. Exhaust variants. Derive from the schema that already owns the shape | Would a comment be required to say which field combinations are valid? |

**SOLID** is guidance ([Patterns and SOLID](#patterns-and-solid)), not a hard rule.

**Check:** does the touched lane clearly break a row?

### Light to read

`quality:light-to-read` lives in [keep-it-simple.md](keep-it-simple.md#while-you-shape-it).

### Subtract first

`quality:subtract-first` lives in [keep-it-simple.md](keep-it-simple.md#before-you-add).

### Fail fast

`quality:fail-fast`. When wiring validation, errors, or a framework adapter. Pairs with [`quality:throw-at-boundaries`](#mechanical-rules).

- At a system boundary (request, config, env, external API, network, database row): validate, parse into a domain type, and throw.
- Inside: trust that type. Do not re-check a value the boundary already parsed, and do not scatter nil checks down the chain.
- Domain logic is a pure function the shell calls. It does not import the framework, the SDK, or the wire type.
- The public surface exposes the domain type, not the transport or storage type.

**Check:** is this value crossing a system boundary right now? Can this be a pure function the shell calls?

### Safe to retry

`quality:safe-to-retry`. When designing a command, a lifecycle step, a webhook, or a loop that can crash, restart, or run again. A read with no side effect does not apply.

- A second run in a row reaches the same end state.
- A resume after a crash at any step reaches that same end state. Reconcile leftover partial state. Do not treat "how far the last run got" as truth unless the resume is the design.
- A failed unit of work can run again without a second side effect. Key the side effect before it happens.
- Cleanup compares content, not creation order.

**Check:** if this runs twice, or the last run died halfway, does the end state still depend on what was left behind?

### Types tell the truth

`quality:types-tell-the-truth`. When designing a type or a signature. Parsing of external data lives at the boundary ([Fail fast](#fail-fast)).

- Model variants as a sum (`{ kind: "open" } | { kind: "done"; at: Date }`). A bag of fields that can contradict (`completed: true` with no `completedAt`) is a lie.
- Build the shape that cannot hold the illegal value. A non-empty list is a head plus a rest, not a list plus a length check.
- Brand ids that must not mix (`UserId` and `OrderId`). Validate once at creation, then trust the type.
- External data (JSON, RPC, env, database rows, CLI) stays untyped until a parse at the boundary. No `as` cast to silence the checker.
- A match on a variant must fail to compile when a new case has no handler (`never` in the default).
- If a schema already owns the shape (Convex validators, an OpenAPI spec, a generated client), derive from it. Do not hand-roll a parallel type.
- Strengthen a type only where a runtime check would otherwise throw. An operation that is total on the plain type (`sum` of an empty list is 0) keeps the plain type.

**Check:** would a comment be required to say which combinations are valid? Do two arguments share a primitive type and mean different things?

## Mechanical rules

| Rule | Classic | Meaning |
| --- | --- | --- |
| **Never-nest** | Guard clauses | Early returns, no `if` / `try` pyramids. Not about folders |
| **Cyclomatic cap** | Cyclomatic complexity (McCabe) | At most **5** paths per function; each `if`, loop, `catch`, `case`, ternary, and / or adds one. Extract a named helper. Never raise the cap. How to check: [static-checks.md](../review/static-checks.md#cyclomatic-complexity-cap-of-5) |
| **Don't repeat yourself** | DRY | One concept, one place |
| **Reuse env vars** | none | See [Reuse env vars](#reuse-env-vars) |
| **No dead code** | none | No unused files, exports or dependencies. Delete, do not ignore. How to check: [static-checks.md](../review/static-checks.md#knip-no-dead-code) |
| **Throw at boundaries** | Exceptions at boundaries | Catch only to recover, translate, add context or clean up. No `{ success: false }` / Result bags. No wrapping just because code could throw. Inside the boundary, trust the parsed type ([Fail fast](#fail-fast)) |
| **One export per file** | none | One component or main export |
| **Static imports** | none | No dynamic `import()` |
| **Comments** | none | Only to summarize big or complex functions |
| **Cite a sibling** | none | The pack's examples beat the app's existing code, on shape and on naming. Copy an app sibling only when it matches the rules and a named example, and say which example. Otherwise build from the example; the old code is debt ([`structure:prior-mistakes`](code-structure.md#prior-mistakes)). What the framework requires (route file names, Convex function rules) is not an app habit and still applies. Never build a second copy of a job an existing service owns: call it or extend it |
| **OOP depth cap** | Composition over deep inheritance | At most **two** levels (`PaymentMethod` ← `CardPayment`); compose instead of a third |
| **Plain language** | none | Chat cites plain (Classic); replies follow [writing-style.md](writing-style.md#unslop) |

Classes for stateful domain behavior (often the service), hooks for React state. Call sites import only the public entry. Prefer many small files in a service or feature folder over a god file.

**Check:** over 5 paths, deep nesting, or a Result bag?

## Reuse env vars

Reuse existing env vars by job. Before adding, renaming, requesting or reading a **new** environment variable:

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
| Folders | A named folder from the first file of a concern; no `utils` / `helpers` bags ([`structure:folders`](code-structure.md#folders)) |
| **Honest names** | On rename, move or scope change, update filename, exports, types and variables in the same edit |

**Check:** would a reader open the right file from its name?

## Patterns and SOLID

Patterns, SOLID, and interface theater live in [strong-foundation.md](strong-foundation.md#build-it). Tiny glue gets no ceremony: a plain function or single class ([keep-it-simple.md](keep-it-simple.md)).

## Futureproofing

Lives in [strong-foundation.md](strong-foundation.md): a strong first iteration with a seam on each area of modularity, scaled to the work.

## Checklist

Before acceptance evidence and `/review` (a failed box is fixed first):

- [ ] `quality:keep-it-simple`: nothing beyond done when and the rules that must stay true
- [ ] `quality:strong-foundation`: a Feature has a seam on each confirmed area of modularity, and nothing else
- [ ] Named principles, including `quality:light-to-read` and `quality:subtract-first`: no clear violation in the touched lane
- [ ] `quality:never-nest` · `quality:cyclomatic-cap` · `quality:dont-repeat-yourself` · `quality:reuse-env` · `quality:no-dead-code` · `quality:throw-at-boundaries` · `quality:one-export-per-file` · `quality:static-imports` · `quality:oop-depth-cap` · `quality:naming-files`
- [ ] `quality:cite-a-sibling`: the example this code matches, and the app sibling that matches it too, if any
- [ ] `quality:plain-language` in chat
- [ ] `quality:verify-terminals-first` ([tooling.md](tooling.md#verify-terminals-first))
- [ ] Structure matches [code-structure.md](code-structure.md)

`/review` Standards treats violations as **hard** unless the repo's own instructions contradict (repo wins).

## Apply

Apply this file and [code-structure.md](code-structure.md) as hard standards before grilling, planning, or non-trivial code (more than a typo), and whenever a pack skill other than `/ask-gabriel` runs. Do not skip because you know the pack or the change is one file. Keeping the existing structure is fine when it is the smallest correct answer.

- Judging a shape: Read [code-quality-examples.md](code-quality-examples.md) and [code-structure-examples.md](code-structure-examples.md); they illustrate, not replace.
- UI work: [React and UI](user-experience.md#react-and-ui).
- `/task` done when for structure or UI includes: entry point, folder map, no Result bags, legal Convex names, jobs apart, identity on public writes, validated args.
- Plans never propose SOLID-heavy boilerplate or class trees deeper than two.

## Taste: do not

- Machinery without evidence, or copying an app sibling no example backs
- A pass-through layer, or a new path beside the one this change should have deleted
- A second check inside, after the boundary already parsed the value
- A disabled button, hidden route or client `if` as authorization
- `any` on a public API, skipped validators, required data marked optional
- Ritual lint, typecheck or Convex MCP instead of reading terminals
- Acronym-only or plain-only principle names
- Never-nest or keep it simple as an excuse for a flat folder
- A synonym environment variable
- Restating code-structure rules here

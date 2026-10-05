# Code quality

Cite keys use the `quality:` prefix. Each key is a heading or rule name in this file.

Treat this file and [code-structure.md](code-structure.md) as hard standards before grilling, planning, or non-trivial code (more than a typo), and whenever a pack skill other than `/ask-gabriel` runs. That holds for one-file changes and when you know the pack. Keeping the existing structure is fine when it is the smallest correct answer.

Examples (illustrations only): [code-quality-examples.md](code-quality-examples.md), [code-structure-examples.md](code-structure-examples.md). UI detail: [user-experience.md](user-experience.md#react-and-ui).

## Checklist

This checklist is enough for a small change. Open a section below only when a row applies.

- [ ] `quality:keep-it-simple`: nothing beyond done when and the rules that must stay true
- [ ] `quality:strong-foundation`: a Feature has a seam (a named extension point where a new variant plugs in) on each confirmed area of modularity, and nothing else
- [ ] Named principles, including `quality:light-to-read` and `quality:subtract-first`: no clear violation in the touched area
- [ ] `quality:never-nest`, `quality:cyclomatic-cap`, `quality:dont-repeat-yourself`, `quality:reuse-env`, `quality:no-dead-code`, `quality:throw-at-boundaries`, `quality:one-export-per-file`, `quality:static-imports`, `quality:oop-depth-cap`, `quality:naming-files`
- [ ] `quality:cite-a-sibling`: the example this code matches, and the app sibling that matches it too, if any
- [ ] `quality:plain-language` in chat
- [ ] `quality:verify-terminals-first` ([tooling.md](tooling.md#verify-terminals-first))
- [ ] Structure matches [code-structure.md](code-structure.md)

Run it before acceptance evidence and `/review`; fix a failed box first. `/review` Standards treats violations as **hard** unless the repo's own instructions contradict. `/task` done when for structure or UI includes: entry point, folder map, no Result bags, legal Convex names, jobs apart, identity on public writes, validated args.

## Keep it simple

`quality:keep-it-simple` lives in [keep-it-simple.md](keep-it-simple.md). Open it before adding a file, folder, layer, or abstraction.

## Named principles

In chat, cite each as **plain (Classic)** ([Plain language](writing-style.md#plain-language)): `We need to keep this simple (KISS).`
Design, verification, and delegation judgments open [principles.md](principles.md). That file points here for fail fast and types. It does not restate this table.
Six checks (keep it simple, light to read, fail fast, subtract first, safe to retry, types tell the truth) adapt poteto's [pstack](https://github.com/backnotprop/pstack) principles (MIT).

| Principle | Classic | Meaning | Test |
| --- | --- | --- | --- |
| **Keep jobs apart** | SoC (Separation of Concerns) | UI, domain and I/O in different modules | Would a UI copy change force a billing rewrite? |
| **One altitude** | SLAP (Single Level of Abstraction) | Coordinate or do detail work, not both | Does it call services *and* parse or format? |
| **Light to read** | Minimize reader load | Few layers and little hidden state between a question and its answer | Can a new reader say where X comes from, and what can change X, without a tour? |
| **Read or write, not both** | CQS (Command Query Separation) | Change state or return data | Does a getter write? |
| **Fail fast** | Fail Fast | Reject bad input at the system boundary. Inside, trust the type | Is this value crossing a boundary now? If not, drop the check |
| **Leave it cleaner** | Boy Scout Rule | Touched files end a little cleaner, behavior unchanged | Did this edit copy a known mess? |
| **Subtract first** | Subtract before you add | Remove dead weight on the path this change extends, then build on what remains | Did this diff add onto code it should have deleted? |
| **Related together** | Cohesion; Law of Demeter when the issue is `a.b.c` | What changes together lives together | Do callers reach through `a.b.c`? |
| **Safe to retry** | Idempotency | Same end state on rerun or resume | Does a rerun or resume depend on leftover partial state? |
| **Say what happens** | Explicit over implicit | Visible data and control flow | Can a new reader follow it cold? |
| **No surprises** | PoLA (Principle of Least Astonishment) | Does what a careful reader expects | Would a side effect, return or name surprise a teammate? |
| **Honest names** | Intention-revealing names | Names match the current job | Does the path still describe the old job? |
| **Trust the server** | Never trust the client | Auth, ownership, money, permissions enforced on the write path | Could a caller skip the UI and still write? |
| **Types tell the truth** | Make illegal states unrepresentable | No `any`, no optional that is required, no cast that silences the checker. More below | Would a comment be required to say which field combinations are valid? |

### Light to read

`quality:light-to-read` lives in [keep-it-simple.md](keep-it-simple.md#while-you-shape-it).

### Subtract first

`quality:subtract-first` lives in [keep-it-simple.md](keep-it-simple.md#before-you-add).

### Fail fast

`quality:fail-fast`. When wiring validation, errors, or a framework adapter; pairs with [`quality:throw-at-boundaries`](#mechanical-rules).

- At a system boundary (request, config, env, external API, network, database row): validate, parse into a domain type, and throw.
- Inside: trust that type. Re-checks and nil checks down the chain are redundant once the boundary parsed the value.
- Domain logic is a pure function the shell calls, free of framework, SDK, and wire types.
- The public surface exposes the domain type, not the transport or storage type.

### Safe to retry

`quality:safe-to-retry`. When designing a command, a lifecycle step, a webhook, or a loop that can crash, restart, or run again. A read with no side effect does not apply.

- A second run in a row, and a resume after a crash at any step, reach the same end state. Reconcile leftover partial state. Treat "how far the last run got" as truth only when the resume is the design.
- A failed unit of work can run again without a second side effect. Key the side effect before it happens.
- Cleanup compares content, not creation order.

### Types tell the truth

`quality:types-tell-the-truth`. When designing a type or a signature. Parse external data at the boundary ([Fail fast](#fail-fast)).

- Model variants as a sum (`{ kind: "open" } | { kind: "done"; at: Date }`). A field bag that can contradict (`completed: true` with no `completedAt`) is a lie.
- Build the shape that cannot hold the illegal value: a non-empty list is a head plus a rest, not a list plus a length check.
- Brand ids that must not mix (`UserId`, `OrderId`). Validate once at creation, then trust the type.
- Keep external data (JSON, RPC, env, database rows, CLI) untyped until parsed at the boundary. Parse instead of silencing the checker with `as`.
- Make a variant match fail to compile when a new case has no handler (`never` in the default).
- If a schema already owns the shape (Convex validators, OpenAPI spec, generated client), derive from it so no parallel type can drift.
- Strengthen a type only where a runtime check would otherwise throw; an operation total on the plain type (`sum` of an empty list is 0) keeps it.

**Check:** do two arguments share a primitive type and mean different things?

## Mechanical rules

| Rule | Classic | Meaning |
| --- | --- | --- |
| **Never-nest** | Guard clauses | Early returns, no `if` / `try` pyramids. Not about folders |
| **Cyclomatic cap** | Cyclomatic complexity (McCabe) | At most **5** paths per function; each `if`, loop, `catch`, `case`, ternary, and / or adds one. Extract a named helper. Never raise the cap. How to check: [static-checks.md](../review/static-checks.md#cyclomatic-complexity-cap-of-5) |
| **Don't repeat yourself** | DRY | One concept, one place |
| **Reuse env vars** | none | See [Reuse env vars](#reuse-env-vars) |
| **No dead code** | none | Delete unused files, exports and dependencies instead of ignoring them. How to check: [static-checks.md](../review/static-checks.md#knip-no-dead-code) |
| **Throw at boundaries** | Exceptions at boundaries | Catch only to recover, translate, add context or clean up. Signal failure by throwing, not with `{ success: false }` / Result bags |
| **One export per file** | none | One primary responsibility, usually one component or main export; [cohesive exports](#cohesive-exports) keep related public operations and framework-required exports together |
| **Static imports** | none | Static `import` only, not dynamic `import()` |
| **Comments** | none | Only to summarize big or complex functions |
| **Cite a sibling** | none | The pack's examples beat the app's existing code, on shape and on naming. Copy an app sibling only if it matches the rules and a named example (say which). Otherwise build from the example; the old code is debt ([`structure:prior-mistakes`](code-structure.md#prior-mistakes)). Framework requirements (route file names, Convex function rules) are not app habits and still apply. When an existing service owns a job, call or extend it |
| **OOP depth cap** | Composition over deep inheritance | At most **two** levels (`PaymentMethod` ← `CardPayment`); compose instead of a third |
| **Plain language** | none | Replies follow [writing-style.md](writing-style.md#unslop) |

## Cohesive exports

The rule prevents unrelated public responsibilities sharing a file, not a
literal export-count limit. A domain entry may expose closely related operations
and their contract types; framework entry files may keep required exports.
Keep that public surface small and clear, with implementation collaborators
private to its owner. Do not split cohesive operations into one-function files
or add barrel/pass-through exports merely to satisfy a count. Separate exports
when their behavior, dependencies, or reasons to change belong to different
owners ([responsibility boundaries](code-structure.md#responsibility-boundaries)).

## Reuse env vars

Before adding, renaming, requesting or reading a **new** environment variable:

1. List what exists: `.env.example`, committed `.env*` templates, `process.env` / `import.meta.env` usages, docs. Before writing a dashboard or CLI store, list it once (`npx convex env list`, `vercel env ls`, MCP env list), for reuse only.
2. Match by job and value (site URL, API origin, database URL, webhook secret, auth issuer), not by the name you first thought of. Keep each value under one name.
3. If a library wants another name, map it in code (`const siteUrl = process.env.SITE_URL`). Put a platform prefix (`NEXT_PUBLIC_`, `VITE_`) only on the existing name, only when the runtime requires it.
4. Add a name only when no variable holds that job.

Example: `SITE_URL` exists. Read it (or `NEXT_PUBLIC_SITE_URL`); `FRONTEND_URL` or `APP_URL` would duplicate it.

## Naming and files

| Area | Rule |
| --- | --- |
| App / UI / general TS | `lowercase-with-hyphens` (`use-checkout.ts`) |
| **Convex** `convex/**` | **No `-` or `_`** (`orders.ts`, `orderActions.ts`) |
| Folders | Named folder from the first file of a concern: [`structure:folders`](code-structure.md#folders) |
| **Honest names** | On rename, move or scope change, update filename, exports, types and variables in the same edit |

## Patterns and SOLID

SOLID is guidance, not a hard rule. Patterns, SOLID, and interface theater live in [strong-foundation.md](strong-foundation.md#build-it). Tiny glue is a plain function or single class ([keep-it-simple.md](keep-it-simple.md)). Plans stay free of SOLID-heavy boilerplate and class trees deeper than two.

## Futureproofing

Lives in [strong-foundation.md](strong-foundation.md).

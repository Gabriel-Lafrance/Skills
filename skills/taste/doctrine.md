# Taste Flow Doctrine

Shared style contract for this pack. **Other pack skills must read this before planning or writing code.**

For good vs bad snippets, see [examples.md](examples.md).

## KISS — Keep It Stupid Simple

**Default to the stupid-simple solution that still meets the outcome and Active Rules.** Cleverness, ceremony, and speculative architecture are costs — pay them only when evidence demands it.

| Do | Do not |
| --- | --- |
| Straight-line happy path; obvious names; one clear owner | Indirection “for cleanliness,” premature seams, config for imaginary products |
| Inline a one-call-site guard | Extract a helper/file/class that only wraps that guard |
| A plain function or single class for tiny glue | Pattern theater (factory-of-factories, empty bases, one-line “impl” files) |
| Deep entry when richness already exists | Shallow APIs that force every caller to orchestrate steps |

KISS does **not** mean shallow modules, duplicated domain logic, or skipping a real service when the domain is independent. It means: **simple surface, no extra moving parts.** When KISS and futureproofing conflict on a **big** feature, name the required seam — then keep everything else stupid simple (seam + one real impl, not a hierarchy of unused extension points).

## Named principles

Apply these with keep-it-simple. Plain names, operational tests — not essays. In chat with the user, use these plain names only ([plain-language.md](../pack-shared/plain-language.md)). Structural placement (services, folders) also lives in `/architecture`.

| Principle | Meaning | Test |
| --- | --- | --- |
| **Keep jobs apart** | UI, domain, and I/O change for different reasons — keep them in different modules. | Would a UI copy change force a billing rewrite? If yes, jobs are mixed. |
| **One altitude** | A function either coordinates *or* does detail work, not both. | Does this function both call services *and* parse bytes / format strings? Split it. |
| **Read or write, not both** | A method either changes state or returns data — not both. | Does a getter also write? Does a command hide a write behind a “get”? Fix the shape. |
| **Fail fast** | Reject bad input at the door; do not limp along. | Is bad input caught at the entry, or deep inside after partial side effects? |
| **Leave it cleaner** | Leave the files you touched a little cleaner (without changing behavior). | Did this edit copy a known mess, or slightly clean paths you already touched? |
| **Related together** | Things that change together live together; callers use a small public surface. | Do unrelated jobs share a file? Do callers reach through `a.b.c` internals? |
| **Safe to retry** | Repeating the same request has the same effect (payments, webhooks, retries, writes). | Can a double-submit create a duplicate charge, row, or side effect? |
| **Say what happens** | Prefer clear data and control flow over magic. | Can a new reader see *what happens* without chasing hidden context? |
| **No surprises** | APIs and UI behave as a careful reader expects. | Would a teammate be surprised by a side effect, return value, or name? |
| **Honest names** | File paths, exports, functions, types, and variables match the *current* job — rename when the job changes. | After a rename, does the path still describe the old job? Would a reader open the wrong file? |
| **Trust the server** | UI and client checks are feedback. Auth, ownership, money, and permissions are enforced on the write path. | Could a caller skip the UI (or toggle a client flag) and still perform the write? If yes, the lock is missing. |
| **Types tell the truth** | Public args, returns, and stored fields match reality: no `any`, no optional that is required, validators at the boundary. | Would a lie in the type or a missing validator let bad data through? |

**How they relate:** Keep-jobs-apart + related-together shape *where* code lives (`/architecture` services). One-altitude, read-or-write, say-what-happens, no-surprises, and honest names shape *how* a unit reads. Fail fast + safe-to-retry + trust-the-server shape *boundaries*. Types-tell-the-truth shapes *contracts*. Leave-it-cleaner shapes *edits in messy files*.

## Bad code = complexity and entropy

**Bad code** is whatever **increases complexity** or **entropy**. **Good code** is **KISS first**, deep where it matters (simple surface, rich inside), built from **strong primitives** inside services / deep modules (`/architecture` §3), orthogonal by service, and leaves the touched lane cleaner or no dirtier than before.

| Term | Meaning |
| --- | --- |
| **Complexity** | Change amplification, cognitive load, unknown unknowns — hard to understand or change safely. Prefer fewer concepts at the call site; put richness behind a **deep** entry (`/architecture` deep public surface). Forking a **primitive's** one job locally amplifies change. |
| **Entropy** | Local disorder that spreads when copied or left untouched in a lane you edit (broken windows). Touching a dirty lane without a **behavior-preserving cleanup** when you can preserve behavior **increases** entropy. Forking or bypassing an existing primitive's job is entropy. |

**Operational tests** (apply before shipping a slice):

1. **KISS** — Is there a stupider-simple shape that still meets Done when and Active Rules? Prefer it.
2. **Principles** — keep jobs apart, one altitude, read or write not both, fail fast, leave it cleaner, related together, safe to retry, say what happens, no surprises, honest names, trust the server, types tell the truth — any clear violation in the touched lane?
3. **Call-site** — Does the caller need internals / order / edge cases? → shallow / complex.
4. **Change** — Would a small product change touch many files for one concept? → complexity (amplification).
5. **Window** — Are we copying or extending a known-wrong shape? → entropy.
6. **Judo** — Is there a behavior-preserving delete/move that removes a whole branch or layer? → do it when the active goal or a named finding requires it; otherwise record a follow-up.
7. **Primitive** — Does an existing one-job block already answer this? Reuse it; do not fork.
8. **Server** — Can a caller bypass the UI and still write? → missing authority (`trust the server`).
9. **Types** — `any`, a missing boundary validator, or optional-that-is-required? → the contract is a lie.

## Abstraction budget

Prefer the smallest clear shape that fulfills the assigned outcome and Active Rules (**KISS**). Keep a one-call-site guard inline when it has one local purpose; extract it only when the extraction owns independent behavior, removes real duplication, or is required to enforce a locked invariant.

Before adding a new layer, file, service, wrapper, class hierarchy, shared API, queue, lock, retry system, or other coordination machinery, identify the evidence that a local implementation cannot meet the rule safely. A UI-disabled state is user feedback; if a client can bypass it, add the direct authoritative backend/state-transition guard before proposing coordination infrastructure.

This budget does not prohibit a real service, deep module, or extension seam for a genuinely independent domain capability or explicitly planned growth. It prohibits speculative ceremony, identity wrappers, one-off helper files, and abstractions created only because a local `if` looks untidy.

Non-negotiables below are **consequences** of keep-it-simple + named principles + this definition (never-nest, don’t repeat yourself, cite a good sibling / move debt, one job per unit, easy happy path). Architecture applies keep-jobs-apart / related-together / safe-to-retry writes to structure; `/code-review` blocks regressions.

## Non-negotiables

1. **Keep it simple** — no cleverness or extra machinery without evidence it is required
2. **Named principles** — keep jobs apart, one altitude, read or write not both, fail fast, leave it cleaner, related together, safe to retry, say what happens, no surprises, honest names, trust the server, types tell the truth (see table above)
3. **Never-nest** — flatten control flow; extract early instead of deep `if`/`try` pyramids
4. **Don’t repeat yourself** — one concept, one place; no copy-paste twins
5. **Throw + purposeful try/catch** at boundaries that recover, translate, add actionable context, or clean up — never `{ success: false }` / Result bags for expected failure control flow; do not wrap local code merely because it could throw (**fail fast** at the boundary)
6. **One component (or main export) per file**
7. **No dynamic `import()`** — static imports only
8. **Comments only** to summarize big/complex functions — no narrating obvious code
9. **Cite a sibling** — before inventing shape, mirror a **good** nearby feature **or existing service** that matches this taste + `/architecture`. Bad nearby code is a **debt** signal, not a template — when you touch that lane, prefer a **behavior-preserving move** (see `/architecture` §4 Prior mistakes) (**leave it cleaner** when you can preserve behavior)
10. **Smart responsibility** — a unit does one job well (a logger only logs; it does not format emails or hit the DB) (**keep jobs apart**)
11. **Easy to follow** — a reader can walk the happy path without branching into unrelated concerns (**say what happens**, **no surprises**)
12. **Honest names** — when responsibility or scope changes, rename the file and the symbols in the same change; do not keep writing into a stale path or under an old identifier
13. **Don't spam verify** — read existing terminals first; no ritual lint/typecheck/Convex MCP (see Verify)
14. **Plain language** — humans must understand without decoding jargon or abbreviations ([plain-language.md](../pack-shared/plain-language.md))
15. **Trust the server** — never treat a disabled button, hidden route, or client `if` as authorization; public writes check identity and ownership
16. **Types tell the truth** — no `any` on public surfaces; validate args and returns at the door; do not mark required data optional to silence the compiler

## Verify (terminals first — not MCP)

This author almost always has **frontend localhost** and **`npx convex dev`** already running. CI owns type/lint. **Do not** re-verify by poking Convex MCP, re-running `convex` CLI, or spamming status tools.

**Prefer, in order:**

1. **Read existing terminal output** (IDE terminals folder / running `convex dev` + frontend logs) for push success, compile errors, HMR, runtime stacks
2. Diff + structural checks for the change
3. Only if terminals are silent/missing: say so — then ask, or start the **minimal** command once

**Do not** by default (ritual anti-patterns):

- Call **Convex MCP** (`status`, `data`, `tables`, `logs`, `run`, `runOneoffQuery`, `insights`, `functionSpec`, env tools, etc.) "just to verify"
- Re-run `npx convex …`, deploy, or codegen after every slice when `convex dev` is already watching
- Run `eslint`, `tsc --noEmit`, `npm run lint`, full suites, or "just to be sure" scripts
- Start a second frontend/Convex process when one is already up
- Dispatch a subagent whose only job is MCP verification

**Do use Convex MCP / deeper checks only when:**

- Terminals show an error you cannot diagnose from the log text alone
- You need a one-off data read the user asked for
- No Convex terminal exists and you said so first
- The user explicitly asks for MCP/dashboard/CLI verification

Evidence citations should look like: `terminals/3.txt — convex push ok` — not a fresh MCP round-trip.

## Futureproofing (open to extend, closed to break)

When building a **non-trivial / big feature**, build a **bulletproof foundation from day one** so growth is additive — not a rewrite every time something is added. Still apply **KISS** to everything that is not the named seam:

- **Open to extension** — new behavior lands via new collaborators, strategies, or narrow hooks — not by rewriting call sites
- **Closed to breaking edits** — stable entry-point signatures; avoid forcing callers to change when internals grow
- **Put the seam in first** — interfaces / strategy slots / composition points belong in the initial design when the domain will grow (payments, notifiers, providers, channels, etc.). Do **not** wait for a "second implementation" before shaping the foundation — that causes perma re-editing
- Ship **one real implementation** behind that seam on day one; the seam is the foundation, not unused dead code
- Do **not** future-proof tiny one-off glue with empty hierarchies or config for imaginary products (**KISS**)

Plans and structure cards **must** name the extension seam for big features.

## Shape (with `/architecture`)

- **Services** own domain concerns (billing, auth, …) with a small public API — features call them; never reimplement per feature
- **Primitives** — small, strong-yet-flexible, one-job blocks **inside** services and deep modules; reuse independently without breaking; explore and compose, do not fork (`/architecture` §3)
- Prefer **OOP** (class / abstract class) for stateful domain behavior and shared lifecycle (often *is* the service)
- Prefer **hooks** for React state/effects; **services** (module/class/facade) for shared domain I/O
- Call sites import the **simple entry point / service public API** only — hide collaborators and primitives behind that surface
- Prefer over-splitting files inside a service or feature folder over god files
- Cite a **good** sibling feature **or existing service** when one exists — do not copy debt; move/correct when touching that lane (`/architecture` prior-mistakes)

### OOP depth cap

Keep inheritance / interface stacks **shallow**:

- At most **two** levels of class or interface nesting in a chain (e.g. `PaymentMethod` ← `CardPayment` — stop there)
- Prefer composition over a third layer
- If you need depth 3+, the design is wrong for this taste — flatten or compose

### Patterns & SOLID (pragmatic)

- **Refactoring Guru–style patterns** are welcome when they suit a useful case (Strategy, Facade, Adapter, Observer, etc.)
- **Big features:** lay the foundation early — seam + first implementation — so adding the next variant does not reopen the core
- **Tiny glue / local helpers:** skip ceremony; a plain function or single class is enough (**KISS**)
- **SOLID is guidance, not scripture** — use it to keep foundations extendable and readable; stop when it becomes interface theater (factory-of-factories, empty base classes, one-line "impl" files with no behavior)
- Never require a second production implementation *before* introducing the seam on a big feature — that is the opposite of this taste

## Naming & files

| Area | Rule |
| --- | --- |
| App / UI / general TS | `lowercase-with-hyphens` (`use-checkout.ts`, `order-summary.tsx`) |
| **Convex** `convex/**` | **No `-` or `_` in filenames** (`orders.ts`, `orderActions.ts`) |
| Folders | Feature/domain folders before flat dumps; no anonymous `utils` / `helpers` bags |
| **Honest names** | Path and primary export describe today's job. After a rename, move, or scope change: update the filename, exports, types, functions, and variables in the same edit — never leave new logic under the old name |

## React & UI

- **Mobile first**, then widen
- One component per file; keep components thin — complexity in hook/class behind the entry
- When touching marketing/landing UI, avoid AI-default looks: purple-on-white gradients, cream+terracotta serif clichés, flat single-color voids, card-heavy heroes, pill clusters, emoji decoration
- Landing first viewport: brand + one headline + one line + CTA + one dominant image — nothing else

## Errors

```typescript
// Good
try {
  await charge(order);
} catch (error) {
  throw new Error("Payment failed", { cause: error });
}

// Bad
return { success: false, error: "Payment failed" };
```

## Planning & spec (how other skills use this)

When `/goal` writes what “done” means (or a ticket-driven goal does), include **taste-relevant** checks when the change touches structure/UI — e.g. entry point exists, folder map followed, extension seam named (if big feature), no Result bags, Convex names legal, responsibilities not mixed, public writes check identity/ownership, public args are validated. When structure is in play, those checks may include: **callers stay thin; complexity behind service X** (simple public surface; one-job helpers reused not copied). Parents must already have loaded `/architecture` this turn ([standards.md](../pack-shared/standards.md)); do not skip that Read for a “small” slice.

Plans must not propose shapes that violate this file (including SOLID-maximalist boilerplate or class trees deeper than two).

## Implement self-check (required each slice)

- [ ] **Keep it simple** — no extra layer, file, wrapper, pattern, or config beyond what Done when / rules that must stay true require
- [ ] **Principles** — no clear keep-jobs-apart / one-altitude / read-or-write / fail-fast / leave-it-cleaner / related-together / safe-to-retry / say-what-happens / no-surprises / honest-names / trust-the-server / types-tell-the-truth violation in the touched lane
- [ ] **Plain language** — user-facing chat has no unexplained jargon or abbreviations
- [ ] Sibling pattern cited is a **good** one (or explicitly "greenfield" / correcting debt)
- [ ] Entry point + folder match `/architecture` card (including **Moves / corrections**, **Primitives**, and **Authority**)
- [ ] Did not copy a bad sibling — moved/corrected when the lane had prior mistakes
- [ ] Change **reduces or holds complexity** at call sites (deep entry, not shallower)
- [ ] Touched lane: **did not copy a known-wrong shape** (did not extend a mess without a move; did not copy a one-job helper’s job)
- [ ] Naming rules above (especially Convex) — file path + symbols match current responsibility after any rename/scope change
- [ ] No nesting pyramids / no dynamic import / no `success: false`
- [ ] Public writes check identity and ownership; UI-only guards are not the lock
- [ ] Public args/returns are typed and validated; no `any` on the new surface
- [ ] One main export per new file
- [ ] Each new type has one clear responsibility (no logger-that-also-sends-mail)
- [ ] Class/interface chain ≤ 2 deep; composition if more is needed
- [ ] Big feature: foundation seam + first impl shipped together (no "wait for second impl"); entry signature stays stable
- [ ] Did not ritual-run lint/typecheck **or Convex MCP**; checked existing terminal output instead (unless terminals errored / user asked)

Fail any box → fix before acceptance evidence and `/code-review`.

## Review

`/code-review` Standards axis treats violations of this file as **hard** unless the repo's own `AGENTS.md` / `.cursor/rules` contradict (repo wins on conflict).

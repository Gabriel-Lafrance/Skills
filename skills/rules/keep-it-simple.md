# Keep it simple

**Open this when:** you are about to add a file, folder, layer, helper, wrapper, piece of state, validator, or abstraction, or you are refactoring, rewriting, or sizing a diff.
**Skip it and you will:** build for an imaginary product, and the next person finds the code exhausting to maintain.

Cite keys: `quality:keep-it-simple`, `quality:subtract-first`, `quality:light-to-read`. Adapted in part from poteto's [pstack](https://github.com/backnotprop/pstack) (MIT).

## Rule

Get the most result from the least code and complexity (KISS, Keep It Stupid Simple). Build only for the product you have (YAGNI). A new concern gets its own folder ([`structure:folders`](code-structure.md#folders)). Name the concept instead of adding a `utils` or `helpers` dump.

**The test:** if a person would find this code exhausting to maintain, it is the wrong shape.

## Before you add

- **About to add anything:** look for a deletion first. On the path this change extends, remove the dead path, the redundant check, and the stub with no new content, then build (subtract first (Subtract before you add)). The removal lands before the addition: replace the old path instead of adding the new one beside it to clean up later. Unrelated debt stays a follow-up ([`structure:prior-mistakes`](code-structure.md#prior-mistakes)).
- **About to polish:** cut to the minimum the spec demands first.
- **About to handle an edge case:** design for observed usage. Add only the validators, parsers, guards, config, persistence, and retries the spec demands. Each speculative one drags more guards behind it.
- **About to add a layer, service, wrapper, class tree, shared API, queue, lock, or retry system:** name why a local version fails. If you cannot, skip it. A confirmed area of modularity is a named reason ([strong-foundation.md](strong-foundation.md)). If a client can bypass a disabled UI state, add the backend guard first ([`structure:authority`](code-structure.md#authority)).
- **About to extract:** extract only when the extraction owns its own behavior, removes real duplication, or enforces a locked rule. Keep an untidy `if`, and a guard used in one place, inline.
- **About to add state:** go from locals, to fields, to module state. Avoid new globals and any field every caller must remember. Derive a value instead of keeping a second copy in sync. A new layer or piece of state must remove at least as much load somewhere else.
- **About to thread a new signal through types, schemas, or pipelines:** stop and look for a direct path.
- **About to write small glue:** write one plain function or class instead of factories of factories, empty base classes, or one-line files.

## While you shape it

- **Decide once,** at the boundary. Make a choice or name an invariant in one place and pass the result, so layers and consumers need not repeat it.
- **Keep the call path flat** (light to read (Minimize reader load)). If "where does this value come from?" takes more than three hops, flatten. A deep entry that hides real work is welcome ([`structure:deep-public-surface`](code-structure.md#deep-public-surface)); a chain of pass-throughs is not. Inline a wrapper with one caller. Add an adapter only with a second implementation.
- **Take the smallest diff** that meets done when. Fewer lines beat elegant boilerplate.
- **Fix small leaks early.** Remove tiny pass-throughs, representation leaks, and duplicated choices before they spread. Small leaks become permanent coordination costs.
- **Reuse** an existing one-job helper instead of forking it ([`structure:primitives`](code-structure.md#primitives)). A small product change touches one place per concept.
- A seam (a named extension point where a new variant plugs in) on a confirmed area of modularity is foundation, not ceremony ([strong-foundation.md](strong-foundation.md)). The limits in this file apply to glue and to areas nobody confirmed.

## What simple is not

- Simple still means deep modules, one copy of each domain rule, and a real service for an independent domain.
- Fix a known-wrong shape instead of extending it. A behavior-preserving delete or move that removes a branch or layer happens when the goal or a named finding requires it; otherwise record a follow-up.
- Leave the design a little simpler, behind the same or a smaller surface, than you found it (leave it cleaner (Boy Scout Rule)).

## Check

- Could a simpler shape, including a deletion, still pass? Use it.
- Did the removal land before the addition?
- Can a new reader say where X comes from, and what can change X, without a tour?
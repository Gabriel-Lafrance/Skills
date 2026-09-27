# Keep it simple

**Open this when:** you are about to add a file, folder, layer, helper, wrapper, piece of state, validator, or abstraction, or you are refactoring, rewriting, or sizing a diff.
**Skip it and you will:** build for an imaginary product, and the next person finds the code exhausting to maintain.

Cite keys: `quality:keep-it-simple`, `quality:subtract-first`, `quality:light-to-read`. Adapted in part from poteto's [pstack](https://github.com/backnotprop/pstack) (MIT).

## Rule

Get the most result from the least code and complexity (KISS, Keep It Stupid Simple). Do not build for an imaginary product (YAGNI). A new concern gets its own folder ([`structure:folders`](code-structure.md#folders)). No `utils` or `helpers` dumps: name the concept.

**The test:** if a person would find this code exhausting to maintain, it is the wrong shape.

## Before you add

- **About to add anything:** look for a deletion first. On the path this change extends, remove the dead path, the redundant check, and the stub with no new content, then build (subtract first (Subtract before you add)). The removal lands before the addition; never add the new path beside the old one to clean up later. Unrelated debt stays a follow-up ([`structure:prior-mistakes`](code-structure.md#prior-mistakes)).
- **About to polish:** cut to the minimum the spec demands first.
- **About to handle an edge case:** design for observed usage. No speculative validators, parsers, guards, config, persistence, or retries the spec does not demand. Each one drags more guards behind it.
- **About to add a layer, service, wrapper, class tree, shared API, queue, lock, or retry system:** name why a local version fails. If you cannot, do not add it. A confirmed area of modularity is a named reason ([strong-foundation.md](strong-foundation.md)). If a client can bypass a disabled UI state, add the backend guard first ([`structure:authority`](code-structure.md#authority)).
- **About to extract:** only when the extraction owns its own behavior, removes real duplication, or enforces a locked rule. An untidy `if` is not a reason. A guard used in one place stays inline.
- **About to add state:** locals, then fields, then module state. No new global, and no field every caller must remember. Derive a value instead of keeping a second copy in sync. A new layer or piece of state must remove at least as much load somewhere else.
- **About to thread a new signal through types, schemas, or pipelines:** stop and look for a direct path.
- **About to write small glue:** one plain function or class. No factories of factories, empty base classes, or one-line files.

## While you shape it

- **Decide once.** Make a choice in one place and pass the result. Do not repeat it at each layer.
- **Keep the call path flat** (light to read (Minimize reader load)). If "where does this value come from?" takes more than three hops, flatten. A deep entry that hides real work is welcome ([`structure:deep-public-surface`](code-structure.md#deep-public-surface)); a chain of pass-throughs is not. Inline a wrapper with one caller. No adapter without a second implementation.
- **Name the invariant once,** at the boundary. Do not restate it in every consumer.
- **Take the smallest diff** that meets done when. Fewer lines beat elegant boilerplate.
- **Sweat the small leaks.** Remove tiny pass-throughs, representation leaks, and duplicated choices before they spread. Small leaks become permanent coordination costs.
- **Reuse** an existing one-job helper instead of forking it ([`structure:primitives`](code-structure.md#primitives)). A small product change touches one place per concept.
- A seam on a confirmed area of modularity is foundation, not ceremony ([strong-foundation.md](strong-foundation.md)). The bans in this file apply to glue and to areas nobody confirmed.

## What simple is not

- Simple never means shallow modules, duplicated domain logic, or skipping a real service for an independent domain.
- Never extend a known-wrong shape. A behavior-preserving delete or move that removes a branch or layer happens when the goal or a named finding requires it; otherwise record a follow-up.
- Leave the design a little simpler, behind the same or a smaller surface, than you found it (leave it cleaner (Boy Scout Rule)).

## Check

- Could a simpler shape, including a deletion, still pass? Use it.
- Did the removal land before the addition?
- Can a new reader say where X comes from, and what can change X, without a tour?
- Does every new file sit in a folder named for its concern?

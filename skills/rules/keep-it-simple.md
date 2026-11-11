# Keep it simple

Cite keys: `quality:keep-it-simple`, `quality:subtract-first`, `quality:light-to-read`. Adapted in part from poteto's [pstack](https://github.com/backnotprop/pstack) (MIT).

## Rule

Get the most result from the least code and complexity (KISS, Keep It Stupid Simple). Build only for the product you have (YAGNI). A new concern gets its own folder ([`structure:folders`](code-structure.md#folders)). Name the concept instead of adding a `utils` or `helpers` dump.

**The test:** if a person would find this code exhausting to maintain, it is the wrong shape.

## Before you add

- **About to add anything:** look for a deletion first. On the path this change extends, remove the dead path, the redundant check, and the empty stub, then build (subtract first (Subtract before you add)). Replace the old path instead of adding the new one beside it. Unrelated debt stays a follow-up ([`structure:prior-mistakes`](code-structure.md#prior-mistakes)).
- **About to polish:** cut to the minimum the spec demands first.
- **About to handle an edge case:** design for observed usage. Add only the validators, parsers, guards, config, persistence, and retries the spec demands.
- **About to add a layer, service, wrapper, class tree, shared API, queue, lock, or retry system:** name why a local version fails, or skip it. A confirmed area of modularity is a named reason ([strong-foundation.md](strong-foundation.md)).
- **About to extract:** follow [responsibility boundaries](code-structure.md#responsibility-boundaries). An untidy `if` alone is not a file boundary.
- **About to add state:** go from locals, to fields, to module state. Avoid new globals and any field every caller must remember. Derive a value instead of syncing a second copy. A new layer or piece of state must remove at least as much load elsewhere.
- **About to thread a new signal through types, schemas, or pipelines:** look for a direct path first.
- **About to write small glue:** one plain function or class, not factories of factories, empty base classes, or one-line files.

## While you shape it

- **Keep the call path flat** (light to read (Minimize reader load)). If "where does this value come from?" takes more than three hops, flatten. A deep entry that hides real work is welcome ([`structure:deep-public-surface`](code-structure.md#deep-public-surface)); a chain of pass-throughs is not, so inline a one-caller wrapper that only forwards or renames. An adapter must hide real dependency translation or implement a confirmed seam; an interchangeable adapter layer needs a real second implementation or a confirmed area of modularity ([strong-foundation.md](strong-foundation.md)).
- **Take the smallest coherent diff** that meets done when. Judge reader and change burden, not line or file count: a meaningful extraction can add a file and cut unrelated reading.

## What simple is not

- Simple still means deep modules, one copy of each domain rule, and a real service for an independent domain.
- Leave the design a little simpler, behind the same or a smaller surface (leave it cleaner (Boy Scout Rule)).

## Check

- Could a simpler shape, including a deletion, still pass? Use it.
- Did the removal land before the addition?

# Strong foundation

Cite key: `quality:strong-foundation`.

## Rule

Build the first iteration strong enough that the next change request adds a piece instead of rebuilding. For a Feature, that means a domain model, a service with a stable public API, and a **seam** (a named extension point where a new variant plugs in) on each **area of modularity**: a part of the feature that will vary or multiply (providers, channels, rules, roles, formats, tenants, states).

Keep it simple (KISS) governs the code inside each piece ([keep-it-simple.md](keep-it-simple.md)); this file governs the feature's shape.

**The test:** name the next likely change request. With this foundation, is it one new collaborator plus one registration, with no caller edited? If it is a rewrite, the foundation is missing a seam.

## Scale to the work

| Work | Foundation |
| --- | --- |
| Feature with its own domain concept or screen | Full foundation: domain model, service public API, a seam on each area of modularity, one real implementation behind each seam |
| Feature that fits an existing seam | Extend that seam: one new collaborator and its registration. Say which seam it extends |
| Feature that fits no seam where one should exist | Split: a Refactor that adds the seam first (behavior preserved), then the Feature on top, so no special case gets bolted onto the foundation |
| Refactor | May add a seam that a named later change needs |
| Tweak, Bug, Chore | Keep the existing shape. Add a seam only if the grill named an area of modularity |

## Find the areas of modularity

Stop at the first source that answers:

1. The ticket's `## Areas of modularity` or `## Foundation` section and its settled decisions.
2. The rest of the ticket, PR, or linked issue: named providers, "later we want", customer asks.
3. The request and the repo: an existing provider folder, a sibling service with a strategy, a second caller, an `if` or `switch` on a type or provider name, a TODO, a domain that usually multiplies (payments, notifications, auth providers, storage, exports, pricing rules).

Separate confirmed areas from candidates. Ask only when an unresolved area would materially change behavior, contracts, scope, or cost ([Asking the user](writing-style.md#asking-the-user)). Never ask a yes or no on every candidate or invent future variants. A Tweak, Bug, or Chore adds no foundation interview.

A seam goes only on an area someone named and the user did not reject.

## Build it

- **Seam first:** an interface, a strategy slot, an adapter, a registry, or a state machine goes in the first design for each confirmed area, before a second implementation exists.
- **One real implementation** ships behind each seam on day one.
- **Model the domain in a structure,** not in scattered conditionals: a state machine instead of synced booleans, a registry or discriminated union instead of an `if` chain that grows by one branch per variant.
- **Open to extension, closed to breaking edits:** new behavior lands in new collaborators; entry-point signatures stay stable.
- **Named patterns** (Strategy, Adapter, Facade, Observer, State) are welcome when they fit a confirmed area. SOLID is guidance for keeping the foundation extendable.
- **Skip interface theater** (abstractions with no behavior): factories of factories, empty base classes, one-line impl files, class trees deeper than two, or a seam on an area nobody confirmed.

Examples: [Foundation first](code-quality-examples.md#foundation-first-big-features), [Futureproof extension seam](code-quality-examples.md#futureproof-extension-seam), [SOLID theater vs foundation](code-quality-examples.md#solid-theater-vs-foundation), [Foundation seam](code-structure-examples.md#foundation-seam-big-service), [Foundation patterns](code-structure-examples.md#foundation-patterns-folder-trees). The whole path from ticket to follow-up: [journeys/new-feature.md](journeys/new-feature.md).

## Check

- Does every confirmed area of modularity have a seam with one real implementation?

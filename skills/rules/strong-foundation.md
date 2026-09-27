# Strong foundation

**Open this when:** you are about to grill, plan, or build a Feature, write a Research or Plan ticket, or review a Feature diff.
**Skip it and you will:** hardcode the first provider into every caller, and the second one becomes a rewrite instead of one new file.

Cite key: `quality:strong-foundation`.

## Rule

Code evolves and the first version is rarely final. Build the first iteration strong enough that the next change request adds a piece instead of rebuilding. For a Feature, that means a domain model, a service with a stable public API, and a **seam** on each **area of modularity**: a part of the feature that will vary or multiply (providers, channels, rules, roles, formats, tenants, states).

Structural decisions protect future options. The code inside each piece stays simple ([keep-it-simple.md](keep-it-simple.md)). The two do not conflict: keep it simple (KISS) governs how each piece is written, and this file governs the feature's shape.

**The test:** name the next likely change request. With this foundation, is it one new collaborator plus one registration, with no caller edited? If it is a rewrite, the foundation is missing a seam.

## Scale to the work

Pick the row from the work kind (Feature, Tweak, Bug, Refactor, Chore), whether it comes from a ticket or you infer it from the request.

| Work | Foundation |
| --- | --- |
| Feature with its own domain concept or screen | Full foundation: domain model, service public API, a seam on each area of modularity, one real implementation behind each seam |
| Feature that fits an existing seam | Extend that seam: one new collaborator and its registration. No new foundation. Say which seam it extends |
| Feature that fits no seam where one should exist | Split: a Refactor that adds the seam first (behavior preserved), then the Feature on top. Do not bolt a special case onto the foundation |
| Refactor | May add a seam that a named later change needs |
| Tweak, Bug, Chore | No new seam unless the grill named an area of modularity. Keep the existing shape |

## Find the areas of modularity

Use the best source you have, in this order. Stop at the first one that answers.

1. The ticket's `## Areas of modularity` (Research) or `## Foundation` (Plan) section.
2. The rest of the ticket, PR, or linked issue: named providers, "later we want", customer asks.
3. The request and the repo: an existing provider folder, a sibling service with a strategy, a second caller, an `if` or `switch` on a type or provider name, a TODO, a domain that usually multiplies (payments, notifications, auth providers, storage, exports, pricing rules).

Then confirm each candidate with the user in the grill: one yes or no question per area, with a recommended answer from the evidence. Example: "Will there be more than one payment provider? a) yes, Stripe now and more later recommended b) no, Stripe only." A well-written ticket that already settled it needs no question. A Tweak, Bug, or Chore skips the question. With no ticket and a one-line request, ask only about the one or two strongest candidates.

An area the user says no to gets no seam. An area nobody named gets no seam.

## Build it

- **Seam first:** an interface, a strategy slot, an adapter, a registry, or a state machine goes in the first design for each confirmed area. Do not wait for the second implementation.
- **One real implementation** ships behind each seam on day one. The seam is the foundation, not dead code.
- **Model the domain in a structure,** not in scattered conditionals: a state machine instead of synced booleans, a registry or discriminated union instead of an `if` chain that grows by one branch per variant.
- **Open to extension, closed to breaking edits:** new behavior lands in new collaborators; entry-point signatures stay stable.
- **Named patterns** (Strategy, Adapter, Facade, Observer, State) are welcome when they fit a confirmed area. SOLID is guidance for keeping the foundation extendable, not scripture.
- **No interface theater:** factories of factories, empty base classes, one-line impl files with no behavior, class trees deeper than two, or a seam on an area nobody confirmed.

Plans and Structure cards name each seam and the next change it makes small. Examples: [Foundation first](code-quality-examples.md#foundation-first-big-features), [Futureproof extension seam](code-quality-examples.md#futureproof-extension-seam), [SOLID theater vs foundation](code-quality-examples.md#solid-theater-vs-foundation), [Foundation seam](code-structure-examples.md#foundation-seam-big-service), [Foundation patterns](code-structure-examples.md#foundation-patterns-folder-trees). The whole path from ticket to follow-up: [journeys/new-feature.md](journeys/new-feature.md).

## Check

- Does every confirmed area of modularity have a seam with one real implementation?
- Is there a seam on an area nobody confirmed? Remove it.
- Name the next likely change request: is it one new file plus one registration?

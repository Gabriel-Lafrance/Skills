# Architecture

This skill is the structural gate: domain services with public APIs, deep
surfaces built from primitives inside those modules, simple entry points,
folder maps, write-path authority, behavior-preserving moves for prior
mistakes, and write-path scalability. Run it before `/goal` planning when
structure or data shape matters, or mid-implement when the diff is about to
sprawl.

**Read first:** [../pack-shared/standards.md](../pack-shared/standards.md) ·
[doctrine.md](doctrine.md) · [examples.md](examples.md) · **`/taste`**

Explore via Task subagents per [../pack-shared/subagents.md](../pack-shared/subagents.md): non-trivial sibling/service/folder research **must** use a Task; ≥2 independent lanes **must** run in parallel. You write the structure card from their reports. Skip Tasks only for greenfield-trivial structure with no repo to explore.

## Process

1. **Explore** using the checklist in [flow.md](flow.md#process)
2. **Draft** the doctrine **Structure** card (Output: always / if writes / if lists / if big feature)
3. **Implement against the card** (folders first, moves before new feature code, primitives inside deep modules, write-path aggregates and authority)
4. **Self-check** the doctrine Output keys before done

Open structure decisions → one `/grill-me` Questions batch (follow [../pack-shared/asking.md](../pack-shared/asking.md)).

## Hand-offs

- Structure card approved → `/goal`
- Scale or duplicated-service or missing write-path authority failures → acceptance evidence / `/code-review`

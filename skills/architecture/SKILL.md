---
name: architecture
description: >-
  Shape scalable code: domain services with public APIs, simple entry points,
  clear folders, and write-path data design (store aggregates on write — never
  recompute metrics on every render or read). Agents may auto-invoke. Use before
  or during planning/implementation when adding features, splitting logic,
  designing data/reads, or when about to dump files, duplicate domain logic, or
  scan-on-read. Public skill — users and agents may call this. Under /goal use
  /architecture-flow.
---

# Architecture

This skill is the structural gate: domain services with public APIs, simple entry points, folder maps, behavior-preserving moves for prior mistakes, and write-path scalability. Run it before `/goal` planning when structure or data shape matters, or mid-implement when the diff is about to sprawl.

**Read first:** [doctrine.md](doctrine.md) · [examples.md](examples.md) · **`/taste-flow`**

Inside a `/goal` workspace, use **`/architecture-flow`** instead of this skill.

**Explore via subagents** when useful: parallel `explore` Tasks for sibling features, existing services, and target folders; you write the structure card from their reports.

## Process

1. **Explore** — existing services, wrong shapes in the lane, entry patterns, write-vs-read siblings
2. **Draft structure card** — Services, Moves / corrections, Feature entry, Folder map, Scalability (see doctrine)
3. **Implement against the card** — folders first, moves before new feature code, write-path aggregates
4. **Self-check** — doctrine checklist before done

Open structure decisions → one `/grill-me` Questions batch (follow [../asking.md](../asking.md)).

## Hand-offs

- Structure card approved → `/goal`
- Under `/goal` → `/architecture-flow` → `/create-plan-flow`
- Scale or duplicated-service failures → `/validate-flow` / `/code-review-flow`

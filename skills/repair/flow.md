# Repair flow

Use for a repair inside an active parent wave. Read [doctrine.md](doctrine.md)
and the shared [execution context](../pack-shared/execution-context.md).

## Parent handoff

The parent provides the outcome, ticket if any, current lane, non-goals, Active
Rules, relevant acceptance, dependencies, and the exact slice to investigate.
The repair inherits those constraints and returns its evidence, decision, and
next step in chat. It does not resolve or create hidden filesystem state.

## Process

1. Re-state the parent lane and hunt pessimistically inside it.
2. Classify Local, Narrow, or Massive.
3. For Local/Narrow: grill → binary acceptance in the current context →
   smallest fix → `/validate` against both repair and parent criteria.
4. If validation fails, repair again; if scope becomes Massive, escalate to the
   parent for a new bounded goal or split. Do not sprawl.
5. On pass, return a compact completion handoff to the parent wave.

Workers receive the full bounded context and “smallest footprint only”; omit
their `model` unless the user requested one. Do not ask workers to reconstruct
intent from a path or hidden state.

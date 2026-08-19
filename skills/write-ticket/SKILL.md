---
name: write-ticket
description: >-
  Create or refine one Feature, Tweak, Bug, Refactor, Chore, or Hotfix ticket
  from a single prompt. Infers type and body, always runs full /analyze,
  and asks only a too-short grill or missing tracker metadata. Use for Linear
  or GitHub tickets, including “don’t forget this” captures; never inside /task.
disable-model-invocation: true
---

# Write Ticket

**Must read:** [../pack-shared/standards.md](../pack-shared/standards.md) — Read `/taste` and `/architecture` doctrines this turn before analyzing or drafting. Do not skip.

**Read:** [doctrine.md](doctrine.md) · [reference.md](reference.md) · **Ask style:** [../pack-shared/asking.md](../pack-shared/asking.md)

This skill is a user start. Do not nest it under `/task`. It writes a tracker ticket; `/trackers` reads.
Always run `/analyze` to full memo depth (this parent owns the next step). Do not run a type-specific
open grill. Do not invoke full `/grill-me`.

## Process

1. Load an existing ticket or seed from the prompt. Infer type, tracker, and
   body fields. Do not ask what research can answer.
2. If the idea is too short to analyze, send **one** asking-contract batch
   (include missing metadata in that same batch). Wait. Otherwise skip grill.
3. Run `/analyze` fully on the seed (Task workers, complete memo).
4. Fill the **same six sections** every type (Type, Diagram, Ask, Done when,
   Out of scope, Start here) using that type’s preset. Announce the draft.
   If metadata is still missing, one metadata batch — then write. If
   metadata was already known, write after the draft is visible. No
   “write this?” question. Status is Todo unless the prompt (or existing
   ticket) already names one.

Question templates, bodies, and tracker fields live in the reference and doctrine.

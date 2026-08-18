---
name: write-ticket
description: >-
  Create or refine one Feature, Tweak, Bug, Refactor, Chore, or Hotfix ticket
  from a single prompt. Infers type and body, always runs full flow /analyze,
  and asks only a too-short grill or missing tracker metadata. Use for Linear
  or GitHub tickets, including “don’t forget this” captures; never inside /goal.
disable-model-invocation: true
---

# Write Ticket

**Must read:** [../pack-shared/standards.md](../pack-shared/standards.md) — Read `/taste` and `/architecture` doctrines this turn before analyzing or drafting. Do not skip.

**Variants:** [../pack-shared/variants.md](../pack-shared/variants.md) — standalone-only. If flow is requested, use the no-flow message.

**Read:** [doctrine.md](doctrine.md) · [reference.md](reference.md) · **Ask style:** [../pack-shared/asking.md](../pack-shared/asking.md)

**Standalone only.** This skill writes a tracker ticket; `/trackers` reads.
Always run **flow** `/analyze` to full memo depth. Do not run a type-specific
open grill. Do not invoke full `/grill-me`.

## Process

1. Load an existing ticket or seed from the prompt. Infer type, tracker, and
   body fields. Do not ask what research can answer.
2. If the idea is too short to analyze, send **one** asking-contract batch
   (include missing metadata in that same batch). Wait. Otherwise skip grill.
3. Run **flow** `/analyze` fully on the seed (Task workers, complete memo).
4. Fill the type template from the memo, including the analysis Mermaid
   diagram after Type. Announce the draft. If metadata is still missing, one
   metadata batch — then write. If metadata was already known, write after
   the draft is visible. No “write this?” question. Status is Todo unless
   the prompt (or existing ticket) already names one.

Question templates, bodies, and tracker fields live in the reference and doctrine.

---
name: grill-me
description: >-
  Relentless interview to sharpen a plan or design until shared understanding.
  Asks all known questions in one numbered batch (reply like 1a, 2b, 3a); later
  findings may open a new batch. Agents may auto-invoke. Use when grilling or
  clarifying fuzzy intent outside /goal. Under /goal use /grill-me-flow.
---

# Grill Me

Interview until you and the user share understanding. **Standalone** — for goal workspaces use **`/grill-me-flow`**.

**Read:** [doctrine.md](doctrine.md) · **Ask style:** [../asking.md](../asking.md)

Follow doctrine Rules + Closing gates. Batch every known question in one message per asking.md. Do not write `plans/*` or implement until all closing gates pass.

## Hand-offs

- Structure needed → `/architecture`, then `/create-plan` or `/goal`
- Ready to build a loop → `/goal`
- Ready for one plan file → `/create-plan`

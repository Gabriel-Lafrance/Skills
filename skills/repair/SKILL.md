---
name: repair
description: >-
  Find bugs that are in the code (pessimistic) and fix with the smallest
  footprint. Another AI wrote this — there are bugs. Grill the user on what/how
  to fix, write acceptance criteria, fix, then /validate-flow. Agents may
  auto-invoke. Use when debugging, something is broken, or a Linear/GitHub issue
  is a defect. Under /goal use /repair-flow. Escalate massive bugs to /goal.
  State under .agents/temp/repairs/<repair-id>/.
---

# Repair

Pessimistic bug hunt + **smallest possible fix**. Read [doctrine.md](doctrine.md). Ask style: [../asking.md](../asking.md).

Under `/goal` / `/implement-flow`, use **`/repair-flow`** instead.

## Process

1. **Workspace** — `.agents/temp/repairs/<repair-id>/` + REGISTRY
2. **Hunt** — pessimistic; classify Local / Narrow / Massive
3. **Grill** — what/how via `/grill-me` + asking.md (blocking for Local/Narrow)
4. **Acceptance** — `ACCEPTANCE.md`
5. **Smallest fix** — grilled approach only
6. **Validate** — `/validate-flow` (required)

Massive → escalate to `/goal`. Do not patch-sprawl.

## Hand-offs

- Pass validate → stop (or `/code-review` if user wants)
- Inside goal → `/repair-flow`
- Massive → `/goal`

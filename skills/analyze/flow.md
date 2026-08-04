# Analyze (flow)

Parent-supplied analysis inside a long-running wave. Read [doctrine.md](doctrine.md).
Use the shared [execution context](../pack-shared/execution-context.md).

## Parent brief required

The parent must supply: ask or brief, outcome/Done when when known, lane,
ticket/PR, fixed point, Locked decisions, and which mode to run:

| Mode | When |
| --- | --- |
| Standard research | `/write-ticket` grilled brief, `/just-do-it` pre-build analyze |
| Review remediation | Named Fix-now rows from `/code-review` or `/just-do-it` |

## Process

1. Refresh the parent-supplied execution context; do not re-grill product intent.
2. Investigate only the surfaces needed for the brief via Task workers per
   [../pack-shared/subagents.md](../pack-shared/subagents.md) (parallel explore
   when lanes are independent).
3. Post the doctrine memo (standard or review-remediation template).
4. Return the memo to the parent. Do **not** invent standalone hand-off UX.

### Parent-owned hand-offs

- `/write-ticket`: return the memo; the parent drafts and writes the ticket.
- `/just-do-it` standard research: parent may instruct the `promote + start`
  hand-off under its autonomy policy after the memo is shown.
- Review remediation: parent shows the complete memo, then promotes under its
  rules (user explicit, or `/just-do-it` recommended Fix-now after the memo).

## Anti-patterns

- Loading standalone hand-off Questions when a parent owns the next step
- Broadening into product discovery during review remediation
- Creating tickets, implementing code, or writing tests

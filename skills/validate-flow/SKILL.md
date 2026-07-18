---
name: validate-flow
description: >-
  Internal gate-out: prove acceptance criteria with live evidence (any terminal,
  fast CLI) and an out-loud code-path walk for linking gaps. Criteria from goal
  workspaces, repair ACCEPTANCE.md, tickets, or pasted Done when. Pessimistic —
  do not assume it works. May call repair-flow / taste / architecture / design.
  Looked up by /goal, /repair, /repair-flow. Never for users or auto-invocation.
disable-model-invocation: true
---

# Validate Flow

**Gate out.** Read [doctrine.md](doctrine.md).

## Process

1. **Restate the bar** — criteria from goal / repair / ticket / paste; stop and ask if none
2. **Code-path walk** — out loud; missing link = fail
3. **Cross-plan seams** — required when goal INDEX has 2+ plans (doctrine §3)
4. **Evidence pass** — terminals first, fast CLI if needed
5. **Scalability / taste / design** — when relevant (doctrine)
6. **Report** — doctrine template
7. **Next step** — pass → `/code-review-flow` (goal wave); fail → `/repair-flow` or `/repair`

Under `/goal`, run after implement workers finish. Cross-plan seam ownership lives here — not a separate step in `/goal`.

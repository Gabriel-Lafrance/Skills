# Validate Flow

**Gate out.** Read [doctrine.md](doctrine.md) and use the shared
[execution context](../pack-shared/execution-context.md).

The parent invokes validation after integrating applicable implementation
slices. It supplies Done when, Active Rules, every current slice and its
acceptance criteria, plus relevant Ticket / PR and Git references in chat.
Stop and ask if that contract is incomplete.

## Process

1. **Restate the bar** — inline Done when, slice criteria, and `INV-*` rules.
2. **Walk code paths** — out loud; a missing link fails validation.
3. **Walk cross-slice seams** — required for two or more inline current
   slices; validation owns this check.
4. **Gather evidence** — terminals first, narrow CLI only for gaps; use
   [reference.md](reference.md) for browser-reachable UI when available.
5. **Check quality** — scalability, taste, services/primitives, and design
   when relevant.
6. **Report in chat** — use the doctrine template; do not create status,
   workspace, plan, or acceptance artifacts.
7. **Hand back to the parent** — pass may proceed to `/code-review`; fail
   becomes a bounded in-chat fix slice and is revalidated.

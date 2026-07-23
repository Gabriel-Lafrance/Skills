# Validate Flow

**Gate out.** Read [doctrine.md](doctrine.md).

For goal-scoped validation, resolve `goal_root` per [../workspace-roots.md](../workspace-roots.md) before reading acceptance artifacts.

## Process

1. **Restate the bar** — criteria from goal / repair / ticket / paste, including assigned `INV-*` Active Rules; stop and ask if none
2. **Code-path walk** — out loud; missing link = fail
3. **Cross-plan seams** — required when goal INDEX has 2+ plans (doctrine §3)
4. **Evidence pass** — terminals first, fast CLI if needed; UI or browser-reachable criteria use [reference.md](reference.md) when Browser capability is available
5. **Scalability / taste / design** — when relevant (doctrine)
6. **Report** — doctrine template
7. **Next step** — pass → `/code-review` (goal wave); fail → `/repair` or `/repair`

Under `/goal`, run after implement workers finish. Cross-plan seam ownership lives here — not a separate step in `/goal`.

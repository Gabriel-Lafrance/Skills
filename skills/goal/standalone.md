# Goal (standalone)

User-owned end-to-end build. Read [doctrine.md](doctrine.md) and
[reference.md](reference.md).

## Process

1. Establish in-chat execution context.
2. Run the doctrine lifecycle: grill → plan → implement → acceptance evidence →
   `/code-review` → Fix mode as needed.
3. Announce completion. After all gates pass, offer the `/publish` hand-off
   batch in [reference.md](reference.md). Do not commit, push, or open a PR
   from `/goal`.

This variant owns the build. Shipping decisions go through `/publish` after an
explicit hand-off. Do not invent a parent.

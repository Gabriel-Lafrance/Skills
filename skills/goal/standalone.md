# Goal (standalone)

User-owned end-to-end build. Read [../pack-shared/standards.md](../pack-shared/standards.md),
then [doctrine.md](doctrine.md) and [reference.md](reference.md).

## Process

1. Establish in-chat execution context.
2. Run the [lifecycle](reference.md#lifecycle): grill → plan → implement → acceptance evidence →
   `/code-review` → Fix mode as needed.
3. Announce completion. Offer ship Questions only after all gates pass (see
   reference). Do not commit or open a PR unless the user answers yes. If they
   ask to open a PR, follow [../pack-shared/pr-ship.md](../pack-shared/pr-ship.md)
   — not a private recipe, and not “only `/publish` does canvas and demo.”

This variant owns shipping decisions. Do not invent a parent.

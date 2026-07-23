---
name: analyze
description: >-
  Standalone task analysis: parallel Task explore crunch, always writes
  findings under a scoped analysis workspace, optional user-helped sharpening,
  optional promote to a /goal workspace. No ticket write by default. Use when
  analyzing a task or idea; /write-ticket calls this before drafting. Not for
  /goal. Unsure → /ask-gabriel.
disable-model-invocation: true
---

# Analyze

**Variants:** [../variants.md](../variants.md) — **standalone-only** (no `flow.md`). If flow is requested, use the **no flow** message.

**Standalone only.** Never call from `/goal`. Does **not** write Linear/GitHub — that is `/write-ticket`.

**Read:** [doctrine.md](doctrine.md) · [../workspace-roots.md](../workspace-roots.md) · **Ask style:** [../asking.md](../asking.md) · **Taste / structure:** `/taste`, `/architecture` when relevant.

**Subagent model:** omit Task `model`. Wait for Task results — never sleep/poll for subagents.

## Process (outline)

1. Resolve `analysis_root` / `analyses_container` (always write)
2. Parallel `explore` Tasks → synthesize
3. Write `ANALYSIS.md` (required)
4. Optional sharpen Questions batch
5. Hand-off batch (done / sharpen / promote / write-ticket / promote+goal)
6. Promote only on explicit yes — see doctrine

Unsure which skill next → `/ask-gabriel`.

---
name: rules
description: Never invoke directly. Holds the rule files AGENTS.md and skills link to; open one only when they name it.
category: Documents
disable-model-invocation: true
---

# Pack rules

Never recommend `/rules`.

## Read when

`AGENTS.md` says when to open each file it names. The rest:

- [convex.md](convex.md): in a repo with a `convex/` folder, for Convex naming, folders, queries, validators, and terminals
- [t3-code.md](t3-code.md): in T3 Code, before browser preview, delegation, or a PR watch
- [dev-server-logs.md](dev-server-logs.md): accessible service output, OS-aware log-only viewers, remote fallback, visibility evidence and lifecycle
- [pr-lifecycle.md](pr-lifecycle.md): parent-owned watching, latest-head readiness, cleanup and intent-aware takeover
- [journeys/](journeys/new-feature.md): one file per journey, listed in [`/ask-gabriel`](../ask-gabriel/SKILL.md#journeys), each following one piece of billing work through the skills and rules

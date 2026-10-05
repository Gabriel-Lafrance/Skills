# Keep judgment in the main context

**Open this when:** you are about to search a codebase, read a large file, dig through logs or long command output, or make many mechanical edits.
**Skip it and you will:** make worse decisions for the rest of the session.

## Rule

Keep decisions, talking with the user, and judging results in the main context. Hand mechanical or context-bloating work to a subagent:

- searching the codebase
- reading large files
- digging through noisy logs or long command output
- bulk mechanical edits

Ask the subagent for a short result (paths, snippets, a summary), not a dump. Check what it returns before you pass its conclusions on.

When the harness has no subagent, do the work with narrow reads (a search with a precise pattern, a line range) instead of whole files.

## Selective navigation

Start from the task's domain terms, known entry, ticket pointers, or changed
paths. Locate candidate files and symbols, then inspect the relevant public
signatures, responsibilities, and direct callers before loading implementations.
Read the owning implementation and relevant schemas, tests, or integrations to
verify behavior; a signature is a navigation clue, not proof. Follow additional
dependencies only when they can affect the decision or observable result.

For a broad or unfamiliar flow, carry a compact path / signature / responsibility
sketch in the existing chat handoff, Structure map, or optional Files / Start here
section. Include only the task's owners and meaningful dependency edges; verify
live pointers before editing. Reuse it while current instead of rediscovering
the same boundary. An obvious local edit needs only its entry pointer.

Do not load a whole-repository map by default, add a navigation tool dependency,
or create an index/document merely to perform a small task. Avoid duplicating
volatile implementation details in maps. A search or scout returns relevant
pointers and conclusions, not every match or unrelated source file. Widen the
search when the current pointers are incomplete or evidence contradicts them.

## Check

Is the main context holding decisions and short results, not raw search output or whole files?
Can the next reader locate the task's entry and behavior owner from the relevant
paths and signatures, then read only the implementations needed to verify them?

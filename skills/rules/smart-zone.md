# Stay in your smart zone

**Open this when:** you are about to search a codebase, read a large file, dig through logs or long command output, or make many mechanical edits.
**Skip it and you will:** fill your context with noise, and your decisions get worse for the rest of the session.

## Rule

Keep decisions, talking with the user, and judging results in the main context. Hand dumb or context-bloating work to a subagent:

- searching the codebase
- reading large files
- digging through noisy logs or long command output
- bulk mechanical edits

Ask the subagent for a short result (paths, snippets, a summary), not a dump. Judge what it returns yourself; do not forward its conclusions unchecked.

When the harness has no subagent, do the work with narrow reads (a search with a precise pattern, a line range) instead of whole files.

## Check

Is the main context holding decisions and short results, not raw search output or whole files?

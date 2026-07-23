# Repair

Pessimistic bug hunt + **smallest possible fix**. Read [doctrine.md](doctrine.md). Ask style: [../pack-shared/asking.md](../pack-shared/asking.md).


## Process

1. **Workspace** — `.agents/temp/repairs/<repair-id>/` + REGISTRY
2. **Hunt** — pessimistic; classify Local / Narrow / Massive
3. **Grill** — what/how via `/grill-me` + asking.md (blocking for Local/Narrow)
4. **Acceptance** — `ACCEPTANCE.md`
5. **Smallest fix** — grilled approach only
6. **Validate** — `/validate` (required)

Massive → escalate to `/goal`. Do not patch-sprawl.

## Hand-offs

- Pass validate → stop (or `/code-review` if user wants)
- Inside goal → `/repair`
- Massive → `/goal`

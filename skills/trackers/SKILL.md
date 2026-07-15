---
name: trackers
description: >-
  Fetch and update Linear and GitHub issues from ticket IDs or URLs. Agents may
  auto-invoke. Use when the user passes TEAM-123, IN-1234, #123, owner/repo#123,
  or a Linear/GitHub URL. Under /goal use /trackers-flow for ticket goals and
  close-out.
---

# Trackers (Linear + GitHub)

This pack expects **Linear** and **GitHub** as the issue surfaces. Cursor account linking (Cloud Agents) is separate — local skills talk to trackers via **MCP** and **`gh`**.

Inside an active `/goal` loop, use **`/trackers-flow`** for fetch + ACHIEVED close-out.

## Detect the tracker

| Input | Tracker |
| --- | --- |
| `IN-1234`, `ENG-99`, `TEAM-123` (letters-digits) | **Linear** |
| `linear.app/.../issue/...` URL | **Linear** |
| `#123`, `owner/repo#123`, `github.com/.../issues/123` | **GitHub** |
| Ambiguous number only | Ask once: Linear or GitHub? |

One ticket ID per goal unless the user explicitly names several related ones.

## Discover tools first

Before calling anything:

1. `GetMcpTools` with pattern `linear|github` (or inspect the Linear / GitHub server directly).
2. Read the live tool schema — names drift (`save_issue` vs `update_issue`). Prefer whatever the server lists **now**.
3. If a server is `needsAuth`, run its `mcp_auth` once, then rediscover tools.

## Fetch (required before planning)

### Linear

Prefer MCP tools matching: `get_issue`, `list_comments`, `list_issue_statuses` (exact names from discovery).

Pass the identifier as given (`IN-1234`). Pull:

- Title, description, status, priority, labels, assignee
- Acceptance criteria / checklist in the description
- Comments that add constraints (ignore pure chatter)
- Linked PRs / git branch if present

### GitHub

Prefer GitHub MCP if present; otherwise **`gh`**:

```bash
gh issue view <N> --json number,title,body,labels,assignees,state,url,comments
# or
gh issue view owner/repo#N --json number,title,body,labels,assignees,state,url,comments
```

If `gh` is missing or unauthenticated, say so and stop — do not invent the ticket body.

## Normalize into a ticket brief

```markdown
# Ticket
- **ID:** IN-1234
- **Tracker:** Linear | GitHub
- **URL:** …
- **Title:** …

# Ask
<what the ticket wants, user perspective>

# Acceptance (from ticket)
1. …
2. …

# Constraints
- …

# Out of scope
- … (explicit non-goals from ticket or comments)

# Raw
<link or path only — do not paste the full body into every later prompt>
```

Missing acceptance criteria → ask **one** question or derive binary Done when from the Ask (and show it for approval).

## While working

- Treat the ticket brief as the **spec source** for `/create-plan`, `/validate`, `/code-review`.
- Do **not** spam status comments on every checkpoint.
- Optional: set Linear/GitHub status to In Progress / started once implementation begins (only if a clear "started" state exists and the user did not forbid writes).

## Close-out (after ACHIEVED)

Only after `/validate` passes every Done when / acceptance row.

### Linear

1. Comment with a short resolution: what changed, how verified, PR/branch link if any.
2. Move status to **Done** / **Completed** (use `list_issue_statuses` / save-or-update issue tool from discovery — never guess state IDs).

### GitHub

```bash
gh issue comment <N> --body "$(cat <<'EOF'
## Resolved
<summary>

### Evidence
- <validate highlights>
- <PR or commit if any>
EOF
)"

gh issue close <N> --reason completed
```

If the workflow is "PR closes the issue", open/link the PR with `Fixes #N` and leave closing to merge — say that explicitly instead of double-closing.

## Failures

| Problem | Action |
| --- | --- |
| No Linear MCP | Tell the user to add Linear from Cursor MCP tools (`https://mcp.linear.app/mcp`), then retry. Do not fake the ticket. |
| No `gh` / not logged in | Ask them to install/auth `gh`, or paste the issue body once. |
| Ticket not found | Stop; confirm ID / team / repo. |
| Write tools missing | Still implement locally; report that close-out must be manual. |

## Anti-patterns

- Inventing title/AC from the ID alone
- Closing the ticket before validate evidence exists
- Dumping the full ticket body into every skill turn (keep the brief; link the raw)
- Using Cloud Agent Linear assignment as a substitute for fetch in this chat

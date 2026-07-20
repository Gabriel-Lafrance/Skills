# Trackers Flow — read only


This pack talks to trackers via **MCP** and **`gh`**. Cursor Cloud Agent linking is separate.

## Hard rule: read only

**Allowed:** get/list/view issue, PR, comments, statuses (for understanding), checklists in description, linked QA notes.

**Forbidden (never):**

- Status / state changes (“In Progress”, Done, close)
- Comments, replies, or resolution notes
- `save_issue` / `update_issue` / create / assign
- `gh issue comment`, `gh issue close`, `gh pr comment` (write), or any mutate API
- Closing or “close-out” after ACHIEVED

Ticket close is the **user’s** job (manual or PR merge). This skill only **reads**.

## Detect the tracker

| Input | Tracker |
| --- | --- |
| `IN-1234`, `ENG-99`, `TEAM-123` (letters-digits) | **Linear** |
| `linear.app/.../issue/...` URL | **Linear** |
| `#123`, `owner/repo#123`, `github.com/.../issues/123` | **GitHub** |
| `github.com/.../pull/N` or PR ref | **GitHub** (PR) |
| Ambiguous number only | Ask once: Linear or GitHub? |

One ticket ID per goal unless the caller explicitly names several related ones.

## Discover tools first

Before calling anything:

1. `GetMcpTools` with pattern `linear|github` (or inspect the Linear / GitHub server directly).
2. Read the live tool schema — prefer **read** tools (`get_issue`, `list_comments`, `get_pull_request`, …). Ignore write tools.
3. If a server is `needsAuth`, run its `mcp_auth` once, then rediscover tools.

## Fetch

### Linear

Prefer MCP read tools matching: `get_issue`, `list_comments`, `list_issue_statuses` (exact names from discovery — statuses are for labeling the brief, not for writing).

Pass the identifier as given (`IN-1234`). Pull:

- Title, description, status, priority, labels, assignee
- Acceptance criteria / QA checklists in the description
- Comments that add constraints (ignore pure chatter)
- Linked PRs / git branch if present — then fetch PR title/body/review comments when available (read only)

### GitHub

Prefer GitHub MCP read tools if present; otherwise **`gh`** view/list only:

```bash
gh issue view <N> --json number,title,body,labels,assignees,state,url,comments
# or
gh issue view owner/repo#N --json number,title,body,labels,assignees,state,url,comments

gh pr view <N> --json number,title,body,url,comments,reviews,commits
```

If `gh` is missing or unauthenticated, say so and stop — do not invent the ticket/PR body.

## Normalize into a ticket brief

```markdown
# Ticket
- **ID:** IN-1234
- **Tracker:** Linear | GitHub
- **URL:** …
- **Title:** …

# Ask
<what the ticket wants, user perspective>

# Acceptance / QA (from ticket)
1. …
2. …

# Constraints
- …

# Out of scope
- … (explicit non-goals from ticket or comments)

# Linked PR (if any)
- **URL:** …
- **Summary:** …
- **Review notes worth keeping:** …

# Raw
<link or path only — do not paste the full body into every later prompt>
```

Missing acceptance criteria → ask **one** question or derive binary Done when from the Ask (and show it for approval). Do not write that back to the tracker.

## How callers use the brief

- Spec source for `/create-plan`, `/validate`, `/code-review`
- Store a **link** in `GOAL.md` under `/goal` — not the full body in every prompt

## Failures

| Problem | Action |
| --- | --- |
| No Linear MCP | Tell the user to add Linear from Cursor MCP tools (`https://mcp.linear.app/mcp`), then retry. Do not fake the ticket. |
| No `gh` / not logged in | Ask them to install/auth `gh`, or paste the issue body once. |
| Ticket / PR not found | Stop; confirm ID / team / repo. |

## Anti-patterns

- Invoking this skill alone as “update my ticket”
- Inventing title/AC from the ID alone
- Any write/close/comment to Linear or GitHub
- Dumping the full ticket body into every skill turn (keep the brief; link the raw)
- Using Cloud Agent Linear assignment as a substitute for fetch in this chat

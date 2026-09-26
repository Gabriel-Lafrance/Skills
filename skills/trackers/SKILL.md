---
name: trackers
description: >-
  Read-only Linear/GitHub ticket and PR context for specifications and
  Done when. Used by parent orchestrators and never writes to trackers.
disable-model-invocation: true
---

# Trackers

Read a Linear or GitHub ticket or PR via **MCP** or **`gh`** and return a compact ticket brief in the parent's inline [execution context](../pack-shared/execution-context.md). An inner step for `/task`, not a typical user start. Do not persist the brief in agent-owned state. Cursor Cloud Agent linking is separate.

## Read when

- Every run, so the ticket's taste and architecture Done when checks are recognized: [code-quality.md](../rules/code-quality.md) and [code-structure.md](../rules/code-structure.md) ([standards.md](../pack-shared/standards.md)).
- Before asking the user anything: [asking.md](../pack-shared/asking.md).

Keep taste/architecture Done when checks and constraints from the ticket in
the brief. A Plan also keeps its rules, structure, files, snippets,
done-when, tests, and already-decided lines. Research keeps the need, the
problem, and what the grill settled.

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

One ticket ID per bounded execution context unless the caller explicitly names
several related ones.

## Discover tools first

Before calling anything:

1. List the harness's MCP tools for Linear and GitHub.
2. Read the live tool schema. Prefer **read** tools (`get_issue`, `list_comments`, `get_pull_request`, …). Ignore write tools.
3. If a server needs authentication, ask the user to authenticate it, then list the tools again.

## Fetch

### Linear

Prefer MCP read tools matching: `get_issue`, `list_comments`, `list_issue_statuses` (exact names from discovery; statuses are for labeling the brief, not for writing).

Pass the identifier as given (`IN-1234`). Pull:

- Title, description, status, priority, labels, assignee
- Done when checks (acceptance or QA checklists) in the description
- Comments that add constraints (ignore pure chatter)
- Linked PRs / git branch if present, then fetch PR title/body/review comments when available (read only)

### GitHub

Prefer GitHub MCP read tools if present; otherwise **`gh`** view/list only:

```bash
gh issue view <N> --json number,title,body,labels,assignees,state,url,comments
# or
gh issue view owner/repo#N --json number,title,body,labels,assignees,state,url,comments

gh pr view <N> --json number,title,body,url,comments,reviews,commits
```

If `gh` is missing or unauthenticated, say so and stop. Do not invent the ticket/PR body.

## Normalize into a ticket brief

```markdown
# Ticket
- **ID:** IN-1234
- **Tracker:** Linear | GitHub
- **URL:** …
- **Title:** …
- **Stage:** Memo | Research | Plan | unknown
- **Kind:** Feature | Tweak | Bug | Refactor | Chore | unset

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

# Source
<ticket or PR URL only; do not paste the full body into every later prompt>
```

Missing Done when → ask **one** question or derive binary Done when from the Ask (and show it for approval). Do not write that back to the tracker.

## How callers use the brief

- Spec source for the parent brief, acceptance evidence, and `/review`
- Keep the Ticket / PR reference and relevant Done when in chat; the
  parent combines them with Git and repository evidence
- Do not create a workspace, status, plan, register, or tracker update

## Failures

| Problem | Action |
| --- | --- |
| No Linear MCP | Tell the user to add the Linear MCP server (`https://mcp.linear.app/mcp`) in their harness, then retry. Do not fake the ticket. |
| No `gh` / not logged in | Ask them to install/auth `gh`, or paste the issue body once. |
| Ticket / PR not found | Stop; confirm ID / team / repo. |

## Anti-patterns

- Invoking this skill alone as “update my ticket”
- Inventing title/AC from the ID alone
- Any write/close/comment to Linear or GitHub
- Dumping the full ticket body into every skill turn (keep the brief; link the source)
- Using Cloud Agent Linear assignment as a substitute for fetch in this chat

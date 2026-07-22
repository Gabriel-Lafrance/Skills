---
name: publish
description: >-
  Standalone only — never used in /goal. Put work on a typed branch
  (feature|bug|refactor/<ticket>-<slug>), push, then ask whether to draft and
  publish a GitHub PR (What changed, How to QA, ticket link). Use when the user
  wants to ship a branch/PR after work is done. Unsure → /ask-gabriel.
disable-model-invocation: true
---

# Publish

**Variants:** [../variants.md](../variants.md) — this skill is **standalone-only** (no `flow.md`). If flow is requested, use the **no flow** missing-variant message.

**Standalone only.** Never call from `/goal`, never ship a `publish-flow`. Opens a **GitHub PR** via `gh` — Linear/GitHub issues are **linked**, not written (use `/write-ticket` to create tickets; `/trackers` is read-only).

**Ask style:** [../asking.md](../asking.md)

Ship local work: **lock type + ticket → branch → push → ask PR → draft → publish**.

## Change types

Every run locks **one** type (same trio as `/write-ticket`):

| Type | Branch prefix | Use when |
| --- | --- | --- |
| **Feature** | `feature/` | New capability, enhancement, intentional product change |
| **Bug** | `bug/` | Defect fix |
| **Refactor** | `refactor/` | Reshape / relocate / debt without intended product behavior change |

## Branch naming

```text
{type}/{ticket}-{slug}
```

| Part | Rule |
| --- | --- |
| `{type}` | `feature` · `bug` · `refactor` |
| `{ticket}` | Linear id (`IN-1234`) or GitHub issue (`42` / `owner-repo-42` when needed). If no ticket → ask once; do not invent |
| `{slug}` | lowercase kebab — short verb phrase of what the branch does |

**Examples:** `bug/IN-1234-fix-checkout-total` · `feature/ENG-99-add-invite-flow` · `refactor/42-extract-billing-service`

No spaces. No colons. Keep under ~60 chars when practical.

## Inputs

| Input | Mode |
| --- | --- |
| `IN-1234`, `ENG-99`, Linear URL | Ticket = that Linear id; fetch title via Linear MCP or `/trackers` when useful |
| `#42`, `owner/repo#42`, GitHub issue URL | Ticket = issue number; fetch via `gh` when useful |
| Type named (`bug`, `feature`, `refactor`) | Pre-lock that type; still confirm if ambiguous |
| Branch already correct | Reuse; do not recreate |
| “don’t push” / “local only” | Branch only — skip push + PR |
| Dirty tree / no commits ahead | Stop and ask — this skill does **not** invent commits |

## Process

### 1. Inspect git

In parallel:

- `git status` / `git branch --show-current`
- `git remote` + default base (`main`, else `master`)
- Commits ahead of base: `git log <base>..HEAD --oneline`
- Diff summary: `git diff <base>...HEAD --stat`

**Hard stops:**

| State | Action |
| --- | --- |
| No `gh` / not logged in | Say so; stop before PR (branch+push may still proceed if remotes work) |
| Dirty working tree (uncommitted) | Ask once: commit first (user must request commit) / stash / abort — do **not** auto-commit |
| Nothing to publish (no commits ahead of base, clean) | Stop; nothing to ship |
| Detached HEAD | Create a real branch before continuing |

### 2. Lock type + ticket

Lettered Questions (unless both already clear from context):

```markdown
## Questions
Reply like: 1a 2a

1. Change type?
   - a) Feature ← recommended when new/enhanced capability
   - b) Bug ← recommended when fixing broken/wrong behavior
   - c) Refactor ← recommended when move/cleanup/debt, no new product behavior
2. Ticket?
   - a) <detected IN-#### / #N> ← recommended when present
   - b) Other — paste Linear id, GitHub #, or URL
```

**Wait** if either is open. Ticket is **required when known or detectable**; if none exists, ask once whether to proceed with a descriptive slug-only branch (`{type}/no-ticket-{slug}`) or stop and run `/write-ticket` first — recommend `/write-ticket` when the work clearly belongs on a tracker.

### 3. Branch + push (default)

Unless the user already said **don’t push** / **local only**:

1. Build branch name `{type}/{ticket}-{slug}` (slug from commits / ticket title / user phrase).
2. **Announce** in Locked (asking.md):

```markdown
## Locked (correct if wrong)
**Type:** Bug
**Ticket:** IN-1234
**Branch:** `bug/IN-1234-fix-checkout-total`
**Base:** `main`
**Push:** yes
```

3. Create / switch:
   - On `main`/`master` (or wrong type/ticket branch) → `git checkout -b <branch>` (or rename with `git branch -m` when already on a disposable local branch with the right commits).
   - Already on the correct branch → keep it.
4. **Push** with upstream: `git push -u origin HEAD` (request network permissions as needed).
5. Skip push only when the user said so — still create/rename the branch locally.

Do **not** force-push. Do **not** push to `main`/`master`.

### 4. Ask: draft + publish PR?

After a successful push (or when already pushed):

```markdown
## Questions
Reply like: 1a

1. Draft a PR and publish it?
   - a) yes — show draft first, then publish ← recommended
   - b) no — stop after branch+push
   - c) draft only — show in chat, do not create
```

**Wait.** If `1b` → stop; return branch name + remote URL. If `1c` → draft in chat only. If `1a` → continue.

### 5. Draft PR body

Build from commits + diff + ticket. Show the **full** proposed title + body in chat. Match the locked type template below.

Then:

```markdown
## Questions
Reply like: 1a

1. Publish this PR as shown?
   - a) yes ← recommended
   - b) no — say what to edit
```

**Wait.** No silent `gh pr create`.

### 6. Publish PR

On yes only:

```bash
gh pr create --title "<title>" --base <base> --body "$(cat <<'EOF'
…approved body…
EOF
)"
```

Title shape: `[IN-1234] Short imperative summary` (or `[#42] …`). Include ticket id when present.

Confirm with the PR URL. Do **not** write Linear comments or change ticket status (user / merge process owns that). Optionally note in chat that they may link the PR on Linear.

## PR body templates

### Feature

```markdown
## Type
Feature

## Ticket
<Linear URL or `IN-1234` · GitHub `#N`>

## What changed
- …

## How to QA
1. …
2. …
- [ ] Expected: …

## Notes
- … (omit section if none)
```

### Bug

```markdown
## Type
Bug

## Ticket
<Linear URL or `IN-1234` · GitHub `#N`>

## What changed
- Fixed: …
- Root cause (if known): …

## How to QA
1. Repro steps that used to fail: …
2. Confirm expected behavior: …
- [ ] Bug no longer reproduces
- [ ] No obvious regression in adjacent flow

## Notes
- … (omit section if none)
```

### Refactor

```markdown
## Type
Refactor

## Ticket
<Linear URL or `IN-1234` · GitHub `#N`>

## What changed
- Moved / reshaped: …
- What must not change: …

## How to QA
1. …
2. …
- [ ] Behavior still holds (same user-visible outcomes)
- [ ] No new product behavior landed with this PR

## Notes
- … (omit section if none)
```

Keep How to QA concrete (paths, roles, clicks, commands). Prefer checkable lines. Link the tracker issue/URL in **Ticket** — required when a ticket was locked.

## Failures

| Problem | Action |
| --- | --- |
| Dirty tree | Ask commit/stash/abort — never auto-commit |
| No commits ahead | Stop |
| Push rejected | Show remote error; do not force-push |
| `gh` missing / unauth | Branch+push OK; stop before PR with install/auth help |
| PR already open for branch | Return existing URL; ask update body vs stop |
| User declines PR | Leave branch pushed; no PR |
| Unknown type | Lock via Questions before branching |

## Anti-patterns

- Invoking under `/goal` or inventing a flow twin
- Auto-committing uncommitted work
- Force-push or pushing to default branch
- Creating a PR before the draft+publish Questions
- Skipping type lock or ticket when detectable
- Colon in branch names (`bug/IN-1234:slug`) — use `{type}/{ticket}-{slug}`
- Writing Linear / closing tickets from this skill
- Empty How to QA (“test it works”)
- Turning a Refactor PR into a Feature dump or Bug report without the matching template
- Implementing new product work here — publish only

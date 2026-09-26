# Manual evals

These prompts check whether a real agent follows the pack. They are for pack authors. `/setup-toolkit` does not install this folder.

The main risk: the agent reads the short `AGENTS.md` index and never opens the rule files it points to. Each prompt below needs at least one rule file to pass.

## How to run

1. Make a scratch app repo. A tiny Next.js + Convex app with an `orders` table and a `SITE_URL` line in `.env.example` covers every prompt. Any JS/TS repo works for prompts 2, 3, and 4.
2. Install the pack in that repo the way a user would.
3. Open a fresh session for each prompt, in each harness you test (Cursor, Claude Code, Codex, and others).
4. Paste the prompt as written. Do not add hints.
5. Score each criterion pass or fail. A criterion passes only if the agent did it without being told.
6. Note which rule files the agent opened. Use the tool log, not the agent's claim.
7. Record the results in the PR description of the change you are testing. There is no results file.

## Prompts

### 1. Delete an order

Prompt: `Add a Convex mutation to delete an order.`

- [ ] Calls the repo's identity helper and fails when there is no user.
- [ ] Checks that the order belongs to that user before deleting.
- [ ] Does not accept `userId` from the client.
- [ ] Puts the new concern in its own folder (not a new sibling in `convex/` root when a second file appears).
- [ ] Adds no test.

Rules it needs: `rules/code-quality.md`, `rules/code-structure.md`, `rules/testing.md`.

### 2. Site URL env var

Prompt: `Add an env var for the public site URL.` (the repo already has `SITE_URL`)

- [ ] Finds and reuses `SITE_URL`.
- [ ] Adds no synonym such as `FRONTEND_URL` or `APP_URL`.

Rules it needs: `rules/code-quality.md` (Reuse env vars).

### 3. Plan team invites

Prompt: `Plan adding team invites.`

- [ ] Sends one batched Questions message with lettered options and a `recommended` pick, before any plan.
- [ ] Waits for the answer, then sends Locked in as a separate message.
- [ ] The plan has a Mermaid change diagram with both Before and After.

Rules it needs: `rules/planning.md`, `pack-shared/asking.md`, `grill-me/doctrine.md`.

### 4. Review the branch

Prompt: `Review my current branch.` (make a branch with a function over 5 paths and one unused export)

- [ ] Runs the Knip and complexity 5 check, or explains why it cannot.
- [ ] Labels each finding Fix now or Follow-up.
- [ ] Talks in plain words and cites principles as plain (Classic), for example keep jobs apart (SoC).

Rules it needs: `rules/tooling.md`, `rules/code-quality.md`, `rules/writing-style.md`.

### 5. Empty orders list

Prompt: `Make the empty orders list nicer.` Then, in the same session: `too many clicks`.

- [ ] Shows no caption like "No orders" when a create action can be the message.
- [ ] Updates `docs/design.md` in the same turn as the complaint (or creates it first if missing).
- [ ] UI copy has no em dash, en dash, or horizontal bar.

Rules it needs: `rules/user-experience.md`, `rules/writing-style.md`.

## When a prompt fails

1. Open the rule file that prompt needed and confirm the rule is there and clear.
2. Check the tool log. If the agent never opened that file, the index failed, not the rule.
3. Sharpen the "Read it when" wording for that row in `AGENTS.md` so the trigger matches the prompt a user types.
4. If sharper wording still fails across harnesses, promote the rule to a line in Hard rules.
5. Keep `AGENTS.md` under 8 KB. If a new hard rule pushes it over, shorten another line first.
6. Rerun the failed prompt in a fresh session in every harness before you merge.

# Verification reference

## Tools

After the harness's own tools ([harness first](../rules/tooling.md#harness-first-discovery)), use in this order:

1. The repo's own end-to-end harness (Playwright, Cypress, a PTY or expect script, a seed command).
2. A scratch Playwright script run with `npx` from the OS temp directory. Add no dependency to the app. Use the project's browser installation when available; if a required browser cannot be installed safely, report the check as inconclusive.

Convex apps: drive functions with `npx convex run` against the dev deployment and read `npx convex logs`. Convex MCP is allowed during a `/verification` run ([Verify terminals first](../rules/tooling.md#verify-terminals-first) lists this exception).

## Repository test suites

Select suites under [verification scope](../rules/execution.md#verification-scope). If a standard runner finds relevant tests but no script names them, use its documented command. Lint, type checks, and builds are not test suites unless they execute tests.

- Use supported package/path/project filters for bounded checks when dependency coverage remains adequate. Full verification uses every configured project/browser requested; a root aggregate may cover child suites. Check its coverage and run omitted required suites. Do not run the same suite twice because two scripts name it, or invent a filter that silently drops affected consumers.
- Reuse safe local services, create disposable test data when needed, and run suites that do not depend on a failed suite even if one exits nonzero.
- If no tests or test commands exist after the inventory, record `no test suites found`. Do not add test files, install new test tooling, or change runner configuration during verification.

## Ways to verify

Pick the moves that establish the bounded claim; unrelated layers stay unrun.

### You added or changed UI

- Start at the real entry point with representative company, selection, recommendation, or draft context. Walk the changed flow to its result and execute the next meaningful action; verify expected prefilled or carried data remains available and editable. Reload after a successful write and confirm the result stuck.
- Click each control you added or rewired. It should navigate, send a request, change the page, open a dialog, or move focus; one that does nothing is dead ([snippet](#dead-control-probe)).
- Watch the page settle from load through the first interaction when you touched layout, loading, images, or fonts. Measure layout shift and name the element that moved; above 0.1 is a problem ([snippet](#layout-shift-probe)).
- A new console error, unhandled rejection, or unintended 4xx or 5xx request is a finding.
- Force the states you touched: loading, empty, error, disabled, success. Compare them with `docs/design.md`.
- On a failed write, check that edits survive and retry works. Cancel or go back and verify the prior context and focus return. An opened dialog or editor with missing known inputs fails the interaction contract.
- When screenshot capture is available, inspect representative settled states at relevant viewports against the existing product: primary action prominence, component reuse, typography, spacing, density, and clipping. Report concrete discrepancies. A screenshot does not replace exercising behavior.
- Click the primary action twice fast when it writes: one row, one charge, one message.
- Resize to mobile (390 wide) and desktop (1440 wide) when you changed layout or styling: no horizontal scroll, clipped text, or overlap.
- Tab through the controls you added: reachable in order, focus visible, Enter and Space activate, Escape closes dialogs ([`ux:quality-floor`](../rules/user-experience.md#quality-floor)).
- Use back, forward, and a deep link when you changed routing or guards. Signed out, a protected route redirects.
- Changed visible text shows no raw keys or placeholders.

### You added or changed an endpoint, mutation, or action

- Call it with a real session and read the status, the body, and the stored row.
- Send bad input: it is rejected at the door with no side effect.
- Call it signed out, and as another user against someone else's resource: both are rejected on the server ([`structure:authority`](../rules/code-structure.md#authority)).
- Repeat the same request when it claims to be safe to retry: one effect.

### You added a migration, schema change, or backfill

- Seed local or disposable data in the old shape, run it, and compare schema, indexes, and row counts before and after.
- Run it again: a no-op or a safe failure.
- Run the down migration when the tool has one.
- Walk the flow that reads the changed data, over old and new rows.

### You added or changed a worker, queue consumer, cron, or scheduled job

- Trigger it now (CLI, admin trigger, `npx convex run`, one tick of the dev scheduler) instead of waiting for the schedule.
- Confirm the side effect (row, email in the catcher, file, sandbox call) and one run in the log.
- Feed it a failing input: it retries or dead-letters as designed, with no duplicate effect.
- Start two runs close together when overlap is possible: nothing is processed twice.
- Read the registered schedule string or config against the intent.

### You added or changed a webhook or integration

- Replay a sample payload through the provider's CLI or a saved fixture to the local endpoint.
- Send a bad signature: rejected.
- Deliver the same event twice: one effect.

### You changed a CLI or script

- Run the real command against a sample project. Read the exit code, the output, and the files written.
- Diff the output the change should not touch: byte-identical.

### You fixed a bug

- Show the [control](doctrine.md#proof-standards): the old failure, then the pass on the change.

## Drive snippets

Scratch scripts, run from the OS temp directory.

### Layout shift probe

```ts
await page.addInitScript(() => {
  (window as any).__shifts = [];
  new PerformanceObserver((list) => {
    for (const entry of list.getEntries() as any[]) {
      if (entry.hadRecentInput) continue;
      (window as any).__shifts.push({
        value: entry.value,
        nodes: entry.sources?.map((s: any) => s.node?.outerHTML?.slice(0, 120)),
      });
    }
  }).observe({ type: "layout-shift", buffered: true });
});
await page.goto(url);
await page.waitForLoadState("networkidle");
const shifts = await page.evaluate(() => (window as any).__shifts);
const score = shifts.reduce((sum: number, s: any) => sum + s.value, 0);
console.log({ score, shifts });
```

### Dead control probe

Scope `controls` to the elements you added or rewired, not the whole page.

```ts
const controls = page.locator('[data-testid="new-toolbar"] :is(button, a[href], [role="button"]):visible');
for (const control of await controls.all()) {
  const label = (await control.getAttribute("aria-label")) ?? (await control.innerText());
  if (/delete|remove|pay|charge|send/i.test(label)) continue;
  const before = { url: page.url(), dom: await page.content() };
  let requested = false;
  const onRequest = () => (requested = true);
  page.on("request", onRequest);
  await control.click();
  await page.waitForTimeout(800);
  page.off("request", onRequest);
  const changed = page.url() !== before.url || (await page.content()) !== before.dom;
  if (!requested && !changed) console.log("dead:", label);
  if (page.url() !== before.url) await page.goBack();
}
```

## Recipe template

Written or edited only after the user says yes. Every section comes from what a run actually did; no placeholders.

```markdown
# Verification

How an agent launches, drives, and checks this app.

## Launch
- Command, ports, env vars, seed data, sign-in for the test user
- Ready when: <log line, port answering, prompt>

## Doctor
- One read-only check: process up, right build, port is ours, sign-in works

## Tests
- Commands for every distinct repository suite, working directories, required local services, and safe test data

## Drive
- UI: <browser tool or harness, stable selectors (labels, test ids, routes)>
- Backend: <curl base URL and auth, CLI commands, job triggers>

## Evidence
- What to capture and where (outside the repo)

## Cleanup
- What to stop and reset. Evidence stays

## Features
- <Feature>: how to reach it (user point of view), how to drive it, what end state proves it works, gotchas
```

### Proposing recipe edits

List each edit as a bullet with the reason. The report's **Next** line offers them ("Reply `recipe` to save these edits"); nothing waits.

## Handoff

Use stable check IDs and acceptance mappings from [handoffs and evidence](../rules/execution.md#handoffs-and-evidence), including delegated runner results. Focused work can use a short scope, results, and gaps paragraph; use the tables for multiple checks or a full verification request.

```markdown
## Verification: <verified | failed | inconclusive>
| Live check | How it was verified | Outcome | Evidence |
| --- | --- | --- | --- |
| <Done when item, rule, or change> | <the move you picked> | verified \| failed \| inconclusive | <command and output, status, row count, log line, layout-shift score, artifact path> |

| Test suite | Working directory and command | Outcome | Evidence |
| --- | --- | --- | --- |
| <unit / integration / end-to-end / other, or no test suites found> | <path and exact selected command, or none> | verified \| failed \| inconclusive \| none | <exit code, passed / failed / skipped counts, failure excerpt or log path> |

- **Scope and reason:** <affected behavior/dependencies/risk; focused or full request>
- **Target:** <pinned revision and diff identity; check IDs and acceptance mapping>
- **Reused evidence:** <check, relevant unchanged code/context and source, or none>
- **Not run:** <unselected scope and why; never described as passing>
- **Environment:** <local or preview URL, build identity>
- **Resources and cleanup:** <owned processes/data, cleanup completed or remaining>
- **Live layers not exercised:** <layers the change did not touch, in one line>
- **Failed:** <each with the smallest repro, or none>
- **Tests worth keeping:** <the [proposal](../rules/testing.md#proposal), tests written with file and command, or none>
- **Inconclusive:** <each with the missing prerequisite, or none>
- **Recipe edits proposed:** <list, or none>
```

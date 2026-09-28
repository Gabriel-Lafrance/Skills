# Verification reference

## Tools

Use what the harness and repo already have, in this order:

1. The harness browser tool (for example Cursor's browser or a Chrome integration) for interactive UI checks.
2. The repo's own end-to-end harness (Playwright, Cypress, a PTY or expect script, a seed command).
3. A scratch Playwright script run with `npx` from the OS temp directory. Do not add a dependency to the app. If a browser download is needed, say so and ask once.
4. `curl` or the framework CLI for endpoints, the database client for rows, the queue or scheduler CLI for jobs, and the process logs.

Convex apps: drive functions with `npx convex run` against the dev deployment and read `npx convex logs`. Convex MCP is allowed during a `/verification` run ([Verify terminals first](../rules/tooling.md#verify-terminals-first) lists this exception).

## Ways to verify

This is a menu, not a checklist. Start from what the work actually did (the diff, the slices, the Done when items). For each thing you changed, pick the few moves below that would show it works, and skip the rest. Two added buttons get a UI pass on that view, not a migration or endpoint pass. Go one layer wider only where the change crosses a boundary: a new button that calls a new endpoint gets the click, the request, and the stored row.

### You added or changed UI

- Open the changed view and walk the flow from its entry route to the result. Reload and confirm the result stuck.
- Click each control you added or rewired. It should navigate, send a request, change the page, open a dialog, or move focus; one that does nothing is dead ([snippet](#dead-control-probe)).
- Watch the page settle from load through the first interaction when you touched layout, loading, images, or fonts. Measure layout shift and name the element that moved; above 0.1 is a problem ([snippet](#layout-shift-probe)).
- Keep the console and network panel open. A new error, unhandled rejection, or failed request (4xx or 5xx) the flow did not intend is a finding.
- Force the states you touched: loading, empty, error, disabled, success. Compare them with `docs/design.md`.
- Click the primary action twice fast when it writes: one row, one charge, one message.
- Resize to mobile (390 wide) and desktop (1440 wide) when you changed layout or styling: no horizontal scroll, clipped text, or overlap.
- Tab through the controls you added: reachable in order, focus visible, Enter and Space activate, Escape closes dialogs ([`ux:quality-floor`](../rules/user-experience.md#quality-floor)).
- Use back, forward, and a deep link when you changed routing or guards. Signed out, a protected route redirects.
- Read the visible text you changed against `docs/design.md` and the locale files: no raw keys or placeholders.

### You added or changed an endpoint, mutation, or action

- Call it with a real session and read the status, the body, and the stored row.
- Send bad input: it is rejected at the door with no side effect.
- Call it signed out, and as another user against someone else's resource: both are rejected on the server (hard rule 4 in `AGENTS.md`).
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

- Reproduce the old failure on the base commit, or with the fix reverted when that is cheap. Then show the same steps pass on the change.

## Drive snippets

Scratch scripts only. Run them from the OS temp directory; never commit them.

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

`docs/verification.md` in the app. Written or edited only after the user says yes. Every section comes from what a run actually did; no placeholders.

```markdown
# Verification

How an agent launches, drives, and checks this app.

## Launch
- Command, ports, env vars, seed data, sign-in for the test user
- Ready when: <log line, port answering, prompt>

## Doctor
- One read-only check: process up, right build, port is ours, sign-in works

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

At the end of a run, list each edit as a bullet with the reason, then ask:

```markdown
## Questions
Reply like: 1a

1. Save these edits to `docs/verification.md`?
   - a) yes, all ← recommended
   - b) some: say which
   - c) no
```

## Handoff

```markdown
## Verification: <verified | failed | inconclusive>
| What changed | How it was verified | Outcome | Evidence |
| --- | --- | --- | --- |
| <Done when item, rule, or change> | <the move you picked> | verified \| failed \| inconclusive | <command and output, status, row count, log line, layout-shift score, artifact path> |

- **Environment:** <local or preview URL, build or commit>
- **Not exercised:** <layers the change did not touch, in one line>
- **Failed:** <each with the smallest repro, or none>
- **Inconclusive:** <each with the missing prerequisite, or none>
- **Recipe edits proposed:** <list, or none>
```

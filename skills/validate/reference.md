# Browser Validation Reference

Load this only when a user-visible or browser-reachable acceptance criterion needs runtime proof. Terminal and code-path evidence remain the first choice for non-visual criteria.

## Capability and preconditions

- Cursor's native Browser must be available in the current Agent session. A skill cannot enable it, bypass approval, or override Browser Protection, policy, or origin allowlists.
- Read the relevant terminal first. Reuse an already-running development server; do not start a duplicate server just to inspect a page.
- Use a reachable local URL or approved preview, safe non-destructive test data, and only the credentials already available to the session.
- Browser state can persist for the workspace. Reset the test state when safe, or record the starting state in the report.
- If Browser access, the app, credentials, or required test data are unavailable, mark the criterion `blocked`. Do not call visual validation a pass.

## Workflow

1. Inspect the existing browser tab when one is available; otherwise open the target route.
2. Capture the baseline for each required viewport or state.
3. Exercise the acceptance criterion without creating destructive or irreversible data.
4. Check the visible result and, when the Browser exposes them, console errors and failed network requests.
5. Capture the final state with a snapshot or screenshot.
6. Follow the Browser tool's lock lifecycle for longer interactions. Do not retry a failed interaction without new evidence.

Exercise only states that are relevant to the criterion: responsive layout, empty, loading, error, success, and primary interactions.

## Evidence

Record browser evidence in the validation report:

```markdown
| Source | What it showed |
| --- | --- |
| Browser: `<URL>` · `<viewport>` | `<flow/state>` → `<observed result>` · `<snapshot or screenshot>` |
```

## Results

- **Pass:** Every required visible outcome was observed and the browser did not expose a relevant error.
- **Fail:** The observed UI, interaction, console, or network result contradicts the criterion.
- **Blocked:** Browser tools, policy approval, app reachability, credentials, captcha, or safe test data prevents verification. State exactly what is needed.
- **N/A:** The criterion has no browser-reachable behavior.

## Anti-patterns

- Hard-coding Cursor Browser tool names or assuming they are always present.
- Treating terminal output as proof of a visual result.
- Calling an unperformed browser check a pass.
- Brute-forcing login, captcha, approval, or repeated failed interactions.
- Using browser actions that mutate shared or production-like data without explicit authorization.

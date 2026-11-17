# Accessible development-server logs

Use the repo's supported dev orchestration and
[harness-first discovery](tooling.md#harness-first-discovery). Add no logging
framework, dependency, or public log endpoint. This grants no permission to
start services, change sensitive logging, or bypass harness restrictions.

## Startup and capture

Reuse running services, terminals, and log streams. Opening logs never
restarts or duplicates a server; missing past output from a running process is
a gap, not a reason to restart it without authority. Start only the services
this project needs; do not assume web, API and Convex.

For an authorized startup, capture stdout **and** stderr for each service
from the start, through the orchestrator's persistent terminal or log options,
else minimal tee or redirection. Label lines such as `[web]` or `[api]`, with
timestamps where practical; use separate files rather than new aggregation
machinery.

Put logs in a user-local temp directory outside Git and public/static
directories. Never dump the full environment or seed credentials into logs;
redact secrets before displaying or sharing output. Record which process
owns each stream and whether it survives harness closure.

## Viewer choice

Prefer native harness terminal/log tools first, including opening existing
service output. If native output is unavailable or hidden and a visible viewer
is requested or needed within scope, discover an installed local terminal. The
viewer only follows existing logs; service orchestration stays separate.

| Actual environment | Supported route to discover |
| --- | --- |
| Windows | Detect PowerShell and an available terminal. Use Windows Terminal only if present; otherwise a supported PowerShell console. Give the tab/window a descriptive title. |
| macOS | Detect an available terminal app and permitted launch interface. Use its supported command/file handoff; do not assume `osascript` or a particular app is installed/allowed. |
| Linux desktop | Detect the installed terminal emulator and its argument contract. Do not assume a terminal name, `tmux`, or desktop session. |
| Remote/container/headless host | Use accessible harness output, or give the log path and exact follow command for the connected host/session. A window spawned on a cloud host is not visible on the user's desktop. Explain the access route; report a gap if none exists. |

Pass paths and arguments through supported structured interfaces when possible.
Quote for the **actual** shell and each launch boundary, including spaces,
apostrophes and metacharacters; never interpolate unchecked shell text. Prefer one shell over nested
command strings. Do not install a terminal or weaken access controls.

Return an exact copyable fallback with the real quoted absolute log path and
execution host, not a variable or placeholder. Command shapes:

- PowerShell: `Get-Content -LiteralPath $taskLogPath -Tail 200 -Wait`
- POSIX shell with a supported `tail`: `tail -n 200 -f "$task_log_path"`

For multiple services give separate commands or use the existing labelled
aggregate stream. Do not promise following across rotation, truncation, or
file replacement without verifying the follower supports it.

## Evidence and lifecycle

Read a recent log sample through the actual path and confirm service identity,
freshness, stderr capture and any claimed labels. Check viewer errors. A
running terminal process proves only launch, not that the user sees the window
or that new output arrives. Report what was observed, and state visibility or
live-follow uncertainty when it cannot be checked.

Closing the **log-only** viewer leaves services running. Stopping services
follows the owning orchestrator's cleanup policy; do not leave a new server
running because the viewer is separate. Do not promise lifetime beyond the
actual process/session manager. Keep log retention bounded, and save needed evidence
before deleting logs. Leave log paths and access commands in the
chat handoff, with process ownership and cleanup responsibility. Preserve existing E2E suites and browser
permissions: readable logs are debugging evidence, not verification.

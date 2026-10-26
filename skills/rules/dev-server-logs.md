# Accessible development-server logs

Apply when starting or debugging a web project, including a browser preview.
Use the repo's supported dev orchestration and
[harness-first discovery](tooling.md#harness-first-discovery). This adds no
logging framework, dependency, public log endpoint, or permission to start
services, change sensitive logging, or bypass harness restrictions.

## Startup and capture

Inspect the actual execution host, OS, shell, GUI availability, repo launch
scripts and existing processes/ports/terminals before choosing commands. Reuse
running services and supported log streams. Identify only the services this
project needs; do not assume web, API and Convex are always present. Opening
logs must never restart or duplicate a server. Missing historical output from
an already-running process is a gap, not a reason to restart it without authority.

For an authorized startup, arrange accessible stdout **and** stderr for each
actual service from the start. Prefer the orchestrator's existing persistent
terminal/output or log options; otherwise use minimal supported capture/tee or
redirection, accounting for buffering, process ownership and exit status. Keep
service labels such as `[web]` or `[api]`, with timestamps where practical.
Separate files are fine when aggregation would require new machinery.

Use a safe user-local runtime/temp log directory on the execution host, outside
Git and public/static directories, with access limited appropriately. Choose
paths from the actual project/run, not a copied ticket or another session.
Never dump the full environment or seed credentials into logs. Avoid capturing
secrets unnecessarily; redact sensitive output before displaying or sharing it.
Record which process owns each stream and whether it survives harness closure.

## Viewer choice

Prefer usable native harness terminal/log tools first, including opening the
existing service output when supported. Do not assume every harness hides logs.
If native output is unavailable/hidden and a visible viewer is requested or
needed within scope, discover a suitable installed local terminal. The viewer
only follows existing logs; service orchestration remains separate.

| Actual environment | Supported route to discover |
| --- | --- |
| Windows | Detect PowerShell and an available terminal. Use Windows Terminal only if present; otherwise a supported PowerShell console. A descriptive tab/window title helps locate the viewer. |
| macOS | Detect an available terminal app and permitted launch interface. Use its supported command/file handoff; do not assume `osascript` or a particular app is installed/allowed. |
| Linux desktop | Detect the actual installed terminal emulator and its argument contract. Do not assume a terminal name, `tmux`, or desktop session. |
| Remote/container/headless host | Use accessible harness output, or provide the log path and exact follow command for the appropriate connected host/session. A window spawned on a cloud host is not visible evidence on the user's desktop. Explain the access route; report a gap if none is available. |

Pass paths/arguments through supported structured interfaces when possible.
Quote for the **actual** shell and each launch boundary, including spaces,
apostrophes and metacharacters; never interpolate unchecked shell text. In
PowerShell single-quoted literals, double embedded apostrophes. In POSIX sh
single-quoted literals, represent an embedded apostrophe by closing the quote,
adding a quoted apostrophe, then reopening it. Prefer one shell over nested
command strings. Do not install a terminal or weaken access controls.

Return an exact copyable fallback with the real quoted absolute log path and
execution host, not an unresolved variable or placeholder. Command shapes:

- PowerShell: `Get-Content -LiteralPath $taskLogPath -Tail 200 -Wait`
- POSIX shell with a supported `tail`: `tail -n 200 -f "$task_log_path"`

Here the variables stand for already-resolved paths; substitute safe literal
paths in the user's command. For multiple services give separate commands or
use the existing labelled aggregate stream. Check the follower's behavior for
rotation/truncation if relevant; don't promise reliable following after file
replacement without verifying that tool's support.

## Evidence and lifecycle

Read a recent log sample through the actual path and confirm service identity,
freshness, stderr capture and any claimed labels. Check viewer errors. A
spawned/running terminal process proves only launch, not that the user can see
the window or that new output is arriving. Report what was observed, and state
visibility or live-follow uncertainty explicitly when it cannot be checked.

Closing the **log-only** viewer must leave services running. Conversely, stopping
services follows the owning orchestrator's cleanup policy; do not leave a new
server running merely because the viewer is separate. Do not promise lifetime
beyond the actual process/session manager. Leave log paths and access commands
in the existing chat handoff, with process ownership and cleanup responsibility.
Use a bounded retention/cleanup policy suitable for the session; avoid unbounded
disk growth and retain needed evidence before removing logs. Preserve existing
E2E suites and browser permissions: readable logs are debugging evidence, not
a replacement for verification.

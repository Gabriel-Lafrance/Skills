# Security Policy

## Supported versions

This repository publishes Cursor agent skills as Markdown. Only the latest
`main` branch is supported.

| Branch | Supported |
| --- | --- |
| `main` | Yes |
| Other branches / tags | No |

## Reporting a vulnerability

**Do not** open a public GitHub issue for security-sensitive reports.

Prefer GitHub’s private reporting (when enabled on this repo):

1. Open https://github.com/Gabriel-Lafrance/Skills/security/advisories/new
2. Describe the issue, impact, and steps to reproduce
3. Include skill paths or install steps if relevant

If private advisories are unavailable, contact the maintainer on GitHub:
[@Gabriel-Lafrance](https://github.com/Gabriel-Lafrance) — use a private
channel and do not paste exploit details in public issues or PRs.

## What to expect

- Acknowledgement when the report is received (usually within a few days)
- A brief assessment of impact and whether a fix or docs change is needed
- Credit in the advisory or release notes if you want it (say so in the report)

## Scope notes

This pack is documentation and agent instructions, not a hosted service. Still
report anything that could cause unsafe agent behavior when users install the
skills (for example: prompts that encourage leaking secrets, destructive git
defaults, or undisclosed exfiltration).

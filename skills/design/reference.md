# Design reference

Load with [SKILL.md](SKILL.md) for the file shape, route crawl, login pause, and merge rules. Bars stay in [doctrine.md](doctrine.md).

## Heading skeleton

Write `docs/design.md` with these H2s. Add H3+ whenever a thing needs a name of its own. Do not add Summary.

```markdown
# Design

Living source of truth for this app's UX and UI. No summary. No size cap.
Add a heading when something new needs its own place.

## Visual language

Color, type, space, motion, density, iconography, and what the product
refuses (for example a banned pairing).

## Components

Reusable UI pieces and how each one behaves, including hover, disabled,
loading, empty, and error when those states exist.

## Patterns / behavior

Cross-screen interaction rules. Prefer fewer clicks and keystrokes when
the next input is obvious. Write the why next to the rule.

## Screens / flows

One subsection per route or job. What the user is here to finish, the
happy path, and the other states (empty, loading, error, success,
no-permission).

## Preferences

Stated likes, dislikes, and exceptions, including why they save work.
```

If a fact does not fit, create a heading that describes it. Do not invent a sixth required H2 unless the product truly has a distinct kind (for example marketing vs in-app). Prefer nesting under an existing H2.

## Route crawl

Discover routes from the repo, then visit each:

| Stack signal | Where to look |
| --- | --- |
| Next.js App Router | `app/**/page.tsx`, `page.jsx`, `page.mdx` |
| Next.js Pages Router | `pages/**/*.tsx` excluding `_app` / `_document` / api |
| React Router | `<Route path=…>` / `createBrowserRouter` objects |
| Expo / RN Router | `app/**` routes excluding `_layout` only files |
| Other | The repo's existing router table; do not guess a framework |

Visit **every** discovered route after login. Record URL, what the screen is for, primary action, states you can reach without destructive data, and repeating components. Skip auth-callback or logout URLs that would drop the session; note them as skipped.

Work in a Task so the main chat can stay on login and integration ([subagents.md](../pack-shared/subagents.md)).

## Login pause

Workers do not chat with the user. The parent:

1. Opens or reuses the Browser on the local app.
2. Asks the user to log in there.
3. Waits until the user says they are in.
4. Then dispatches the crawl Task.

Do not brute-force login, paste secrets, or retry captcha. If login never happens, write the code-derived file and mark visual capture blocked ([browser-evidence.md](../pack-shared/browser-evidence.md)).

## Merge into an existing file

When updating `docs/design.md`:

1. Read the whole file. That text is the rule, including user edits.
2. Add new screens and components under the heading that names them.
3. Patch a bullet only when this turn observed a replacement, or the user stated a new preference.
4. Do not restore text the user removed.
5. Do not collapse long sections into a digest.
6. Keep `docs/design.md` as the only path.

## User-facing vs `/implement`

Dispatch `/design` when the slice outcome is a screen, component, visible copy, or client interaction. Dispatch `/implement` when the slice is schema, services, APIs, or other non-UI work. Split mixed work into two slices when the lanes do not overlap. If one slice must touch both, `/design` owns it and still follows `/architecture` for the non-UI files in the allowlist.

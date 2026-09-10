# Design reference

Load with [SKILL.md](SKILL.md) for the file shape, route inventory, and merge rules. Bars stay in [doctrine.md](doctrine.md).

## Heading skeleton

Write `docs/design.md` with these H2s. Add H3+ whenever a thing needs a name of its own. Do not add Summary.

```markdown
# Design

Living source of truth for this app's UX and UI. No summary. No size cap.
Add a heading when something new needs its own place.

## Visual language

Identity for this product. Record what you observed or what the user stated:
color roles with hex when visible, type (display / body / utility), space and
density, motion, iconography, and what the product refuses (including AI-default
looks this app is not). Do not invent a look here.

## Components

Reusable UI pieces and how each one behaves, including hover, disabled,
loading, empty, and error when those states exist.

## Patterns / behavior

Cross-screen interaction rules. Write the why next to the rule. Pack
experience bars live in the skill, not as a sixth required heading here.
If this product must add friction (money slower, extra delete confirm),
put that under **Preferences**.

## Screens / flows

One subsection per route or job. What the user is here to finish, the
happy path, and the other states (empty, loading, error, success,
no-permission).

## Preferences

Stated likes, dislikes, and exceptions, including why they save work.
```

If a fact does not fit, create a heading that describes it. Do not invent a sixth required H2 unless the product truly has a distinct kind (for example marketing vs in-app). Prefer nesting under an existing H2.

## Route inventory

Discover routes from the repo, then inventory each from code:

| Stack signal | Where to look |
| --- | --- |
| Next.js App Router | `app/**/page.tsx`, `page.jsx`, `page.mdx` |
| Next.js Pages Router | `pages/**/*.tsx` excluding `_app` / `_document` / api |
| React Router | `<Route path=…>` / `createBrowserRouter` objects |
| Expo / RN Router | `app/**` routes excluding `_layout` only files |
| Other | The repo's existing router table; do not guess a framework |

Inventory **every** discovered route from code. Record URL, what the screen is for, primary action, states declared in code, and repeating components. Capture Visual language from tokens, theme, and CSS (color roles + hex, type, density, motion, refuses). Note routes whose behavior only shows at runtime as gaps; do not invent them.

Work in a Task ([subagents.md](../pack-shared/subagents.md)).

## Merge into an existing file

When updating `docs/design.md`:

1. Read the whole file. That text is the rule, including user edits.
2. Add new screens and components under the heading that names them.
3. Patch a bullet only when this turn observed a replacement, the user stated a new preference, or the user wants to change how the design is done.
4. Do not restore text the user removed.
5. Do not collapse long sections into a digest.
6. Keep `docs/design.md` as the only path.

## User-facing vs `/implement`

Dispatch `/design` when the slice outcome is a screen, component, visible copy, or client interaction. Dispatch `/implement` when the slice is schema, services, APIs, or other non-UI work. Split mixed work into two slices when the lanes do not overlap. If one slice must touch both, `/design` owns it and still follows `/architecture` for the non-UI files in the allowlist.

## Identity

Resolve in this order. Stop at the first source that actually specifies look and feel:

1. `docs/design.md` Visual language
2. Existing tokens / theme / CSS variables in the repo
3. What the user stated this turn

If none of those exist, the parent asks. A worker returns `blocked` and names this gap. Do not pick a palette "to get started."

## Professional craft

Do the design work in thinking, then ship once. The user should not need a second "make it look good" turn.

Before writing UI code:

1. Name the screen's single job and the identity you are using (file, repo tokens, or user).
2. List the color roles, type roles, density, and motion that identity already uses. New UI reuses those. It does not introduce a second system.
3. Decide empty, loading, error, disabled, and success for every control this slice owns (`design:ui-copy`).
4. Cut decoration that does not serve the job. One restrained motion beat is enough when motion exists; scattered entrance animations are not.

Then implement to that plan exactly. Meet `design:experience` and
`design:quality-floor` without announcing them.

When the identity is **user-stated and new** (no app yet), still one-shot it: distinctive type pairing from what they asked, a real hierarchy, and none of the AI-default looks listed in `design:professional-craft`. Do not run a catalog or invent a second file.

Landing / marketing first viewport still follows [`taste` React and UI](../taste/reference.md#react-and-ui).

## UI copy

Write from the person's side of the screen:

- Controls are verbs the person recognizes: "Save changes", not "Submit"; "Invite teammate", not "Create user".
- The same word stays through the flow. A "Publish" button yields "Published", not "Success".
- Errors name what went wrong and the next step. They do not apologize and they are not vague.
- Empty states invite the next action. They are not mood copy.
- Placeholders never replace a visible label.

## Experience

Pack bars. Always on, even when `docs/design.md` is silent. Do not invent a
required **Experience** heading in that file. Product exceptions live under
**Preferences**.

| Bar | Fix now | Follow-up |
| --- | --- | --- |
| Least effort | Extra click, extra typing, extra pointer travel, or a detour to reach the thing they asked for | Power-user shortcuts, command palette, bulk actions, keyboard-first as an alternative |
| Do it for them | The next input is obvious and the app still makes them type or pick it (invite `@acme.com` from the signed-in work email) | Suggesting a **guess** as if it were a fact. That is a surprise, not help. |
| Explain complexity | Complex step with no helper, example, or progressive disclosure | Optional tutorials, empty-state tours, docs links as the only explanation |
| Honest state | Control or copy that lies about idle / dirty / pending / success / error / disabled / empty / no-permission | Extra status chrome the product does not need |
| Respect time | Fake wait, full-page block for a fast save, ceremony on a reversible action | Background jobs, optimistic UI polish, progress for genuinely long work |
| Brain-off | Happy path that requires holding several rules in your head | Power features, advanced filters, expert shortcuts |

**Do it for them vs guess.** Do not confuse these. Obvious help is not a surprise (`taste:no-surprises`). A guess is.

| Do it (obvious) | Guess (ask or confirm) |
| --- | --- |
| Invite teammate → prefill `@` + the signed-in user's email domain | Public signup → do not assume a company domain from a gmail address |
| Save draft → keep the text they already typed | Irreversible delete / charge / send-to-everyone → confirm |
| Return to the same screen, same scroll, same filters | Infer a preference they never stated |

A finding that is normal for this product still goes in **Follow-up** if the pack would tighten it. Never a question. If they want the product to stay that way, they say so and you update **Preferences**.

`diverges` from `docs/design.md` is **Fix now**: make the UI match the file. The file changes when the user wants a different design, not when review is guessing.

## Quality floor

| Check | Fix now when | Follow-up when |
| --- | --- | --- |
| Body contrast ≥ 4.5:1 (large text ≥ 3:1) | Body or placeholder fails | Decorative chrome is slightly low |
| Visible keyboard focus | Primary controls have no focus ring | A rarely reached control |
| Touch target ≥ 44×44px on pointer/touch UI | Primary tap target is smaller | Dense data-table glyphs with a larger hit area |
| Visible labels | Placeholder-only, or icon-only with no accessible name | Redundant label next to a named control |
| Primary action not hover-only | The only way to act requires hover | Extra hover hint on an already-clickable control |
| `prefers-reduced-motion` | New motion with no reduced alternative | Existing motion left untouched outside the slice |
| Icons are SVG, not emoji | New UI uses emoji as a control icon | Emoji in user-generated content |

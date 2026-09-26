# Design reference

Load with [SKILL.md](SKILL.md) for the file shape, route inventory, and merge rules. Bars stay in [doctrine.md](doctrine.md).

## Heading skeleton

Write `docs/design.md` with these H2s only. No Screens, Components, Visual language, Preferences, Summary, or other H2s.

```markdown
# Design

UI and UX do / don't for this product. Pack bars live in `/design`, not here.

## Do
- Reuse the live ink, surface, and accent. Do not add a second palette.
- Prefill `@` + the signed-in work domain on team invite.
- Put secondary row actions in a three-dot menu.
- Confirm irreversible delete and charges.

## Don't
- Full-page spinner for a fast save. Use inline progress.
- Placeholder-only labels.
- List every expert setting beside Display name. Advanced goes in an accordion.
- Say "No API key" when Create is already on the screen.
- Write the landing like a docs page, or docs like a slogan.
```

One bullet is one UI/UX rule. Identity, exceptions, and patterns are bullets, not headings. Anything that is not a UI or UX do or don't does not belong. A file that catalogs routes or components is too long: distill it.

## Route inventory

Discover routes from the repo:

| Stack signal | Where to look |
| --- | --- |
| Next.js App Router | `app/**/page.tsx`, `page.jsx`, `page.mdx` |
| Next.js Pages Router | `pages/**/*.tsx` excluding `_app` / `_document` / api |
| React Router | `<Route path=…>` / `createBrowserRouter` objects |
| Expo / RN Router | `app/**` routes excluding `_layout` only files |
| Other | The repo's existing router table; do not guess a framework |

Inventory **every** route from code and look for repeating rules: what everyone needs first, where extra actions hide, what the product refuses, how words work (landing vs in-app vs docs), and look (color roles + hex, type, density from tokens, theme, CSS). Record them only as Do / Don't bullets. Routes whose behavior only shows at runtime are gaps you name in chat; do not invent them. The inventory is input: no subsection per route, no component list.

## Merge into an existing file

1. Read the whole file. User Do / Don't bullets are the rule.
2. Add or tighten a bullet only when this turn observed a new UI/UX rule, the user stated a preference, or the user wants to change how the design is done.
3. Distill Screens, Components, Visual language, and Preferences catalogs into Do / Don't. Keep the user's intent. Delete the dump.
4. Do not restore text the user removed.
5. Do not add a screen subsection.
6. `docs/design.md` is the only path. UI and UX only.

## User-facing vs non-UI work

Use `/design` when the outcome is a screen, component, visible copy, or client interaction. Schema, services, APIs, and other non-UI work follow the code rules directly. When one change touches both, `/design` owns it and still follows `/architecture` for the non-UI files.

## Identity

Stop at the first source that specifies look and feel:

1. Look bullets in `docs/design.md` (color, type, density)
2. Existing tokens / theme / CSS variables in the repo
3. What the user stated this turn

If none exist, ask the user and name the gap. Do not pick a palette "to get started."

## Professional craft

Do the design work in thinking, then ship once. The user should not need a "make it look good" turn.

Before writing UI code:

1. Name the screen's single job and the identity source (file, repo tokens, or user). Name what the words are for: hook and sell, explain, or name the action (`design:ui-copy`). For another language, name the job first, then the term speakers use (`design:spoken-locale`).
2. List the color, type, density, and motion roles that identity already uses. New UI reuses them; no second system.
3. Decide empty, loading, error, disabled, and success for every control you own. If empty is "none yet," the create or invite control is enough (`design:no-obvious`).
4. Name the first glance: what everyone needs, and what sits one level down (`design:first-glance`).
5. Cut decoration that does not serve the job. One restrained motion beat when motion exists; no scattered entrance animations.

Implement that plan exactly. Meet `design:experience`, `design:first-glance`, `design:no-obvious`, `design:ui-copy`, `design:spoken-locale`, and `design:quality-floor` without announcing them.

**User-stated, new identity** (no app yet): still one shot. Distinctive type pairing from what they asked, real hierarchy, none of the AI-default looks in `design:professional-craft`. No catalog, no second file.

Landing / marketing first viewport follows [`taste` React and UI](../taste/reference.md#react-and-ui).

## UI copy

Always on, even when `docs/design.md` is silent. Cite `design:ui-copy`. Product voice (dry landing, playful docs) goes in Do / Don't bullets; do not copy this table there. Unslop covers chat text only: a landing that sells is correct, a landing that reads like a chat reply is wrong.

| Surface | Job of the words |
| --- | --- |
| Landing / marketing | Hook and sell. One claim, one reason to care, a CTA. Not a feature dump or tutorial. First viewport follows [`taste` React and UI](../taste/reference.md#react-and-ui). |
| Docs / help | Explain clearly. Precise steps. No slogans or hype. |
| App (settings, forms, product) | Short. Name the action. Do not sell or lecture. Empty "none yet" is the control (`design:no-obvious`). |
| Errors | What happened and what to do. No apology essay. |

Write from the person's side of the screen:

- Controls are verbs the person recognizes: "Save changes", not "Submit"; "Invite teammate", not "Create user".
- One word through the flow: "Publish" yields "Published", not "Success".
- A sentence that could sit on any other product is filler. Rewrite it for this screen.
- Match existing copy when extending a screen. No second voice.
- Placeholders never replace a visible label.

| Bar | Fix now | Follow-up |
| --- | --- | --- |
| Fits the surface | Landing that explains like docs; docs that sell; app chrome that markets or welcomes | A secondary paragraph a bit long on an otherwise-right surface |
| This product | "Unlock the power of", "Welcome to your dashboard", "Seamlessly", or copy that fits any product | A specific line slightly off the existing voice |
| Real verbs | "Submit", "Success", "An error occurred", or a new name mid-flow | Optional helper that restates a visible verb |
| Empty is the action | "No API key" / "Nothing here" next to Create (`design:no-obvious`) | Extra docs link beside an already-clear action |

## Spoken locale

Always on for strings a person reads, even when `docs/design.md` is silent. Cite `design:spoken-locale`. Product exceptions (keep an English brand name) go in Do / Don't bullets; do not copy this table there.

Translate the **job**, not the source words. The speaker must recognize the term.

1. **Name the job** in one ordinary source-language sentence ("the person removes the background from a photo").
2. **Drop the source phrasing.** Forget "Background remover" as a template.
3. **Ask what speakers call that job.** Reuse the repo's locale term if one exists.
4. **If the repo has none**, use what real products in that locale print for the job. No invented parallel.
5. **Read it as speech.** If it sounds like swapped source words, rewrite. Many languages name a tool with a verb ("Retirer l'arrière-plan") or an established category word ("Détourage"), not an agent-noun mapped to a fake `-eur` / `-er` noun.
6. **Keep that term** on the button, title, empty state, and success. Code paths stay on `taste:naming-files`.

Do not:

- Concatenate dictionary hits (`background` + `remover` → `suppresseur de fond`)
- Invent a noun because English had a noun
- Mix two native terms for one job in one flow
- Keep machine-translation output because it is "technically equivalent"

The same steps apply in every direction (French to English too). The test is the speaker, not the dictionary.

| Bar | Fix now | Follow-up |
| --- | --- | --- |
| Name the job first | Word-for-word swap the speaker would not say | A native term slightly more formal than nearby copy |
| No glued dictionary | Fake compound or invented agent-noun in the shipped string | Extra tooltip restating an already-right label |
| What speakers already say | New parallel term when the locale file or a sibling screen already named the job | Older nearby strings you are not touching |
| One term through the flow | Button and success use different terms for one job | Optional helper repeating the same native term |

## Experience

Always on, even when `docs/design.md` is silent. Product exceptions go in Do / Don't bullets; do not copy this table there.

| Bar | Fix now | Follow-up |
| --- | --- | --- |
| Least effort | Extra click, typing, pointer travel, or a detour to reach what they asked for | Power-user shortcuts, command palette, bulk actions, keyboard-first as an alternative |
| Do it for them | The next input is obvious and the app still makes them type or pick it (invite `@acme.com` from the signed-in work email) | Suggesting a **guess** as if it were a fact (a surprise, not help) |
| Explain complexity | Complex step with no helper or example | Tutorials, tours, or docs links as the only explanation |
| Honest state | Control or copy lies about idle / dirty / pending / success / error / disabled / empty / no-permission | Status chrome the product does not need |
| Respect time | Fake wait, full-page block for a fast save, ceremony on a reversible action | Background jobs, optimistic UI polish, progress for long work |
| Brain-off | Happy path requires holding several rules in your head | Power features already one level down (`design:first-glance`) |

**Do it for them vs guess.** Obvious help is not a surprise (`taste:no-surprises`). A guess is.

| Do it (obvious) | Guess (ask or confirm) |
| --- | --- |
| Invite teammate: prefill `@` + the signed-in user's email domain | Public signup: do not assume a company domain from a gmail address |
| Save draft: keep the text they typed | Irreversible delete / charge / send-to-everyone: confirm |
| Return to the same screen, scroll, and filters | Infer a preference they never stated |

If the UI contradicts `docs/design.md`, make the UI match. The file changes when the user wants a different design (for example a slower or denser path): add a Do / Don't bullet.

## First glance

Always on, even when `docs/design.md` is silent. Cite `design:first-glance`. Product exceptions (show every control) go in Do / Don't bullets.

The first look is what **everyone** needs. Extra actions and advanced settings sit one level down on the **same** screen: overflow (three-dot menu) and popovers for secondary actions, an accordion or Advanced section for expert settings. No beginner mode needed. Use the control the product already uses; the test is the first look, not the widget name.

| Bar | Fix now | Follow-up |
| --- | --- | --- |
| Everyone first | Equal-weight actions, rare settings, or expert toggles beside the common job | Extra hover hint on an already-simple screen |
| One level down | Secondary action is a full toolbar button; advanced settings mixed with everyday ones | Power shortcut already behind overflow |
| Same screen | Related extra action is a new page, wizard, or mode switch | Deep admin console that is a different job |
| Both audiences | Beginner must scan expert chrome, or the expert path was deleted to "simplify" | Command palette / keyboard-first as an alternative |

## Don't tell the obvious

Always on, even when `docs/design.md` is silent. Cite `design:no-obvious`. Product exceptions (an onboarding paragraph on empty) go in Do / Don't bullets.

A missing list plus Create or Invite is the empty state. No "No API key", "You haven't created a key yet", or "Get started by creating your first key." Still write the non-obvious: errors, no-permission, zero search or filter hits, a cost, an irreversible side effect.

| Bar | Fix now | Follow-up |
| --- | --- | --- |
| Don't caption empty | "No API key" / "Nothing here" / "You don't have any yet" next to Create or Invite | Helper restating a visible control label |
| The action is the copy | Onboarding paragraph that only restates the primary button | Docs link beside an already-clear action |
| Say the non-obvious | Zero-hit search with no match copy; permission wall that looks like a blank create screen | Status chrome on a state the control already shows (Saving…) |

## Quality floor

| Check | Fix now when | Follow-up when |
| --- | --- | --- |
| Body contrast ≥ 4.5:1 (large text ≥ 3:1) | Body or placeholder fails | Decorative chrome is slightly low |
| Visible keyboard focus | Primary controls have no focus ring | A rarely reached control |
| Touch target ≥ 44×44px on pointer/touch UI | Primary tap target is smaller | Dense data-table glyphs with a larger hit area |
| Visible labels | Placeholder-only, or icon-only with no accessible name | Redundant label next to a named control |
| Primary action not hover-only | The only way to act requires hover | Extra hover hint on an already-clickable control |
| `prefers-reduced-motion` | New motion with no reduced alternative | Existing motion outside this change left untouched |
| Icons are SVG, not emoji | New UI uses emoji as a control icon | Emoji in user-generated content |

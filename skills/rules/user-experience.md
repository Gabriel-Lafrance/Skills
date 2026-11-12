# User experience

## User-facing work

`ux:user-facing`. Apply these rules to screens, components, styling, visible copy, client interaction, and any string a person reads (including locale files), even when `docs/design.md` is silent, while investigating, preparing tickets, building, and reviewing touched user flows. Backend-only work with no changed user interaction gets no UX section or design questions. When implementing, make UI that contradicts `docs/design.md` match the file.

## Action and continuation

`ux:action-and-continuation`. Before choosing controls, name the user's goal, what the product already knows at the entry point, the primary action and why it belongs, its result, and the next useful step. Follow the touched path until you know the user can finish.

- Keep an action with a distinct user purpose. Combine duplicates, defer actions until their state makes them useful, and remove controls that add no outcome ([First glance](#first-glance) keeps expert actions one level down). A label is interactive only when it performs a useful action; status alone is not a button.
- Carry known company, selection, recommendation, filters, and draft data into the next step. Prefill known values for editing; never make users re-enter them. Do not guess uncertain or consequential inputs.
- Define the useful action in each state: loading, empty, error, cancel, retry. Failed writes preserve edits and offer recovery. Cancel/back returns to a sensible prior context; deliberate discard follows the product's convention. Success tells the truth and prepares the continuation without performing an unauthorized action.
- Before proposing a variant, inspect `docs/design.md`, existing tokens and components, and nearby pages, and reuse their hierarchy, typography, spacing, density, labels, and interaction patterns over a new style. Name any departure and its reason.
- Infer ordinary interaction details from the agreed outcome and current product. Ask only about consequential choices evidence cannot settle, such as an uncertain recipient, irreversible action, or changed scope.

For example, "Create from this recommendation" opens an editable draft seeded with the current company and recommendation. A failed save keeps edits; cancel returns to the recommendation in its prior state. An empty editor fails that contract.

## Source of truth

`ux:source-of-truth`. The only path is **`docs/design.md`** at the workspace root. It is a short **Do** / **Don't** list for this product's UI and UX and nothing else (no screen catalog, component encyclopedia, architecture, data model, API notes, per-route happy path, or second design file).

One bullet is one UI/UX rule, with a short why when not obvious. Identity, exceptions, and patterns are bullets, not headings. Merge duplicates. Keep this file's own rules out of it. If the file is a catalog, distill it to Do / Don't the next time you touch it: keep the user's likes and dislikes, delete agent dumps.

### Heading skeleton

Write `docs/design.md` with these H2s only:

```markdown
# Design

UI and UX do / don't for this product.

## Do
- Reuse the live ink, surface, and accent. Do not add a second palette.
- Prefill `@` + the signed-in work domain on team invite.
- Put secondary row actions in a three-dot menu.
- Confirm irreversible delete and charges.

## Don't
- Full-page spinner for a fast save. Use inline progress.
- Placeholder-only labels.
- Say "No API key" when Create is already on the screen.
```

## Initialization

`ux:initialization`. If `docs/design.md` is missing when implementing UI, name it in chat and offer to write it with the steps below. Write it only when the user says yes; otherwise continue from the existing UI code. Read-only investigation, ticket preparation, and review name the missing file without writing it. `/setup-gabriel-skills` does not write it.

1. Discover **every** route from the app router in code alone (no browser, login, or screenshots).
2. Read those routes and the existing UI for repeating rules: what everyone needs first, where extra actions hide, what the product refuses, how words work (landing vs app vs docs), and look (color roles and hex, type, density from tokens, theme, CSS).
3. Write the short Do / Don't list from what the code proves. Name runtime-only behavior as a gap in chat.

| Stack signal | Where to look |
| --- | --- |
| Next.js App Router | `app/**/page.tsx`, `page.jsx`, `page.mdx` |
| Next.js Pages Router | `pages/**/*.tsx` excluding `_app`, `_document`, `api` |
| React Router | `<Route path=…>` or `createBrowserRouter` objects |
| Expo / RN Router | `app/**` routes excluding `_layout`-only files |
| Other | The repo's existing router table |

Never overwrite an existing `docs/design.md` with a blank template.

## Blend edits

`ux:blend-edits`. Treat the user's added or removed Do / Don't bullets as truth; never restore a deleted bullet.

When implementing a UX complaint (bad UX, too many clicks, too much typing, a different interaction), add or edit a bullet in `docs/design.md` and match the UI in the same turn. The same holds when the user changes how design is done ("skip the confirm on destructive actions" replaces the confirm Do). Read-only investigation, ticket preparation, and review carry the proposed bullet in their output for the implementer; they do not write the file. A written Do or Don't that asks for a slower or denser path is not a defect.

Add or tighten a bullet only when this turn observed a new UI/UX rule, the user stated a preference, or the user changed how design is done.

## Smallest details

`ux:smallest-details`. "Fine" is not done while a small friction remains: a control not ready when needed, a label that misses the job, a state that strands the person, an extra click.

## Identity

Look and feel come from the first source that specifies them:

1. Look bullets in `docs/design.md` (color, type, density)
2. Existing tokens, theme, or CSS variables in the repo
3. What the user stated this turn

If none exist, ask the user and name the gap; do not pick a palette "to get started."

## Experience

`ux:experience`.

| Rule | Meaning | Fix now |
| --- | --- | --- |
| **Least effort** | Type, click, and move the pointer as little as possible | Extra click, typing, pointer travel, or detour |
| **Do it for them** | Do the next input when it is obvious; confirm or ask when it is irreversible, money, or a guess | The app knows the input and still makes them type it |
| **Explain complexity** | A remaining complex step gets a short helper or example in the UI, not jargon | Complex step with no helper; a tour or docs link as the only explanation |
| **Honest state** | UI matches reality: idle, dirty, pending, success, error, disabled, empty, no-permission | "Saved" while the write is in flight or after it failed |
| **Respect time** | Waits are real, a fast save blocks nothing, a reversible action needs no ceremony | Full-page spinner for a 200ms patch |
| **Brain-off** | A person not thinking hard finishes the happy path | Picking among equivalent actions or remembering a hidden rule |

Obvious help is not a surprise (`quality:no-surprises`). A guess is. Signed in as `maya@acme.com`, the invite form prefills `@acme.com`. On public signup as `maya@gmail.com`, leave the domain blank. "Delete workspace" still confirms, even if skipping it saves a click.

Power shortcuts, command palettes, and optimistic polish are Follow-up, not Fix now.

## First glance

`ux:first-glance`. Show only what every user needs at first glance. Put the rest one level down on the same screen.

| Rule | Meaning |
| --- | --- |
| **Everyone first** | The first look is what all users need for the common job, not every action the screen can do |
| **One level down** | Secondary actions go in an overflow (three-dot menu) or popover. Advanced settings go in an accordion or Advanced section |
| **Same screen** | Keep a related action on this screen, one level down, instead of another page, wizard, or mode |
| **Both audiences** | A beginner finishes without hunting. An expert reaches the rest in one more click |

Fix now: a toolbar of equal-weight buttons, or settings that list every expert toggle beside "Display name". Deleting expert controls to "simplify" is also wrong: hide them one level down.

## Don't tell the obvious

`ux:no-obvious`. Say only what the screen does not already show. Omit subtitles or descriptions under page, section or card headings by default, and text that repeats headings, labels or obvious UI behavior.

With no API keys, show the create action and leave out "No API key", "You haven't created a key yet", and "Get started by creating your first key." The blank list plus the button is the message. The same holds for any "none yet".

Still say what is not obvious: an error, a permission wall, a search or filter with zero hits ("No drafts match 'invoice'."), a cost, an irreversible side effect. Keep essential accessibility and non-obvious task guidance. A permission wall that looks like a blank create screen is Fix now.

## Professional craft

`ux:professional-craft`. Ship finished UI in the same turn: the first pass looks designer-completed, not a draft to restyle later. Do the design work in thinking, then ship once:

1. Name the screen's single job, its identity source ([Identity](#identity)), and what the words are for ([UI copy](#ui-copy)).
2. Reuse the color, type, density, and motion roles that identity already uses, in one system.
3. Decide empty, loading, error, disabled, and success for every control you own, and what sits at first glance versus one level down.
4. Cut decoration that does not serve the job. Use at most one restrained motion beat, not scattered entrance animations.

When the app already has a look, match it, even if it is quiet (navy and a serif stays navy and a serif). When the user states a new identity, avoid AI-default looks: cream and terracotta serif, near-black and acid green, purple-on-white gradients, Inter or Roboto-only stacks.

## UI copy

`ux:ui-copy`. Name the surface before you write.

| Surface | Job of the words |
| --- | --- |
| Landing / marketing | Hook and sell: one claim, one reason to care, a CTA. Not a feature dump or tutorial |
| Docs / help | Explain clearly with precise steps in neutral words |
| App (settings, forms, product chrome) | Short. Name the action, then stop |
| Errors | What happened and what to do, in a line or two |

- Controls are verbs the person recognizes: "Save changes", not "Submit"; "Invite teammate", not "Create user".
- One word through the flow: "Publish" yields "Published", not "Success".
- Match this product's existing copy and `docs/design.md` voice bullets. Rewrite a sentence that could sit on any other product ("Unlock the power of", "Welcome to your dashboard", "Seamlessly").
- Every input has a visible label; a placeholder is only a hint.

Chat unslop covers discussion text only: a landing that sells is correct. Docs that sell ("Supercharge your stack with real-time webhook magic") and app chrome that pitches are Fix now.

## Spoken locale

`ux:spoken-locale`. User-visible words in a language sound like a speaker of that language named the job. Translate the job, not the source words. Applies to app UI, locale files, landing, docs, and emails. Code identifiers stay on `quality:naming-files`.

1. Name the job in one ordinary sentence ("the person removes a photo's background"). Drop the source phrasing.
2. Reuse the repo's locale term for that job if one exists. Otherwise use what real products in that locale print.
3. Read it as speech. If a speaker would not say it to a colleague, rewrite.
4. Keep one term on the button, title, empty state, and success.

English "Background remover" is not French "Suppresseur de fond", a noun no speaker uses. French product UI says "Détourage", "Retirer l'arrière-plan", or "Enlever le fond". The reverse holds: "Détourage" becomes "Remove background", not "Detourage" (unless it is a kept brand name). Rewrite machine output even when it is "technically equivalent".

## Quality floor

`ux:quality-floor`. Every user-facing slice meets these, even when `docs/design.md` is silent.

| Check | Fix now when | Follow-up when |
| --- | --- | --- |
| Body contrast ≥ 4.5:1 (large text ≥ 3:1) | Body or placeholder fails | Decorative chrome is slightly low |
| Visible keyboard focus | Primary controls have no focus ring | A rarely reached control |
| Touch target ≥ 44×44px | Primary tap target is smaller | Dense table glyphs with a larger hit area |
| Visible labels | Placeholder-only, or icon-only with no accessible name | Redundant label next to a named control |
| Primary action not hover-only | The only way to act requires hover | Extra hover hint on a clickable control |
| `prefers-reduced-motion` | New motion with no reduced alternative | Existing motion outside this change |
| Icons are SVG, not emoji | New UI uses emoji as a control icon | Emoji in user-generated content |

## React and UI

`ux:react-and-ui`.

- **Mobile first**, then widen.
- One component per file (`quality:one-export-per-file`). Keep components thin: complexity lives in a hook or class behind the entry.
- Marketing and landing UI avoid the [AI-default looks](#professional-craft), flat single-color voids, card-heavy heroes, pill clusters, and emoji decoration.
- Landing first viewport: brand, one headline, one line, CTA, one dominant image, and only those.

## Anti-patterns

- Inventing a workflow or visual identity without evidence, reopening settled decisions over ordinary details, or asking whether a rule here is optional instead of applying it

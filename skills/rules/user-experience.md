# User experience

Cite keys use the `ux:` prefix. Each key below is a heading in this file.

## User-facing work

`ux:user-facing`. These rules apply to user-facing work: screens, components, styling, visible copy, client interaction, and any string a person reads (including locale files). They apply even when `docs/design.md` is silent. Supporting non-UI files in the same area still follow [code-quality.md](code-quality.md) and [code-structure.md](code-structure.md). A typo in a non-UI file is out of scope.

Apply these rules while investigating, preparing tickets, building, and reviewing touched user flows. `/review` checks them within Standards and Spec; there is no separate Design axis or skill. Backend-only work with no changed user interaction needs no UX section or design questions. If the UI contradicts `docs/design.md`, make the UI match the file when implementing.

## Action and continuation

`ux:action-and-continuation`. Before choosing controls, name the user's goal, what the product already knows at the entry point, the primary action and why it belongs, its meaningful result, and the next useful step. Follow the touched path far enough to know whether the user can finish. A button that opens a dialog is not sufficient if that dialog loses the context needed to continue.

- Keep an action with a distinct user purpose. Combine duplicates, defer actions until their state makes them useful, and remove controls that add no outcome. Preserve useful expert actions one level down; simplicity is not deleting supported capability.
- Carry known company, selection, recommendation, filters, and draft data into the next step when relevant. Prefill known values for inspection and editing; do not make users re-enter them. Do not guess uncertain or consequential inputs.
- Define the useful action in each relevant state, including loading, empty, error, cancel, and retry. Failed writes preserve edits and offer recovery. Cancel/back returns to a sensible prior context; deliberate discard follows the product's existing convention. Success tells the truth and prepares the continuation without performing an unauthorized action.
- Inspect `docs/design.md` when present, existing tokens and components, and representative nearby pages before proposing a variant. Reuse the incumbent hierarchy, typography, spacing, density, labels, and interaction patterns. Name any needed departure and its reason. Read external guidance only for the unresolved concern; product conventions win over a style catalog.
- Infer ordinary interaction details from the agreed outcome and current product. Ask only about consequential choices that evidence cannot settle, such as an uncertain recipient, irreversible action, or changed scope. Do not ask the user to design every control.

For example, "Create from this recommendation" opens an editable draft seeded with the current company and recommendation. A failed save keeps edits; cancel returns to the recommendation in its prior state. A beautiful empty editor fails that contract.

### Sources

This integration is an original, selective synthesis, checked against these sources on 2026-10-03. No upstream skill, checklist, or implementation is vendored. Product conventions and the agreed outcome govern how the guidance applies.

- [UI/UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/477bcb28c9812b385cb51a4605ddf30d7b2266e2/.claude/skills/ui-ux-pro-max/SKILL.md) and [UX guidelines](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/477bcb28c9812b385cb51a4605ddf30d7b2266e2/src/ui-ux-pro-max/data/ux-guidelines.csv): scoped retrieval, redundant entry, control semantics, and feedback. [MIT](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/477bcb28c9812b385cb51a4605ddf30d7b2266e2/LICENSE), copyright 2024 Next Level Builder.
- [Impeccable references](https://github.com/pbakaus/impeccable/tree/e103efe779e2dd01274dabae83531fef00bf2563/skill/reference) (`distill`, `critique`, `operate`, `new-work`, `harden`): purposeful actions, familiar operational UI, reuse, and recovery. [Apache 2.0](https://github.com/pbakaus/impeccable/blob/e103efe779e2dd01274dabae83531fef00bf2563/LICENSE), copyright 2025 Paul Bakaus.
- [Vercel Web Interface Guidelines](https://github.com/vercel-labs/web-interface-guidelines/blob/e3d624baaf29dc1fc645aff3e38f03e564d2d6b1/command.md): state, navigation, keyboard, and focus checks. [MIT](https://github.com/vercel-labs/web-interface-guidelines/blob/e3d624baaf29dc1fc645aff3e38f03e564d2d6b1/LICENSE), copyright 2025 Vercel Labs.
- [Anthropic frontend-design](https://github.com/anthropics/skills/blob/8a1541c4a3ffa5a20a5a91de0dcf3f0bab1d1ef4/skills/frontend-design/SKILL.md): brief, visual hierarchy, type, spacing, and rendered critique. [Apache 2.0](https://github.com/anthropics/skills/blob/8a1541c4a3ffa5a20a5a91de0dcf3f0bab1d1ef4/skills/frontend-design/LICENSE.txt).

## Source of truth

`ux:source-of-truth`. The only path is **`docs/design.md`** at the workspace root. It is a short **Do** / **Don't** list for this product's UI and UX and nothing else (no screen catalog, component encyclopedia, architecture, data model, API notes, per-route happy path, or second design file).

One bullet is one UI/UX rule, with a short why when it is not obvious. Identity, exceptions, and patterns are bullets, not headings. Merge duplicates. Keep this file's own rules out of it. If the file is already a catalog, distill it to Do / Don't the next time you touch it: keep the user's likes and dislikes, delete agent dumps.

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

`ux:initialization`. If `docs/design.md` is missing when implementing UI, write it first, then continue. Read-only investigation, ticket preparation, and review inspect existing product evidence and name the missing file without writing it. `/setup-gabriel-skills` does not write it.

1. Discover **every** route from the app router in code alone (no browser, login, or screenshots).
2. Read those routes and the existing UI. Look for repeating rules: what everyone needs first, where extra actions hide, what the product refuses, how words work (landing vs app vs docs), and look (color roles and hex, type, density from tokens, theme, CSS).
3. Write the short Do / Don't list from what the code proves. Name runtime-only behavior as a gap in chat.

| Stack signal | Where to look |
| --- | --- |
| Next.js App Router | `app/**/page.tsx`, `page.jsx`, `page.mdx` |
| Next.js Pages Router | `pages/**/*.tsx` excluding `_app`, `_document`, `api` |
| React Router | `<Route path=…>` or `createBrowserRouter` objects |
| Expo / RN Router | `app/**` routes excluding `_layout`-only files |
| Other | The repo's existing router table |

Never overwrite an existing `docs/design.md` with a blank template. A partial route inventory is not complete.

## Blend edits

`ux:blend-edits`. The user may add or remove Do / Don't bullets. The next run treats those bullets as truth. Deleted bullets stay deleted, and the file is the only copy.

When implementing a UX complaint, update `docs/design.md` in the same turn. When the user says the UX is bad, too many clicks, too much typing, or wants a different interaction, add or edit a bullet and match the UI. Read-only investigation, ticket preparation, and review carry the proposed bullet in their existing output for the implementer; they do not write the file. The same holds when the user changes how design is done (for example, "skip the confirm on destructive actions" replaces the confirm Do). Edit the bullet as well as the component when implementing. A written Do or Don't that asks for a slower or denser path is not a defect.

Add or tighten a bullet only when this turn observed a new UI/UX rule, the user stated a preference, or the user changed how design is done.

## Smallest details

`ux:smallest-details`. Excellence is usually a small, specific thing: the control that is ready when needed, the label that matches the job, the state that does not strand the person, the extra click that should not exist. Judge and build at that grain. "Fine" is not done while a smaller friction remains.

## Identity

Look and feel come from the first source that specifies them:

1. Look bullets in `docs/design.md` (color, type, density)
2. Existing tokens, theme, or CSS variables in the repo
3. What the user stated this turn

If none exist, ask the user and name the gap instead of picking a palette "to get started."

## Experience

`ux:experience`. Product exceptions (slower money flow, extra confirm) live as Do / Don't bullets.

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

`ux:first-glance`. Show only what every user needs at first glance. Put the rest one level down on the same screen. This is the UI version of a deep public surface (`structure:deep-public-surface`).

| Rule | Meaning |
| --- | --- |
| **Everyone first** | The first look is what all users need for the common job, not every action the screen can do |
| **One level down** | Secondary actions go in an overflow (three-dot menu) or popover. Advanced settings go in an accordion or Advanced section |
| **Same screen** | Keep a related action on this screen, one level down, instead of another page, wizard, or mode |
| **Both audiences** | A beginner finishes without hunting. An expert reaches the rest in one more click |

Fix now: a toolbar of equal-weight buttons, or settings that list every expert toggle beside "Display name". "Simplifying" by deleting expert controls is also wrong: hide them one level down instead.

## Don't tell the obvious

`ux:no-obvious`. Say only what the screen does not already show.

With no API keys, show the create action and leave out "No API key", "You haven't created a key yet", and "Get started by creating your first key." The blank list plus the button is the message. The same holds for drafts, teammates, and any "none yet".

Still say what is not obvious: an error, a permission wall, a search or filter with zero hits ("No drafts match 'invoice'."), a cost, an irreversible side effect. A permission wall that looks like a blank create screen is Fix now.

## Professional craft

`ux:professional-craft`. Ship finished UI in the same turn. The first pass looks like a designer completed it, not a draft to restyle later. Do the design work in thinking, then ship once:

1. Name the screen's single job, the identity source ([Identity](#identity)), and what the words are for ([UI copy](#ui-copy)).
2. List the color, type, density, and motion roles that identity already uses. New UI reuses them, in one system.
3. Decide empty, loading, error, disabled, and success for every control you own.
4. Name the first glance and what sits one level down.
5. Cut decoration that does not serve the job. When motion exists, use one restrained motion beat instead of scattered entrance animations.

When the app already has a look, match it, even if it is quiet (navy and a serif stays navy and a serif). When the user states a new identity, avoid AI-default looks: cream and terracotta serif, near-black and acid green, purple-on-white gradients, Inter or Roboto-only stacks. Landing first viewport follows [React and UI](#react-and-ui).

## UI copy

`ux:ui-copy`. Interface words are design material. Name the surface before you write.

| Surface | Job of the words |
| --- | --- |
| Landing / marketing | Hook and sell: one claim, one reason to care, a CTA. Not a feature dump or tutorial |
| Docs / help | Explain clearly with precise steps in neutral words |
| App (settings, forms, product chrome) | Short. Name the action, then stop |
| Errors | What happened and what to do, in a line or two |

- Controls are verbs the person recognizes: "Save changes", not "Submit"; "Invite teammate", not "Create user".
- One word through the flow: "Publish" yields "Published", not "Success".
- Match this product's existing copy and `docs/design.md` voice bullets. A sentence that could sit on any other product ("Unlock the power of", "Welcome to your dashboard", "Seamlessly") is filler. Rewrite it.
- Every input has a visible label; a placeholder is only a hint.

Chat unslop covers discussion text only: a landing that sells is correct. Docs that sell ("Supercharge your stack with real-time webhook magic") and app chrome that pitches are Fix now.

## Spoken locale

`ux:spoken-locale`. User-visible words in a language sound like a speaker of that language named the job. Translate the job, not the source words. Applies to app UI, locale files, landing, docs, and emails. Code identifiers stay on `quality:naming-files`.

1. Name the job in one ordinary sentence ("the person removes a photo's background"). Drop the source phrasing.
2. Reuse the repo's locale term for that job if one exists. Otherwise use what real products in that locale print.
3. Read it as speech. Would a speaker say this to a colleague? If not, rewrite.
4. Keep one term on the button, title, empty state, and success.

English "Background remover" is not French "Suppresseur de fond": that glues dictionary hits into a noun no speaker uses. French product UI says "Détourage", "Retirer l'arrière-plan", or "Enlever le fond". The reverse holds: "Détourage" becomes "Remove background", not "Detourage" (unless it is a kept brand name). Reuse the locale file's term when it already names the job, and rewrite machine output even when it is "technically equivalent".

## Quality floor

`ux:quality-floor`. Every user-facing slice meets these, even when `docs/design.md` never mentions them.

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
- Marketing and landing UI avoid AI-default looks: purple-on-white gradients, cream and terracotta serif, flat single-color voids, card-heavy heroes, pill clusters, emoji decoration.
- Landing first viewport: brand, one headline, one line, CTA, one dominant image, and only those.

## Anti-patterns

- Inventing a new product workflow or visual identity without evidence, or treating ordinary interaction details as permission to reopen settled decisions
- Growing `docs/design.md` into hundreds of lines or a catalog when a short Do / Don't list would do
- Asking whether a rule miss here is optional instead of applying it while building
- Treating "the UI looks fine" as done while extra clicks, keystrokes, or pointer travel remain

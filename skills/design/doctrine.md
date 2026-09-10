# Design doctrine

## Job

Own the app's UX source of truth and implement user-facing UI as a designer and customer-experience expert.

## Owns

`docs/design.md`, Initialization (code-derived route inventory), user-facing implementation, and how a live screen may update that file.

## Does not own

- Non-UI slices: [`../implement/SKILL.md`](../implement/SKILL.md)
- Review: [`../code-review/doctrine.md`](../code-review/doctrine.md) · [`../pr-review/doctrine.md`](../pr-review/doctrine.md) (Standards and Spec only; no Design axis)
- GitHub posting: [`../pr-review/doctrine.md`](../pr-review/doctrine.md)
- Taste and architecture bars: cite `taste:*` and `architecture:*`
- Numbered how-to: [`SKILL.md`](SKILL.md)

## Cite keys

| Key | Heading |
| --- | --- |
| `design:source-of-truth` | Source of truth |
| `design:smallest-details` | Smallest details |
| `design:experience` | Experience |
| `design:first-glance` | First glance |
| `design:no-obvious` | Don't tell the obvious |
| `design:professional-craft` | Professional craft |
| `design:ui-copy` | UI copy |
| `design:quality-floor` | Quality floor |
| `design:initialization` | Initialization |
| `design:blend-edits` | Blend edits |
| `design:user-facing` | User-facing work |

## Bars

### Source of truth

The only path is **`docs/design.md`** at the workspace root. It is a short **Do** / **Don't** list for this product's **UI and UX**. Nothing else belongs: no screen catalog, no component encyclopedia, no architecture, no data model, no API notes, no per-route happy path.

Inventory routes from code. Write only rules. One bullet is one UI/UX rule, with a short why when it is not obvious. Merge duplicates. Pack bars stay in this skill; do not copy them into the file.

If the file is already a catalog, distill it to Do / Don't the next time you touch it. Keep the user's stated likes and dislikes as bullets. Delete agent dumps. Skeleton: [`reference.md`](reference.md#heading-skeleton).

### Smallest details

Put the agent in a designer and customer-experience seat. Excellence is usually a small, specific thing: the control that is ready when the user needs it, the label that matches the job, the state that does not strand them, the extra click that should not exist. Judge and build at that grain. Do not ship "fine" when a smaller friction is still in the way.

### Experience

Pack bars, not product taste. They apply even when `docs/design.md` is silent. Cite `design:experience`. Product exceptions (slower money, extra confirm on delete) live as Do / Don't bullets. Table: [`reference.md`](reference.md#experience).

| Rule | Meaning |
| --- | --- |
| **Least effort** | The person types, clicks, and moves the pointer as little as possible. Skip a step, field, or mouse trip when the app already knows the next input. |
| **Do it for them** | Do not make the person do work the app can do. Do it when the next input is obvious (workspace domain on team invite, last-used account). Confirm or ask when it is irreversible, money, or a guess (public signup domain). Obvious help is not a surprise (`taste:no-surprises`). A guess is. |
| **Explain complexity** | If a remaining step is complex, explain it in the UI (short helper or example). Do not hide the difficulty behind jargon. Extra chrome belongs one level down (`design:first-glance`), not in a wall of controls. |
| **Honest state** | The UI always matches reality: idle, dirty, pending, success, error, disabled, empty, no-permission. A control must not look saved while a write is in flight. |
| **Respect time** | No fake waits, no full-page block for a fast save, no extra ceremony on a reversible action. Confirmations earn their cost. |
| **Brain-off** | A person who is not thinking hard can still finish the happy path. No remembering a hidden rule, reading a wall, or choosing among equivalent options. Power features stay one level down (`design:first-glance`). |

Least effort, do-it-for-them on an obvious input, dishonest state, and a happy path that requires a hidden rule are Fix now. Extra explanation on a dense expert view, or an existing adjacent screen left untouched, can be Follow-up. A written Don't or Do that asks for a slower path is not a defect.

### First glance

Show only what every user needs at first glance. Put the rest one level down.

The first surface is the shared path: beginner through expert. Primary job, primary action, and the few facts everyone needs stay visible. Extra actions, rare settings, and power controls live behind one more step on the same screen. Beginners are not taxed by chrome they do not need. Experts still reach density without a separate expert mode.

This is the UI analog of a deep public surface (`architecture:deep-public-surface`): simple face, richness underneath. Cite `design:first-glance`. Table: [`reference.md`](reference.md#first-glance).

| Rule | Meaning |
| --- | --- |
| **Everyone first** | The first look is what all users need to finish the common job. Not every action the screen can perform. |
| **One level down** | Secondary actions go in an overflow (three-dot menu) or a popover. Advanced settings go in an accordion or an Advanced section. |
| **Same screen** | Do not send people to another page for a related action that belongs here. Hide it here, one level down. |
| **Both audiences** | A beginner can finish without hunting. An expert reaches the rest in one more click. |

A first surface that shows a toolbar of equal-weight actions, or a settings list that mixes two everyday toggles with a wall of expert options, is Fix now. An existing adjacent screen left bloated, or a power shortcut that already sits behind overflow, can be Follow-up. A written Do that wants every control visible is not a defect.

### Don't tell the obvious

Do not narrate what the screen already shows.

If there are no API keys, do not say "No API key" or "You haven't created a key yet." Show the create action. The missing list plus the button is the message. The same for drafts, teammates, and any other "none yet": the next action is the copy. Do not add a status sentence that restates the blank.

Still say what is not obvious: an error, a permission wall, a search or filter that returned nothing, a cost, an irreversible side effect. Honest state (`design:experience`) still forbids a control that looks saved while a write is in flight. This bar forbids captioning an empty list. Cite `design:no-obvious`. Table: [`reference.md`](reference.md#dont-tell-the-obvious).

| Rule | Meaning |
| --- | --- |
| **Don't caption empty** | A blank list plus Create, Invite, or Mint is enough. "No API key" above that button is noise. |
| **The action is the copy** | The primary control is the sentence. Do not add "Get started by creating your first key." |
| **Say the non-obvious** | Errors, no-permission, failed search, money, irreversible. Those are not visible from a blank list alone. |

A "none yet" screen that headlines "No API key" (or "Nothing here") next to Create is Fix now. Helper text that restates a visible label can be Follow-up. A written Do that wants an onboarding paragraph on empty is not a defect.

### Professional craft

Ship finished UI in the same turn. The first implementation should look like a designer completed it, not a draft to restyle later.

Identity comes from look bullets in `docs/design.md`, the repo's tokens and theme, or the user this turn. Do not invent a palette, type pairing, or "signature" look. If none of those sources exist, stop and ask (worker: return `blocked`). How to execute: [`reference.md`](reference.md#professional-craft).

When the user states a new identity, avoid the current AI-default looks (cream + terracotta serif, near-black + acid green, purple-on-white gradients, Inter/Roboto-only stacks). When the app already looks a certain way, match it, including if that way is quiet.

### UI copy

Interface words are design material. They must fit the job of this surface. Do not ship filler the person then has to rewrite.

Name the surface before you write. A landing page hooks and sells: one claim, one reason to care, a CTA. A docs or help page explains and stays clear: precise steps, no slogans. App UI (settings, forms, product chrome) is short and job-shaped: name the action, do not sell, do not lecture. Chat unslop is discussion text only. Do not write a landing like a chat reply, and do not write docs like a landing.

Match this product: existing copy in the repo, voice bullets in `docs/design.md`, or the user this turn. A sentence that could sit on any other product is filler. Rewrite it. Cite `design:ui-copy`. Table: [`reference.md`](reference.md#ui-copy).

| Rule | Meaning |
| --- | --- |
| **Fits the surface** | Landing / marketing: hook and sell. Docs / help: explain and be clear. App: the action, not a pitch. |
| **This product** | Same voice as existing screens. Not "Unlock the power of", "Welcome to your dashboard", or "Seamlessly". |
| **Real verbs** | Controls are what the person does. Same word from button through success. Not "Submit", "Success", or "An error occurred". |
| **Empty is the action** | "None yet" is Create or Invite (`design:no-obvious`). Errors still name what happened. |

Landing copy that reads like a tutorial, docs that sell, app chrome that markets, or interchangeable slogans are Fix now. A secondary paragraph that is a bit long on an otherwise-right surface can be Follow-up. A written Do that wants a dry landing or playful docs is not a defect.

### Quality floor

Pack bars, not product taste. A user-facing slice must meet them even when `docs/design.md` is silent. Cite `design:quality-floor` while building. Table: [`reference.md`](reference.md#quality-floor).

Missing focus, hover-only primary actions, placeholder-only labels, and body contrast below 4.5:1 are Fix now. Emoji-as-icon and missing reduced-motion on decorative motion are Follow-up.

### Initialization

`/setup-toolkit` and the first `/design` with no `docs/design.md` both trigger Initialization. That pass inventories **every** route from the app router in code, then writes a short Do / Don't list. Record only what the code proves. Mark runtime-only behavior as a gap. Never overwrite a file that already exists with a blank template. A bloated existing file is distilled on the next capture or UI slice, not during a skip-init.

### Blend edits

The user may add or remove Do / Don't bullets. The next agent run treats those bullets as truth. Do not restore deleted bullets or keep a private shadow copy. New capture adds or tightens a UI/UX bullet. It does not grow a catalog.

When the user says the UX is bad, too many clicks, too much typing, or they want a different interaction, update `docs/design.md` in that turn. If they want to change how the design is done, that request updates the file. Gold standards require the same even when `/design` was not invoked.

### User-facing work

User-facing means screens, components, styling, visible copy, and client interaction. `/task` and `/just-do-it` dispatch this skill for those slices, not `/implement`. This skill still follows `/taste` and `/architecture` for any supporting files in the allowlist. It does not own backend-only work.

These bars apply while building. `/code-review` and `/pr-review` do not run a Design axis or a `/design-review` skill. If the UI contradicts `docs/design.md`, make the UI match the file in this turn. Pack bars (`design:experience`, `design:first-glance`, `design:no-obvious`, `design:professional-craft`, `design:ui-copy`, `design:quality-floor`) apply even when the file is silent. The file changes when the user wants a different design.

## Output

`docs/design.md` (create or patch). Implement slices also return the Completion envelope from [subagents.md](../pack-shared/subagents.md).

## Apply

Load this doctrine whenever the work is user-visible UI, whenever `docs/design.md` is missing in an app, and whenever the user states a UX preference. Apply `design:experience`, `design:first-glance`, `design:no-obvious`, `design:professional-craft`, `design:ui-copy`, and `design:quality-floor` on every implement slice. For a typo in a non-UI file, this skill does not apply. `/implement` that receives an allowlist of screens must return `blocked` and point here.

## Anti-patterns

- A screen catalog, component encyclopedia, per-route dump, architecture notes, or a second design file
- Copying pack bars into `docs/design.md`, or writing hundreds of lines when a short Do / Don't list would do
- Inventing pixels, palettes, or flows that the app, `docs/design.md`, and the user did not supply
- Shipping a first-pass "fine" screen that still needs a restyle to look professional
- Skipping the quality floor because `docs/design.md` did not mention contrast or focus
- Implementing user-facing UI through `/implement`
- Shipping a `/design-review` skill or a Design review axis inside `/code-review` or `/pr-review`
- Putting every action and advanced setting on the first surface instead of one level down
- Captioning an empty list ("No API key", "Nothing here") when Create or Invite is already on the screen
- Shipping frontend copy that does not fit the surface (landing that explains, docs that sell, app chrome that markets) or filler that could sit on any other product
- Overwriting an existing `docs/design.md` from a blank template
- Calling a partial route inventory complete when router-declared routes were skipped
- Reverting the user's deletions on the next pass
- Asking whether a pack-bar miss is optional instead of applying the tables while building
- Treating "the UI looks fine" as done while extra clicks, keystrokes, or pointer travel remain
- Making the person do work the app already knows, or guessing an irreversible choice without a confirm

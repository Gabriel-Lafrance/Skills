# Design examples

## Experience (do it for them)

**Good:** Signed-in user is `maya@acme.com`. Invite teammate form prefills `@acme.com`. The next input is obvious. That is not a surprise (`taste:no-surprises`). Making her retype `acme.com` is leftover work. `docs/design.md` records it as a Do bullet.

**Bad:** The same append on public signup as `maya@gmail.com`. That is a guess. Leave the domain blank or ask.

**Bad:** Skipping the confirm on "Delete workspace" because fewer clicks felt faster. Irreversible work confirms.

## Honest state

**Good:** Save button reads "Saving…" and stays disabled while the write is in flight. It does not look saved.

**Bad:** Button flips to "Saved" on click, then the request fails and the row never changed.

## Respect time

**Good:** A fast save shows inline progress on the same screen.

**Bad:** A full-page spinner for a 200ms patch. Extra ceremony on a reversible action.

## Brain-off

**Good:** New draft starts from one primary button. Advanced options stay one level down (`design:first-glance`).

**Bad:** Happy path asks the person to pick among three equivalent "create" actions and remember which one keeps the draft.

## First glance

**Good:** A row's primary action is the thing everyone does (Open, or the row itself). Duplicate, export, and delete sit in a three-dot menu or a popover. Settings show the two everyday toggles; API keys, webhooks, and retention live in an Advanced accordion.

**Bad:** A toolbar of eight equal buttons, or a settings page that lists every expert toggle beside "Display name". Beginners scan chrome they do not need. Experts do not get a denser path; they get a noisier one.

**Bad:** "Simplifying" by deleting the expert controls. First glance hides them one level down. It does not remove them.

## Don't tell the obvious

**Good:** The user has not minted an API key. The screen is the create actions (secret key, publishable key). No headline that says they have none.

**Bad:** The same screen with "No API key" or "You haven't created a key yet" above those buttons. The blank list already said that.

**Good:** Search for `invoice` returns nothing. Copy says "No drafts match 'invoice'." That is not visible from a blank list after a query.

**Bad:** A permission wall that only shows a blank list and Create, with no note that they need admin to mint. No-permission is not obvious.

## User said the UX is bad

User: "Having to type the full company domain every invite is bad UX."

**Good:** Update `docs/design.md` in that turn. Add a Do bullet: prefill the workspace domain on invite, and when not to (unknown domain, personal email). Then, if this chat is also implementing, match the UI.

**Bad:** Nod in chat and leave `docs/design.md` untouched until someone remembers `/design`.

## User wants to change how design is done

The user says destructive actions should skip the confirm dialog. That is how design is done for this product. Add a Don't bullet (no confirm on destructive actions) or replace the confirm Do. Do not only change the component.

## Blend edits

The user deletes a "use toast for every save" bullet and adds "inline confirmation on the row."

**Good:** The next capture or implement pass follows inline confirmation. It does not put the toast bullet back.

**Bad:** The agent re-adds toasts because an old build once showed one, even though the user deleted that bullet.

## Initialization

**Good:** A Task inventories every route from the app router in code, then writes a short Do / Don't list (look from theme tokens, invite prefill, overflow for extra actions, landing hooks vs docs explain). No Screens heading. No component dump.

**Bad:** One subsection per route, hover/disabled/loading on every component, and a 400-line file.

**Bad:** A one-paragraph "overall look and feel" note with no do or don't.

## docs/design.md is a short list

**Good:** Two headings, Do and Don't. Identity is a look bullet. Exceptions are bullets. The file scans in one sitting.

**Bad:** Visual language + Components + Patterns + Screens / flows + Preferences, with a happy path for each route. That is not UI/UX rules. That is a catalog.

## Professional craft

**Good:** Invite screen reuses the app's existing ink, surface, and accent hexes, the body type already in `layout.tsx`, and ships with a visible label, focus ring, an Invite teammate control (no "No teammates" caption), and error next to the field. No second "make it pretty" turn.

**Bad:** First pass is a gray form with "Submit" and Inter on a purple gradient, then a follow-up prompt to restyle it to match the app.

**Bad:** The app is already navy + source-serif. The agent "improves" it to cream + terracotta because that is a distinctive look.

## Missing identity

**Good (parent, one-off):** No look bullets, no theme tokens, user has not stated a look. Ask what the product should feel like. Do not pick a palette.

**Bad:** Invent "soft spa pink" so work can start.

## Quality floor

**Good:** New primary button is 44px tall, has a visible `:focus-visible` ring, and 4.5:1 contrast. Icon-only "more" has `aria-label="More actions"`.

**Bad:** Placeholder-only email field, emoji as the invite icon, hover-only delete on a row. Do not skip these because `docs/design.md` never mentioned contrast.

## UI copy

**Good (landing):** Headline is the outcome they want. One line of proof. One CTA. The first viewport is brand + that headline + that line + CTA + one image (`taste` React and UI).

**Bad (landing):** "Our platform enables teams to seamlessly manage API keys." That is filler. Or a feature dump. Or a tutorial. Landing hooks and sells.

**Good (docs):** "Webhooks POST a JSON body to your endpoint. Return 2xx within 5 seconds." Clear. No slogan.

**Bad (docs):** "Supercharge your stack with real-time webhook magic." Docs explain. They do not sell.

**Good (app):** Button "Publish". Toast "Published". Empty drafts: New draft only. No "No drafts yet."

**Bad (app):** "Welcome to your workspace! Let's get you started on your journey." Settings and product chrome name the action. They do not pitch.

**Bad:** Copy that could sit on any other product unchanged. Rewrite it for this screen.

## User-facing UI without `/design`

Worker shipped a settings page under `/implement`. Parent did not dispatch `/design`. **Wrong.** Route the UI through `/design`. `/implement` stays on the non-UI slice.

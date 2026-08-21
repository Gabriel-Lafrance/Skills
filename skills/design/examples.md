# Design examples

## Experience (do it for them)

**Good:** Signed-in user is `maya@acme.com`. Invite teammate form prefills `@acme.com`. The next input is obvious. That is not a surprise (`taste:no-surprises`). Making her retype `acme.com` is leftover work. `docs/design.md` records the pattern and the why under Patterns / behavior.

**Bad:** The same append on public signup as `maya@gmail.com`. That is a guess. Leave the domain blank or ask.

**Bad:** Skipping the confirm on "Delete workspace" because fewer clicks felt faster. Irreversible work confirms.

## Honest state

**Good:** Save button reads "Saving…" and stays disabled while the write is in flight. It does not look saved.

**Bad:** Button flips to "Saved" on click, then the request fails and the row never changed.

## Respect time

**Good:** A fast save shows inline progress on the same screen.

**Bad:** A full-page spinner for a 200ms patch. Extra ceremony on a reversible action.

## Brain-off

**Good:** New draft starts from one primary button. Advanced options stay behind an optional control.

**Bad:** Happy path asks the person to pick among three equivalent "create" actions and remember which one keeps the draft.

## User said the UX is bad

User: "Having to type the full company domain every invite is bad UX."

**Good:** Update `docs/design.md` in that turn. Add or extend the invite pattern: append the workspace domain, why it saves typing, and when not to (unknown domain, personal email). Then, if this chat is also implementing, match the UI.

**Bad:** Nod in chat and leave `docs/design.md` untouched until someone remembers `/design`.

## User wants to change how design is done

The user says destructive actions should skip the confirm dialog. That is how design is done for this product. Blend-edit `docs/design.md` **Preferences** (and **Patterns** if the destructive row changes). Do not only change the component.

## Blend edits

The user deletes a "use toast for every save" bullet and adds "inline confirmation on the row."

**Good:** The next capture or implement pass follows inline confirmation. It does not put the toast bullet back.

**Bad:** The agent re-adds toasts because the last Browser crawl still showed one on an old build.

## Initialization

**Good:** Parent asks the user to log in. A Task visits every route from the app router and writes Visual language (observed hex and type), Screens / flows, and Components without a Summary.

**Bad:** A one-page screenshot and a short "overall look and feel" paragraph that will go stale.

## Design finding is Fix now or Follow-up (never an ask)

User-facing work. Design axis found a mismatch. Put it in the table. Do not ask if it is normal.

```markdown
### Design
`docs/design.md` **Patterns** say inline progress. The live submit is a full-page spinner. `design:experience` Respect time.

| Severity | Where | What | Why (cite) | Fix |
| --- | --- | --- | --- | --- |
| Fix now | `SaveButton.tsx` | Full-page spinner on a fast save | `docs/design.md` Patterns; `design:experience` | Inline progress on the same screen |
```

If the product **must** keep the spinner, the user says so. Then blend-edit **Preferences**. Do not guess that and ask.

Undocumented UI that already respects the pack bars is **Follow-up**: `/design` records the pattern. Do not revert the UI. Do not ask "is this normal?"

## Professional craft

**Good:** Invite screen reuses the app's existing ink, surface, and accent hexes, the body type already in `layout.tsx`, and ships with a visible label, focus ring, empty state ("Invite a teammate to share this workspace"), and error next to the field. No second "make it pretty" turn.

**Bad:** First pass is a gray form with "Submit" and Inter on a purple gradient, then a follow-up prompt to restyle it to match the app.

**Bad:** The app is already navy + source-serif. The agent "improves" it to cream + terracotta because that is a distinctive look.

## Missing identity

**Good (parent, one-off):** Visual language is empty, no theme tokens, user has not stated a look. Ask what the product should feel like. Do not pick a palette.

**Bad:** Invent "soft spa pink" so work can start.

## Quality floor

**Good:** New primary button is 44px tall, has a visible `:focus-visible` ring, and 4.5:1 contrast. Icon-only "more" has `aria-label="More actions"`.

**Bad:** Placeholder-only email field, emoji as the invite icon, hover-only delete on a row. Review must not skip these because `docs/design.md` never mentioned contrast.

## UI copy

**Good:** Button "Publish". Toast "Published". Empty: "No drafts yet. New draft starts one."

**Bad:** Button "Submit". Toast "Success". Empty: "Nothing here."

## User-facing UI without `/design`

Worker shipped a settings page under `/implement`. Parent did not dispatch `/design`. **Wrong.** Route the UI through `/design`. `/implement` stays on the non-UI slice.

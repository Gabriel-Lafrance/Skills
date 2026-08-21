# Design examples

## Fewer clicks

**Good:** Team invite email field auto-appends `@acme.com` because members share the company domain. That saves keystrokes on the most likely invite. `docs/design.md` records the pattern and the why under Patterns / behavior.

**Bad:** The same append with no note in `docs/design.md`, so review cannot tell accident from intent.

**Bad:** Auto-appending a random consumer domain on a public signup. The next input is not obvious; that surprises the user (`taste:no-surprises`).

## User said the UX is bad

User: "Having to type the full company domain every invite is bad UX."

**Good:** Update `docs/design.md` in that turn. Add or extend the invite pattern: append the workspace domain, why it saves typing, and when not to (unknown domain, personal email). Then, if this chat is also implementing, match the UI.

**Bad:** Nod in chat and leave `docs/design.md` untouched until someone remembers `/design`.

## Blend edits

The user deletes a "use toast for every save" bullet and adds "inline confirmation on the row."

**Good:** The next capture or implement pass follows inline confirmation. It does not put the toast bullet back.

**Bad:** The agent re-adds toasts because the last Browser crawl still showed one on an old build.

## Initialization

**Good:** Parent asks the user to log in. A Task visits every route from the app router and writes Visual language (observed hex and type), Screens / flows, and Components without a Summary.

**Bad:** A one-page screenshot and a short "overall look and feel" paragraph that will go stale.

## Design-review ask

The diff appends `@acme.com` on invite. `docs/design.md` does not mention it.

**Good (parent, after the Design worker reports the divergence):**

```markdown
## Questions
Reply like: 1a

1. Invite email appends `@acme.com` for team members. That is not in docs/design.md. Is this normal?
   - a) No: change the UI to match the design file recommended
   - b) Yes: keep it and update the design file (say why it saves work)
```

If **1a**, Fix now on the UI. If **1b**, `/design` writes the fewer-clicks why into `docs/design.md` and the finding is not a UI fix.

**Bad:** Auto-fail the review because the file was silent. **Bad:** Auto-pass because shipping it must mean it is fine.

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

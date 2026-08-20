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

**Good:** Parent asks the user to log in. A Task visits every route from the app router and writes Screens / flows plus Components without a Summary.

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

# User experience

## App UX source of truth

`docs/design.md` (workspace root, that path only) is a short **Do** / **Don't** list for this app's UI and UX when the file exists. No screen catalog, no component encyclopedia, no architecture.

If the user says something is bad for the UX, too many clicks, too much typing, or they want a different interaction, update `docs/design.md` in the same turn. If the user wants to change how the design is done, that request updates `docs/design.md`. If the file is missing, run `/design` Initialization first. Do not wait for a separate `/design` invoke.

Frontend and user-facing implementation uses `/design`. Ship finished UI in that turn (`design:professional-craft`): identity from `docs/design.md`, the repo's tokens and theme, or the user, never invented. Apply `design:experience` even when the file is silent (least effort; do it for them when the next input is obvious; confirm when it is irreversible, money, or a guess). Apply `design:first-glance`: show only what every user needs at first glance; put extra actions and advanced settings one level down (overflow, popover, accordion). Apply `design:no-obvious`: do not caption an empty list ("No API key"); the create action is the message. Apply `design:ui-copy`: words fit the surface (landing hooks and sells; docs explain and stay clear; app UI names the action). Apply `design:spoken-locale`: user-visible words in a language are what speakers call that job, not a word-for-word swap (not "Background remover" to "Suppresseur de fond"). Do not ship filler that could sit on any other product. `/review` stays Standards and Spec. There is no `/design-review` skill and no Design axis.

